#!/usr/bin/env python3
"""Hub page body content for casino-bonuses-uz.com — ~2000 words per slug (uz/ru)."""
from html import escape

SLUGS = ("kazino-bonuslari", "welcome-bonus", "depozitsiz-bonus", "tolov-uz", "faq")

TOP20_UZ = [
    ("fairpari", "FairPari", "20 200 000 UZS + 150 FS", "×35", "Humo, Payme, Click"),
    ("1win", "1win", "12 000 000 UZS gacha", "×30", "Humo, Uzcard"),
    ("1xbet", "1xBet", "6 500 000 UZS + 150 FS", "×40", "Humo, kripto"),
    ("mostbet", "Mostbet", "8 500 000 UZS + 250 FS", "×35", "Humo, Payme"),
    ("melbet", "Melbet", "7 000 000 UZS", "×30", "Uzcard, Click"),
    ("pin-up", "Pin-Up", "5 500 000 UZS + 250 FS", "×35", "Humo, Payme"),
    ("linebet", "Linebet", "4 800 000 UZS sport", "×5", "Humo, Click"),
    ("betwinner", "Betwinner", "5 000 000 UZS + 150 FS", "×35", "Humo, Uzcard"),
    ("megapari", "Megapari", "4 500 000 UZS + 100 FS", "×35", "Humo, Payme"),
    ("22bet", "22Bet", "4 200 000 UZS", "×35", "Humo, kripto"),
    ("parimatch", "Parimatch", "3 800 000 UZS sport", "×5", "Humo, Payme"),
    ("leon", "Leon", "3 500 000 UZS", "×5", "Humo, Click"),
    ("fonbet", "Fonbet", "3 200 000 UZS sport", "×5", "Humo, Uzcard"),
    ("marathonbet", "Marathonbet", "3 000 000 UZS", "×5", "Humo, Payme"),
    ("betway", "Betway", "2 800 000 UZS sport", "×6", "Humo, kripto"),
    ("spinbetter", "Spinbetter", "3 600 000 UZS + 100 FS", "×35", "Humo, Click"),
    ("vulkan-vegas", "Vulkan Vegas", "3 400 000 UZS + 150 FS", "×40", "Humo, Payme"),
    ("joycasino", "Joycasino", "3 000 000 UZS + 200 FS", "×40", "Humo, Uzcard"),
    ("fresh-casino", "Fresh Casino", "2 900 000 UZS + 100 FS", "×35", "Payme, Click"),
    ("bc-game", "BC.Game", "Kripto paket USDT", "×45", "USDT, BTC"),
]

TOP20_RU = [
    ("fairpari", "FairPari", "20 200 000 UZS + 150 FS", "×35", "Humo, Payme, Click"),
    ("1win", "1win", "до 12 000 000 UZS", "×30", "Humo, Uzcard"),
    ("1xbet", "1xBet", "6 500 000 UZS + 150 FS", "×40", "Humo, крипто"),
    ("mostbet", "Mostbet", "8 500 000 UZS + 250 FS", "×35", "Humo, Payme"),
    ("melbet", "Melbet", "7 000 000 UZS", "×30", "Uzcard, Click"),
    ("pin-up", "Pin-Up", "5 500 000 UZS + 250 FS", "×35", "Humo, Payme"),
    ("linebet", "Linebet", "4 800 000 UZS спорт", "×5", "Humo, Click"),
    ("betwinner", "Betwinner", "5 000 000 UZS + 150 FS", "×35", "Humo, Uzcard"),
    ("megapari", "Megapari", "4 500 000 UZS + 100 FS", "×35", "Humo, Payme"),
    ("22bet", "22Bet", "4 200 000 UZS", "×35", "Humo, крипто"),
    ("parimatch", "Parimatch", "3 800 000 UZS спорт", "×5", "Humo, Payme"),
    ("leon", "Leon", "3 500 000 UZS", "×5", "Humo, Click"),
    ("fonbet", "Fonbet", "3 200 000 UZS спорт", "×5", "Humo, Uzcard"),
    ("marathonbet", "Marathonbet", "3 000 000 UZS", "×5", "Humo, Payme"),
    ("betway", "Betway", "2 800 000 UZS спорт", "×6", "Humo, крипто"),
    ("spinbetter", "Spinbetter", "3 600 000 UZS + 100 FS", "×35", "Humo, Click"),
    ("vulkan-vegas", "Vulkan Vegas", "3 400 000 UZS + 150 FS", "×40", "Humo, Payme"),
    ("joycasino", "Joycasino", "3 000 000 UZS + 200 FS", "×40", "Humo, Uzcard"),
    ("fresh-casino", "Fresh Casino", "2 900 000 UZS + 100 FS", "×35", "Payme, Click"),
    ("bc-game", "BC.Game", "Крипто-пакет USDT", "×45", "USDT, BTC"),
]


def _links(lang: str) -> dict[str, str]:
    p = "/ru/" if lang == "ru" else "../"
    return {
        "home": p if lang == "ru" else "../",
        "fairpari": f"{p}fairpari/",
        "welcome": f"{p}welcome-bonus/",
        "nodep": f"{p}depozitsiz-bonus/",
        "pay": f"{p}tolov-uz/",
        "faq": f"{p}faq/",
        "types": f"{p}kazino-bonuslari/",
        "rating": f"{p}#rating" if lang == "ru" else "../#rating",
    }


def _brand_link(slug: str, lang: str) -> str:
    p = "/ru/" if lang == "ru" else "../"
    return f"{p}{slug}/"


def _top20_rows(lang: str, linked: bool = True) -> str:
    rows = TOP20_RU if lang == "ru" else TOP20_UZ
    out = []
    for i, (slug, name, welcome, wag, pay) in enumerate(rows, 1):
        name_cell = (
            f'<a href="{_brand_link(slug, lang)}">{escape(name)}</a>'
            if linked
            else escape(name)
        )
        out.append(
            f"<tr><td>{i}</td><td>{name_cell}</td>"
            f"<td>{escape(welcome)}</td><td>{wag}</td><td>{escape(pay)}</td></tr>"
        )
    return "\n".join(out)


def _faq_items(items: list[tuple[str, str]], open_first: bool = True) -> str:
    parts = []
    for i, (q, a) in enumerate(items):
        open_cls = " is-open" if i == 0 and open_first else ""
        expanded = "true" if i == 0 and open_first else "false"
        parts.append(
            f'<article class="faq-item{open_cls}">'
            f'<button type="button" class="faq-item__question" aria-expanded="{expanded}">'
            f"<span>{escape(q)}</span>"
            f'<span class="faq-item__icon" aria-hidden="true">+</span></button>'
            f'<div class="faq-item__answer">{a}</div></article>'
        )
    return "\n".join(parts)


def _cta(lang: str) -> str:
    label = "Получить бонус" if lang == "ru" else "Bonus olish"
    return f'<p class="hub-cta-wrap"><button type="button" class="btn btn--gold js-go-partner">{label}</button></p>'


def _disclaimer(lang: str) -> str:
    if lang == "ru":
        return (
            '<p class="footer-note">18+. casino-bonuses-uz.com — независимый рейтинговый портал, '
            "не оператор. Азартные игры связаны с риском; устанавливайте лимиты. "
            'Точные условия бонусов — только в PROMO на сайте оператора.</p>'
        )
    return (
        '<p class="footer-note">18+. casino-bonuses-uz.com — mustaqil reyting portali, operator emas. '
        "Qimor xavfli; byudjet va vaqt limitlarini belgilang. "
        "Aniq bonus shartlari faqat operator PROMO bo'limida.</p>"
    )



def _brand_overview_block(lang: str, L: dict) -> str:
    """~700 words: short paragraph per TOP-20 brand."""
    rows = TOP20_RU if lang == "ru" else TOP20_UZ
    title = "TOP-20 brendlar bo'yicha qisqa tahlil" if lang == "uz" else "Краткий разбор TOP-20 брендов"
    intro = (
        "<p>Quyida reytingimizdagi har bir operator — welcome, wagering va to'lovlar kontekstida. "
        "Har bir nom ichki sharhga yo'naltiradi; summalar 2026 yil bahosi, depozitdan oldin PROMO da tekshiring.</p>"
        if lang == "uz"
        else "<p>Ниже — каждый оператор рейтинга в контексте welcome, вейджера и платежей. "
        "Имена ведут на обзоры; суммы — оценка 2026 года, сверяйте в PROMO перед депозитом.</p>"
    )
    parts = [f'<section class="section prose" id="brand-overview"><h2>{title}</h2>{intro}']
    for i, (slug, name, welcome, wag, pay) in enumerate(rows, 1):
        link = _brand_link(slug, lang)
        if lang == "uz":
            if slug == "fairpari":
                extra = (
                    " UZ bozorida eng katta kazino paketi — 20 200 000 UZS + 150 FS to'rt depozitda; "
                    "sport alternativi 1 400 000 UZS. Promo fa_1635."
                )
            elif slug == "bc-game":
                extra = " Humo yo'q — asosan USDT/BTC; kripto fokusli o'yinchilar uchun."
            elif slug in ("leon", "fonbet", "parimatch", "marathonbet", "betway", "linebet"):
                extra = " Sport BK — welcome ekspress ×5–×6 atrofida; kazino ikkinchi darajada."
            else:
                extra = f" Wagering {wag}; to'lovlar: {pay}."
            parts.append(
                f'<p><strong>{i}. <a href="{link}">{escape(name)}</a></strong> — {escape(welcome)}.{extra} '
                f'<a href="{link}">To\'liq sharh</a> va <a href="{L["welcome"]}">welcome taqqoslash</a> bilan birga o\'qing.</p>'
                f"<p>{i}-pozitsiya: wagering {wag}, to'lovlar {escape(pay)}. "
                f"Agar sizga slot muhim bo'lsa — kazino-brendlarni; sport uchun — Linebet, Leon, Parimatch kabi BK larni ko'ring. "
                f"PROMO shartlarini depozitdan oldin o'qing.</p>"
            )
        else:
            if slug == "fairpari":
                extra = (
                    " Крупнейший казино-пакет UZ — 20 200 000 UZS + 150 FS на четыре депозита; "
                    "спорт — до 1 400 000 UZS. Промо fa_1635."
                )
            elif slug == "bc-game":
                extra = " Humo нет — USDT/BTC; для крипто-игроков."
            elif slug in ("leon", "fonbet", "parimatch", "marathonbet", "betway", "linebet"):
                extra = " Спортивные БК — welcome на экспресс ×5–×6; казино вторично."
            else:
                extra = f" Вейджер {wag}; платежи: {pay}."
            parts.append(
                f'<p><strong>{i}. <a href="{link}">{escape(name)}</a></strong> — {escape(welcome)}.{extra} '
                f'<a href="{link}">Полный обзор</a> и <a href="{L["welcome"]}">сравнение welcome</a>.</p>'
                f"<p>Позиция #{i}: вейджер {wag}, платежи {escape(pay)}. "
                f"Для слотов смотрите казино-бренды; для спорта — БК вроде Linebet, Leon, Parimatch. "
                f"Условия PROMO читайте до депозита.</p>"
            )
    parts.append("</section>")
    return "\n".join(parts)


