#!/usr/bin/env python3
"""Rebuild legal *.html shells with unified header, footer, sticky, CSS."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from build_rating_site import CSS_V, DOMAIN, footer_block, head_block  # noqa: E402

LEGAL = [
    ("maxfiylik-siyosati.html", "uz", "https://casino-bonuses-uz.com/maxfiylik-siyosati",
     "https://casino-bonuses-uz.com/maxfiylik-siyosati", "https://casino-bonuses-uz.com/ru/politika-konfidentsialnosti"),
    ("foydalanish-shartlari.html", "uz", "https://casino-bonuses-uz.com/foydalanish-shartlari",
     "https://casino-bonuses-uz.com/foydalanish-shartlari", "https://casino-bonuses-uz.com/ru/usloviya-ispolzovaniya"),
    ("cookie-siyosati.html", "uz", "https://casino-bonuses-uz.com/cookie-siyosati",
     "https://casino-bonuses-uz.com/cookie-siyosati", "https://casino-bonuses-uz.com/ru/politika-cookie"),
    ("masuliyatli-oyin.html", "uz", "https://casino-bonuses-uz.com/masuliyatli-oyin",
     "https://casino-bonuses-uz.com/masuliyatli-oyin", "https://casino-bonuses-uz.com/ru/otvetstvennaya-igra"),
    ("ru/politika-konfidentsialnosti.html", "ru", "https://casino-bonuses-uz.com/ru/politika-konfidentsialnosti",
     "https://casino-bonuses-uz.com/maxfiylik-siyosati", "https://casino-bonuses-uz.com/ru/politika-konfidentsialnosti"),
    ("ru/usloviya-ispolzovaniya.html", "ru", "https://casino-bonuses-uz.com/ru/usloviya-ispolzovaniya",
     "https://casino-bonuses-uz.com/foydalanish-shartlari", "https://casino-bonuses-uz.com/ru/usloviya-ispolzovaniya"),
    ("ru/politika-cookie.html", "ru", "https://casino-bonuses-uz.com/ru/politika-cookie",
     "https://casino-bonuses-uz.com/cookie-siyosati", "https://casino-bonuses-uz.com/ru/politika-cookie"),
    ("ru/otvetstvennaya-igra.html", "ru", "https://casino-bonuses-uz.com/ru/otvetstvennaya-igra",
     "https://casino-bonuses-uz.com/masuliyatli-oyin", "https://casino-bonuses-uz.com/ru/otvetstvennaya-igra"),
]


def _meta(html: str, tag: str) -> str:
    if tag == "title":
        m = re.search(r"<title>([^<]+)</title>", html, re.I)
    else:
        m = re.search(rf'<meta name="{tag}" content="([^"]*)"', html, re.I)
    return m.group(1).strip() if m else ""


def _main(html: str) -> str:
    m = re.search(r"(<main id=\"main\"[^>]*>.*?</main>)", html, re.DOTALL | re.I)
    if not m:
        raise ValueError("main block not found")
    return m.group(1)


def _ld_json(html: str) -> str:
    blocks = re.findall(
        r'<script type="application/ld\+json">.*?</script>',
        html,
        re.DOTALL | re.I,
    )
    return "\n".join(blocks)


def patch(path: Path, lang: str, canonical: str, href_uz: str, href_ru: str) -> None:
    raw = path.read_text(encoding="utf-8")
    title = _meta(raw, "title")
    desc = _meta(raw, "description")
    main = _main(raw)
    extra_head = _ld_json(raw)
    if extra_head:
        extra_head = extra_head + "\n"
    page = (
        f"{head_block(lang, title, desc, canonical, href_uz=href_uz, href_ru=href_ru, depth=0, extra_head=extra_head)}"
        f"{main}\n"
        f"{footer_block(lang, depth=0)}"
    )
    path.write_text(page, encoding="utf-8")
    print("legal:", path.relative_to(ROOT))


def main():
    for rel, lang, canonical, href_uz, href_ru in LEGAL:
        patch(ROOT / rel, lang, canonical, href_uz, href_ru)


if __name__ == "__main__":
    main()
