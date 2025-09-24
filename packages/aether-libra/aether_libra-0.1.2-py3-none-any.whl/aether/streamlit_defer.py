# streamlit_defer.py
from __future__ import annotations

import functools
import concurrent.futures as cf
import dataclasses
import hashlib
import json
import math
import time
from datetime import date, datetime, time as dtime
from decimal import Decimal
from pathlib import Path
from typing import Any, Callable, Iterable
from uuid import UUID

import streamlit as st

try:
    import numpy as _np  # type: ignore
except Exception:  # numpy が無い環境でも動くように
    _np = None


def placeholder(name: str | None = None) -> st.delta_generator.DeltaGenerator:
    """
    描画用のプレースホルダー（Slot）を作る薄いラッパ。

    Streamlit では 1 回のラン（スクリプト実行）内で `st.empty()` に対して
    後から“上書き”することで **差し替え** を実現します。この関数は
    プレースホルダーの概念を明示化するための薄いラッパです。
    引数 `name` は人間が読んで分かるラベル目的で、型付けや表示位置には関与しません。

    Returns
    -------
    DeltaGenerator
        `st.empty()` と同じ、描画先のプレースホルダー

    Examples
    --------
    >>> import streamlit as st
    >>> from streamlit_defer import placeholder, wait_for
    >>> ph = placeholder("main")                                 # ← プレースホルダーを確保
    >>> ph.write("A only ...")                            # ← まず A を暫定表示
    >>> data = wait_for("load_B", loader=lambda: 123)   # ← 擬似await（未完なら sleep→rerun）
    >>> ph.write(f"A + B = {data}")                       # ← 同じ placeholder に“差し替え”
    """
    return st.empty()


def wait_for(
    loader: Callable[[], Any],
    *,
    depends_on: Any | None = None,
    key: str | None = None,
    poll_sec: float = 5.0,
) -> Any:
    """
    “擬似 await”：重い処理（loader）が完了するまで軽く待機し、完了したら結果を返す。

    Streamlit は 1 リクエスト＝スクリプトの“同期実行”であり、途中で本物の
    `await` による UI 差分更新はできません。本関数は **未完なら少し待って rerun**、
    **完了したら値を返す** という動作で、`async/await` に近い書き味を実現します。

    Parameters
    ----------
    loader : Callable[[], Any]
        バックグラウンドで実行する重い処理。
        **注意：この中で `st.*` を呼ばないこと**（UI API はメインスレッド専用）
    depends_on : Any, optional
        依存条件（dependencies）。これが**変わったら自動的に再 submit** します。
        例：タプル/辞書/データクラス/日付など“状態の要点”を渡してください。
        （内部で正規化→ハッシュ化して比較します）
    key : str, optional
        ジョブを識別する名前。指定しない場合は `loader` から自動生成します。
    poll_sec : float, default 1.0
        未完了時に再試行するまでの待機秒数（`time.sleep` の秒数）

    Returns
    -------
    Any
        `loader` の戻り値。未完了の場合、この関数は `sleep→rerun()` により
        “次のラン”で復帰し、完了時に値を返します。

    Examples
    --------
    1) プレースホルダー（placeholder）を使って “A ⇒ A+B に差し替え” する基本形：

    >>> import streamlit as st
    >>> from streamlit_defer import placeholder, wait_for
    >>>
    >>> ph = placeholder("main")             # 差し替え先
    >>> ph.write("A...")                     # まず A を描画
    >>>
    >>> # B を擬似 await（未完ならこの行で sleep→rerun される）
    >>> dfB = wait_for(
    ...     loader=lambda: load_B(params),
    ...     depends_on=("params", tuple(params)),
    ...     poll_sec=1.0,
    ... )
    >>>
    >>> # 完了したら同じ placeholder に差し替え
    >>> ph.write("A + B ready!")

    2) 複数の重い処理を**同時に開始**しておき、必要な場所で順に結果を受け取る（推奨）：
       先に `start(...)` で並列起動 → 各表示箇所で `wait_for(...)` する。

    >>> from streamlit_defer import placeholder, start, wait_for
    >>>
    >>> ph2 = placeholder("chart_B")
    >>> ph3 = placeholder("chart_C")
    >>>
    >>> # 先に同時スタート（この時点では待たない）
    >>> start(loader=lambda: load_B(paramsB), depends_on=("B", paramsB), key="B")
    >>> start(loader=lambda: load_C(paramsC), depends_on=("C", paramsC), key="C")
    >>>
    >>> # 表示側は、それぞれの箇所で“待って差し替え”
    >>> dfB = wait_for(loader=lambda: load_B(paramsB), depends_on=("B", paramsB), key="B")
    >>> ph2.altair_chart(chart_B(dfB), use_container_width=True)
    >>>
    >>> dfC = wait_for(loader=lambda: load_C(paramsC), depends_on=("C", paramsC), key="C")
    >>> ph3.altair_chart(chart_C(dfC), use_container_width=True)

    Notes
    -----
    - `depends_on` に**巨大な構造体（DataFrame など）**は渡さないでください。
      クエリ条件や ID、期間など“要点だけ”を渡すのがベストプラクティス。
    - `depends_on` を渡さない場合、同じ `key`（自動生成含む）のジョブは**使い回し**ます。
      条件変更で再取得したい場合は `depends_on` にその条件を入れてください。
    """
    # ハッシュ化して、(key, hash) の組を実体キーにする
    dep_hash = _hash_depends(depends_on)
    base_key = _derive_base_key(loader, key)  # ← 自動キー生成
    state_key_future = f"_streamlit_defer_future__{base_key}__{dep_hash}"
    state_key_latest = f"_streamlit_defer_latest__{base_key}"

    # “最新版ハッシュ” を記録。変わったら古い参照は使われなくなる（次回以降自然にGC）。
    st.session_state[state_key_latest] = dep_hash

    # まだ submit していないならここで実行
    if state_key_future not in st.session_state:
        st.session_state[state_key_future] = _executor().submit(loader)

    fut: cf.Future = st.session_state[state_key_future]

    if fut.done():
        exc = fut.exception()
        if exc:
            # 失敗は例外としてそのまま UI に出す（必要なら try/except で握る）
            raise exc
        return fut.result()

    # 未完了：少し待ってから rerun（UI スレッドのみ）
    time.sleep(poll_sec)
    _safe_rerun()
    # ここには戻ってこない（rerun 後の“次のラン”で入口から再実行される）
    raise RuntimeError("unreachable after rerun()")  # 保険