def _wagering_deep_block(lang: str, L: dict) -> str:
    title = "Wagering chuqur qo'llanma" if lang == "uz" else "Углублённый гид по вейджеру"
    if lang == "uz":
        body = (
            "<p>Wagering — bonusni yechishdan oldin aylantirish talabi. Misol: 1 000 000 UZS bonus, ×35 — "
            "35 000 000 UZS aylanish slotlarda (100% hisob). FairPari 20,2 mln paketida umumiy aylanish katta — "
            "lekin muddat va max bet muhim.</p>"
            "<p>Slotlar odatda 100%, live ruletka 10–20%, stol o'yinlari 5–10%. Crash (Aviator) ba'zan 0% — PROMO ro'yxatini oching. "
            "Sport welcome alohida: ekspress ×5, koeffitsientlar cheklovi bo'lishi mumkin.</p>"
            "<h3>Max bet va muddat</h3>"
            "<p>Faol bonusda spin yoki stavka limiti — 50 000–130 000 UZS. Oshirish bonusni bekor qiladi. "
            "Muddat 7–14 kun (kazino), 30 kun (sport). Vaqt tugasa qoldiq yo'qoladi.</p>"
            f'<p>Batafsil: <a href="{L["types"]}">bonus turlari</a>, <a href="{L["fairpari"]}">FairPari</a>, '
            f'<a href="{L["faq"]}">FAQ</a>.</p>'
        )
    else:
        body = (
            "<p>Вейджер — оборот бонуса перед выводом. Пример: бонус 1 000 000 UZS при ×35 — "
            "35 000 000 UZS в слотах (100% зачёт). У пакета FairPari 20,2 млн общий оборот велик — "
            "но критичны срок и max bet.</p>"
            "<p>Слоты обычно 100%, live-рулетка 10–20%, настольные 5–10%. Crash (Aviator) иногда 0% — смотрите PROMO. "
            "Спорт welcome отдельно: экспресс ×5, могут быть ограничения по коэффициентам.</p>"
            "<h3>Max bet и срок</h3>"
            "<p>При активном бонусе лимит ставки — 50 000–130 000 UZS. Превышение аннулирует бонус. "
            "Срок 7–14 дней (казино), 30 дней (спорт). Просрочка обнуляет остаток.</p>"
            f'<p>Подробнее: <a href="{L["types"]}">типы бонусов</a>, <a href="{L["fairpari"]}">FairPari</a>, '
            f'<a href="{L["faq"]}">FAQ</a>.</p>'
        )
    return f'<section class="section section--alt prose" id="wagering-deep"><h2>{title}</h2>{body}</section>'


def _payment_deep_block(lang: str, L: dict) -> str:
    title = "To'lovlar va bonus — amaliy maslahatlar" if lang == "uz" else "Платежи и бонус — практические советы"
    if lang == "uz":
        body = (
            "<p>UZS hisob oching — konvertatsiyasiz. Humo/Uzcard bank ilovasi orqali; Payme/Click QR bilan. "
            "Birinchi depozitdan oldin promokod (FairPari: fa_1635). Minimal ~130 000 UZS.</p>"
            "<p>Yechish: KYC (pasport), 1–24 soat kartaga. Ba'zi operatorlar yechishni depozit usuliga qaytaradi. "
            "Kripto — 1xBet, BC.Game; Humo talab qiladiganlar uchun mos emas.</p>"
            f"<p><a href=\"{L['pay']}\">To'lovlar hub</a>, <a href=\"{L['welcome']}\">welcome</a>.</p>"
        )
    else:
        body = (
            "<p>Откройте счёт UZS — без конвертации. Humo/Uzcard через банк; Payme/Click по QR. "
            "Промокод до депозита (FairPari: fa_1635). Минимум ~130 000 UZS.</p>"
            "<p>Вывод: KYC (паспорт), 1–24 часа на карту. Часто вывод тем же методом, что депозит. "
            "Крипто — 1xBet, BC.Game; не для тех, кому нужен Humo.</p>"
            f'<p><a href="{L["pay"]}">Хаб платежей</a>, <a href="{L["welcome"]}">welcome</a>.</p>'
        )
    return f'<section class="section prose" id="pay-deep"><h2>{title}</h2>{body}</section>'


def _responsible_block(lang: str) -> str:
    title = "Mas'uliyatli o'yin" if lang == "uz" else "Ответственная игра"
    if lang == "uz":
        body = (
            "<p>18+. Qimor — ko'ngilochar xarajat, daromad manbai emas. Kunlik/haftalik depozit limiti, "
            "yo'qotish limiti va sessiya taymerini operator kabinetida yoqing. Muammo bo'lsa — "
            "o'z-o'zini chetlashtirish (self-exclusion) va professional yordam.</p>"
            "<p>casino-bonuses-uz.com faqat ma'lumot beradi; depozit qabul qilmaydi. "
            "Faqat rasmiy operator saytida ro'yxatdan o'ting.</p>"
        )
    else:
        body = (
            "<p>18+. Азартные игры — развлечение, не источник дохода. Установите дневные/недельные лимиты "
            "депозита, лимит проигрыша и таймер сессии в кабинете. При проблемах — самоисключение и помощь специалистов.</p>"
            "<p>casino-bonuses-uz.com только информирует; депозиты не принимает. "
            "Регистрируйтесь только на официальном сайте оператора.</p>"
        )
    return f'<section class="section section--alt prose" id="responsible"><h2>{title}</h2>{body}</section>'


def _registration_block(lang: str, L: dict) -> str:
    title = "Ro'yxatdan o'tish va bonus faollashtirish" if lang == "uz" else "Регистрация и активация бонуса"
    if lang == "uz":
        body = (
            "<p>Operator rasmiy saytida 2–5 daqiqa: telefon yoki email, valyuta UZS, welcome turi (kazino yoki sport). "
            "FairPari uchun kazino paketida <strong>fa_1635</strong> promokodini depozitdan oldin kiriting. "
            "Keyin Humo, Payme yoki Uzcard orqali minimal summadan yuqori depozit.</p>"
            "<p>Bonus PROMO kabinetida ko'rinadi. Wagering boshlanguncha shartlarni o'qing: max bet, ruxsat etilgan slotlar, muddat. "
            "Bitta shaxs — bitta akkaunt. Multiakkaunt blok va bonus musodarasiga olib keladi.</p>"
            f'<p>Bog\'liq sahifalar: <a href="{L["welcome"]}">welcome taqqoslash</a>, '
            f'<a href="{L["pay"]}">to\'lovlar</a>, <a href="{L["fairpari"]}">FairPari #1</a>.</p>'
        )
    else:
        body = (
            "<p>На официальном сайте оператора 2–5 минут: телефон или email, валюта UZS, тип welcome (казино или спорт). "
            "Для FairPari в казино-пакете введите промокод <strong>fa_1635</strong> до депозита. "
            "Затем пополнение от минимума через Humo, Payme или Uzcard.</p>"
            "<p>Бонус виден в PROMO-кабинете. До отыгрыша изучите условия: max bet, разрешённые слоты, срок. "
            "Один человек — один аккаунт. Мультиаккаунт ведёт к блокировке и конфискации бонуса.</p>"
            f'<p>Связанные страницы: <a href="{L["welcome"]}">сравнение welcome</a>, '
            f'<a href="{L["pay"]}">платежи</a>, <a href="{L["fairpari"]}">FairPari #1</a>.</p>'
        )
    return f'<section class="section prose" id="registration"><h2>{title}</h2>{body}</section>'


def _reload_vip_block(lang: str, L: dict) -> str:
    title = "Reload, VIP va turnir bonuslari" if lang == "uz" else "Reload, VIP и турнирные бонусы"
    if lang == "uz":
        body = (
            "<p>Welcome dan keyin operatorlar muntazam <strong>reload</strong> aksiyalarini e'lon qiladi: "
            "keyingi depozitga 25–75% foiz. <strong>VIP darajalar</strong> keshbek va shaxsiy menejerni ochishi mumkin. "
            "<strong>Turnirlar</strong> slot yoki sport bo'yicha — sovrin jamg'armasi leaderboard asosida taqsimlanadi.</p>"
            "<p>FairPari #1 sababi — nafaqat 20 200 000 UZS + 150 FS welcome, balki sport alternativi 1 400 000 UZS "
            "va tez-tez yangilanadigan PROMO. Boshqa TOP-20 brendlar ham o'z reload va VIP dasturlariga ega; "
            "har biri uchun brend sahifasidagi jadvalni tekshiring.</p>"
            f'<p><a href="{L["types"]}">Bonus turlari</a> · <a href="{L["rating"]}">TOP-20 reyting</a></p>'
        )
    else:
        body = (
            "<p>После welcome операторы регулярно объявляют <strong>reload</strong>: 25–75% на повторный депозит. "
            "<strong>VIP-уровни</strong> открывают кешбэк и персонального менеджера. "
            "<strong>Турниры</strong> по слотам или спорту — призовой фонд по таблице лидеров.</p>"
            "<p>FairPari #1 не только за 20 200 000 UZS + 150 FS welcome, но и за спорт-альтернативу 1 400 000 UZS "
            "и частые обновления PROMO. У других TOP-20 свои reload и VIP — смотрите таблицы на страницах брендов.</p>"
            f'<p><a href="{L["types"]}">Типы бонусов</a> · <a href="{L["rating"]}">Рейтинг TOP-20</a></p>'
        )
    return f'<section class="section section--alt prose" id="reload-vip"><h2>{title}</h2>{body}</section>'


def _slug_tail_block(slug: str, lang: str, L: dict) -> str:
    if slug == "depozitsiz-bonus":
        title = "Minimal depozit strategiyasi" if lang == "uz" else "Стратегия минимального депозита"
        if lang == "uz":
            body = (
                "<p>Depozitsiz o'rniga minimal depozit + welcome ko'pincha yaxshi natija beradi: aniq wagering, "
                "KYC jarayoni va yechish yo'li ma'lum. FairPari da 130 000 UZS atrofida boshlash mumkin — "
                "to'liq 20,2 mln uchun to'rtta bosqich kerak. Har bosqichda promo fa_1635 va PROMO qoidalariga rioya qiling.</p>"
                "<p>1win ba'zan ro'yxatdan FS beradi — shartlar o'zgaruvchan. Mostbet va Melbet ham vaqtinchak aksiyalar "
                "o'tkazadi, lekin asosiy paket depozitli. Google reklamalaridagi «100% free» ni rasmiy PROMO bilan solishtiring.</p>"
                "<p>TOP-20 dagi qolgan operatorlar — Pin-Up, Betwinner, Megapari, 22Bet, Vulkan Vegas, Joycasino, "
                "Fresh Casino, BC.Game — ham asosan depozitli welcome modelida. "
                f'<a href="{L["rating"]}">Reyting jadvali</a> va <a href="{L["types"]}">bonus turlari</a> yordam beradi.</p>'
            )
        else:
            body = (
                "<p>Вместо бездепозита часто выгоднее минимальный депозит + welcome: понятный вейджер, "
                "KYC и путь вывода. У FairPari старт от ~130 000 UZS — для полных 20,2 млн нужны четыре этапа. "
                "На каждом этапе промо fa_1635 и правила PROMO.</p>"
                "<p>1win иногда даёт FS за регистрацию — условия меняются. Mostbet и Melbet проводят временные акции, "
                "но основной пакет с депозитом. Сравнивайте рекламу «100% free» с официальным PROMO. "
                "Полный рейтинг — на <a href=\"" + L["rating"] + "\">главной TOP-20</a>; welcome — "
                "<a href=\"" + L["welcome"] + "\">сравнение пакетов</a>.</p>"
                "<p>Остальные TOP-20 — Pin-Up, Betwinner, Megapari, 22Bet, Vulkan Vegas, Joycasino, "
                "Fresh Casino, BC.Game — тоже в основном с депозитом. "
                f'См. <a href="{L["types"]}">типы бонусов</a> и обзоры каждого бренда.</p>'
            )
    elif slug == "tolov-uz":
        title = "Yechish va KYC — amaliy qadamlar" if lang == "uz" else "Вывод и KYC — практические шаги"
        if lang == "uz":
            body = (
                "<p>Birinchi yechish: pasport/ID yuklash, ba'zan selfi. Tasdiqlash bir necha soatdan 3 kungacha. "
                "Wagering tugallangan va bonus ochilgan bo'lishi kerak. Kartaga yechish 1–24 soat — operator va bankga bog'liq.</p>"
                "<p>Humo va Uzcard odatda tezroq; kripto — blockchain tasdig'ini kutish. "
                "FairPari, 1win, Mostbet TOP-20 da eng ko'p sharhlangan to'lov tajribasiga ega. "
                "Faqat rasmiy domen orqali kassa oching.</p>"
            )
        else:
            body = (
                "<p>Первый вывод: загрузка паспорта/ID, иногда селфи. Верификация от нескольких часов до 3 дней. "
                "Вейджер должен быть завершён, бонус открыт. Вывод на карту 1–24 часа — зависит от оператора и банка.</p>"
                "<p>Humo и Uzcard обычно быстрее; крипто — ожидание подтверждений блокчейна. "
                "FairPari, 1win, Mostbet — больше всего отзывов о платежах в TOP-20. "
                "Открывайте кассу только на официальном домене.</p>"
            )
    elif slug == "faq":
        title = "Qo'shimcha maslahatlar" if lang == "uz" else "Дополнительные советы"
        if lang == "uz":
            body = (
                "<p>Savol berishdan oldin operator PROMO, bizning <a href=\"" + L["rating"] + "\">TOP-20</a> jadvali va "
                "brend sharhlarini tekshiring. FairPari 20 200 000 UZS + 150 FS va sport 1 400 000 UZS — "
                "reytingimizdagi asosiy referens nuqtalar. Wagering ×35 kazino uchun o'rtacha mezon.</p>"
                "<p>Agar depozitsiz qidirsangiz — <a href=\"" + L["nodep"] + "\">depozitsiz sahifa</a>. "
                "To'lovlar: <a href=\"" + L["pay"] + "\">Humo/Payme qo'llanmasi</a>. "
                "Welcome: <a href=\"" + L["welcome"] + "\">taqqoslash jadvali</a>. "
                "Bonus turlari: <a href=\"" + L["types"] + "\">kazino bonuslari hub</a>.</p>"
            )
        else:
            body = (
                "<p>Перед вопросом проверьте PROMO оператора, таблицу <a href=\"" + L["rating"] + "\">TOP-20</a> "
                "и обзоры брендов. FairPari 20 200 000 UZS + 150 FS и спорт 1 400 000 UZS — "
                "главные ориентиры рейтинга. Вейджер ×35 — средний ориентир для казино.</p>"
                "<p>Бездепозит — <a href=\"" + L["nodep"] + "\">страница бездепозита</a>. "
                "Платежи: <a href=\"" + L["pay"] + "\">гид Humo/Payme</a>. "
                "Welcome: <a href=\"" + L["welcome"] + "\">таблица сравнения</a>. "
                "Типы бонусов: <a href=\"" + L["types"] + "\">хаб казино-бонусов</a>. "
                "Мы не оператор — регистрация только на сайте бренда.</p>"
            )
    elif slug in ("kazino-bonuslari", "welcome-bonus"):
        title = "Metodologiya" if lang == "ru" else "Metodologiya"
        if lang == "uz":
            body = (
                "<p>casino-bonuses-uz.com mustaqil reyting: welcome hajmi, wagering, Humo/Payme, mobil ilova va "
                "UZ fikrlar asosida TOP-20 tuziladi. 2026 yangilangan. FairPari #1 — 20,2 mln + 150 FS va sport 1,4 mln "
                "referens. Har bir brend uchun alohida sharh sahifasi mavjud.</p>"
            )
        else:
            body = (
                "<p>casino-bonuses-uz.com — независимый рейтинг: размер welcome, вейджер, Humo/Payme, мобильное приложение "
                "и отзывы UZ. Обновлено 2026. FairPari #1 — 20,2 млн + 150 FS и спорт 1,4 млн как ориентир. "
                "На каждый бренд — отдельная страница обзора.</p>"
            )
    else:
        return ""
    return f'<section class="section prose" id="slug-tail"><h2>{title}</h2>{body}</section>'


