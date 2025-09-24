"""
Streamlit用ビューア
- 「変数名 (ファイルパス) → shape → dataframe」の順で表示。
- 見出しレベルを引数で制御可能（"title"|"header"|"subheader"|1..6|"h1".."h6"）
"""
from typing import List, Callable
from pathlib import Path
import re
import streamlit as st
from .polars_csv_loader import DatasetRec  # ← あなたの loader に合わせて

def _make_heading_writer(heading: str | int) -> Callable[[str], None]:
    """
    heading:
      - "title" | "header" | "subheader" ・・・ st.title 等をそのまま使う
      - 1..6 or "h1".."h6"                ・・・ Markdownの # を使って任意レベル
    """
    # 1) 文字列API（title/header/subheader）
    if isinstance(heading, str) and heading in {"title", "header", "subheader"}:
        return getattr(st, heading)

    # 2) 数値 or "hN" → Markdown 見出し
    level: int | None = None
    if isinstance(heading, int):
        level = heading
    elif isinstance(heading, str):
        m = re.fullmatch(r"h([1-6])", heading.lower())
        if m:
            level = int(m.group(1))

    if level is None:
        # フォールバック
        return st.subheader

    level = max(1, min(6, level))
    hashes = "#" * level
    return lambda text: st.markdown(f"{hashes} {text}")

def display_inputs(
    records: List[DatasetRec],
    # title: str = "CSV viewer",
    header_level: str | int = "subheader",  # ← ここでレベル指定
) -> None:
    """
    import streamlit as st
    from aether import load_inputs, assign_to_namespace, display_inputs

    st.set_page_config(layout="wide")

    recs = load_inputs("../input", var_name_map={"train.csv": "df", "test.csv": "df_test"})
    assign_to_namespace(recs, globals()) # グローバル変数に入れる(必要なら)
    display_inputs(recs, header_level='header')
    """
    # st.title(title)
    if not records:
        st.info("No CSV files found.")
        return

    write_heading = _make_heading_writer(header_level)

    for r in records:
        # 例: "df (input/train.csv)"
        write_heading(f"{r.var_name} ({r.path.as_posix()})")
        st.write(r.df.shape)
        st.dataframe(r.df, hide_index=True, use_container_width=True)
