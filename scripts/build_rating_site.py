#!/usr/bin/env python3
"""Rebuild casino-bonuses-uz.com: 20 brands, casino.ru card UI, SEO, i18n."""
from __future__ import annotations
import json
import re
from pathlib import Path
from html import escape

from brand_qttk_content import render_body, faq_schema, brand_footer_faq
from hub_expand_2000 import hub_body, SLUGS as HUB_SLUGS
from index_expand_2000 import index_extra_sections, index_footer_faq

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://casino-bonuses-uz.com"
CSS_V = "20260619e"


def _table_end(html: str, start: int) -> int:
    depth = 0
    pos = start
    while pos < len(html):
        if html.startswith("<table", pos):
            depth += 1
            close = html.find(">", pos)
            pos = close + 1 if close != -1 else pos + 1
        elif html.startswith("</table>", pos):
            depth -= 1
            pos += len("</table>")
            if depth == 0:
                return pos
        else:
            pos += 1
    return len(html)


def wrap_data_tables(html: str) -> str:
    marker = '<table class="data-table'
    out: list[str] = []
    pos = 0
    while True:
        start = html.find(marker, pos)
        if start == -1:
            out.append(html[pos:])
            break
        before = html[max(0, start - 120):start]
        if re.search(r'<div class="(?:table-scroll|data-table-wrap)"[^>]*>\s*$', before):
            end = _table_end(html, start)
            out.append(html[pos:end])
            pos = end
            continue
        end = _table_end(html, start)
        out.append(html[pos:start])
        out.append('<div class="table-scroll">')
        out.append(html[start:end])
        out.append("</div>")
        pos = end
    return "".join(out)


def write_html(path: Path, html: str) -> None:
    path.write_text(wrap_data_tables(html), encoding="utf-8")
PARTNER = "https://bobaffs.org/click?o=1603&a=189"