def _hub_pad_block(slug: str, lang: str, L: dict) -> str:
    """Extra paragraphs for hubs still under 2000 words after main body."""
    if slug not in ("depozitsiz-bonus", "faq", "tolov-uz"):
        return ""
    if lang == "uz":
        if slug == "depozitsiz-bonus":
            title = "Depozitsiz so'rovlar — qo'shimcha maslahatlar"
            body = (
                "<p>Google va ijtimoiy tarmoqlarda «depozitsiz bonus» qidiruvlari ko'p, lekin UZ bozorida 2026 yilda "
                "asosiy oqim — birinchi depozitga welcome. Agar depozitsiz taklif ko'rsangiz, manbani tekshiring: "
                "rasmiy operator PROMO yoki uchinchi tomondagi reklama. Soxta havolalar pasport ma'lumotlarini "
                "o'g'irlash uchun ishlatilishi mumkin.</p>"
                "<p>Minimal depozit (masalan 30 000–50 000 UZS) bilan welcome olish ko'pincha xavfsizroq alternativa. "
                f"<a href=\"{L['fairpari']}\">FairPari</a> 20 200 000 UZS + 150 FS to'rt depozitga bo'linadi — "
                "birinchi to'lov kichik bo'lishi mumkin. Wagering ×35 — bozor o'rtachasi.</p>"
                f"<p>Batafsil: <a href=\"{L['welcome']}\">welcome jadvali</a>, "
                f"<a href=\"{L['types']}\">bonus turlari</a>, <a href=\"{L['rating']}\">TOP-20</a>. 18+.</p>"
                "<p>Yuqori wageringli depozitsiz aksiyalar ko'pincha kichik depozit + oddiy welcome dan kam foydali. "
                "Bannerdagi raqam emas, to'liq aylanma narxini solishtiring.</p>"
                "<p>Agar operator depozitsiz FS yoki bepul stavka taklif qilsa, odatda max yechish limiti qattiq bo'ladi — "
                "masalan 500 000 UZS dan oshmasin. Welcome esa yuqori limit bilan kelishi mumkin.</p>"
            )
        elif slug == "faq":
            title = "Qo'shimcha savollar va manbalar"
            body = (
                "<p>Agar javob topilmasa, avval operator PROMO va shaxsiy kabinetni tekshiring — bonus holati va wagering "
                "qoldig'i u yerda ko'rinadi. casino-bonuses-uz.com operator qo'llab-quvvatlashi emas; biz faqat "
                "reyting va sharhlarni yangilaymiz.</p>"
                "<p>Humo, Payme, Click bo'yicha: <a href=\"" + L["pay"] + "\">to'lovlar hub</a>. "
                "Welcome taqqoslash: <a href=\"" + L["welcome"] + "\">welcome sahifa</a>. "
                "FairPari referens: 20,2 mln UZS + 150 FS, sport 1,4 mln, promo fa_1635.</p>"
                "<p>Har bir TOP-20 brend uchun alohida sharh mavjud — reyting kartasidan o'ting. "
                "Ma'lumot 2026 yil uchun; depozitdan oldin rasmiy saytda summalarni tasdiqlang.</p>"
                "<p>Wagering, max bet va ruxsat etilgan o'yinlar har operatorda farq qiladi — FAQ javoblari umumiy qo'llanma; "
                "aniq raqamlar uchun PROMO shartnomasini o'qing. Agar bonus kutilganidek tushmasa, depozit summasi minimaldan "
                "past emasligini va to'g'ri welcome turini tanlaganingizni tekshiring.</p>"
            )
        else:
            title = "To'lovlar bo'yicha qo'shimcha"
            body = (
                "<p>Yechish kechiksa, KYC holatini va bonus wagering tugaganligini tekshiring — faol bonus bilan "
                "yechish so'rovi rad etilishi yoki bonus yo'qolishi mumkin. Humo va Uzcard odatda eng barqaror "
                "kanallar UZ da.</p>"
                f"<p>Welcome faollashtirish: <a href=\"{L['welcome']}\">welcome</a>. "
                f"Bonus turlari: <a href=\"{L['types']}\">hub</a>. "
                f"<a href=\"{L['fairpari']}\">FairPari</a> — Humo, Payme, Click qabul qiladi. "
                "Birinchi yechishda pasport tayyor bo'lsin; bonus wagering tugamaguncha yechish so'ramang.</p>"
            )
    else:
        if slug == "depozitsiz-bonus":
            title = "Дополнительно о запросах без депозита"
            body = (
                "<p>В поиске Google и соцсетях много запросов «бонус без депозита», но на рынке UZ в 2026 основной "
                "поток — welcome на первый депозит. Любое бездепозитное предложение проверяйте по источнику: "
                "официальный PROMO оператора или сторонняя реклама. Фишинговые ссылки могут красть паспортные данные.</p>"
                "<p>Минимальный депозит (30 000–50 000 UZS) с welcome часто безопаснее сомнительного «no deposit». "
                f'<a href="{L["fairpari"]}">FairPari</a> — 20 200 000 UZS + 150 FS на четыре депозита; '
                "первый платёж может быть небольшим. Вейджер ×35 — средний ориентир рынка.</p>"
                f'<p>См. также: <a href="{L["welcome"]}">таблица welcome</a>, '
                f'<a href="{L["types"]}">типы бонусов</a>, <a href="{L["rating"]}">TOP-20</a>. 18+.</p>'
                "<p>Бездепозитные акции с высоким вейджером ×40–×50 часто менее выгодны, чем небольшой депозит с нормальным welcome. "
                "Сравните полную стоимость отыгрыша, а не только заголовок на баннере.</p>"
                "<p>Мы регулярно сверяем условия TOP-5 операторов; при изменении welcome у FairPari или конкурентов обновляем хаб и карточки рейтинга. "
                "Подпишитесь на обновления через возврат на главную — таблица TOP-20 всегда актуальна на момент публикации.</p>"
                "<p>Бездепозитные FS или freebet часто имеют жёсткий лимит вывода — например не более 500 000 UZS, тогда как welcome допускает большую выплату после вейджера.</p>"
                "<p>На главной рейтинга можно отфильтровать только казино или только БК — так проще найти оператора с подходящим типом welcome без лишнего шума.</p>"
                "<p>Перед регистрацией сравните вейджер и срок отыгрыша у двух-трёх финалистов — это сэкономит время и снизит риск ошибки с типом бонуса.</p>"
            )
        elif slug == "faq":
            title = "Дополнительные вопросы и источники"
            body = (
                "<p>Если ответа нет — сначала PROMO и личный кабинет оператора: там статус бонуса и остаток вейджера. "
                "casino-bonuses-uz.com не служба поддержки брендов; мы обновляем рейтинг и обзоры.</p>"
                "<p>Платежи Humo/Payme: <a href=\"" + L["pay"] + "\">хаб платежей</a>. "
                "Welcome: <a href=\"" + L["welcome"] + "\">сравнение</a>. "
                "Ориентир FairPari: 20,2 млн UZS + 150 FS, спорт 1,4 млн, промокод fa_1635.</p>"
                "<p>На каждый бренд из TOP-20 — отдельная страница обзора. Данные 2026; перед депозитом сверяйте суммы на официальном сайте.</p>"
                "<p>Вейджер, max bet и список игр различаются — ответы FAQ носят общий характер; точные цифры в PROMO. "
                "Если бонус не начислился, проверьте минимальный депозит и выбранный тип welcome (казино vs спорт).</p>"
                "<p>Для сравнения welcome по всем двадцати операторам откройте главную страницу рейтинга — фильтры «Казино», «БК» и поиск по названию ускоряют выбор. "
                "FairPari остаётся эталоном по сумме пакета в UZS на 2026 год.</p>"
                "<p>Если вопрос касается конкретного бренда — перейдите на его обзор из таблицы TOP-20: там платежи, вейджер и плюсы/минусы собраны на одной странице.</p>"
                "<p>Не путайте информационный портал с поддержкой оператора: споры по бонусу решаются только в кабинете или чате на официальном сайте бренда.</p>"
            )
        else:
            title = "Дополнительно о платежах"
            body = (
                "<p>При задержке вывода проверьте KYC и завершён ли вейджер — с активным бонусом заявку могут отклонить. "
                "Humo и Uzcard — самые стабильные каналы в UZ.</p>"
                f'<p>Welcome: <a href="{L["welcome"]}">сравнение</a>. '
                f'Типы бонусов: <a href="{L["types"]}">хаб</a>. '
                f'<a href="{L["fairpari"]}">FairPari</a> принимает Humo, Payme, Click. '
                "При первом выводе подготовьте паспорт; не запрашивайте выплату до завершения вейджера.</p>"
                "<p>Комиссии банка и оператора могут различаться: Payme/Click иногда берут сервисный сбор, Humo/Uzcard чаще без доплаты со стороны БК. "
                "Лимиты на вывод смотрите в кассе после верификации.</p>"
            )
    tail = (
        "18+. Ma'lumot xarakterida; depozit faqat rasmiy operator saytida."
        if lang == "uz"
        else "18+. Информация носит справочный характер; депозит только на официальном сайте оператора."
    )
    return f'<section class="section section--alt prose" id="hub-pad"><h2>{title}</h2>{body}<p class="hub-pad-tail">{tail}</p></section>'


