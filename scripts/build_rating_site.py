#!/usr/bin/env python3
"""Rebuild casino-bonuses-uz.com: 20 brands, casino.ru card UI, SEO, i18n."""
from __future__ import annotations
import json
import re
from pathlib import Path
from html import escape

from brand_qttk_content import render_body, faq_schema

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://casino-bonuses-uz.com"
CSS_V = "20260618b"
PARTNER = "https://bobaffs.org/click?o=1603&a=189"

# 20 brands popular in Google UZ (casino + BK)
BRANDS = [
    {"slug": "fairpari", "name": "FairPari", "rating": 5.0, "type": "both",
     "welcome_uz": "20 200 000 UZS + 150 FS", "welcome_ru": "20 200 000 UZS + 150 FS",
     "wagering": "×35", "pay": "Humo, Payme, Click",
     "pros_uz": ["Eng katta kazino welcome UZ", "Mahalliy to'lovlar", "APK va PWA"],
     "cons_uz": ["Sport va kazino welcome bir vaqtda emas"],
     "pros_ru": ["Крупнейший welcome в UZ", "Локальные платежи", "APK и PWA"],
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
    {"slug": "linebet", "name": "Linebet", "rating": 4.4, "type": "bk",
     "welcome_uz": "4 800 000 UZS sport", "welcome_ru": "4 800 000 UZS спорт",
     "wagering": "×5", "pay": "Humo, Click",
     "pros_uz": ["Sport welcome ×5", "Ekspress aksiyalar"],
     "cons_uz": ["Kazino tanlovi cheklangan"],
     "pros_ru": ["Спорт welcome ×5", "Экспресс-акции"],
     "cons_ru": ["Ограниченный казино-раздел"],
     "tags_uz": ["Sport", "Live stavka"], "tags_ru": ["Спорт", "Live-ставки"]},
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
    {"slug": "parimatch", "name": "Parimatch", "rating": 4.2, "type": "bk",
     "welcome_uz": "3 800 000 UZS sport", "welcome_ru": "3 800 000 UZS спорт",
     "wagering": "×5", "pay": "Humo, Payme",
     "pros_uz": ["Sport brend", "Live koeffitsientlar"],
     "cons_uz": ["Kazino bonus cheklangan"],
     "pros_ru": ["Спортивный бренд", "Live-коэффициенты"],
     "cons_ru": ["Ограниченный казино-бонус"],
     "tags_uz": ["Sport", "Live"], "tags_ru": ["Спорт", "Live"]},
    {"slug": "leon", "name": "Leon", "rating": 4.2, "type": "bk",
     "welcome_uz": "3 500 000 UZS", "welcome_ru": "3 500 000 UZS",
     "wagering": "×5", "pay": "Humo, Click",
     "pros_uz": ["Oddiy interfeys", "Sport fokus"],
     "cons_uz": ["Kichik welcome"],
     "pros_ru": ["Простой интерфейс", "Фокус на спорт"],
     "cons_ru": ["Небольшой welcome"],
     "tags_uz": ["Sport"], "tags_ru": ["Спорт"]},
    {"slug": "fonbet", "name": "Fonbet", "rating": 4.1, "type": "bk",
     "welcome_uz": "3 200 000 UZS sport", "welcome_ru": "3 200 000 UZS спорт",
     "wagering": "×5", "pay": "Humo, Uzcard",
     "pros_uz": ["Tajribali BK", "Live matnlar"],
     "cons_uz": ["UZ kazino cheklangan"],
     "pros_ru": ["Опытный БК", "Live-трансляции"],
     "cons_ru": ["Казино в UZ ограничено"],
     "tags_uz": ["Sport", "Live"], "tags_ru": ["Спорт", "Live"]},
    {"slug": "marathonbet", "name": "Marathonbet", "rating": 4.1, "type": "bk",
     "welcome_uz": "3 000 000 UZS", "welcome_ru": "3 000 000 UZS",
     "wagering": "×5", "pay": "Humo, Payme",
     "pros_uz": ["Yuqori koeffitsientlar", "Sport ekspertiza"],
     "cons_uz": ["Kazino bo'limi kichik"],
     "pros_ru": ["Высокие коэффициенты", "Спортивная экспертиза"],
     "cons_ru": ["Малый раздел казино"],
     "tags_uz": ["Sport"], "tags_ru": ["Спорт"]},
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
     "wagering": "×35", "pay": "Humo, Click",
     "pros_uz": ["Yangi platforma", "Slot turnirlari"],
     "cons_uz": ["Kam sharhlar UZ"],
     "pros_ru": ["Новая платформа", "Турниры на слотах"],
     "cons_ru": ["Мало отзывов в UZ"],
     "tags_uz": ["Slotlar", "Sport"], "tags_ru": ["Слоты", "Спорт"]},
    {"slug": "vulkan-vegas", "name": "Vulkan Vegas", "rating": 4.0, "type": "casino",
     "welcome_uz": "3 400 000 UZS + 150 FS", "welcome_ru": "3 400 000 UZS + 150 FS",
     "wagering": "×40", "pay": "Humo, Payme",
     "pros_uz": ["Kazino fokus", "Ko'p slot provayderlar"],
     "cons_uz": ["Sport yo'q", "×40 wagering"],
     "pros_ru": ["Фокус на казино", "Много провайдеров"],
     "cons_ru": ["Нет спорта", "Вейджер ×40"],
     "tags_uz": ["Slotlar", "Live kazino"], "tags_ru": ["Слоты", "Live-казино"]},
    {"slug": "joycasino", "name": "Joycasino", "rating": 3.9, "type": "casino",
     "welcome_uz": "3 000 000 UZS + 200 FS", "welcome_ru": "3 000 000 UZS + 200 FS",
     "wagering": "×40", "pay": "Humo, Uzcard",
     "pros_uz": ["200 FS", "Slot aksiyalar"],
     "cons_uz": ["Faqat kazino", "Yuqori wagering"],
     "pros_ru": ["200 FS", "Акции на слоты"],
     "cons_ru": ["Только казино", "Высокий вейджер"],
     "tags_uz": ["Slotlar"], "tags_ru": ["Слоты"]},
    {"slug": "fresh-casino", "name": "Fresh Casino", "rating": 3.9, "type": "casino",
     "welcome_uz": "2 900 000 UZS + 100 FS", "welcome_ru": "2 900 000 UZS + 100 FS",
     "wagering": "×35", "pay": "Payme, Click",
     "pros_uz": ["Zamonaviy dizayn", "Tez ro'yxat"],
     "cons_uz": ["Kichik welcome"],
     "pros_ru": ["Современный дизайн", "Быстрая регистрация"],
     "cons_ru": ["Небольшой welcome"],
     "tags_uz": ["Slotlar", "Crash"], "tags_ru": ["Слоты", "Crash"]},
    {"slug": "bc-game", "name": "BC.Game", "rating": 3.8, "type": "casino",
     "welcome_uz": "Kripto paket USDT", "welcome_ru": "Крипто-пакет USDT",
     "wagering": "×45", "pay": "USDT, BTC",
     "pros_uz": ["Kripto kazino", "Provably fair o'yinlar"],
     "cons_uz": ["Humo yo'q", "Yuqori wagering"],
     "pros_ru": ["Крипто-казино", "Provably fair"],
     "cons_ru": ["Нет Humo", "Высокий вейджер"],
     "tags_uz": ["Kripto", "Crash", "Slotlar"], "tags_ru": ["Крипто", "Crash", "Слоты"]},
]