def start(
    loader: Callable[[], Any],
    *,
    depends_on: Any | None = None,
    key: str | None = None,
) -> cf.Future:
    """
    Submit-only（非ブロッキング）で重い処理をバックグラウンド開始する。

    - **待たない／rerunもしない**：単にジョブを`submit`して `Future` を返すだけ。
    - **同一( loader, depends_on, key )に対しては冪等**：二重起動を防ぐ（既に走っていれば同じFutureを返す）。
    - 複数の重いジョブ（例：BとC）を**同時に走らせたい場合**に有効。
      先に `start(...)` を呼んでおき、その後で各表示箇所ごとに `wait_for(...)` で結果を受け取る。

    Parameters
    ----------
    loader : Callable[[], Any]
        バックグラウンドで実行する重い処理。
        **注意：この中で `st.*` を呼ばないこと**（UI API はメインスレッド専用）
    depends_on : Any, optional
        依存条件。これが**変わったら新しいジョブ**として扱い、再submitされる。
        例：タプル/辞書/日付など“状態の要点”を渡す（内部で正規化→ハッシュ化して識別）。
    key : str, optional
        ジョブ識別名。省略時は `loader.__module__ + "." + loader.__qualname__` から**自動生成**。

    Returns
    -------
    concurrent.futures.Future
        `loader` の結果を表す Future。完了済みかどうかは `future.done()` で確認可能。

    Examples
    --------
    2つの重い処理を**同時に開始**しておき、必要な場所で順に `wait_for` で受け取る：

    >>> from streamlit_defer import placeholder, start, wait_for
    >>>
    >>> ph2 = placeholder("chart_B")
    >>> ph3 = placeholder("chart_C")
    >>>
    >>> # 先に“同時スタート”（この時点では待たない）
    >>> start(loader=lambda: load_B(paramsB), depends_on=("B", paramsB), key="B")
    >>> start(loader=lambda: load_C(paramsC), depends_on=("C", paramsC), key="C")
    >>>
    >>> # 表示側はそれぞれの箇所で“結果を待って”差し替える
    >>> dfB = wait_for(loader=lambda: load_B(paramsB), depends_on=("B", paramsB), key="B")
    >>> ph2.altair_chart(chart_B(dfB), use_container_width=True)
    >>>
    >>> dfC = wait_for(loader=lambda: load_C(paramsC), depends_on=("C", paramsC), key="C")
    >>> ph3.altair_chart(chart_C(dfC), use_container_width=True)
    """
    base_key = _derive_base_key(loader, key)
    dep_hash = _hash_depends(depends_on)
    state_key_future = f"_streamlit_defer_future__{base_key}__{dep_hash}"
    if state_key_future not in st.session_state:
        st.session_state[state_key_future] = _executor().submit(loader)
    return st.session_state[state_key_future]


