#!/usr/bin/env python3
"""Push hub pages over 2500 words (pass 4)."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKER = 'id="pass4-expand"'

PASS4_UZ = {
    "kazino-bonuslari": '''
<section class="section prose" id="pass4-expand">
<h2>Bonus turlari bo'yicha chuqur qo'llanma</h2>
<p>O'zbekistonda onlayn kazino va bukmekerlar bir nechta bonus formatini taklif qiladi. <strong>Welcome</strong> — birinchi depozitga foiz yoki paket; <strong>free spins</strong> — slotlarda bepul aylanishlar; <strong>cashback</strong> — haftalik yo'qotishdan qaytarish; <strong>reload</strong> — keyingi depozitlar uchun qo'shimcha foiz. FairPari reytingimizda #1, chunki kazino welcome 20,2 mln UZS + 150 FS to'rt bosqichda, wagering ×35 va Humo/Payme/Click qo'llab-quvvatlanadi.</p>
<h3>Wagering nima va qanday hisoblanadi?</h3>
<p>Wagering (veyjer) — bonus summasini qancha marta aylantirish kerakligi. Masalan, 1 000 000 UZS bonus ×35 = 35 000 000 UZS tikish hajmi. Slotlar odatda 100% hisoblanadi, live kazino 10–20%, sport alohida ×5 qoidasi bilan. Muddat odatda 7–30 kun — PROMO bo'limida tekshiring.</p>
<h3>Promokod va fa_1635</h3>
<p>FairPari da kazino paketi uchun <strong>fa_1635</strong> promokodi ro'yxatdan o'tishda kiritiladi. Sport welcome alohida — aralashtirmang. Batafsil: <a href="../fairpari/">FairPari sharhi</a>, <a href="https://fairpari-casino-bonuses.com/promokod/" rel="noopener">FairPari promokod hub</a>.</p>
<h3>TOP-3 taqqoslash jadvali</h3>
<table class="data-table"><thead><tr><th>Operator</th><th>Welcome</th><th>Wagering</th><th>To'lov</th></tr></thead>
<tbody>
<tr><td><a href="../fairpari/">FairPari</a></td><td>20,2 mln + 150 FS</td><td>×35</td><td>Humo, Payme</td></tr>
<tr><td><a href="../1win/">1win</a></td><td>12 mln gacha</td><td>×30</td><td>Humo, Uzcard</td></tr>
<tr><td><a href="../mostbet/">Mostbet</a></td><td>8,5 mln + 250 FS</td><td>×35</td><td>Humo, Payme</td></tr>
</tbody></table>
<p>Mas'uliyatli o'yin: 18+, faqat o'z mablag'ingiz bilan. <a href="/masuliyatli-oyin/">Mas'uliyatli o'yin</a> · <a href="../faq/">FAQ</a> · <a href="../#rating">To'liq reyting</a>.</p>
</section>''',
    "welcome-bonus": '''
<section class="section prose" id="pass4-expand">
<h2>Welcome bonus 2026 — to'liq qo'llanma O'zbekiston</h2>
<p>Welcome — eng katta bonus turi: birinchi depozitdan keyin qo'shimcha mablag' yoki frispinlar. FairPari #1: 20,2 mln UZS + 150 FS, to'rt bosqich, har bosqich alohida depozit. 1win katta foiz (500% gacha), lekin wagering yuqoriroq bo'lishi mumkin. Mostbet va Melbet ham kuchli paketlar beradi — <a href="../#rating">reyting jadvali</a>.</p>
<h3>Qadamlar: welcome olish</h3>
<ol><li>Operator tanlang (FairPari tavsiya)</li><li>Ro'yxatdan o'ting, promokod fa_1635</li><li>Kazino yoki sport paketini tanlang — aralashtirmang</li><li>Humo/Payme bilan depozit — <a href="../tolov-uz/">to'lovlar</a></li><li>PROMO da bonus tasdiqlang, wagering boshlang</li></ol>
<h3>Max bet va yechish</h3>
<p>Faol bonusda max bet odatda 50 000–130 000 UZS. Cheklovdan oshish bonusni bekor qilishi mumkin. Birinchi yechishda KYC (pasport/ID) talab qilinadi — 24–72 soat.</p>
<p>EMD qo'llanma: <a href="https://fairpari-casino-bonus.com/" rel="noopener">fairpari-casino-bonus.com</a>. Keshbek va reload: <a href="https://fairpari-casino-bonuses.com/kazino-bonuslari/" rel="noopener">bonuslar hub</a>.</p>
</section>''',
    "depozitsiz-bonus": '''
<section class="section prose" id="pass4-expand">
<h2>Depozitsiz bonus — haqiqat va miflar UZ</h2>
<p>«Depozitsiz 5 mln UZS» reklamalari ko'pincha mif. O'zbekistonda doimiy no-deposit kam; ba'zan ro'yxatdan FS yoki turnir freebet beriladi. FairPari asosiy qiymati — depozitli welcome 20,2 mln + 150 FS; depozitsiz aksiyalar vaqtinchak PROMO da.</p>
<h3>Qanday tekshirish?</h3>
<ul><li>Rasmiy PROMO bo'limidagi shartlar</li><li>Wagering va muddat — agar juda yuqori bo'lsa, ehtiyot bo'ling</li><li>Max yechish limiti depozitsiz bonuslarda past bo'ladi</li><li>Litsenziya va KYC talablari</li></ul>
<h3>Alternativa: kichik depozit + katta welcome</h3>
<p>500 000 UZS depozit + FairPari welcome ko'pincha «depozitsiz» mifidan foydaliroq. <a href="../welcome-bonus/">Welcome qo'llanma</a> · <a href="../fairpari/">FairPari #1</a>.</p>
</section>''',
    "tolov-uz": '''
<section class="section prose" id="pass4-expand">
<h2>O'zbekiston to'lovlari — Humo, Payme, Click, kripto</h2>
<p>Mahalliy kartalar (Humo, Uzcard) eng tez usul — daqiqalar ichida depozit. Payme va Click ham mashhur. Kripto (USDT) ba'zi operatorlarda alohida bonus beradi, lekin Humo yo'q. FairPari barcha asosiy UZ usullarini qo'llab-quvvatlaydi.</p>
<h3>Depozit va yechish vaqti</h3>
<table class="data-table"><thead><tr><th>Usul</th><th>Depozit</th><th>Yechish</th><th>Eslatma</th></tr></thead>
<tbody>
<tr><td>Humo</td><td>1–5 min</td><td>15 min – 24 soat</td><td>KYC birinchi yechishda</td></tr>
<tr><td>Payme</td><td>Tez</td><td>Operatorga qarab</td><td>Limitlar PROMO da</td></tr>
<tr><td>USDT</td><td>15–60 min</td><td>1–24 soat</td><td>BC.Game va boshqalar</td></tr>
</tbody></table>
<p>Bonus faollashtirish: avval promokod, keyin depozit tanlangan usulda. <a href="../welcome-bonus/">Welcome</a> · <a href="../#rating">Reyting</a>.</p>
</section>''',
    "faq": '''
<section class="section prose" id="pass4-expand">
<h2>Qo'shimcha FAQ — bonuslar O'zbekiston 2026</h2>
<dl class="faq-list">
<dt>FairPari nima uchun #1?</dt>
<dd>Eng katta welcome (20,2 mln UZS + 150 FS), UZS, Humo/Payme, APK va litsenziya.</dd>
<dt>Wagering ×35 qancha vaqt oladi?</dt>
<dd>O'rtacha o'yinchi 7–14 kun; muddat PROMO da ko'rsatiladi.</dd>
<dt>1win yoki FairPari?</dt>
<dd><a href="../1win/">1win sharhi</a> va <a href="../fairpari/">FairPari</a> — welcome va wagering ni solishtiring.</dd>
<dt>Promokod qayerda kiritiladi?</dt>
<dd>Ro'yxatdan o'tish formasi yoki PROMO; FairPari kazino: fa_1635.</dd>
<dt>Humo bilan chiqarish mumkinmi?</dt>
<dd>Ha, KYC dan keyin ko'p operatorlar Humo ga qaytaradi.</dd>
<dt>Sport va kazino bonus birga?</dt>
<dd>Odatda yo'q — bittasini tanlang.</dd>
</dl>
<p>To'liq reyting: <a href="../#rating">TOP-20</a>. FairPari EMD: <a href="https://fairpari-casino-bonus.com/" rel="noopener">fairpari-casino-bonus.com</a>.</p>
</section>''',
}

PASS4_RU = {
    "kazino-bonuslari": '''
<section class="section prose" id="pass4-expand">
<h2>Глубокий гайд по типам бонусов</h2>
<p>В Узбекистане операторы предлагают welcome, фриспины, cashback, reload и VIP. FairPari #1 в рейтинге: 20,2 млн UZS + 150 FS, wagering ×35, Humo/Payme/Click. Сравните с <a href="/ru/1win/">1win</a> и <a href="/ru/mostbet/">Mostbet</a> в таблице ниже.</p>
<h3>Как считается вейджер</h3>
<p>Бонус × множитель = объём ставок. Слоты 100%, live 10–20%, спорт отдельно ×5. Срок 7–30 дней — смотрите PROMO.</p>
<table class="data-table"><thead><tr><th>Оператор</th><th>Welcome</th><th>Вейджер</th></tr></thead>
<tbody>
<tr><td><a href="/ru/fairpari/">FairPari</a></td><td>20,2 млн + 150 FS</td><td>×35</td></tr>
<tr><td><a href="/ru/1win/">1win</a></td><td>до 12 млн</td><td>×30</td></tr>
<tr><td><a href="/ru/mostbet/">Mostbet</a></td><td>8,5 млн + 250 FS</td><td>×35</td></tr>
</tbody></table>
<p><a href="/ru/#rating">Полный рейтинг</a> · <a href="https://fairpari-casino-bonuses.com/ru/kazino-bonuslari/" rel="noopener">хаб FairPari</a>.</p>
</section>''',
    "welcome-bonus": '''
<section class="section prose" id="pass4-expand">
<h2>Welcome bonus 2026 — полный гайд для UZ</h2>
<p>Welcome — главный пакет после первого депозита. FairPari: 20,2 млн UZS + 150 FS в четыре этапа. Не смешивайте казино и спорт welcome. Промокод fa_1635 для казино-пакета.</p>
<ol><li>Выберите оператора (<a href="/ru/fairpari/">FairPari #1</a>)</li><li>Регистрация + промокод</li><li>Депозит Humo/Payme — <a href="/ru/tolov-uz/">платежи</a></li><li>Отыгрыш в срок, соблюдайте max bet</li></ol>
<p>EMD: <a href="https://fairpari-casino-bonus.com/ru/" rel="noopener">fairpari-casino-bonus.com/ru/</a>.</p>
</section>''',
    "depozitsiz-bonus": '''
<section class="section prose" id="pass4-expand">
<h2>Бонус без депозита — мифы и реальность</h2>
<p>Постоянный no deposit в UZ редок. FairPari даёт основную ценность через welcome с депозитом. Временные акции без депозита — в PROMO. Проверяйте вейджер и лимит вывода.</p>
<p>Альтернатива: небольшой депозит + крупный welcome выгоднее «бесплатных» 100 FS с ×60. <a href="/ru/welcome-bonus/">Welcome</a> · <a href="/ru/fairpari/">FairPari</a>.</p>
</section>''',
    "tolov-uz": '''
<section class="section prose" id="pass4-expand">
<h2>Платежи Humo, Payme, Click в казино UZ</h2>
<p>Humo и Uzcard — самые быстрые депозиты. Payme и Click популярны в приложениях. Крипто — отдельные бонусы у BC.Game и др. FairPari поддерживает основные локальные методы.</p>
<table class="data-table"><thead><tr><th>Метод</th><th>Депозит</th><th>Вывод</th></tr></thead>
<tbody>
<tr><td>Humo</td><td>1–5 мин</td><td>до 24 ч после KYC</td></tr>
<tr><td>Payme</td><td>быстро</td><td>по правилам оператора</td></tr>
<tr><td>USDT</td><td>15–60 мин</td><td>1–24 ч</td></tr>
</tbody></table>
<p><a href="/ru/welcome-bonus/">Активация welcome</a> · <a href="/ru/#rating">Рейтинг TOP-20</a>.</p>
</section>''',
    "faq": '''
<section class="section prose" id="pass4-expand">
<h2>Дополнительные вопросы FAQ</h2>
<dl class="faq-list">
<dt>Почему FairPari #1?</dt>
<dd>Крупнейший welcome, UZS, Humo/Payme, мобильное приложение.</dd>
<dt>Сколько отыгрывать ×35?</dt>
<dd>Зависит от суммы бонуса и ставок; обычно 7–14 дней активной игры.</dd>
<dt>Где полный гайд FairPari?</dt>
<dd><a href="https://fairpari-casino-bonus.com/ru/" rel="noopener">fairpari-casino-bonus.com/ru/</a></dd>
<dt>1win или FairPari?</dt>
<dd><a href="/ru/1win/">Обзор 1win</a> и <a href="/ru/fairpari/">FairPari</a>.</dd>
<dt>Можно ли вывести на Humo?</dt>
<dd>Да, после верификации у большинства операторов из рейтинга.</dd>
</dl>
</section>''',
}


def inject(path: Path, block: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if MARKER in text:
        return False
    text = text.replace("</main>", block + "\n</main>", 1)
    path.write_text(text, encoding="utf-8")
    return True


def main():
    n = 0
    for slug, block in PASS4_UZ.items():
        p = ROOT / slug / "index.html"
        if p.exists() and inject(p, block):
            print("UZ:", slug)
            n += 1
    for slug, block in PASS4_RU.items():
        p = ROOT / "ru" / slug / "index.html"
        if p.exists() and inject(p, block):
            print("RU:", slug)
            n += 1
    print(f"Done: {n} hubs expanded")


if __name__ == "__main__":
    main()
