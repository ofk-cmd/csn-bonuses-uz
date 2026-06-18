#!/usr/bin/env python3
"""Extra sections for brand reviews — target 2000+ words total with base qttk body."""
from html import escape

COMPETITORS = {
    "fairpari": ("1win", "Mostbet"),
    "1win": ("FairPari", "Mostbet"),
    "1xbet": ("FairPari", "Betwinner"),
    "mostbet": ("FairPari", "1win"),
    "melbet": ("FairPari", "Mostbet"),
    "pin-up": ("FairPari", "Mostbet"),
    "linebet": ("Fonbet", "Leon"),
    "betwinner": ("1xBet", "Megapari"),
    "megapari": ("FairPari", "22Bet"),
    "22bet": ("Megapari", "Melbet"),
    "parimatch": ("Leon", "Fonbet"),
    "leon": ("Parimatch", "Linebet"),
    "fonbet": ("Parimatch", "Marathonbet"),
    "marathonbet": ("Fonbet", "Betway"),
    "betway": ("Marathonbet", "Leon"),
    "spinbetter": ("Vulkan Vegas", "Joycasino"),
    "vulkan-vegas": ("Joycasino", "Spinbetter"),
    "joycasino": ("Vulkan Vegas", "Fresh Casino"),
    "fresh-casino": ("Joycasino", "Spinbetter"),
    "bc-game": ("Vulkan Vegas", "1xBet"),
}


def _faq_extended(b, rank, lang):
    name = b["name"]
    welcome = b["welcome_ru"] if lang == "ru" else b["welcome_uz"]
    slug = b["slug"]
    c1, c2 = COMPETITORS.get(slug, ("FairPari", "1win"))
    if lang == "ru":
        return [
            (f"Сколько времени на отыгрыш welcome в {name}?", f"Обычно 7–30 дней с момента активации. Точный срок — в PROMO на сайте оператора. Вейджер {b['wagering']}."),
            (f"Можно ли вывести бонус {name} без депозита?", f"Нет — welcome начисляется после первого депозита. Запросы «без депозита» — отдельные акции, если есть."),
            (f"{name} или FairPari — что выбрать?", f"FairPari #1 в рейтинге: 20,2 млн UZS + 150 FS. {name} — #{rank}, welcome {welcome}. Сравните таблицу ниже."),
            (f"Какой промокод у {name}?", "У FairPari в UZ часто fa_1635 для казино-пакета. У других операторов — поле при регистрации или в PROMO."),
            (f"Работает ли {name} с Humo и Payme?", f"По нашим данным: {b['pay']}. Проверьте кассу после регистрации — список методов меняется."),
            (f"Есть ли лимит ставки при отыгрыше?", "Да, max bet при активном бонусе — типично 50 000–130 000 UZS. Превышение может аннулировать бонус."),
            (f"Как связаться с поддержкой {name}?", "Live-чат и email на официальном сайте. casino-bonuses-uz.com не является службой поддержки оператора."),
            (f"Нужна ли верификация для вывода?", "Да, KYC при первом выводе: паспорт/ID, иногда селфи. Срок — от нескольких часов до 3 дней."),
            (f"Совместим ли спорт-бонус с казино welcome?", "Обычно нет — выбирают один тип при регистрации. У FairPari спорт и казино — разные пакеты."),
            (f"Как отменить бонус в {name}?", "В кабинете или через поддержку до начала отыгрыша. После ставок с бонусным балансом отмена невозможна."),
            (f"Сравнение {name} с {c1} и {c2}", f"См. раздел «Сравнение» на этой странице и обзоры /{c1.lower().replace(' ', '-')}/ и других брендов в рейтинге."),
            (f"Актуален ли обзор {name} в 2026?", f"Дата обновления рейтинга — 2026. Суммы welcome сверяйте на официальном сайте перед депозитом."),
        ]
    return [
        (f"{name} da welcome wagering uchun qancha vaqt bor?", f"Odatda faollashtirishdan keyin 7–30 kun. Aniq muddat — operator PROMO da. Wagering {b['wagering']}."),
        (f"{name} bonusini depozitsiz yechish mumkinmi?", "Yo'q — welcome birinchi depozitdan keyin. «Depozitsiz» alohida vaqtinchak aksiyalar bo'lishi mumkin."),
        (f"{name} yoki FairPari — qaysi biri yaxshiroq?", f"FairPari #1: 20,2 mln UZS + 150 FS. {name} — #{rank}, welcome {welcome}. Quyidagi jadvalni solishtiring."),
        (f"{name} promokodi bormi?", "FairPari UZ da ko'pincha fa_1635 (kazino). Boshqa operatorlarda ro'yxatdan o'tishda yoki PROMO da."),
        (f"{name} Humo va Payme qabul qiladimi?", f"Ma'lumotimiz: {b['pay']}. Ro'yxatdan keyin kassada tekshiring."),
        (f"Wagering paytida max bet limiti bormi?", "Ha, odatda 50 000–130 000 UZS. Oshirish bonusni bekor qilishi mumkin."),
        (f"{name} qo'llab-quvvatlash qanday?", "Rasmiy saytda live-chat va email. casino-bonuses-uz.com operator emas."),
        (f"Yechish uchun verifikatsiya kerakmi?", "Ha, birinchi yechishda KYC: pasport/ID. Muddat — bir necha soatdan 3 kungacha."),
        (f"Sport va kazino welcome bir vaqtda bo'ladimi?", "Odatda yo'q — bittasini tanlaysiz. FairPari da sport va kazino alohida paketlar."),
        (f"{name} bonusini qanday bekor qilish mumkin?", "Kabinet yoki qo'llab-quvvatlash orqali wagering boshlanmaguncha. Keyin bekor qilib bo'lmaydi."),
        (f"{name} vs {c1} va {c2}", f"«Taqqoslash» bo'limi va /{c1.lower().replace(' ', '-')}/ kabi boshqa sharhlarni o'qing."),
        (f"{name} sharhi 2026 da dolzarbmi?", "Reyting 2026 yangilangan. Depozitdan oldin rasmiy saytda summalarni tekshiring."),
    ]


