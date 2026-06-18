#!/usr/bin/env python3
"""Full SEO audit for UZ bonus sites — run from any site root or pass paths."""
from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

BOBAFFS = "bobaffs.org/click?o=1603&a=189"
LEGAL_MARKERS = (
    "cookie", "politika", "maxfiylik", "foydalanish", "masuliyat",
    "usloviya", "terms", "privacy", "responsible", "otvetstvennaya",
)


def strip_html(html: str) -> str:
    html = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.S | re.I)
    html = re.sub(r"<style[^>]*>.*?</style>", "", html, flags=re.S | re.I)
    return re.sub(r"<[^>]+>", " ", html)


def word_count(html: str) -> int:
    return len(strip_html(html).split())


def meta(html: str, name: str) -> str:
    m = re.search(
        rf'<meta[^>]+name="{re.escape(name)}"[^>]+content="([^"]*)"',
        html,
        re.I,
    )
    if not m:
        m = re.search(
            rf'<meta[^>]+content="([^"]*)"[^>]+name="{re.escape(name)}"',
            html,
            re.I,
        )
    return m.group(1) if m else ""


def og(html: str, prop: str) -> str:
    m = re.search(
        rf'<meta[^>]+property="{re.escape(prop)}"[^>]+content="([^"]*)"',
        html,
        re.I,
    )
    return m.group(1) if m else ""


def canonical(html: str) -> str:
    m = re.search(r'<link rel="canonical" href="([^"]+)"', html, re.I)
    return m.group(1) if m else ""


def title_tag(html: str) -> str:
    m = re.search(r"<title>([^<]+)</title>", html, re.I)
    return m.group(1).strip() if m else ""


def h1s(html: str) -> list[str]:
    return [re.sub(r"\s+", " ", x).strip() for x in re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.S | re.I)]