STAR = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>'


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


def card_html(b: dict, rank: int, lang: str) -> str:
    prefix = "/ru/" if lang == "ru" else "/"
    logo = f"{'../' if lang == 'ru' else ''}{logo_path(b['slug'])}"
    welcome = b["welcome_ru"] if lang == "ru" else b["welcome_uz"]
    pros = b["pros_ru"] if lang == "ru" else b["pros_uz"]
    cons = b["cons_ru"] if lang == "ru" else b["cons_uz"]
    tags = b["tags_ru"] if lang == "ru" else b["tags_uz"]
    t = b["type"]
    type_label = {"both": ("Kazino + BK", "Казино + БК"), "bk": ("Bukmeker", "Букмекер"), "casino": ("Kazino", "Казино")}[t][1 if lang == "ru" else 0]
    btn_get = "Получить" if lang == "ru" else "Olish"
    btn_review = "Обзор" if lang == "ru" else "Sharh"
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
    <img class="casino-card__logo" src="{logo}" alt="{escape(b["name"])}" width="64" height="64" loading="lazy" />
  </div>
  <div class="casino-card__body">
    <div class="casino-card__head">
      <h3 class="casino-card__title"><a href="{prefix}{b["slug"]}/">{escape(b["name"])}</a></h3>
      <div class="casino-card__score">{STAR}<span>{b["rating"]:.1f}</span></div>
    </div>
    <div class="casino-card__badges">{hit}<span class="casino-card__badge casino-card__badge--type">{type_label}</span></div>
    <p class="casino-card__bonus-line">{escape(welcome)} <span class="casino-card__bonus-hint">wagering {b["wagering"]}</span></p>
    <div class="casino-card__proscons">
      <ul class="casino-card__pros">{pros_li}</ul>
      <ul class="casino-card__cons">{cons_li}</ul>
    </div>
    <div class="casino-card__tags">{tags_html}</div>
    <p class="casino-card__pay"><strong>{pay_label}:</strong> {escape(b["pay"])}</p>
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
        title = "O'zbekistonda eng yaxshi kazino va BK bonuslari — 2026 reytingi"
        count = f'Topildi: <strong data-rating-visible>20</strong> / <strong>20</strong> operator'
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