# 20 brands popular in Google UZ (casino + BK)
BRANDS = [
    {"slug": "fairpari", "name": "FairPari", "rating": 5.0, "type": "both",
     "welcome_uz": "20 200 000 UZS + 150 FS", "welcome_ru": "20 200 000 UZS + 150 FS",
     "wagering": "×35", "pay": "Humo, Payme, Click",
     "pros_uz": ["Eng katta kazino welcome UZ", "UZ interfeysi (fairpari.com/uz)", "APK va PWA"],
     "cons_uz": ["Sport va kazino welcome bir vaqtda emas"],
     "pros_ru": ["Крупнейший welcome в UZ", "UZ-интерфейс (fairpari.com/uz)", "APK и PWA"],
     "cons_ru": ["Спорт и казино welcome не вместе"],
     "tags_uz": ["Slotlar", "Live", "Sport", "Kazino"], "tags_ru": ["Слоты", "Live", "Спорт", "Казино"],
     "hit": True},
    {"slug": "1win", "name": "1win", "rating": 4.8, "type": "both",
     "welcome_uz": "12 000 000 UZS gacha", "welcome_ru": "до 12 000 000 UZS",
     "wagering": "×30", "pay": "Humo, Uzcard",
     "pros_uz": ["Kuchli mobil ilova", "Keng sport liniyasi"],
     "cons_uz": ["Welcome FairPari dan kichikroq"],
     "pros_ru": ["Сильное мобильное приложение", "Широкая линия"],
     "cons_ru": ["Welcome меньше FairPari"],
     "tags_uz": ["Slotlar", "Sport", "Crash"], "tags_ru": ["Слоты", "Спорт", "Crash"]},
    {"slug": "1xbet", "name": "1xBet", "rating": 4.7, "type": "both",
     "welcome_uz": "6 500 000 UZS + 150 FS", "welcome_ru": "6 500 000 UZS + 150 FS",
     "wagering": "×40", "pay": "Humo, kripto",
     "pros_uz": ["Juda keng sport bozorlari", "Kripto depozit"],
     "cons_uz": ["Yuqori wagering ×40"],
     "pros_ru": ["Очень широкая линия", "Криптодепозит"],
     "cons_ru": ["Высокий вейджер ×40"],
     "tags_uz": ["Sport", "Live", "Kazino"], "tags_ru": ["Спорт", "Live", "Казино"]},
    {"slug": "mostbet", "name": "Mostbet", "rating": 4.6, "type": "both",
     "welcome_uz": "8 500 000 UZS + 250 FS", "welcome_ru": "8 500 000 UZS + 250 FS",
     "wagering": "×35", "pay": "Humo, Payme",
     "pros_uz": ["250 FS paketda", "Sport va kazino"],
     "cons_uz": ["Wagering o'rtacha yuqori"],
     "pros_ru": ["250 FS в пакете", "Спорт и казино"],
     "cons_ru": ["Средне-высокий вейджер"],
     "tags_uz": ["Slotlar", "Sport"], "tags_ru": ["Слоты", "Спорт"]},
    {"slug": "melbet", "name": "Melbet", "rating": 4.5, "type": "both",
     "welcome_uz": "7 000 000 UZS", "welcome_ru": "7 000 000 UZS",
     "wagering": "×30", "pay": "Uzcard, Click",
     "pros_uz": ["×30 wagering", "Uzcard qabul"],
     "cons_uz": ["FS kamroq"],
     "pros_ru": ["Вейджер ×30", "Принимает Uzcard"],
     "cons_ru": ["Меньше FS"],
     "tags_uz": ["Sport", "Kazino"], "tags_ru": ["Спорт", "Казино"]},
    {"slug": "pin-up", "name": "Pin-Up", "rating": 4.5, "type": "both",
     "welcome_uz": "5 500 000 UZS + 250 FS", "welcome_ru": "5 500 000 UZS + 250 FS",
     "wagering": "×35", "pay": "Humo, Payme",
     "pros_uz": ["Tanilgan brend", "250 FS"],
     "cons_uz": ["Welcome limit pastroq"],
     "pros_ru": ["Известный бренд", "250 FS"],
     "cons_ru": ["Лимит welcome ниже"],
     "tags_uz": ["Slotlar", "Sport"], "tags_ru": ["Слоты", "Спорт"]},
    {"slug": "linebet", "name": "Linebet", "rating": 4.4, "type": "both",
     "welcome_uz": "4 800 000 UZS sport", "welcome_ru": "4 800 000 UZS спорт",
     "wagering": "×5", "pay": "Humo, Click",
     "pros_uz": ["Sport welcome ×5", "Kazino GAMES va slotlar", "iOS/Android ilova"],
     "cons_uz": ["Bannerda ba'zan RUB ko'rsatiladi"],
     "pros_ru": ["Спорт welcome ×5", "Казино GAMES и слоты", "Приложение iOS/Android"],
     "cons_ru": ["В баннере иногда RUB вместо UZS"],
     "tags_uz": ["Sport", "Slotlar", "Kazino"], "tags_ru": ["Спорт", "Слоты", "Казино"]},
    {"slug": "betwinner", "name": "Betwinner", "rating": 4.4, "type": "both",
     "welcome_uz": "5 000 000 UZS + 150 FS", "welcome_ru": "5 000 000 UZS + 150 FS",
     "wagering": "×35", "pay": "Humo, Uzcard",
     "pros_uz": ["1xBet tarmog'i", "Kripto mavjud"],
     "cons_uz": ["Interfeys murakkab"],
     "pros_ru": ["Сеть 1xBet", "Есть крипто"],
     "cons_ru": ["Сложный интерфейс"],
     "tags_uz": ["Sport", "Kazino"], "tags_ru": ["Спорт", "Казино"]},
    {"slug": "megapari", "name": "Megapari", "rating": 4.3, "type": "both",
     "welcome_uz": "4 500 000 UZS + 100 FS", "welcome_ru": "4 500 000 UZS + 100 FS",
     "wagering": "×35", "pay": "Humo, Payme",
     "pros_uz": ["Keshbek aksiyalar", "UZS hisob"],
     "cons_uz": ["Kamroq mashhur UZ da"],
     "pros_ru": ["Кешбэк-акции", "Счёт UZS"],
     "cons_ru": ["Менее популярен в UZ"],
     "tags_uz": ["Sport", "Slotlar"], "tags_ru": ["Спорт", "Слоты"]},
    {"slug": "22bet", "name": "22Bet", "rating": 4.3, "type": "both",
     "welcome_uz": "4 200 000 UZS", "welcome_ru": "4 200 000 UZS",
     "wagering": "×35", "pay": "Humo, kripto",
     "pros_uz": ["Past minimal depozit", "Kripto"],
     "cons_uz": ["FS kam"],
     "pros_ru": ["Низкий мин. депозит", "Крипто"],
     "cons_ru": ["Мало FS"],
     "tags_uz": ["Sport", "Kazino"], "tags_ru": ["Спорт", "Казино"]},
    {"slug": "parimatch", "name": "Parimatch", "rating": 4.2, "type": "both",
     "welcome_uz": "3 800 000 UZS sport", "welcome_ru": "3 800 000 UZS спорт",
     "wagering": "×5", "pay": "Humo, Payme",
     "pros_uz": ["Sport brend", "Kazino va live bo'limlari"],
     "cons_uz": ["Welcome sportga yo'naltirilgan"],
     "pros_ru": ["Спортивный бренд", "Разделы казино и live"],
     "cons_ru": ["Welcome ориентирован на спорт"],
     "tags_uz": ["Sport", "Live", "Kazino"], "tags_ru": ["Спорт", "Live", "Казино"]},
    {"slug": "leon", "name": "Leon", "rating": 4.2, "type": "both",
     "welcome_uz": "3 500 000 UZS", "welcome_ru": "3 500 000 UZS",
     "wagering": "×5", "pay": "Humo, Click",
     "pros_uz": ["Oddiy interfeys", "Sport va kazino (ru-uz)"],
     "cons_uz": ["Welcome kichikroq"],
     "pros_ru": ["Простой интерфейс", "Спорт и казино (ru-uz)"],
     "cons_ru": ["Небольшой welcome"],
     "tags_uz": ["Sport", "Slotlar", "Kazino"], "tags_ru": ["Спорт", "Слоты", "Казино"]},
    {"slug": "fonbet", "name": "Fonbet", "rating": 4.1, "type": "bk",
     "welcome_uz": "3 200 000 UZS sport", "welcome_ru": "3 200 000 UZS спорт",
     "wagering": "×5", "pay": "Humo, Uzcard",
     "pros_uz": ["Tajribali BK", "Live matnlar"],
     "cons_uz": ["UZ kazino cheklangan"],
     "pros_ru": ["Опытный БК", "Live-трансляции"],
     "cons_ru": ["Казино в UZ ограничено"],
     "tags_uz": ["Sport", "Live"], "tags_ru": ["Спорт", "Live"]},
    {"slug": "marathonbet", "name": "Marathonbet", "rating": 4.1, "type": "both",
     "welcome_uz": "3 000 000 UZS", "welcome_ru": "3 000 000 UZS",
     "wagering": "×5", "pay": "Humo, Payme",
     "pros_uz": ["Yuqori koeffitsientlar", "Sport va live kazino"],
     "cons_uz": ["Interfeys eskiroq"],
     "pros_ru": ["Высокие коэффициенты", "Спорт и live-казино"],
     "cons_ru": ["Интерфейс устаревает"],
     "tags_uz": ["Sport", "Kazino", "Live"], "tags_ru": ["Спорт", "Казино", "Live"]},
    {"slug": "betway", "name": "Betway", "rating": 4.0, "type": "bk",
     "welcome_uz": "2 800 000 UZS sport", "welcome_ru": "2 800 000 UZS спорт",
     "wagering": "×6", "pay": "Humo, kripto",
     "pros_uz": ["Xalqaro brend", "Mobil qulay"],
     "cons_uz": ["UZS limit past"],
     "pros_ru": ["Международный бренд", "Удобная мобилка"],
     "cons_ru": ["Низкий лимит UZS"],
     "tags_uz": ["Sport"], "tags_ru": ["Спорт"]},
    {"slug": "spinbetter", "name": "Spinbetter", "rating": 4.0, "type": "both",
     "welcome_uz": "3 600 000 UZS + 100 FS", "welcome_ru": "3 600 000 UZS + 100 FS",
     "wagering": "×35", "pay": "Humo, Uzcard, Click",
     "pros_uz": ["Humo va Uzcard", "Sport va kazino bo'limlari"],
     "cons_uz": ["Kam sharhlar UZ"],
     "pros_ru": ["Humo и Uzcard", "Спорт и казино на одной платформе"],
     "cons_ru": ["Мало отзывов в UZ"],
     "tags_uz": ["Slotlar", "Sport", "Kazino"], "tags_ru": ["Слоты", "Спорт", "Казино"]},
    {"slug": "vulkan-vegas", "name": "Vulkan Vegas", "rating": 4.0, "type": "both",
     "welcome_uz": "3 400 000 UZS + 150 FS", "welcome_ru": "3 400 000 UZS + 150 FS",
     "wagering": "×40", "pay": "Humo, Payme",
     "pros_uz": ["Katta slot katalogi", "Sport va kazino"],
     "cons_uz": ["Bannerda EUR", "×40 wagering"],
     "pros_ru": ["Большой каталог слотов", "Спорт и казино"],
     "cons_ru": ["Баннер в EUR", "Вейджер ×40"],
     "tags_uz": ["Slotlar", "Live kazino", "Sport"], "tags_ru": ["Слоты", "Live-казино", "Спорт"]},
    {"slug": "joycasino", "name": "Joycasino", "rating": 3.9, "type": "both",
     "welcome_uz": "3 000 000 UZS + 200 FS", "welcome_ru": "3 000 000 UZS + 200 FS",
     "wagering": "×40", "pay": "Humo, Uzcard",
     "pros_uz": ["200 FS", "Sport va kazino"],
     "cons_uz": ["Yuqori wagering"],
     "pros_ru": ["200 FS", "Спорт и казино"],
     "cons_ru": ["Высокий вейджер"],
     "tags_uz": ["Slotlar", "Sport", "Live"], "tags_ru": ["Слоты", "Спорт", "Live"]},
    {"slug": "fresh-casino", "name": "Fresh Casino", "rating": 3.9, "type": "both",
     "welcome_uz": "2 900 000 UZS + 100 FS", "welcome_ru": "2 900 000 UZS + 100 FS",
     "wagering": "×35", "pay": "Payme, Click",
     "pros_uz": ["Zamonaviy dizayn", "Sport va slotlar"],
     "cons_uz": ["Welcome kichikroq"],
     "pros_ru": ["Современный дизайн", "Спорт и слоты"],
     "cons_ru": ["Небольшой welcome"],
     "tags_uz": ["Slotlar", "Crash", "Sport"], "tags_ru": ["Слоты", "Crash", "Спорт"]},
    {"slug": "bc-game", "name": "BC.Game", "rating": 3.8, "type": "both",
     "welcome_uz": "Kripto paket USDT", "welcome_ru": "Крипто-пакет USDT",
     "wagering": "×45", "pay": "USDT, BTC",
     "pros_uz": ["Kripto kazino", "Sport BTi va crash"],
     "cons_uz": ["Humo yo'q", "Yuqori wagering"],
     "pros_ru": ["Крипто-казино", "Спорт BTi и crash"],
     "cons_ru": ["Нет Humo", "Высокий вейджер"],
     "tags_uz": ["Kripto", "Crash", "Sport"], "tags_ru": ["Крипто", "Crash", "Спорт"]},
]

