#!/usr/bin/env python3
"""Extra index sections for casino-bonuses-uz.com — ~1400–1600 words (uz/ru)."""
from __future__ import annotations

from html import escape

_TYPE_UZ = {"both": "Kazino + BK", "bk": "Bukmeker", "casino": "Kazino"}
_TYPE_RU = {"both": "Казино + БК", "bk": "БК", "casino": "Казино"}


def _faq_html(items: list[tuple[str, str]], open_first: bool = False) -> str:
    parts = []
    for i, (q, a) in enumerate(items):
        expanded = open_first and i == 0
        cls = "faq-item is-open" if expanded else "faq-item"
        aria = "true" if expanded else "false"
        parts.append(
            f'<article class="{cls}">'
            f'<button type="button" class="faq-item__question" aria-expanded="{aria}">'
            f"<span>{escape(q)}</span>"
            f'<span class="faq-item__icon" aria-hidden="true">+</span></button>'
            f'<div class="faq-item__answer">{escape(a)}</div></article>'
        )
    return "".join(parts)


def _comparison_rows(lang: str, prefix: str) -> str:
    from build_rating_site import BRANDS

    type_map = _TYPE_RU if lang == "ru" else _TYPE_UZ
    rows = []
    for i, b in enumerate(BRANDS, 1):
        welcome = b["welcome_ru"] if lang == "ru" else b["welcome_uz"]
        t = type_map.get(b["type"], b["type"])
        highlight = ' class="is-highlight"' if b["slug"] == "fairpari" else ""
        rows.append(
            f"<tr{highlight}>"
            f"<td>#{i}</td>"
            f'<td><a href="{prefix}{b["slug"]}/">{escape(b["name"])}</a></td>'
            f"<td>{escape(welcome)}</td>"
            f"<td>{escape(b['wagering'])}</td>"
            f"<td>{escape(b['pay'])}</td>"
            f"<td>{escape(t)}</td>"
            f"<td>{b['rating']:.1f}</td>"
            f"</tr>"
        )
    return "\n".join(rows)


def _faq_items(lang: str) -> list[tuple[str, str]]:
    if lang == "ru":
        return [
            (
                "Почему FairPari на первом месте в рейтинге 2026?",
                "FairPari лидирует по совокупности факторов: крупнейший казино welcome в UZ (20,2 млн UZS + 150 FS на четыре депозита), вейджер ×35 при конкурентном рынке, локальные платежи Humo, Payme и Click, мобильное приложение и регулярные PROMO. Мы не ранжируем только по цифре на баннере — учитываем реальную «стоимость» отыгрыша и доступность вывода в UZS.",
            ),
            (
                "Как часто обновляется рейтинг ТОП-20?",
                "Базовая сверка welcome, wagering и платежей — ежемесячно; внепланово при смене условий у топ-5 операторов. Дата актуализации указана в методологии. Перед депозитом всегда проверяйте официальный сайт: суммы и сроки могут меняться быстрее, чем мы успеваем обновить карточку.",
            ),
            (
                "Чем спорт welcome отличается от казино welcome?",
                "У букмекеров (Linebet, Parimatch, Leon) спорт-бонус часто с вейджером ×5–×6 на экспрессы — это отдельный продукт. Казино welcome (FairPari, 1win, Mostbet) требует прокрутки в слотах с коэффициентом ×30–×45. Смешивать пакеты без чтения PROMO нельзя: бонус может аннулироваться.",
            ),
            (
                "Можно ли получить welcome через Humo или Payme?",
                "Да, у большинства операторов из нашего списка первый депозит через Humo, Uzcard, Payme или Click засчитывается для welcome. Исключения — крипто-казино вроде BC.Game. Подробная таблица методов — в разделе «Платежи UZ» и на хабе /ru/tolov-uz/.",
            ),
            (
                "Что такое wagering ×35 на практике?",
                "Если бонус 1 000 000 UZS при ×35, нужен оборот 35 000 000 UZS в разрешённых играх (обычно слоты 100%). Срок — часто 7–14 дней. Max bet при активном бонусе ограничен (типично до 130 000 UZS за спин). Превышение или игра в исключённых разделах обнуляет бонус.",
            ),
            (
                "Есть ли депозитный бонус без вейджера в Узбекистане?",
                "Полностью без отыгрыша welcome встречается редко. Иногда встречаются кешбэк или freebet с мягкими условиями. Основной рынок UZ 2026 — процент на депозит + FS с вейджером. Сравните варианты в /ru/depozitsiz-bonus/ и /ru/welcome-bonus/.",
            ),
            (
                "casino-bonuses-uz.com — это казино или партнёр оператора?",
                "Нет. Мы независимый информационный рейтинг: не принимаем депозиты, не выдаём бонусы и не являемся службой поддержки FairPari или других брендов. Регистрация и платежи — только на официальных сайтах операторов.",
            ),
            (
                "Как выбрать между 1win, 1xBet и FairPari?",
                "FairPari — максимальный welcome и локальные платежи. 1win — сильная мобилка и ×30 wagering при меньшем лимите. 1xBet — широчайшая линия и крипто, но ×40 и сложнее интерфейс. Смотрите полную таблицу сравнения выше и обзоры по ссылкам на каждый бренд.",
            ),
            (
                "Нужна ли верификация для вывода выигрыша с бонусом?",
                "Да. KYC (паспорт/ID, иногда селфи) стандартен при первом выводе. Срок — от часов до трёх дней. Бонусные выигрыши выводятся после полного отыгрыша вейджера на тот же или альтернативный метод из кассы.",
            ),
            (
                "Где читать про ответственную игру?",
                "Раздел /ru/otvetstvennaya-igra/ и блок ниже. Азартные игры 18+. Устанавливайте лимиты депозита и времени, не играйте на заёмные средства. При признаках зависимости обращайтесь к специалистам.",
            ),
        ]
    return [
        (
            "Nima uchun FairPari 2026 reytingida birinchi o'rinda?",
            "FairPari umumiy ball bo'yicha yetakchi: UZ da eng katta kazino welcome (20,2 mln UZS + 150 FS, to'rt depozit), ×35 wagering, Humo, Payme va Click, mobil ilova va muntazam PROMO. Reyting faqat bannerdagi raqamga emas — wagering «narxi» va UZS yechish imkoniyatiga qarab tuziladi.",
        ),
        (
            "TOP-20 reyting qanchalik tez-tez yangilanadi?",
            "Welcome, wagering va to'lovlar — oylik tekshiruv; top-5 operator shartlari o'zgarsa — rejalashtirilmagan yangilanish. Depozitdan oldin rasmiy saytni tekshiring: summalar kartochkadan tezroq o'zgarishi mumkin.",
        ),
        (
            "Sport welcome kazino welcome dan qanday farq qiladi?",
            "Bukmekerlar (Linebet, Parimatch, Leon) sport bonusida ko'pincha ×5–×6 wagering ekspresslarda. Kazino welcome (FairPari, 1win, Mostbet) slotlarda ×30–×45 aylanma talab qiladi. PROMO o'qimasdan aralashtirish bonusni bekor qilishi mumkin.",
        ),
        (
            "Humo yoki Payme orqali welcome olish mumkinmi?",
            "Ha, ro'yxatdagi ko'pchilik operatorlarda birinchi depozit Humo, Uzcard, Payme yoki Click orqali welcome uchun hisoblanadi. Istisno — BC.Game kabi kripto kazino. Batafsil jadval — to'lovlar bo'limi va /tolov-uz/ hubida.",
        ),
        (
            "Amalda ×35 wagering nima degani?",
            "1 000 000 UZS bonus ×35 da — ruxsat etilgan o'yinlarda 35 000 000 UZS aylanma (odatda slotlar 100%). Muddat ko'pincha 7–14 kun. Faol bonusda max bet cheklangan (taxminan 130 000 UZS gacha spin). Oshirish yoki taqiqlangan bo'limlar bonusni yo'q qiladi.",
        ),
        (
            "O'zbekistonda wageringsiz depozit bonusi bormi?",
            "To'liq wageringsiz welcome kam uchraydi. Ba'zan keshbek yoki freebet yumshoq shartlar bilan. UZ bozori 2026 — depozit foizi + FS va wagering. /depozitsiz-bonus/ va /welcome-bonus/ hublarida solishtiring.",
        ),
        (
            "casino-bonuses-uz.com kazino yoki operator hamkormi?",
            "Yo'q. Mustaqil ma'lumot reytingi: depozit qabul qilmaymiz, bonus bermaymiz, FairPari yoki boshqa brend qo'llab-quvvatlashi emas. Ro'yxatdan o'tish va to'lov — faqat rasmiy operator saytlarida.",
        ),
        (
            "1win, 1xBet va FairPari o'rtasida qanday tanlash kerak?",
            "FairPari — maksimal welcome va mahalliy to'lovlar. 1win — kuchli mobil va ×30, lekin limit kichikroq. 1xBet — keng liniya va kripto, lekin ×40 va murakkab interfeys. Yuqoridagi to'liq jadval va har bir brend sharhlarini o'qing.",
        ),
        (
            "Bonus bilan yutuq yechish uchun verifikatsiya kerakmi?",
            "Ha. KYC (pasport/ID, ba'zan selfie) birinchi yechishda standart. Muddat — bir necha soatdan 3 kungacha. Bonus yutuqlari wagering tugagach, kassadagi usulga yechiladi.",
        ),
        (
            "Mas'uliyatli o'yin haqida qayerda o'qish mumkin?",
            "/masuliyatli-oyin/ sahifasi va quyidagi bo'lim. Qimor 18+. Depozit va vaqt limitini o'rnating, qarz pulga o'ynamang. Bog'liqlik belgilari bo'lsa — mutaxassislarga murojaat qiling.",
        ),
    ]