def head_block(lang: str, title: str, desc: str, url: str, extra_css: str = "", href_uz: str = "", href_ru: str = "") -> str:
    if not href_uz:
        href_uz = f"{DOMAIN}/"
    if not href_ru:
        href_ru = f"{DOMAIN}/ru/"
    canonical = url
    og_loc = "ru_UZ" if lang == "ru" else "uz_UZ"
    html_lang = "ru-UZ" if lang == "ru" else "uz-UZ"
    switch_href = "/" if lang == "ru" else "/ru/"
    switch_label = "UZ" if lang == "ru" else "RU"
    switch_lang = "uz-UZ" if lang == "ru" else "ru-UZ"
    if lang == "ru":
        nav = '<a href="/ru/#rating">Рейтинг</a><a href="/ru/kazino-bonuslari/">Типы бонусов</a><a href="/ru/fairpari/">FairPari</a><a href="/ru/faq/">FAQ</a>'
        home = "/ru/"
        cta = "Получить бонус"
        brand_alt = "Casino Bonuses UZ"
    else:
        nav = '<a href="#rating">Reyting</a><a href="kazino-bonuslari/">Bonus turlari</a><a href="fairpari/">FairPari</a><a href="faq/">FAQ</a>'
        home = "/"
        cta = "Bonus olish"
        brand_alt = "Casino Bonuses UZ"
    css_base = f'../css' if lang == "ru" else 'css'
    assets = f'{css_base}/../assets' if lang == "ru" else 'assets'
    return f'''<!DOCTYPE html>
<html lang="{html_lang}" data-site="rating-light">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="#ffffff" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(desc)}" />
  <link rel="icon" href="{assets}/favicon.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="{css_base}/style.css?v={CSS_V}" />
  <link rel="stylesheet" href="{css_base}/fairpari-light-theme.css?v={CSS_V}" />
  <link rel="stylesheet" href="{css_base}/rating-cards.css?v={CSS_V}" />
  {extra_css}
  <link rel="canonical" href="{canonical}" />
  <link rel="alternate" hreflang="uz-UZ" href="{href_uz}" />
  <link rel="alternate" hreflang="ru-UZ" href="{href_ru}" />
  <link rel="alternate" hreflang="x-default" href="{href_uz}" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Casino Bonuses UZ" />
  <meta property="og:title" content="{escape(title)}" />
  <meta property="og:description" content="{escape(desc)}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:image" content="{DOMAIN}/assets/hero-bonus-light.webp" />
  <meta property="og:image:alt" content="{escape(brand_alt)}" />
  <meta property="og:locale" content="{og_loc}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{escape(title)}" />
  <meta name="twitter:description" content="{escape(desc)}" />
  <meta name="twitter:image" content="{DOMAIN}/assets/hero-bonus-light.webp" />
</head>
<body class="site-fairpari-light">
<header class="site-header"><div class="site-header__inner">
  <a class="brand" href="{home}"><img src="{assets}/logo-fairpari.svg" alt="{brand_alt}" width="132" height="20" /></a>
  <nav class="nav-desktop">{nav}<a class="lang-switch" href="{switch_href}" hreflang="{switch_lang}" style="margin-left:12px;font-weight:600">{switch_label}</a></nav>
  <button type="button" class="btn btn--gold js-go-partner">{cta}</button>
</div></header>'''


