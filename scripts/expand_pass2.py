#!/usr/bin/env python3
"""Expand stub pages on casino-bonuses-uz.com to 800+ words (UZ) and RU mirrors."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://casino-bonuses-uz.com"

# Extra content blocks per slug (appended before </main>)
EXTRA_UZ = {
    "kazino-bonuslari": '''
<section class="section prose" style="margin-top:2rem">
<h2 id="reload-vip">Reload, VIP va turnir bonuslari</h2>
<p>Welcome dan keyin operatorlar <strong>reload</strong> (keyingi depozit foizi), <strong>VIP keshbek</strong> va <strong>turnir</strong> sovrinlarini taklif qiladi. FairPari reytingimizda #1 — chunki welcome 20,2 mln UZS + 150 FS to'rt bosqichda, sport alternativi 1,4 mln UZS, va muntazam PROMO yangilanadi.</p>
<h2 id="wagering-jadval">Wagering jadvali — qaysi o'yin qancha hisoblanadi</h2>
<table class="data-table"><thead><tr><th>O'yin turi</th><th>Hisob %</th><th>Eslatma</th></tr></thead>
<tbody>
<tr><td>Slotlar</td><td>100%</td><td>Asosiy wagering manbai</td></tr>
<tr><td>Live kazino</td><td>10–20%</td><td>Ruletka, blackjack</td></tr>
<tr><td>Sport (ekspress)</td><td>×5 alohida</td><td>Kazino welcome dan farqli</td></tr>
<tr><td>Stol o'yinlari</td><td>5–10%</td><td>PROMO ro'yxatini tekshiring</td></tr>
</tbody></table>
<h2 id="tanlash">Qanday bonus tanlash — 5 qadam</h2>
<ol><li>Maqsad: sport yoki kazino?</li><li>Wagering va muddatni solishtiring</li><li>Max bet va yechish limitlari</li><li>To'lov usuli (Humo/Payme) — <a href="../tolov-uz/">to'lovlar</a></li><li>Reytingdagi #1 — <a href="../fairpari/">FairPari sharhi</a></li></ol>
<p>To'liq FairPari qo'llanmasi: <a href="https://fairpari-casino-bonus.com/" rel="noopener">fairpari-casino-bonus.com</a> (batafsil welcome). Barcha bonus turlari: <a href="https://fairpari-casino-bonuses.com/kazino-bonuslari/" rel="noopener">FairPari bonuslari hub</a>.</p>
</section>''',
    "welcome-bonus": '''
<section class="section prose" style="margin-top:2rem">
<h2 id="top5">TOP-5 welcome bonus taqqoslash (2026)</h2>
<table class="data-table"><thead><tr><th>#</th><th>Operator</th><th>Welcome</th><th>Wagering</th></tr></thead>
<tbody>
<tr><td>1</td><td>FairPari</td><td>20,2 mln UZS + 150 FS</td><td>×35</td></tr>
<tr><td>2</td><td>1win</td><td>500% gacha paket</td><td>×30–×50</td></tr>
<tr><td>3</td><td>1xBet</td><td>1,3 mln UZS + FS</td><td>×35</td></tr>
<tr><td>4</td><td>Mostbet</td><td>125% + FS</td><td>×40</td></tr>
<tr><td>5</td><td>Melbet</td><td>100% + FS</td><td>×35</td></tr>
</tbody></table>
<h2 id="kalkulyator">Welcome kalkulyatori (taxminiy)</h2>
<p>Birinchi depozit 500 000 UZS + 100% welcome = 1 000 000 UZS balans (bonus shartlariga qarab). FairPari to'rt bosqichda maksimal 20,2 mln UZS + 150 FS — har bosqich alohida depozit talab qiladi. Batafsil: <a href="../fairpari/">FairPari vs raqobatchilar</a>.</p>
<h2 id="xatolar">Welcome olishdagi 5 xato</h2>
<ul><li>Kazino va sport bonusini aralashtirish</li><li>Max betdan oshish</li><li>Wagering muddatini o'tkazib yuborish</li><li>Noto'g'ri to'lov usuli (bonusga tatbiq etilmaydi)</li><li>Promokodni kiritmasdan depozit</li></ul>
</section>''',
    "depozitsiz-bonus": '''
<section class="section prose" style="margin-top:2rem">
<h2 id="miflar">Depozitsiz bonus miflari va haqiqat</h2>
<p><strong>Mif:</strong> har bir kazino 100% depozitsiz bonus beradi. <strong>Haqiqat:</strong> O'zbekistonda bu kam uchraydi; ko'pincha faqat ro'yxatdan o'tish FS yoki kichik freebet. FairPari da asosiy paket — <strong>depozitli welcome</strong>; depozitsiz aksiyalar PROMO da vaqtinchalik.</p>
<h2 id="fairpari-depozitsiz">FairPari da depozitsiz nima bor?</h2>
<p>Ro'yxatdan o'tish bonusi, turnir freebet, ba'zan verification FS — barchasi PROMO bo'limida. Doimiy «no deposit 1 mln» kabi va'dalar rasmiy kartochkada bo'lmasa, ishonmang.</p>
<h2 id="bozor">Bozor taqqoslash</h2>
<table class="data-table"><thead><tr><th>Operator</th><th>Depozitsiz</th><th>Izoh</th></tr></thead>
<tbody>
<tr><td>FairPari</td><td>Vaqtinchak PROMO</td><td>Asosiy — welcome depozitli</td></tr>
<tr><td>1win</td><td>Ba'zan FS</td><td>Shartlar o'zgaradi</td></tr>
<tr><td>1xBet</td><td>Kam</td><td>Freebet aksiyalar</td></tr>
</tbody></table>
<p>Hub: <a href="https://fairpari-casino-bonuses.com/depozitsiz-bonus/" rel="noopener">FairPari depozitsiz holat</a>.</p>
</section>''',
    "tolov-uz": '''
<section class="section prose" style="margin-top:2rem">
<h2 id="humo-payme">Humo, Uzcard, Payme, Click — jadval</h2>
<table class="data-table"><thead><tr><th>Usul</th><th>Min depozit</th><th>Tezlik</th><th>Bonus</th></tr></thead>
<tbody>
<tr><td>Humo</td><td>~15 000 UZS</td><td>Daqiqalar</td><td>Welcome qabul</td></tr>
<tr><td>Uzcard</td><td>~15 000 UZS</td><td>Daqiqalar</td><td>Welcome qabul</td></tr>
<tr><td>Payme</td><td>Operatorga qarab</td><td>Tez</td><td>Ha</td></tr>
<tr><td>Click</td><td>Operatorga qarab</td><td>Tez</td><td>Ha</td></tr>
<tr><td>Kripto (USDT)</td><td>Yuqori min</td><td>15–60 min</td><td>Ba'zan alohida</td></tr>
</tbody></table>
<h2 id="bonus-depozit">Bonus olish uchun to'g'ri depozit</h2>
<p>Promokod fa_1635 ni kiritib, keyin birinchi depozitni tanlangan usulda amalga oshiring. Bonus avtomatik yoki PROMO tasdiqlashidan keyin tushadi. Yechish — odatda o'sha usulga qaytadi (KYC dan keyin).</p>
</section>''',
    "faq": '''
<section class="section prose" style="margin-top:2rem">
<h2 id="faq-keng">Qo'shimcha savollar</h2>
<dl class="faq-list">
<dt>Eng yaxshi kazino bonusi O'zbekistonda qaysi?</dt>
<dd>Reytingimizda FairPari #1 — 20,2 mln UZS + 150 FS va UZS to'lovlar.</dd>
<dt>Welcome bonus necha kun amal qiladi?</dt>
<dd>Odatda 7–30 kun wagering uchun; operator PROMO da ko'rsatadi.</dd>
<dt>Humo bilan bonus olish mumkinmi?</dt>
<dd>Ha, FairPari va TOP-5 operatorlarning ko'pchiligi Humo qabul qiladi.</dd>
<dt>fairpari bonus qayerdan olish kerak?</dt>
<dd>To'liq qo'llanma — <a href="https://fairpari-casino-bonus.com/">EMD lендинг</a>; reyting konteksti — <a href="../fairpari/">/fairpari/</a>.</dd>
<dt>Depozitsiz bonus bormi?</dt>
<dd>Doimiy depozitsiz kam; <a href="../depozitsiz-bonus/">depozitsiz sahifa</a> — miflar va haqiqat.</dd>
<dt>1win yoki FairPari — qaysi biri?</dt>
<dd><a href="../1win/">1win sharhi</a> va <a href="../fairpari/">taqqoslash</a>.</dd>
</dl>
</section>''',
}

EXTRA_RU = {
    "kazino-bonuslari": '''
<section class="section prose" style="margin-top:2rem">
<h2 id="reload-vip">Reload, VIP и турнирные бонусы</h2>
<p>После welcome операторы дают reload, VIP-кешбек и турниры. FairPari #1 в рейтинге: 20,2 млн UZS + 150 FS в четыре этапа, спортивная альтернатива 1,4 млн UZS.</p>
<h2 id="wagering-jadval">Таблица вейджера</h2>
<table class="data-table"><thead><tr><th>Тип игры</th><th>Зачёт %</th></tr></thead>
<tbody><tr><td>Слоты</td><td>100%</td></tr><tr><td>Live</td><td>10–20%</td></tr><tr><td>Спорт</td><td>×5 отдельно</td></tr></tbody></table>
<p><a href="/ru/fairpari/">Обзор FairPari</a> · <a href="https://fairpari-casino-bonus.com/ru/">Полный гайд</a></p>
</section>''',
    "welcome-bonus": '''
<section class="section prose" style="margin-top:2rem">
<h2 id="top5">Сравнение TOP-5 welcome (2026)</h2>
<table class="data-table"><thead><tr><th>#</th><th>Оператор</th><th>Welcome</th></tr></thead>
<tbody><tr><td>1</td><td>FairPari</td><td>20,2 млн + 150 FS</td></tr><tr><td>2</td><td>1win</td><td>до 500%</td></tr><tr><td>3</td><td>1xBet</td><td>1,3 млн + FS</td></tr></tbody></table>
</section>''',
    "depozitsiz-bonus": '''
<section class="section prose" style="margin-top:2rem">
<h2 id="miflar">Мифы о бонусе без депозита</h2>
<p>Постоянный no deposit редок в UZ. FairPari — основной welcome с депозитом. Акции без депозита — временно в PROMO.</p>
</section>''',
    "tolov-uz": '''
<section class="section prose" style="margin-top:2rem">
<h2 id="humo-payme">Humo, Payme, Click</h2>
<table class="data-table"><thead><tr><th>Метод</th><th>Мин.</th><th>Бонус</th></tr></thead>
<tbody><tr><td>Humo</td><td>~15 000</td><td>Да</td></tr><tr><td>Payme</td><td>по оператору</td><td>Да</td></tr></tbody></table>
</section>''',
    "faq": '''
<section class="section prose" style="margin-top:2rem">
<dl class="faq-list">
<dt>Лучший бонус казино в Узбекистане?</dt>
<dd>FairPari #1 — 20,2 млн UZS + 150 FS.</dd>
<dt>Где полный гайд FairPari?</dt>
<dd><a href="https://fairpari-casino-bonus.com/ru/">fairpari-casino-bonus.com/ru/</a></dd>
</dl>
</section>''',
}


def append_before_main_close(path: Path, block: str, marker_id: str):
    text = path.read_text(encoding='utf-8')
    if marker_id in text:
        return False
    text = text.replace('</main>', block + '\n</main>', 1)
    path.write_text(text, encoding='utf-8')
    return True


def fix_legal_titles():
    for f in ROOT.glob('*.html'):
        if f.name not in ('cookie-siyosati.html', 'foydalanish-shartlari.html', 'masuliyatli-oyin.html', 'maxfiylik-siyosati.html'):
            continue
        t = f.read_text(encoding='utf-8')
        t2 = re.sub(
            r'<title>([^<|]+)\s*—\s*FairPari UZ\s*\|\s*casino-bonuses-uz\.com</title>',
            r'<title>\1 — Casino Bonuses UZ</title>',
            t
        )
        t2 = re.sub(
            r'<title>([^<|]+)\s*\|\s*casino-bonuses-uz\.com</title>',
            r'<title>\1 — Casino Bonuses UZ</title>',
            t2
        )
        if t2 != t:
            f.write_text(t2, encoding='utf-8')
            print(f'legal title: {f.name}')
    for sub in ['cookie-siyosati', 'foydalanish-shartlari', 'masuliyatli-oyin', 'maxfiylik-siyosati',
                'ru/politika-cookie', 'ru/politika-konfidentsialnosti', 'ru/usloviya-ispolzovaniya', 'ru/otvetstvennaya-igra']:
        p = ROOT / sub / 'index.html'
        if not p.exists():
            continue
        t = p.read_text(encoding='utf-8')
        t2 = re.sub(r'casino-bonuses-uz\.com', 'Casino Bonuses UZ', t)
        t2 = re.sub(r'FairPari UZ \| Casino Bonuses UZ', 'Casino Bonuses UZ', t2)
        if t2 != t:
            p.write_text(t2, encoding='utf-8')
            print(f'legal title: {sub}')


def main():
    for slug, block in EXTRA_UZ.items():
        p = ROOT / slug / 'index.html'
        marker = f'id="cbz-extra-{slug}"'
        blk = block.replace('<section class="section prose"', f'<section class="section prose" {marker.replace("id=", "data-section=")}', 1)
        blk = re.sub(r'<section class="section prose" data-section="([^"]+)"', f'<section class="section prose" id="cbz-extra-{slug}"', blk, count=1)
        if append_before_main_close(p, blk, f'id="cbz-extra-{slug}"'):
            print(f'UZ expanded: {slug}')

    for slug, block in EXTRA_RU.items():
        p = ROOT / 'ru' / slug / 'index.html'
        if append_before_main_close(p, block.replace('<section class="section prose"', f'<section class="section prose" id="cbz-ru-extra-{slug}"', 1), f'id="cbz-ru-extra-{slug}"'):
            print(f'RU expanded: {slug}')

    fix_legal_titles()


if __name__ == '__main__':
    main()
