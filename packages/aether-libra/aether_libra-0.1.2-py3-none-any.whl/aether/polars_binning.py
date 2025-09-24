from IPython.display import display
import polars as pl
import types
import matplotlib.ticker as mticker
import math
from dataclasses import dataclass
from typing import Optional

from .decorator_tracer import tracer


@dataclass
class get_col_bin_trace:
    df_bin_detail_info: Optional[pl.DataFrame] = None
    col_bin: str = None

@tracer
def get_col_bin_auto(
    *dfs: pl.DataFrame,
    col: str,
    col_bin: str = None,
    num_n_bins: int = 10,
    num_sig_digits: int = 3,
    dt_truncate_unit: str = "1mo",
    verbose: int = 0,
    traceable: bool = False,
) -> tuple[pl.DataFrame, ...]:
    """
    
    Examples:
    ```python
    # df_original, df_test_original = df.clone(), df_test.clone()

    df_new, df_test_new, df_bin_detail_info = aether.get_col_bin_auto(df_original, df_test_original, col='date')
    df, df_test = df.with_columns(df_new), df_test.with_columns(df_test_new)
    display(df, df_test)
    ```
    """

    dfs_with_col = [df for df in dfs if col in df.columns]
    if not dfs_with_col:
        raise ValueError(f"指定された列 `{col}` を持つDataFrameが1つもありません")
    
    dtype = dfs_with_col[0].schema[col]

    if dtype.is_numeric():
        return get_col_bin_numeric(*dfs, col=col, col_bin=col_bin, num_n_bins=num_n_bins, num_sig_digits=num_sig_digits, verbose=verbose, traceable=traceable)
    elif dtype in (pl.Date, pl.Datetime):
        return get_col_bin_datetime(*dfs, col=col, col_bin=col_bin, dt_truncate_unit=dt_truncate_unit, verbose=verbose, traceable=traceable)
    elif dtype in (pl.Utf8, pl.Categorical):
        return get_col_bin_categorical(*dfs, col=col, col_bin=col_bin, verbose=verbose, traceable=traceable)
    else:
        raise ValueError(f"Unsupported dtype: {dtype}")


@tracer
def get_col_bin_numeric(
    *dfs: pl.DataFrame,
    col: str,
    col_bin: str = None,
    num_n_bins: int = 10,
    num_sig_digits: int = 3,
    verbose: int = 0,
    traceable: bool = False,
) -> tuple[pl.DataFrame, ...]:

    if col_bin is None:
        col_bin = f"{col}_bin"
    dfs_with_col = [df for df in dfs if col in df.columns]
    df_concat = pl.concat([df.select(col) for df in dfs_with_col])
    min_val = df_concat.select(col).to_series().min()
    max_val = df_concat.select(col).to_series().max()
    locator = mticker.MaxNLocator(nbins=num_n_bins)
    bins = locator.tick_values(min_val, max_val)
    bins = sorted(set(_round_sig(b, num_sig_digits) for b in bins))# 有効数字で丸める⇒重複を排す(丸めた影響でかぶりが出る可能性がある)⇒並びが崩れるので並べ直す
    breaks = bins[1:-1]
    labels = _make_bin_labels(bins)

    starts = bins[:-1]
    ends = bins[1:]
    centers = [(s + e) / 2 for s, e in zip(starts, ends)]

    dfs_bin = []
    for df in dfs:
        if col in df.columns:
            df_bin = df.select(pl.col(col).cut(breaks=breaks, labels=labels).alias(col_bin))
        else:
            # 元の列がない場合、全部値がNullの列を返す
            # df_bin = pl.DataFrame({col_bin: [None] * df.height})
            df_bin = pl.DataFrame({col_bin: [None] * df.height}).with_columns(pl.col(col_bin).cast(pl.Categorical))
        dfs_bin.append(df_bin)
        if verbose:
            print("df_bin:")
            display(df_bin)

    df_bin_detail_info = pl.DataFrame({
        col_bin: labels,
        f"{col_bin}_start": starts,
        f"{col_bin}_end": ends,
        f"{col_bin}_median": centers
    }).with_columns([pl.col(col_bin).cast(pl.Categorical)])

    if verbose:
        print("df_bin_detail_info:")
        display(df_bin_detail_info)

    # return (*dfs_bin, df_bin_detail_info)
    if traceable:
        trace = get_col_bin_trace(df_bin_detail_info=df_bin_detail_info, col_bin=col_bin)
        return (*dfs_bin, trace)
    return dfs_bin


