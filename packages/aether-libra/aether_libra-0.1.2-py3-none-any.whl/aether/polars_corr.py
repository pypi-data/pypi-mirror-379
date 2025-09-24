import polars as pl
import numpy as np
from typing import Literal, Optional


def corr_with_target(
    df: pl.DataFrame,
    col_target: str,
    *,
    max_unique_ratio: float = 0.3,   # 行数に対するユニーク比がこれを超えたらスキップ
    max_unique_count: int = 100,     # ユニーク数がこれを超えたらスキップ
    treat_datetime: Literal["epoch", "ignore"] = "epoch",  # 日付列の扱い
    treat_duration: Literal[
        "seconds", "milliseconds", "microseconds", "nanoseconds", "ignore"
    ] = "seconds",                    # Duration（時間差）の扱い
    drop_na: bool = True,            # 欠損は両列同時に落として計算（内部でNaNマスク）
) -> pl.DataFrame:
    """
    df と col_target を受け取り、全列についてターゲットとの相関“係数”を返す。

    ルール:
      - 数値列: Pearson相関
      - カテゴリ列(文字列/カテゴリ型): One-hot化した各ダミー列とターゲットの Pearson を計算し、
        その最大値（絶対値で最大のもの）をその列の“強さ”とする
      - 日付/日時列: treat_datetime に応じて
          - "epoch": エポック(μs)整数に変換して Pearson
          - "ignore": スキップ
      - Duration列: treat_duration に応じて
          - "seconds" / "milliseconds" / "microseconds" / "nanoseconds": それぞれ合計量に変換して Pearson
          - "ignore": スキップ
      - 高カーディナリティのカテゴリ列はスキップ（理由も note に入れる）

    返却カラム:
      - column: 対象列名
      - kind: numeric / categorical / datetime / duration / skipped
      - method:
          - pearson
          - onehot_max_pearson
          - datetime_epoch_pearson
          - duration_total_<unit>_pearson
          - skipped
      - corr: 相関係数（カテゴリは最大ダミー相関）
      - abs_corr: |corr|
      - note: スキップ理由や補足

    Examples
    --------
    >>> # 1) ある col の相関係数だけ取り出す（存在すれば1行）
    >>> res = corr_with_target(df, "sales")
    >>> float(res.filter(pl.col("column") == "price")["corr"][0])

    >>> # 2) 相関係数の絶対値が強い順に df の列順を並べ替える
    >>> res = corr_with_target(df, "sales")
    >>> order = (
    ...     res.drop_nulls("abs_corr")
    ...        .sort("abs_corr", descending=True)["column"]
    ...        .to_list()
    ... )
    >>> ordered_cols = [c for c in order if c in df.columns and c != "sales"]
    >>> df_reordered = df.select(["sales", *ordered_cols])  # 先頭にターゲットを置く例
    """
    # ---------- helpers ----------
    def _pearson_np(x: np.ndarray, y: np.ndarray) -> Optional[float]:
        """NaN同時除去して Pearson を計算。計算不可なら None。"""
        x = x.astype("float64", copy=False)
        y = y.astype("float64", copy=False)
        mask = ~np.isnan(x) & ~np.isnan(y)
        if mask.sum() < 2:
            return None
        xv = x[mask]
        yv = y[mask]
        # 分散ゼロなら相関は定義できない
        if np.std(xv) == 0 or np.std(yv) == 0:
            return None
        return float(np.corrcoef(xv, yv)[0, 1])

    # ---------- validations ----------
    if col_target not in df.columns:
        raise ValueError(f"{col_target=} が df に存在しません。")
    n = df.height
    if n < 2:
        raise ValueError("行数が少なすぎて相関を計算できません。")
    if not df[col_target].dtype.is_numeric():
        raise TypeError("現在の実装は数値ターゲットのみ対応です（カテゴリターゲットは未対応）。")

    y_all = df[col_target].to_numpy()

    out = []
    if col_target in df.columns and df.width == 1:
        # --- col_targetそのものならスキップ ---
        out.append({
            "column": col_target,
            "kind": "skipped",
            "method": "skipped",
            "corr": None,
            "abs_corr": None,
            "note": f"col equals col_target",
        })
    else:
        for col in df.columns:

            # --- col_targetそのものならスキップ ---
            if col == col_target:
                continue
            
            dt = df[col].dtype

            # --- 数値列 ---
            if dt.is_numeric():
                x = df[col].to_numpy()
                corr = _pearson_np(x, y_all)
                out.append({
                    "column": col,
                    "kind": "numeric",
                    "method": "pearson",
                    "corr": corr,
                    "abs_corr": abs(corr) if corr is not None else None,
                    "note": "",
                })
                continue

            # --- 日付/日時列 ---
            if dt in (pl.Date, pl.Datetime):
                if treat_datetime == "ignore":
                    out.append({
                        "column": col,
                        "kind": "datetime",
                        "method": "skipped",
                        "corr": None,
                        "abs_corr": None,
                        "note": "datetime ignored",
                    })
                    continue
                # epoch(μs)を数値化
                x = (
                    df.select(pl.col(col).dt.epoch("us").cast(pl.Int64))
                    .to_series()
                    .to_numpy()
                )
                corr = _pearson_np(x, y_all)
                out.append({
                    "column": col,
                    "kind": "datetime",
                    "method": "datetime_epoch_pearson",
                    "corr": corr,
                    "abs_corr": abs(corr) if corr is not None else None,
                    "note": "converted to epoch(us)",
                })
                continue

            # --- Duration（時間差）列 ---
            if dt == pl.Duration:
                if treat_duration == "ignore":
                    out.append({
                        "column": col,
                        "kind": "duration",
                        "method": "skipped",
                        "corr": None,
                        "abs_corr": None,
                        "note": "duration ignored",
                    })
                    continue

                # 単位→対応する total_* 変換
                unit_to_expr = {
                    "seconds": pl.col(col).dt.total_seconds(),
                    "milliseconds": pl.col(col).dt.total_milliseconds(),
                    "microseconds": pl.col(col).dt.total_microseconds(),
                    "nanoseconds": pl.col(col).dt.total_nanoseconds(),
                }
                if treat_duration not in unit_to_expr:
                    raise ValueError(f"unsupported treat_duration={treat_duration!r}")

                x = df.select(unit_to_expr[treat_duration].cast(pl.Float64)).to_series().to_numpy()
                corr = _pearson_np(x, y_all)
                out.append({
                    "column": col,
                    "kind": "duration",
                    "method": f"duration_total_{treat_duration}_pearson",
                    "corr": corr,
                    "abs_corr": abs(corr) if corr is not None else None,
                    "note": f"converted to total {treat_duration}",
                })
                continue

            # --- 文字列/カテゴリ列を One-hot ---
            if dt in (pl.Utf8, pl.Categorical):
                # 高カーディナリティ判定
                nunique = int(df.select(pl.col(col).n_unique()).item())
                if nunique > max_unique_count or (nunique / max(n, 1)) > max_unique_ratio:
                    out.append({
                        "column": col,
                        "kind": "categorical",
                        "method": "skipped",
                        "corr": None,
                        "abs_corr": None,
                        "note": f"high cardinality (n_unique={nunique})",
                    })
                    continue

                # One-hot
                dummies = df.select(col).to_dummies()
                if dummies.width == 0:
                    out.append({
                        "column": col,
                        "kind": "categorical",
                        "method": "skipped",
                        "corr": None,
                        "abs_corr": None,
                        "note": "no dummy columns produced",
                    })
                    continue

                best_corr = None
                best_dummy = None
                for dcol in dummies.columns:
                    x = dummies[dcol].to_numpy().astype(float)
                    corr = _pearson_np(x, y_all)
                    if corr is None:
                        continue
                    if (best_corr is None) or (abs(corr) > abs(best_corr)):
                        best_corr = corr
                        best_dummy = dcol

                out.append({
                    "column": col,
                    "kind": "categorical",
                    "method": "onehot_max_pearson",
                    "corr": best_corr,
                    "abs_corr": abs(best_corr) if best_corr is not None else None,
                    "note": f"max dummy: {best_dummy}" if best_dummy else "all dummies invalid",
                })
                continue

            # --- その他の型はスキップ ---
            out.append({
                "column": col,
                "kind": "skipped",
                "method": "skipped",
                "corr": None,
                "abs_corr": None,
                "note": f"unsupported dtype: {dt}",
            })

    return pl.DataFrame(out).sort(["abs_corr", "column"], descending=[True, False])