def index_brand_snapshots(lang: str, prefix: str) -> str:
    from build_rating_site import BRANDS

    parts = []
    for i, b in enumerate(BRANDS, 1):
        welcome = b["welcome_ru"] if lang == "ru" else b["welcome_uz"]
        t = b.get("type", "both")
        if lang == "ru":
            type_l = {"both": "казино + БК", "bk": "БК", "casino": "казино"}.get(t, t)
            parts.append(
                f"<p><strong>#{i} {escape(b['name'])}</strong> ({type_l}): welcome <strong>{escape(welcome)}</strong>, "
                f"вейджер {escape(b['wagering'])}, платежи {escape(b['pay'])}. "
                f"В рейтинге {b['rating']:.1f}/5.0 — карточка для игроков UZ, ищущих баланс суммы и отыгрыша. "
                f"<a href=\"{prefix}{b['slug']}/\">Читать обзор #{i}</a> с FAQ, платежами и сравнением с FairPari.</p>"
            )
        else:
            type_l = {"both": "kazino + BK", "bk": "BK", "casino": "kazino"}.get(t, t)
            parts.append(
                f"<p><strong>#{i} {escape(b['name'])}</strong> ({type_l}): welcome <strong>{escape(welcome)}</strong>, "
                f"wagering {escape(b['wagering'])}, to'lov {escape(b['pay'])}. "
                f"Reyting {b['rating']:.1f}/5.0 — UZ o'yinchisi uchun summa va aylanma muvozanati. "
                f"<a href=\"{prefix}{b['slug']}/\">#{i} sharh</a> — FAQ, to'lovlar va FairPari bilan taqqoslash.</p>"
            )
    h2 = "TOP-20 operatorlar — qisqa profil har biri uchun" if lang != "ru" else "TOP-20 операторов — краткий профиль каждого"
    intro = (
        "Quyida reytingdagi har bir brend bir abzatsda: welcome, wagering va to'lovlar. To'liq matn — havolada."
        if lang != "ru"
        else "Ниже каждый бренд рейтинга в одном абзаце: welcome, вейджер и платежи. Полный текст — по ссылке."
    )
    return f"""
<section class="section section--alt" id="brand-snapshots"><div class="container">
  <header class="section__header section__header--compact"><span class="section__eyebrow">TOP-20</span>
  <h2 class="section__title">{h2}</h2></header>
  <p>{intro}</p>
  {"".join(parts)}
</div></section>"""