STAR = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>'

HUB_LINKS = [
    ("kazino-bonuslari", "Типы казино-бонусов", "Kazino bonus turlari"),
    ("welcome-bonus", "Welcome-бонусы 2026", "Welcome bonuslar 2026"),
    ("depozitsiz-bonus", "Бонусы без депозита", "Depozitsiz bonuslar"),
    ("tolov-uz", "Платежи Humo, Payme, Click", "Humo, Payme, Click to'lovlari"),
    ("faq", "FAQ", "FAQ"),
]

BRAND_TYPE_LABELS = {
    "both": ("Казино + букмекеры", "Kazino + bukmekerlar"),
    "bk": ("Букмекеры", "Bukmekerlar"),
    "casino": ("Только казино", "Faqat kazino"),
}

LEGAL_LINKS = {
    "ru": [
        ("politika-konfidentsialnosti.html", "Конфиденциальность"),
        ("usloviya-ispolzovaniya.html", "Условия использования"),
        ("politika-cookie.html", "Политика cookie"),
        ("otvetstvennaya-igra.html", "Ответственная игра"),
    ],
    "uz": [
        ("maxfiylik-siyosati.html", "Maxfiylik siyosati"),
        ("foydalanish-shartlari.html", "Foydalanish shartlari"),
        ("cookie-siyosati.html", "Cookie siyosati"),
        ("masuliyatli-oyin.html", "Mas'uliyatli o'yin"),
    ],
}

PAY_TOKEN_MAP = {
    "humo": ("humo", "Humo"),
    "payme": ("payme", "Payme"),
    "click": ("click", "Click"),
    "uzcard": ("uzcard", "Uzcard"),
    "kripto": ("usdt", "USDT"),
    "крипто": ("usdt", "USDT"),
    "usdt": ("usdt", "USDT"),
    "btc": ("bitcoin", "BTC"),
    "bitcoin": ("bitcoin", "Bitcoin"),
}


def pay_logos_html(pay: str, lang: str) -> str:
    assets = assets_href(lang, 0)
    imgs: list[str] = []
    for part in pay.split(","):
        key = part.strip().lower()
        if not key:
            continue
        mapped = PAY_TOKEN_MAP.get(key)
        if not mapped:
            for token, value in PAY_TOKEN_MAP.items():
                if token in key:
                    mapped = value
                    break
        if not mapped:
            continue
        slug, alt = mapped
        imgs.append(
            f'<img class="casino-card__pay-logo" src="{assets}/logos/payments/{slug}.svg" '
            f'alt="{escape(alt)}" width="72" height="24" loading="lazy" />'
        )
    if not imgs:
        return escape(pay)
    return f'<span class="casino-card__pay-logos" role="list">{"".join(imgs)}</span>'


def logo_path(slug: str) -> str:
    return f"assets/logos/brands/{slug}.svg"


def ensure_logos():
    d = ROOT / "assets/logos/brands"
    d.mkdir(parents=True, exist_ok=True)
    colors = ["#0d9488", "#2563eb", "#7c3aed", "#dc2626", "#ea580c", "#0891b2", "#4f46e5", "#be185d"]
    for i, b in enumerate(BRANDS):
        p = d / f"{b['slug']}.svg"
        if p.exists():
            continue
        c = colors[i % len(colors)]
        initials = "".join(w[0] for w in b["name"].replace("-", " ").split()[:2]).upper()[:2]
        p.write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
