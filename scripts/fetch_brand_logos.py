#!/usr/bin/env python3
"""Fetch/copy real operator logos into assets/logos/brands/."""
from __future__ import annotations

import shutil
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets/logos/brands"
PROMETEY_OPS = Path("/Users/vv/Desktop/prometey-b/assets/operators")

COPY_FROM_PROMETEY = {
    "1win": "1win.svg",
    "1xbet": "1xbet.svg",
    "mostbet": "mostbet.svg",
    "melbet": "melbet.svg",
    "pin-up": "pin-up.svg",
    "betwinner": "betwinner.svg",
    "leon": "leon.svg",
    "parimatch": "parimatch.svg",
}

# Google favicon / clearbit fallback domains
FETCH_DOMAINS = {
    "fairpari": "fairpari.com",
    "linebet": "linebet.com",
    "megapari": "megapari.com",
    "22bet": "22bet.com",
    "fonbet": "fonbet.com",
    "marathonbet": "marathonbet.com",
    "betway": "betway.com",
    "spinbetter": "spinbetter.com",
    "vulkan-vegas": "vulkanvegas.com",
    "joycasino": "joycasino.com",
    "fresh-casino": "fresh.casino",
    "bc-game": "bc.game",
}

CARD_SVG_WRAP = '''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="64" height="64" viewBox="0 0 64 64" role="img" aria-label="{label}">
<rect width="64" height="64" rx="12" fill="#ffffff"/>
<image xlink:href="data:image/png;base64,{b64}" x="4" y="4" width="56" height="56" preserveAspectRatio="xMidYMid meet"/>
</svg>'''


def fetch_png_b64(domain: str) -> str | None:
    import base64

    for url in (
        f"https://www.google.com/s2/favicons?domain={domain}&sz=128",
        f"https://logo.clearbit.com/{domain}",
    ):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = resp.read()
                if len(data) > 200:
                    return base64.b64encode(data).decode("ascii")
        except Exception:
            continue
    return None


def wrap_fairpari():
    src = ROOT / "assets/logo-fairpari.svg"
    if src.exists():
        shutil.copy2(src, OUT / "fairpari.svg")
        print("fairpari: logo-fairpari.svg")


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    wrap_fairpari()

    for slug, fname in COPY_FROM_PROMETEY.items():
        src = PROMETEY_OPS / fname
        if src.exists():
            shutil.copy2(src, OUT / f"{slug}.svg")
            print(f"{slug}: prometey {fname}")
        else:
            print(f"{slug}: MISSING {src}")

    for slug, domain in FETCH_DOMAINS.items():
        if slug == "fairpari" and (OUT / "fairpari.svg").exists():
            continue
        b64 = fetch_png_b64(domain)
        if b64:
            (OUT / f"{slug}.svg").write_text(
                CARD_SVG_WRAP.format(label=slug, b64=b64), encoding="utf-8"
            )
            print(f"{slug}: fetched {domain}")
        else:
            print(f"{slug}: FAILED {domain}")


if __name__ == "__main__":
    main()
