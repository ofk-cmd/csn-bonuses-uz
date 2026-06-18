#!/usr/bin/env python3
"""Qttk.uz-style brand review body sections (UZ + RU)."""
from html import escape

# Per-brand facts (operator site patterns, catalog size estimates for UZ market)
META = {
    "fairpari": {"site": "fairpari.com/uz", "year": "2018", "license_uz": "Curacao OGL/2024/1143/0865",
                 "license_ru": "Кюрасао OGL/2024/1143/0865", "providers": "80+", "slots_uz": "12 000+ slot va live",
                 "slots_ru": "12 000+ слотов и live", "sports": "53", "min_dep": "~130 000 UZS",
                 "sport_welcome_uz": "1 400 000 UZS", "sport_welcome_ru": "1 400 000 UZS",
                 "app_uz": "Android APK, iOS PWA", "app_ru": "Android APK, iOS PWA"},
    "1win": {"site": "1win.com", "year": "2016", "license_uz": "Curacao", "license_ru": "Кюрасао",
             "providers": "70+", "slots_uz": "10 000+", "slots_ru": "10 000+", "sports": "40+",
             "min_dep": "~50 000 UZS", "sport_welcome_uz": "12 000 000 UZS gacha", "sport_welcome_ru": "до 12 000 000 UZS",
             "app_uz": "Android APK, mobil sayt", "app_ru": "Android APK, мобильный сайт"},
    "1xbet": {"site": "1xbet.com", "year": "2007", "license_uz": "Curacao", "license_ru": "Кюрасао",
              "providers": "100+", "slots_uz": "8 000+", "slots_ru": "8 000+", "sports": "60+",
              "min_dep": "~30 000 UZS", "sport_welcome_uz": "6 500 000 UZS + 150 FS", "sport_welcome_ru": "6 500 000 UZS + 150 FS",
              "app_uz": "Android, iOS", "app_ru": "Android, iOS"},
    "mostbet": {"site": "mostbet.com", "year": "2009", "license_uz": "Curacao", "license_ru": "Кюрасао",
                "providers": "60+", "slots_uz": "5 000+", "slots_ru": "5 000+", "sports": "35+",
                "min_dep": "~40 000 UZS", "sport_welcome_uz": "8 500 000 UZS + 250 FS", "sport_welcome_ru": "8 500 000 UZS + 250 FS",
                "app_uz": "Android APK", "app_ru": "Android APK"},
    "melbet": {"site": "melbet.com", "year": "2012", "license_uz": "Curacao", "license_ru": "Кюрасао",
               "providers": "50+", "slots_uz": "4 500+", "slots_ru": "4 500+", "sports": "30+",
               "min_dep": "~35 000 UZS", "sport_welcome_uz": "7 000 000 UZS", "sport_welcome_ru": "7 000 000 UZS",
               "app_uz": "Android APK", "app_ru": "Android APK"},
    "pin-up": {"site": "pin-up.uz", "year": "2016", "license_uz": "Curacao", "license_ru": "Кюрасао",
               "providers": "45+", "slots_uz": "5 000+", "slots_ru": "5 000+", "sports": "25+",
               "min_dep": "~50 000 UZS", "sport_welcome_uz": "5 500 000 UZS + 250 FS", "sport_welcome_ru": "5 500 000 UZS + 250 FS",
               "app_uz": "Android APK, PWA", "app_ru": "Android APK, PWA"},
    "linebet": {"site": "linebet.com", "year": "2019", "license_uz": "Curacao", "license_ru": "Кюрасао",
                "providers": "20+", "slots_uz": "2 000+", "slots_ru": "2 000+", "sports": "30+",
                "min_dep": "~30 000 UZS", "sport_welcome_uz": "4 800 000 UZS", "sport_welcome_ru": "4 800 000 UZS",
                "app_uz": "Mobil sayt", "app_ru": "Мобильный сайт"},
    "betwinner": {"site": "betwinner.com", "year": "2018", "license_uz": "Curacao", "license_ru": "Кюрасао",
                  "providers": "80+", "slots_uz": "6 000+", "slots_ru": "6 000+", "sports": "50+",
                  "min_dep": "~30 000 UZS", "sport_welcome_uz": "5 000 000 UZS + 150 FS", "sport_welcome_ru": "5 000 000 UZS + 150 FS",
                  "app_uz": "Android APK", "app_ru": "Android APK"},
    "megapari": {"site": "megapari.com", "year": "2019", "license_uz": "Curacao", "license_ru": "Кюрасао",
                 "providers": "55+", "slots_uz": "4 000+", "slots_ru": "4 000+", "sports": "35+",
                 "min_dep": "~40 000 UZS", "sport_welcome_uz": "4 500 000 UZS + 100 FS", "sport_welcome_ru": "4 500 000 UZS + 100 FS",
                 "app_uz": "Android APK", "app_ru": "Android APK"},
    "22bet": {"site": "22bet.com", "year": "2017", "license_uz": "Curacao", "license_ru": "Кюрасао",
              "providers": "50+", "slots_uz": "3 500+", "slots_ru": "3 500+", "sports": "40+",
              "min_dep": "~25 000 UZS", "sport_welcome_uz": "4 200 000 UZS", "sport_welcome_ru": "4 200 000 UZS",
              "app_uz": "Android, iOS", "app_ru": "Android, iOS"},
    "parimatch": {"site": "parimatch.com", "year": "1994", "license_uz": "Curacao", "license_ru": "Кюрасао",
                  "providers": "15+", "slots_uz": "1 500+", "slots_ru": "1 500+", "sports": "25+",
                  "min_dep": "~50 000 UZS", "sport_welcome_uz": "3 800 000 UZS", "sport_welcome_ru": "3 800 000 UZS",
                  "app_uz": "Android APK", "app_ru": "Android APK"},
    "leon": {"site": "leon.bet", "year": "2007", "license_uz": "Curacao", "license_ru": "Кюрасао",
             "providers": "10+", "slots_uz": "1 000+", "slots_ru": "1 000+", "sports": "20+",
             "min_dep": "~40 000 UZS", "sport_welcome_uz": "3 500 000 UZS", "sport_welcome_ru": "3 500 000 UZS",
             "app_uz": "Mobil sayt, APK", "app_ru": "Мобильный сайт, APK"},
    "fonbet": {"site": "fonbet.com", "year": "1994", "license_uz": "Curacao / lokal", "license_ru": "Кюрасао / локальная",
               "providers": "10+", "slots_uz": "800+", "slots_ru": "800+", "sports": "25+",
               "min_dep": "~50 000 UZS", "sport_welcome_uz": "3 200 000 UZS", "sport_welcome_ru": "3 200 000 UZS",
               "app_uz": "Android APK", "app_ru": "Android APK"},
    "marathonbet": {"site": "marathonbet.com", "year": "1997", "license_uz": "Curacao", "license_ru": "Кюрасао",
                    "providers": "8+", "slots_uz": "500+", "slots_ru": "500+", "sports": "30+",
                    "min_dep": "~40 000 UZS", "sport_welcome_uz": "3 000 000 UZS", "sport_welcome_ru": "3 000 000 UZS",
                    "app_uz": "Mobil sayt", "app_ru": "Мобильный сайт"},
    "betway": {"site": "betway.com", "year": "2006", "license_uz": "MGA / Curacao", "license_ru": "MGA / Кюрасао",
               "providers": "15+", "slots_uz": "1 200+", "slots_ru": "1 200+", "sports": "20+",
               "min_dep": "~50 000 UZS", "sport_welcome_uz": "2 800 000 UZS", "sport_welcome_ru": "2 800 000 UZS",
               "app_uz": "Android, iOS", "app_ru": "Android, iOS"},
    "spinbetter": {"site": "spinbetter.com", "year": "2020", "license_uz": "Curacao", "license_ru": "Кюрасао",
                   "providers": "40+", "slots_uz": "3 000+", "slots_ru": "3 000+", "sports": "25+",
                   "min_dep": "~35 000 UZS", "sport_welcome_uz": "3 600 000 UZS + 100 FS", "sport_welcome_ru": "3 600 000 UZS + 100 FS",
                   "app_uz": "Android APK", "app_ru": "Android APK"},
    "vulkan-vegas": {"site": "vulkanvegas.com", "year": "2017", "license_uz": "Curacao", "license_ru": "Кюрасао",
                     "providers": "50+", "slots_uz": "4 000+", "slots_ru": "4 000+", "sports": "—",
                     "min_dep": "~40 000 UZS", "sport_welcome_uz": "—", "sport_welcome_ru": "—",
                     "app_uz": "Mobil sayt", "app_ru": "Мобильный сайт"},
    "joycasino": {"site": "joycasino.com", "year": "2014", "license_uz": "Curacao", "license_ru": "Кюрасао",
                  "providers": "35+", "slots_uz": "3 500+", "slots_ru": "3 500+", "sports": "—",
                  "min_dep": "~35 000 UZS", "sport_welcome_uz": "—", "sport_welcome_ru": "—",
                  "app_uz": "Mobil sayt", "app_ru": "Мобильный сайт"},
    "fresh-casino": {"site": "fresh.casino", "year": "2018", "license_uz": "Curacao", "license_ru": "Кюрасао",
                     "providers": "30+", "slots_uz": "2 500+", "slots_ru": "2 500+", "sports": "—",
                     "min_dep": "~30 000 UZS", "sport_welcome_uz": "—", "sport_welcome_ru": "—",
                     "app_uz": "PWA", "app_ru": "PWA"},
    "bc-game": {"site": "bc.game", "year": "2017", "license_uz": "Curacao", "license_ru": "Кюрасао",
                "providers": "25+", "slots_uz": "2 000+ / kripto", "slots_ru": "2 000+ / крипто", "sports": "15+",
                "min_dep": "USDT", "sport_welcome_uz": "Kripto paket", "sport_welcome_ru": "Крипто-пакет",
                "app_uz": "Android, PWA", "app_ru": "Android, PWA"},
}


