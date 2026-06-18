#!/usr/bin/env python3
"""Apply fairpari v2 template to casino-bonuses-uz.com HTML pages."""
from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://casino-bonuses-uz.com"
ASSET_V = "20260618v2"
TODAY = "2026-06-18"
SKIP = ("assets", "scripts")


def css_prefix(path: Path) -> str:
    depth = len(path.relative_to(ROOT).parts) - 1
    return "../" * depth if depth else ""


def patch_html(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    orig = text
    prefix = css_prefix(path)

    if 'data-template="v2"' not in text:
        text = text.replace("<html ", '<html data-template="v2" ', 1)

    if "fairpari-v2.css" not in text:
        text = re.sub(
            rf'(<link rel="stylesheet" href="{re.escape(prefix)}css/fairpari-light-theme\.css\?v=[^"]+" />\n)',
            rf'\1<link rel="stylesheet" href="{prefix}css/fairpari-v2.css?v={ASSET_V}" />\n',
            text,
            count=1,
        )

    text = re.sub(r"\?v=202606\d{2}[a-z0-9]*", f"?v={ASSET_V}", text)
    text = text.replace("../css/../assets/", f"{prefix}assets/")
    text = text.replace('href="../css/../assets/', f'href="{prefix}assets/')

    if text != orig:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main():
    n = 0
    for p in ROOT.rglob("*.html"):
        if any(s in p.parts for s in SKIP):
            continue
        if patch_html(p):
            n += 1
            print("patched:", p.relative_to(ROOT))
    print(f"Done: {n} files patched")


if __name__ == "__main__":
    main()