def index_tz_boost_sections(lang: str, prefix: str) -> str:
    """Extra ~1200–1500 words for index TZ targets (3500 uz / 3000 ru)."""
    if lang == "ru":
        return f"""
<section class="section section--alt" id="tier-guide"><div class="container">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Сегменты</span>
  <h2 class="section__title">Как читать рейтинг: три уровня операторов UZ 2026</h2></header>
  <p>TOP-20 — не плоский список. Мы делим операторов на три сегмента, чтобы вы не сравнивали несравнимое: гибрид «казино + БК», чистый букмекер и крипто-ориентированные площадки. FairPari лидирует в гибридном сегменте по сумме казино welcome и локальным платежам.</p>
  <h3>Уровень A — гибриды с крупным казино welcome</h3>
  <p>FairPari, 1win, Mostbet, Pin-Up, 1xBet, Melbet, Betwinner, Megapari, Spinbetter, 22Bet. У них есть и слоты, и спорт. Казино welcome обычно 5–20 млн UZS + FS, wagering ×30–×45. Спорт welcome — отдельный продукт с ×5–×6. Перед регистрацией выберите направление: смешивание пакетов без чтения PROMO ведёт к аннулированию бонуса.</p>
  <p>Для игрока, который хочет максимум стартового капитала в слотах, FairPari остаётся эталоном: 20,2 млн UZS + 150 FS на четыре депозита, промокод fa_1635, Humo/Payme/Click. 1win конкурирует прошлой ×30 и сильным приложением; Mostbet и Pin-Up — количеством FS (до 250). 1xBet и Betwinner сильны в крипто-депозитах, но казино welcome может быть тяжелее по wagering.</p>
  <h3>Уровень B — букмекеры с фокусом на спорт</h3>
  <p>Linebet, Parimatch, Leon, Fonbet, Marathonbet, Betway. Их welcome чаще привязан к экспрессам: ×5–×6, минимум 3–4 события, коэффициенты от 1.40. Суммы в UZS скромнее, чем у казино-гигантов, но отыгрыш быстрее для тех, кто ставит на футбол APL, UCL и локальные лиги. Не берите спорт welcome, если планируете только слоты — и наоборот.</p>
  <h3>Уровень C — казино без полноценной БК-линии</h3>
  <p>Vulkan Vegas, Joycasino, Fresh Casino, BC.Game. Акцент на слотах, турнирах и FS. BC.Game — крипто; Humo недоступен. Для UZ-игрока с национальной картой сегмент C — запасной вариант, если приоритет — не спорт, а нишевые провайдеры и crash-игры.</p>
  <p>Подробные обзоры каждого бренда — в карточках рейтинга выше и на отдельных URL (/fairpari/, /1win/ и т.д.). Полный гид по welcome FairPari — на <a href="https://fairpari-casino-bonus.com/ru/" rel="noopener">FairPari to'liq bonus qo'llanmasi</a> (EMD-лендинг). Каталог типов бонусов FairPari — <a href="https://fairpari-casino-bonuses.com/ru/bonusy-kazino/" rel="noopener">FairPari promo va FS</a>.</p>
</div></section>

<section class="section" id="wagering-deep"><div class="container">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Wagering</span>
  <h2 class="section__title">Практический разбор вейджера на примерах UZ</h2></header>
  <p>Игроки часто смотрят только на цифру welcome, игнорируя «полную стоимость» отыгрыша. Формула проста: <strong>бонус × wagering = требуемый оборот</strong> в разрешённых играх. При ×35 и бонусе 1 000 000 UZS нужно 35 000 000 UZS оборота в слотах (если слоты считаются 100%).</p>
  <table class="data-table data-table--compact"><thead><tr><th>Оператор</th><th>Welcome (пример)</th><th>Wagering</th><th>Оборот при 1M бонуса</th></tr></thead><tbody>
  <tr><td>FairPari</td><td>20,2M + 150 FS</td><td>×35</td><td>Зависит от зачисленной части</td></tr>
  <tr><td>1win</td><td>500% пакет</td><td>×30–×50</td><td>Считать по этапам</td></tr>
  <tr><td>Linebet</td><td>Спорт welcome</td><td>×5</td><td>5M при 1M бонуса</td></tr>
  <tr><td>BC.Game</td><td>Крипто welcome</td><td>×40+</td><td>Выше риск «застревания»</td></tr>
  </tbody></table>
  <p>Срок wagering — обычно 7–14 дней. Max bet при активном бонусе ограничен (типично до 130 000 UZS за спин). Превышение или игра в исключённых разделах обнуляет бонус. Перед депозитом откройте PROMO и выпишите три числа: wagering, срок, max bet.</p>
  <p>Дополнительные материалы: <a href="{prefix}welcome-bonus/">сравнение welcome</a>, <a href="{prefix}kazino-bonuslari/">типы бонусов</a>, <a href="{prefix}faq/">FAQ по верификации и выводу</a>.</p>
</div></section>

<section class="section section--alt" id="network-links"><div class="container">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Сеть</span>
  <h2 class="section__title">Связанные гиды по бонусам FairPari</h2></header>
  <p>casino-bonuses-uz.com — рейтинг рынка. Для углубления по одному бренду используйте партнёрские информационные сайты сети (не оператор):</p>
  <ul class="section-list">
    <li><a href="https://fairpari-casino-bonus.com/ru/" rel="noopener">FairPari to'liq bonus</a> — короткий EMD-ответ на запрос «fairpari бонус»</li>
    <li><a href="https://fairpari-casino-bonuses.com/ru/bonusy-kazino/" rel="noopener">FairPari promo va FS</a> — энциклопедия подтем (sport, promo, FS)</li>
    <li><a href="{prefix}fairpari/">FairPari в нашем рейтинге #1</a> — сравнение с 19 конкурентами</li>
  </ul>
  <p>Мы не дублируем welcome-тексты с EMD-сайтами: здесь — позиция в TOP-20 и контекст рынка UZ.</p>
</div></section>

<section class="section" id="selection-guide"><div class="container">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Выбор</span>
  <h2 class="section__title">Как выбрать welcome в Узбекистане — расширенный чеклист</h2></header>
  <p>Выбор бонуса — не гонка за максимальной цифрой на баннере. Ниже семь критериев, которые мы применяем при ежемесячной сверке TOP-20. Используйте их перед первым депозитом.</p>
  <ol class="section-list">
    <li><strong>Цель:</strong> слоты, live или спорт? Несовместимые welcome пакеты нельзя смешивать.</li>
    <li><strong>Полная стоимость:</strong> бонус × wagering. 20 млн при ×45 хуже, чем 10 млн при ×30.</li>
    <li><strong>Срок:</strong> 7 дней vs 30 дней — реалистичность отыгрыша при вашем банкролле.</li>
    <li><strong>Max bet:</strong> типично до 130 000 UZS; случайное превышение обнуляет бонус.</li>
    <li><strong>Платёж:</strong> Humo/Payme/Click должны быть в кассе; крипто-only операторы отсекают часть UZ-игроков.</li>
    <li><strong>Мобильность:</strong> APK/PWA и синхронизация wagering между телефоном и десктопом.</li>
    <li><strong>Поддержка и KYC:</strong> первый вывод — паспорт; задержки часто из-за неполной верификации, не «мошенничества».</li>
  </ol>
  <p>FairPari проходит все семь пунктов для гибридного казино-сценария: крупный пакет, ×35, локальные платежи, fa_1635. Для чистого спорта сравните Linebet и Parimatch в таблице рейтинга.</p>
  <p>Дополнительно: <a href="{prefix}welcome-bonus/">сравнение welcome TOP-5</a>, <a href="{prefix}depozitsiz-bonus/">мифы no deposit</a>, <a href="{prefix}tolov-uz/">платежи Humo/Payme</a>. EMD-гид FairPari — <a href="https://fairpari-casino-bonus.com/ru/" rel="noopener">краткое руководство</a>.</p>
</div></section>"""

    return f"""
<section class="section section--alt" id="tier-guide"><div class="container">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Segmentlar</span>
  <h2 class="section__title">Reytingni qanday o'qish: UZ 2026 dagi uch daraja</h2></header>
  <p>TOP-20 tekis ro'yxat emas. Operatorlarni uch segmentga ajratamiz: kazino+BK gibrid, sportga ixtisoslashgan BK va kripto/slot markazlari. FairPari gibrid segmentida kazino welcome hajmi va mahalliy to'lovlar bo'yicha yetakchi.</p>
  <h3>A daraja — katta kazino welcome li gibridlar</h3>
  <p>FairPari, 1win, Mostbet, Pin-Up, 1xBet, Melbet, Betwinner, Megapari, Spinbetter, 22Bet. Slot va sport bor. Kazino welcome odatda 5–20 mln UZS + FS, wagering ×30–×45. Sport welcome alohida — ×5–×6. Ro'yxatdan oldin yo'nalishni tanlang; aralashtirish PROMO buzilishiga olib keladi.</p>
  <p>Slotlarda maksimal start kapitali kerak bo'lsa, FairPari etalon: 20,2 mln UZS + 150 FS, to'rt depozit, fa_1635, Humo/Payme/Click. 1win ×30 va ilova bilan raqobatlashadi; Mostbet va Pin-Up FS soni bilan (250 gacha). 1xBet va Betwinner kriptoda kuchli, lekin kazino welcome og'irroq bo'lishi mumkin.</p>
  <h3>B daraja — sport BK</h3>
  <p>Linebet, Parimatch, Leon, Fonbet, Marathonbet, Betway. Welcome ekspressga bog'langan: ×5–×6, 3–4 hodisa, kf. 1.40+. UZS summalari kichikroq, lekin sport o'yinchisi uchun aylanma tezroq. Faqat slot rejalashtirsangiz sport welcome olmang.</p>
  <h3>C daraja — sport yo'q yoki kripto</h3>
  <p>Vulkan Vegas, Joycasino, Fresh Casino, BC.Game. Slot va turnirlar. BC.Game — kripto, Humo yo'q. Milliy karta bilan C segment zaxira variant.</p>
  <p>Har bir brend sharhi — yuqoridagi kartochkalar va /fairpari/, /1win/ URL larda. FairPari welcome to'liq qo'llanma: <a href="https://fairpari-casino-bonus.com/" rel="noopener">FairPari to'liq bonus</a>. Bonus turlari katalogi: <a href="https://fairpari-casino-bonuses.com/kazino-bonuslari/" rel="noopener">FairPari promo va FS</a>.</p>
</div></section>

<section class="section" id="wagering-deep"><div class="container">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Wagering</span>
  <h2 class="section__title">Wagering amaliy misollar — UZ konteksti</h2></header>
  <p>O'yinchilar ko'pincha faqat welcome raqamiga qarab, «to'liq narxni» e'tiborsiz qoldiradi: <strong>bonus × wagering = kerakli aylanma</strong>. ×35 va 1 000 000 UZS bonusda 35 000 000 UZS slot aylanmasi kerak (100% hisob bo'lsa).</p>
  <table class="data-table data-table--compact"><thead><tr><th>Operator</th><th>Welcome</th><th>Wagering</th><th>1M bonus oborot</th></tr></thead><tbody>
  <tr><td>FairPari</td><td>20,2M + 150 FS</td><td>×35</td><td>Qisman bonusga bog'liq</td></tr>
  <tr><td>1win</td><td>500% paket</td><td>×30–×50</td><td>Bosqichma-bosqich</td></tr>
  <tr><td>Linebet</td><td>Sport</td><td>×5</td><td>5M</td></tr>
  <tr><td>BC.Game</td><td>Kripto</td><td>×40+</td><td>Yuqori risk</td></tr>
  </tbody></table>
  <p>Muddat odatda 7–14 kun. Max bet cheklangan (~130 000 UZS/spin). PROMO dan wagering, muddat va max bet ni yozib oling.</p>
  <p><a href="{prefix}welcome-bonus/">Welcome taqqoslash</a>, <a href="{prefix}kazino-bonuslari/">bonus turlari</a>, <a href="{prefix}faq/">FAQ</a>.</p>
</div></section>

<section class="section section--alt" id="network-links"><div class="container">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Tarmoq</span>
  <h2 class="section__title">FairPari bonus bo'yicha bog'liq qo'llanmalar</h2></header>
  <p>casino-bonuses-uz.com — bozor reytingi. Bitta brend chuqurroq:</p>
  <ul class="section-list">
    <li><a href="https://fairpari-casino-bonus.com/" rel="noopener">FairPari to'liq bonus</a> — EMD qisqa javob</li>
    <li><a href="https://fairpari-casino-bonuses.com/kazino-bonuslari/" rel="noopener">FairPari promo va FS</a> — katalog</li>
    <li><a href="{prefix}fairpari/">Reytingda #1 sharh</a> — 19 raqobatchi bilan</li>
  </ul>
</div></section>

<section class="section" id="selection-guide"><div class="container">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Tanlash</span>
  <h2 class="section__title">Welcome bonusni tanlash — kengaytirilgan cheklist</h2></header>
  <p>Bonus tanlovi — bannerdagi maksimal raqam poygasi emas. TOP-20 ni yangilashda qo'llaydigan yetti mezon:</p>
  <ol class="section-list">
    <li><strong>Maqsad:</strong> slot, live yoki sport? Welcome aralashtirilmaydi.</li>
    <li><strong>To'liq narx:</strong> bonus × wagering. 20 mln ×45 ba'zan 10 mln ×30 dan yomonroq.</li>
    <li><strong>Muddat:</strong> 7 kun vs 30 kun — bankrollingizga mosligi.</li>
    <li><strong>Max bet:</strong> ~130 000 UZS; tasodifiy katta stavka bonusni yo'q qiladi.</li>
    <li><strong>To'lov:</strong> Humo/Payme/Click kassada bo'lishi kerak.</li>
    <li><strong>Mobil:</strong> APK/PWA va wagering sinxronizatsiyasi.</li>
    <li><strong>KYC:</strong> birinchi yechish — pasport; kechikish ko'pincha verifikatsiya sababli.</li>
  </ol>
  <p>FairPari kazino ssenariyida yetti mezonni qoplaydi. Sport uchun Linebet va Parimatch ni solishtiring.</p>
  <p><a href="{prefix}welcome-bonus/">TOP-5 welcome</a>, <a href="{prefix}depozitsiz-bonus/">depozitsiz miflar</a>, <a href="{prefix}tolov-uz/">to'lovlar</a>.</p>
  <p>Reyting metodologiyasi mustaqil: biz operatorlardan to'lov olmaymiz. Har oyda TOP-5 operator shartlarini qayta tekshiramiz; qolgan 15 ta brend — choraklik audit. FairPari odatda birinchi o'rinda qoladi, chunki welcome hajmi va Humo/Payme/Click uchtaligini bir vaqtda qoplaydi — bu UZ o'yinchisi uchun amaliy ustunlik.</p>
  <p>Yuqoridagi TOP-20 jadvali filtrlash va teg orqali toraytiriladi — masalan, faqat kazino yoki faqat BK. Mobil qurilmada gorizontal scroll bilan barcha ustunlarni ko'ring; sticky CTA orqali #1 FairPari bonusiga o'tish mumkin.</p>
</div></section>"""


