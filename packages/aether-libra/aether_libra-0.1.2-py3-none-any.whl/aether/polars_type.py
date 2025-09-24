from __future__ import annotations
from typing import Literal, Sequence, Optional
import polars as pl
import polars.selectors as cs


from .polars_varargs_ops import find_first_df_with_col


def check_dtype(
    *dfs: pl.DataFrame,
    col: str,
    selectors: Optional[Sequence] = None,
    dtypes: Optional[Sequence[pl.DataType]] = None,
    require_exists: bool = True,
    also_use_by_dtype: bool = True,
) -> bool:
    """
    df[col] が selector群 または dtype群 のどれかに一致するか（OR）を判定する。

    Parameters
    ----------
    df : pl.DataFrame
    col : str
        対象列名
    selectors : Sequence, optional
        polars.selectors.* の戻り値のシーケンス（例: [cs.integer(), cs.float()]）
        ネスト（[ [cs.integer(), cs.float()] ]）でもOK
    dtypes : Sequence[pl.DataType], optional
        pl.Int64, pl.Float64, pl.Date ... などの dtype 群
        ネスト（[ [pl.Int64, pl.Float64] ]）でもOK
    require_exists : bool, default True
        列が存在しないとき KeyError を投げる。False なら False を返す
    also_use_by_dtype : bool, default True
        dtype群について、直接一致に加えて cs.by_dtype(dtypes) でも判定する

    Returns
    -------
    bool

    Notes
    -----
    OR 判定のみ（いずれか一致で True）。AND が欲しければ別関数化してね。
    """
    df = find_first_df_with_col(*dfs, col=col)

    # 存在チェック
    if col not in df.columns:
        if require_exists:
            raise KeyError(f"column not found: {col}")
        return False

    # selector 判定
    if selectors:
        for sel in selectors:
            if callable(sel):
                sel = sel()
            if col in df.select(sel).columns:
                return True

    # dtype 判定（直接一致）
    if dtypes:
        dt = df.schema[col]
        for t in dtypes:
            if dt == t:
                return True

        # dtype 判定（by_dtypeでも見ると便利なことが多い）
        if also_use_by_dtype:
            if col in df.select(cs.by_dtype(dtypes)).columns:
                return True

    return False


def get_dtype_icon(*dfs: pl.DataFrame, col: str) -> str:
    df_first = find_first_df_with_col(*dfs, col=col)
    return _get_dtype_icon(df_first, col=col)


# icon対応済み型名（必要最小限）
_DTypeName = Literal[
    "int", "float", "datetime", "date", "duration",
    "string", "categorical", "unknown"
]


def _get_dtype_icon(df: pl.DataFrame, col: str) -> str:
    """
    dtype_name を使ってアイコン（絵文字）を返す薄い関数。
    """
    kind = _get_dtype_name(df, col)
    mapping = {
        "int": "🔢",
        "float": "🔟",
        "datetime": "🕒",
        "date": "📅",
        "duration": "⌛",
        "string": "🆎",        # 環境により白表示（仕様）
        "categorical": "🏷️",
        "unknown": "❓",
    }
    return mapping.get(kind, "❓")


def _get_dtype_name(df: pl.DataFrame, col: str) -> _DTypeName:
    """
    df と col から、ざっくり型名（Literal）を返す。
    区別するのは: int / float / datetime / date / duration / string / categorical。
    それ以外は 'unknown'。
    """
    if col not in df.columns:
        raise KeyError(f"column not found: {col}")

    def _has(sel) -> bool:
        return col in df.select(sel).columns

    if _has(_sel_int()):
        return "int"
    if _has(_sel_float()):
        return "float"
    if _has(_sel_datetime()):
        return "datetime"
    if _has(_sel_date()):
        return "date"
    if _has(_sel_duration()):
        return "duration"
    if _has(_sel_string()):
        return "string"
    if _has(_sel_categorical()):
        return "categorical"
    return "unknown"


def _sel_int():
    return cs.integer() if hasattr(cs, "integer") else cs.by_dtype(
        [pl.Int8, pl.Int16, pl.Int32, pl.Int64, pl.UInt8, pl.UInt16, pl.UInt32, pl.UInt64]
    )

def _sel_float():
    if hasattr(cs, "float"):
        return cs.float()
    return cs.by_dtype([pl.Float32, pl.Float64])

def _sel_datetime():
    return cs.datetime() if hasattr(cs, "datetime") else cs.by_dtype(pl.Datetime)

def _sel_date():
    return cs.date() if hasattr(cs, "date") else cs.by_dtype(pl.Date)

def _sel_duration():
    return cs.duration() if hasattr(cs, "duration") else cs.by_dtype(pl.Duration)

def _sel_string():
    return cs.string() if hasattr(cs, "string") else cs.by_dtype(pl.Utf8)

def _sel_categorical():
    return cs.by_dtype(pl.Categorical)   # Enum 等は未対応（割り切り）
