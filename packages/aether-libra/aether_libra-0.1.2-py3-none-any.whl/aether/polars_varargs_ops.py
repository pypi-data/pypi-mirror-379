import polars as pl
from typing import Optional, Tuple


def find_first_df_with_col(
        *dfs: pl.DataFrame, 
        col: str,
        assert_same_dtype: bool = True,
        ) -> Optional[pl.DataFrame]:
    """
    可変長引数 dfs の中から、指定した列 col を持つ最初の DataFrame を返す。
    見つからなければ None を返す。

    Parameters
    ----------
    col : str
        探したい列名。
    *dfs : pl.DataFrame
        検索対象となる DataFrame 群。

    Returns
    -------
    Optional[pl.DataFrame]
        最初に該当列を持つ DataFrame。なければ None。

    Notes
    -----
    関数を呼ばずに済ませたい場合は、以下のワンライナーでも同等の動作をします::

        first_df = next((df for df in dfs if col in df.columns), None)

    Examples
    --------
    >>> df1 = pl.DataFrame({"a": [1, 2]})
    >>> df2 = pl.DataFrame({"b": [3, 4]})
    >>> df3 = pl.DataFrame({"c": [5, 6]})
    >>> find_first_df_with_col("b", df1, df2, df3)
    shape: (2, 1)
    ┌─────┐
    │ b   │
    │ --- │
    │ i64 │
    ╞═════╡
    │ 3   │
    │ 4   │
    └─────┘
    """
    if assert_same_dtype:
        assert_same_dtype_for_col(*dfs, col=col)

    for df in dfs:
        if col in df.columns:
            return df
    return None


def assert_same_dtype_for_col(*dfs: pl.DataFrame, col: str) -> None:
    """
    可変長 dfs のうち、col を持つ DF だけを対象に dtype が一致していることを確認。
    - 0件 or 1件しか持っていなければ何もしない
    - 複数あり、型が混在していれば AssertionError
    """
    types = {df.schema[col] for df in dfs if col in df.columns}
    if len(types) <= 1:
        return
    raise AssertionError(f"dtype mismatch for column '{col}': found types = {', '.join(map(str, types))}")


def align_columns_strict(*dfs: pl.DataFrame, verbose: int = 1) -> Tuple[pl.DataFrame, ...]:
    """
    可変長の複数DataFrameで列を揃える（concatはしない、追加のみ）。
    - ない列は None を、その列の「最初に見つかったDF」の dtype に cast して追加。
    - 既存列の型は一切キャストしない（型不一致があれば詳細をprintして AssertionError）。
    - 列順は「列が最初に登場した順」に統一。

    Parameters
    ----------
    *dfs : pl.DataFrame
        対象のDataFrame群（順序が「型の基準」と「列順の基準」に使われます）
    verbose : int, default 1
        1以上で不一致の詳細をprint。0ならprintしない（ただし例外は投げる）。

    Returns
    -------
    Tuple[pl.DataFrame, ...]
        列が揃えられたDataFrameのタプル（元DFは不変）

    Raises
    ------
    AssertionError
        同名列でdtypeが一致しない列が1つでもある場合（自動キャストはしない）。
    """
    if not dfs:
        return tuple()

    # --- 1) 列の「最初に登場した順序」と「基準dtype（最初に見つかったDFのdtype）」を決める ---
    first_seen_order: list[str] = []
    ref_dtype: dict[str, pl.DataType] = {}
    for i, df in enumerate(dfs):
        for col, dt in df.schema.items():
            if col not in ref_dtype:
                ref_dtype[col] = dt
                first_seen_order.append(col)

    # --- 2) 同名列のdtypeが全DFで一致しているかチェック（不一致なら詳細printして例外） ---
    mismatches: dict[str, dict[str, list[int]]] = {}  # col -> {dtype_str: [df_index,...]}
    for idx, df in enumerate(dfs):
        for col, dt in df.schema.items():
            ref = ref_dtype[col]  # この列の「最初に見つかったdtype」
            if dt != ref:
                entry = mismatches.setdefault(col, {})
                entry.setdefault(str(dt), []).append(idx)
                entry.setdefault(str(ref), [])  # ref表記もまとめのため保持（後で使う）

    if mismatches:
        if verbose:
            for col, dt_map in mismatches.items():
                print(f"[Type mismatch] column = '{col}'")
                # どのdtypeがどのDFにあったか一覧
                # ref側を先に出したいので並び替え
                keys = list(dt_map.keys())
                # 参照dtype（最初に見つかったdtype）を先頭へ
                ref_key = str(ref_dtype[col])
                keys = [ref_key] + [k for k in keys if k != ref_key]
                for k in keys:
                    idxs = dt_map.get(k, [])
                    mark = " (ref)" if k == ref_key else ""
                    print(f"  dtype {k}{mark} : dfs {idxs}")
        raise AssertionError(
            "列のdtypeが一致しません（詳細はprint出力を参照）。"
            " 自動キャストは行わないため、事前にdtypeを合わせてから実行してください。"
        )

    # --- 3) ない列を None.cast(基準dtype) で追加（既存列は触らない） ---
    aligned: list[pl.DataFrame] = []
    for df in dfs:
        missing = [c for c in ref_dtype.keys() if c not in df.columns]
        if missing:
            add_exprs = [pl.lit(None).cast(ref_dtype[c]).alias(c) for c in missing]
            df2 = df.with_columns(add_exprs)
        else:
            df2 = df

        # 列順を「最初に登場した順」に統一（余剰列があれば末尾へ）
        keep = [c for c in first_seen_order if c in df2.columns]
        rest = [c for c in df2.columns if c not in keep]
        df2 = df2.select([*keep, *rest])
        aligned.append(df2)

    return tuple(aligned)