def extra_sections(b: dict, rank: int, lang: str) -> str:
    """~1500 words of extra HTML sections (uz/ru)."""
    name = b["name"]
    slug = b["slug"]
    welcome = b["welcome_ru"] if lang == "ru" else b["welcome_uz"]
    t = b["type"]
    c1, c2 = COMPETITORS.get(slug, ("FairPari", "1win"))
    prefix = "/ru/" if lang == "ru" else "/"
    fp_link = f'{prefix}fairpari/'

    if lang == "ru":
        wag_block = f"""
<section class="section" id="wagering-guide">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Вейджер</span>
  <h2 class="section__title">Как отыграть welcome {name} — пошагово</h2></header>
  <p>Вейджер <strong>{b['wagering']}</strong> означает: сумму бонуса (и иногда депозита) нужно прокрутить указанное число раз в разрешённых играх. Пример: бонус 1 000 000 UZS при ×35 — оборот 35 000 000 UZS в слотах со 100% зачётом. Срок обычно 7–14 дней; просрочка обнуляет бонус.</p>
  <p>Перед первой ставкой откройте PROMO: там max bet (часто до 130 000 UZS за спин), список слотов с полным зачётом и исключения (live, настольные игры). Live-казино часто даёт 10–20% к вейджеру — отыгрыш замедляется.</p>
  <h3>Типичные ошибки при отыгрыше</h3>
  <ul class="section-list">
    <li>Ставка выше max bet при активном бонусе</li>
    <li>Игра в разделах с 0% зачёта (некоторые crash/live)</li>
    <li>Запрос вывода до завершения вейджера — бонус сгорает</li>
    <li>Смешение спорт-бонуса и казино welcome в одном аккаунте без правил</li>
    <li>Игнорирование срока — остаток бонуса аннулируется автоматически</li>
  </ul>
  <p>Для сравнения: <a href="{fp_link}">FairPari</a> — вейджер ×35 на 20,2 млн UZS + 150 FS, четыре депозита. Если welcome {name} меньше, но вейджер ниже (например ×30 у Melbet), итоговая «стоимость» отыгрыша может быть сопоставимой — считайте оборот, а не только цифру на баннере.</p>
</section>"""

        reg_block = f"""
<section class="section section--alt" id="registration-detail">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Регистрация</span>
  <h2 class="section__title">Детальная инструкция: аккаунт {name} в UZ</h2></header>
  <p>Регистрация на официальном сайте оператора занимает 2–5 минут. casino-bonuses-uz.com — независимый рейтинг: мы не принимаем депозиты и не выдаём бонусы. Все действия — только на сайте {name}.</p>
  <ol class="section-list">
    <li>Откройте официальный домен (избегайте фишинга — проверяйте SSL и адрес).</li>
    <li>Нажмите «Регистрация» / «Sign up» — выберите телефон, email или соцсеть, если доступно.</li>
    <li>Валюта счёта: <strong>UZS</strong> — так проще с Humo, Uzcard, Payme без конвертации.</li>
    <li>Если есть поле промокода — введите до первого депозита (для FairPari в кластере UZ часто fa_1635).</li>
    <li>Выберите тип welcome: казино или спорт — обычно нельзя сменить после активации.</li>
    <li>Подтвердите SMS/email, войдите в кабинет, откройте «Касса» / «Deposit».</li>
    <li>Первый депозит от минимума ({b['pay']}) — бонус зачислится по правилам PROMO.</li>
  </ol>
  <p>Один человек — один аккаунт. Мультиаккаунты ведут к блокировке и конфискации бонуса. Возраст 18+.</p>
</section>"""

        pay_block = f"""
<section class="section" id="payments-detail">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Платежи UZ</span>
  <h2 class="section__title">Депозит и вывод в {name} для Узбекистана</h2></header>
  <p>Локальные методы — основа рынка UZ: <strong>Humo</strong>, <strong>Uzcard</strong>, электронные <strong>Payme</strong> и <strong>Click</strong>. {name} в нашем обзоре принимает: {escape(b['pay'])}. Криптовалюта (USDT, BTC) доступна не у всех — у BC.Game и части БК это основной канал.</p>
  <table class="data-table data-table--striped"><thead><tr><th>Метод</th><th>Депозит</th><th>Вывод</th><th>Комментарий</th></tr></thead><tbody>
  <tr><td>Humo</td><td>Минуты</td><td>1–24 ч</td><td>Популярен в UZ, часто без комиссии со стороны БК</td></tr>
  <tr><td>Uzcard</td><td>Минуты</td><td>1–24 ч</td><td>Аналог Humo по скорости</td></tr>
  <tr><td>Payme / Click</td><td>Мгновенно</td><td>Зависит от оператора</td><td>Удобно с телефона</td></tr>
  <tr><td>Крипто</td><td>15–60 мин</td><td>До 24 ч</td><td>Курс и минимум выше</td></tr>
  </tbody></table>
  <p>Первый вывод почти всегда требует <strong>KYC</strong>: фото документа, иногда селфи. Подготовьте паспорт заранее — это ускорит выплату welcome-выигрыша. Лимиты дневные/недельные смотрите в кабинете.</p>
</section>"""

        cmp_block = f"""
<section class="section section--alt" id="comparison">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Сравнение</span>
  <h2 class="section__title">{name} vs FairPari, {c1} и {c2}</h2></header>
  <p>Позиция в рейтинге casino-bonuses-uz.com: <strong>#{rank}</strong>. Лидер рынка UZ по welcome — <a href="{fp_link}">FairPari</a> (20 200 000 UZS + 150 FS, вейджер ×35). Ниже — ориентир для выбора между {name} и ближайшими конкурентами.</p>
  <table class="data-table data-table--compact"><thead><tr><th>Оператор</th><th>Welcome (обзор)</th><th>Вейджер</th><th>Платежи</th></tr></thead><tbody>
  <tr><td>FairPari #1</td><td>20,2 млн UZS + 150 FS</td><td>×35</td><td>Humo, Payme, Click</td></tr>
  <tr><td>{name}</td><td>{escape(welcome)}</td><td>{b['wagering']}</td><td>{escape(b['pay'])}</td></tr>
  <tr><td>{c1}</td><td>См. <a href="{prefix}{c1.lower().replace(' ', '-').replace('.', '')}/">обзор</a></td><td>—</td><td>—</td></tr>
  </tbody></table>
  <p>Если приоритет — максимальный стартовый пакет в UZS, FairPari остаётся эталоном. {name} может выигрывать по вейджеру, мобильному приложению или линии спорта — смотрите плюсы в начале страницы.</p>
</section>"""

        casino_extra = ""
        if t in ("both", "casino"):
            casino_extra = f"""
<section class="section" id="slots-detail">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Казино</span>
  <h2 class="section__title">Слоты и live в {name} — что учитывать с бонусом</h2></header>
  <p>Каталог казино-раздела {name} включает слоты, live-столы и crash-игры. При welcome обычно 100% зачёта идут в видеослоты: Pragmatic Play, Amatic, Endorphina и др. Live-рулетка и блэкджек — с пониженным процентом или исключены из отыгрыша.</p>
  <p>Популярные у игроков UZ названия (наличие зависит от провайдеров оператора): Gates of Olympus, Sweet Bonanza, Aviator (crash), Crazy Time (live). Демо-режим помогает оценить волатильность до депозита с бонусом.</p>
  <p>Фриспины из welcome часто привязаны к конкретным слотам — список в PROMO. Выигрыш с FS тоже подлежит вейджеру {b['wagering']}.</p>
</section>"""

        sport_extra = ""
        if t in ("both", "bk"):
            sport_extra = f"""
<section class="section section--alt" id="sport-detail">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Спорт</span>
  <h2 class="section__title">Ставки на спорт {name} — линия и бонусы</h2></header>
  <p>Спортивный раздел: прематч и live, экспрессы и ординары. Welcome для спорта обычно с вейджером ×5 на экспрессах из 3+ событий с минимальным коэффициентом — условия уточняйте в PROMO. Казино welcome и спорт welcome, как правило, не комбинируются.</p>
  <p>Для UZ актуальны футбол (ЛЧ, АПЛ), баскетбол (NBA), теннис, иногда киберспорт. Мобильные ставки — через приложение или мобильную версию сайта.</p>
</section>"""

        method_block = """
<section class="section" id="methodology">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Методология</span>
  <h2 class="section__title">Как мы оцениваем бонусы в рейтинге</h2></header>
  <p>casino-bonuses-uz.com — независимый агрегатор. Мы не оператор, не принимаем ставки и депозиты. Оценка #{rank} для {name} строится на: размере welcome в UZS, вейджере, локальных платежах (Humo, Payme), мобильном доступе, отзывах игроков UZ и прозрачности правил PROMO.</p>
  <p>Данные обновляются в 2026 году; перед депозитом сверяйте цифры на официальном сайте. 18+. Играйте ответственно — лимиты и самоисключение в кабинете оператора.</p>
  <p>Мы сравниваем не только заголовок на баннере, но и полную «стоимость» бонуса: произведение суммы на вейджер, срок отыгрыша, max bet и список игр с полным зачётом. Оператор с меньшим welcome, но ×30 и длинным сроком иногда выгоднее, чем крупный пакет с ×45 и неделей на оборот.</p>
  <p>Для игроков из Ташкента, Самарканда, Бухары и других городов UZ критичны Humo/Uzcard без конвертации и вывод в UZS без скрытых комиссий. Если {name} принимает {pay}, это плюс в нашей таблице — но проверяйте кассу после регистрации.</p>
</section>""".replace("{name}", name).replace("{rank}", str(rank)).replace("{pay}", escape(b['pay']))

        tags_str = ", ".join(b.get("tags_ru", b.get("tags_uz", [])))
        deep_block = f"""
<section class="section section--alt" id="mobile-app">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Мобильный доступ</span>
  <h2 class="section__title">Приложение и мобильная версия {name}</h2></header>
  <p>Большинство игроков UZ заходят с телефона: Android APK, iOS через PWA или мобильная версия сайта. {name} в нашем обзоре поддерживает ставки и казино с смартфона — уточните в разделе «Приложение» на официальном сайте. Скачивайте APK только с домена оператора, не с сторонних форумов: фишинг и поддельные клиенты — частая проблема в регионе.</p>
  <p>После установки войдите в тот же аккаунт, что и на десктопе: welcome и wagering синхронизируются. Push-уведомления о новых PROMO удобны, но не отключайте лимиты депозита в настройках ответственной игры. Если приложение недоступно в магазине, PWA (ярлык на главный экран) — безопасная альтернатива без установки из неизвестного источника.</p>
  <p>Сравнение: <a href="{fp_link}">FairPari</a> активно продвигает APK и PWA для UZ — это один из факторов лидерства в рейтинге. У {name} проверьте стабильность live-ставок и слотов в мобильном клиенте перед крупным депозитом с welcome.</p>
</section>

<section class="section" id="vip-reload">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Акции</span>
  <h2 class="section__title">Reload, кешбэк и VIP в {name}</h2></header>
  <p>Welcome — только старт. Дальше операторы удерживают игроков reload-бонусами (процент на 2–5-й депозит), еженедельным кешбэком от проигрыша, турнирами слотов и VIP-уровнями с персональным менеджером. У {name} условия смотрите в PROMO после отыгрыша welcome — не активируйте второй бонус, пока не закрыт вейджер первого.</p>
  <p>Кешбэк обычно с мягким вейджером ×3–×10, но начисляется на чистый минус за период. VIP-программы дают ускоренный вывод и повышенные лимиты — но требуют оборота. Для casual-игрока UZ чаще важнее прозрачный welcome и Humo, чем многоуровневый VIP.</p>
  <p>Турниры: призовой фонд в UZS или FS, таблица лидеров по сумме ставок. Участие добровольное — читайте правила, чтобы не превысить бюджет ради места в топе.</p>
</section>

<section class="section section--alt" id="withdrawal-guide">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Вывод</span>
  <h2 class="section__title">Как вывести выигрыш после welcome в {name}</h2></header>
  <p>После полного отыгрыша вейджера {b['wagering']} бонусный баланс переходит в реальные средства — если не нарушены правила PROMO. Запрос вывода: кабинет → «Вывод» → выбор метода ({escape(b['pay'])}). Первый раз почти всегда KYC: загрузите чёткое фото паспорта, иногда селфи с документом. Срок проверки — от 1 часа до 3 рабочих дней.</p>
  <p>Не пытайтесь вывести до завершения wagering — система аннулирует бонус и может заморозить аккаунт при подозрении на злоупотребление. Минимальная сумма вывода и комиссия указаны в кассе. Humo/Uzcard обычно 1–24 часа после одобрения; крипто — быстрее, но с учётом курса.</p>
  <p>Если вывод задерживается, обратитесь в live-чат с номером заявки. casino-bonuses-uz.com не обрабатывает платежи — только информируем о типичных сроках по рынку UZ 2026.</p>
</section>

<section class="section" id="providers-market">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Рынок UZ</span>
  <h2 class="section__title">Провайдеры и контекст рынка для {name}</h2></header>
  <p>Казино-раздел {name} (если доступен) обычно включает провайдеров: Pragmatic Play, Amatic, Endorphina, Evolution (live), Spribe (Aviator). Наличие конкретных студий зависит от лицензии и договоров оператора — каталог меняется. Слоты с высокой волатильностью быстрее съедают банкролл при отыгрыше — для wagering часто выбирают среднюю волатильность.</p>
  <p>Рынок Узбекистана 2026: игроки сравнивают welcome в UZS, а не в USD/EUR. Лидер по сумме — FairPari (20,2 млн + 150 FS). {name} на позиции #{rank} — альтернатива, если вам ближе {tags_str} или условия {b['wagering']}.</p>
  <p>Букмекерский сегмент (если тип «both» или БК): конкуренция между Linebet, Parimatch, Leon и гибридами вроде {name}. Спорт welcome с ×5 на экспрессах проще отыграть математически, чем казино ×35, но суммы меньше.</p>
</section>

<section class="section section--alt" id="responsible-brand">
  <header class="section__header section__header--compact"><span class="section__eyebrow">18+</span>
  <h2 class="section__title">Ответственная игра с бонусом {name}</h2></header>
  <p>Бонус увеличивает банкролл, но не гарантирует прибыль. Установите лимит депозита и времени в кабинете {name} до первой ставки. Не гонитесь за отыгрышем в последний день срока — это ведёт к импульсивным ставкам. Если чувствуете потерю контроля — самоисключение и пауза. Помощь: раздел ответственной игры на сайте оператора и локальные горячие линии.</p>
  <p>casino-bonuses-uz.com — информационный портал для совершеннолетних (18+) в Узбекистане. Мы не поощряем чрезмерную игру и не обещаем «лёгкий заработок» на welcome.</p>
</section>"""

    else:
        wag_block = f"""
<section class="section" id="wagering-guide">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Wagering</span>
  <h2 class="section__title">{name} welcome wagering — bosqichma-bosqich</h2></header>
  <p><strong>{b['wagering']}</strong> wagering degani: bonus (va ba'zan depozit) summasini ruxsat etilgan o'yinlarda shuncha marta aylantirish kerak. Misol: 1 000 000 UZS bonus, ×35 — 35 000 000 UZS aylanma slotlarda (100% hisob). Muddat odatda 7–14 kun.</p>
  <p>PROMO ni o'qing: max bet (ko'pincha 130 000 UZS gacha), to'liq hisoblanadigan slotlar, live/crash istisnolari. Live kazino 10–20% — wagering sekinlashadi.</p>
  <h3>Wageringdagi xatolar</h3>
  <ul class="section-list">
    <li>Max betdan yuqori stavka</li>
    <li>0% hisoblanadigan bo'limlarda o'ynash</li>
    <li>Wagering tugamay yechish so'rash — bonus yo'qoladi</li>
    <li>Sport va kazino bonusini aralashtirish</li>
    <li>Muddatni o'tkazib yuborish</li>
  </ul>
  <p><a href="{fp_link}">FairPari</a>: ×35, 20,2 mln UZS + 150 FS. {name} welcome kichikroq bo'lsa ham, past wagering (masalan ×30) umumiy aylanmani kamaytirishi mumkin.</p>
</section>"""

        reg_block = f"""
<section class="section section--alt" id="registration-detail">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Ro'yxatdan o'tish</span>
  <h2 class="section__title">{name} da batafsil ro'yxatdan o'tish UZ</h2></header>
  <p>Rasmiy operator saytida 2–5 daqiqa. casino-bonuses-uz.com mustaqil reyting — depozit qabul qilmaydi.</p>
  <ol class="section-list">
    <li>Rasmiy domenni oching (SSL va manzilni tekshiring).</li>
    <li>«Ro'yxatdan o'tish» — telefon, email yoki ijtimoiy tarmoq.</li>
    <li>Valyuta: <strong>UZS</strong>.</li>
    <li>Promokod maydoni (FairPari klasterida fa_1635).</li>
    <li>Welcome turi: kazino yoki sport — keyin o'zgartirish qiyin.</li>
    <li>SMS/email tasdiqlash, kassaga o'tish.</li>
    <li>Birinchi depozit — bonus PROMO qoidalariga ko'ra.</li>
  </ol>
  <p>Bir kishi — bitta akkaunt. 18+.</p>
</section>"""

        pay_block = f"""
<section class="section" id="payments-detail">
  <header class="section__header section__header--compact"><span class="section__eyebrow">To'lovlar</span>
  <h2 class="section__title">{name} depozit va yechish O'zbekiston</h2></header>
  <p>UZ standarti: <strong>Humo</strong>, <strong>Uzcard</strong>, <strong>Payme</strong>, <strong>Click</strong>. {name}: {escape(b['pay'])}.</p>
  <table class="data-table data-table--striped"><thead><tr><th>Usul</th><th>Depozit</th><th>Yechish</th><th>Izoh</th></tr></thead><tbody>
  <tr><td>Humo</td><td>Daqiqalar</td><td>1–24 soat</td><td>UZ da mashhur</td></tr>
  <tr><td>Uzcard</td><td>Daqiqalar</td><td>1–24 soat</td><td>Humo ga o'xshash</td></tr>
  <tr><td>Payme / Click</td><td>Tez</td><td>Operatorga qarab</td><td>Telefondan qulay</td></tr>
  <tr><td>Kripto</td><td>15–60 min</td><td>24 soatgacha</td><td>USDT, BTC</td></tr>
  </tbody></table>
  <p>Birinchi yechishda <strong>KYC</strong>: hujjat surati. Limitlar kabinetda.</p>
</section>"""

        cmp_block = f"""
<section class="section section--alt" id="comparison">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Taqqoslash</span>
  <h2 class="section__title">{name} vs FairPari, {c1}</h2></header>
  <p>Reyting pozitsiyasi: <strong>#{rank}</strong>. <a href="{fp_link}">FairPari #1</a> — 20 200 000 UZS + 150 FS, ×35.</p>
  <table class="data-table data-table--compact"><thead><tr><th>Operator</th><th>Welcome</th><th>Wagering</th><th>To'lov</th></tr></thead><tbody>
  <tr><td>FairPari</td><td>20,2 mln + 150 FS</td><td>×35</td><td>Humo, Payme</td></tr>
  <tr><td>{name}</td><td>{escape(welcome)}</td><td>{b['wagering']}</td><td>{escape(b['pay'])}</td></tr>
  <tr><td>{c1}</td><td colspan="3"><a href="{prefix}{c1.lower().replace(' ', '-').replace('.', '')}/">Sharh</a></td></tr>
  </tbody></table>
</section>"""

        casino_extra = ""
        if t in ("both", "casino"):
            casino_extra = f"""
<section class="section" id="slots-detail">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Slotlar</span>
  <h2 class="section__title">{name} slotlar va live — bonus bilan</h2></header>
  <p>Slotlar, live, crash UZS da. Welcome odatda vide slotlarda 100% hisoblanadi. Live ruletka kamroq %. Mashhur: Gates of Olympus, Sweet Bonanza, Aviator, Crazy Time — operator provayderlariga bog'liq.</p>
  <p>FS welcome ichida ma'lum slotlarga bog'langan — PROMO ro'yxati. FS yutug'i ham {b['wagering']} wagering.</p>
</section>"""

        sport_extra = ""
        if t in ("both", "bk"):
            sport_extra = f"""
<section class="section section--alt" id="sport-detail">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Sport</span>
  <h2 class="section__title">{name} sport stavkalari</h2></header>
  <p>Pre-match, live, ekspress. Sport welcome ×5 ekspress (taxminiy). Kazino welcome bilan aralashtirilmaydi. UZ da futbol, basketbol, tennis mashhur.</p>
</section>"""

        method_block = """
<section class="section" id="methodology">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Metodologiya</span>
  <h2 class="section__title">Reyting qanday tuziladi</h2></header>
  <p>casino-bonuses-uz.com mustaqil agregator. {name} uchun #{rank} — welcome, wagering, Humo/Payme, mobil, UZ sharhlar asosida. 2026 yangilangan. 18+.</p>
  <p>Biz faqat bannerdagi raqamni emas, bonusning to'liq «narxini» ham hisoblaymiz: summa × wagering, muddat, max bet va to'liq hisoblanadigan o'yinlar ro'yxati. Kichik welcome, lekin ×30 va uzoq muddat ba'zan katta paket + ×45 dan foydaliroq bo'lishi mumkin.</p>
  <p>Toshkent, Samarqand, Buxoro va boshqa shaharlardan o'yinchilar uchun UZS konvertatsiyasiz Humo/Uzcard muhim. {name} da {pay} qabul qilinsa — bu plus, lekin ro'yxatdan keyin kassani tekshiring.</p>
</section>""".replace("{name}", name).replace("{rank}", str(rank)).replace("{pay}", escape(b['pay']))

        tags_str = ", ".join(b.get("tags_uz", []))
        deep_block = f"""
<section class="section section--alt" id="mobile-app">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Mobil</span>
  <h2 class="section__title">{name} ilovasi va mobil versiya</h2></header>
  <p>UZ o'yinchilari ko'pincha telefondan o'ynaydi: Android APK, iOS PWA yoki mobil sayt. {name} rasmiy saytida «Ilova» bo'limini tekshiring. APK ni faqat operator domenidan yuklang — forumdagi soxta fayllar xavfli.</p>
  <p>Desktop va mobil bir akkaunt: welcome va wagering sinxron. Push-bildirishnomalar qulay, lekin depozit limitini o'chirmang. Play Market da bo'lmasa — PWA (bosh ekranga yorliq) xavfsiz alternativa.</p>
  <p><a href="{fp_link}">FairPari</a> UZ uchun APK/PWA ni faol targ'ib qiladi. {name} da live va slotlar mobil mijozda barqarorligini katta depozitdan oldin sinab ko'ring.</p>
</section>

<section class="section" id="vip-reload">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Aksiyalar</span>
  <h2 class="section__title">{name} reload, keshbek va VIP</h2></header>
  <p>Welcome — faqat boshlanish. Keyin reload (2–5-depozit foizi), haftalik keshbek, slot turnirlari va VIP darajalar. {name} PROMO da shartlarni o'qing — birinchi wagering tugamaguncha ikkinchi bonusni faollashtirmang.</p>
  <p>Keshbek odatda ×3–×10 wagering bilan, davr uchun sof minusdan. VIP tezroq yechish va yuqori limit — lekin aylanma talab qiladi. Oddiy UZ o'yinchisi uchun shaffof welcome va Humo ko'pincha VIP dan muhimroq.</p>
  <p>Turnirlar: UZS yoki FS mukofot, stavka summasi bo'yicha reyting. Qoidalar va byudjetni o'qing.</p>
</section>

<section class="section section--alt" id="withdrawal-guide">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Yechish</span>
  <h2 class="section__title">{name} da welcome dan keyin yechish</h2></header>
  <p>{b['wagering']} wagering to'liq bajarilgach bonus real balansga o'tadi — PROMO buzilmagan bo'lsa. Yechish: kabinet → «Withdraw» → {escape(b['pay'])}. Birinchi marta KYC: pasport surati, ba'zan selfie. Tekshiruv 1 soatdan 3 ish kunigacha.</p>
  <p>Wagering tugamay yechish so'rash — bonus yo'qoladi. Minimal summa va komissiya kassada. Humo/Uzcard odatda 1–24 soat; kripto tezroq, kursni hisobga oling.</p>
  <p>Kechiksa — live-chat, ariza raqami bilan. casino-bonuses-uz.com to'lov qilmaydi.</p>
</section>

<section class="section" id="providers-market">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Bozor</span>
  <h2 class="section__title">{name} va UZ bozori konteksti</h2></header>
  <p>{name} kazino bo'limida (mavjud bo'lsa) Pragmatic, Amatic, Endorphina, Evolution, Spribe kabi provayderlar bo'lishi mumkin — katalog o'zgaradi. Yuqori volatillik bankrollni tez kamaytiradi; wagering uchun o'rta volatillik tanlanadi.</p>
  <p>2026 UZ: o'yinchilar USD emas, UZS welcome solishtiradi. Lider — FairPari (20,2 mln + 150 FS). {name} #{rank} — agar sizga {tags_str} yoki {b['wagering']} yaqin bo'lsa.</p>
  <p>BK segmentida Linebet, Parimatch, Leon va {name} kabi gibridlar raqobatlashadi. Sport welcome ×5 ekspressda matematik jihatdan osonroq, summalar kichikroq.</p>
</section>

<section class="section section--alt" id="responsible-brand">
  <header class="section__header section__header--compact"><span class="section__eyebrow">18+</span>
  <h2 class="section__title">{name} bonusi bilan mas'uliyatli o'yin</h2></header>
  <p>Bonus bankrollni oshiradi, foyda kafolatlamaydi. Birinchi stavkadan oldin depozit va vaqt limiti qo'ying. Oxirgi kunda wagering quvish — impulsiv stavkalar. Nazorat yo'qolsa — o'z-o'zini chetlashtirish.</p>
  <p>casino-bonuses-uz.com — 18+ ma'lumot portali. Ortiqcha o'yinni rag'batlantirmaymiz.</p>
</section>"""

    return wag_block + reg_block + pay_block + casino_extra + sport_extra + cmp_block + method_block + deep_block + _uz_parity_block(b, rank, lang) + brand_tz_boost(b, rank, lang)


