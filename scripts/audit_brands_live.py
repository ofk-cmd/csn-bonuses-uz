#!/usr/bin/env python3
"""Live audit of official brand sites — product type, nav, license, bonuses (Playwright/Chromium)."""
from __future__ import annotations

import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brand_qttk_content import META  # noqa: E402
from build_rating_site import BRANDS  # noqa: E402

SPORT_KW = re.compile(
    r"\b(sport|sports|stavk|betting|line|live\s*bet|prematch|esport|cyber|"
    r"спорт|ставк|букмекер|линия|киберспорт)\b",
    re.I,
)
CASINO_KW = re.compile(
    r"\b(casino|kazino|slot|slots|live\s*casino|games|crash|aviator|"
    r"казино|слот|игр|live\s*казино|рулетк|покер|блэкджек)\b",
    re.I,
)
LICENSE_KW = re.compile(
    r"(curacao|curaçao|mga|malta|anjouan|kahnawake|license|licen[cs]e|"
    r"litsenz|ogl/\d|gambling\s*commission|регулятор)",
    re.I,
)
BONUS_KW = re.compile(r"\b(bonus|welcome|promo|freespin|фриспин|бонус|акци)\b", re.I)
PAY_KW = re.compile(
    r"\b(humo|uzcard|payme|click|usdt|btc|crypto|visa|mastercard|"
    r"master\s*card|uzs|сум)\b",
    re.I,
)


def norm_domain(site: str) -> str:
    s = site.strip().rstrip("/")
    if not s.startswith("http"):
        s = "https://" + s
    return s


def same_operator(url: str, site: str, brand_name: str = "") -> bool:
    a = urlparse(url).netloc.lower().replace("www.", "")
    b = urlparse(norm_domain(site)).netloc.lower().replace("www.", "")
    if a == b or a.endswith("." + b) or b.endswith("." + a):
        return True
    brand = brand_name.lower().replace(" ", "").replace(".", "").replace("-", "")
    brand_tokens = [
        brand,
        brand.replace("casino", ""),
        "1xbet" if brand == "1xbet" else "",
        "1win" if brand == "1win" else "",
        "22bet" if "22bet" in brand else "",
        "bcgame" if brand == "bcgame" else "",
        "vulkanvegas" if "vulkan" in brand else "",
        "freshcasino" if "fresh" in brand else "",
    ]
    for tok in brand_tokens:
        if tok and tok in a.replace("-", "").replace(".", ""):
            return True
    # common mirror TLDs for BK clones
    mirror_markers = ("fairpari", "melbet", "betwinner", "megapari", "22bet", "22bt", "parimatch", "fonbet")
    for m in mirror_markers:
        if m in b.replace("-", "") and m in a.replace("-", ""):
            return True
    return False


def extract_links(page) -> list[dict]:
    return page.evaluate(
        """() => {
        const out = [];
        for (const a of document.querySelectorAll('a[href]')) {
          const t = (a.innerText || a.textContent || '').trim().replace(/\\s+/g, ' ');
          const href = a.href;
          if (!href || href.startsWith('javascript:')) continue;
          if (t.length > 80) continue;
          out.push({text: t, href});
        }
        return out;
    }"""
    )


def extract_meta(page) -> dict:
    return page.evaluate(
        """() => ({
        title: document.title || '',
        description: (document.querySelector('meta[name="description"]') || {}).content || '',
        lang: document.documentElement.lang || '',
        h1: (document.querySelector('h1') || {}).innerText || '',
    })"""
    )


def footer_text(page) -> str:
    return page.evaluate(
        """() => {
        const f = document.querySelector('footer');
        if (f) return (f.innerText || '').slice(0, 4000);
        const nodes = [...document.querySelectorAll('body *')].slice(-40);
        return nodes.map(n => n.innerText || '').join(' ').slice(-3000);
    }"""
    )


def body_sample(page) -> str:
    return page.evaluate(
        """() => (document.body.innerText || '').replace(/\\s+/g, ' ').slice(0, 12000)"""
    )