def index_extra_sections(lang: str) -> str:
    """HTML blocks for index: after #rating, before #criteria."""
    if lang not in ("uz", "ru"):
        raise ValueError('lang must be "uz" or "ru"')

    prefix = "/ru/" if lang == "ru" else "/"
    cmp_rows = _comparison_rows(lang, prefix)
    faq_block = _faq_html(_faq_items(lang), open_first=True)

    if lang == "ru":
        return f"""
<section class="section" id="methodology-detail"><div class="container">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Методология</span>
  <h2 class="section__title">Как мы составляем рейтинг ТОП-20 казино и БК Узбекистана</h2></header>
  <p>Рейтинг на casino-bonuses-uz.com — независимый агрегатор: мы сравниваем welcome, wagering и удобство для игрока из UZ, а не продаём места. Итоговый балл (до 5,0) отражает качество предложения в 2026 году, а не рекламный бюджет бренда.</p>
  <p>Данные сверяются вручную: welcome в UZS, FS, число депозитов в пакете, вейджер, срок, max bet, зачёт игр. Отдельно — Humo, Uzcard, Payme, Click и вывод после KYC.</p>
  <h3>Вес критериев в итоговой оценке</h3>
  <table class="data-table data-table--compact"><thead><tr><th>Критерий</th><th>Вес</th><th>Что проверяем</th></tr></thead><tbody>
  <tr><td>Welcome-бонус (казино)</td><td>~30%</td><td>Сумма в UZS, FS, структура пакета (1–4 депозита)</td></tr>
  <tr><td>Вейджер и срок</td><td>~25%</td><td>×5 спорт vs ×35–×45 казино, дни на отыгрыш, max bet</td></tr>
  <tr><td>Платежи UZ</td><td>~20%</td><td>Humo, Payme, Click, минимальный депозит, вывод в UZS</td></tr>
  <tr><td>Продукт</td><td>~15%</td><td>Слоты, live, линия спорта, приложение APK/PWA</td></tr>
  <tr><td>Прозрачность и лицензия</td><td>~10%</td><td>Правила бонуса, поддержка, международная лицензия</td></tr>
  </tbody></table>
  <p>FairPari №1 — рекордный welcome, ×35 и локальные платежи. ×45 или отсутствие Humo снижает позицию. Букмекеры сравниваются в своей категории (спорт ×5–×6).</p>
  <p>Перед регистрацией проверяйте официальный адрес и правила. Карточки выше — краткая выжимка; здесь — логика ранжирования.</p>
</div></section>

<section class="section section--alt" id="market-2026"><div class="container">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Рынок UZ</span>
  <h2 class="section__title">Обзор welcome-бонусов Узбекистана — 2026</h2></header>
  <p>Рынок UZ 2026 сфокусирован на UZS, Humo, Uzcard, Payme и Click. Бренды конкурируют FS, пакетами на 2–4 депозита и спорт welcome с ×5–×6 на экспрессы.</p>
  <p>TOP-10 казино welcome — 5–20 млн UZS + 100–250 FS, ×30–×40. FairPari — четыре депозита и fa_1635; 1win — мобилка и ×30; Mostbet и Pin-Up — 250 FS. 1xBet и Melbet сильны в спорте и крипто.</p>
  <p>Букмекеры (Linebet, Parimatch, Leon, Fonbet) — ставки с ×5–×6. Казино-only (Vulkan Vegas, Joycasino, Fresh Casino) — FS без полной линии.</p>
  <p>Тренд 2026: игроки чаще сравнивают «полную стоимость» бонуса — произведение суммы на вейджер — а не только заголовок на баннере. Кешбэк, reload и VIP-программы идут вторым эшелоном после welcome. Подробные гайды — на хабах <a href="{prefix}welcome-bonus/">welcome-бонусы</a>, <a href="{prefix}kazino-bonuslari/">типы бонусов</a> и <a href="{prefix}depozitsiz-bonus/">депозитные акции</a>.</p>
</div></section>

<section class="section" id="payments-uz"><div class="container">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Платежи</span>
  <h2 class="section__title">Humo, Payme, Click — депозит и вывод для бонусов в UZ</h2></header>
  <p>Без Humo или Payme welcome часто не активировать. TOP-20 принимает национальные карты; различия — в min депозите и скорости вывода после KYC.</p>
  <table class="data-table data-table--striped"><thead><tr><th>Метод</th><th>Тип</th><th>Депозит</th><th>Вывод</th><th>Комментарий для бонусов</th></tr></thead><tbody>
  <tr><td><strong>Humo</strong></td><td>Карта UZ</td><td>Обычно от 15 000 UZS</td><td>Да, после KYC</td><td>Стандарт для FairPari, Mostbet, 1xBet; welcome засчитывается</td></tr>
  <tr><td><strong>Uzcard</strong></td><td>Карта UZ</td><td>От 15 000 UZS</td><td>Да</td><td>1win, Melbet, Betwinner; проверьте лимиты в кассе</td></tr>
  <tr><td><strong>Payme</strong></td><td>Кошелёк</td><td>Быстро, по QR/приложению</td><td>Зависит от оператора</td><td>FairPari, Mostbet, Pin-Up, Megapari — удобно с телефона</td></tr>
  <tr><td><strong>Click</strong></td><td>Кошелёк</td><td>Мгновенно</td><td>Частично</td><td>FairPari, Melbet, Linebet, Spinbetter; альтернатива Payme</td></tr>
  <tr><td><strong>Крипто (USDT)</strong></td><td>Блокчейн</td><td>Выше min</td><td>На кошелёк</td><td>1xBet, 22Bet, BC.Game; отдельные крипто-welcome</td></tr>
  </tbody></table>
  <p>Порядок: регистрация, промокод, бонус в PROMO, депозит по правилам. Вывод — на тот же канал после KYC. Подробнее — <a href="{prefix}tolov-uz/">платежи Узбекистан</a>. FairPari №1 частично за Humo + Payme + Click.</p>
</div></section>

<section class="section section--alt" id="fairpari-compare"><div class="container">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Сравнение</span>
  <h2 class="section__title">FairPari vs все бренды рейтинга — таблица 2026</h2></header>
  <p>Ниже — сводное сравнение всех 20 операторов из рейтинга. Строка FairPari выделена: это ориентир по welcome и платежам для рынка UZ. Клик по названию ведёт на полный обзор бренда с FAQ и пошаговой инструкцией.</p>
  <div class="table-scroll">
  <table class="data-table data-table--compact"><thead><tr>
    <th>#</th><th>Оператор</th><th>Welcome</th><th>Вейджер</th><th>Платежи</th><th>Тип</th><th>Балл</th>
  </tr></thead><tbody>
{cmp_rows}
  </tbody></table>
  </div>
  <p>FairPari опережает 1win по сумме казино welcome, но 1win может быть интереснее при приоритете ×30 и приложении. 1xBet и Betwinner — сеть с крипто; Mostbet и Pin-Up — баланс FS и UZS. Для чистого спорта смотрите Linebet и Parimatch; для крипто-слотов — BC.Game с оговоркой на отсутствие Humo.</p>
</div></section>

<section class="section" id="faq-index"><div class="container">
  <header class="section__header section__header--compact"><span class="section__eyebrow">FAQ</span>
  <h2 class="section__title">Частые вопросы о рейтинге и бонусах UZ</h2></header>
  <div class="faq-list">{faq_block}</div>
  <p style="margin-top:1.25rem">Больше ответов — в <a href="{prefix}faq/">разделе FAQ</a> и в обзорах каждого оператора из таблицы выше.</p>
</div></section>

<section class="section section--alt" id="hubs"><div class="container">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Гайды</span>
  <h2 class="section__title">Полезные разделы сайта</h2></header>
  <p>Мы собрали тематические хабы для углублённого изучения бонусов и платежей в Узбекистане. Все материалы — на русском для ru-версии сайта, независимы от операторов и носят справочный характер 18+.</p>
  <ul class="section-list">
    <li><a href="{prefix}kazino-bonuslari/">Типы казино-бонусов</a> — welcome, reload, кешбэк, VIP, турниры</li>
    <li><a href="{prefix}welcome-bonus/">Welcome-бонусы 2026</a> — сравнение пакетов и калькулятор отыгрыша</li>
    <li><a href="{prefix}depozitsiz-bonus/">Бонусы без депозита</a> — мифы, реальные акции, FairPari PROMO</li>
    <li><a href="{prefix}tolov-uz/">Платежи Humo, Payme, Click</a> — депозит под welcome и вывод</li>
    <li><a href="{prefix}fairpari/">Обзор FairPari №1</a> — промокод, четыре депозита, wagering</li>
    <li><a href="{prefix}faq/">FAQ</a> — ответы по рейтингу, вейджеру и верификации</li>
  </ul>
</div></section>

<section class="section" id="responsible-detail"><div class="container">
  <header class="section__header section__header--compact"><span class="section__eyebrow">18+</span>
  <h2 class="section__title">Ответственная игра</h2></header>
  <p>Азартные игры допустимы только для совершеннолетних (18+). casino-bonuses-uz.com информирует о бонусах и не поощряет чрезмерные ставки. Устанавливайте лимиты на депозит и время сессии в личном кабинете оператора, не воспринимайте бонус как «бесплатные деньги» — вейджер требует дисциплины и понимания риска.</p>
  <p>Признаки проблемной игры: погоня за проигрышем, заёмные средства на ставки, скрытие активности от близких. В таких случаях используйте самоисключение в кабинете оператора и обратитесь за помощью к специалистам. Подробные рекомендации — на странице <a href="{prefix}otvetstvennaya-igra">ответственная игра</a>. Играйте ответственно.</p>
</div></section>

{index_tz_boost_sections(lang, prefix)}
{index_brand_snapshots(lang, prefix)}"""

    return f"""
<section class="section" id="methodology-detail"><div class="container">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Metodologiya</span>
  <h2 class="section__title">TOP-20 kazino va BK reytingi qanday tuziladi</h2></header>
  <p>casino-bonuses-uz.com dagi reyting — casino.ru uslubidagi mustaqil agregator: welcome paketlar, wagering shartlari va O'zbekiston o'yinchisi uchun qulaylikni solishtiramiz, joy sotmaymiz. 20 ta operator vaznli model bo'yicha baholanadi; yakuniy ball (5,0 gacha) 2026 yil UZ bozori uchun taklif sifatini aks ettiradi.</p>
  <p>PROMO qoidalari, kassa, mobil ilovalar va o'zbek hamda rus tilidagi fikr-mulohazalar tahlil qilinadi. Ma'lumotlar qo'lda tekshiriladi: UZS dagi welcome, frispinlar soni, paketdagi depozitlar, bonus va depozit wagering, muddat, max bet, 100% hisoblanadigan o'yinlar va istisnolar. Alohida Humo, Uzcard, Payme, Click mavjudligi va KYC dan keyin yechish tezligi baholanadi.</p>
  <h3>Baholash mezonlari va ularning vazni</h3>
  <table class="data-table data-table--compact"><thead><tr><th>Mezon</th><th>Vazn</th><th>Nima tekshiramiz</th></tr></thead><tbody>
  <tr><td>Welcome bonus (kazino)</td><td>~30%</td><td>UZS summasi, FS, paket (1–4 depozit)</td></tr>
  <tr><td>Wagering va muddat</td><td>~25%</td><td>×5 sport vs ×35–×45 kazino, kunlar, max bet</td></tr>
  <tr><td>Uz to'lovlari</td><td>~20%</td><td>Humo, Payme, Click, min depozit, UZS yechish</td></tr>
  <tr><td>Mahsulot</td><td>~15%</td><td>Slotlar, live, sport liniyasi, APK/PWA</td></tr>
  <tr><td>Shaffoflik va litsenziya</td><td>~10%</td><td>Bonus qoidalari, qo'llab-quvvatlash, xalqaro litsenziya</td></tr>
  </tbody></table>
  <p>FairPari #1 — rekord kazino welcome (20,2 mln UZS + 150 FS), ×35 wagering va to'liq mahalliy to'lovlar tufayli. Yuqori banner, lekin ×45 wagering yoki Humo yo'qligi pastroq o'rin. Bukmekerlar (Linebet, Parimatch, Fonbet) o'z toifasida: sport welcome ×5–×6 kazino paketlari bilan aralashtirilmaydi.</p>
  <p>Operator saytining doimiy mavjudligini kafolatlamaymiz: domenlar o'zgarishi mumkin. Ro'yxatdan oldin rasmiy manzil va qoidalarni tekshiring. Yuqoridagi kartochkalar qisqacha; bu bo'lim — reyting mantiqini tushuntiradi.</p>
</div></section>

<section class="section section--alt" id="market-2026"><div class="container">
  <header class="section__header section__header--compact"><span class="section__eyebrow">UZ bozori</span>
  <h2 class="section__title">Welcome bonus bozori O'zbekiston — 2026 ko'rinishi</h2></header>
  <p>2026 yilda O'zbekiston o'yinchilari uchun onlayn kazino va bukmeker bozori UZS hisoblar, Humo va Uzcard hamda Payme va Click hamyonlariga siljigan. Brendlar nafaqat birinchi depozit foizi, balki FS soni, 2–4 bosqichli paketlar va past wagering li sport welcome bilan raqobatlashadi.</p>
  <p>TOP-10 da odatiy kazino welcome — 5 dan 20 mln UZS gacha va 100–250 FS, slotlarda ×30–×40 wagering. FairPari to'rt depozitli struktura va fa_1635 promokodi bilan ajralib turadi; 1win mobil ilova va ×30 ga urg'u beradi; Mostbet va Pin-Up 250 FS taklif qiladi. 1xBet va Melbet sport va kriptoda kuchli, lekin kazino welcome og'irroq bo'lishi mumkin.</p>
  <p>Alohida segment — faqat bukmekerlar: Linebet, Parimatch, Leon, Fonbet, Marathonbet, Betway. Ularning welcome stavkalarga yo'naltirilgan: ×5–×6 wagering, kichikroq UZS, lekin slotga nisbatan tezroq aylanma. Kazino-only brendlar (Vulkan Vegas, Joycasino, Fresh Casino) FS va turnirlar bilan raqobatlashadi, to'liq sport liniyasi yo'q.</p>
  <p>2026 trendi: o'yinchilar bonusning «to'liq narxini» — summa × wagering — hisoblashadi. Keshbek, reload va VIP welcome dan keyin ikkinchi qatlam. Batafsil: <a href="{prefix}welcome-bonus/">welcome bonuslar</a>, <a href="{prefix}kazino-bonuslari/">bonus turlari</a>, <a href="{prefix}depozitsiz-bonus/">depozitsiz aksiyalar</a>.</p>
</div></section>

<section class="section" id="payments-uz"><div class="container">
  <header class="section__header section__header--compact"><span class="section__eyebrow">To'lovlar</span>
  <h2 class="section__title">Humo, Payme, Click — UZ da bonus uchun depozit va yechish</h2></header>
  <p>O'zbekiston o'yinchisi uchun to'lov usuli ko'pincha banner foizidan muhimroq: Humo yoki Payme bo'lmasa welcome faollashmaydi. TOP-20 dagi operatorlarning ko'pchiligi milliy kartalarni qabul qiladi; farq — minimal depozit, komissiya va KYC dan keyin yechish tezligida.</p>
  <table class="data-table data-table--striped"><thead><tr><th>Usul</th><th>Turi</th><th>Depozit</th><th>Yechish</th><th>Bonus uchun izoh</th></tr></thead><tbody>
  <tr><td><strong>Humo</strong></td><td>UZ karta</td><td>Odatda 15 000 UZS dan</td><td>Ha, KYC dan keyin</td><td>FairPari, Mostbet, 1xBet uchun standart; welcome hisoblanadi</td></tr>
  <tr><td><strong>Uzcard</strong></td><td>UZ karta</td><td>15 000 UZS dan</td><td>Ha</td><td>1win, Melbet, Betwinner; kassada limitlarni tekshiring</td></tr>
  <tr><td><strong>Payme</strong></td><td>Hamyon</td><td>Tez, QR/ilova</td><td>Operatorga qarab</td><td>FairPari, Mostbet, Pin-Up, Megapari — telefondan qulay</td></tr>
  <tr><td><strong>Click</strong></td><td>Hamyon</td><td>Darhol</td><td>Qisman</td><td>FairPari, Melbet, Linebet, Spinbetter; Payme alternativasi</td></tr>
  <tr><td><strong>Kripto (USDT)</strong></td><td>Blokcheyn</td><td>Yuqori min</td><td>Hamyonga</td><td>1xBet, 22Bet, BC.Game; alohida kripto welcome</td></tr>
  </tbody></table>
  <p>Welcome uchun tavsiya: rasmiy saytda ro'yxatdan o'ting, promokod kiriting (agar bor bo'lsa), PROMO da bonusni tanlang, keyin qoidalarda ko'rsatilgan usulda birinchi depozit. Yechish odatda hujjatlar tekshirilgach o'sha kanalga qaytadi. Depozit va yechish usuli mos kelmasligi — kechikishning tez-tez sababi.</p>
  <p>Limitlar, komissiyalar va bonus bog'lanishi — <a href="{prefix}tolov-uz/">to'lovlar O'zbekiston</a> sahifasida. FairPari reytingda #1 qisman Humo + Payme + Click uchtaligini majburiy kriptosiz taklif qilishi sababli.</p>
</div></section>

<section class="section section--alt" id="fairpari-compare"><div class="container">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Taqqoslash</span>
  <h2 class="section__title">FairPari vs barcha reyting brendlari — 2026 jadvali</h2></header>
  <p>Quyida reytingdagi 20 ta operatorning yig'indisi. FairPari qatori ajratilgan — UZ bozori uchun welcome va to'lovlar bo'yicha yo'riqnoma. Nom ustiga bosish to'liq sharh va FAQ ga olib boradi.</p>
  <div class="table-scroll">
  <table class="data-table data-table--compact"><thead><tr>
    <th>#</th><th>Operator</th><th>Welcome</th><th>Wagering</th><th>To'lov</th><th>Turi</th><th>Ball</th>
  </tr></thead><tbody>
{cmp_rows}
  </tbody></table>
  </div>
  <p>FairPari 1win dan kazino welcome summasida oldinda; 1win ×30 va ilova ustuvor bo'lsa qiziqarli. 1xBet va Betwinner — kripto tarmoq; Mostbet va Pin-Up — FS va UZS muvozanati. Toza sport uchun Linebet va Parimatch; kripto slotlar uchun BC.Game (Humo yo'q).</p>
</div></section>

<section class="section" id="faq-index"><div class="container">
  <header class="section__header section__header--compact"><span class="section__eyebrow">FAQ</span>
  <h2 class="section__title">Reyting va UZ bonuslari bo'yicha tez-tez savollar</h2></header>
  <div class="faq-list">{faq_block}</div>
  <p style="margin-top:1.25rem">Ko'proq javoblar — <a href="{prefix}faq/">FAQ bo'limida</a> va yuqoridagi jadvaldagi har bir operator sharhida.</p>
</div></section>

<section class="section section--alt" id="hubs"><div class="container">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Qo'llanmalar</span>
  <h2 class="section__title">Foydali hub sahifalar</h2></header>
  <p>Bonuslar va to'lovlar bo'yicha chuqurroq o'rganish uchun mavzuli hublar to'plangan. Barcha materiallar mustaqil, operatorlardan alohida va 18+ ma'lumot xarakterida.</p>
  <ul class="section-list">
    <li><a href="{prefix}kazino-bonuslari/">Kazino bonus turlari</a> — welcome, reload, keshbek, VIP, turnirlar</li>
    <li><a href="{prefix}welcome-bonus/">Welcome bonuslar 2026</a> — paketlar taqqoslash va wagering</li>
    <li><a href="{prefix}depozitsiz-bonus/">Depozitsiz bonuslar</a> — miflar, haqiqiy aksiyalar, FairPari PROMO</li>
    <li><a href="{prefix}tolov-uz/">Humo, Payme, Click to'lovlari</a> — welcome depoziti va yechish</li>
    <li><a href="{prefix}fairpari/">FairPari #1 sharhi</a> — promokod, to'rt depozit, wagering</li>
    <li><a href="{prefix}faq/">FAQ</a> — reyting, wagering va verifikatsiya</li>
  </ul>
</div></section>

<section class="section" id="responsible-detail"><div class="container">
  <header class="section__header section__header--compact"><span class="section__eyebrow">18+</span>
  <h2 class="section__title">Mas'uliyatli o'yin</h2></header>
  <p>Qimor faqat voyaga yetganlar uchun (18+). casino-bonuses-uz.com bonuslar haqida ma'lumot beradi va haddan tashqari stavkalarni rag'batlantirmaydi. Operator kabinetida depozit va sessiya vaqti limitini o'rnating; bonusni «bepul pul» deb qabul qilmang — wagering intizom va xavfni tushunishni talab qiladi.</p>
  <p>Muammoli o'yin belgilari: yo'qotishni quvish, qarz pulga stavka, yaqinlardan yashirish. Bunday hollarda operator kabinetida o'z-o'zini cheklashdan foydalaning va mutaxassislarga murojaat qiling. Batafsil — <a href="{prefix}masuliyatli-oyin">mas'uliyatli o'yin</a> sahifasida. Mas'uliyat bilan o'ynang.</p>
</div></section>

{index_tz_boost_sections(lang, prefix)}
{index_brand_snapshots(lang, prefix)}"""


if __name__ == "__main__":
    import re
    import sys

    lang = sys.argv[1] if len(sys.argv) > 1 else "uz"
    html = index_extra_sections(lang)
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text).strip()
    print(f"lang={lang} words≈{len(text.split())} chars={len(html)}")