def _faq_items(b, rank, lang):
    name = b["name"]
    welcome = b["welcome_ru"] if lang == "ru" else b["welcome_uz"]
    m = META.get(b["slug"], META["1win"])
    site = m["site"]
    if lang == "ru":
        return [
            (f"{name} легален в Узбекистане?", f"{name} работает по международной лицензии. Проверьте местные правила онлайн-азартных игр в UZ."),
            (f"Какой welcome у {name}?", f"По нашему рейтингу #{rank}: {welcome}, вейджер {b['wagering']}. Уточняйте на официальном сайте."),
            (f"Какие платежи принимает {name}?", f"{b['pay']}. Депозит и вывод — в кабинете оператора после регистрации."),
            (f"Есть ли мобильное приложение {name}?", m["app_ru"]),
            (f"Где официальный сайт {name}?", f"Используйте только {site} или проверенные ссылки. casino-bonuses-uz.com — не оператор."),
        ]
    return [
        (f"{name} O'zbekistonda qonuniymi?", f"{name} xalqaro litsenziya asosida ishlaydi. UZ qoidalarini alohida tekshiring."),
        (f"{name} welcome bonusi qancha?", f"Reytingimizda #{rank}: {welcome}, wagering {b['wagering']}. Aniq shartlar operator saytida."),
        (f"{name} qaysi to'lovlarni qabul qiladi?", f"{b['pay']}. Depozit va yechish — ro'yxatdan keyin kassada."),
        (f"{name} mobil ilovasi bormi?", m["app_uz"]),
        (f"{name} rasmiy sayti qaysi?", f"Faqat {site} yoki tekshirilgan havolalar. casino-bonuses-uz.com operator emas."),
    ]