<rect width="64" height="64" rx="12" fill="{c}"/>
<text x="32" y="38" text-anchor="middle" fill="#fff" font-family="system-ui,sans-serif" font-size="22" font-weight="700">{initials}</text>
</svg>''', encoding="utf-8")


def rel_prefix(lang: str) -> str:
    return "../" if lang == "ru" else ""


def site_root_prefix(lang: str, depth: int = 0) -> str:
    """Path from HTML file to site root. depth 0=index, 1=brand/hub nested."""
    if lang == "ru":
        return "../" if depth == 0 else "../../"
    return "" if depth == 0 else "../"


def css_href(lang: str, depth: int = 0) -> str:
    p = site_root_prefix(lang, depth)
    return f"{p}css" if p else "css"


def assets_href(lang: str, depth: int = 0) -> str:
    p = site_root_prefix(lang, depth)
    return f"{p}assets" if p else "assets"


def js_href(lang: str, depth: int = 0) -> str:
    p = site_root_prefix(lang, depth)
    return f"{p}js" if p else "js"


def css_links(lang: str, depth: int = 0, extra: str = "") -> str:
    base = css_href(lang, depth)
    v = CSS_V
    return f'''<link rel="stylesheet" href="{base}/style.css?v={v}" />
  <link rel="stylesheet" href="{base}/fairpari-light-theme.css?v={v}" />
  <link rel="stylesheet" href="{base}/fairpari-v2.css?v={v}" />
  <link rel="stylesheet" href="{base}/rating-cards.css?v={v}" />
  <link rel="stylesheet" href="{base}/rating-site-ui.css?v={v}" />
  {extra}'''


def top10_brand_links(lang: str, prefix: str, link_class: str = "nav-mobile__link") -> str:
    links: list[str] = []
    for rank, b in enumerate(BRANDS[:10], 1):
        label = f"#{rank} {b['name']}"
        if b["slug"] == "fairpari":
            label += " ★"
        links.append(
            f'<a class="{link_class}" href="{prefix}{b["slug"]}/">{escape(label)}</a>'
        )
    return "".join(links)


def desktop_brands_dropdown(lang: str, prefix: str) -> str:
    label = "Казино и БК" if lang == "ru" else "Kazino va BK"
    menu_label = "ТОП-10 рейтинга" if lang == "ru" else "TOP-10 reyting"
    return (
        f'<div class="nav-dropdown">'
        f'<button type="button" class="nav-dropdown__toggle" aria-expanded="false" '
        f'aria-haspopup="true" aria-controls="nav-brands-menu">'
        f'{escape(label)}<span class="nav-dropdown__chevron" aria-hidden="true"></span>'
        f"</button>"
        f'<div class="nav-dropdown__menu" id="nav-brands-menu" role="menu" '
        f'aria-label="{escape(menu_label)}">'
        f'{top10_brand_links(lang, prefix, "nav-dropdown__link")}'
        f"</div></div>"
    )


def mobile_nav_html(lang: str) -> tuple[str, str]:
    prefix = "/ru/" if lang == "ru" else "/"
    legal_prefix = "/ru/" if lang == "ru" else "/"
    idx = 0 if lang == "ru" else 1

    if lang == "ru":
        rating_l = "Рейтинг"
        bonus_l = "Типы бонусов"
        brands_l = "Казино и БК"
        fairpari_l = "FairPari"
        faq_l = "FAQ"
        primary_title = "Разделы"
        guides_title = "Гайды и справочники"
        all_brands_l = "Все операторы TOP-20"
        legal_title = "Правовая информация"
        menu_label = "Меню сайта"
        open_label = "Открыть меню"
        close_label = "Закрыть меню"
        cta_l = "Получить бонус"
    else:
        rating_l = "Reyting"
        bonus_l = "Bonus turlari"
        brands_l = "Kazino va BK"
        fairpari_l = "FairPari"
        faq_l = "FAQ"
        primary_title = "Bo'limlar"
        guides_title = "Qo'shimcha qo'llanmalar"
        all_brands_l = "Barcha TOP-20 operatorlar"
        legal_title = "Huquqiy ma'lumot"
        menu_label = "Sayt menyusi"
        open_label = "Menyuni ochish"
        close_label = "Menyuni yopish"
        cta_l = "Bonus olish"

    sections: list[str] = []

    sections.append(
        f'<div class="nav-mobile__section nav-mobile__section--primary">'
        f'<p class="nav-mobile__heading">{escape(primary_title)}</p>'
        f'<a class="nav-mobile__link nav-mobile__link--primary" href="{prefix}#rating">{escape(rating_l)}</a>'
        f'<a class="nav-mobile__link nav-mobile__link--primary" href="{prefix}kazino-bonuslari/">{escape(bonus_l)}</a>'
        f'<div class="nav-mobile__disclosure nav-mobile__disclosure--inline" data-nav-disclosure>'
        f'<button type="button" class="nav-mobile__disclosure-btn nav-mobile__link--primary" aria-expanded="false">'
        f'{escape(brands_l)}<span class="nav-mobile__chevron" aria-hidden="true"></span>'
        f"</button>"
        f'<div class="nav-mobile__disclosure-panel" hidden>'
        f'{top10_brand_links(lang, prefix)}'
        f"</div></div>"
        f'<a class="nav-mobile__link nav-mobile__link--primary" href="{prefix}fairpari/">{escape(fairpari_l)}</a>'
        f'<a class="nav-mobile__link nav-mobile__link--primary" href="{prefix}faq/">{escape(faq_l)}</a>'
        f"</div>"
    )

    extra_guides = "".join(
        f'<a class="nav-mobile__link" href="{prefix}{slug}/">{escape(labels[idx])}</a>'
        for slug, *labels in HUB_LINKS
        if slug not in ("kazino-bonuslari", "faq")
    )
    if extra_guides:
        sections.append(
            f'<div class="nav-mobile__section">'
            f'<p class="nav-mobile__heading">{escape(guides_title)}</p>'
            f"{extra_guides}</div>"
        )

    all_brand_links = "".join(
        f'<a class="nav-mobile__link" href="{prefix}{b["slug"]}/">'
        f"#{rank} {escape(b['name'])}{' ★' if b['slug'] == 'fairpari' else ''}</a>"
        for rank, b in enumerate(BRANDS, 1)
    )
    sections.append(
        f'<div class="nav-mobile__section nav-mobile__disclosure" data-nav-disclosure>'
        f'<button type="button" class="nav-mobile__disclosure-btn" aria-expanded="false">'
        f'{escape(all_brands_l)}<span class="nav-mobile__chevron" aria-hidden="true"></span>'
        f"</button>"
        f'<div class="nav-mobile__disclosure-panel" hidden>'
        f"{all_brand_links}"
        f"</div></div>"
    )

    legal_links = "".join(
        f'<a class="nav-mobile__link" href="{legal_prefix}{path}">{escape(label)}</a>'
        for path, label in LEGAL_LINKS[lang]
    )
    sections.append(
        f'<div class="nav-mobile__section">'
        f'<p class="nav-mobile__heading">{escape(legal_title)}</p>'
        f"{legal_links}</div>"
    )

    body = "\n".join(sections)
    toggle = (
        f'<button type="button" class="nav-toggle" aria-expanded="false" '
        f'aria-controls="site-nav-mobile" aria-label="{escape(open_label)}" '
        f'data-label-open="{escape(open_label)}" data-label-close="{escape(close_label)}">'
        f'<span aria-hidden="true"></span><span aria-hidden="true"></span><span aria-hidden="true"></span>'
        f"</button>"
    )
    panel = (
        f'<div class="nav-mobile-backdrop" id="nav-mobile-backdrop" hidden aria-hidden="true"></div>'
        f'<nav class="nav-mobile" id="site-nav-mobile" aria-label="{escape(menu_label)}" hidden>'
        f'<div class="nav-mobile__top">'
        f'<p class="nav-mobile__title">{escape(menu_label)}</p>'
        f'<button type="button" class="nav-mobile__close" aria-label="{escape(close_label)}">'
        f'<span aria-hidden="true">×</span></button>'
        f"</div>"
        f'<div class="nav-mobile__body">{body}</div>'
        f'<div class="nav-mobile__footer">'
        f'<button type="button" class="btn btn--gold btn--block js-go-partner">{escape(cta_l)}</button>'
        f"</div>"
        f"</nav>"
    )
    return toggle, panel


def lang_switcher_html(lang: str, href_uz: str, href_ru: str) -> str:
    uz_path = href_uz.replace(DOMAIN, "") if href_uz.startswith("http") else (href_uz or "/")
    ru_path = href_ru.replace(DOMAIN, "") if href_ru.startswith("http") else (href_ru or "/ru/")
    aria = "Язык сайта" if lang == "ru" else "Sayt tili"
    if lang == "ru":
        return f'''<nav class="lang-switcher" aria-label="{aria}">
  <span class="lang-switcher__item is-active" aria-current="page">RU</span>
  <a class="lang-switcher__item" href="{uz_path}" hreflang="uz-UZ">UZ</a>
</nav>'''
    return f'''<nav class="lang-switcher" aria-label="{aria}">
  <span class="lang-switcher__item is-active" aria-current="page">UZ</span>
  <a class="lang-switcher__item" href="{ru_path}" hreflang="ru-UZ">RU</a>
</nav>'''


def header_block(lang: str, depth: int = 0, href_uz: str = "", href_ru: str = "") -> str:
    assets = assets_href(lang, depth)
    home = "/ru/" if lang == "ru" else "/"
    prefix = "/ru/" if lang == "ru" else "/"
    if lang == "ru":
        nav = (
            '<a href="/ru/#rating">Рейтинг</a>'
            '<a href="/ru/kazino-bonuslari/">Типы бонусов</a>'
            f'{desktop_brands_dropdown(lang, prefix)}'
            '<a href="/ru/fairpari/">FairPari</a>'
            '<a href="/ru/faq/">FAQ</a>'
        )
        cta = "Получить бонус"
    else:
        nav = (
            '<a href="/#rating">Reyting</a>'
            '<a href="/kazino-bonuslari/">Bonus turlari</a>'
            f'{desktop_brands_dropdown(lang, prefix)}'
            '<a href="/fairpari/">FairPari</a>'
            '<a href="/faq/">FAQ</a>'
        )
        cta = "Bonus olish"
    nav_aria = "Разделы" if lang == "ru" else "Sayt bo'limlari"
    lang_nav = lang_switcher_html(lang, href_uz, href_ru)
    nav_toggle, nav_panel = mobile_nav_html(lang)
    return f'''<header class="site-header"><div class="site-header__inner">
  <a class="brand" href="{home}"><img class="brand__logo-img" src="{assets}/logo-casino-bonuses-uz.svg" alt="Casino Bonuses UZ" width="180" height="32" loading="eager" /></a>
  <nav class="nav-desktop" aria-label="{nav_aria}">{nav}</nav>
  <div class="header-actions">
    {lang_nav}
    <button type="button" class="btn btn--gold js-go-partner">{cta}</button>
    {nav_toggle}
  </div>
