# defer_mode.py
from __future__ import annotations
from contextvars import ContextVar
from contextlib import contextmanager
from typing import Dict, Optional
import streamlit as st


# 遅延モードのON/OFF（ContextVarで入れ子対応）
_DEFER = ContextVar("DEFER", default=False)

# フォーム開始時点の URL クエリのスナップショット（入れ子対応）
_BASELINE_STACK_KEY = "_qp_defer_baselines"

# 更新予定を貯めるバッファ: { key: str | None }
#   - str  … その値に更新
#   - None … キー削除
_DEFER_BUF_KEY = "_qp_deferred_updates"

def in_defer_mode() -> bool:
    return _DEFER.get()

# def _baseline() -> Dict[str, str]:
#     stack = st.session_state.get(_BASELINE_STACK_KEY, [])
#     if stack:
#         return stack[-1]
#     # ベースラインが無ければ、現在のURLを参照
#     return dict(st.query_params)

@contextmanager
def defer_mode():
    """
    この with の中は“遅延モード”。
    - 各部品は URL を書き換えず、差分だけ内部バッファに積む
    - フォーム送信時に apply_deferred_qp_updates() を1回呼べばOK
    """
    token = _DEFER.set(True)
    stack = st.session_state.setdefault(_BASELINE_STACK_KEY, [])
    stack.append(dict(st.query_params))  # ベースラインを積む
    try:
        yield
    finally:
        _DEFER.reset(token)
        stack.pop()

def buffer_put_if_changed(key: str, init_str: str, new_str: str, *, delete_if_empty: bool = False) -> None:
    """
    遅延モード時のみ、ベースライン(init_str)と比較して“変化があった”キーだけをバッファに積む。
    - init_str: URLから復元した初期値（シリアライズ済み）
    - new_str : 現在のUI値（シリアライズ済み）
    - delete_if_empty: new_str=="" の場合にキー削除(None)として扱う
    """
    if not in_defer_mode():
        return

    # init_str は“その部品の初期値”。URLの当初状態と一致するので、
    # ユーザが何も変えていなければ new_str == init_str となり、書かない。
    if new_str == init_str:
        return

    buf: Dict[str, Optional[str]] = st.session_state.setdefault(_DEFER_BUF_KEY, {})
    if delete_if_empty and new_str == "":
        buf[key] = None   # 削除
    else:
        buf[key] = new_str  # 更新

def apply_deferred_query_params_updates() -> bool:
    """
    バッファの差分を URL に一括適用。何か適用したら True を返す。
    - 値(None)は削除、文字列は更新
    """
    buf: Dict[str, Optional[str]] = st.session_state.get(_DEFER_BUF_KEY, {})
    if not buf:
        return False

    to_update = {k: v for k, v in buf.items() if v is not None}
    to_delete = [k for k, v in buf.items() if v is None]

    if to_update:
        st.query_params.update(to_update)
    for k in to_delete:
        try:
            del st.query_params[k]
        except Exception:
            # 古いStreamlitの場合は pop を試す
            try:
                st.query_params.pop(k)  # type: ignore[attr-defined]
            except Exception:
                pass

    st.session_state[_DEFER_BUF_KEY] = {}
    return bool(to_update or to_delete)

def clear_deferred_buffer() -> None:
    """遅延バッファを安全に捨てる（内部構造を知らなくてOK）"""
    st.session_state.pop(_DEFER_BUF_KEY, None)

def clear_deferred_query_params_updates(keys: list[str] | None = None) -> None:
    """
    フィルタのURLパラメータをリセット。
    - keys=None なら全消し
    - keys=[...] なら指定キーだけ削除
    遅延バッファも同時にクリアする
    """
    if keys is None:
        st.query_params.clear()
    else:
        for k in keys:
            st.query_params.pop(k, None)
    clear_deferred_buffer()