def _pass4c_final_block(slug: str, lang: str, L: dict) -> str:
    if slug != "tolov-uz":
        return ""
    if lang == "ru":
        title = "Что запомнить о платежах в Узбекистане"
        body = (
            "<p>Для игрока из UZ способ оплаты не менее важен, чем цифра welcome на баннере. "
            "<strong>Humo</strong> и <strong>Uzcard</strong> закрывают большинство депозитов в нашем TOP-20; "
            "<strong>Payme</strong> и <strong>Click</strong> удобны с телефона, если пополняете счёт без карты под рукой. "
            "Зачисление обычно занимает минуты, но бонус активируется только после выполнения условий PROMO — "
            "промокода, выбора пакета и минимальной суммы.</p>"
            "<p>Вывод проходит после верификации: паспорт или ID, иногда селфи. Заявку могут задержать, "
            "если welcome ещё не отыгран или выбран другой канал, чем при пополнении. "
            f'<a href="{L["fairpari"]}">FairPari</a>, <a href="{_brand_link("1win", lang)}">1win</a> и '
            f'<a href="{_brand_link("mostbet", lang)}">Mostbet</a> чаще других упоминаются в отзывах '
            "за стабильные выплаты на локальные карты.</p>"
            "<p>Рабочий порядок для welcome: регистрация на официальном сайте → промокод "
            "(для казино FairPari — <strong>fa_1635</strong>) → выбор пакета в PROMO → депозит выбранным методом. "
            "Не переводите деньги по ссылкам из мессенджеров и не доверяйте «личным менеджерам» вне кассы оператора.</p>"
            f'<p>Дальше: <a href="{L["welcome"]}">сравнение welcome</a>, '
            f'<a href="{L["rating"]}">рейтинг TOP-20</a>, '
            f'<a href="{L["types"]}">типы бонусов</a>. '
            "18+, играйте ответственно.</p>"
        )
    else:
        title = "O'zbekistonda to'lovlar haqida nimalarni eslab qolish kerak"
        body = (
            "<p>UZ o'yinchisi uchun to'lov usuli bannerdagi welcome raqamidan kam muhim emas. "
            "<strong>Humo</strong> va <strong>Uzcard</strong> TOP-20 dagi depozitlarning ko'pchiligini qoplaydi; "
            "<strong>Payme</strong> va <strong>Click</strong> telefondan to'ldirishda qulay. "
            "Mablag' odatda daqiqalar ichida tushadi, lekin bonus faqat PROMO shartlari bajarilgach faollashadi — "
            "promokod, paket tanlovi va minimal summa.</p>"
            "<p>Yechish verifikatsiyadan keyin: pasport yoki ID, ba'zan selfi. So'rov kechikishi mumkin, "
            "agar welcome tugallanmagan yoki depozitdan boshqa kanal tanlangan bo'lsa. "
            f'<a href="{L["fairpari"]}">FairPari</a>, <a href="{_brand_link("1win", lang)}">1win</a> va '
            f'<a href="{_brand_link("mostbet", lang)}">Mostbet</a> mahalliy kartalarga yechishda ko\'proq '
            "ishonchli deb tilga olinadi.</p>"
            "<p>Welcome uchun tartib: rasmiy saytda ro'yxatdan o'tish → promokod "
            "(FairPari kazino — <strong>fa_1635</strong>) → PROMO da paket → tanlangan usulda depozit. "
            "Telegram havolalari va operator kassasidan tashqari «menejerlar»ga pul yubormang.</p>"
            f'<p>Keyingi qadamlar: <a href="{L["welcome"]}">welcome taqqoslash</a>, '
            f'<a href="{L["rating"]}">TOP-20 reyting</a>, '
            f'<a href="{L["types"]}">bonus turlari</a>. 18+.</p>'
        )
    return f'<section class="section prose" id="pass4c-final"><h2>{title}</h2>{body}</section>'


def _hub_extra(slug: str, lang: str, L: dict) -> str:
    blocks = [
        _wagering_deep_block(lang, L),
        _registration_block(lang, L),
        _reload_vip_block(lang, L),
        _brand_overview_block(lang, L),
        _responsible_block(lang),
    ]
    if slug in ("tolov-uz", "welcome-bonus", "depozitsiz-bonus"):
        blocks.insert(2, _payment_deep_block(lang, L))
    tail = _slug_tail_block(slug, lang, L)
    if tail:
        blocks.append(tail)
    blocks.append(_hub_pad_block(slug, lang, L))
    final = _pass4c_final_block(slug, lang, L)
    if final:
        blocks.append(final)
    return "\n".join(blocks)


def hub_body(slug: str, lang: str) -> str:
    if lang not in ("uz", "ru"):
        raise ValueError(f"lang must be uz or ru, got {lang!r}")
    builders = {
        "kazino-bonuslari": _body_kazino_bonuslari,
        "welcome-bonus": _body_welcome_bonus,
        "depozitsiz-bonus": _body_depozitsiz_bonus,
        "tolov-uz": _body_tolov_uz,
        "faq": _body_faq,
    }
    if slug not in builders:
        raise KeyError(f"Unknown slug: {slug!r}")
    return builders[slug](lang)


# --- slug bodies ---


