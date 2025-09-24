"""
streamlit_components.py
=======================
URL クエリ（`st.query_params`）と **常時同期** できる Streamlit 入力部品集（シンプル版）。

方針
----
- **`key` = `qp_key`**：URLキーはウィジェット `key` を**そのまま**使う
  - URLに使えない文字（`:` や空白など）は **サニタイズ**（`[^a-zA-Z0-9_-]` → `_`、連続/端の `_` を整理）
  - そのため **通常は qp_key を渡す必要なし**（引数は残すが任意）
- **フォーム対応**：`sync="auto"`（既定）
  - フォーム外：on_change で **即時URL更新**（= rerun あり）
  - `with defer_mode():` 内：**差分だけバッファ**に記録 → `apply_deferred_qp_updates()` で一括反映
- **空値の扱い**（一貫ポリシー）
  - 文字列：空文字は URL キー削除
  - 配列   ：空配列は URL キー削除
  - チェック：OFF は URL キー削除 / ON は "1"
  - 数値/日付：常に値を持つ（削除しない）

モジュール例（フォームまとめ反映）
--------------------------------
```python
import streamlit as st
from datetime import date, timedelta
from streamlit_form import defer_mode, apply_deferred_qp_updates
from streamlit_components import input_text_url

today = date.today()
default_start = today - timedelta(days=30)

with st.form("search"):
    with defer_mode():  # ← on_change を抑止し、差分だけ内部バッファに貯める
        q = input_text_url("キーワード", key="q")
    submitted = st.form_submit_button("検索")

if submitted:
    if apply_deferred_qp_updates():  # ← 差分だけURLへ一括反映（空は削除）
        st.rerun()

st.write("URL:", dict(st.query_params))
```

依存
----
- `streamlit_form`（任意。無い場合でも安全フォールバックで動作）
  - `in_defer_mode()`
  - `buffer_put_if_changed(key, init_str, new_str, delete_if_empty=False)`
  - `apply_deferred_qp_updates()`（フォーム送信時にアプリ側で呼ぶ）
- `streamlit_query_params_access`（同一フォルダ）
  - `qp_get_* / qp_set_*` 群
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import List, Optional, Dict
import re

import streamlit as st

# ---------------------------------------------------------------------
# フォーム遅延モードとの連携（存在しなければフォールバック）
# ---------------------------------------------------------------------
try:
    from .streamlit_form import in_defer_mode, buffer_put_if_changed, clear_deferred_query_params_updates
except Exception:  # pragma: no cover
    def in_defer_mode() -> bool:
        return False
    def buffer_put_if_changed(key: str, init_str: str, new_str: str, *, delete_if_empty: bool = False) -> None:
        return

# ---------------------------------------------------------------------
# URL アクセス関数
# ---------------------------------------------------------------------
from .streamlit_query_params_access import (
    qp_get_list, qp_get_int, qp_get_float, qp_get_bool, qp_get_date,
    qp_set_int, qp_set_float, qp_set_bool, qp_set_list, qp_set_date,
    qp_get_str, qp_set_str,
)

# ---------------------------------------------------------------------
# 内部ユーティリティ
# ---------------------------------------------------------------------
def _onchange(sync: str | bool, cb):
    """
    sync: "auto" | True | False
    - "auto": defer_mode 中は on_change なし（= 遅延）、それ以外は on_change=cb

    Examples
    --------
    ```python
    # フォーム外（即時反映）
    v = st.text_input("q", key="q", on_change=_onchange("auto", sync_func))

    # フォーム内（遅延） -> defer_mode() コンテキスト下では on_change は None になる
    with defer_mode():
        v = st.text_input("q", key="q", on_change=_onchange("auto", sync_func))
    ```
    """
    if sync == "auto":
        sync = not in_defer_mode()
    return cb if sync else None

def _sanitize_qp_key(widget_key: str) -> str:
    """
    `key` をそのまま URL キーとして使えるようにサニタイズ。
    - 許容: [a-zA-Z0-9_-]
    - その他は `_` に
    - 連続アンダースコアを1つに、先頭末尾の `_` を除去

    Examples
    --------
    ```python
    _sanitize_qp_key("main:filters:sort")  # -> "main_filters_sort"
    _sanitize_qp_key("  score  ")          # -> "score"
    ```
    """
    s = re.sub(r"[^a-zA-Z0-9_-]", "_", widget_key)
    s = re.sub(r"_+", "_", s).strip("_")
    return s or "x"  # 万一空になった場合の保険

def _qp_from_key(widget_key: str, qp_key: Optional[str]) -> str:
    """
    外部から qp_key を渡されたらそれを優先。無ければ `key` をサニタイズして使う。

    Examples
    --------
    ```python
    _qp_from_key("sort_radio", None)          # -> "sort_radio"
    _qp_from_key("main:date_start", None)     # -> "main_date_start"
    _qp_from_key("price_min", "pmin")         # -> "pmin"
    ```
    """
    return _sanitize_qp_key(qp_key) if qp_key else _sanitize_qp_key(widget_key)

def _ser_list(xs: List[str]) -> str:
    """
    URLに載せるCSV（可読優先）。必要に応じて quote 版に差し替え可能。

    Examples
    --------
    ```python
    _ser_list(["Books", "Tech"])  # -> "Books,Tech"
    ```
    """
    return ",".join(xs)

def _qp_delete(k: str) -> None:
    """
    URL からキーを安全に削除（存在しなくてもエラーにしない）。

    Examples
    --------
    ```python
    _qp_delete("q")  # st.query_params から "q" を除去
    ```
    """
    try:
        del st.query_params[k]
    except Exception:
        st.query_params.pop(k, None)

# ---------------------------------------------------------------------
# dataclass（汎用）
# ---------------------------------------------------------------------
@dataclass
class NumberRange:
    """数値レンジ（low <= high を期待）"""
    low: float
    high: float

@dataclass
class DateRange:
    """日付レンジ（start <= end を期待）"""
    start: date
    end: date

# =====================================================================
# 汎用入力部品（qp_key は任意。未指定で OK）
# =====================================================================
def input_multiselect_url(
    label: str,
    options: List[str],
    key: str,
    qp_key: Optional[str] = None,
    *,
    sync: str | bool = "auto",
    scrub_invalid: bool = True,   # ← 追加: options外のURL値を描画時に掃除
) -> List[str]:
    """
    マルチセレクト。URL は CSV（`A,B,C`）。
    - 空配列 → URL キー削除

    Parameters
    ----------
    label : str
        ラベル文字列
    options : list[str]
        選択肢
    key : str
        ウィジェット key（= 基本は URL キーとしても使用）
    qp_key : str | None
        URLキーを明示したい場合のみ指定（通常は不要）
    sync : "auto" | True | False
        on_change 同期モード

    Returns
    -------
    list[str]

    Examples
    --------
    ```python
    # 即時反映
    cats = input_multiselect_url("カテゴリー", ["All","Books","Tech"], key="cat")

    # フォームまとめ反映
    with st.form("f"):
        with defer_mode():
            cats = input_multiselect_url("カテゴリー", ["All","Books"], key="cat")
        if st.form_submit_button("反映"):
            if apply_deferred_qp_updates(): st.rerun()

    # URLキーを明示したい（通常不要）
    cats2 = input_multiselect_url("カテゴリー", ["All","Books"], key="cat2", qp_key="category")
    ```
    - 空配列 → URL キー削除
    """
    qk = _qp_from_key(key, qp_key)

    # --- 追加：描画前スクラブ（URLの無効トークンを除去） ---
    raw = qp_get_list(qk)
    filtered = [x for x in raw if x in options]
    if scrub_invalid and raw != filtered:
        if in_defer_mode():
            # フォーム中は差分だけ記録（空なら削除）
            buffer_put_if_changed(qk, _ser_list(raw), _ser_list(filtered), delete_if_empty=(len(filtered) == 0))
        else:
            # 即時モードはその場で修正/削除
            if filtered:
                qp_set_list(qk, filtered)
            else:
                _qp_delete(qk)
    init = filtered  # ← フィルタ済みを初期値に

    def _sync():
        v = st.session_state[key]
        if not v:
            _qp_delete(qk)
        else:
            qp_set_list(qk, v)

    selected = st.multiselect(label, options, default=init, key=key, on_change=_onchange(sync, _sync))
    buffer_put_if_changed(qk, _ser_list(init), _ser_list(selected), delete_if_empty=True)
    return selected


def input_text_url(
    label: str,
    key: str,
    qp_key: Optional[str] = None,
    default: str = "",
    placeholder: Optional[str] = None,
    *,
    multiline: bool = False,
    max_chars: Optional[int] = None,
    height: Optional[int] = None,
    sync: str | bool = "auto",
) -> str:
    """
    テキスト（単行/複数行）。空文字は URL キー削除。

    Parameters
    ----------
    label : str
    key : str
    qp_key : str | None
    default : str
    placeholder : str | None
    multiline : bool
        True で複数行（`st.text_area`）
    max_chars : int | None
    height : int | None
    sync : "auto" | True | False

    Returns
    -------
    str

    Examples
    --------
    ```python
    q = input_text_url("キーワード", key="q", placeholder="例）iPhone ケース")
    memo = input_text_url("メモ", key="notes", multiline=True, height=120)

    # URLキーだけ別名にしたい
    q2 = input_text_url("キーワード(別名)", key="q_alt", qp_key="query")
    ```
    """
    qk = _qp_from_key(key, qp_key)
    init = qp_get_str(qk, default)

    def _sync():
        v = str(st.session_state[key])
        if v == "":
            _qp_delete(qk)
        else:
            qp_set_str(qk, v)

    if multiline:
        val = st.text_area(label, value=init, key=key, on_change=_onchange(sync, _sync),
                           placeholder=placeholder, height=height, max_chars=max_chars)
    else:
        val = st.text_input(label, value=init, key=key, on_change=_onchange(sync, _sync),
                            placeholder=placeholder, max_chars=max_chars)

    buffer_put_if_changed(qk, init, str(val), delete_if_empty=True)
    return str(val)


def input_checkbox_url(
    label: str,
    key: str,
    qp_key: Optional[str] = None,
    default: bool = False,
    *,
    sync: str | bool = "auto",
) -> bool:
    """
    チェックボックス。ON は "1"、OFF は **URL キー削除**。

    Parameters
    ----------
    label : str
    key : str
    qp_key : str | None
    default : bool
    sync : "auto" | True | False

    Returns
    -------
    bool

    Examples
    --------
    ```python
    sale = input_checkbox_url("セール品のみ", key="only_sale")

    # 既定 True
    active = input_checkbox_url("有効", key="active", default=True)
    ```
    """
    qk = _qp_from_key(key, qp_key)
    init = qp_get_bool(qk, default)

    def _sync():
        v = bool(st.session_state[key])
        if v:
            qp_set_bool(qk, True)
        else:
            _qp_delete(qk)

    val = st.checkbox(label, value=init, key=key, on_change=_onchange(sync, _sync))
    buffer_put_if_changed(qk, "1" if init else "", "1" if val else "", delete_if_empty=True)
    return bool(val)


def input_number_url(
    label: str,
    key: str,
    qp_key: Optional[str] = None,
    default: float = 0,
    min_value: Optional[float] = None,
    step: Optional[float] = None,
    as_float: bool = False,
    *,
    sync: str | bool = "auto",
) -> float:
    """
    数値（単体）。`as_float=False` で int として扱う。

    Parameters
    ----------
    label : str
    key : str
    qp_key : str | None
    default : float
    min_value : float | None
    step : float | None
    as_float : bool
    sync : "auto" | True | False

    Returns
    -------
    float  # intモードでも float で返す（必要なら呼び出し側で int() に）

    Examples
    --------
    ```python
    n = input_number_url("件数", key="limit", default=10, min_value=0, step=1)
    th = input_number_url("しきい値", key="th", default=0.5, as_float=True, step=0.1)
    ```
    """
    qk = _qp_from_key(key, qp_key)
    init = qp_get_float(qk, float(default)) if as_float else float(qp_get_int(qk, int(default)))

    def _sync():
        v = float(st.session_state[key])
        (qp_set_float if as_float else qp_set_int)(qk, v if as_float else int(v))

    val = st.number_input(
        label,
        value=init if as_float else int(init),
        min_value=min_value if as_float else (int(min_value) if min_value is not None else None),
        step=step if as_float else (int(step) if step is not None else 1),
        key=key, on_change=_onchange(sync, _sync),
    )

    init_str = f"{float(init)}" if as_float else f"{int(init)}"
    new_str  = f"{float(val)}"  if as_float else f"{int(val)}"
    buffer_put_if_changed(qk, init_str, new_str, delete_if_empty=False)
    return float(val) if as_float else float(int(val))


def input_number_range_url(
    label: str,
    key_low: str, key_high: str,
    qp_low: Optional[str] = None, qp_high: Optional[str] = None,
    default_low: float = 0,
    default_high: float = 100,
    as_float: bool = False,
    min_value: Optional[float] = None,
    step: Optional[float] = None,
    *,
    sync: str | bool = "auto",
) -> NumberRange:
    """
    数値レンジ（2つの number_input）。
    - `key_low`, `key_high` をそのまま URL キーに（必要なら qp_* で上書き可能）

    Parameters
    ----------
    label : str
    key_low, key_high : str
    qp_low, qp_high : str | None
    default_low, default_high : float
    as_float : bool
    min_value : float | None
    step : float | None
    sync : "auto" | True | False

    Returns
    -------
    NumberRange

    Examples
    --------
    ```python
    price = input_number_range_url("価格", key_low="price_min", key_high="price_max",
                                   default_low=0, default_high=100, min_value=0, step=1)

    # float レンジ
    rng = input_number_range_url("スコア範囲", key_low="score_min", key_high="score_max",
                                 as_float=True, default_low=0.1, default_high=0.9, step=0.1)
    ```
    """
    ql = _qp_from_key(key_low,  qp_low)
    qh = _qp_from_key(key_high, qp_high)

    low0  = qp_get_float(ql,  float(default_low))  if as_float else float(qp_get_int(ql,  int(default_low)))
    high0 = qp_get_float(qh, float(default_high))  if as_float else float(qp_get_int(qh, int(default_high)))

    _min  = min_value if as_float else (int(min_value) if min_value is not None else None)
    _step = step if as_float else (int(step) if step is not None else 1)

    def _sync_low():
        v = float(st.session_state[key_low]);  (qp_set_float if as_float else qp_set_int)(ql, v if as_float else int(v))
    def _sync_high():
        v = float(st.session_state[key_high]); (qp_set_float if as_float else qp_set_int)(qh, v if as_float else int(v))

    c1, c2 = st.columns(2)
    with c1:
        vlow = st.number_input(f"{label}（下限）", value=low0 if as_float else int(low0),
                               min_value=_min, step=_step, key=key_low,  on_change=_onchange(sync, _sync_low))
    with c2:
        vhigh= st.number_input(f"{label}（上限）", value=high0 if as_float else int(high0),
                               min_value=_min, step=_step, key=key_high, on_change=_onchange(sync, _sync_high))

    buffer_put_if_changed(ql, f"{float(low0)}"  if as_float else f"{int(low0)}",  f"{float(vlow)}"  if as_float else f"{int(vlow)}",  delete_if_empty=False)
    buffer_put_if_changed(qh, f"{float(high0)}" if as_float else f"{int(high0)}", f"{float(vhigh)}" if as_float else f"{int(vhigh)}", delete_if_empty=False)

    return NumberRange(low=float(vlow) if as_float else float(int(vlow)),
                       high=float(vhigh) if as_float else float(int(vhigh)))


def input_date_url(
    label: str,
    key: str,
    qp_key: Optional[str] = None,
    default: Optional[date] = None,  # ← Optional に
    *,
    sync: str | bool = "auto",
) -> date:
    """
    単一日付。`default=None` で未指定初期化（URLにキーが無ければ today を表示するが保存しない）。
    """
    qk = _qp_from_key(key, qp_key)
    raw_before = st.query_params.get(qk)  # None or "YYYY-MM-DD"
    today = date.today()

    if raw_before is not None:
        d0 = qp_get_date(qk, today) or today
    else:
        d0 = default or today

    def _sync():
        qp_set_date(qk, st.session_state[key])

    val = st.date_input(label, value=d0, key=key, on_change=_onchange(sync, _sync), format="YYYY-MM-DD")

    # URLの生値（空文字）基準で差分
    buffer_put_if_changed(qk, raw_before or "", val.isoformat(), delete_if_empty=False)
    return val


def input_daterange_url(
    label: str,
    key: str,
    qp_start: Optional[str] = None, qp_end: Optional[str] = None,
    default_start: date = date.today(), default_end: date = date.today(),
    *,
    sync: str | bool = "auto",
) -> DateRange:
    """
    date_input（範囲モード）。**両端が揃った時のみ** URL を更新。
    - URL キーは `key+"_start"` / `key+"_end"` をサニタイズしたもの（任意で qp_* 上書き）

    Parameters
    ----------
    label : str
    key : str
    qp_start, qp_end : str | None
    default_start, default_end : date
    sync : "auto" | True | False

    Returns
    -------
    DateRange

    Examples
    --------
    ```python
    period = input_daterange_url("期間", key="date",
                                 default_start=date(2025,1,1), default_end=date(2025,1,31))
    # URL: ?date_start=2025-01-01&date_end=2025-01-31
    ```
    """
    base = _sanitize_qp_key(key)
    qs = _sanitize_qp_key(qp_start) if qp_start else f"{base}_start"
    qe = _sanitize_qp_key(qp_end)   if qp_end   else f"{base}_end"

    s0 = qp_get_date(qs, default_start) or default_start
    e0 = qp_get_date(qe, default_end)   or default_end

    def _sync():
        rng = st.session_state[key]
        if isinstance(rng, tuple) and len(rng) == 2:
            s, e = rng
            qp_set_date(qs, s); qp_set_date(qe, e)

    rng = st.date_input(label, value=(s0, e0), key=key, on_change=_onchange(sync, _sync), format="YYYY-MM-DD")
    s, e = (rng if isinstance(rng, tuple) else (s0, e0))

    buffer_put_if_changed(qs, s0.isoformat(), s.isoformat(), delete_if_empty=False)
    buffer_put_if_changed(qe, e0.isoformat(), e.isoformat(), delete_if_empty=False)
    return DateRange(start=s, end=e)


def input_daterange_two_url(
    *,
    label_start: str,
    label_end: str,
    key_start: str, key_end: str,
    qp_start: Optional[str] = None, qp_end: Optional[str] = None,
    default_start: Optional[date] = None,  # ← Optional に
    default_end: Optional[date] = None,    # ← Optional に
    sync: str | bool = "auto",
) -> DateRange:
    """
    期間を「開始日」「終了日」の **2つの date_input** で構成。
    - 片方だけ変えても即時にその片側の URL を更新（フォーム内は差分記録）
    - URL キーはそれぞれ `key_*` をサニタイズ（任意で qp_* 上書き）
    - `default_start` / `default_end` に None を渡すと「未指定初期化」を表し、
      URL キーが無い場合はウィジェット表示のみプレースホルダー日付（today）で埋める。
      （※ その状態では URL には何も書かれない）

    Parameters
    ----------
    label_start, label_end : str
    key_start, key_end : str
    qp_start, qp_end : str | None
    default_start, default_end : date | None
        None の場合は「未指定初期化」。URL にキーが無い場合でも、
        ウィジェットにはプレースホルダー（today）を表示するが URL は更新しない。
    sync : "auto" | True | False

    Returns
    -------
    DateRange
        ※ 戻り値は `date` 固定（None は返さない）。未指定の概念は「URLにキーが無い」で表現する。
          必要なら呼び出し側で `qs in st.query_params` を確認してください。

    Examples
    --------
    ```python
    # 未指定初期化（URLに date_start/end が無ければ today を見せるだけで保存しない）
    period = input_daterange_two_url(
        label_start="開始日", label_end="終了日",
        key_start="date_start", key_end="date_end",
        default_start=None, default_end=None,
    )

    # 既定を与える（URLが無ければこの初期値を表示し、変更時のみURL反映）
    period2 = input_daterange_two_url(
        label_start="開始日", label_end="終了日",
        key_start="date_start", key_end="date_end",
        default_start=date(2025,1,1), default_end=date(2025,1,31),
    )

    # URLキー名だけ別名にしたい
    period3 = input_daterange_two_url(
        label_start="開始日", label_end="終了日",
        key_start="date_from", key_end="date_to",
        qp_start="from", qp_end="to",
        default_start=None, default_end=None,
    )
    ```
    """
    qs = _qp_from_key(key_start, qp_start)
    qe = _qp_from_key(key_end,   qp_end)

    # --- URLに元値があるかどうか（未指定の検出は URL キー有無で判断） ---
    raw_s_before = st.query_params.get(qs)  # None or "YYYY-MM-DD"
    raw_e_before = st.query_params.get(qe)

    # --- ウィジェットの表示値（プレースホルダーを含む） ---
    # URL に値があるならそれを優先。無ければ default_*、それも無ければ today を表示用に使う。
    today = date.today()
    if raw_s_before is not None:
        s0 = qp_get_date(qs, today) or today
    else:
        s0 = default_start or today

    if raw_e_before is not None:
        e0 = qp_get_date(qe, today) or today
    else:
        e0 = default_end or today

    def _sync_start():
        qp_set_date(qs, st.session_state[key_start])

    def _sync_end():
        qp_set_date(qe, st.session_state[key_end])

    c1, c2 = st.columns(2)
    with c1:
        s_val = st.date_input(
            label_start,
            value=s0,
            key=key_start,
            on_change=_onchange(sync, _sync_start),
            format="YYYY-MM-DD",
        )
    with c2:
        e_val = st.date_input(
            label_end,
            value=e0,
            key=key_end,
            on_change=_onchange(sync, _sync_end),
            format="YYYY-MM-DD",
        )

    # --- 差分バッファは「URLの生値」基準で比較（未指定=空文字） ---
    buffer_put_if_changed(qs, raw_s_before or "", s_val.isoformat(), delete_if_empty=False)
    buffer_put_if_changed(qe, raw_e_before or "", e_val.isoformat(), delete_if_empty=False)

    return DateRange(start=s_val, end=e_val)


# def input_radio_url(
#     label: str,
#     options: List[str],
#     key: str,
#     qp_key: Optional[str] = None,
#     index_default: int = 0,
#     *,
#     horizontal: bool = False,
#     sync: str | bool = "auto",
#     scrub_invalid: bool = True,   # ← 追加：URLの無効値を描画時に掃除
# ) -> str:
#     """
#     ラジオ（必ず1つ選ぶ → 空は存在しない）。

