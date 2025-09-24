import time
import polars as pl
import pandas as pd
from typing import Iterable, Callable, Optional
from pandas.io.formats.style import Styler


# ========== 小さなタイマー/ロガー ==========
class _Timer:
    def __init__(self, label: str, log: Optional[Callable[[str], None]]):
        self.label = label
        self.log = log
    def __enter__(self):
        self.t0 = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        if self.log is not None:
            dt = time.perf_counter() - self.t0
            self.log(f"[{self.label}] {dt:.3f}s")

def _default_log(msg: str):
    print(f"[describe] {time.strftime('%H:%M:%S')} {msg}")


# 対象列かどうか（top計算の対象判定）
_INT_DTYPES = {
    pl.Int8, pl.Int16, pl.Int32, pl.Int64,
    pl.UInt8, pl.UInt16, pl.UInt32, pl.UInt64,
}

def _top_eligible(dtype: pl.datatypes.DataType, *, include_float: bool) -> bool:
    # 文字列 / カテゴリ / Enum / 真偽 / 整数は常に対象
    if dtype in (pl.Utf8, pl.Categorical, pl.Enum, pl.Boolean):
        return True
    if dtype.__class__ in _INT_DTYPES or dtype in _INT_DTYPES:
        return True
    # Float はフラグで制御
    if include_float and dtype in (pl.Float32, pl.Float64):
        return True
    # それ以外（Decimal/Datetime/Struct/Listなど）は対象外
    return False