def footer_block(lang: str) -> str:
    css_base = "../css" if lang == "ru" else "css"
    if lang == "ru":
        links = '''<a href="/ru/">Главная</a>
<a href="/ru/kazino-bonuslari/">Типы бонусов</a>
<a href="/ru/fairpari/">FairPari</a>
<a href="/ru/faq/">FAQ</a>'''
        legal = '''<a href="/ru/politika-konfidentsialnosti">Конфиденциальность</a>
<a href="/ru/usloviya-ispolzovaniya">Условия</a>
<a href="/ru/politika-cookie">Cookie</a>
<a href="/ru/otvetstvennaya-igra">Ответственная игра</a>'''
        disc = "18+. casino-bonuses-uz.com — независимый рейтинг. Не оператор."
        sticky = ("Стартовый пакет:", "20,2 млн UZS + 150 фриспинов", "Активировать", "Закрыть")
        skip = ""
        nav_aria = "Разделы"
    else:
        links = '''<a href="/">Bosh sahifa</a>
<a href="kazino-bonuslari/">Kazino bonuslari</a>
<a href="fairpari/">FairPari</a>
<a href="faq/">FAQ</a>'''
        legal = '''<a href="/maxfiylik-siyosati">Maxfiylik</a>
<a href="/foydalanish-shartlari">Shartlar</a>
<a href="/cookie-siyosati">Cookie</a>
<a href="/masuliyatli-oyin">Mas'uliyatli o'yin</a>'''
        disc = "18+. casino-bonuses-uz.com — mustaqil reyting. Operator emas."
        sticky = ("Start paketi:", "20,2 mln UZS + 150 frispin", "Faollashtirish", "Yopish")
        skip_label = "Asosiy kontentga o'tish"
        skip = f'<a class="skip-link" href="#main">{skip_label}</a>\n'
        nav_aria = "Sayt bo'limlari"
    return f'''{skip}<nav class="footer-links footer-links--audit" aria-label="{nav_aria}">
{links}
</nav>
<footer class="site-footer"><div class="container">
  <nav class="footer-legal">{legal}</nav>
  <p class="footer-disclaimer">{disc}</p>
</div></footer>
<script src="{css_base}/../js/partner.js?v={CSS_V}"></script>
<script src="{css_base}/../js/main.js?v={CSS_V}"></script>
<script src="{css_base}/../js/rating-filter.js?v={CSS_V}"></script>
<aside class="sticky-cta sticky-cta--dock" id="sticky-cta" role="complementary">
  <div class="sticky-cta__panel">
    <p class="sticky-cta__text"><span class="sticky-cta__prefix">{sticky[0]}</span> <strong class="sticky-cta__highlight">{sticky[1]}</strong></p>
    <button type="button" class="btn btn--gold sticky-cta__btn js-go-partner">{sticky[2]}</button>
    <button type="button" class="sticky-cta__close" aria-label="{sticky[3]}">×</button>
  </div>
</aside>
</body></html>'''