</div></header>
{nav_panel}'''


def card_html(b: dict, rank: int, lang: str) -> str:
    prefix = "/ru/" if lang == "ru" else "/"
    logo = f"{assets_href(lang, 0)}/logos/brands/{b['slug']}.svg"
    welcome = b["welcome_ru"] if lang == "ru" else b["welcome_uz"]
    pros = b["pros_ru"] if lang == "ru" else b["pros_uz"]
    cons = b["cons_ru"] if lang == "ru" else b["cons_uz"]
    tags = b["tags_ru"] if lang == "ru" else b["tags_uz"]
    t = b["type"]
    type_label = {"both": ("Kazino + BK", "Казино + БК"), "bk": ("Bukmeker", "Букмекер"), "casino": ("Kazino", "Казино")}[t][1 if lang == "ru" else 0]
    btn_get = "Регистрация" if lang == "ru" else "Ro'yxatdan o'tish"
    btn_review = "Полный обзор" if lang == "ru" else "To'liq sharh"
    hit = ""
    if b.get("hit"):
        hit = f'<span class="casino-card__badge casino-card__badge--hit">{"Хит сезона" if lang == "ru" else "Mavsum hiti"}</span>'
    pros_li = "".join(f"<li>{escape(p)}</li>" for p in pros)
    cons_li = "".join(f"<li>{escape(c)}</li>" for c in cons)
    tags_html = "".join(f'<span class="casino-card__tag">{escape(tg)}</span>' for tg in tags)
    pay_label = "Платёж" if lang == "ru" else "To'lov"
    return f'''<article class="casino-card" data-rank="{rank}" data-type="{t}" data-name="{escape(b["name"])}">
  <div class="casino-card__rank-col">
    <span class="casino-card__rank">#{rank}</span>
    <img class="casino-card__logo" src="{logo}" alt="{escape(b["name"])}" width="120" height="48" loading="lazy" />
    <h3 class="casino-card__title"><a href="{prefix}{b["slug"]}/">{escape(b["name"])}</a></h3>
    <div class="casino-card__score">{STAR}<span>{b["rating"]:.1f}</span></div>
  </div>
  <div class="casino-card__body">
    <div class="casino-card__badges">{hit}<span class="casino-card__badge casino-card__badge--type">{type_label}</span></div>
    <p class="casino-card__bonus-line">{escape(welcome)} <span class="casino-card__bonus-hint">wagering {b["wagering"]}</span></p>
    <div class="casino-card__proscons">
      <ul class="casino-card__pros">{pros_li}</ul>
      <ul class="casino-card__cons">{cons_li}</ul>
    </div>
    <div class="casino-card__tags">{tags_html}</div>
    <div class="casino-card__pay"><strong>{pay_label}:</strong> {pay_logos_html(b["pay"], lang)}</div>
    <div class="casino-card__actions">
      <button type="button" class="btn btn--gold btn--sm js-go-partner">{btn_get}</button>
      <a class="btn btn--ghost btn--sm" href="{prefix}{b["slug"]}/">{btn_review}</a>
    </div>
  </div>
</article>'''


def rating_section(lang: str) -> str:
    cards = "\n".join(card_html(b, i + 1, lang) for i, b in enumerate(BRANDS))
    if lang == "ru":
        title = "Лучшие бонусы казино и БК в Узбекистане — рейтинг 2026"
        count = f'Найдено: <strong data-rating-visible>20</strong> из <strong>20</strong> операторов'
        filters = [
            ("all", "Все", True), ("both", "Казино + БК", False),
            ("casino", "Казино", False), ("bk", "Букмекеры", False),
        ]
        search_ph = "Поиск оператора…"
    else:
        title = "O'zbekistonda eng yaxshi kazino va BK bonuslari — reyting 2026"
        count = f'Topildi: <strong data-rating-visible>20</strong> dan <strong>20</strong> operator'
        filters = [
            ("all", "Hammasi", True), ("both", "Kazino + BK", False),
            ("casino", "Kazino", False), ("bk", "Bukmeker", False),
        ]
        search_ph = "Operator qidirish…"
    filt = "".join(
        f'<button type="button" class="rating-filter__btn{" is-active" if act else ""}" data-filter="{k}">{lbl}</button>'
        for k, lbl, act in filters
    )
    return f'''<section class="section" id="rating">
  <div class="container">
    <h2 class="section__title">{title}</h2>
    <div class="rating-toolbar">
      <p class="rating-toolbar__count">{count}</p>
      <div class="rating-filter">{filt}</div>
      <input type="search" class="rating-search" placeholder="{search_ph}" aria-label="{search_ph}" />
    </div>
    <div class="rating-cards">{cards}</div>
  </div>
</section>'''


def head_block(lang: str, title: str, desc: str, url: str, extra_css: str = "", href_uz: str = "", href_ru: str = "", depth: int = 0, extra_head: str = "") -> str:
    if not href_uz:
        href_uz = f"{DOMAIN}/"
    if not href_ru:
        href_ru = f"{DOMAIN}/ru/"
    canonical = url
    og_loc = "ru_UZ" if lang == "ru" else "uz_UZ"
    html_lang = "ru-UZ" if lang == "ru" else "uz-UZ"
    assets = assets_href(lang, depth)
    skip_label = "Перейти к основному содержанию" if lang == "ru" else "Asosiy kontentga o'tish"
    skip = f'<a class="skip-link" href="#main">{skip_label}</a>\n'
    return f'''<!DOCTYPE html>
<html lang="{html_lang}" data-site="rating-light" data-template="v2">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="#ffffff" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(desc)}" />
  <link rel="icon" href="{assets}/favicon.svg" type="image/svg+xml" />
  {css_links(lang, depth, extra_css)}
  <link rel="canonical" href="{canonical}" />
  <link rel="alternate" hreflang="uz-UZ" href="{href_uz}" />
  <link rel="alternate" hreflang="ru-UZ" href="{href_ru}" />
  <link rel="alternate" hreflang="x-default" href="{href_uz}" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Casino Bonuses UZ" />
  <meta property="og:title" content="{escape(title)}" />
  <meta property="og:description" content="{escape(desc)}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:image" content="{DOMAIN}/assets/hero-casino-uz-banner.webp" />
  <meta property="og:image:alt" content="Casino Bonuses UZ" />
  <meta property="og:locale" content="{og_loc}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{escape(title)}" />
  <meta name="twitter:description" content="{escape(desc)}" />
  <meta name="twitter:image" content="{DOMAIN}/assets/hero-casino-uz-banner.webp" />
  {extra_head}
</head>
<body class="site-fairpari-light">
{skip}{header_block(lang, depth, href_uz=href_uz, href_ru=href_ru)}'''


def footer_block(lang: str, depth: int = 0, index_faq: str = "") -> str:
    assets = assets_href(lang, depth)
    js = js_href(lang, depth)
    if lang == "ru":
        nav_links = '''<a href="/ru/#rating">Рейтинг</a>
<a href="/ru/kazino-bonuslari/">Типы бонусов</a>
<a href="/ru/welcome-bonus/">Welcome</a>
<a href="/ru/fairpari/">FairPari</a>
<a href="/ru/faq/">FAQ</a>'''
        legal = '''<a href="/ru/politika-konfidentsialnosti">Конфиденциальность</a>
