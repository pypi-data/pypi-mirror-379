"""
データ読み込みユーティリティ（Polars前提 / Streamlit非依存）

# 目的
- 指定ディレクトリ配下の CSV を **再帰的** に探索し、Polars で読み込む。
- 表示はせずに、(var_name, path, df) をもつレコード（DatasetRec）の **リスト** として返す。
- 変数名は「マップ優先 → 推論」。重複時は自動で `_<n>` を付番して衝突回避。
- 並び順ルール：
  1) **浅い階層** を優先（ベース直下 → サブフォルダ）
  2) 同階層内では **train → test → その他(相対パスのアルファベット順)**

# よく使う呼び出し例（表示なしでシンプルに使う）
    from loader import load_inputs, assign_to_namespace

    # 読み込み（../input を再帰探索）
    recs = load_inputs("../input", var_name_map={"train.csv": "df", "test.csv": "df_test"})

    # 呼び出し側の **グローバル** に df / df_test などを生やす
    assign_to_namespace(recs, globals())

    # 以降は普通に使える
    # print(df.shape, df_test.shape)

# 補足
- var_name_map のキーは「相対パス（例: 'sub/xx.csv'）, ファイル名, stem」のいずれでも指定可。
- Notebook / Streamlit での表示はそれぞれ `viewer_notebook.py` / `viewer_streamlit.py` を使用。
"""

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Any, List, Dict, Set
import polars as pl


@dataclass
class DatasetRec:
    var_name: str
    path: Path
    df: pl.DataFrame


def _infer_varname(stem: str) -> str:
    s = stem.lower()
    if s == "train":
        return "df"
    if s == "test":
        return "df_test"
    s = re.sub(r"[^0-9a-zA-Z_]", "_", s)
    s = re.sub(r"_{2,}", "_", s).strip("_")
    return f"df_{s}" if s else "df_data"


def _name_priority(stem: str) -> int:
    s = stem.lower()
    if s == "train":
        return 0
    if s == "test":
        return 1
    return 2  # その他


def _pick_mapped_name(mapping: Dict[str, str], base: Path, f: Path) -> str | None:
    rel = f.relative_to(base).as_posix()
    return mapping.get(rel) or mapping.get(f.name) or mapping.get(f.stem)


def load_inputs(
    input_dir: str = "../input",
    var_name_map: Dict[str, str] | None = None,
) -> List[DatasetRec]:
    """
    再帰でCSV探索→Polarsで読み込み→ DatasetRec(var_name, path, df) のリストを返す。
    並び順: 浅い階層 → 同階層では train → test → その他(相対パスのアルファベット)。
    """
    base = Path(input_dir)
    files = sorted(base.rglob("*.csv"))

    def _order_key(f: Path):
        rel = f.relative_to(base)
        depth = len(rel.parts)
        pri = _name_priority(f.stem)
        return (depth, pri, rel.as_posix().lower())

    files.sort(key=_order_key)

    mapping = var_name_map or {}
    used: Set[str] = set()
    recs: List[DatasetRec] = []

    for f in files:
        name = _pick_mapped_name(mapping, base, f) or _infer_varname(f.stem)
        # 衝突回避（_2, _3, ...）
        base_name = name
        i = 2
        while name in used:
            name = f"{base_name}_{i}"
            i += 1

        df = pl.read_csv(str(f))
        recs.append(DatasetRec(name, f, df))
        used.add(name)

    return recs


def assign_to_namespace(records: List[DatasetRec], ns: Dict[str, Any]) -> None:
    """呼び出し側から渡された名前空間（例: globals()）に df を生やす。"""
    for r in records:
        ns[r.var_name] = r.df