#     Parameters
#     ----------
#     label : str
#     options : list[str]
#     key : str
#     qp_key : str | None
#     index_default : int
#     horizontal : bool
#     sync : "auto" | True | False

#     Returns
#     -------
#     str

#     Examples
#     --------
#     ```python
#     sort = input_radio_url("並び順", ["関連度","価格の安い順","価格の高い順"], key="sort_radio", horizontal=True)
#     ```
#     ラジオ（必ず1つ選ぶ → 空は存在しない）。
#     """
#     qk = _qp_from_key(key, qp_key)

#     # --- 追加：描画前スクラブ ---
#     raw_in_url = st.query_params.get(qk)
#     if scrub_invalid and (raw_in_url is not None) and (raw_in_url not in options):
#         if in_defer_mode():
#             buffer_put_if_changed(qk, str(raw_in_url), "", delete_if_empty=True)
#         else:
#             _qp_delete(qk)

#     init_val = qp_get_str(qk, options[index_default] if options else "")
#     idx = options.index(init_val) if init_val in options and options else index_default

#     def _sync(): qp_set_str(qk, st.session_state[key])

#     val = st.radio(label, options, index=idx, key=key, on_change=_onchange(sync, _sync), horizontal=horizontal)
#     buffer_put_if_changed(qk, str(init_val), str(val), delete_if_empty=False)
#     return str(val)
from typing import List, Optional, Callable, Iterable
import streamlit as st