@tracer
def get_col_bin_datetime(
    *dfs: pl.DataFrame,
    col: str,
    col_bin: str = None,
     dt_truncate_unit: str = "1mo",
    verbose: int = 0,
    traceable: bool = False,
) -> tuple[pl.DataFrame, ...]:

    if col_bin is None:
        col_bin = f"{col}_bin"
    dfs_with_col = [df for df in dfs if col in df.columns]
    df_concat = pl.concat([df.select(col) for df in dfs_with_col])

    # minをbin始まりとしてtruncate(切り捨て)して、maxに1期間分余分に足したもの(ケツのbinを切り捨てずに切り出すため。後の処理で使う)
    min_truncated = df_concat.select(pl.col(col).min().dt.truncate(dt_truncate_unit)).item()
    max_plus_1_unit = df_concat.select(pl.col(col).max().dt.offset_by(dt_truncate_unit)).item()

    # ビンの生成
    is_date = df_concat[col].dtype == pl.Date
    range_fn = pl.date_range if is_date else pl.datetime_range
    bin_starts_plus1 = range_fn(start=min_truncated, end=max_plus_1_unit, interval=dt_truncate_unit, eager=True) # ケツに1期間を足したリスト
    bin_starts = bin_starts_plus1[:-1].to_list() # ケツの1期間は削る
    bin_ends = bin_starts_plus1[1:].to_list() # 最初の1期間は削る
    bin_medians = [s + (e - s) // 2 for s, e in zip(bin_starts, bin_ends)]

    # ビンの詳細テーブル
    df_bin_detail_info = pl.DataFrame({
        col_bin: bin_starts,
        f"{col_bin}_start": bin_starts,
        f"{col_bin}_end": bin_ends,
        f"{col_bin}_median": bin_medians
    })

    dfs_bin = []
    for df in dfs:
        if col in df.columns:
            col_expr = pl.col(col).dt.truncate(dt_truncate_unit)
            if not is_date:
                # only Datetime needs cast
                unit = df_bin_detail_info.schema[col_bin].time_unit
                col_expr = col_expr.dt.cast_time_unit(unit)
            df_bin = df.select(col_expr.alias(col_bin))
        else:
            df_bin = pl.DataFrame({col_bin: [None] * df.height})
        dfs_bin.append(df_bin)
        if verbose:
            print("df_bin:")
            display(df_bin)

    if verbose:
        print("df_bin_detail_info:")
        display(df_bin_detail_info)

    # return (*dfs_bin, df_bin_detail_info)
    if traceable:
        trace = get_col_bin_trace(df_bin_detail_info=df_bin_detail_info, col_bin=col_bin)
        return (*dfs_bin, trace)
    return dfs_bin


@tracer
def get_col_bin_categorical(
    *dfs: pl.DataFrame,
    col: str,
    col_bin: str = None,
     verbose: int = 0,
    traceable: bool = False,
) -> tuple[pl.DataFrame, ...]:

    if col_bin is None:
        col_bin = f"{col}_bin" # カテゴリカルの場合何もしないので意味がないが、他と揃えるためにbin列として新設する
    dfs_bin = []
    for df in dfs:
        if col in df.columns:
            df_bin = df.select(pl.col(col).alias(col_bin))
        else:
            df_bin = pl.DataFrame({col_bin: [None] * df.height})
        dfs_bin.append(df_bin)
        if verbose:
            print("df_bin:")
            display(df_bin)
    # return (*dfs_bin, None)
    if traceable:
        trace = get_col_bin_trace(df_bin_detail_info=None, col_bin=col_bin)
        return (*dfs_bin, trace)
    return dfs_bin

def _round_sig(x: float, sig: int) -> float:
    if x == 0:
        return 0.0
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)


def _make_bin_labels(bins: list[float]) -> list[str]:
    return [f"{start}–{end}" for start, end in zip(bins[:-1], bins[1:])]


def assert_df_bin_detail_info_columns(df: pl.DataFrame, col_bin: str) -> None:
    """
    指定された col_bin に基づき、df_bin_detail_info が必要な列を持っているか確認する。

    必須列:
        - col_bin
        - {col_bin}_start
        - {col_bin}_end
        - {col_bin}_median

    Raises:
        AssertionError: いずれかの列が存在しない場合
    """
    required_cols = [
        col_bin,
        f"{col_bin}_start",
        f"{col_bin}_end",
        f"{col_bin}_median",
    ]
    missing = [col for col in required_cols if col not in df.columns]

    assert not missing, f"Missing columns in df_bin_detail_info: {missing}"


"""
__all__ を動的に生成（このモジュール内の関数だけを対象にする）
"""
__all__ = [
    name for name, val in globals().items()
    if (
        (isinstance(val, types.FunctionType) or isinstance(val, type))  # 関数 or クラス
        and 
        val.__module__ == __name__  # このモジュール内のものに限定
    )
]