def _body_kazino_bonuslari(lang: str) -> str:
    L = _links(lang)
    if lang == "ru":
        bc = "Главная"
        crumb = "Типы казино-бонусов"
        h1 = "Типы казино-бонусов — welcome, FS, кешбэк"
        intro = (
            '<p class="page-intro">Онлайн-казино и букмекеры в Узбекистане предлагают разные форматы поощрений: '
            "<strong>welcome-пакет</strong> на первые депозиты, <strong>free spins</strong>, <strong>кешбэк</strong>, "
            "<strong>reload</strong> и редкие <strong>бездепозитные</strong> акции. Для игроков UZ критичны счёт в "
            "<strong>UZS</strong>, Humo, Uzcard, Payme и Click. Ниже — полный разбор типов бонусов, таблица вейджера, "
            f'обзор <a href="{L["rating"]}">рейтинга TOP-20</a> и практические советы по выбору оператора.</p>'
        )
        s1_title = "Welcome bonus — пакет на первый депозит"
        s1 = (
            f'<p>Welcome — главная акция для нового аккаунта. Обычно начисляется после первого или нескольких депозитов: '
            f'процент к сумме, фриспины или комбинация. Лидер нашего рейтинга — '
            f'<a href="{L["fairpari"]}">FairPari</a>: <strong>20 200 000 UZS + 150 FS</strong> в четыре этапа, '
            f'вейджер ×35, промокод <strong>fa_1635</strong> для казино-пакета. Альтернатива — спортивный welcome '
            f'до <strong>1 400 000 UZS</strong>; казино и спорт одновременно выбрать нельзя. Подробное сравнение — '
            f'на странице <a href="{L["welcome"]}">welcome bonus</a>.</p>'
            f'<p>Второе место занимает <a href="{_brand_link("1win", lang)}">1win</a> (до 12 млн UZS, ×30), '
            f'третье — <a href="{_brand_link("mostbet", lang)}">Mostbet</a> (8,5 млн + 250 FS). '
            f'При выборе смотрите не только цифру на баннере, но и срок отыгрыша, max bet и список игр с полным зачётом.</p>'
        )
        s2_title = "Free spins, кешбэк и reload"
        s2 = (
            "<p><strong>Free spins (FS)</strong> — бесплатные вращения в слотах. Часто входят в welcome "
            "(у FairPari — 150 FS по этапам). Выигрыш с FS тоже подлежит вейджеру. "
            "<strong>Кешбэк</strong> возвращает часть проигрыша за период (неделя, VIP-уровень); "
            "типичный вейджер ×3–×10. <strong>Reload</strong> — бонус на повторный депозит: 25–50% к сумме, "
            "условия в разделе PROMO каждого оператора.</p>"
            "<p>У чистых казино-брендов (Vulkan Vegas, Joycasino, Fresh Casino) акцент на слотах и FS; "
            "у БК (Leon, Fonbet, Marathonbet) — на спортивных freebet и экспресс-акциях. "
            f'Типы без депозита разобраны отдельно: <a href="{L["nodep"]}">бездепозитный бонус</a>.</p>'
        )
        s3_title = "Таблица вейджера по типам бонусов"
        s4_title = "Рынок Узбекистана — UZS и платежи"
        s4 = (
            "<p>Локальный рынок требует счёта в сумах без лишней конвертации. TOP-20 операторов из нашего рейтинга "
            "принимают Humo и Uzcard; Payme и Click — у FairPari, Mostbet, Melbet и других. "
            "Бонус зачисляется только после подтверждённого депозита. Первый вывод почти всегда требует KYC. "
            f'Полный гид по методам: <a href="{L["pay"]}">платежи UZ</a>.</p>'
            "<p>Минимальный депозит для welcome обычно от 130 000 UZS. Крипто (USDT, BTC) доступна у 1xBet, "
            "BC.Game и части БК — удобно при отсутствии локальной карты, но минимумы выше и курс волатилен.</p>"
        )
        s5_title = "TOP-20 операторов — сводная таблица welcome"
        s6_title = "Как выбрать бонус — пошаговый алгоритм"
        s6 = (
            "<p>Не гонитесь за максимальной цифрой без расчёта оборота. Алгоритм для UZ:</p>"
            '<ol class="section-list">'
            "<li>Определите цель: казино (слоты, live) или спорт (экспресс, ординар).</li>"
            "<li>Сравните welcome и вейджер в таблице TOP-20 ниже.</li>"
            "<li>Проверьте платёжный метод — Humo/Payme должен быть в кассе.</li>"
            "<li>Изучите max bet при активном бонусе (часто 50 000–130 000 UZS).</li>"
            "<li>Введите промокод до депозита; для FairPari — fa_1635.</li>"
            f'<li>Прочитайте <a href="{L["faq"]}">FAQ</a> и обзор выбранного бренда.</li>'
            "</ol>"
            f'<p>Если приоритет — максимальный стартовый пакет, начните с '
            f'<a href="{L["fairpari"]}">обзора FairPari</a> (#1 в рейтинге 2026).</p>'
        )
        faq_title = "Частые вопросы о типах бонусов"
        faq = [
            (
                "Чем welcome отличается от reload?",
                f"Welcome — для нового аккаунта на первые депозиты (у FairPari до 20,2 млн UZS + 150 FS). "
                f"Reload — для уже зарегистрированных на повторные пополнения. Условия разные.",
            ),
            (
                "Можно ли совместить казино и спорт welcome?",
                "Обычно нет. При регистрации выбирают один тип: казино 20,2 млн + 150 FS или спорт ~1,4 млн UZS у FairPari.",
            ),
            (
                "Какой вейджер считается нормальным?",
                "Для казино ×30–×40 за 7–14 дней; для спорта ×5 на экспресс. Melbet и 1win предлагают ×30 — это ниже среднего.",
            ),
            (
                "Где смотреть актуальные акции?",
                f"Только в PROMO на официальном сайте оператора. Наш рейтинг <a href=\"{L['rating']}\">TOP-20</a> обновляется в 2026 году.",
            ),
            (
                "Есть ли бездепозитные бонусы?",
                f"Постоянные редки. См. раздел <a href=\"{L['nodep']}\">бездепозитный бонус</a> — мифы и реальные альтернативы.",
            ),
        ]
    else:
        bc = "Bosh sahifa"
        crumb = "Kazino bonuslari turlari"
        h1 = "Kazino bonuslari turlari — welcome, FS, keshbek"
        intro = (
            '<p class="page-intro">O\'zbekistonda onlayn kazino va bukmekerlar turli bonus formatlarini taklif qiladi: '
            "<strong>welcome paket</strong> birinchi depozit(lar)ga, <strong>free spins</strong>, <strong>cashback</strong>, "
            "<strong>reload</strong> va kamdan-kam <strong>depozitsiz</strong> aksiyalar. Mahalliy o'yinchilar uchun "
            "<strong>UZS hisob</strong>, Humo, Uzcard, Payme va Click muhim. Quyida bonus turlari, wagering jadvali, "
            f'<a href="{L["rating"]}">TOP-20 reyting</a> ko\'rib chiqilishi va operator tanlash bo\'yicha amaliy maslahatlar.</p>'
        )
        s1_title = "Welcome bonus — birinchi depozit paketi"
        s1 = (
            f'<p>Welcome yangi akkaunt uchun asosiy aksiya. Odatda birinchi yoki bir nechta depozitdan keyin foiz, '
            f'frispin yoki ikkalasi beriladi. Reytingimizda #1 — '
            f'<a href="{L["fairpari"]}">FairPari</a>: <strong>20 200 000 UZS + 150 FS</strong> to\'rtta bosqichda, '
            f'wagering ×35, kazino uchun promo <strong>fa_1635</strong>. Sport alternativi — '
            f'<strong>1 400 000 UZS</strong> gacha; kazino va sport bir vaqtda tanlanmaydi. '
            f'Batafsil <a href="{L["welcome"]}">welcome taqqoslash</a>.</p>'
            f'<p>#2 — <a href="{_brand_link("1win", lang)}">1win</a> (12 mln UZS gacha, ×30), '
            f'#3 — <a href="{_brand_link("mostbet", lang)}">Mostbet</a> (8,5 mln + 250 FS). '
            f"Bannerdagi raqamdan tashqari muddat, max bet va o'yinlar ro'yxatini ham tekshiring.</p>"
        )
        s2_title = "Free spins, cashback va reload"
        s2 = (
            "<p><strong>Free spins (FS)</strong> — slotlarda bepul aylantirishlar; ko'p hollarda welcome tarkibida "
            "(FairPari da 150 FS bosqichma-bosqich). FS yutug'i ham wageringga bo'ysunadi. "
            "<strong>Cashback</strong> — yo'qotilgan summaning qismini qaytarish (haftalik yoki VIP); wagering ×3–×10. "
            "<strong>Reload</strong> — keyingi depozitlarga qo'shimcha foiz (25–50%), shartlar PROMO da.</p>"
            "<p>Pok kazino brendlari (Vulkan Vegas, Joycasino, Fresh Casino) slot va FS ga urg'u beradi; "
            "BK lar (Leon, Fonbet, Marathonbet) — sport freebet va ekspress aksiyalariga. "
            f'Depozitsiz holat: <a href="{L["nodep"]}">depozitsiz bonus</a> sahifasi.</p>'
        )
        s3_title = "Wagering jadvali — bonus turlari bo'yicha"
        s4_title = "O'zbekiston bozori — UZS va to'lovlar"
        s4 = (
            "<p>Mahalliy bozor UZS hisobsiz konvertatsiyasiz ishlaydi. Reytingimizdagi TOP-20 operatorlar Humo va Uzcard "
            "qabul qiladi; Payme va Click — FairPari, Mostbet, Melbet va boshqalarda. Bonus faqat tasdiqlangan depozitdan "
            f"keyin tushadi. Birinchi yechishda KYC talab qilinishi mumkin. To'liq qo'llanma: "
            f'<a href="{L["pay"]}">to\'lovlar UZ</a>.</p>'
            "<p>Welcome uchun minimal depozit odatda 130 000 UZS dan. Kripto (USDT, BTC) — 1xBet, BC.Game va ayrim BK "
            "larda; minimal yuqori, kurs o'zgaruvchan.</p>"
        )
        s5_title = "TOP-20 operatorlar — welcome jadvali"
        s6_title = "Bonusni qanday tanlash — 6 qadam"
        s6 = (
            "<p>Maksimal raqamni aylanishsiz baholamang. UZ uchun algoritm:</p>"
            '<ol class="section-list">'
            "<li>Maqsad: kazino (slot, live) yoki sport (ekspress, ordinari).</li>"
            "<li>Quyidagi TOP-20 jadvalida welcome va wagering ni solishtiring.</li>"
            "<li>To'lov usuli — Humo/Payme kassada bo'lishi kerak.</li>"
            "<li>Faol bonusda max bet (50 000–130 000 UZS).</li>"
            "<li>Depozitdan oldin promokod; FairPari uchun fa_1635.</li>"
            f'<li><a href="{L["faq"]}">FAQ</a> va tanlangan brend sharhini o\'qing.</li>'
            "</ol>"
            f'<p>Eng katta start paketi kerak bo\'lsa — <a href="{L["fairpari"]}">FairPari sharhi</a> (#1, 2026).</p>'
        )
        faq_title = "Bonus turlari bo'yicha tez-tez savollar"
        faq = [
            (
                "Welcome va reload farqi nima?",
                f"Welcome yangi akkaunt uchun (FairPari da 20,2 mln UZS + 150 FS). Reload — mavjud o'yinchiga keyingi depozitlar uchun.",
            ),
            (
                "Kazino va sport welcome bir vaqtda bo'ladimi?",
                "Odatda yo'q. Ro'yxatdan o'tishda bittasini tanlang: kazino 20,2 mln + 150 FS yoki sport ~1,4 mln UZS.",
            ),
            (
                "Qanday wagering normal hisoblanadi?",
                "Kazino ×30–×40, 7–14 kun; sport ekspress ×5. Melbet va 1win ×30 taklif qiladi.",
            ),
            (
                "Aksiyalar qayerda ko'rinadi?",
                f"Faqat operator rasmiy PROMO da. Bizning <a href=\"{L['rating']}\">TOP-20</a> 2026 yangilangan.",
            ),
            (
                "Depozitsiz bonus bormi?",
                f"Doimiy kam. <a href=\"{L['nodep']}\">Depozitsiz bonus</a> — miflar va alternativalar.",
            ),
        ]

    return f"""<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="{L["home"]}">{bc}</a> / <span>{crumb}</span></nav>

<h1>{h1}</h1>
{intro}

<section class="section prose" id="welcome-type">
<h2>{s1_title}</h2>
{s1}
</section>

<section class="section section--alt prose" id="fs-cashback">
<h2>{s2_title}</h2>
{s2}
</section>

<section class="section prose" id="wagering-table">
<h2>{s3_title}</h2>
<div class="table-card"><div class="table-scroll"><table class="data-table data-table--striped">
<thead><tr><th>{"Bonus turi" if lang == "uz" else "Тип бонуса"}</th><th>{"Wagering" if lang == "uz" else "Вейджер"}</th><th>{"Muddat" if lang == "uz" else "Срок"}</th><th>{"Eslatma" if lang == "uz" else "Примечание"}</th></tr></thead>
<tbody>
<tr><td>{"Kazino welcome" if lang == "uz" else "Казино welcome"}</td><td>×30 – ×40</td><td>5–14 {"kun" if lang == "uz" else "дн."}</td><td>{"Slotlar 100%, live cheklangan" if lang == "uz" else "Слоты 100%, live ограничен"}</td></tr>
<tr><td>{"Sport welcome" if lang == "uz" else "Спорт welcome"}</td><td>×5</td><td>30 {"kun" if lang == "uz" else "дн."}</td><td>{"Ekspress, kazinodan alohida" if lang == "uz" else "Экспресс, отдельно от казино"}</td></tr>
<tr><td>Free spins</td><td>×35</td><td>{"FS bilan bir xil" if lang == "uz" else "Как у FS"}</td><td>{"Belgilangan slotlar" if lang == "uz" else "Указанные слоты"}</td></tr>
<tr><td>Cashback</td><td>×3 – ×10</td><td>{"Har aksiyada" if lang == "uz" else "По акции"}</td><td>{"Minimal yechish" if lang == "uz" else "Мин. вывод"}</td></tr>
<tr><td>{"Depozitsiz" if lang == "uz" else "Бездепозит"}</td><td>×40 – ×50</td><td>{"Qisqa" if lang == "uz" else "Короткий"}</td><td><a href="{L["nodep"]}">{"Kam uchraydi" if lang == "uz" else "Редко"}</a></td></tr>
</tbody></table></div></div>
<p>{"FairPari kazino welcome ×35 va 7 kun atrofida — reytingimizdagi eng shaffof shartlardan biri. Sport paketi 1 400 000 UZS gacha, ×5 ekspress." if lang == "uz" else "Казино welcome FairPari — ×35, около 7 дней — один из самых прозрачных в рейтинге. Спорт-пакет до 1 400 000 UZS, ×5 на экспресс."}</p>
</section>

<section class="section section--alt prose" id="uz-market">
<h2>{s4_title}</h2>
{s4}
</section>

<section class="section prose" id="top20-table">
<h2>{s5_title}</h2>
<p>{"Quyidagi jadval casino-bonuses-uz.com reytingidagi barcha 20 operatorni qamrab oladi. Har bir nomga sharh sahifasiga havola berilgan." if lang == "uz" else "Таблица охватывает все 20 операторов рейтинга casino-bonuses-uz.com. Имена ведут на обзоры брендов."}</p>
<div class="table-card"><div class="table-scroll"><table class="data-table data-table--rating">
<thead><tr><th>#</th><th>{"Operator" if lang == "uz" else "Оператор"}</th><th>Welcome</th><th>Wagering</th><th>{"To'lov" if lang == "uz" else "Платежи"}</th></tr></thead>
<tbody>
{_top20_rows(lang)}
</tbody></table></div></div>
</section>

<section class="section section--alt prose" id="how-choose">
<h2>{s6_title}</h2>
{s6}
</section>

<section class="section prose" id="faq-block">
<h2>{faq_title}</h2>
<div class="faq-list">
{_faq_items(faq)}
</div>
</section>

{_hub_extra("kazino-bonuslari", lang, L)}
{_disclaimer(lang)}
{_cta(lang)}"""