def input_radio_url(
    label: str,
    options: List[str],
    key: str,
    qp_key: Optional[str] = None,
    index_default: int = 0,
    *,
    horizontal: bool = False,
    sync: str | bool = "auto",
    scrub_invalid: bool = True,          # URLの無効値を描画時に掃除
    disabled: Optional[Iterable[str]] = None,  # ← 追加: 無効化する選択肢（値で指定）
    is_enabled: Optional[Callable[[str], bool]] = None,  # ← 追加: 値→有効/無効を返す関数
    disabled_marker: str = "🔘",         # ← 追加: グレー表示の頭に付ける記号（お好みで）
) -> str:
    """
    ラジオ（必ず1つ選ぶ）。無効な選択肢は右横にグレーで「選べない風」に表示。
    URLクエリと双方向同期。

    Parameters
    ----------
    label : str
    options : list[str]              # 表示/値は同一のシンプル想定
    key : str
    qp_key : str | None
    index_default : int
    horizontal : bool
    sync : "auto" | True | False
    scrub_invalid : bool             # URLに無効値が来たら掃除
    disabled : Iterable[str] | None  # 無効にする値の集合
    is_enabled : Callable[[str], bool] | None  # 有効判定の関数（disabledより優先）
    disabled_marker : str

    Returns
    -------
    str
    """
    qk = _qp_from_key(key, qp_key)

    # --- 有効/無効の仕分け ---
    disabled_set = set(disabled or [])
    def _enabled(x: str) -> bool:
        if is_enabled is not None:
            return bool(is_enabled(x))
        return x not in disabled_set

    enabled_options = [x for x in options if _enabled(x)]
    disabled_options = [x for x in options if not _enabled(x)]

    # --- 追加：描画前スクラブ（存在しない or 無効値は消す） ---
    raw_in_url = st.query_params.get(qk)
    if scrub_invalid and (raw_in_url is not None):
        if (raw_in_url not in options) or (raw_in_url in disabled_options):
            if in_defer_mode():
                buffer_put_if_changed(qk, str(raw_in_url), "", delete_if_empty=True)
            else:
                _qp_delete(qk)
            raw_in_url = None  # 後段の初期化で考慮

    # --- 初期値の決定（URL or デフォルト）。デフォルトが無効なら先頭の有効にフォールバック ---
    if not enabled_options:
        # すべて無効の場合：グレーのみ表示して空文字を返す
        st.write(label)
        if disabled_options:
            dummy_html = "　".join(
                f"<span style='color:gray;'>{disabled_marker} {lbl}</span>" for lbl in disabled_options
            )
            st.markdown(f"<div style='margin: 0.4em 0 0.8em 0;'>{dummy_html}</div>", unsafe_allow_html=True)
        st.warning("現在選択可能な項目がありません。")
        return ""

    init_val = qp_get_str(qk, options[index_default] if options else "")
    if (init_val not in enabled_options):
        # URLの値が無効/存在しない/無効化された場合は、index_defaultを有効側に合わせる
        fallback = options[index_default] if 0 <= index_default < len(options) else enabled_options[0]
        init_val = fallback if fallback in enabled_options else enabled_options[0]

    idx = enabled_options.index(init_val)

    # --- レイアウト：有効ラジオ + 無効グレー ---
    # 横幅は「ラベル長の合計」でざっくり配分（簡便な幅合わせ）
    len_enabled = sum(len(s) for s in enabled_options) or 1
    len_disabled = sum(len(s) for s in disabled_options) or 1
    col1, col2 = st.columns([len_enabled, len_disabled])

    def _sync():
        qp_set_str(qk, st.session_state[key])

    with col1:
        val = st.radio(
            label,
            enabled_options,
            index=idx,
            key=key,
            on_change=_onchange(sync, _sync),
            horizontal=horizontal,
        )

    with col2:
        if disabled_options:
            dummy_html = "　".join(
                f"<span style='color:gray;'>{disabled_marker} {lbl}</span>" for lbl in disabled_options
            )
            # ラベル行とだいたい高さを合わせる
            st.markdown(
                f"<div style='margin-top: 2.1em; font-size: 0.95em;'>{dummy_html}</div>",
                unsafe_allow_html=True
            )

    # 最後に差分があればバッファへ
    buffer_put_if_changed(qk, str(init_val), str(val), delete_if_empty=False)
    return str(val)



