#!/usr/bin/env python3
"""Regenerate sitemap.xml with lastmod for all 6 desktop sites."""
from __future__ import annotations
from datetime import datetime
from pathlib import Path
import re

SITES = {
    "casino-bonuses-uz.com": {
        "root": Path("/Users/vv/Desktop/casino-bonuses-uz"),
        "domain": "https://casino-bonuses-uz.com",
        "legal_clean": True,
    },
    "fairpari-casino-bonus.com": {
        "root": Path("/Users/vv/Desktop/fairpari-casino-bonus"),
        "domain": "https://fairpari-casino-bonus.com",
        "legal_clean": True,
    },
    "fairpari-casino-bonuses.com": {
        "root": Path("/Users/vv/Desktop/fairpari-casino-bonuses"),
        "domain": "https://fairpari-casino-bonuses.com",
        "legal_clean": False,
    },
    "fairpari-casino-uz.com": {
        "root": Path("/Users/vv/Desktop/fairpari-casino"),
        "domain": "https://fairpari-casino-uz.com",
        "legal_clean": False,
    },
    "dawo.uz": {
        "root": Path("/Users/vv/Desktop/dawo-uz"),
        "domain": "https://dawo.uz",
        "legal_clean": False,
    },
    "prometey-b.kz": {
        "root": Path("/Users/vv/Desktop/ofk-cmd-aviator"),
        "domain": "https://prometey-b.kz",
        "legal_clean": False,
    },
}

SKIP = re.compile(r"google|assets|node_modules| 2/", re.I)
LEGAL = re.compile(
    r"cookie|privacy|maxfiylik|masuliyat|otvetstv|usloviya|foydalanish|politika|terms|responsible|konfidents",
    re.I,
)


def lastmod(f: Path) -> str:
    return datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d")


def priority(loc: str) -> str:
    if loc.rstrip("/").endswith((".com", ".uz", ".kz")):
        return "1.0"
    if "/ru/" in loc and loc.rstrip("/").endswith("/ru"):
        return "1.0"
    if "/en/" in loc and loc.rstrip("/").endswith("/en"):
        return "1.0"
    if "/kk/" in loc and loc.rstrip("/").endswith("/kk"):
        return "1.0"
    if LEGAL.search(loc):
        return "0.3"
    return "0.8"


def collect_entries(root: Path, domain: str, legal_clean: bool) -> list[tuple[str, str, str]]:
    entries: list[tuple[str, str, str]] = []
    for f in sorted(root.rglob("*.html")):
        rel = str(f.relative_to(root))
        if SKIP.search(rel):
            continue
        if rel == "index.html":
            loc = f"{domain}/"
        elif rel.endswith("/index.html"):
            loc = f"{domain}/{rel[:-11]}/"
        elif legal_clean and rel.endswith(".html"):
            loc = f"{domain}/{rel[:-5]}"
        else:
            loc = f"{domain}/{rel}"
        entries.append((loc, lastmod(f), rel))
    # stable sort: home first, then alpha
    entries.sort(key=lambda x: (0 if x[0].rstrip("/").endswith((".com", ".uz", ".kz")) else 1, x[0]))
    return entries


def write_sitemap(cfg: dict) -> int:
    root: Path = cfg["root"]
    domain: str = cfg["domain"]
    entries = collect_entries(root, domain, cfg.get("legal_clean", False))
    seen: set[str] = set()
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    count = 0
    for loc, lm, _ in entries:
        if loc in seen:
            continue
        seen.add(loc)
        pri = priority(loc)
        lines.append(f"  <url><loc>{loc}</loc><lastmod>{lm}</lastmod><priority>{pri}</priority></url>")
        count += 1
    lines.append("</urlset>")
    out = root / "sitemap.xml"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{domain}: {count} urls → {out}")
    return count


def main():
    for name, cfg in SITES.items():
        if not cfg["root"].exists():
            print(f"SKIP {name}: not found")
            continue
        write_sitemap(cfg)


if __name__ == "__main__":
    main()