def build_index(lang: str):
    if lang == "ru":
        path = ROOT / "ru/index.html"
        title = "Лучшие бонусы казино Узбекистан — рейтинг ТОП-20 2026"
        desc = "Рейтинг 20 казино и БК Узбекистан 2026: welcome-бонусы, wagering, Humo/Payme. FairPari №1 — 20,2 млн UZS + 150 FS. 18+."
        url = f"{DOMAIN}/ru/"
        hero_h1 = "ТОП-20 бонусов казино и БК <em>Узбекистан 2026</em>"
        hero_sub = "Welcome-пакеты, wagering и Humo/Payme — независимый рейтинг casino.ru-стиля."
        hero_btn = "Бонус FairPari №1"
        img = "../assets/hero-bonus-light.webp"
        img_alt = "Бонусы казино Узбекистан"
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
        title = "O'zbekistonda eng yaxshi kazino bonuslari — TOP-20 2026"
        desc = "20 ta kazino va BK reytingi O'zbekiston 2026: welcome bonuslar, wagering, Humo/Payme. FairPari #1 — 20,2 mln UZS + 150 FS. 18+."
        url = f"{DOMAIN}/"
        hero_h1 = "TOP-20 kazino va BK bonuslari <em>O'zbekiston 2026</em>"
        hero_sub = "Welcome paketlar, wagering va Humo/Payme — casino.ru uslubida mustaqil reyting."
        hero_btn = "#1 FairPari bonus"
        img = "assets/hero-bonus-light.webp"
        img_alt = "Kazino bonuslari O'zbekiston"
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
    crit_text = "Бонус, wagering, UZS, платежи Humo/Payme, мобильное приложение, лицензия." if lang == "ru" else "Bonus hajmi, wagering, UZS, Humo/Payme to'lovlar, mobil ilova, litsenziya."
    resp_title = "Ответственная игра 18+" if lang == "ru" else "Mas'uliyatli o'yin 18+"
    resp_link = "/ru/otvetstvennaya-igra" if lang == "ru" else "/masuliyatli-oyin"
    resp_label = "Ответственная игра" if lang == "ru" else "Mas'uliyatli o'yin"
    resp_prefix = "Играйте ответственно. " if lang == "ru" else ""
    body = f'''{head_block(lang, title, desc, url, extra, href_uz=url if lang != "ru" else f"{DOMAIN}/", href_ru=f"{DOMAIN}/ru/")}
<main id="main">
<section class="hero"><div class="container hero__slide-inner hero__slide-inner--split">
  <div class="hero__copy">
    <h1 class="hero__title">{hero_h1}</h1>
    <p class="hero__subtitle">{hero_sub}</p>
    <button type="button" class="btn btn--gold btn--lg js-go-partner">{hero_btn}</button>
  </div>
  <figure class="hero__art"><img src="{img}" alt="{img_alt}" loading="eager" /></figure>
</div></section>
{rating_section(lang)}
<section class="section section--alt" id="criteria"><div class="container">
  <h2 class="section__title">{crit_title}</h2>
  <p>{crit_text}</p>
</div></section>
<section class="section" id="responsible"><div class="container">
  <h2 class="section__title">{resp_title}</h2>
  <p>{resp_prefix}<a href="{resp_link}">{resp_label}</a>.</p>
</div></section>
</main>
{footer_block(lang)}'''
    path.write_text(body, encoding="utf-8")
    print(f"index: {path.relative_to(ROOT)}")