def classify_links(links: list[dict], base_url: str) -> dict:
    sport_hits, casino_hits = [], []
    for item in links:
        blob = f"{item.get('text','')} {item.get('href','')}"
        if SPORT_KW.search(blob):
            sport_hits.append(item)
        if CASINO_KW.search(blob):
            casino_hits.append(item)
    # dedupe by href
    def dedupe(items):
        seen = set()
        out = []
        for it in items:
            h = it.get("href", "")
            if h in seen:
                continue
            seen.add(h)
            out.append(it)
        return out[:25]

    return {
        "sport_nav": dedupe(sport_hits),
        "casino_nav": dedupe(casino_hits),
    }


def product_type(sport_nav: list, casino_nav: list, body: str) -> str:
    has_sport = bool(sport_nav) or bool(SPORT_KW.search(body[:8000]))
    has_casino = bool(casino_nav) or bool(CASINO_KW.search(body[:8000]))
    if has_sport and has_casino:
        return "both"
    if has_casino:
        return "casino"
    if has_sport:
        return "bk"
    return "unknown"


ALT_URLS = {
    "pin-up": ["https://pin-up.world/", "https://pin-up.com/"],
    "fresh-casino": ["https://fresh.casino/en", "https://fresh8.casino/"],
    "betway": ["https://betway.com/en/sports", "https://sports.betway.com/"],
    "parimatch": ["https://parimatch.com/en"],
    "fonbet": ["https://fonbet.com/"],
}


def audit_brand(page, b: dict, rank: int) -> dict:
    slug = b["slug"]
    meta = META.get(slug, META["1win"])
    start_url = norm_domain(meta["site"])
    result = {
        "rank": rank,
        "slug": slug,
        "name": b["name"],
        "rating_site_type": b["type"],
        "official_url_requested": start_url,
        "final_url": "",
        "load_status": "ok",
        "redirect_off_domain": False,
        "title": "",
        "meta_description": "",
        "page_lang": "",
        "h1": "",
        "product_type_live": "unknown",
        "has_sport_section": False,
        "has_casino_section": False,
        "sport_nav_samples": [],
        "casino_nav_samples": [],
        "license_snippets": [],
        "bonus_snippets": [],
        "payment_mentions": [],
        "registration_hints": [],
        "app_hints": [],
        "footer_excerpt": "",
        "body_excerpt": "",
        "notes": [],
        "checked_at": datetime.now().isoformat(timespec="seconds"),
    }

    start_urls = [norm_domain(meta["site"])] + ALT_URLS.get(slug, [])

    try:
        resp = None
        final = ""
        for attempt_url in start_urls:
            try:
                resp = page.goto(attempt_url, wait_until="domcontentloaded", timeout=60000)
            except Exception as nav_err:
                err_s = str(nav_err)
                if "interrupted" not in err_s and "ERR_" not in err_s:
                    if attempt_url == start_urls[-1]:
                        raise
                    continue
                result["notes"].append(err_s[:180])
                resp = None
            time.sleep(3)
            try:
                page.wait_for_load_state("networkidle", timeout=15000)
            except Exception:
                pass
            time.sleep(1)
            final = page.url
            if final.startswith("chrome-error"):
                if attempt_url != start_urls[-1]:
                    continue
                result["load_status"] = "error"
                result["notes"].append("Browser error page after navigation")
                return result
            if resp and resp.status == 403 and attempt_url != start_urls[-1]:
                continue
            title_now = page.title() or ""
            body_now = body_sample(page)
            if "cloudflare" in title_now.lower() and "blocked" in body_now.lower():
                if attempt_url != start_urls[-1]:
                    continue
            break

        result["official_url_requested"] = start_urls[0]
        if len(start_urls) > 1 and final and not final.startswith(start_urls[0].rstrip("/")):
            result["notes"].append(f"Alternate URL used from list: tried {len(start_urls)} variants")
        result["final_url"] = final
        if not same_operator(final, meta["site"], b["name"]):
            result["redirect_off_domain"] = True
            result["load_status"] = "redirect_mirror"
            result["notes"].append(f"Working mirror/workflow domain: {final}")
            # continue audit on mirror — content is still operator UI

        if resp and resp.status >= 400:
            result["load_status"] = f"http_{resp.status}"
            result["notes"].append(f"HTTP status {resp.status}")

        meta_info = extract_meta(page)
        result.update(
            {
                "title": meta_info.get("title", ""),
                "meta_description": meta_info.get("description", ""),
                "page_lang": meta_info.get("lang", ""),
                "h1": meta_info.get("h1", ""),
            }
        )

        links = extract_links(page)
        classified = classify_links(links, final)
        result["sport_nav_samples"] = [
            {"text": x["text"], "href": x["href"]} for x in classified["sport_nav"][:12]
        ]
        result["casino_nav_samples"] = [
            {"text": x["text"], "href": x["href"]} for x in classified["casino_nav"][:12]
        ]

        body = body_sample(page)
        foot = footer_text(page)
        result["body_excerpt"] = body[:2500]
        result["footer_excerpt"] = foot[:1500]

        ptype = product_type(classified["sport_nav"], classified["casino_nav"], body)
        result["product_type_live"] = ptype
        result["has_sport_section"] = ptype in ("both", "bk")
        result["has_casino_section"] = ptype in ("both", "casino")

        for m in LICENSE_KW.finditer(foot + " " + body[:6000]):
            start = max(0, m.start() - 60)
            end = min(len(foot + body), m.end() + 120)
            snippet = (foot + body)[start:end].strip()
            if snippet and snippet not in result["license_snippets"]:
                result["license_snippets"].append(snippet[:220])
            if len(result["license_snippets"]) >= 5:
                break

        for m in BONUS_KW.finditer(body[:9000]):
            start = max(0, m.start() - 40)
            end = min(len(body), m.end() + 140)
            snippet = body[start:end].strip()
            if len(snippet) > 25 and snippet not in result["bonus_snippets"]:
                result["bonus_snippets"].append(snippet[:240])
            if len(result["bonus_snippets"]) >= 8:
                break

        pays = set(PAY_KW.findall(body[:10000] + " " + foot))
        result["payment_mentions"] = sorted({p.lower() for p in pays})

        reg_links = [
            x for x in links
            if re.search(r"regist|sign\s*up|join|ro'yxat|регист", x.get("text", "") + x.get("href", ""), re.I)
        ]
        result["registration_hints"] = [
            {"text": x["text"], "href": x["href"]} for x in reg_links[:8]
        ]

        app_links = [
            x for x in links
            if re.search(r"app|apk|android|ios|download|mobile|ilova|прилож", x.get("text", "") + x.get("href", ""), re.I)
        ]
        result["app_hints"] = [
            {"text": x["text"], "href": x["href"]} for x in app_links[:8]
        ]

        # mismatch with our rating card type
        if b["type"] != ptype and ptype != "unknown":
            result["notes"].append(
                f"Rating site lists type={b['type']}, live audit={ptype}"
            )

    except Exception as e:
        result["load_status"] = "error"
        result["notes"].append(str(e)[:300])

    return result


