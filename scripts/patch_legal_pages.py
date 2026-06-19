#!/usr/bin/env python3
"""Rebuild legal *.html shells with unified header, footer, sticky, CSS."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from build_rating_site import DOMAIN, footer_block, head_block  # noqa: E402

UPDATED = "2026-06-18"

LEGAL = [
    ("maxfiylik-siyosati.html", "uz", "privacy",
     "https://casino-bonuses-uz.com/maxfiylik-siyosati",
     "https://casino-bonuses-uz.com/maxfiylik-siyosati",
     "https://casino-bonuses-uz.com/ru/politika-konfidentsialnosti"),
    ("foydalanish-shartlari.html", "uz", "terms",
     "https://casino-bonuses-uz.com/foydalanish-shartlari",
     "https://casino-bonuses-uz.com/foydalanish-shartlari",
     "https://casino-bonuses-uz.com/ru/usloviya-ispolzovaniya"),
    ("cookie-siyosati.html", "uz", "cookie",
     "https://casino-bonuses-uz.com/cookie-siyosati",
     "https://casino-bonuses-uz.com/cookie-siyosati",
     "https://casino-bonuses-uz.com/ru/politika-cookie"),
    ("masuliyatli-oyin.html", "uz", "responsible",
     "https://casino-bonuses-uz.com/masuliyatli-oyin",
     "https://casino-bonuses-uz.com/masuliyatli-oyin",
     "https://casino-bonuses-uz.com/ru/otvetstvennaya-igra"),
    ("ru/politika-konfidentsialnosti.html", "ru", "privacy",
     "https://casino-bonuses-uz.com/ru/politika-konfidentsialnosti",
     "https://casino-bonuses-uz.com/maxfiylik-siyosati",
     "https://casino-bonuses-uz.com/ru/politika-konfidentsialnosti"),
    ("ru/usloviya-ispolzovaniya.html", "ru", "terms",
     "https://casino-bonuses-uz.com/ru/usloviya-ispolzovaniya",
     "https://casino-bonuses-uz.com/foydalanish-shartlari",
     "https://casino-bonuses-uz.com/ru/usloviya-ispolzovaniya"),
    ("ru/politika-cookie.html", "ru", "cookie",
     "https://casino-bonuses-uz.com/ru/politika-cookie",
     "https://casino-bonuses-uz.com/cookie-siyosati",
     "https://casino-bonuses-uz.com/ru/politika-cookie"),
    ("ru/otvetstvennaya-igra.html", "ru", "responsible",
     "https://casino-bonuses-uz.com/ru/otvetstvennaya-igra",
     "https://casino-bonuses-uz.com/masuliyatli-oyin",
     "https://casino-bonuses-uz.com/ru/otvetstvennaya-igra"),
]

META = {
    "privacy": {
        "ru": {
            "title": "Политика конфиденциальности — Casino Bonuses UZ",
            "desc": "Политика конфиденциальности casino-bonuses-uz.com: какие данные собираются, cookie, безопасность и права пользователя. 18+.",
            "h1": "Политика конфиденциальности",
            "crumb": "Конфиденциальность",
            "home": "Главная",
        },
        "uz": {
            "title": "Maxfiylik siyosati — Casino Bonuses UZ",
            "desc": "casino-bonuses-uz.com maxfiylik siyosati: qanday ma'lumotlar to'planadi, cookie, xavfsizlik va foydalanuvchi huquqlari. 18+.",
            "h1": "Maxfiylik siyosati",
            "crumb": "Maxfiylik siyosati",
            "home": "Bosh sahifa",
        },
    },
    "terms": {
        "ru": {
            "title": "Условия использования — Casino Bonuses UZ",
            "desc": "Условия использования casino-bonuses-uz.com: независимый рейтинг, ограничение 18+, отказ от ответственности, интеллектуальная собственность.",
            "h1": "Условия использования",
            "crumb": "Условия использования",
            "home": "Главная",
        },
        "uz": {
            "title": "Foydalanish shartlari — Casino Bonuses UZ",
            "desc": "casino-bonuses-uz.com foydalanish shartlari: mustaqil reyting, 18+ cheklov, javobgarlikdan voz kechish, intellektual mulk.",
            "h1": "Foydalanish shartlari",
            "crumb": "Foydalanish shartlari",
            "home": "Bosh sahifa",
        },
    },
    "cookie": {
        "ru": {
            "title": "Политика cookie — Casino Bonuses UZ",
            "desc": "Политика cookie casino-bonuses-uz.com: какие cookie используются, как ими управлять и о сторонних cookie.",
            "h1": "Политика cookie",
            "crumb": "Политика cookie",
            "home": "Главная",
        },
        "uz": {
            "title": "Cookie siyosati — Casino Bonuses UZ",
            "desc": "casino-bonuses-uz.com cookie siyosati: qanday cookie ishlatiladi, ularni qanday boshqarish va uchinchi tomon cookie haqida.",
            "h1": "Cookie siyosati",
            "crumb": "Cookie siyosati",
            "home": "Bosh sahifa",
        },
    },
    "responsible": {
        "ru": {
            "title": "Ответственная игра — Casino Bonuses UZ",
            "desc": "Ответственная игра 18+: признаки проблемной игры, лимиты, самоисключение и помощь. Независимый рейтинг casino-bonuses-uz.com.",
            "h1": "Ответственная игра",
            "crumb": "Ответственная игра",
            "home": "Главная",
        },
        "uz": {
            "title": "Mas'uliyatli o'yin — Casino Bonuses UZ",
            "desc": "Mas'uliyatli o'yin 18+: muammoli o'yin belgilari, limitlar, o'z-o'zini chetlashtirish va yordam. Mustaqil reyting casino-bonuses-uz.com.",
            "h1": "Mas'uliyatli o'yin",
            "crumb": "Mas'uliyatli o'yin",
            "home": "Bosh sahifa",
        },
    },
}


def _legal_nav(lang: str) -> str:
    if lang == "ru":
        return """<nav class="legal-doc__nav">