def brand_tz_boost(b: dict, rank: int, lang: str) -> str:
    """~400 words extra per brand for TZ ≥2500 target."""
    name = b["name"]
    welcome = b["welcome_ru"] if lang == "ru" else b["welcome_uz"]
    prefix = "/ru/" if lang == "ru" else "/"
    c1, c2 = COMPETITORS.get(b["slug"], ("FairPari", "1win"))

    if lang == "ru":
        return f"""
<section class="section section--alt" id="mobile-payments-deep">
  <header class="section__header section__header--compact"><span class="section__eyebrow">UZ</span>
  <h2 class="section__title">{name} — мобильное приложение и платежи в деталях</h2></header>
  <p>Для игроков Узбекистана мобильный доступ и Humo/Payme часто важнее размера баннера. {name} принимает: {escape(b['pay'])}. Скачивайте APK или PWA только с официального сайта — зеркала в Telegram несут риск фишинга.</p>
  <p>Типичный сценарий: регистрация в приложении → выбор UZS → промокод (если есть) → депозит Humo → бонус в PROMO → слоты для wagering. Вывод на ту же карту после KYC. Первый вывод может занять до 72 часов — это норма для верификации, не «задержка бонуса».</p>
  <h3>Сравнение с {c1} и {c2}</h3>
  <p>Если welcome {name} ({welcome}) меньше, чем у FairPari, проверьте wagering: иногда ×30 у 1win компенсирует меньшую сумму на баннере. {c2} может выигрывать линией live-ставок, но проигрывать в FS. Используйте <a href="{prefix}#rating">рейтинг TOP-20</a> для бокового сравнения, а не только один обзор.</p>
  <p>Полный гид FairPari: <a href="https://fairpari-casino-bonus.com/ru/" rel="noopener">FairPari to'liq bonus</a>. Каталог подтем: <a href="https://fairpari-casino-bonuses.com/ru/bonusy-kazino/" rel="noopener">FairPari promo va FS</a>.</p>
  <h3>Частые проблемы с бонусом</h3>
  <p>Бонус не начислился — проверьте порядок промокода и депозита; иногда нужна кнопка «Получить бонус». Вейджер не двигается — играете ли вы в слотах (100% зачёт)? Вывод отклонён — KYC и соблюдение max bet.</p>
  <p>Карточка рейтинга #{rank}: welcome {escape(welcome)}, вейджер {b['wagering']}. Обновлено 2026-06-18.</p>
  <table class="data-table data-table--compact"><thead><tr><th>Оператор</th><th>Welcome</th><th>Вейджер</th></tr></thead><tbody>
  <tr><td>{escape(name)}</td><td>{escape(welcome)}</td><td>{b['wagering']}</td></tr>
  <tr><td>{escape(c1)}</td><td>В рейтинге</td><td><a href="{prefix}{c1.lower().replace(' ', '-')}/">сравнить</a></td></tr>
  <tr><td>{escape(c2)}</td><td>В рейтинге</td><td><a href="{prefix}{c2.lower().replace(' ', '-')}/">сравнить</a></td></tr>
  <tr><td>FairPari №1</td><td>20,2 млн + 150 FS</td><td>×35</td></tr>
  </tbody></table>
  <h3>Рынок Узбекистана и {name}</h3>
  <p>В 2026 году {name} известен игрокам UZ пакетом {welcome}. Вейджер {b['wagering']} — {"мягче" if "×3" in b["wagering"] or "×5" in b["wagering"] else "средний"} для рынка. Платежи: {escape(b['pay'])}. Мы независимый рейтинг, не оператор; суммы из официального PROMO и могут меняться.</p>
  <p>Новичкам: сначала <a href="{prefix}kazino-bonuslari/">типы бонусов</a> и <a href="{prefix}welcome-bonus/">сравнение welcome</a>, затем переход на официальный сайт. 18+.</p>
  <h3>Пошаговая активация welcome в {name}</h3>
  <ol class="section-list">
    <li>Откройте официальный сайт {name} (не зеркала из соцсетей).</li>
    <li>Регистрация: телефон или email, валюта UZS.</li>
    <li>Выберите тип welcome — казино или спорт, если предлагается выбор.</li>
    <li>Введите промокод, если требуется для вашего региона.</li>
    <li>В кассе выберите {escape(b['pay'].split(',')[0].strip())} или другой доступный метод.</li>
    <li>Внесите депозит не ниже минимума из PROMO.</li>
    <li>Убедитесь, что бонус отображается в кабинете или разделе «Бонусы».</li>
    <li>Играйте в разрешённых играх, соблюдая max bet до завершения вейджера {b['wagering']}.</li>
  </ol>
</section>"""

    return f"""
<section class="section section--alt" id="mobile-payments-deep">
  <header class="section__header section__header--compact"><span class="section__eyebrow">UZ</span>
  <h2 class="section__title">{name} — mobil ilova va to'lovlar batafsil</h2></header>
  <p>O'zbekiston o'yinchisi uchun mobil kirish va Humo/Payme ko'pincha banner hajmidan muhimroq. {name} qabul qiladi: {escape(b['pay'])}. APK yoki PWA ni faqat rasmiy saytdan yuklang — Telegram oynalari fishing xavfi.</p>
  <p>Oddiy ssenariy: ilovada ro'yxat → UZS → promokod → Humo depozit → PROMO da bonus → wagering uchun slotlar. KYC dan keyin o'sha kartaga yechish. Birinchi yechish 72 soatgacha — verifikatsiya, «bonus kechikishi» emas.</p>
  <h3>{c1} va {c2} bilan taqqoslash</h3>
  <p>Welcome {name} ({welcome}) FairPari dan kichik bo'lsa, wagering ni solishtiring: ba'zan 1win ×30 bannerni qoplaydi. {c2} live liniyada yutishi, FS da yutqazishi mumkin. <a href="{prefix}#rating">TOP-20 reyting</a> dan foydalaning.</p>
  <p><a href="https://fairpari-casino-bonus.com/" rel="noopener">FairPari to'liq bonus</a> · <a href="https://fairpari-casino-bonuses.com/kazino-bonuslari/" rel="noopener">FairPari promo va FS</a></p>
  <h3>Tez-tez uchraydigan muammolar</h3>
  <p>Bonus tushmadi — promokod va depozit tartibini tekshiring; ba'zi operatorlarda avval «Bonus olish» tugmasi kerak. Wagering o'ynamaydi — live yoki sport bo'limida o'ynayapsizmi? Slotlar 100% hisoblanadi. Yechish rad etildi — KYC hujjatlari va max bet buzilmaganligini tasdiqlang.</p>
  <p>Reyting kartochkasi #{rank}: welcome {escape(welcome)}, wagering {b['wagering']}. Yangilanish 2026-06-18.</p>
  <table class="data-table data-table--compact"><thead><tr><th>Operator</th><th>Welcome</th><th>Wagering</th></tr></thead><tbody>
  <tr><td>{escape(name)}</td><td>{escape(welcome)}</td><td>{b['wagering']}</td></tr>
  <tr><td>{escape(c1)}</td><td>Reytingda</td><td><a href="{prefix}{c1.lower().replace(' ', '-')}/">solishtirish</a></td></tr>
  <tr><td>{escape(c2)}</td><td>Reytingda</td><td><a href="{prefix}{c2.lower().replace(' ', '-')}/">solishtirish</a></td></tr>
  <tr><td>FairPari #1</td><td>20,2 mln + 150 FS</td><td>×35</td></tr>
  </tbody></table>
  <h3>O'zbekiston bozori va {name}</h3>
  <p>2026 yilda {name} UZ o'yinchilari orasida {welcome} bilan tanilgan. Wagering {b['wagering']} — bozor o'rtachasiga nisbatan {"yengil" if "×3" in b["wagering"] or "×5" in b["wagering"] else "o'rtacha"}. To'lovlar: {escape(b['pay'])} — depozit va yechish uchun asosiy kanallar. Biz mustaqil reyting sifatida operator emasmiz; barcha summalar rasmiy PROMO dan olingan va o'zgarishi mumkin.</p>
  <p>Agar siz birinchi marta onlayn kazino yoki BK tanlayotgan bo'lsangiz, avval <a href="{prefix}kazino-bonuslari/">bonus turlari</a> va <a href="{prefix}welcome-bonus/">welcome taqqoslash</a> ni o'qing, keyin ushbu sharhdagi CTA orqali rasmiy saytga o'ting. 18+.</p>
  <h3>{name} da welcome faollashtirish — 8 qadam</h3>
  <ol class="section-list">
    <li>{name} rasmiy saytini oching (ijtimoiy tarmoq oynalari emas).</li>
    <li>Ro'yxatdan o'tish: telefon yoki email, UZS valyuta.</li>
    <li>Welcome turini tanlang — kazino yoki sport.</li>
    <li>Kerak bo'lsa promokod kiriting.</li>
    <li>Kassada {escape(b['pay'].split(',')[0].strip())} yoki boshqa usulni tanlang.</li>
    <li>PROMO dagi minimal depozitdan kam bo'lmagan summa kiriting.</li>
    <li>Bonus kabinetda yoki «Bonuslar» bo'limida ko'rinishini tekshiring.</li>
    <li>Wagering {b['wagering']} tugaguncha ruxsat etilgan o'yinlarda max bet ga rioya qiling.</li>
  </ol>
</section>"""


