import polars as pl

def head_tail(
    df: pl.DataFrame,
    n: int = 5,
    *,
    drop_duplicates: bool = True,
    subset: list[str] | str | None = None,
) -> pl.DataFrame:
    """
    先頭n行＋末尾n行を「順序を保って」返す。
    重複を落とす場合も head→tail の出現順を維持する。
    """
    # 先頭と末尾（末尾は slice(-n) でもOK）
    df_preview = pl.concat([df.head(n), df.tail(n)], how="vertical", rechunk=False)

    if drop_duplicates:
        df_preview = df_preview.unique(
            subset=subset, keep="first", maintain_order=True
        )
        
    return df_preview

# モンキーパッチ（必要なら）
pl.DataFrame.head_tail = head_tail