def render_body(b: dict, rank: int, lang: str, logo: str) -> str:
    name = b["name"]
    slug = b["slug"]
    welcome = b["welcome_ru"] if lang == "ru" else b["welcome_uz"]
    pros = b["pros_ru"] if lang == "ru" else b["pros_uz"]
    cons = b["cons_ru"] if lang == "ru" else b["cons_uz"]
    m = META.get(slug, META["1win"])
    t = b["type"]
    site = m["site"]

    if lang == "ru":
        L = {
            "about_eyebrow": "О платформе", "about_h2": f"{name} — обзор в цифрах для UZ",
            "about_sub": f"Краткие факты по {site}: провайдеры, каталог, бонусы. Актуальные лимиты — на сайте оператора.",
            "row_site": "Сайт", "row_lang": "Языки", "row_lang_v": "узбекский, русский, английский",
            "row_cur": "Валюта", "row_cur_v": "UZS (сум)", "row_prov": "Провайдеры", "row_slots": "Игры",
            "row_sport": "Виды спорта", "row_year": "Год", "row_lic": "Лицензия",
            "row_cas_w": "Казино welcome", "row_sp_w": "Спорт welcome", "row_min": "Мин. депозит", "row_app": "Приложение",
            "feat_eyebrow": "Преимущества", "feat_h2": f"{name} для игроков Узбекистана",
            "feat_sub": "UZS-счёт, локальные платежи и мобильный доступ",
            "reg_eyebrow": "Регистрация", "reg_h2": f"Как зарегистрироваться в {name}",
            "reg_sub": "Типичные шаги на официальном сайте",
            "reg_lead": f"Создайте аккаунт на {site}: выберите UZS, укажите телефон или email, при необходимости — welcome-бонус. casino-bonuses-uz.com не принимает депозиты.",
            "app_eyebrow": "Мобильная версия", "app_h2": f"Мобильное приложение {name}",
            "cas_eyebrow": "Казино", "cas_h2": f"Онлайн-казино {name}",
            "cas_p": f"Слоты, live-столы и crash-игры в UZS. Каталог: {m['slots_ru']}. Проверьте раздел PROMO перед депозитом.",
            "sport_eyebrow": "Спорт", "sport_h2": f"Ставки на спорт {name}",
            "sport_p": f"Прематч и live, экспрессы. Линия: {m['sports']} видов спорта. Спортивный welcome — отдельно от казино.",
            "bon_eyebrow": "Бонусы", "bon_h2": f"Бонусы {name} — welcome и акции",
            "bon_sub": f"Обзор пакета: {welcome}, вейджер {b['wagering']}",
            "bon_th1": "Бонус", "bon_th2": "Сумма", "bon_th3": "Условия",
            "bon_row1": "Welcome", "bon_row1c": f"Вейджер {b['wagering']}; срок и max bet — в PROMO",
            "bon_row2": "Фриспины", "bon_row2v": "В пакете welcome", "bon_row2c": "Wagering на выигрыш FS; срок ~7–14 дней",
            "bon_row3": "Кешбэк / reload", "bon_row3v": "По акциям", "bon_row3c": "Временные предложения в кабинете",
            "spbon_h2": f"Спорт-бонусы {name}", "spbon_row": "Спорт welcome",
            "pay_eyebrow": "Платежи", "pay_h2": f"Пополнение и вывод в {name}",
            "pay_sub": "Humo, Uzcard, Payme, Click — стандарт для UZ",
            "pay_th1": "Метод", "pay_th2": "Депозит / вывод", "pay_th3": "Срок",
            "sec_eyebrow": "Безопасность", "sec_h2": f"Безопасность {name}",
            "sec_p": "HTTPS, KYC при первом выводе, лимиты в кабинете. 18+. Играйте ответственно.",
            "pc_eyebrow": "Итог", "pc_h2": f"{name}: плюсы и минусы",
            "pc_sub": "Практичный обзор, не реклама", "pc_pros": "Плюсы", "pc_cons": "Минусы",
            "rev_eyebrow": "Мнения", "rev_h2": f"Что говорят игроки UZ о {name}",
            "rev_sub": "Типичные темы в обсуждениях",
            "rev_p": f"В отзывах UZ чаще хвалят {b['pay']} и мобильный доступ. Критикуют вейджер и KYC. Проверяйте PROMO на {site}.",
            "faq_eyebrow": "FAQ", "faq_h2": f"FAQ {name}: бонус, регистрация, вывод",
            "cta": "Получить бонус", "back": '<a href="/ru/#rating">← К рейтингу</a>',
            "compare": f'Сравните с <a href="/ru/fairpari/">FairPari №1</a> — 20,2 млн UZS + 150 FS.',
            "h1": f"{name} — обзор бонусов (#{rank})",
            "intro": f"<strong>{name}</strong> в рейтинге <strong>#{rank}</strong>. Welcome: <strong>{welcome}</strong>, вейджер <strong>{b['wagering']}</strong>.",
            "nav_aria": "Разделы", "nav_about": "О платформе", "nav_features": "Плюсы",
            "nav_reg": "Регистрация", "nav_bon": "Бонусы", "nav_pay": "Платежи",
            "app_note": "Скачивайте только с официального сайта.",
            "sec_limit": "Лимиты и самоисключение",
            "steps": [f"Откройте {site} и нажмите «Регистрация».",
                      "Выберите телефон или email, валюту UZS.",
                      "При необходимости укажите промокод и тип welcome.",
                      "Подтвердите аккаунт и внесите первый депозит."],
        }
        slots_val = m["slots_ru"]
        lic_val = m["license_ru"]
        sport_w = m["sport_welcome_ru"]
        app_val = m["app_ru"]
    else:
        L = {
            "about_eyebrow": "Platforma haqida", "about_h2": f"{name} — UZ uchun raqamlarda sharh",
            "about_sub": f"{site} bo'yicha qisqa faktlar: provayderlar, katalog, bonuslar. Dolzarb limitlar operator saytida.",
            "row_site": "Sayt", "row_lang": "Tillar", "row_lang_v": "o'zbek, rus, ingliz",
            "row_cur": "Valyuta", "row_cur_v": "UZS (so'm)", "row_prov": "Provayderlar", "row_slots": "O'yinlar",
            "row_sport": "Sport turlari", "row_year": "Yil", "row_lic": "Litsenziya",
            "row_cas_w": "Kazino welcome", "row_sp_w": "Sport welcome", "row_min": "Min. depozit", "row_app": "Ilova",
            "feat_eyebrow": "Afzalliklar", "feat_h2": f"{name} — O'zbekiston o'yinchilari uchun",
            "feat_sub": "UZS hisob, mahalliy to'lovlar va mobil kirish",
            "reg_eyebrow": "Ro'yxatdan o'tish", "reg_h2": f"{name} da qanday ro'yxatdan o'tiladi",
            "reg_sub": "Rasmiy saytdagi odatiy bosqichlar",
            "reg_lead": f"{site} da akkaunt oching: UZS tanlang, telefon yoki email kiriting, kerak bo'lsa welcome belgilang. casino-bonuses-uz.com depozit qabul qilmaydi.",
            "app_eyebrow": "Mobil", "app_h2": f"{name} mobil ilovasi",
            "cas_eyebrow": "Kazino", "cas_h2": f"{name} onlayn kazino",
            "cas_p": f"Slotlar, live va crash UZS da. Katalog: {m['slots_uz']}. Depozitdan oldin PROMO ni tekshiring.",
            "sport_eyebrow": "Sport", "sport_h2": f"{name} sport stavkalari",
            "sport_p": f"Pre-match va live, ekspresslar. Liniya: {m['sports']} tur. Sport welcome kazinodan alohida.",
            "bon_eyebrow": "Bonuslar", "bon_h2": f"{name} bonuslari — welcome va aksiyalar",
            "bon_sub": f"Paket: {welcome}, wagering {b['wagering']}",
            "bon_th1": "Bonus", "bon_th2": "Miqdor", "bon_th3": "Shartlar",
            "bon_row1": "Welcome", "bon_row1c": f"Wagering {b['wagering']}; muddat va max bet — PROMO da",
            "bon_row2": "Frispinlar", "bon_row2v": "Welcome paketida", "bon_row2c": "FS yutug'i wagering; ~7–14 kun",
            "bon_row3": "Keshbek / reload", "bon_row3v": "Aksiyaga ko'ra", "bon_row3c": "Vaqtinchak takliflar kabinetda",
            "spbon_h2": f"{name} sport bonuslari", "spbon_row": "Sport welcome",
            "pay_eyebrow": "To'lovlar", "pay_h2": f"{name} da to'ldirish va yechish",
            "pay_sub": "Humo, Uzcard, Payme, Click — UZ standarti",
            "pay_th1": "Usul", "pay_th2": "Depozit / yechish", "pay_th3": "Muddat",
            "sec_eyebrow": "Xavfsizlik", "sec_h2": f"{name} xavfsizligi",
            "sec_p": "HTTPS, birinchi yechishda KYC, kabinetda limitlar. 18+. Mas'uliyat bilan o'ynang.",
            "pc_eyebrow": "Xulosa", "pc_h2": f"{name}: afzalliklar va kamchiliklar",
            "pc_sub": "Amaliy sharh, reklama emas", "pc_pros": "Afzalliklar", "pc_cons": "Kamchiliklar",
            "rev_eyebrow": "Fikrlar", "rev_h2": f"UZ o'yinchilarining {name} haqidagi fikrlari",
            "rev_sub": "Muhokamalardagi takrorlanuvchi mavzular",
            "rev_p": f"UZ sharhlarida {b['pay']} va mobil kirish maqtaladi. Wagering va KYC tanqid qilinadi. {site} da PROMO ni tekshiring.",
            "faq_eyebrow": "FAQ", "faq_h2": f"{name} FAQ: bonus, ro'yxatdan o'tish, yechish",
            "cta": "Bonusni olish", "back": '<a href="/#rating">← Reytingga</a>',
            "compare": f'<a href="/fairpari/">FairPari #1</a> bilan solishtiring — 20,2 mln UZS + 150 FS.',
            "h1": f"{name} — bonus sharhi (#{rank})",
            "intro": f"<strong>{name}</strong> reytingimizda <strong>#{rank}</strong>. Welcome: <strong>{welcome}</strong>, wagering <strong>{b['wagering']}</strong>.",
            "nav_aria": "Bo'limlar", "nav_about": "Platforma", "nav_features": "Afzalliklar",
            "nav_reg": "Ro'yxatdan o'tish", "nav_bon": "Bonuslar", "nav_pay": "To'lovlar",
            "app_note": "Faqat rasmiy saytdan yuklab oling.",
            "sec_limit": "Limitlar va self-exclusion",
            "steps": [f"{site} ni oching va «Ro'yxatdan o'tish» ni bosing.",
                      "Telefon yoki email, valyuta UZS tanlang.",
                      "Kerak bo'lsa promokod va welcome turini belgilang.",
                      "Akkauntni tasdiqlang va birinchi depozitni kiriting."],
        }
        slots_val = m["slots_uz"]
        lic_val = m["license_uz"]
        sport_w = m["sport_welcome_uz"]
        app_val = m["app_uz"]

  # Feature cards from pros + generic
    feats = []
    icons = ["🎁", "💳", "📱", "🔐"]
    for i, p in enumerate(pros[:4]):
        feats.append((icons[i % 4], p, ""))
    while len(feats) < 4:
        feats.append((icons[len(feats)], pros[0] if pros else name, ""))

    feat_html = "".join(
        f'<article class="feature-card"><div class="feature-card__icon">{ic}</div>'
        f'<h3 class="feature-card__title">{escape(t)}</h3>'
        f'<p class="feature-card__text">{escape(tx) if tx else escape(t)}</p></article>'
        for ic, t, tx in feats
    )

    steps_html = "".join(f"<li>{escape(s)}</li>" for s in L["steps"])

    sport_row = ""
    if t in ("both", "bk") and sport_w != "—":
        sport_row = f"<tr><td>{L['row_sp_w']}</td><td>{escape(sport_w)}</td></tr>"

    casino_sec = ""
    if t in ("both", "casino"):
        casino_sec = f'''
<section class="section section--alt" id="casino">
  <header class="section__header section__header--compact"><span class="section__eyebrow">{L["cas_eyebrow"]}</span>
  <h2 class="section__title">{L["cas_h2"]}</h2></header>
  <p>{L["cas_p"]}</p>
</section>'''

    sport_sec = ""
    if t in ("both", "bk"):
        sport_sec = f'''
<section class="section" id="sports">
  <header class="section__header section__header--compact"><span class="section__eyebrow">{L["sport_eyebrow"]}</span>
  <h2 class="section__title">{L["sport_h2"]}</h2></header>
  <p>{L["sport_p"]}</p>
</section>'''

    sp_bonus_sec = ""
    if t in ("both", "bk") and sport_w != "—":
        sp_bonus_sec = f'''
<section class="section section--alt" id="betting-bonuses">
  <header class="section__header section__header--compact"><span class="section__eyebrow">{L["sport_eyebrow"]}</span>
  <h2 class="section__title">{L["spbon_h2"]}</h2></header>
  <table class="data-table data-table--compact"><thead><tr><th>{L["bon_th1"]}</th><th>{L["bon_th2"]}</th><th>{L["bon_th3"]}</th></tr></thead>
  <tbody><tr><td>{L["spbon_row"]}</td><td>{escape(sport_w)}</td><td>Wagering ×5 ekspress (taxminiy)</td></tr></tbody></table>
</section>'''

    from brand_expand_2000 import all_faq_items
    faq_items = all_faq_items(b, rank, lang)
    faq_html = "".join(
        f'<article class="faq-item{" is-open" if i == 0 else ""}">'
        f'<button type="button" class="faq-item__question" aria-expanded="{"true" if i == 0 else "false"}">'
        f'<span>{escape(q)}</span><span class="faq-item__icon" aria-hidden="true">+</span></button>'
        f'<div class="faq-item__answer">{escape(a)}</div></article>'
        for i, (q, a) in enumerate(faq_items)
    )

    pros_li = "".join(f"<li>{escape(p)}</li>" for p in pros)
    cons_li = "".join(f"<li>{escape(c)}</li>" for c in cons)

    if lang == "ru":
        pay_dep1 = m["min_dep"]
        pay_time1 = "Минуты"
        pay_dep2 = "Депозит + вывод"
        pay_time2 = "1–3 дня"
    else:
        pay_dep1 = m["min_dep"] + " dan"
        pay_time1 = "Daqiqalar"
        pay_dep2 = "Depozit + yechish"
        pay_time2 = "1–3 kun"

    pay_rows = ""
    for method, dep, time in [
        (b["pay"].split(",")[0].strip(), pay_dep1, pay_time1),
        ("Humo / Uzcard" if "Humo" in b["pay"] or "Uzcard" in b["pay"] else b["pay"], pay_dep2, pay_time2),
    ]:
        pay_rows += f"<tr><td>{escape(method)}</td><td>{escape(dep)}</td><td>{escape(time)}</td></tr>"

    from brand_expand_2000 import extra_sections
    extra_html = extra_sections(b, rank, lang)

    return f'''
<article class="brand-review">
  <div class="casino-card" style="margin-bottom:1.5rem">
    <div class="casino-card__rank-col"><span class="casino-card__rank">#{rank}</span>
    <img class="casino-card__logo" src="{logo}" alt="{escape(name)}" width="64" height="64"/></div>
    <div class="casino-card__body">
      <h1 class="casino-card__title" style="font-size:1.5rem">{L["h1"]}</h1>
      <p>{L["intro"]}</p>
    </div>
  </div>
  <nav class="on-page-nav" aria-label="{L["nav_aria"]}">
    <a href="#about">{L["nav_about"]}</a>
    <a href="#features">{L["nav_features"]}</a>
    <a href="#registration">{L["nav_reg"]}</a>
    <a href="#bonuses">{L["nav_bon"]}</a>
    <a href="#payments">{L["nav_pay"]}</a>
    <a href="#faq">FAQ</a>
  </nav>

  <section class="section" id="about">
    <header class="section__header section__header--compact"><span class="section__eyebrow">{L["about_eyebrow"]}</span>
    <h2 class="section__title">{L["about_h2"]}</h2>
    <p class="section__subtitle">{L["about_sub"]}</p></header>
    <table class="data-table data-table--compact"><tbody>
      <tr><td>{L["row_site"]}</td><td>{escape(site)}</td></tr>
      <tr><td>{L["row_lang"]}</td><td>{L["row_lang_v"]}</td></tr>
      <tr><td>{L["row_cur"]}</td><td>{L["row_cur_v"]}</td></tr>
      <tr><td>{L["row_prov"]}</td><td>{m["providers"]}</td></tr>
      <tr><td>{L["row_slots"]}</td><td>{escape(slots_val)}</td></tr>
      <tr><td>{L["row_sport"]}</td><td>{m["sports"]}</td></tr>
      <tr><td>{L["row_year"]}</td><td>{m["year"]}</td></tr>
      <tr><td>{L["row_lic"]}</td><td>{escape(lic_val)}</td></tr>
      <tr><td>{L["row_cas_w"]}</td><td>{escape(welcome)}</td></tr>
      {sport_row}
      <tr><td>{L["row_min"]}</td><td>{m["min_dep"]}</td></tr>
      <tr><td>{L["row_app"]}</td><td>{escape(app_val)}</td></tr>
    </tbody></table>
  </section>

  <section class="section section--alt" id="features">
    <header class="section__header section__header--compact"><span class="section__eyebrow">{L["feat_eyebrow"]}</span>
    <h2 class="section__title">{L["feat_h2"]}</h2><p class="section__subtitle">{L["feat_sub"]}</p></header>
    <div class="features-grid">{feat_html}</div>
  </section>

  <section class="section" id="registration">
    <header class="section__header section__header--compact"><span class="section__eyebrow">{L["reg_eyebrow"]}</span>
    <h2 class="section__title">{L["reg_h2"]}</h2><p class="section__subtitle">{L["reg_sub"]}</p></header>
    <p>{L["reg_lead"]}</p>
    <ol class="section-list">{steps_html}</ol>
  </section>

  <section class="section section--alt" id="app">
    <header class="section__header section__header--compact"><span class="section__eyebrow">{L["app_eyebrow"]}</span>
    <h2 class="section__title">{L["app_h2"]}</h2></header>
    <p>{escape(app_val)}. {L["app_note"]}</p>
  </section>
  {casino_sec}
  {sport_sec}

  <section class="section" id="bonuses">
    <header class="section__header section__header--compact"><span class="section__eyebrow">{L["bon_eyebrow"]}</span>
    <h2 class="section__title">{L["bon_h2"]}</h2><p class="section__subtitle">{L["bon_sub"]}</p></header>
    <table class="data-table data-table--compact"><thead><tr><th>{L["bon_th1"]}</th><th>{L["bon_th2"]}</th><th>{L["bon_th3"]}</th></tr></thead>
    <tbody>
      <tr><td>{L["bon_row1"]}</td><td>{escape(welcome)}</td><td>{L["bon_row1c"]}</td></tr>
      <tr><td>{L["bon_row2"]}</td><td>{L["bon_row2v"]}</td><td>{L["bon_row2c"]}</td></tr>
      <tr><td>{L["bon_row3"]}</td><td>{L["bon_row3v"]}</td><td>{L["bon_row3c"]}</td></tr>
    </tbody></table>
  </section>
  {sp_bonus_sec}

  <section class="section section--alt" id="payments">
    <header class="section__header section__header--compact"><span class="section__eyebrow">{L["pay_eyebrow"]}</span>
    <h2 class="section__title">{L["pay_h2"]}</h2><p class="section__subtitle">{L["pay_sub"]}</p></header>
    <table class="data-table data-table--compact"><thead><tr><th>{L["pay_th1"]}</th><th>{L["pay_th2"]}</th><th>{L["pay_th3"]}</th></tr></thead>
    <tbody>{pay_rows}</tbody></table>
  </section>

  <section class="section" id="security">
    <header class="section__header section__header--compact"><span class="section__eyebrow">{L["sec_eyebrow"]}</span>
    <h2 class="section__title">{L["sec_h2"]}</h2></header>
    <p>{L["sec_p"]}</p>
    <ul class="section-list">
      <li>SSL / HTTPS</li>
      <li>KYC</li>
      <li>{L["sec_limit"]}</li>
      <li>{escape(lic_val)}</li>
    </ul>
  </section>

  <section class="section section--alt" id="pros-cons">
    <header class="section__header section__header--compact"><span class="section__eyebrow">{L["pc_eyebrow"]}</span>
    <h2 class="section__title">{L["pc_h2"]}</h2><p class="section__subtitle">{L["pc_sub"]}</p></header>
    <div class="pros-cons">
      <div class="pros-cons__col pros-cons__col--pros"><h3 class="pros-cons__heading">{L["pc_pros"]}</h3><ul class="pros-cons__list">{pros_li}</ul></div>
      <div class="pros-cons__col pros-cons__col--cons"><h3 class="pros-cons__heading">{L["pc_cons"]}</h3><ul class="pros-cons__list">{cons_li}</ul></div>
    </div>
  </section>

  <section class="section" id="reviews">
    <header class="section__header section__header--compact"><span class="section__eyebrow">{L["rev_eyebrow"]}</span>
    <h2 class="section__title">{L["rev_h2"]}</h2><p class="section__subtitle">{L["rev_sub"]}</p></header>
    <p>{L["rev_p"]}</p>
  </section>

  <section class="section section--alt" id="faq">
    <header class="section__header section__header--compact"><span class="section__eyebrow">{L["faq_eyebrow"]}</span>
    <h2 class="section__title">{L["faq_h2"]}</h2></header>
    <div class="faq-list">{faq_html}</div>
  </section>
  {extra_html}

  <p>{L["compare"]}</p>
  <p>{L["back"]}</p>
  <button type="button" class="btn btn--gold js-go-partner">{L["cta"]}</button>
</article>'''


def faq_schema(b, rank, lang):
    import json
    from brand_expand_2000 import all_faq_items
    items = all_faq_items(b, rank, lang)
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in items
        ],
    }, ensure_ascii=False)