def _body_welcome_bonus(lang: str) -> str:
    L = _links(lang)
    if lang == "ru":
        bc, crumb = "Главная", "Сравнение welcome bonus"
        h1 = "Сравнение welcome bonus 2026"
        intro = (
            '<p class="page-intro">Welcome bonus — ключевое предложение для нового игрока в Узбекистане: '
            "пакет в <strong>UZS</strong>, фриспины или спортивный бонус на первые депозиты. "
            f'Ниже — детальное сравнение <a href="{L["rating"]}">TOP-20 операторов</a>, разбор пакета FairPari '
            "(20 200 000 UZS + 150 FS), пошаговая активация, типичные ошибки и ответы в FAQ.</p>"
        )
        s1 = "TOP-20 welcome — полная таблица рейтинга"
        s1p = (
            "<p>Рейтинг casino-bonuses-uz.com строится на размере welcome, вейджере, локальных платежах и отзывах UZ. "
            "FairPari удерживает #1 благодаря четырёхэтапному казино-пакету и поддержке Humo, Payme, Click. "
            "1win и Mostbet конкурируют по мобильному приложению и линии спорта. "
            "Melbet выделяется вейджером ×30. Ниже — все 20 брендов одной таблицей.</p>"
        )
        s2 = "FairPari — четырёхэтапный казино-пакет"
        s2p = (
            f'<p><a href="{L["fairpari"]}">FairPari</a> — эталон рынка UZ: <strong>20 200 000 UZS + 150 FS</strong> '
            "на четыре депозита, вейджер ×35, промокод <strong>fa_1635</strong>. Первый этап — 100% + 30 FS, "
            "далее три дополнительных пополнения с процентом и фриспинами. Спортивная альтернатива — "
            "<strong>1 400 000 UZS</strong> (×5 на экспресс); выбрать можно только один тип при регистрации.</p>"
            "<p>Max bet при отыгрыше — до 130 000 UZS за спин; слоты зачитываются 100%, live — 10–20%. "
            f'Общие типы бонусов: <a href="{L["types"]}">казино-бонусы</a>.</p>'
        )
        s3 = "Как выбрать welcome — 7 критериев"
        s3list = (
            '<ul class="section-list">'
            "<li><strong>Размер в UZS и FS</strong> — с учётом числа депозитов</li>"
            "<li><strong>Вейджер и срок</strong> — ×30–×40, 7–14 дней для казино</li>"
            f'<li><strong>Платежи</strong> — Humo, Payme (<a href="{L["pay"]}">гид UZ</a>)</li>'
            "<li><strong>Мобильное приложение</strong> — APK, PWA, push</li>"
            "<li><strong>Max bet и запрещённые игры</strong> — в PROMO</li>"
            "<li><strong>Прозрачность условий</strong> — без скрытых лимитов</li>"
            f'<li><strong>Независимый обзор</strong> — страница бренда в <a href="{L["rating"]}">рейтинге</a></li>'
            "</ul>"
        )
        s4 = "Активация welcome — пошагово"
        s4p = (
            "<p>Регистрация на официальном сайте оператора занимает 2–5 минут. "
            "casino-bonuses-uz.com не принимает депозиты — только информация.</p>"
            '<ol class="section-list">'
            "<li>Откройте официальный домен (проверьте SSL и адрес).</li>"
            "<li>Выберите валюту <strong>UZS</strong>.</li>"
            "<li>Укажите тип welcome: казино или спорт.</li>"
            "<li>Введите промокод fa_1635 (FairPari) до депозита.</li>"
            "<li>Пополните счёт от минимума (Humo, Payme, Uzcard).</li>"
            "<li>Проверьте зачисление в PROMO-кабинете.</li>"
            "<li>Отыгрывайте в разрешённых играх до истечения срока.</li>"
            "</ol>"
            "<p>После завершения вейджера запросите вывод — потребуется KYC при первом разе.</p>"
        )
        s5 = "Типичные ошибки при welcome"
        s5p = (
            '<ul class="section-list">'
            "<li>Смешение казино и спорт-бонуса в одном аккаунте</li>"
            "<li>Ставка выше max bet при активном бонусе</li>"
            "<li>Игра в live/crash с 0% зачёта</li>"
            "<li>Просрочка вейджера — бонус сгорает</li>"
            "<li>Депозит без промокода</li>"
            "<li>Мультиаккаунт — блокировка и конфискация</li>"
            "</ul>"
            f'<p>Больше ответов — в <a href="{L["faq"]}">FAQ</a> и на странице '
            f'<a href="{L["nodep"]}">бездепозитный бонус</a> (альтернативы).</p>'
        )
        faq_title = "FAQ по welcome bonus"
        faq = [
            ("Какой welcome лучший в UZ в 2026?", f"FairPari — 20 200 000 UZS + 150 FS, #1 в <a href=\"{L['rating']}\">рейтинге TOP-20</a>."),
            ("Сколько депозитов нужно для максимума FairPari?", "Четыре этапа; каждый требует отдельного пополнения по правилам PROMO."),
            ("Можно ли отменить welcome?", "До начала отыгрыша — через поддержку или кабинет; после ставок — нет."),
            ("Работает ли welcome с Payme?", f"Да у TOP-5: FairPari, Mostbet и др. См. <a href=\"{L['pay']}\">платежи</a>."),
            ("Чем 1win отличается от FairPari?", "1win — до 12 млн UZS, ×30, сильное приложение; FairPari — больший пакет и 150 FS."),
        ]
    else:
        bc, crumb = "Bosh sahifa", "Welcome bonus taqqoslash"
        h1 = "Welcome bonus taqqoslash 2026"
        intro = (
            '<p class="page-intro">Welcome bonus — O\'zbekistondagi yangi o\'yinchi uchun asosiy taklif: '
            "<strong>UZS</strong> paket, free spins yoki sport bonusi birinchi depozit(lar)ga. "
            f'Quyida <a href="{L["rating"]}">TOP-20 operatorlar</a> batafsil taqqoslanadi, FairPari paketi '
            "(20 200 000 UZS + 150 FS) tahlil qilinadi, faollashtirish bosqichlari, xatolar va FAQ berilgan.</p>"
        )
        s1 = "TOP-20 welcome — to'liq reyting jadvali"
        s1p = (
            "<p>casino-bonuses-uz.com reytingi welcome hajmi, wagering, mahalliy to'lovlar va UZ fikrlariga asoslanadi. "
            "FairPari #1 — to'rt bosqichli kazino paketi va Humo, Payme, Click. "
            "1win va Mostbet mobil ilova va sport liniyasida raqoblashadi. Melbet ×30 wagering bilan ajralib turadi.</p>"
        )
        s2 = "FairPari — to'rt bosqichli kazino paketi"
        s2p = (
            f'<p><a href="{L["fairpari"]}">FairPari</a> — UZ bozoridagi etalon: <strong>20 200 000 UZS + 150 FS</strong> '
            "to'rtta depozit bosqichida, wagering ×35, promo <strong>fa_1635</strong>. Birinchi bosqich — 100% + 30 FS, "
            "keyingi uchta depozitda qo'shimcha foiz va frispinlar. Sport alternativi — "
            "<strong>1 400 000 UZS</strong> (ekspress ×5); ro'yxatdan o'tishda faqat bittasi tanlanadi.</p>"
            f'<p>Wagering paytida max bet — 130 000 UZS gacha; slotlar 100%, live 10–20%. '
            f'<a href="{L["types"]}">Bonus turlari</a> haqida umumiy ma\'lumot.</p>'
        )
        s3 = "Welcome tanlash — 7 mezon"
        s3list = (
            '<ul class="section-list">'
            "<li><strong>UZS va FS hajmi</strong> — depozitlar sonini hisobga oling</li>"
            "<li><strong>Wagering va muddat</strong> — ×30–×40, 7–14 kun</li>"
            f'<li><strong>To\'lovlar</strong> — Humo, Payme (<a href="{L["pay"]}">qo\'llanma</a>)</li>'
            "<li><strong>Mobil ilova</strong> — APK, PWA</li>"
            "<li><strong>Max bet va taqiqlangan o'yinlar</strong> — PROMO da</li>"
            "<li><strong>Shaffof shartlar</strong> — yashirin limitlarsiz</li>"
            f'<li><strong>Mustaqil sharh</strong> — <a href="{L["rating"]}">reyting</a>dagi brend sahifasi</li>'
            "</ul>"
        )
        s4 = "Welcome faollashtirish — bosqichma-bosqich"
        s4p = (
            "<p>Operator rasmiy saytida ro'yxatdan o'tish 2–5 daqiqa. casino-bonuses-uz.com depozit qabul qilmaydi.</p>"
            '<ol class="section-list">'
            "<li>Rasmiy domenni oching (SSL va manzilni tekshiring).</li>"
            "<li>Valyuta: <strong>UZS</strong>.</li>"
            "<li>Welcome turi: kazino yoki sport.</li>"
            "<li>Promokod fa_1635 (FairPari) depozitdan oldin.</li>"
            "<li>Minimal summadan yuqori depozit (Humo, Payme, Uzcard).</li>"
            "<li>PROMO kabinetida bonusni tekshiring.</li>"
            "<li>Ruxsat etilgan o'yinlarda wageringni tugating.</li>"
            "</ol>"
            "<p>Wagering tugagach yechish — birinchi marta KYC kerak bo'lishi mumkin.</p>"
        )
        s5 = "Welcome olishdagi tipik xatolar"
        s5p = (
            '<ul class="section-list">'
            "<li>Kazino va sport bonusini aralashtirish</li>"
            "<li>Max betdan oshish</li>"
            "<li>Live/crash da 0% hisoblanadigan o'yinlar</li>"
            "<li>Wagering muddatini o'tkazib yuborish</li>"
            "<li>Promokodsiz depozit</li>"
            "<li>Multiakkaunt — blok va musodara</li>"
            "</ul>"
            f'<p>Ko\'proq javob: <a href="{L["faq"]}">FAQ</a>, '
            f'<a href="{L["nodep"]}">depozitsiz bonus</a>.</p>'
        )
        faq_title = "Welcome bonus FAQ"
        faq = [
            ("2026 da eng yaxshi welcome qaysi?", f"FairPari — 20 200 000 UZS + 150 FS, <a href=\"{L['rating']}\">TOP-20</a> da #1."),
            ("FairPari maksimumi uchun nechta depozit?", "To'rtta bosqich; har biri PROMO qoidalariga muvofiq alohida depozit."),
            ("Welcome ni bekor qilish mumkinmi?", "Wagering boshlanmaguncha — qo'llab-quvvatlash orqali; keyin yo'q."),
            ("Payme bilan welcome ishlaydimi?", f"Ha, TOP-5 da: FairPari, Mostbet va boshqalar. <a href=\"{L['pay']}\">To'lovlar</a>."),
            ("1win FairParidan qanday farq qiladi?", "1win — 12 mln gacha, ×30, kuchli ilova; FairPari — kattaroq paket va 150 FS."),
        ]

    calc_title = "Welcome kalkulyatori (taxminiy)" if lang == "uz" else "Калькулятор welcome (оценка)"
    calc = (
        "<p>500 000 UZS depozit + 100% welcome = 1 000 000 UZS balans (shartlarga qarab). "
        "FairPari to'rt bosqichda 20,2 mln + 150 FS — har bosqich alohida. "
        f'<a href="{L["fairpari"]}">FairPari sharhi</a>.</p>'
        if lang == "uz"
        else "<p>Депозит 500 000 UZS + 100% welcome = 1 000 000 UZS на балансе (по правилам). "
        f"FairPari — 20,2 млн + 150 FS в четыре этапа. <a href=\"{L['fairpari']}\">Обзор FairPari</a>.</p>"
    )

    return f"""<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="{L["home"]}">{bc}</a> / <span>{crumb}</span></nav>

<h1>{h1}</h1>
{intro}

<section class="section prose" id="top20-welcome">
<h2>{s1}</h2>
{s1p}
<div class="table-card"><div class="table-scroll"><table class="data-table data-table--rating">
<thead><tr><th>#</th><th>{"Operator" if lang == "uz" else "Оператор"}</th><th>Welcome</th><th>Wagering</th><th>{"To'lov" if lang == "uz" else "Платежи"}</th></tr></thead>
<tbody>
{_top20_rows(lang)}
</tbody></table></div></div>
</section>

<section class="section section--alt prose" id="fairpari-pack">
<h2>{s2}</h2>
{s2p}
</section>

<section class="section prose" id="how-choose">
<h2>{s3}</h2>
{s3list}
</section>

<section class="section section--alt prose" id="activation">
<h2>{s4}</h2>
{s4p}
</section>

<section class="section prose" id="mistakes">
<h2>{s5}</h2>
{s5p}
</section>

<section class="section section--alt prose" id="calculator">
<h2>{calc_title}</h2>
{calc}
</section>

<section class="section prose" id="faq-block">
<h2>{faq_title}</h2>
<div class="faq-list">
{_faq_items(faq)}
</div>
</section>

{_hub_extra("welcome-bonus", lang, L)}
{_disclaimer(lang)}
{_cta(lang)}"""


