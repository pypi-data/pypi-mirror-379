"""
Notebook/Jupyter用ビューア
- 「変数名 (ファイルパス) → shape → DataFrame」を display。
- 見出しは Markdown の # を使って header_level で制御（1〜6）。
- 大きい表は head_n を指定すると軽量表示。
"""

from typing import List, Optional
from IPython.display import display, Markdown
import pandas as pd
from .polars_csv_loader import DatasetRec


def display_inputs_notebook(
    records: List[DatasetRec],
    header_level: int = 3,
) -> None:
    """
    from aether import load_inputs, assign_to_namespace, display_inputs_notebook

    recs = load_inputs("../input", var_name_map={"train.csv": "df", "test.csv": "df_test"})
    assign_to_namespace(recs, globals()) # グローバル変数に入れる(必要なら)
    display_inputs_notebook(recs, header_level=3)
    """
    if not records:
        display(Markdown("_No CSV files found._"))
        return

    # レベルは 1〜6 に丸める
    level = max(1, min(6, int(header_level)))
    hashes = "#" * level

    for r in records:
        # 見出し（Markdown）
        display(Markdown(f"{hashes} {r.var_name} ({r.path.as_posix()})"))

        display(r.df)