def input_selectbox_url(
    label: str,
    options: List[str],
    key: str,
    qp_key: Optional[str] = None,
    index_default: int = 0,
    *,
    sync: str | bool = "auto",
    scrub_invalid: bool = True,   # ← 追加：URLの無効値を描画時に掃除
    empty_deletes: bool = True,   # ← 追加：'' を選んだら URL キー削除
) -> str:
    """
    selectbox（必ず1つ選ぶ → 空は存在しない）。

    Parameters
    ----------
    label : str
    options : list[str]
    key : str
    qp_key : str | None
    index_default : int
    sync : "auto" | True | False

    Returns
    -------
    str

    Examples
    --------
    ```python
    sort_sel = input_selectbox_url("並び順（セレクト）", ["関連度","価格の安い順","価格の高い順","新着順"], key="sort_select")
    ```
    selectbox（必ず1つ選ぶ → 空は存在しない）。
    """
    qk = _qp_from_key(key, qp_key)

    # --- 追加：描画前スクラブ（optionsに無いURL値を消す） ---
    raw_in_url = st.query_params.get(qk)
    if scrub_invalid and (raw_in_url is not None) and (raw_in_url not in options):
        if in_defer_mode():
            buffer_put_if_changed(qk, str(raw_in_url), "", delete_if_empty=True)
        else:
            _qp_delete(qk)

    init_val = qp_get_str(qk, options[index_default] if options else "")
    idx = options.index(init_val) if options and (init_val in options) else index_default

    def _sync():
        v = st.session_state[key]
        if empty_deletes and (v == "" or v is None):
            _qp_delete(qk)
        else:
            qp_set_str(qk, v)

    val = st.selectbox(label, options, index=idx, key=key, on_change=_onchange(sync, _sync))
    new_for_buf = "" if (empty_deletes and (val == "" or val is None)) else str(val)
    buffer_put_if_changed(qk, str(init_val), new_for_buf, delete_if_empty=empty_deletes)
    return str(val)



