from IPython.display import display, Markdown

import polars as pl

import os
import json
import hashlib
import functools
import inspect
import ast
import datetime
from pathlib import Path
from typing import Callable


# --- 設定 ---
CACHE_POLARS_ENABLED = os.getenv("CACHE_POLARS_ENABLED", "1").strip().lower() in ("1", "true", "on")
CACHE_POLARS_DIR = Path(os.getenv("CACHE_POLARS_DIR", "./cache"))
if CACHE_POLARS_ENABLED:
    CACHE_POLARS_DIR.mkdir(exist_ok=True)


# --- メインデコレータ ---
"""
cache_polarsデコレータ（Polars DataFrame / Parquet専用）
"""
def cache_polars(func: Callable = None, *, expire_days: int | None = None, reset_hour: int | None = None):
    """
    PolarsのDataFrameをParquet形式でキャッシュするデコレータ。
    - 戻り値は pl.DataFrame 限定。
    - 保存形式は .parquet のみ。
    - 環境変数で有効期限や基準時刻を調整可能。

    環境変数の例 (.env):
        # キャッシュを有効にするかどうか (1: 有効, 0: 無効)
        CACHE_POLARS_ENABLED=1

        # キャッシュ用のフォルダパス
        CACHE_POLARS_DIR=./cache

        # キャッシュの有効期限（日数）
        #   -1 の場合は無期限
        CACHE_POLARS_EXPIRE_DAYS=-1

        # キャッシュ有効期限の基準時刻
        #   指定時刻直前のファイル更新を起点に有効期限を判定
        #   -1 の場合は指定なし
        CACHE_POLARS_RESET_HOUR=-1
    
    使用例:
        ```python
        @cache_polars
        def some_function() -> pl.DataFrame:
            ...
        ```
    """
    def decorator(inner_func: Callable):
        @functools.wraps(inner_func)
        def wrapper(*args, **kwargs):
            # --- ハッシュキー作成 ---
            key_hash = _make_cache_key(inner_func, args, kwargs)
            func_name = inner_func.__name__
            base_filename = _make_cache_filename(func_name, key_hash)

            # --- 有効期限設定 ---
            expire = expire_days if expire_days is not None else int(os.getenv("CACHE_POLARS_EXPIRE_DAYS", "-1"))
            reset_env = os.getenv("CACHE_POLARS_RESET_HOUR", "-1").strip()
            reset = reset_hour if reset_hour is not None else (None if int(reset_env) < 0 else int(reset_env))

            # --- キャッシュファイル検索（ts無視） ---
            matched_files = list(CACHE_POLARS_DIR.glob(f"{func_name}_*_{key_hash}.parquet"))
            if CACHE_POLARS_ENABLED and matched_files:
                path = max(matched_files, key=os.path.getmtime)
                if _is_cache_valid(path, expire, reset):
                    print(f"[Cache HIT] {path}")
                    return pl.read_parquet(path)
                else:
                    print(f"[Cache EXPIRED] {path}")

            # --- 実行・保存 ---
            result = inner_func(*args, **kwargs)
            if not isinstance(result, pl.DataFrame):
                raise TypeError("[Cache SAVE ERROR] Only pl.DataFrame is supported.")
            _save_result(base_filename, result)
            return result

        return wrapper

    return decorator if func is None else decorator(func)

# --- キャッシュファイル名作成関数(＝命名規約。他の処理でもこれを前提としている) ---
def _make_cache_filename(func_name: str, key_hash: str) -> str:
    """
    関数名とハッシュからキャッシュファイル名を生成。
    キー部分は最初の関数名と、最後の関数コード＋引数のハッシュ部分。
    参考情報として作成日時を間に入れてる。
    例: funcname_20250808_1230_abcd1234.parquet
    """
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    return f"{func_name}_{ts}_{key_hash}"

# --- 有効期限チェック関数 ---
def _is_cache_valid(path: Path, expire_days: int, reset_hour: int | None) -> bool:
    # --- 無期限なら常に有効 ---
    if expire_days < 0:
        return True

    # --- ファイルの更新時刻（キャッシュ生成時刻） ---
    mtime = datetime.datetime.fromtimestamp(path.stat().st_mtime)

    # --- 現在時刻 ---
    now = datetime.datetime.now()

    # --- 基準時刻がない場合は「mtimeからの経過日数」で判定 ---
    if reset_hour is None:
        # 例: 有効期限1日 → 24時間以内なら有効
        return (now - mtime) <= datetime.timedelta(days=expire_days)

    # --- 基準時刻がある場合のロジック ---
    # キャッシュ作成日の reset_hour を基準にする
    base = mtime.replace(hour=reset_hour, minute=0, second=0, microsecond=0)
    # mtime が reset_hour より前なら、基準日は前日の reset_hour にする
    if mtime < base:
        base -= datetime.timedelta(days=1)

    expiry_time = base + datetime.timedelta(days=expire_days)
    return now <= expiry_time

# --- 結果保存（古いファイル削除 + エラー時raise） ---
def _save_result(base_filename: str, result: pl.DataFrame):
    path = CACHE_POLARS_DIR / f"{base_filename}.parquet"

    # base_filename = funcname_YYYYMMDD_HHMM_hash
    try:
        prefix, _, key_hash = base_filename.rsplit("_", 2)
    except ValueError:
        print(f"[Cache SAVE WARNING] Invalid base_filename format: {base_filename}")
        prefix = base_filename
        key_hash = None

    # 古い同一キーのファイルを削除（同じ関数名・同じハッシュ）
    if key_hash:
        pattern = f"{prefix}_*_{key_hash}.parquet"
        for old_path in CACHE_POLARS_DIR.glob(pattern):
            try:
                old_path.unlink()
                print(f"[Cache DELETED] {old_path}")
            except Exception as e:
                print(f"[Cache DELETE FAILED] {old_path}: {e}")

    try:
        result.write_parquet(path)
        print(f"[Cache SAVED] {path}")
    except Exception as e:
        print(f"[Cache SAVE FAILED] {path}: {e}")
        raise

# --- ソースコードの正規化 ---
def _get_clean_source(func) -> str:
    try:
        source = inspect.getsource(func)
        parsed = ast.parse(source)
        return ast.unparse(parsed)
    except Exception:
        return "unavailable"

# --- ハッシュキー作成 ---
def _make_cache_key(func, args, kwargs) -> str:
    src = _get_clean_source(func)
    ser_args = _serialize(args)
    ser_kwargs = _serialize(kwargs)
    content = json.dumps({"source": src, "args": ser_args, "kwargs": ser_kwargs}, sort_keys=True)
    return hashlib.sha256(content.encode("utf-8")).hexdigest()

# --- 引数のシリアライズ ---
def _serialize(obj):
    if isinstance(obj, (str, int, float, bool, type(None))):
        return obj
    elif isinstance(obj, (list, tuple)):
        return [_serialize(x) for x in obj]
    elif isinstance(obj, dict):
        return {str(k): _serialize(v) for k, v in obj.items()}
    elif isinstance(obj, pl.DataFrame):
        return {
            "shape": obj.shape,
            "columns": obj.columns,
            "dtypes": [str(dt) for dt in obj.dtypes],
            "sample_hash": _hash_head_tail(obj)
        }
    else:
        return str(obj)

# --- head/tailのみの簡易ハッシュ ---
def _hash_head_tail(df: pl.DataFrame, n=5) -> str:
    sample = pl.concat([df.head(n), df.tail(n)], how="vertical")
    return hashlib.sha256(sample.write_csv().encode()).hexdigest()