def main():
    out_dir = Path("/Users/vv/Desktop/Cursor/18.06.2026/otchety/casino-bonuses-uz")
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "brand-live-audit.json"
    md_path = out_dir / "brand-live-dossier.md"
    csv_path = out_dir / "brand-live-audit.csv"

    from playwright.sync_api import sync_playwright

    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            locale="ru-RU",
            timezone_id="Asia/Tashkent",
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1440, "height": 900},
            extra_http_headers={
                "Accept-Language": "ru-RU,ru;q=0.9,uz-UZ;q=0.8,en;q=0.7",
            },
        )
        page = context.new_page()
        for i, b in enumerate(BRANDS, 1):
            print(f"[{i}/20] {b['name']}...", flush=True)
            results.append(audit_brand(page, b, i))
            # isolate brands — shared cookies cause cross-redirects between BK clones
            context.clear_cookies()
            try:
                page.goto("about:blank", timeout=5000)
            except Exception:
                pass
        browser.close()

    json_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")

    # CSV summary
    import csv

    with csv_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow([
            "rank", "name", "official_url", "final_url", "load_status",
            "product_type_live", "has_sport", "has_casino",
            "rating_site_type", "match", "payments", "license_count", "bonus_count",
        ])
        for r in results:
            w.writerow([
                r["rank"], r["name"], r["official_url_requested"], r["final_url"],
                r["load_status"], r["product_type_live"], r["has_sport_section"],
                r["has_casino_section"], r["rating_site_type"],
                "yes" if r["rating_site_type"] == r["product_type_live"] or r["product_type_live"] == "unknown" else "no",
                ", ".join(r["payment_mentions"]),
                len(r["license_snippets"]), len(r["bonus_snippets"]),
            ])

    # Markdown dossier
    lines = [
        "# Досье брендов UZ — live-аудит официальных сайтов",
        "",
        f"Дата проверки: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "Метод: Playwright/Chromium, прямой заход на официальные домены из рейтинга.",
        "Источник: только страницы операторов (без агрегаторов).",
        "",
        "## Сводка",
        "",
        "| # | Бренд | Тип (live) | Спорт | Казино | Статус | Совпадение с рейтингом |",
        "|---|-------|------------|-------|--------|--------|------------------------|",
    ]
    type_ru = {"both": "Ставки + казино", "bk": "Только ставки", "casino": "Только казино", "unknown": "Не определено"}
    for r in results:
        match = "✓" if r["rating_site_type"] == r["product_type_live"] or r["product_type_live"] == "unknown" else "⚠"
        lines.append(
            f"| {r['rank']} | {r['name']} | {type_ru.get(r['product_type_live'], r['product_type_live'])} | "
            f"{'да' if r['has_sport_section'] else 'нет'} | {'да' if r['has_casino_section'] else 'нет'} | "
            f"{r['load_status']} | {match} |"
        )

    lines.append("\n---\n")
    for r in results:
        lines.extend([
            f"## {r['rank']}. {r['name']}",
            "",
            f"- **Официальный URL:** {r['official_url_requested']}",
            f"- **Финальный URL:** {r['final_url'] or '—'}",
            f"- **Статус загрузки:** {r['load_status']}",
            f"- **Тип продукта (live):** {type_ru.get(r['product_type_live'], r['product_type_live'])}",
            f"- **В рейтинге указано:** {r['rating_site_type']}",
            f"- **Title:** {r['title']}",
            f"- **H1:** {r['h1'] or '—'}",
            f"- **Язык страницы:** {r['page_lang'] or '—'}",
            "",
        ])
        if r["sport_nav_samples"]:
            lines.append("### Навигация — спорт")
            for s in r["sport_nav_samples"][:8]:
                lines.append(f"- {s['text']} → `{s['href']}`")
            lines.append("")
        if r["casino_nav_samples"]:
            lines.append("### Навигация — казино/игры")
            for s in r["casino_nav_samples"][:8]:
                lines.append(f"- {s['text']} → `{s['href']}`")
            lines.append("")
        if r["license_snippets"]:
            lines.append("### Лицензия (фрагменты со страницы)")
            for s in r["license_snippets"]:
                lines.append(f"- …{s}…")
            lines.append("")
        if r["bonus_snippets"]:
            lines.append("### Бонусы / промо (фрагменты)")
            for s in r["bonus_snippets"][:6]:
                lines.append(f"- {s}")
            lines.append("")
        if r["payment_mentions"]:
            lines.append(f"### Платежи (упоминания на странице): {', '.join(r['payment_mentions'])}")
            lines.append("")
        if r["app_hints"]:
            lines.append("### Приложение / мобильный доступ")
            for s in r["app_hints"][:5]:
                lines.append(f"- {s['text']} → `{s['href']}`")
            lines.append("")
        if r["registration_hints"]:
            lines.append("### Регистрация")
            for s in r["registration_hints"][:5]:
                lines.append(f"- {s['text']} → `{s['href']}`")
            lines.append("")
        if r["notes"]:
            lines.append("### Примечания")
            for n in r["notes"]:
                lines.append(f"- {n}")
            lines.append("")
        if r["footer_excerpt"]:
            lines.append("<details><summary>Футер (выдержка)</summary>\n\n")
            lines.append(r["footer_excerpt"][:800])
            lines.append("\n</details>\n")
        lines.append("---\n")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Saved: {json_path}")
    print(f"Saved: {md_path}")
    print(f"Saved: {csv_path}")


if __name__ == "__main__":
    main()