def input_slider_url(
    label: str,
    key: str,
    qp_key: Optional[str] = None,
    *,
    min_value: float,
    max_value: float,
    default: float,
    step: Optional[float] = None,
    as_float: bool = False,
    sync: str | bool = "auto",
) -> float:
    """
    数値スライダ（単値）。int/float を切替可。

    Parameters
    ----------
    label : str
    key : str
    qp_key : str | None
    min_value, max_value : float
    default : float
    step : float | None
    as_float : bool
    sync : "auto" | True | False

    Returns
    -------
    float

    Examples
    --------
    ```python
    score = input_slider_url("スコア", key="score", min_value=0, max_value=100, default=50, step=1)
    ratio = input_slider_url("比率", key="ratio", min_value=0.0, max_value=1.0, default=0.5, step=0.05, as_float=True)
    ```
    """
    qk = _qp_from_key(key, qp_key)
    init = qp_get_float(qk, float(default)) if as_float else float(qp_get_int(qk, int(default)))

    def _sync():
        v = float(st.session_state[key])
        (qp_set_float if as_float else qp_set_int)(qk, v if as_float else int(v))

    _min = min_value if as_float else int(min_value)
    _max = max_value if as_float else int(max_value)
    _val = init if as_float else int(init)
    _step = step if as_float else (int(step) if step is not None else 1)

    val = st.slider(label, min_value=_min, max_value=_max, value=_val, step=_step, key=key, on_change=_onchange(sync, _sync))

    init_str = f"{float(init)}" if as_float else f"{int(init)}"
    new_str  = f"{float(val)}"  if as_float else f"{int(val)}"
    buffer_put_if_changed(qk, init_str, new_str, delete_if_empty=False)
    return float(val) if as_float else float(int(val))