def invalidate(key: str) -> None:
    """
    任意（補助）：特定 `key` のジョブを手動で失効させる。

    通常は `depends_on` の変化で自動的に再 submit されるため呼ぶ必要はありません。
    特別に「同じ depends_on でも強制で取り直したい」ケースのみ使ってください。
    """
    prefix = f"_streamlit_defer_future__{key}__"
    for k in list(st.session_state.keys()):
        if str(k).startswith(prefix):
            st.session_state.pop(k, None)
    st.session_state.pop(f"_streamlit_defer_latest__{key}", None)


# ─────────────────────────────────────────────────────────────
# 内部ユーティリティ
# ─────────────────────────────────────────────────────────────

# ヘルパ：loader から安定キーを導出（partial やラッパでも中身の関数名を使う）
def _derive_base_key(loader: Callable[[], Any], key: str | None) -> str:
    if key:  # ユーザー指定があればそれを尊重
        return key
    fn = loader.func if isinstance(loader, functools.partial) else loader
    mod = getattr(fn, "__module__", "unknown")
    qn = getattr(fn, "__qualname__", getattr(fn, "__name__", "loader"))
    return f"{mod}.{qn}"

def _executor() -> cf.ThreadPoolExecutor:
    ex = st.session_state.get("_streamlit_defer_executor")
    if ex is None:
        ex = cf.ThreadPoolExecutor(max_workers=4)
        st.session_state["_streamlit_defer_executor"] = ex
    return ex


def _safe_rerun() -> None:
    # Streamlit バージョン差吸収
    if hasattr(st, "rerun"):
        st.rerun()
    else:
        st.experimental_rerun()  # type: ignore[attr-defined]


def _hash_depends(obj: Any) -> str:
    """
    depends_on を安定化→JSON化→SHA256 でハッシュし、キーに使う。
    """
    norm = _normalize(obj)
    payload = json.dumps(norm, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _normalize(x: Any) -> Any:
    """
    依存値を“安定的に比較可能な形”へ正規化（再帰）。
    - 型の違い（list/tuple/set など）はタグで区別
    - dict はキーでソート
    - float の NaN/Inf は安定化
    - datetime/date/time は ISO 文字列化
    - dataclass は asdict
    - numpy があれば scalar/ndarray をそれぞれ item()/tolist()
    """
    # dataclass
    if dataclasses.is_dataclass(x):
        x = dataclasses.asdict(x)

    # None / bool / int / str はそのまま
    if x is None or isinstance(x, (bool, int, str)):
        return x

    # float の安定化
    if isinstance(x, float):
        if math.isnan(x):
            return ["float", "NaN"]
        if math.isinf(x):
            return ["float", "Infinity" if x > 0 else "-Infinity"]
        return x

    # Decimal / UUID / Path は文字列化
    if isinstance(x, (Decimal, UUID, Path)):
        return [type(x).__name__, str(x)]

    # 時刻系は ISO 文字列に
    if isinstance(x, (datetime, date, dtime)):
        return [type(x).__name__, x.isoformat()]

    # bytes は hex 文字列に
    if isinstance(x, (bytes, bytearray, memoryview)):
        return ["bytes", bytes(x).hex()]

    # numpy（任意）
    if _np is not None:
        if isinstance(x, (_np.generic,)):  # スカラ
            return _normalize(x.item())
        if isinstance(x, (_np.ndarray,)):  # 配列
            return ["ndarray", _normalize(x.tolist())]

    # list / tuple
    if isinstance(x, (list, tuple)):
        return [type(x).__name__, [_normalize(v) for v in x]]

    # set / frozenset
    if isinstance(x, (set, frozenset)):
        # ソート可能な正規化表現へ
        elems = [_normalize(v) for v in x]
        return [type(x).__name__, sorted(elems, key=lambda v: json.dumps(v, sort_keys=True))]

    # dict
    if isinstance(x, dict):
        items: list[tuple[str, Any]] = []
        for k, v in x.items():
            items.append((str(k), _normalize(v)))
        items.sort(key=lambda kv: kv[0])
        return ["dict", items]

    # それ以外は repr で丸める（最終手段）
    return [type(x).__name__, repr(x)]
