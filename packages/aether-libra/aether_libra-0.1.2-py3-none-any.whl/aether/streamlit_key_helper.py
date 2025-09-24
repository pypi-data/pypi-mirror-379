# st_keys_min.py（ゆるめ版）
def make_key(*parts: str, sep: str = ":") -> str:
    out = []
    for p in parts:
        if not p:
            continue
        s = str(p).strip()
        if s.endswith(sep):  # 誤って "main:" を渡しても二重コロンを防ぐ
            s = s[:-1]
        out.append(s)
    return sep.join(out)