def input_slider_range_url(
    label: str,
    key: str,
    qp_low: Optional[str] = None, qp_high: Optional[str] = None,
    *,
    min_value: float,
    max_value: float,
    default_low: float,
    default_high: float,
    step: Optional[float] = None,
    as_float: bool = False,
    sync: str | bool = "auto",
) -> NumberRange:
    """
    数値レンジスライダ（下限/上限の2値）。
    - URL キーは `key+"_low"`, `key+"_high"` をサニタイズ（任意で qp_* 上書き）

    Parameters
    ----------
    label : str
    key : str
    qp_low, qp_high : str | None
    min_value, max_value : float
    default_low, default_high : float
    step : float | None
    as_float : bool
    sync : "auto" | True | False

    Returns
    -------
    NumberRange

    Examples
    --------
    ```python
    budget = input_slider_range_url("予算", key="budget", min_value=0, max_value=1000,
                                    default_low=100, default_high=500, step=10)

    score_rng = input_slider_range_url("スコア範囲", key="score_rng", min_value=0.0, max_value=1.0,
                                       default_low=0.1, default_high=0.9, step=0.1, as_float=True)
    ```
    """
    base = _sanitize_qp_key(key)
    ql = _sanitize_qp_key(qp_low)  if qp_low  else f"{base}_low"
    qh = _sanitize_qp_key(qp_high) if qp_high else f"{base}_high"

    low0  = qp_get_float(ql,  float(default_low))  if as_float else float(qp_get_int(ql,  int(default_low)))
    high0 = qp_get_float(qh, float(default_high))  if as_float else float(qp_get_int(qh, int(default_high)))

    def _sync():
        lo, hi = st.session_state[key]
        if as_float:
            qp_set_float(ql,  float(lo)); qp_set_float(qh, float(hi))
        else:
            qp_set_int(ql,  int(lo));     qp_set_int(qh, int(hi))

    _min = min_value if as_float else int(min_value)
    _max = max_value if as_float else int(max_value)
    _val = (low0 if as_float else int(low0), high0 if as_float else int(high0))
    _step= step if as_float else (int(step) if step is not None else 1)

    lo, hi = st.slider(label, min_value=_min, max_value=_max, value=_val, step=_step, key=key, on_change=_onchange(sync, _sync))

    buffer_put_if_changed(ql, f"{float(low0)}"  if as_float else f"{int(low0)}",  f"{float(lo)}"  if as_float else f"{int(lo)}",  delete_if_empty=False)
    buffer_put_if_changed(qh, f"{float(high0)}" if as_float else f"{int(high0)}", f"{float(hi)}" if as_float else f"{int(hi)}", delete_if_empty=False)

    return NumberRange(low=float(lo) if as_float else float(int(lo)),
                       high=float(hi) if as_float else float(int(hi)))