# --- 1) describe_ex（stats選択対応版） ---
def describe_ex(
    df: pl.DataFrame,
    detailed: bool = True,
    sig_digits: int = 2,
    stats: list[str] | None = None,
    *,
    profile_log: Optional[Callable[[str], None]] = None,  # ログは必要時だけ渡す（デフォ無音）
    # top 関連
    top_enable: bool = True,           # グローバルOFFはやらない仕様に
    top_include_float: bool = False,    # ← これが新フラグ（デフォ有効＝floatも対象）
    top_max_unique: int = 10_000,      # 高カーディナリティはスキップ
) -> pl.DataFrame:
    """
    拡張describe。stats=Noneでデフォルト（std/medianなし）。
    - 統計ごとに全列まとめて select（多重スキャン回避）
    - n_unique を1回で取得
    - top は Series.value_counts(sort=True) を使い、列名差を吸収
    - float を対象にするかは top_include_float で制御（デフォ True）
    """
    log = profile_log

    if not detailed:
        with _Timer("simple.describe()", log):
            df_simple = df.describe(percentiles=[0.5])
        if sig_digits is not None:
            with _Timer("simple.format", log):
                df_simple = df_simple.with_columns([
                    pl.col(col)
                      .map_elements(lambda x: _format_sig(x, sig_digits), return_dtype=pl.String)
                      .alias(col)
                    for col in df_simple.columns if col != "statistic"
                ])
        return df_simple.cast(pl.Utf8)

    mapping = {
        "non-missing": ("non-missing", lambda s: s.len()),
        "missing":     ("missing",     lambda s: s.null_count()),
        "mean":        ("mean",        lambda s: s.mean()),
        "std":         ("std",         lambda s: s.std()),
        "min":         ("min",         lambda s: s.min()),
        "median":      ("median",      lambda s: s.median()),
        "max":         ("max",         lambda s: s.max()),
    }
    default_stats = ["non-missing","missing","mean","min","max"]
    stat_names = default_stats if stats is None else [s for s in stats if s in mapping]

    rows = []

    # ---- main stats : 統計ごとに1回のselectで全列分を取得 ----
    for sname in stat_names:
        label, func = mapping[sname]
        with _Timer(f"stat:{label}", log):
            exprs = [func(pl.col(c)).alias(c) for c in df.columns]
            out = df.select(exprs)
        row = {"statistic": label}
        for c in df.columns:
            val = out[0, c] if out.height > 0 else None
            row[c] = _format_sig(val, sig_digits)
        rows.append(row)

    # ---- n_unique をまとめて取得 ----
    with _Timer("n_unique", log):
        nunique_row = df.select([pl.col(c).n_unique().alias(c) for c in df.columns])
        nunique_map = {c: int(nunique_row[0, c]) for c in df.columns}

    # ---- dtype/top/top_count 行の雛形 ----
    describe_schema = df.schema
    extra = {
        "dtype":      {"statistic": "dtype"},
        "top":        {"statistic": "top"},
        "top_count":  {"statistic": "top_count"},
        "n_unique":   {"statistic": "n_unique"},
    }
    for c in df.columns:
        extra["dtype"][c] = str(describe_schema[c])
        extra["n_unique"][c] = str(nunique_map[c])

    # ---- top/top_count ----
    if top_enable:
        with _Timer("top_each_column", log):
            for c in df.columns:
                dtype = describe_schema[c]
                # 対象外や高カーディナリティはスキップ（Top/TopCount ともに "－"）
                if (not _top_eligible(dtype, include_float=top_include_float)) or (nunique_map[c] > top_max_unique):
                    extra["top"][c] = "－"
                    extra["top_count"][c] = "－"   # ← 空文字ではなく "－" に変更
                    continue
                try:
                    s = df.select(pl.col(c)).drop_nulls().get_column(c)
                    if s.len() == 0:
                        # 本当に非欠損ゼロ：top="" / count="0"
                        top_val, top_cnt = "", "0"
                    else:
                        vcdf = s.value_counts(sort=True)
                        if "counts" in vcdf.columns:
                            counts_col = "counts"
                        else:
                            counts_col = next((cn for cn in vcdf.columns if cn.endswith("counts")), vcdf.columns[-1])
                        vals_col = next((cn for cn in vcdf.columns if cn != counts_col), vcdf.columns[0])

                        if vcdf.height > 0:
                            top_val = _format_sig(vcdf[0, vals_col], sig_digits)
                            top_cnt = str(int(vcdf[0, counts_col]))
                        else:
                            top_val, top_cnt = "", "0"
                except KeyboardInterrupt:
                    extra["top"][c] = "－"
                    extra["top_count"][c] = "－"
                    if log is not None:
                        log(f"[top:{c}] KeyboardInterrupt, skipped")
                    continue
                except Exception:
                    extra["top"][c] = "－"
                    extra["top_count"][c] = "－"
                    continue
                extra["top"][c] = top_val
                extra["top_count"][c] = top_cnt
    else:
        for c in df.columns:
            extra["top"][c] = "－"
            extra["top_count"][c] = "－"

    with _Timer("assemble", log):
        df_out = pl.DataFrame(rows + [extra[k] for k in ["dtype","top","top_count","n_unique"]]).cast(pl.Utf8)
        desired = ["dtype","non-missing","missing","n_unique","mean","std","min","median","max","top","top_count"]
        actual = df_out.get_column("statistic").to_list()
        order = [s for s in desired if s in actual] + [s for s in actual if s not in desired]
        df_out = (
            df_out.with_columns(
                pl.col("statistic").map_elements(lambda s: order.index(s), return_dtype=pl.Int32).alias("__order")
            )
            .sort("__order")
            .drop("__order")
        )
    return df_out


def _format_sig(x, sig_digits: int) -> str:
    if x is None:
        return ""
    if isinstance(x, float):
        if x == int(x):
            return str(int(x))
        s = f"{x:.{sig_digits}g}"
        if "e" in s or "E" in s:
            s = f"{x:.{sig_digits}f}"
        s = s.rstrip("0").rstrip(".") if "." in s else s
        return s
    return str(x)