def build_review(b: dict, rank: int, lang: str):
    slug = b["slug"]
    prefix = "../" if lang == "ru" else ""
    base = ROOT / ("ru" if lang == "ru" else "") / slug
    base.mkdir(parents=True, exist_ok=True)
    path = base / "index.html"
    welcome = b["welcome_ru"] if lang == "ru" else b["welcome_uz"]
    pros = b["pros_ru"] if lang == "ru" else b["pros_uz"]
    cons = b["cons_ru"] if lang == "ru" else b["cons_uz"]
    alt_lang = "uz" if lang == "ru" else "ru"
    alt_path = f"/{slug}/" if lang == "ru" else f"/ru/{slug}/"
    canonical = f"{DOMAIN}/{'ru/' if lang == 'ru' else ''}{slug}/"

    if lang == "ru":
        title = f"{b['name']} бонус — обзор казино/БК #{rank} Узбекистан 2026"
        desc = f"{b['name']} в Узбекистане: welcome {welcome}, wagering {b['wagering']}, {b['pay']}. Независимый обзор #{rank}, 18+."
        h1 = f"{b['name']} — обзор бонусов (#{rank})"
        crumb_home, crumb = "Главная", b["name"]
        rank_lbl, welcome_lbl, wag_lbl, pay_lbl = "Позиция", "Welcome", "Вейджер", "Платёж"
        pros_h, cons_h = "Плюсы", "Минусы"
        cta = "Получить бонус"
        back = f'<a href="/ru/#rating">← К рейтингу</a>'
        compare = f'Сравните с <a href="/ru/fairpari/">FairPari №1</a> — 20,2 млн UZS + 150 FS.'
        body_intro = f"<strong>{b['name']}</strong> в нашем рейтинге <strong>#{rank}</strong>. Welcome: <strong>{welcome}</strong>, вейджер <strong>{b['wagering']}</strong>."
        switch_href, switch = f"/{slug}/", "UZ"
    else:
        title = f"{b['name']} kazino bonusi — #{rank} sharh O'zbekiston 2026"
        desc = f"{b['name']} O'zbekistonda: welcome {welcome}, wagering {b['wagering']}, {b['pay']}. Mustaqil #{rank} sharh, 18+."
        h1 = f"{b['name']} — bonus sharhi (#{rank})"
        crumb_home, crumb = "Bosh sahifa", b["name"]
        rank_lbl, welcome_lbl, wag_lbl, pay_lbl = "Reyting", "Welcome", "Wagering", "To'lov"
        pros_h, cons_h = "Afzalliklar", "Kamchiliklar"
        cta = "Bonusni olish"
        back = f'<a href="/#rating">← Reytingga</a>'
        compare = f'<a href="/fairpari/">FairPari #1</a> bilan solishtiring — 20,2 mln UZS + 150 FS.'
        body_intro = f"<strong>{b['name']}</strong> reytingimizda <strong>#{rank}</strong>. Welcome: <strong>{welcome}</strong>, wagering <strong>{b['wagering']}</strong>."
        switch_href, switch = f"/ru/{slug}/", "RU"

    pros_ul = "".join(f"<li>{escape(p)}</li>" for p in pros)
    cons_ul = "".join(f"<li>{escape(c)}</li>" for c in cons)
    logo = f"{prefix}{logo_path(slug)}"
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

    hreflang_uz = f"{DOMAIN}/{slug}/"
    hreflang_ru = f"{DOMAIN}/ru/{slug}/"
    html_lang = "ru-UZ" if lang == "ru" else "uz-UZ"
    css_base = "../css" if lang == "ru" else "css"
    home = "/ru/" if lang == "ru" else "/"
    nav_ru = lang == "ru"

    html = f'''<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<meta name="robots" content="index, follow, max-image-preview:large"/>
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}"/>
<link rel="stylesheet" href="{css_base}/style.css?v={CSS_V}"/>
<link rel="stylesheet" href="{css_base}/fairpari-light-theme.css?v={CSS_V}"/>
<link rel="canonical" href="{canonical}"/>
<link rel="alternate" hreflang="uz-UZ" href="{hreflang_uz}"/>
<link rel="alternate" hreflang="ru-UZ" href="{hreflang_ru}"/>
<link rel="alternate" hreflang="x-default" href="{hreflang_uz}"/>
<meta property="og:type" content="article"/>
<meta property="og:site_name" content="Casino Bonuses UZ"/>
<meta property="og:title" content="{escape(title)}"/>
<meta property="og:description" content="{escape(desc)}"/>
<meta property="og:url" content="{canonical}"/>
<meta property="og:image" content="{DOMAIN}/assets/hero-bonus-light.webp"/>
<meta property="og:locale" content="{'ru_UZ' if lang == 'ru' else 'uz_UZ'}"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{escape(title)}"/>
<meta name="twitter:description" content="{escape(desc)}"/>
<script type="application/ld+json">{schema}</script>
<script type="application/ld+json">{faq_ld}</script>
</head>
<body class="site-fairpari-light">
<header class="site-header"><div class="site-header__inner">
<a class="brand" href="{home}"><img src="{prefix}assets/logo-fairpari.svg" alt="Casino Bonuses UZ" width="132" height="20"/></a>
<nav class="nav-desktop">
<a href="{home}#rating">{"Рейтинг" if nav_ru else "Reyting"}</a>
<a href="{home}{"kazino-bonuslari/" if not nav_ru else "kazino-bonuslari/"}">{"Типы бонусов" if nav_ru else "Bonus turlari"}</a>
<a href="{home}fairpari/">FairPari</a>
<a class="lang-switch" href="{switch_href}" hreflang="{'uz-UZ' if lang == 'ru' else 'ru-UZ'}" style="margin-left:12px;font-weight:600">{switch}</a>
</nav>
<button type="button" class="btn btn--gold js-go-partner">{"Получить бонус" if nav_ru else "Bonus olish"}</button>
</div></header>
<main id="main" class="container" style="padding:2rem 1rem">
<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="{home}">{crumb_home}</a> / <span>{crumb}</span></nav>
{article_body}
</main>
{footer_block(lang)}'''
    path.write_text(html, encoding="utf-8")


