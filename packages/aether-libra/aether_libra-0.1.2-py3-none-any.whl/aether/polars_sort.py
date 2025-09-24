import polars as pl
from typing import Sequence

def reorder_columns(
    df: pl.DataFrame,
    columns_in_order: Sequence[str],
    *,
    keep_others: bool = True,
    strict_on_missing: bool = False,
) -> pl.DataFrame:
    """
    DataFrame の列順を指定順に並べ替える。
    
    - columns_in_order に含まれる **文字列** のみ採用（数値等は無視）
    - 重複列名は先に出た方を優先
    - strict_on_missing=True の場合、指定列が df に無いと ValueError
    - keep_others=True（既定）なら、未指定の残り列を末尾に追加

    Parameters
    ----------
    df : pl.DataFrame
    columns_in_order : Sequence[str]
        先頭に配置したい列名の並び
    keep_others : bool, default True
        True: 未指定列を末尾に残す / False: 指定列のみ
    strict_on_missing : bool, default False
        True の場合、存在しない列名があれば例外

    Returns
    -------
    pl.DataFrame
    """
    # 文字列のみ・重複除去（順序保持）
    seen = set()
    wanted = []
    for c in columns_in_order:
        if isinstance(c, str):
            if strict_on_missing and c not in df.columns:
                raise ValueError(f"Column not found: {c!r}")
            if c in df.columns and c not in seen:
                seen.add(c)
                wanted.append(c)

    if keep_others:
        tails = [c for c in df.columns if c not in seen]
        ordered = wanted + tails
    else:
        ordered = wanted

    # pl.col で明示的に列参照（literal誤解釈を避ける）
    return df.select([pl.col(c) for c in ordered])