<a href="/ru/politika-konfidentsialnosti">Конфиденциальность</a>
<a href="/ru/usloviya-ispolzovaniya">Условия</a>
<a href="/ru/politika-cookie">Cookie</a>
<a href="/ru/otvetstvennaya-igra">Ответственная игра</a>
</nav>"""
    return """<nav class="legal-doc__nav">
<a href="/maxfiylik-siyosati">Maxfiylik</a>
<a href="/foydalanish-shartlari">Shartlar</a>
<a href="/cookie-siyosati">Cookie</a>
<a href="/masuliyatli-oyin">Mas'uliyatli o'yin</a>
</nav>"""


def _article_body(kind: str, lang: str) -> str:
    if kind == "privacy":
        if lang == "ru":
            return f"""<h2>Общие сведения</h2>
<p>casino-bonuses-uz.com — независимый рейтинг казино и БК Узбекистана. Мы не оператор, не принимаем депозиты и не предоставляем азартные услуги. Политика действует только для этого домена.</p>
<h2>Какие данные собираются</h2>
<p>Сайт статический. В технических журналах могут фиксироваться: IP-адрес, браузер, время визита, URL и referrer. Регистрация на сайте не требуется; данные карт и паспортов не собираются.</p>
<h2>Cookie и аналитика</h2>
<p>Cookie используются для работы сайта и выбора языка. Их можно ограничить в браузере. Аналитика — только в агрегированном виде, если подключена.</p>
<h2>Защита данных</h2>
<p>Передача по HTTPS (SSL/TLS). Журналы хранятся ограниченное время для безопасности и диагностики.</p>
<h2>Сторонние ссылки</h2>
<p>На страницах есть ссылки на операторов и партнёров. Их политики конфиденциальности действуют на соответствующих сайтах.</p>
<h2>Права пользователя</h2>
<p>Вы можете запросить информацию о журналах или удаление контактных данных. Запросы рассматриваются в течение 30 дней.</p>
<h2>Обновления</h2>
<p>Последнее обновление: {UPDATED}. Изменения публикуются на этой странице.</p>"""
        return f"""<h2>Umumiy ma'lumot</h2>