def input_recent_window_url(
    *,
    label: str = "表示ウィンドウ",
    key: str,
    qp_key: Optional[str] = None,
    options: Optional[List[str]] = None,   # 例: ["1w","3mo","1y","all"]
    default: str = "1w",
    labels: Optional[Dict[str, str]] = None,  # 表示名マップ {"1w":"直近1週間", ...}
    horizontal: bool = True,
    sync: str | bool = "auto",
) -> str:
    """
    「直近どれだけに絞るか」を選ぶ部品（データ非依存）。
    - URL は token（"1w","3mo","1y","all"）

    Parameters
    ----------
    label : str
    key : str
    qp_key : str | None
    options : list[str] | None
    default : str
    labels : dict[str,str] | None
    horizontal : bool
    sync : "auto" | True | False

    Returns
    -------
    str
        選択トークン（"1w" / "3mo" / "1y" / "all"）

    Examples
    --------
    ```python
    win = input_recent_window_url(
        key="recent",
        labels={"1w":"直近1週間","3mo":"直近3ヶ月","1y":"直近1年","all":"全期間"},
        default="1w",
    )
    ```
    """
    qk = _qp_from_key(key, qp_key)
    opts = options or ["1w", "3mo", "1y", "all"]

    init = qp_get_str(qk, default if default in opts else opts[0])
    if init not in opts:
        init = opts[0]
    idx = opts.index(init)

    def _sync(): qp_set_str(qk, st.session_state[key])

    fmt = (lambda t: labels.get(t, t)) if labels else None
    val = st.radio(label, options=opts, index=idx, key=key, on_change=_onchange(sync, _sync),
                   horizontal=horizontal, format_func=fmt)
    buffer_put_if_changed(qk, init, val, delete_if_empty=False)
    return val