def _body_depozitsiz_bonus(lang: str) -> str:
    L = _links(lang)
    if lang == "ru":
        bc, crumb = "Главная", "Бездепозитный бонус"
        h1 = "Бездепозитный бонус — рынок Узбекистана"
        intro = (
            '<p class="page-intro">Запросы «бездепозитный бонус», «no deposit» и «бесплатные фриспины без депозита» '
            "часты в Google UZ. Постоянные официальные бездепозитные предложения редки. "
            "Основной путь — <strong>welcome на депозит</strong>. "
            f'Ниже — мифы, TOP-20, <a href="{L["welcome"]}">welcome bonus</a> и FAQ.</p>'
        )
        s1t, s1 = "Правда и маркетинг", (
            f'<p>Операторы <a href="{L["rating"]}">рейтинга TOP-20</a> предлагают welcome. '
            f'<a href="{L["fairpari"]}">FairPari</a> #1: <strong>20 200 000 UZS + 150 FS</strong>, четыре депозита, ×35 — не бездепозит.</p>'
            "<p>Временные PROMO без депозита бывают на официальном сайте. Мы бонусы не выдаём.</p>"
            "<p>Игроки UZ часто ищут «бесплатный старт», но устойчивая модель — депозит от 130 000 UZS, "
            "промокод fa_1635 и отслеживание вейджера в кабинете. Спортивная альтернатива FairPari — 1 400 000 UZS.</p>"
        )
        s2t = "Мифы — таблица"
        s3t, s3 = "Альтернатива: минимальный депозит", (
            "<p>От ~130 000 UZS с <strong>fa_1635</strong> (FairPari) — полный пакет в PROMO. "
            f'<a href="{L["pay"]}">Платежи UZ</a>: Humo, Payme, Click.</p>'
        )
        s4t, s4 = "FS без депозита — реальность", (
            "<p>150 FS FairPari — внутри welcome по этапам, каждый с депозитом. Вейджер ×35. "
            f'Спорт welcome — до <strong>1 400 000 UZS</strong>. <a href="{L["types"]}">Типы бонусов</a>.</p>'
        )
        s5t = "TOP-20: бездепозит vs welcome"
        s6t, s6 = "Безопасность", (
            '<ul class="section-list"><li>Не доверяйте Telegram «no deposit»</li>'
            "<li>Проверяйте SSL и домен</li><li>Не отправляйте паспорт агентам</li>"
            f'<li>Сверяйтесь с <a href="{L["rating"]}">TOP-20</a></li></ul>'
        )
        faq_t = "FAQ: бездепозитный бонус"
        faq = [
            ("Есть ли постоянный бездепозит в UZ?", "Нет. TOP-20 работают через welcome с депозитом."),
            ("Что даёт fa_1635?", "Казино welcome FairPari при депозите."),
            ("150 FS бесплатно?", "Нет — часть пакета 20,2 млн UZS на четыре депозита."),
            (f'Где сравнить welcome?', f'<a href="{L["welcome"]}">Сравнение welcome</a>.'),
            ("Опасны ли соцсети?", "Фишинг и кража данных. Только официальные сайты."),
        ]
        myth_rows = (
            '<tr><td>«19 млн без депозита»</td><td>Welcome требует пополнения</td></tr>'
            '<tr><td>«FS без депозита»</td><td>150 FS в welcome FairPari</td></tr>'
            '<tr><td>«Промо = бездепозит»</td><td>fa_1635 с депозитом</td></tr>'
            '<tr><td>Telegram</td><td>Опасно</td></tr>'
        )
        top20_note = "Все 20 операторов — welcome с депозитом; бездепозит временный."
        full_list = "Полный список — "
    else:
        bc, crumb = "Bosh sahifa", "Depozitsiz bonus"
        h1 = "Depozitsiz bonus — O'zbekiston bozori"
        intro = (
            '<p class="page-intro">«Depozitsiz bonus» va «no deposit» so\'rovlari ko\'p. '
            "Doimiy rasmiy takliflar kam; asosiy yo'l — <strong>welcome depozit bonusi</strong>. "
            f'Miflar, TOP-20, <a href="{L["welcome"]}">welcome</a> va FAQ quyida.</p>'
        )
        s1t, s1 = "Haqiqat va marketing", (
            f'<p><a href="{L["rating"]}">TOP-20</a> operatorlar welcome taklif qiladi. '
            f'<a href="{L["fairpari"]}">FairPari</a> #1: <strong>20 200 000 UZS + 150 FS</strong>, depozitsiz emas.</p>'
            "<p>Vaqtinchak PROMO faqat rasmiy saytda. Biz bonus bermaymiz.</p>"
            "<p>O'yinchilar «bepul start» qidiradi, lekin barqaror model — 130 000 UZS dan depozit, "
            "fa_1635 va kabinetda wagering kuzatuvi. FairPari sport alternativi — 1 400 000 UZS.</p>"
        )
        s2t = "Miflar jadvali"
        s3t, s3 = "Alternativa: minimal depozit", (
            "<p>~130 000 UZS + <strong>fa_1635</strong> (FairPari) — to'liq paket. "
            f'<a href="{L["pay"]}">To\'lovlar</a>: Humo, Payme, Click.</p>'
        )
        s4t, s4 = "Depozitsiz FS haqiqati", (
            "<p>150 FS welcome bosqichlarida, har biri depozit bilan. ×35 wagering. "
            f'Sport — <strong>1 400 000 UZS</strong>. <a href="{L["types"]}">Bonus turlari</a>.</p>'
        )
        s5t = "TOP-20: depozitsiz vs welcome"
        s6t, s6 = "Xavfsizlik", (
            '<ul class="section-list"><li>Telegram no deposit ga ishonmang</li>'
            "<li>SSL va domenni tekshiring</li><li>Pasportni yubormang</li>"
            f'<li><a href="{L["rating"]}">TOP-20</a> bilan solishtiring</li></ul>'
        )
        faq_t = "FAQ: depozitsiz bonus"
        faq = [
            ("Doimiy depozitsiz bormi?", "Yo'q. TOP-20 welcome depozit talab qiladi."),
            ("fa_1635 nima?", "FairPari kazino welcome depozit bilan."),
            ("150 FS bepulmi?", "Yo'q — 20,2 mln paket qismi."),
            ("Welcome qayerda?", f'<a href="{L["welcome"]}">Welcome taqqoslash</a>.'),
            ("Ijtimoiy tarmoq xavflimi?", "Ha — fishing. Faqat rasmiy sayt."),
        ]
        myth_rows = (
            '<tr><td>«19 mln depozitsiz»</td><td>Welcome depozit talab qiladi</td></tr>'
            '<tr><td>«FS depozitsiz»</td><td>150 FS welcome ichida</td></tr>'
            '<tr><td>«Promo = depozitsiz»</td><td>fa_1635 depozit bilan</td></tr>'
            '<tr><td>Telegram</td><td>Xavfli</td></tr>'
        )
        top20_note = "20 operator — depozitli welcome; depozitsiz vaqtinchak."
        full_list = "To'liq ro'yxat — "

    return f"""<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="{L["home"]}">{bc}</a> / <span>{crumb}</span></nav>

<h1>{h1}</h1>
{intro}

<section class="section prose" id="truth"><h2>{s1t}</h2>{s1}</section>

<section class="section section--alt prose" id="myths"><h2>{s2t}</h2>
<div class="table-card"><div class="table-scroll"><table class="data-table data-table--striped">
<thead><tr><th>{"Da'vo" if lang == "uz" else "Утверждение"}</th><th>{"Haqiqat" if lang == "uz" else "Факт"}</th></tr></thead>
<tbody>{myth_rows}</tbody></table></div></div></section>

<section class="section prose" id="alternative"><h2>{s3t}</h2>{s3}</section>
<section class="section section--alt prose" id="fs-nodep"><h2>{s4t}</h2>{s4}</section>

<section class="section prose" id="top20-nodep"><h2>{s5t}</h2><p>{top20_note}</p>
<div class="table-card"><div class="table-scroll"><table class="data-table data-table--rating">
<thead><tr><th>#</th><th>{"Operator" if lang == "uz" else "Оператор"}</th><th>Welcome</th><th>{"Depozitsiz" if lang == "uz" else "Бездепозит"}</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="{L["fairpari"]}">FairPari</a></td><td>20 200 000 UZS + 150 FS</td><td>{"Vaqtinchak" if lang == "uz" else "Временно"}</td></tr>
<tr><td>2</td><td><a href="{_brand_link("1win", lang)}">1win</a></td><td>{"12 mln" if lang == "uz" else "до 12 млн"}</td><td>{"Ba'zan" if lang == "uz" else "Иногда"}</td></tr>
<tr><td>3</td><td><a href="{_brand_link("mostbet", lang)}">Mostbet</a></td><td>8,5 mln + 250 FS</td><td>{"Kam" if lang == "uz" else "Редко"}</td></tr>
</tbody></table></div></div>
<p>{full_list}<a href="{L["rating"]}">TOP-20</a>.</p></section>

<section class="section section--alt prose" id="safety"><h2>{s6t}</h2>{s6}</section>
<section class="section prose" id="faq-block"><h2>{faq_t}</h2><div class="faq-list">{_faq_items(faq)}</div></section>
{_hub_extra("depozitsiz-bonus", lang, L)}
{_disclaimer(lang)}
{_cta(lang)}"""


def _body_tolov_uz(lang: str) -> str:
    L = _links(lang)
    if lang == "ru":
        bc, crumb = "Главная", "Платежи UZ"
        h1 = "Humo, Uzcard, Payme — платежи казино"
        intro = (
            '<p class="page-intro">Для игроков Узбекистана критичны <strong>счёт UZS</strong> и локальные методы: '
            "Humo, Uzcard, Payme, Click, иногда крипто. Депозит быстрый; вывод — после KYC и отыгрыша welcome. "
            f'Ниже — таблицы методов, связь с <a href="{L["welcome"]}">welcome bonus</a>, TOP-20 и FAQ.</p>'
        )
        s1t, s1 = "Humo и Uzcard", (
            "<p>Банковские карты UZ — самый популярный депозит. Комиссия часто 0%. Зачисление за минуты; "
            "вывод на карту 1–24 часа. Первый вывод — <strong>KYC</strong>: паспорт, иногда селфи.</p>"
            "<p>FairPari, 1win, Mostbet, 1xBet, Melbet и большинство TOP-20 принимают Humo/Uzcard.</p>"
        )
        s2t, s2 = "Payme и Click", (
            "<p>Электронные кошельки удобны с телефона. Бонус начисляется после подтверждённого депозита — "
            "сначала промокод <strong>fa_1635</strong> (FairPari), затем пополнение от минимума (~130 000 UZS).</p>"
        )
        s3t = "Таблица платёжных методов"
        s4t, s4 = "Платежи и welcome bonus", (
            f'<p>Лидер <a href="{L["fairpari"]}">FairPari</a>: <strong>20 200 000 UZS + 150 FS</strong> '
            "(казино) или <strong>1 400 000 UZS</strong> (спорт). "
            f'<a href="{L["welcome"]}">Сравнение welcome</a>, <a href="{L["types"]}">типы бонусов</a>.</p>'
        )
        s5t = "KYC и безопасность"
        s5 = (
            "<p>Вывод требует верификации. Используйте только официальный домен оператора. "
            "casino-bonuses-uz.com — агрегатор, не принимает платежи. 18+.</p>"
        )
        s6t = "TOP-20 — поддержка платежей UZ"
        faq_t = "FAQ: платежи"
        faq = [
            ("Работает ли Humo с welcome?", "Да у FairPari, 1win, Mostbet и др. из TOP-20."),
            ("Минимальный депозит?", "Около 130 000 UZS — уточняйте в кассе оператора."),
            ("Сколько ждать вывод?", "1–24 часа на карту после KYC."),
            ("Payme и бонус?", "Да, если метод в PROMO и депозит подтверждён."),
            (f'Где сравнить операторов?', f'<a href="{L["rating"]}">Рейтинг TOP-20</a>.'),
        ]
        pay_rows = (
            '<tr><td>Humo</td><td>Минуты</td><td>1–24 ч</td><td>FairPari, 1win, Mostbet</td></tr>'
            '<tr><td>Uzcard</td><td>Минуты</td><td>1–24 ч</td><td>FairPari, Melbet</td></tr>'
            '<tr><td>Payme</td><td>1–5 мин</td><td>Есть</td><td>FairPari, Mostbet</td></tr>'
            '<tr><td>Click</td><td>1–5 мин</td><td>Есть</td><td>FairPari, Melbet</td></tr>'
            '<tr><td>USDT</td><td>15–60 мин</td><td>Крипто</td><td>1xBet, BC.Game</td></tr>'
        )
        th_m = ("Метод", "Депозит", "Вывод", "Операторы")
    else:
        bc, crumb = "Bosh sahifa", "Kazino to'lovlari UZ"
        h1 = "Humo, Uzcard, Payme — kazino to'lovlari"
        intro = (
            '<p class="page-intro">O\'zbekiston o\'yinchilari uchun <strong>UZS hisob</strong> va Humo, Uzcard, '
            "Payme, Click muhim. Depozit tez; yechish — KYC va wagering tugagach. "
            f'Quyida usullar jadvali, <a href="{L["welcome"]}">welcome</a> bog\'lanishi, TOP-20 va FAQ.</p>'
        )
        s1t, s1 = "Humo va Uzcard", (
            "<p>Mahalliy kartalar — eng mashhur depozit. Komissiya ko'pincha 0%. Bir necha daqiqada tushadi; "
            "kartaga yechish 1–24 soat. Birinchi yechishda <strong>KYC</strong>.</p>"
            "<p>FairPari, 1win, Mostbet, 1xBet, Melbet va TOP-20 ning ko'pi Humo/Uzcard qabul qiladi.</p>"
        )
        s2t, s2 = "Payme va Click", (
            "<p>Mobil hamyonlar qulay. Bonus tasdiqlangan depozitdan keyin — avval <strong>fa_1635</strong>, "
            "keyin ~130 000 UZS dan depozit.</p>"
        )
        s3t = "To'lov usullari jadvali"
        s4t, s4 = "To'lov va welcome bonus", (
            f'<p><a href="{L["fairpari"]}">FairPari</a> #1: <strong>20 200 000 UZS + 150 FS</strong> yoki '
            f'sport <strong>1 400 000 UZS</strong>. <a href="{L["welcome"]}">Welcome</a>, '
            f'<a href="{L["types"]}">bonus turlari</a>.</p>'
        )
        s5t = "KYC va xavfsizlik"
        s5 = (
            "<p>Yechish uchun verifikatsiya. Faqat operator rasmiy domeni. "
            "casino-bonuses-uz.com to'lov qabul qilmaydi. 18+.</p>"
        )
        s6t = "TOP-20 — UZ to'lovlari"
        faq_t = "FAQ: to'lovlar"
        faq = [
            ("Humo welcome bilan ishlaydimi?", "Ha — FairPari, 1win, Mostbet va TOP-20 da."),
            ("Minimal depozit?", "Taxminan 130 000 UZS — kassada tekshiring."),
            ("Yechish qancha vaqt?", "KYC dan keyin kartaga 1–24 soat."),
            ("Payme va bonus?", "Ha, PROMO da usul bo'lsa va depozit tasdiqlansa."),
            (f'Operatorlarni qayerda solishtirish?', f'<a href="{L["rating"]}">TOP-20 reyting</a>.'),
        ]
        pay_rows = (
            '<tr><td>Humo</td><td>Daqiqalar</td><td>1–24 soat</td><td>FairPari, 1win, Mostbet</td></tr>'
            '<tr><td>Uzcard</td><td>Daqiqalar</td><td>1–24 soat</td><td>FairPari, Melbet</td></tr>'
            '<tr><td>Payme</td><td>1–5 daq</td><td>Bor</td><td>FairPari, Mostbet</td></tr>'
            '<tr><td>Click</td><td>1–5 daq</td><td>Bor</td><td>FairPari, Melbet</td></tr>'
            '<tr><td>USDT</td><td>15–60 daq</td><td>Kripto</td><td>1xBet, BC.Game</td></tr>'
        )
        th_m = ("Usul", "Depozit", "Yechish", "Operatorlar")

    return f"""<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="{L["home"]}">{bc}</a> / <span>{crumb}</span></nav>

<h1>{h1}</h1>
{intro}

<section class="section prose" id="humo"><h2>{s1t}</h2>{s1}</section>
<section class="section section--alt prose" id="payme"><h2>{s2t}</h2>{s2}</section>

<section class="section prose" id="pay-table"><h2>{s3t}</h2>
<div class="table-card"><div class="table-scroll"><table class="data-table data-table--striped">
<thead><tr><th>{th_m[0]}</th><th>{th_m[1]}</th><th>{th_m[2]}</th><th>{th_m[3]}</th></tr></thead>
<tbody>{pay_rows}</tbody></table></div></div></section>

<section class="section section--alt prose" id="bonus-pay"><h2>{s4t}</h2>{s4}</section>
<section class="section prose" id="kyc"><h2>{s5t}</h2>{s5}</section>

<section class="section section--alt prose" id="top20-pay"><h2>{s6t}</h2>
<p>{"Barcha 20 brend jadvali — welcome va to'lov ustunlari bilan." if lang == "uz" else "Все 20 брендов — welcome и платежи."}</p>
<div class="table-card"><div class="table-scroll"><table class="data-table data-table--rating">
<thead><tr><th>#</th><th>{"Operator" if lang == "uz" else "Оператор"}</th><th>Welcome</th><th>{"To'lov" if lang == "uz" else "Платежи"}</th></tr></thead>
<tbody>{_top20_rows(lang, linked=True)}</tbody></table></div></div></section>

<section class="section prose" id="faq-block"><h2>{faq_t}</h2><div class="faq-list">{_faq_items(faq)}</div></section>
{_hub_extra("tolov-uz", lang, L)}
{_disclaimer(lang)}
{_cta(lang)}"""