# --- 2) describe_compare ---
def describe_compare(
    *dfs: pl.DataFrame,
    names: Iterable[str] | None = None,
    stats: list[str] | None = None,
    detailed: bool = True,
    sig_digits: int = 2,
    feature: str | None = None,
    drop_feature_col: bool = True,
    single_feature_layout: str = "stat_rows",
    profile_log: Optional[Callable[[str], None]] = None,
    top_enable: bool = True,
    top_include_float: bool = False,
    top_max_unique: int = 10_000,
) -> pl.DataFrame:
    if names is None:
        names = [f"df{i+1}" for i in range(len(dfs))]
    names = list(names)
    assert len(names) == len(dfs)

    stat_names_ref: list[str] | None = None
    long_frames = []

    for df, nm in zip(dfs, names):
        has_feature = (feature in df.columns) if feature is not None else True
        if has_feature:
            desc = describe_ex(
                df, detailed=detailed, sig_digits=sig_digits, stats=stats,
                profile_log=profile_log,
                top_enable=top_enable, top_include_float=top_include_float, top_max_unique=top_max_unique,
            )
            long = desc.melt(id_vars=["statistic"], variable_name="feature", value_name="value")
            if feature is not None:
                long = long.filter(pl.col("feature") == feature)
            if stat_names_ref is None:
                stat_names_ref = long.select("statistic").to_series().to_list()
            long = long.with_columns(pl.lit(nm).alias("df_name"))
            long_frames.append(long)
        else:
            if stat_names_ref is None:
                default_order = ["dtype","non-missing","missing","n_unique","mean","std","min","median","max","top","top_count"]
                stat_names_ref = [s for s in default_order if (stats is None or s in set(stats+["dtype","n_unique","top","top_count"]))]

            long = pl.DataFrame({
                "statistic": stat_names_ref,
                "feature":   [feature] * len(stat_names_ref) if feature else [""] * len(stat_names_ref),
                "value":     ["－"] * len(stat_names_ref),
                "df_name":   [nm] * len(stat_names_ref),
            })
            long_frames.append(long)

    all_long = pl.concat(long_frames, how="vertical", rechunk=True)

    if feature is not None and single_feature_layout == "stat_rows":
        wide = all_long.pivot(index=["statistic"], columns="df_name", values="value")
        wide = wide.select(["statistic", *[n for n in names if n in wide.columns]])
        if drop_feature_col and "feature" in wide.columns:
            wide = wide.drop("feature")
        return wide

    wide = all_long.pivot(index=["feature","statistic"], columns="df_name", values="value")
    wide = wide.select(["feature","statistic", *[n for n in names if n in wide.columns]])
    if drop_feature_col:
        wide = wide.drop("feature")
    return wide


def to_styler_for_streamlit(
    df_pl: pl.DataFrame,
    color_map: dict[str, str] = {'train': 'lightblue', 'test': 'lightpink'},
    hide_index: bool = True,
    equal_width: bool = True,
    data_col_width_px: int = 120,
    first_col_width_px: int | None = None,
) -> Styler:
    pdf = df_pl.to_pandas()
    styler = pdf.style

    # 先にテーブル全体の体裁だけ設定（色はまだ触らない）
    styler = styler.set_properties(**{"white-space": "nowrap"})
    styler = styler.set_table_styles(
        [{"selector": "th", "props": [("text-align", "left")]}],
        overwrite=True,
    )

    # index非表示（互換＋CSS保険）
    try:
        styler = styler.hide(axis="index")
    except Exception:
        try:
            styler = styler.hide_index()
        except Exception:
            pass
    styler = styler.set_table_styles([
        {"selector": "th.row_heading", "props": [("display", "none")]},
        {"selector": "th.blank",       "props": [("display", "none")]},
    ], overwrite=False)

    # 列幅を固定（テーブルCSS）
    if equal_width:
        n_cols = pdf.shape[1]
        w0 = first_col_width_px if first_col_width_px is not None else data_col_width_px
        css = [{"selector": "table", "props": [("table-layout", "fixed")]}]
        for j in range(n_cols):
            w = w0 if j == 0 else data_col_width_px
            css += [
                {"selector": f"th.col_heading.level0.col{j}", "props": [("width", f"{w}px"), ("max-width", f"{w}px")]},
                {"selector": f"td.col{j}",                     "props": [("width", f"{w}px"), ("max-width", f"{w}px")]},
            ]
        styler = styler.set_table_styles(css, overwrite=False)

    # 列ごとの色
    if color_map:
        for col, color in color_map.items():
            if col in pdf.columns:
                styler = styler.apply(
                    lambda s, c=color: [f"color: {c} !important"] * len(s),
                    axis=0,
                    subset=pd.IndexSlice[:, [col]],
                )

    return styler