def build_sitemap():
    from datetime import datetime

    def lastmod_for_path(rel_path: str) -> str:
        p = ROOT / rel_path
        if p.exists():
            return datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%d")
        return "2026-06-18"

    entries: list[tuple[str, str, str]] = []  # loc, priority, lastmod

    def add(loc: str, pri: str, rel: str):
        entries.append((loc, pri, lastmod_for_path(rel)))

    add(f"{DOMAIN}/", "1.0", "index.html")
    add(f"{DOMAIN}/ru/", "1.0", "ru/index.html")

    hubs = ["kazino-bonuslari", "welcome-bonus", "depozitsiz-bonus", "tolov-uz", "faq"]
    for h in hubs:
        add(f"{DOMAIN}/{h}/", "0.8", f"{h}/index.html")
        add(f"{DOMAIN}/ru/{h}/", "0.8", f"ru/{h}/index.html")

    for b in BRANDS:
        slug = b["slug"]
        add(f"{DOMAIN}/{slug}/", "0.8", f"{slug}/index.html")
        add(f"{DOMAIN}/ru/{slug}/", "0.8", f"ru/{slug}/index.html")

    for leg in ["cookie-siyosati", "foydalanish-shartlari", "masuliyatli-oyin", "maxfiylik-siyosati"]:
        add(f"{DOMAIN}/{leg}", "0.3", f"{leg}.html")
    for leg in ["politika-konfidentsialnosti", "usloviya-ispolzovaniya", "politika-cookie", "otvetstvennaya-igra"]:
        add(f"{DOMAIN}/ru/{leg}", "0.3", f"ru/{leg}.html")

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    seen: set[str] = set()
    for loc, pri, lm in entries:
        if loc in seen:
            continue
        seen.add(loc)
        lines.append(f"  <url><loc>{loc}</loc><lastmod>{lm}</lastmod><priority>{pri}</priority></url>")
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"sitemap.xml updated ({len(seen)} urls)")


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