def form_submit_button_clear_input():
    resetted = st.form_submit_button('クリア')
    if resetted:
        clear_deferred_query_params_updates()
        st.rerun()

def button_clear_input(label: str = 'clear'):
    resetted = st.button(label)
    if resetted:
        clear_deferred_query_params_updates()
        st.rerun()


def input_radio_disabled_url(
    label: str,
    *,
    key: str,                       # 論理名（state/URLの基準）
    options: List[str],             # 値トークン（順序固定）
    default: str,
    qp_key: Optional[str] = None,
    labels: Optional[Dict[str, str]] = None,   # {value: label}
    disabled: Optional[Iterable[str]] = None,
    is_enabled: Optional[Callable[[str], bool]] = None,
    horizontal: bool = True,
    sync: str | bool = "auto",  # 互換のため残すが、この実装では使わない
) -> tuple[str, bool, str]:
    """
    無効選択肢をグレー表示できるラジオ（URLと双方向同期・“選択は絶対に維持”の完全制御版）。

    仕様
    ----
    - options は **値トークンの配列**。順序・内容は再実行でも不変にすること。
    - 表示は `labels` で差し替え。無効値は `:gray[...]` でトーンダウン表示（選択は可能）。
    - 選択はこの関数が **完全制御**：内部ウィジェットの state に依存しない。
      - 毎フレーム、URL/セッションの“真実の値”から **index を算出して描画**。
      - 返ってきた選択で“真実の値”を更新し、URLに反映。
    - **フォールバックや自動差し替えは一切しない**。無効を選んだら `ok=False` を返すだけ。

    戻り値
    ------
    (value, ok, label)
      value : 選ばれた値（options のトークン）
      ok    : その値が現在「有効」かどうか
      label : 表示ラベル（labels が無ければ value と同じ）

    使い方
    ------
    >>> val, ok, lbl = input_radio_disabled_url(
    ...     "粒度", key="dt_unit",
    ...     options=["1d","1h","15m","1m","15s"],
    ...     default="1d",
    ...     labels={"1d":"1日(10年まで)", "1h":"1時間(半年まで)", "15m":"15分(45日まで)", "1m":"1分(3日まで)", "15s":"15秒(1日まで)"},
    ...     disabled={"1h","15m"},   # 例：今は使えない
    ... )
    >>> if not ok:
    ...     st.error(f"「{lbl}」はこの期間では使えません。")  # ここでだけ通知する運用
    """
    vals = list(options)
    lab  = labels or {}
    disp = lambda v: lab.get(v, v)
    qk   = _qp_from_key(key, qp_key)

    disabled_set = set(disabled or [])
    def _is_enabled(v: str) -> bool:
        return bool(is_enabled(v)) if is_enabled is not None else (v not in disabled_set)

    state_key   = f"{key}__value"      # 真実の値（"1d"など）
    widget_key  = f"{key}__radio"      # ラジオ自身のキー（内部UI用）

    # 初期化：URL優先→default→先頭
    if state_key not in st.session_state:
        init = qp_get_str(qk, default if default in vals else (vals[0] if vals else ""))
        if init not in vals and vals:
            init = vals[0]
        st.session_state[state_key] = init

    current_value = st.session_state[state_key]
    if current_value not in vals and vals:
        current_value = vals[0]
        st.session_state[state_key] = current_value

    current_index = vals.index(current_value)

    # 表示フォーマッタ（無効はグレー）
    def _fmt(v: str) -> str:
        s = disp(v)
        return s if _is_enabled(v) else f":gray[{s}]"

    # 変更時の同期（ここでのみURL更新＆rerun）
    def _on_change():
        chosen = st.session_state.get(widget_key, current_value)
        if chosen != st.session_state[state_key]:
            st.session_state[state_key] = chosen
            # URLを即時更新（フォーム遅延モードなら差分記録に切り替えたければここを調整）
            if in_defer_mode():
                raw = st.query_params.get(qk) or ""
                buffer_put_if_changed(qk, str(raw), str(chosen), delete_if_empty=False)
            else:
                qp_set_str(qk, chosen)
            # st.rerun()

    # ラジオ描画：indexは毎回こちらで指定、widget_keyはUI専用
    st.radio(
        label,
        options=vals,
        index=current_index,
        format_func=_fmt,
        horizontal=horizontal,
        key=widget_key,
        on_change=_on_change,   # ← ここで確実に拾う
    )

    # 返却は“真実の値”から
    chosen_value = st.session_state[state_key]
    if in_defer_mode():
        raw = st.query_params.get(qk) or ""
        buffer_put_if_changed(qk, str(raw), str(chosen_value), delete_if_empty=False)
    ok = _is_enabled(chosen_value)
    chosen_label = disp(chosen_value)
    return chosen_value, ok, chosen_label


__all__ = [
    "NumberRange", "DateRange",
    "input_multiselect_url", "input_text_url", "input_checkbox_url",
    "input_number_url", "input_number_range_url",
    "input_date_url", "input_daterange_url", "input_daterange_two_url",
    "input_radio_url", "input_selectbox_url",
    "input_slider_url", "input_slider_range_url",
    "input_recent_window_url",
    'form_submit_button_clear_input', 'button_clear_input', 'input_radio_disabled_url',
]