def hreflangs(html: str) -> dict[str, str]:
    out = {}
    for m in re.finditer(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', html, re.I):
        out[m.group(1)] = m.group(2)
    return out


def has_v2(html: str) -> bool:
    return 'data-template="v2"' in html and "fairpari-v2.css" in html or "rating" in html


def audit_site(root: Path, domain: str) -> dict:
    issues: list[dict] = []
    pages: list[dict] = []
    titles: Counter = Counter()

    html_files = sorted(root.rglob("*.html"))
    for fp in html_files:
        rel = str(fp.relative_to(root))
        html = fp.read_text(encoding="utf-8", errors="ignore")
        is_legal = any(x in rel.lower() for x in LEGAL_MARKERS)
        wc = word_count(html)
        tit = title_tag(html)
        titles[tit] += 1
        partner_ok = BOBAFFS in html or (is_legal and "js-go-partner" not in html)
        if "js-go-partner" in html and BOBAFFS not in (fp.parent / ".." / "js" / "partner.js").resolve().read_text(errors="ignore") if (fp.parent / ".." / "js" / "partner.js").resolve().exists() else "":
            pj = root / "js" / "partner.js"
            if pj.exists() and BOBAFFS not in pj.read_text(errors="ignore"):
                partner_ok = False

        pj = root / "js" / "partner.js"
        if "js-go-partner" in html and pj.exists():
            partner_ok = BOBAFFS in pj.read_text(errors="ignore")

        page = {
            "path": rel,
            "words": wc,
            "title_len": len(tit),
            "title": tit[:80],
            "canonical": canonical(html),
            "h1": h1s(html)[:2],
            "v2": 'data-template="v2"' in html,
            "legal": is_legal,
            "has_cta": "js-go-partner" in html,
        }
        pages.append(page)

        if not is_legal and wc < 2000 and "index.html" in rel:
            issues.append({"p": "P1", "path": rel, "issue": f"thin content {wc} words"})
        if tit and (len(tit) < 30 or len(tit) > 65):
            issues.append({"p": "P2", "path": rel, "issue": f"title length {len(tit)}: {tit[:50]}"})
        if "fairpari-casino-bonus" in tit.lower() or "casino-bonuses-uz.com" in tit.lower():
            issues.append({"p": "P2", "path": rel, "issue": "domain in title"})
        h1_text = " ".join(h1s(html))
        if rel.startswith("ru/") and re.search(r"[oʻ'`]|O'zbekiston|Ro'yxat", h1_text):
            issues.append({"p": "P0", "path": rel, "issue": "UZ chars in RU H1"})
        if rel.startswith("en/") and re.search(r"[oʻ'`]|O'zbekiston|Ro'yxat|Bosh sahifa", h1_text):
            issues.append({"p": "P0", "path": rel, "issue": "UZ chars in EN H1"})
        if h1_text and tit and h1_text.lower()[:20] not in tit.lower() and tit.lower()[:20] not in h1_text.lower():
            if is_legal and "policy" in tit.lower() and "policy" not in h1_text.lower():
                issues.append({"p": "P0", "path": rel, "issue": f"title/H1 mismatch: {tit[:40]} vs {h1_text[:40]}"})

    dup_titles = [(t, c) for t, c in titles.items() if c > 1 and t]
    sm = root / "sitemap.xml"
    sm_html_urls = []
    if sm.exists():
        sm_html_urls = re.findall(r"<loc>([^<]+\.html[^<]*)</loc>", sm.read_text())

    pj = root / "js" / "partner.js"
    partner_file_ok = pj.exists() and BOBAFFS in pj.read_text(errors="ignore")

    cluster_pages = [p for p in pages if not p["legal"] and p["path"].endswith("index.html")]
    under_2500 = [p for p in cluster_pages if p["words"] < 2500]

    return {
        "domain": domain,
        "root": str(root),
        "page_count": len(pages),
        "cluster_count": len(cluster_pages),
        "under_2500": under_2500,
        "v2_pages": sum(1 for p in pages if p["v2"]),
        "partner_js_ok": partner_file_ok,
        "sitemap_html_ext": sm_html_urls,
        "dup_titles": dup_titles[:10],
        "issues": issues[:80],
        "issue_counts": dict(Counter(i["p"] for i in issues)),
        "avg_words_cluster": round(sum(p["words"] for p in cluster_pages) / max(1, len(cluster_pages))),
    }


def main():
    sites = [
        (Path("/Users/vv/Desktop/fairpari-casino-bonus"), "fairpari-casino-bonus.com"),
        (Path("/Users/vv/Desktop/fairpari-casino-bonuses"), "fairpari-casino-bonuses.com"),
        (Path("/Users/vv/Desktop/casino-bonuses-uz"), "casino-bonuses-uz.com"),
    ]
    if len(sys.argv) > 1:
        sites = [(Path(sys.argv[1]), sys.argv[2])]
    results = []
    for root, domain in sites:
        if not root.exists():
            print(f"SKIP {domain} — not found")
            continue
        r = audit_site(root, domain)
        results.append(r)
        print(f"\n=== {domain} ===")
        print(f"pages={r['page_count']} cluster={r['cluster_count']} avg_words={r['avg_words_cluster']}")
        print(f"v2={r['v2_pages']} partner_js={r['partner_js_ok']} P0={r['issue_counts'].get('P0',0)} P1={r['issue_counts'].get('P1',0)}")
        print(f"under_2500: {len(r['under_2500'])}")
        if r["sitemap_html_ext"]:
            print(f"sitemap .html URLs: {len(r['sitemap_html_ext'])}")
        if r["dup_titles"]:
            print(f"dup titles: {r['dup_titles'][:3]}")
        for p in r["under_2500"][:8]:
            print(f"  {p['words']}w {p['path']}")
        for i in [x for x in r["issues"] if x["p"] == "P0"][:8]:
            print(f"  P0 {i['path']}: {i['issue']}")

    out = Path("/Users/vv/Desktop/Cursor/18.06.2026/otchety/seo-audit-3-sites/audit-data-18-06.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nWrote {out}")


if __name__ == "__main__":
    main()
