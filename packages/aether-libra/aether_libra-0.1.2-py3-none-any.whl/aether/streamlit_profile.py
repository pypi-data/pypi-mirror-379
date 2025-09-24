import streamlit as st
import polars as pl
import altair as alt
import time

from .polars_corr import *
from .polars_type import *
from .polars_table import *
from .altair_plot_after_binning_facade import *


def select_columns(
    df: pl.DataFrame,
    label: str,
    exclude: Optional[set[str]] = None,
    default: Optional[Sequence[str]] = None,
    container=st,
    return_all_if_empty: bool = False,
) -> list[str]:
    """
    PolarsのDataFrameから複数列を選択するマルチセレクトUIを指定された場所に表示する。

    Parameters
    ----------
    df : pl.DataFrame
        入力データ
    label : str
        UIに表示するラベル
    exclude : set[str], optional
        選択肢から除外する列名セット
    default : list[str], optional
        デフォルトで選択する列名リスト
    container : Streamlitの表示先, default st
        表示先（例: st, st.sidebar, st.container(), st.expander("詳細")）
    return_all_if_empty : bool, default False
        Trueの場合、選択が空なら全ての候補列を返す

    Returns
    -------
    list[str]
        選択された列名のリスト
    """
    if exclude is None:
        exclude = set()

    options = [col for col in df.columns if col not in exclude]
    default_selection = [col for col in (default or []) if col in options]

    selected = container.multiselect(label, options=options, default=default_selection)

    if not selected and return_all_if_empty:
        return options

    return selected


def show_profile(df: pl.DataFrame, df_test: pl.DataFrame, col_target: str, col_time: str | None = None, verbose: int = 0):
    """
    Examples:
    ```python
    import streamlit as st
    import polars as pl
    from aether import load_inputs, assign_to_namespace
    from aether import show_profile

    st.set_page_config(layout="wide")

    # CSVを一括で読み込み、変数にも割り当てる(これだけではインテリセンスは効かない)
    recs = load_inputs("../input", var_name_map={"train.csv": "df", "test.csv": "df_test"})
    assign_to_namespace(recs, globals()) # df / df_test を生やす（任意）

    # 全部Nullの列はデフォルトではpl.String型にされるので、必要なら直す
    df_test = df_test.with_columns(
        pl.col("US_Stock_GOLD_adj_open").cast(pl.Float64, strict=False),
        pl.col("US_Stock_GOLD_adj_high").cast(pl.Float64, strict=False),
        pl.col("US_Stock_GOLD_adj_low").cast(pl.Float64, strict=False),
        pl.col("US_Stock_GOLD_adj_close").cast(pl.Float64, strict=False),
        pl.col("US_Stock_GOLD_adj_volume").cast(pl.Float64, strict=False),
    )

    show_profile(df, df_test, col_target=None, col_time='date_id')
    ```
    """
    cols = df.columns
    num_cols = len(cols)
    start = time.time()
    # 初期化
    # with st.sidebar.expander('Profiling Status', expanded=True):
    with st.sidebar.container():
        st.markdown("---")  # 水平線
        # st.markdown('**Profiling Status**') # マージンが広い
        st.markdown("<p style='margin:0'><b>Profiling Status</b></p>", unsafe_allow_html=True)
        progress_bar = st.progress(0, text="処理を開始します...")
    for index, col in enumerate(cols):
        elapsed = time.time() - start
        avg = elapsed / index if index > 0 else 2 # 初手はだいたい2秒ぐらいずつと見積もっておく
        eta = avg * (num_cols - index)
        message = f"各列の解析中…  \n表示済の列数: {index} / {num_cols}  \n経過時間: {elapsed:.1f}s  \n平均時間: {avg: .1f}s  \n残り時間: {eta:.1f}s  \n解析中の列番号: {index + 1} / {num_cols}  \n解析中の列名: {col}"
        progress_bar.progress(index / num_cols, text=message)
        show_profile_col(df, df_test, col=col, col_target=col_target, col_time=col_time, key_suffix=index)
    elapsed = time.time() - start
    avg = elapsed / num_cols
    message = f"全列の解析完了  \n表示済の列数: {num_cols} / {num_cols}   \n総時間: {elapsed: .1f}s   \n平均時間: {avg: .1f}s"
    progress_bar.progress(num_cols / num_cols, text=message)
    # time.sleep(1)
    # progress_bar.empty()
    # st.sidebar.info(message)


# @st.cache_data
def show_profile_col(df: pl.DataFrame, df_test: pl.DataFrame, col: str, col_target: str, key_suffix: str, col_time: str | None = None, verbose: int = 0):
    if col_target:
        cols = [col] + ([col_target] if col_target else [])
        df_corr_col = corr_with_target(df.select(pl.col(cols)), col_target=col_target)
        if len(df_corr_col):
            if verbose:
                print('df_corr_col')
                print(df_corr_col)
            corr = df_corr_col.select('abs_corr').item()
            corr_str = f"{corr:.3f}" if corr else '－'
        else:
            corr_str = '－'
    else:
        corr_str = ''
    
    icon = get_dtype_icon(df, df_test, col=col)

    # Title
    title = f"{icon} {col}"
    if corr_str:
        title += f" (corr: {corr_str})"
    st.subheader(title)

    # print(f"col: {col}, schema: {df.schema[col]}")
    col_is_numeric = check_dtype(df, df_test, col=col, selectors=[pl.selectors.numeric()])
    col_target_is_numeric = check_dtype(df, df_test, col=col_target, selectors=[pl.selectors.numeric()]) if col_target else False
    
    st_cols_num = 2 if col_time is None else 3
    st_cols = st.columns(st_cols_num)
    with st_cols[0]:
        # table = aether._draw_profile_table(df, df_test)
        # table = aether.describe_ex(df.select(pl.col(col)))
        # st.dataframe(table)
        comp = describe_compare(df, df_test, feature=col, names=["train","test"])#, stats=stats, sig_digits=2)

        # 列（=DFごと）に色付け
        styler = to_styler_for_streamlit(comp)
        st.table(styler)

    with st_cols[1]:
        chart = plot_histogram_line_after_binning(
            df,
            df_test,
            col_x=col,
            col_y2_line=col_target,
            # col_color='data_name',
            # col_color_scale_mode_hist='domain_range',
            normalize_hist=True,
            verbose=0,
            # available_hist=False,
            # available_line=False,
            )

        st.altair_chart(chart, use_container_width=True, key=f"hist-{col}-{key_suffix}")

    if st_cols_num >= 3:
        with st_cols[2]:
            if col_is_numeric:
                cols_y1=[col]
                cols_y2=[col_target] if col_target_is_numeric else []
                chart = plot_lines_after_binning_dual_axis(
                    df,
                    col_x=col_time,
                    cols_y1=cols_y1, 
                    cols_y2=cols_y2,
                    # col_color='onpromotion',
                    # col_color_scale_mode_line='scheme',
                    # col_color_scale_scheme_line='category10',
                    verbose=0,
                    )

                st.altair_chart(chart, use_container_width=True, key=f"timeline-{col}-{key_suffix}")