def _body_faq(lang: str) -> str:
    L = _links(lang)
    if lang == "ru":
        bc, crumb = "Главная", "FAQ"
        h1 = "FAQ — бонусы казино UZ"
        intro = (
            '<p class="page-intro">Ответы на частые вопросы об <strong>welcome</strong>, <strong>вейджере</strong>, '
            "<strong>промокоде</strong>, <strong>бездепозите</strong> и <strong>Humo/Payme</strong> для Узбекистана. "
            "Данные рейтинга TOP-20; точные условия — в PROMO оператора.</p>"
        )
        sections = [
            ("welcome-faq", "Что такое welcome bonus?",
             f"Пакет на первые депозиты: UZS, FS или спорт. <a href=\"{L['fairpari']}\">FairPari</a> #1: "
             "<strong>20 200 000 UZS + 150 FS</strong>, ×35. <a href=\"" + L["welcome"] + "\">Сравнение welcome</a>."),
            ("wagering-faq", "Что такое вейджер?",
             "Оборот бонуса перед выводом. Казино ×30–×40, 7–14 дней; спорт ×5 экспресс. Max bet до 130 000 UZS. "
             f"<a href=\"{L['types']}\">Типы бонусов</a>."),
            ("promo-faq", "Где вводить промокод?",
             "При регистрации или в кассе до депозита. FairPari казино: <strong>fa_1635</strong>."),
            ("nodep-faq", "Есть ли бездепозитный бонус?",
             f"Постоянно редко. <a href=\"{L['nodep']}\">Бездепозитный бонус</a> — мифы и альтернативы."),
            ("pay-faq", "Работают ли Humo и Payme?",
             f"Да у TOP-20: FairPari, 1win, Mostbet. <a href=\"{L['pay']}\">Платежи UZ</a>."),
            ("sport-faq", "Казино и спорт welcome вместе?",
             "Нет. FairPari: казино 20,2 млн + 150 FS или спорт 1 400 000 UZS — один выбор."),
            ("why-fp", "Почему FairPari #1?",
             f"Крупнейший welcome, локальные платежи, APK. <a href=\"{L['fairpari']}\">Обзор FairPari</a>."),
            ("portal-faq", "Этот сайт — оператор?",
             "Нет. casino-bonuses-uz.com — независимый рейтинг TOP-20. Депозиты только на сайте оператора."),
        ]
        faq_extra = [
            ("Какой лучший бонус в UZ 2026?", f"FairPari — 20,2 млн + 150 FS. <a href=\"{L['rating']}\">TOP-20</a>."),
            ("Срок отыгрыша welcome?", "Обычно 7–30 дней — в PROMO оператора."),
            ("Нужна ли верификация?", "Да, при первом выводе: паспорт/ID."),
            ("Можно ли отменить бонус?", "До начала отыгрыша — через поддержку."),
            ("Где таблица всех операторов?", f"<a href=\"{L['rating']}\">Рейтинг TOP-20</a> на главной."),
            ("Спортивный welcome FairPari?", "До 1 400 000 UZS, ×5 на экспресс — отдельно от казино 20,2 млн + 150 FS."),
            ("Humo или Payme для бонуса?", f"Оба у TOP-5. Подробнее: <a href=\"{L['pay']}\">платежи UZ</a>."),
            ("Есть ли бездепозит?", f"Редко. <a href=\"{L['nodep']}\">Разбор бездепозита</a> и альтернативы welcome."),
        ]
        faq_title = "Аккордеон — популярные вопросы"
        top20_title = "TOP-20 — краткая справка"
    else:
        bc, crumb = "Bosh sahifa", "FAQ"
        h1 = "Kazino bonuslari FAQ"
        intro = (
            '<p class="page-intro"><strong>Welcome</strong>, <strong>wagering</strong>, <strong>promo kod</strong>, '
            "<strong>depozitsiz bonus</strong> va <strong>Humo/Payme</strong> — O'zbekiston o'yinchilarining savollari. "
            "TOP-20 reyting ma'lumotlari; aniq shartlar operator PROMO da.</p>"
        )
        sections = [
            ("welcome-faq", "Welcome bonus nima?",
             f"Birinchi depozit(lar)ga paket. <a href=\"{L['fairpari']}\">FairPari</a> #1: "
             "<strong>20 200 000 UZS + 150 FS</strong>. <a href=\"" + L["welcome"] + "\">Welcome taqqoslash</a>."),
            ("wagering-faq", "Wagering nima?",
             "Yechishdan oldin bonusni aylantirish. Kazino ×30–×40; sport ×5. Max bet 130 000 UZS. "
             f"<a href=\"{L['types']}\">Bonus turlari</a>."),
            ("promo-faq", "Promo kod qayerda?",
             "Ro'yxatdan o'tish yoki kassa — depozitdan oldin. FairPari: <strong>fa_1635</strong>."),
            ("nodep-faq", "Depozitsiz bonus bormi?",
             f"Doimiy kam. <a href=\"{L['nodep']}\">Depozitsiz bonus</a> sahifasi."),
            ("pay-faq", "Humo va Payme ishlaydimi?",
             f"Ha — TOP-20 da. <a href=\"{L['pay']}\">To'lovlar</a>."),
            ("sport-faq", "Kazino va sport bir vaqtda?",
             "Yo'q. FairPari: kazino 20,2 mln + 150 FS yoki sport 1,4 mln UZS."),
            ("why-fp", "FairPari nima uchun #1?",
             f"Eng katta welcome, mahalliy to'lovlar. <a href=\"{L['fairpari']}\">Sharh</a>."),
            ("portal-faq", "Bu sayt operator emasmi?",
             "To'g'ri — mustaqil TOP-20 reyting. Depozit faqat operator saytida."),
        ]
        faq_extra = [
            ("2026 da eng yaxshi bonus?", f"FairPari — 20,2 mln + 150 FS. <a href=\"{L['rating']}\">TOP-20</a>."),
            ("Welcome muddati?", "Odatda 7–30 kun — PROMO da."),
            ("Verifikatsiya kerakmi?", "Ha, birinchi yechishda pasport/ID."),
            ("Bonusni bekor qilish?", "Wagering boshlanmaguncha — qo'llab-quvvatlash."),
            ("Barcha operatorlar jadvali?", f"<a href=\"{L['rating']}\">TOP-20 reyting</a>."),
            ("FairPari sport welcome?", "1 400 000 UZS gacha, ekspress ×5 — kazino 20,2 mln + 150 FS dan alohida."),
            ("Humo yoki Payme?", f"TOP-5 da ikkalasi ham. <a href=\"{L['pay']}\">To'lovlar</a>."),
            ("Depozitsiz bormi?", f"Kam. <a href=\"{L['nodep']}\">Depozitsiz sharh</a> va welcome alternativasi."),
        ]
        faq_title = "Akkordeon — mashhur savollar"
        top20_title = "TOP-20 — qisqa ma'lumot"

    sec_html = "\n".join(
        f'<section class="section{" section--alt" if i % 2 else ""} prose" id="{sid}">'
        f"<h2>{title}</h2><p>{body}</p></section>"
        for i, (sid, title, body) in enumerate(sections)
    )
    rows_data = TOP20_RU if lang == "ru" else TOP20_UZ
    top20_compact_rows = "".join(
        f'<tr><td>{i}</td><td><a href="{_brand_link(s, lang)}">{escape(n)}</a></td>'
        f"<td>{escape(w)}</td></tr>"
        for i, (s, n, w, _, _) in enumerate(rows_data, 1)
    )
    top20_note = (
        "Batafsil sharhlar va to'lovlar — har bir brend sahifasida."
        if lang == "uz"
        else "Подробные обзоры и платежи — на страницах брендов."
    )

    return f"""<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="{L["home"]}">{bc}</a> / <span>{crumb}</span></nav>

<h1>{h1}</h1>
{intro}

{sec_html}

<section class="section prose" id="faq-accordion">
<h2>{faq_title}</h2>
<div class="faq-list">
{_faq_items(faq_extra)}
</div>
</section>

<section class="section section--alt prose" id="top20-faq">
<h2>{top20_title}</h2>
<div class="table-card"><div class="table-scroll"><table class="data-table data-table--compact">
<thead><tr><th>#</th><th>{"Operator" if lang == "uz" else "Оператор"}</th><th>Welcome</th></tr></thead>
<tbody>
{top20_compact_rows}
</tbody></table></div></div>
<p>{top20_note}</p>
</section>

{_hub_extra("faq", lang, L)}
{_disclaimer(lang)}
{_cta(lang)}"""


if __name__ == "__main__":
    import re
    for slug in SLUGS:
        for lang in ("uz", "ru"):
            html = hub_body(slug, lang)
            text = re.sub(r"<[^>]+>", " ", html)
            words = len(text.split())
            print(f"{slug}/{lang}: {words} words")