def _uz_parity_block(b: dict, rank: int, lang: str) -> str:
    """Extra ~650 words for uz reviews to match ru length."""
    if lang != "uz":
        return ""
    name = b["name"]
    welcome = b["welcome_uz"]
    prefix = "/"
    fp_link = f"{prefix}fairpari/"
    return f"""
<section class="section" id="uz-deep-guide">
  <header class="section__header section__header--compact"><span class="section__eyebrow">Qo'llanma</span>
  <h2 class="section__title">{name} bonusi bo'yicha to'liq UZ qo'llanmasi 2026</h2></header>
  <p>O'zbekiston o'yinchilari uchun {name} — reytingimizda <strong>#{rank}</strong> o'rin. Welcome paket: <strong>{escape(welcome)}</strong>, wagering <strong>{b['wagering']}</strong>, to'lovlar: {escape(b['pay'])}. Bu bo'limda bonusni qanday olish, wageringni hisoblash va yechishni rejalashtirish haqida batafsil yozilgan — mustaqil ma'lumot, operator emas.</p>
  <h3>Birinchi depozit va bonus faollashtirish</h3>
  <p>Ro'yxatdan o'tgach, kassada UZS valyutasini tanlang. Humo yoki Uzcard orqali minimal depozit qiling — summa PROMO dagi minimumdan past bo'lmasin. Ba'zi operatorlarda bonus avtomatik, ba'zarida «Bonus olish» tugmasi kerak. {name} shartlarini rasmiy PROMO bo'limida o'qing: birinchi depozit foizi, FS soni va muddat bir joyda ko'rsatiladi.</p>
  <p>Agar kazino va sport welcome alohida bo'lsa (ko'p hibrid BK+ kazino larda shunday), ro'yxatdan oldin yo'nalishni tanlang. Keyin o'zgartirish qiyin. FairPari misolida kazino 20,2 mln UZS + 150 FS yoki sport 1,4 mln UZS — bittasini tanlaysiz. {name} uchun ham shunga o'xshash qoida bo'lishi mumkin.</p>
  <h3>Wagering hisob-kitobi — amaliy misollar</h3>
  <p>Misol: sizga 500 000 UZS bonus berildi, wagering ×35. Kerakli aylanma: 17 500 000 UZS slotlarda (100% hisob). Agar slotlar 100% emas, 10% hisoblanadigan live da o'ynasangiz, vaqt sezilarli darajada uzayadi. Shuning uchun wagering uchun vide slotlar tanlanadi: Gates of Olympus, Sweet Bonanza kabi mashhur o'yinlar — operator ro'yxatida bo'lsa.</p>
  <p>Max bet qoidasi: ko'pincha bir spin yoki stavka 50 000–130 000 UZS dan oshmasin. Bu limitdan yuqori tikish bonusni bekor qilishi mumkin — hatto tasodifan bosilgan katta stavka ham. {name} kabinetida faol bonus bo'lsa, stavka hajmini oldindan tekshiring.</p>
  <h3>To'lovlar va KYC — O'zbekiston realiyasi</h3>
  <p>Mahalliy o'yinchilar Humo, Uzcard, Payme va Click dan foydalanadi. {name} qabul qiladi: {escape(b['pay'])}. Depozit odatda daqiqalar ichida; yechish birinchi marta KYC dan keyin 1–24 soat. Pasport yoki ID skanini oldindan tayyorlang — bu welcome yutug'ini tezroq chiqarishga yordam beradi.</p>
  <p>Kripto (USDT) ba'zi operatorlarda mavjud — kurs va minimal summa kartadan yuqori bo'lishi mumkin. Agar siz faqat milliy kartadan foydalansangiz, kripto bo'limini o'tkazib yuborishingiz mumkin.</p>
  <h3>{name} va reyting lideri FairPari</h3>
  <p><a href="{fp_link}">FairPari #1</a> — 20 200 000 UZS + 150 FS, promo fa_1635, Humo/Payme/Click. {name} kichikroq welcome bersa ham, past wagering yoki kuchli sport liniyasi siz uchun muhimroq bo'lishi mumkin. Taqqoslash jadvali sahifa boshida va <a href="{prefix}#rating">TOP-20 reytingda</a>.</p>
  <p>Boshqa hub sahifalar: <a href="{prefix}welcome-bonus/">welcome taqqoslash</a>, <a href="{prefix}kazino-bonuslari/">bonus turlari</a>, <a href="{prefix}depozitsiz-bonus/">depozitsiz</a>, <a href="{prefix}tolov-uz/">to'lovlar</a>, <a href="{prefix}faq/">FAQ</a>.</p>
  <h3>Mas'uliyatli o'yin eslatmasi</h3>
  <p>Bonus — ko'ngilochar xizmat uchun rag'bat, daromad kafolati emas. Byudjet belgilang, yo'qotishlarni quvmang. 18+. casino-bonuses-uz.com depozit qabul qilmaydi — barcha to'lovlar faqat {name} rasmiy saytida.</p>
  <h3>Tez-tez so'raladigan savollar (qisqa)</h3>
  <p><strong>Promokod kerakmi?</strong> Ba'zi operatorlarda ha — FairPari UZ da fa_1635. {name} uchun PROMO yoki ro'yxatdan o'tish formasini tekshiring.</p>
  <p><strong>Ikkinchi akkaunt ochsam bo'ladimi?</strong> Yo'q — multiakkaunt bonusni bekor qiladi va bloklanishga olib keladi.</p>
  <p><strong>Mobil ilovada wagering hisoblansinmi?</strong> Ha, odatda bitta akkaunt — desktop va telefon sinxron.</p>
  <p><strong>Yechish necha kun?</strong> KYC dan keyin Humo/Uzcard odatda 1–24 soat; birinchi marta uzoqroq bo'lishi mumkin.</p>
  <p><strong>{name} litsenziyasi bormi?</strong> Offshore Curacao yoki boshqa yurisdiksiya ko'p UZ operatorlarida uchraydi — rasmiy sayt footerida ko'rsatiladi. Biz litsenziya raqamini mustaqil tasdiqlamaymiz; faqat ommaviy ma'lumot beramiz.</p>
  <p>Reytingimizda {name} kartasida teglar va qisqa afzalliklar ko'rsatilgan — ularni bosh sahifadagi TOP-20 filtri orqali boshqa operatorlar bilan yonma-yon solishtiring. Yangilanish sanasi 2026; welcome summalari haftalar ichida o'zgarishi mumkin, shuning uchun depozitdan oldin ikki marta tekshirish — odatiy amaliyot tajribali UZ o'yinchilari uchun.</p>
  <p><strong>Xulosa:</strong> {name} — welcome {escape(welcome)}, wagering {b['wagering']}, to'lov {escape(b['pay'])}. Agar ustuvorlik katta boshlang'ich paket bo'lsa, <a href="{fp_link}">FairPari</a> ni ko'ring; agar sport liniyasi yoki past wagering muhim bo'lsa, {name} mantiqiy tanlov bo'lishi mumkin. Har qanday holatda PROMO shartlarini o'qing va 18+ qoidalariga amal qiling.</p>
</section>"""


def all_faq_items(b, rank, lang):
    from brand_qttk_content import _faq_items
    return _faq_items(b, rank, lang) + _faq_extended(b, rank, lang)