<p>casino-bonuses-uz.com — O'zbekiston uchun mustaqil kazino va BK reytingi. Biz operator emasmiz, depozit qabul qilmaymiz va qimor xizmati ko'rsatmaymiz. Siyosat faqat shu domen uchun amal qiladi.</p>
<h2>Qanday ma'lumotlar to'planadi</h2>
<p>Sayt statik. Texnik jurnallarda IP-manzil, brauzer, tashrif vaqti, URL va referrer yozilishi mumkin. Ro'yxatdan o'tish talab qilinmaydi; karta va pasport ma'lumotlari to'planmaydi.</p>
<h2>Cookie va analitika</h2>
<p>Cookie sayt ishlashi va til tanlovi uchun ishlatiladi. Brauzerda cheklash mumkin. Analitika — faqat agregat ko'rinishda, agar ulangan bo'lsa.</p>
<h2>Ma'lumotlarni himoya qilish</h2>
<p>HTTPS (SSL/TLS) orqali uzatish. Jurnallar xavfsizlik va diagnostika uchun cheklangan muddat saqlanadi.</p>
<h2>Uchinchi tomon havolalari</h2>
<p>Sahifalarda operatorlar va hamkor havolalar bor. Ularning maxfiylik siyosati o'z saytlarida amal qiladi.</p>
<h2>Foydalanuvchi huquqlari</h2>
<p>Jurnal yozuvlari yoki aloqa ma'lumotlari haqida so'rov yuborish, tuzatish yoki o'chirishni so'rashingiz mumkin. So'rovlar 30 kun ichida ko'rib chiqiladi.</p>
<h2>Yangilanishlar</h2>
<p>Oxirgi yangilanish: {UPDATED}. O'zgarishlar ushbu sahifada e'lon qilinadi.</p>"""

    if kind == "terms":
        if lang == "ru":
            return f"""<h2>О сайте</h2>
<p>casino-bonuses-uz.com — независимый информационный рейтинг казино и букмекеров Узбекистана. Мы не оператор, не принимаем ставки и депозиты.</p>
<h2>Использование материалов</h2>
<p>Контент предназначен для лиц 18+. Запрещено копирование без ссылки на источник. Суммы welcome и wagering сверяйте на официальных сайтах операторов.</p>
<h2>Отказ от ответственности</h2>
<p>Материалы носят справочный характер и не являются финансовой или юридической консультацией. Решение об игре принимаете только вы.</p>
<h2>Ссылки на операторов</h2>
<p>Партнёрские ссылки могут присутствовать. Переход на сторонние сайты — на ваш риск; действуют их правила.</p>
<h2>Обновления</h2>
<p>Последнее обновление: {UPDATED}.</p>"""
        return f"""<h2>Sayt haqida</h2>
<p>casino-bonuses-uz.com — O'zbekiston kazino va bukmekerlari uchun mustaqil ma'lumot reytingi. Biz operator emasmiz, stavka va depozit qabul qilmaymiz.</p>
<h2>Materiallardan foydalanish</h2>
<p>Kontent 18+ shaxslar uchun. Manba ko'rsatmasdan nusxalash taqiqlanadi. Welcome va wagering summalarini operator rasmiy saytida tekshiring.</p>
<h2>Javobgarlikdan voz kechish</h2>
<p>Materiallar ma'lumot xarakterida; moliyaviy yoki huquqiy maslahat emas. O'ynash qarorini faqat siz qabul qilasiz.</p>
<h2>Operator havolalari</h2>
<p>Hamkor havolalar bo'lishi mumkin. Uchinchi tomon saytlariga o'tish — sizning xavfingiz; ularning qoidalari amal qiladi.</p>
<h2>Yangilanishlar</h2>
<p>Oxirgi yangilanish: {UPDATED}.</p>"""

    if kind == "cookie":
        if lang == "ru":
            return f"""<h2>Что такое cookie</h2>
<p>Cookie — небольшие файлы в браузере для работы сайта, языка и (при наличии) аналитики.</p>
<h2>Какие cookie мы используем</h2>
<ul>
<li>Технические — для навигации и безопасности</li>
<li>Языковые — запоминание выбора UZ/RU</li>
<li>Аналитические — агрегированная статистика посещений (если подключена)</li>
</ul>
<h2>Управление cookie</h2>
<p>Вы можете удалить или заблокировать cookie в настройках браузера. Это может ограничить часть функций сайта.</p>
<h2>Сторонние cookie</h2>
<p>На сайтах операторов по партнёрским ссылкам могут устанавливаться их собственные cookie — см. их политики.</p>
<h2>Обновления</h2>
<p>Последнее обновление: {UPDATED}.</p>"""
        return f"""<h2>Cookie nima</h2>
