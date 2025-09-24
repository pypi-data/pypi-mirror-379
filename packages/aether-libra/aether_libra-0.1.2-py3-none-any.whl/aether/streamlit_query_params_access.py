"""
query_params_access.py
----------------
StreamlitのURLクエリ（st.query_params）と“素直に”やり取りするための
小さなヘルパ関数群。複雑なバインディングは持たない。

設計方針:
- URLは共有/ブックマークのための単純な文字列辞書とみなす
- 更新は st.query_params.update({...}) のみ
- 配列は「カンマ区切り + URLエンコード」で表現（人間にも読める）
"""
from __future__ import annotations
from typing import List, Optional
from urllib.parse import quote, unquote
from datetime import date
import streamlit as st


# ---------- 配列の直感的シリアライズ ----------
def ser_list(xs: List[str]) -> str:
    """['A','B/C'] -> 'A,B%2FC'（URLセーフ・可読）"""
    return ",".join(quote(x, safe="") for x in xs)

def de_list(s: str) -> List[str]:
    """'A,B%2FC' -> ['A','B/C']。空/Noneは [] を返す。"""
    if not s:
        return []
    return [unquote(x) for x in s.split(",") if x]


# ---------- URL から読む ----------
def qp_get_str(name: str, default: str = "") -> str:
    """クエリを文字列で読む。未設定なら default。"""
    v = st.query_params.get(name, default)
    return v if isinstance(v, str) else str(v)

def qp_get_list(name: str) -> List[str]:
    """クエリを配列（カンマ区切り）として読む。"""
    return de_list(qp_get_str(name, ""))

def qp_get_bool(name: str, default: bool = False) -> bool:
    """'1' / 'true' / 'True' を True とみなす。"""
    raw = qp_get_str(name, "1" if default else "0")
    return raw in ("1", "true", "True")

def qp_get_int(name: str, default: int = 0) -> int:
    """intとして読む（失敗時はdefault）。"""
    try:
        return int(qp_get_str(name, str(default)))
    except Exception:
        return default

def qp_get_float(name: str, default: float = 0.0) -> float:
    """floatとして読む（失敗時はdefault）。"""
    try:
        return float(qp_get_str(name, str(default)))
    except Exception:
        return default

def qp_get_date(name: str, default: Optional[date] = None) -> Optional[date]:
    """YYYY-MM-DD として読む。空 or 失敗時は default。"""
    raw = qp_get_str(name, "")
    if not raw:
        return default
    try:
        return date.fromisoformat(raw)
    except Exception:
        return default


# ---------- URL に書く（変更時のみ呼ぶ想定） ----------
def qp_set_str(name: str, value: str) -> None:
    """クエリに文字列をセット。"""
    st.query_params.update({name: value})

def qp_set_list(name: str, xs: List[str]) -> None:
    """クエリに配列をセット（カンマ区切り）。"""
    st.query_params.update({name: ser_list(xs)})

def qp_set_bool(name: str, value: bool) -> None:
    """クエリに bool を '1' / '0' でセット。"""
    st.query_params.update({name: "1" if value else "0"})

def qp_set_int(name: str, value: int) -> None:
    """クエリに int をセット。"""
    st.query_params.update({name: str(int(value))})

def qp_set_float(name: str, value: float) -> None:
    """クエリに float をセット。"""
    st.query_params.update({name: str(float(value))})

def qp_set_date(name: str, value: date) -> None:
    """クエリに日付(ISO)をセット。"""
    st.query_params.update({name: value.isoformat()})

def qp_clear_all() -> None:
    """URLクエリを全削除。"""
    st.query_params.clear()