<a href="/ru/usloviya-ispolzovaniya">Условия</a>
<a href="/ru/politika-cookie">Cookie</a>
<a href="/ru/otvetstvennaya-igra">Ответственная игра</a>
<a class="footer-lang" href="/">O'zbekcha</a>'''
        disc = "Независимый рейтинг казино и БК Узбекистана. Материалы носят информационный характер и не являются приглашением к игре."
        sticky_title = 'Лучшее предложение: <span class="bonus">20 200 000 UZS + 150 FS</span>'
        sticky_btn = "Активировать"
        badge_alt = ("eCOGRA", "DMCA", "BeGambleAware")
    else:
        nav_links = '''<a href="/#rating">Reyting</a>
<a href="/kazino-bonuslari/">Kazino bonuslari</a>
<a href="/welcome-bonus/">Welcome</a>
<a href="/fairpari/">FairPari</a>
<a href="/faq/">FAQ</a>'''
        legal = '''<a href="/maxfiylik-siyosati">Maxfiylik</a>
<a href="/foydalanish-shartlari">Shartlar</a>
<a href="/cookie-siyosati">Cookie</a>
<a href="/masuliyatli-oyin">Mas'uliyatli o'yin</a>
<a class="footer-lang" href="/ru/">Русская версия</a>'''
        disc = "O'zbekiston uchun mustaqil kazino va BK reytingi. Materiallar axborot xarakterida; bu tikish yoki o'ynashga chaqiruv emas."
        sticky_title = 'FairPari start paketi <span class="bonus">20,2 mln UZS + 150 FS</span>'
        sticky_btn = "Faollashtirish"
        badge_alt = ("eCOGRA sertifikat", "DMCA himoya", "BeGambleAware")
    faq_html = f"\n  {index_faq}\n" if index_faq else ""
    return f'''<footer class="site-footer"><div class="container">{faq_html}
  <nav class="footer-nav" aria-label="Footer">{nav_links}</nav>
  <div class="footer-badges">
    <img class="footer-badge-img" src="{assets}/logos/footer/ecogra.svg" alt="{badge_alt[0]}" width="88" height="32" loading="lazy" />
    <img class="footer-badge-img" src="{assets}/logos/footer/dmca.svg" alt="{badge_alt[1]}" width="88" height="32" loading="lazy" />
    <img class="footer-badge-img" src="{assets}/logos/footer/begambleaware.svg" alt="{badge_alt[2]}" width="120" height="32" loading="lazy" />
  </div>
  <nav class="footer-legal-nav">{legal}</nav>
  <p class="footer-disclaimer"><span class="age">18+</span>. {disc}</p>
</div></footer>
<script src="{js}/partner.js?v={CSS_V}"></script>
<script src="{js}/main.js?v={CSS_V}"></script>
<script src="{js}/rating-filter.js?v={CSS_V}"></script>
<div class="sticky-banner" id="sticky-banner" role="complementary" aria-label="Bonus">
  <p class="sticky-banner-title">{sticky_title}</p>
  <button type="button" class="btn btn--gold js-go-partner">{sticky_btn}</button>
</div>
</body></html>'''


def build_index(lang: str):
    if lang == "ru":
        path = ROOT / "ru/index.html"
        title = "Лучшие бонусы казино Узбекистан — рейтинг ТОП-20 2026"
        desc = "Рейтинг 20 казино и БК Узбекистан 2026: welcome-бонусы, wagering, Humo/Payme. FairPari №1 — 20,2 млн UZS + 150 FS. 18+."
        url = f"{DOMAIN}/ru/"
        hero_h1 = "ТОП-20 бонусов казино и БК <em>Узбекистан 2026</em>"
        hero_sub = (
            "Сравниваем welcome-бонусы, вейджер и выплаты в UZS у 20 казино и букмекеров. "
            "Независимый рейтинг для игроков из Узбекистана — Humo, Payme, Click, без платных мест."
        )
        hero_cta = '<a href="#rating" class="btn btn--gold btn--lg">Смотреть рейтинг</a>'
        img = "../assets/hero-casino-uz-banner.webp"
        img_alt = "3D баннер казино-бонусов Узбекистан — слоты, UZS, Humo"
        schema = json.dumps({
            "@context": "https://schema.org",
            "@graph": [
                {"@type": "WebSite", "url": url, "name": "Casino Bonuses UZ", "inLanguage": "ru-UZ"},
                {"@type": "ItemList", "name": "Рейтинг казино и БК Узбекистан 2026",
                 "numberOfItems": 20,
                 "itemListElement": [
                     {"@type": "ListItem", "position": i + 1, "name": b["name"],
                      "url": f"{DOMAIN}/ru/{b['slug']}/"} for i, b in enumerate(BRANDS)
                 ]},
            ]
        }, ensure_ascii=False)
    else:
        path = ROOT / "index.html"
        title = "O'zbekistonda eng yaxshi kazino bonuslari — TOP-20 reyting 2026"
        desc = "O'zbekistonda 20 ta kazino va BK reytingi 2026: welcome bonuslar, wagering, Humo/Payme. FairPari №1 — 20,2 mln UZS + 150 FS. 18+."
        url = f"{DOMAIN}/"
        hero_h1 = "TOP-20 kazino va BK bonuslari <em>O'zbekiston 2026</em>"
        hero_sub = (
            "20 ta kazino va bukmekerda welcome bonuslar, wagering va UZS yechishni solishtiramiz. "
            "O'zbekiston o'yinchilari uchun mustaqil reyting — Humo, Payme, Click, pullik joylar yo'q."
        )
        hero_cta = '<a href="#rating" class="btn btn--gold btn--lg">Reytingni ko\'rish</a>'
        img = "assets/hero-casino-uz-banner.webp"
        img_alt = "3D banner kazino bonuslari O'zbekiston — slotlar, UZS, Humo"
        schema = json.dumps({
            "@context": "https://schema.org",
            "@graph": [
                {"@type": "WebSite", "url": url, "name": "Casino Bonuses UZ", "inLanguage": "uz-UZ"},
                {"@type": "ItemList", "name": "O'zbekiston kazino va BK reytingi 2026",
                 "numberOfItems": 20,
                 "itemListElement": [
                     {"@type": "ListItem", "position": i + 1, "name": b["name"],
                      "url": f"{DOMAIN}/{b['slug']}/"} for i, b in enumerate(BRANDS)
                 ]},
            ]
        }, ensure_ascii=False)

    extra = f'<script type="application/ld+json">{schema}</script>'
    crit_title = "Критерии рейтинга" if lang == "ru" else "Reyting mezonlari"
    crit_text = "Бонус, wagering, UZS, платежи Humo/Payme, мобильное приложение, лицензия." if lang == "ru" else "Bonus, wagering, UZS, Humo/Payme to'lovlar, mobil ilova, litsenziya."
    resp_title = "Ответственная игра 18+" if lang == "ru" else "Mas'uliyatli o'yin 18+"
    resp_link = "/ru/otvetstvennaya-igra" if lang == "ru" else "/masuliyatli-oyin"
    resp_label = "Ответственная игра" if lang == "ru" else "Mas'uliyatli o'yin"
    resp_prefix = "Играйте ответственно. " if lang == "ru" else "Mas'uliyat bilan o'ynang. "
    body = f'''{head_block(lang, title, desc, url, extra, href_uz=url if lang != "ru" else f"{DOMAIN}/", href_ru=f"{DOMAIN}/ru/")}
<main id="main">
<section class="hero">
  <div class="hero__banner">
    <img class="hero__banner-img" src="{img}" alt="{img_alt}" width="1536" height="1024" loading="eager" decoding="async" fetchpriority="high" />
  </div>
  <div class="container hero__inner">
    <div class="hero__copy">
      <h1 class="hero__title">{hero_h1}</h1>
      <p class="hero__subtitle">{hero_sub}</p>
      <div class="hero__actions">{hero_cta}</div>
    </div>
  </div>
</section>
{rating_section(lang)}
{index_extra_sections(lang)}
<section class="section section--alt" id="criteria"><div class="container">
  <h2 class="section__title">{crit_title}</h2>
  <p>{crit_text}</p>
</div></section>
<section class="section" id="responsible"><div class="container">
  <h2 class="section__title">{resp_title}</h2>
  <p>{resp_prefix}<a href="{resp_link}">{resp_label}</a>.</p>
</div></section>
</main>
{footer_block(lang, index_faq=index_footer_faq(lang))}'''
    write_html(path, body)
    print(f"index: {path.relative_to(ROOT)}")