<p>Cookie — brauzerdagi kichik fayllar: sayt ishlashi, til va (mavjud bo'lsa) analitika uchun.</p>
<h2>Qanday cookie ishlatamiz</h2>
<ul>
<li>Texnik — navigatsiya va xavfsizlik uchun</li>
<li>Til — UZ/RU tanlovini eslab qolish</li>
<li>Analitik — agregat tashrif statistikasi (agar ulangan bo'lsa)</li>
</ul>
<h2>Cookie boshqaruvi</h2>
<p>Brauzer sozlamalarida cookie ni o'chirish yoki bloklash mumkin. Bu ayrim funksiyalarni cheklashi mumkin.</p>
<h2>Uchinchi tomon cookie</h2>
<p>Hamkor havolalar orqali operator saytlarida ularning cookie si o'rnatilishi mumkin — ularning siyosatini o'qing.</p>
<h2>Yangilanishlar</h2>
<p>Oxirgi yangilanish: {UPDATED}.</p>"""

    # responsible
    if lang == "ru":
        return f"""<h2>Основные принципы</h2>
<p>Азартные игры — развлечение, а не способ заработка. Играйте только на сумму, которую готовы потерять. Лицам младше 18 лет участие запрещено.</p>
<h2>Признаки проблемной игры</h2>
<ul>
<li>Превышение бюджета или займы на игру</li>
<li>Сокрытие времени и сумм ставок</li>
<li>Попытки отыграть проигрыш</li>
<li>Негативное влияние на работу и семью</li>
</ul>
<h2>Как защитить себя</h2>
<ul>
<li>Установите лимиты депозита и времени</li>
<li>Делайте регулярные перерывы</li>
<li>Используйте самоисключение в кабинете оператора</li>
<li>Читайте условия бонусов и вейджера</li>
</ul>
<h2>Помощь</h2>
<p>Если игра выходит из-под контроля, обратитесь к специалистам. Международные ресурсы: BeGambleAware, GamCare. Решение об игре принимаете только вы.</p>
<h2>Роль нашего сайта</h2>
<p>casino-bonuses-uz.com — независимый рейтинг. Мы не принимаем депозиты и не являемся оператором. Мы не поощряем азартные игры сверх меры.</p>"""
    return f"""<h2>Asosiy tamoyillar</h2>
<p>Qimor — ko'ngilochar, daromad manbai emas. Faqat yo'qotishga tayyor summada o'ynang. 18 yoshdan kichiklarga qatnashish taqiqlanadi.</p>
<h2>Muammoli o'yin belgilari</h2>
<ul>
<li>Byudjetdan oshish yoki qarz pulga o'ynash</li>
<li>Vaqt va stavka summalarini yashirish</li>
<li>Yo'qotishni quvish</li>
<li>Ish va oilaga salbiy ta'sir</li>
</ul>
<h2>O'zingizni himoya qilish</h2>
<ul>
<li>Depozit va vaqt limitini o'rnating</li>
<li>Muntazam tanaffus qiling</li>
<li>Operator kabinetida o'z-o'zini chetlashtirishdan foydalaning</li>
<li>Bonus va wagering shartlarini o'qing</li>
</ul>
<h2>Yordam</h2>
<p>O'yin nazoratdan chiqsa, mutaxassislarga murojaat qiling. Xalqaro resurslar: BeGambleAware, GamCare. O'ynash qarorini faqat siz qabul qilasiz.</p>
<h2>Saytimiz roli</h2>
<p>casino-bonuses-uz.com — mustaqil reyting. Depozit qabul qilmaymiz va operator emasmiz. Haddan tashqari qimorni rag'batlantirmaymiz.</p>"""


def legal_main(lang: str, kind: str) -> str:
    m = META[kind][lang]
    home = "/ru/" if lang == "ru" else "/"
    updated = "Обновлено" if lang == "ru" else "Yangilangan"
    site_note = "Независимый рейтинг casino-bonuses-uz.com" if lang == "ru" else "Mustaqil reyting casino-bonuses-uz.com"
    return f"""<main id="main" class="legal-doc"><div class="container">
<nav class="breadcrumbs"><a href="{home}">{m['home']}</a> / <span>{m['crumb']}</span></nav>
<article>
<h1>{m['h1']}</h1>
<p class="legal-doc__updated">{updated}: {UPDATED} · {site_note}</p>
{_article_body(kind, lang)}
</article>
{_legal_nav(lang)}
</div></main>"""


def patch(path: Path, lang: str, kind: str, canonical: str, href_uz: str, href_ru: str) -> None:
    m = META[kind][lang]
    main = legal_main(lang, kind)
    page = (
        f"{head_block(lang, m['title'], m['desc'], canonical, href_uz=href_uz, href_ru=href_ru, depth=0)}"
        f"{main}\n"
        f"{footer_block(lang, depth=0)}"
    )
    path.write_text(page, encoding="utf-8")
    print("legal:", path.relative_to(ROOT))


def main():
    for rel, lang, kind, canonical, href_uz, href_ru in LEGAL:
        patch(ROOT / rel, lang, kind, canonical, href_uz, href_ru)


if __name__ == "__main__":
    main()