def build_review(b: dict, rank: int, lang: str):
    slug = b["slug"]
    depth = 1
    base = ROOT / ("ru" if lang == "ru" else "") / slug
    base.mkdir(parents=True, exist_ok=True)
    path = base / "index.html"
    welcome = b["welcome_ru"] if lang == "ru" else b["welcome_uz"]
    canonical = f"{DOMAIN}/{'ru/' if lang == 'ru' else ''}{slug}/"
    hreflang_uz = f"{DOMAIN}/{slug}/"
    hreflang_ru = f"{DOMAIN}/ru/{slug}/"

    if lang == "ru":
        title = f"{b['name']} бонус — обзор казино/БК #{rank} Узбекистан 2026"
        desc = f"{b['name']} в Узбекистане: welcome {welcome}, wagering {b['wagering']}, {b['pay']}. Независимый обзор #{rank}, 18+."
        crumb_home = "Главная"
    else:
        title = f"{b['name']} kazino bonusi — #{rank} sharh O'zbekiston 2026"
        desc = f"{b['name']} O'zbekistonda: welcome {welcome}, wagering {b['wagering']}, {b['pay']}. Mustaqil #{rank} sharh, 18+."
        crumb_home = "Bosh sahifa"

    home = "/ru/" if lang == "ru" else "/"
    logo = f"{assets_href(lang, depth)}/logos/brands/{slug}.svg"
    article_body = render_body(b, rank, lang, logo)

    schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "Review",
        "itemReviewed": {"@type": "Organization", "name": b["name"]},
        "reviewRating": {"@type": "Rating", "ratingValue": str(b["rating"]), "bestRating": "5"},
        "author": {"@type": "Organization", "name": "Casino Bonuses UZ"},
        "inLanguage": "ru-UZ" if lang == "ru" else "uz-UZ",
        "url": canonical,
    }, ensure_ascii=False)

    faq_ld = faq_schema(b, rank, lang)
    extra_head = f'''<meta property="og:type" content="article" />
<script type="application/ld+json">{schema}</script>
<script type="application/ld+json">{faq_ld}</script>'''

    html = f'''{head_block(lang, title, desc, canonical, href_uz=hreflang_uz, href_ru=hreflang_ru, depth=depth, extra_head=extra_head)}
<main id="main" class="container" style="padding:2rem 1rem">
<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="{home}">{crumb_home}</a> / <span>{escape(b["name"])}</span></nav>
{article_body}
</main>
{footer_block(lang, depth, index_faq=brand_footer_faq(b, rank, lang))}'''
    write_html(path, html)


HUB_META = {
    "kazino-bonuslari": {
        "uz": {
            "title": "Kazino bonuslari turlari — welcome, FS, keshbek | UZ 2026",
            "desc": "Onlayn kazino bonus turlari O'zbekistonda: welcome paket, depozitsiz so'rovlar, free spins, cashback va reload. Wagering jadvali, Humo/Payme, 18+.",
            "crumb": "Kazino bonuslari turlari",
            "headline": "Kazino bonuslari turlari — welcome, FS, keshbek",
        },
        "ru": {
            "title": "Типы бонусов казино — welcome, FS, кешбэк | UZ 2026",
            "desc": "Типы бонусов онлайн-казино в Узбекистане: welcome, фриспины, cashback, reload. Таблица вейджера, Humo/Payme, рейтинг TOP-20, 18+.",
            "crumb": "Типы казино-бонусов",
            "headline": "Типы казино-бонусов — welcome, FS, кешбэк",
        },
    },
    "welcome-bonus": {
        "uz": {
            "title": "Welcome bonus taqqoslash 2026 — TOP-5 O'zbekiston",
            "desc": "Welcome bonus O'zbekiston 2026: FairPari 20.2M UZS + 150 FS, 1win, Mostbet taqqoslash. Wagering, Humo/Payme, 4 depozit paket. Mustaqil reyting, 18+.",
            "crumb": "Welcome bonus",
            "headline": "Welcome bonus taqqoslash 2026",
        },
        "ru": {
            "title": "Сравнение welcome-бонусов 2026 — Узбекистан",
            "desc": "Welcome-бонус Узбекистан: 20,2 млн UZS + 150 FS, 4 депозита, wagering ×35. Сравнение FairPari и TOP-20 операторов, 18+.",
            "crumb": "Welcome-бонусы",
            "headline": "Сравнение welcome-бонусов 2026",
        },
    },
    "depozitsiz-bonus": {
        "uz": {
            "title": "Depozitsiz bonus O'zbekiston — haqiqat va miflar 2026",
            "desc": "Depozitsiz bonus va no deposit O'zbekistonda: nima haqiqiy, nima marketing. FairPari welcome alternativasi, minimal depozit, wagering ×35. 18+.",
            "crumb": "Depozitsiz bonus",
            "headline": "Depozitsiz bonus — haqiqat va miflar",
        },
        "ru": {
            "title": "Бонус без депозита — рынок Узбекистана 2026",
            "desc": "Запросы «бонус без депозита» и no deposit: что реально, а что маркетинг. Альтернатива — welcome FairPari, минимальный депозит, 18+.",
            "crumb": "Бонус без депозита",
            "headline": "Бонус без депозита — рынок Узбекистан",
        },
    },
    "tolov-uz": {
        "uz": {
            "title": "Humo, Uzcard, Payme — kazino to'lovlari O'zbekiston",
            "desc": "O'zbekistonda kazino to'lovlari: Humo, Uzcard, Click, Payme, kripto. Depozit va yechish vaqti, KYC, bonus faollashtirish. casino-bonuses-uz.com, 18+.",
            "crumb": "To'lovlar",
            "headline": "Kazino to'lovlari O'zbekiston",
        },
        "ru": {
            "title": "Humo, Uzcard, Payme — платежи казино Узбекистан",
            "desc": "Платежи казино в Узбекистане: Humo, Uzcard, Click, Payme, крипто. Депозит, вывод, KYC, активация бонуса. casino-bonuses-uz.com, 18+.",
            "crumb": "Платежи",
            "headline": "Платежи казино в Узбекистане",
        },
    },
    "faq": {
        "uz": {
            "title": "Kazino bonuslari FAQ — welcome, wagering, Humo | O'zbekiston",
            "desc": "Kazino bonuslari FAQ: welcome, depozitsiz bonus, wagering ×35, promo fa_1635, Humo/Payme, yechish. Javoblar casino-bonuses-uz.com portali, 18+.",
            "crumb": "FAQ",
            "headline": "Kazino bonuslari FAQ",
        },
        "ru": {
            "title": "FAQ по бонусам казино — Узбекистан 2026",
            "desc": "Ответы: welcome, бонус без депозита, wagering ×35, Humo/Payme, промокод fa_1635. Портал casino-bonuses-uz.com, 18+.",
            "crumb": "FAQ",
            "headline": "FAQ по бонусам казино",
        },
    },
}


def build_hub(slug: str, lang: str):
    meta = HUB_META[slug][lang]
    depth = 1
    base = ROOT / ("ru" if lang == "ru" else "") / slug
    base.mkdir(parents=True, exist_ok=True)
    path = base / "index.html"
    canonical = f"{DOMAIN}/{'ru/' if lang == 'ru' else ''}{slug}/"
    hreflang_uz = f"{DOMAIN}/{slug}/"
    hreflang_ru = f"{DOMAIN}/ru/{slug}/"
    html_lang = "ru-UZ" if lang == "ru" else "uz-UZ"
    home = "/ru/" if lang == "ru" else "/"
    crumb_home = "Главная" if lang == "ru" else "Bosh sahifa"
    body_content = hub_body(slug, lang)

    schema = json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "WebSite", "@id": f"{DOMAIN}/#website", "url": f"{DOMAIN}/",
             "name": "Casino Bonuses UZ", "inLanguage": html_lang},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": crumb_home, "item": home.rstrip("/") or DOMAIN},
                {"@type": "ListItem", "position": 2, "name": meta["crumb"], "item": canonical},
            ]},
            {"@type": "Article", "headline": meta["headline"], "description": meta["desc"],
             "inLanguage": html_lang, "url": canonical},
        ],
    }, ensure_ascii=False)

    extra_head = f'<script type="application/ld+json">{schema}</script>'
    html = f'''{head_block(lang, meta["title"], meta["desc"], canonical, href_uz=hreflang_uz, href_ru=hreflang_ru, depth=depth, extra_head=extra_head)}
<main id="main" class="container" style="padding:2rem 1rem">
{body_content}
</main>
{footer_block(lang, depth)}'''
    write_html(path, html)
    print(f"hub: {path.relative_to(ROOT)}")


def build_all_hubs():
    for slug in HUB_SLUGS:
        build_hub(slug, "uz")
        build_hub(slug, "ru")


def build_sitemap():
    from datetime import datetime

    def lastmod_for_path(rel_path: str) -> str:
        p = ROOT / rel_path
        if p.exists():
            return datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%d")
        return datetime.now().strftime("%Y-%m-%d")

    def hreflang_links(uz_loc: str, ru_loc: str) -> str:
        return (
            f'    <xhtml:link rel="alternate" hreflang="uz-UZ" href="{uz_loc}" />\n'
            f'    <xhtml:link rel="alternate" hreflang="ru-UZ" href="{ru_loc}" />\n'
            f'    <xhtml:link rel="alternate" hreflang="x-default" href="{uz_loc}" />'
        )

    page_groups: list[tuple[str, str, str, str, str]] = []  # uz_loc, ru_loc, pri, uz_rel, ru_rel

    def add_pair(uz_path: str, ru_path: str, pri: str, uz_rel: str, ru_rel: str):
        page_groups.append((f"{DOMAIN}{uz_path}", f"{DOMAIN}{ru_path}", pri, uz_rel, ru_rel))

    add_pair("/", "/ru/", "1.0", "index.html", "ru/index.html")

    for h in ["kazino-bonuslari", "welcome-bonus", "depozitsiz-bonus", "tolov-uz", "faq"]:
        add_pair(f"/{h}/", f"/ru/{h}/", "0.8", f"{h}/index.html", f"ru/{h}/index.html")

    for b in BRANDS:
        slug = b["slug"]
        add_pair(f"/{slug}/", f"/ru/{slug}/", "0.8", f"{slug}/index.html", f"ru/{slug}/index.html")

    legal_pairs = [
        ("maxfiylik-siyosati", "politika-konfidentsialnosti"),
        ("foydalanish-shartlari", "usloviya-ispolzovaniya"),
        ("cookie-siyosati", "politika-cookie"),
        ("masuliyatli-oyin", "otvetstvennaya-igra"),
    ]
    for uz_leg, ru_leg in legal_pairs:
        add_pair(f"/{uz_leg}", f"/ru/{ru_leg}", "0.3", f"{uz_leg}.html", f"ru/{ru_leg}.html")

    flat_entries: list[tuple[str, str, str]] = []
    for uz_loc, ru_loc, pri, uz_rel, ru_rel in page_groups:
        lm_uz = lastmod_for_path(uz_rel)
        lm_ru = lastmod_for_path(ru_rel)
        lm = max(lm_uz, lm_ru)
        flat_entries.append((uz_loc, pri, lm))
        flat_entries.append((ru_loc, pri, lm))

    # Root sitemap.xml (flat list for tools that read it directly)
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    seen: set[str] = set()
    for loc, pri, lm in flat_entries:
        if loc in seen:
            continue
        seen.add(loc)
        lines.append(f"  <url><loc>{loc}</loc><lastmod>{lm}</lastmod><priority>{pri}</priority></url>")
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # sitemaps/pages.xml with hreflang (referenced from robots.txt via sitemap_index.xml)
    page_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    ]
    for uz_loc, ru_loc, pri, uz_rel, ru_rel in page_groups:
        lm = max(lastmod_for_path(uz_rel), lastmod_for_path(ru_rel))
        links = hreflang_links(uz_loc, ru_loc)
        for loc in (uz_loc, ru_loc):
            page_lines.append("  <url>")
            page_lines.append(f"    <loc>{loc}</loc>")
            page_lines.append(f"    <lastmod>{lm}</lastmod>")
            page_lines.append(f"    <priority>{pri}</priority>")
            page_lines.append(links)
            page_lines.append("  </url>")
    page_lines.append("</urlset>")
    pages_path = ROOT / "sitemaps" / "pages.xml"
    pages_path.parent.mkdir(parents=True, exist_ok=True)
    pages_path.write_text("\n".join(page_lines) + "\n", encoding="utf-8")

    # Refresh lastmod in images sitemap
    images_path = ROOT / "sitemaps" / "images.xml"
    if images_path.exists():
        img_lm = lastmod_for_path("index.html")
        images_path.write_text(
            images_path.read_text(encoding="utf-8").replace("2026-06-10", img_lm),
            encoding="utf-8",
        )

    # sitemap_index.xml
    index_lm = max(lastmod_for_path("index.html"), lastmod_for_path("sitemaps/pages.xml"))
    (ROOT / "sitemap_index.xml").write_text(
        "\n".join([
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
            "  <sitemap>",
            f"    <loc>{DOMAIN}/sitemaps/pages.xml</loc>",
            f"    <lastmod>{index_lm}</lastmod>",
            "  </sitemap>",
            "  <sitemap>",
            f"    <loc>{DOMAIN}/sitemaps/images.xml</loc>",
            f"    <lastmod>{lastmod_for_path('sitemaps/images.xml')}</lastmod>",
            "  </sitemap>",
            "</sitemapindex>",
            "",
        ]),
        encoding="utf-8",
    )

    print(f"sitemap.xml updated ({len(seen)} urls)")
    print(f"sitemaps/pages.xml updated ({len(page_groups) * 2} urls with hreflang)")


def audit_i18n():
    cyr = re.compile(r"[а-яА-ЯёЁ]")
    uz = re.compile(r"\b(siyosati|shartlari|qanday|bonuslari|depozit|kazino|o'yin|to'lov|bosh sahifa|reyting)\b", re.I)
    issues = []
    for f in ROOT.rglob("*.html"):
        rel = str(f.relative_to(ROOT))
        if "assets" in rel or " 2" in rel:
            continue
        text = f.read_text(encoding="utf-8", errors="ignore")
        body = re.sub(r"<script.*?</script>", "", text, flags=re.S | re.I)
        body = re.sub(r"<[^>]+>", " ", body)
        is_ru = rel.startswith("ru/") or "lang=\"ru" in text[:500]
        is_uz = not is_ru and ('lang="uz' in text[:500] or rel in (
            "index.html", "cookie-siyosati.html", "foydalanish-shartlari.html",
            "masuliyatli-oyin.html", "maxfiylik-siyosati.html"
        ) or ("/" in rel and not rel.startswith("ru")))
        if is_ru and uz.search(body):
            issues.append(f"RU has UZ: {rel}")
        if is_uz and not rel.startswith("ru") and cyr.search(body):
            # allow brand names only in tiny amounts - flag if many cyr chars
            if len(cyr.findall(body)) > 3:
                issues.append(f"UZ has CYR: {rel}")
    return issues


def main():
    ensure_logos()
    build_index("uz")
    build_index("ru")
    for i, b in enumerate(BRANDS):
        build_review(b, i + 1, "uz")
        build_review(b, i + 1, "ru")
    build_all_hubs()
    build_sitemap()
    issues = audit_i18n()
    if issues:
        print("i18n warnings:", len(issues))
        for x in issues[:15]:
            print(" ", x)
    else:
        print("i18n: OK")
    print("Done:", len(BRANDS), "brands × 2 langs")


if __name__ == "__main__":
    main()
