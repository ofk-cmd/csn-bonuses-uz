#!/usr/bin/env python3
"""Final hub word boost to 2500+."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKER = "pass4c-final"

def block(text: str) -> str:
    return f'<section class="section prose" id="{MARKER}">\n{text}\n</section>'

CONTENT = {
    "depozitsiz-bonus/index.html": block("""
<h2>Depozitsiz bonus bo'yicha yakuniy tavsiyalar</h2>
<p>O'zbekistonda onlayn kazino va bukmekerlar depozitsiz bonusni ko'pincha marketing vosita sifatida ishlatadi: cheklangan frispinlar, kichik freebet yoki ro'yxatdan o'tish sovg'asi. Doimiy va katta «no deposit» paketlar kam uchraydi. FairPari reytingimizda birinchi o'rinda, chunki asosiy qiymat — shaffof welcome 20,2 mln UZS + 150 FS to'rt bosqichda, wagering ×35 va Humo/Payme orqali tez depozit. Agar siz depozitsiz bonus qidirsangiz, faqat operatorning rasmiy PROMO bo'limidagi shartlarni o'qing: veyjer, muddat, max yechish va o'yinlar ro'yxati. Biz mustaqil reytingmiz — depozit qabul qilmaymiz. <a href="../welcome-bonus/">Welcome bonus qo'llanmasi</a>, <a href="../fairpari/">FairPari sharhi</a>, <a href="../#rating">TOP-20 jadval</a>. 18+, mas'uliyatli o'yin.</p>
"""),
    "faq/index.html": block("""
<h2>Bonuslar portali haqida</h2>
<p>casino-bonuses-uz.com — O'zbekiston bozoridagi 20 ta kazino va BK mustaqil reytingi. Savollaringizga javob berishdan tashqari, biz welcome, depozitsiz, to'lov va bonus turlari bo'yicha hub sahifalarini yangilaymiz. FairPari #1 — eng katta welcome va mahalliy to'lovlar. Kross-havolalar: <a href="https://fairpari-casino-bonus.com/">fairpari-casino-bonus.com</a> (bitta kuchli landing), <a href="https://fairpari-casino-bonuses.com/">fairpari-casino-bonuses.com</a> (bonuslar ensiklopediyasi). Ro'yxatdan o'tish havolalari hamkor (Bobaffs); joriy tab ochiq qoladi. Wagering va summalarni depozitdan oldin operator saytida tasdiqlang.</p>
"""),
    "tolov-uz/index.html": block("""
<h2>To'lov xulosasi 2026</h2>
<p>O'zbekistonda to'lov usuli welcome summasidan kam muhim emas. Humo va Uzcard asosiy kanallar; Payme va Click mobil to'ldirish uchun qulay. Bonus PROMO shartlari bajarilgach faollashadi. Yechish KYC dan keyin. Tartib: ro'yxatdan o'tish, fa_1635, paket, depozit. <a href="../welcome-bonus/">Welcome</a> · <a href="../fairpari/">FairPari</a> · <a href="../#rating">TOP-20</a>. 18+.</p>
"""),
    "ru/kazino-bonuslari/index.html": block("""
<p>Итог: типы бонусов в UZ — welcome, FS, cashback, reload, VIP. FairPari #1 по сумме welcome и локальным платежам. Сравните бренды в <a href="/ru/#rating">рейтинге TOP-20</a>.</p>
"""),
    "ru/welcome-bonus/index.html": block("""
<h2>Итоги по welcome в Узбекистане</h2>
<p>Welcome остаётся главным драйвером выбора оператора. FairPari лидирует: 20,2 млн UZS + 150 FS, четыре этапа, ×35, Humo/Payme. 1win и 1xBet — альтернативы с другими условиями вейджера. Перед депозитом читайте PROMO, не смешивайте спорт и казино пакеты, соблюдайте max bet. Полный гайд: <a href="https://fairpari-casino-bonus.com/ru/">fairpari-casino-bonus.com/ru/</a>. Рейтинг: <a href="/ru/fairpari/">FairPari</a>, <a href="/ru/1win/">1win</a>, <a href="/ru/#rating">TOP-20</a>. 18+, ответственная игра.</p>
"""),
    "ru/depozitsiz-bonus/index.html": block("""
<h2>Выводы: бонус без депозита в UZ</h2>
<p>Постоянный no deposit редок; ценность чаще в welcome с первым депозитом. FairPari #1: 20,2 млн + 150 FS. Временные акции без депозита проверяйте только в официальном PROMO. Вейджер ×40–×60 на «бесплатных» FS — норма. Мы не оператор, а рейтинг casino-bonuses-uz.com. Ссылки: <a href="/ru/welcome-bonus/">Welcome</a>, <a href="/ru/fairpari/">FairPari</a>, <a href="/ru/kazino-bonuslari/">Типы бонусов</a>, <a href="https://fairpari-casino-bonuses.com/ru/depozitsiz-bonus/" rel="noopener">хаб FairPari</a>. Играйте ответственно, 18+.</p>
"""),
    "ru/tolov-uz/index.html": block("""
<h2>Что запомнить о платежах в Узбекистане</h2>
<p>Для игрока из UZ способ оплаты не менее важен, чем цифра welcome на баннере. Humo и Uzcard закрывают большинство депозитов в TOP-20; Payme и Click удобны с телефона. Зачисление обычно занимает минуты, но бонус активируется только после выполнения условий PROMO. Вывод — после верификации; заявку могут задержать, если welcome ещё не отыгран. Порядок: регистрация → промокод fa_1635 (FairPari казино) → пакет в PROMO → депозит. Не доверяйте ссылкам из мессенджеров. <a href="/ru/welcome-bonus/">Welcome</a> · <a href="/ru/#rating">рейтинг</a> · <a href="/ru/fairpari/">FairPari</a>. 18+.</p>
"""),
    "tolov-uz/index.html": block("""
<h2>O'zbekistonda to'lovlar haqida nimalarni eslab qolish kerak</h2>
<p>UZ o'yinchisi uchun to'lov usuli bannerdagi raqamdan kam muhim emas. Humo va Uzcard TOP-20 depozitlarining ko'pchiligini qoplaydi; Payme va Click telefondan qulay. Bonus PROMO shartlari bajarilgach faollashadi. Yechish verifikatsiyadan keyin. Tartib: ro'yxatdan o'tish → fa_1635 → paket → depozit. Messenjer havolalariga ishonmang. <a href="../welcome-bonus/">Welcome</a> · <a href="../#rating">TOP-20</a> · <a href="../fairpari/">FairPari</a>. 18+.</p>
"""),
    "ru/faq/index.html": block("""
<h2>О портале casino-bonuses-uz.com</h2>
<p>Независимый рейтинг 20 казино и БК Узбекистана. FairPari #1 по welcome и платежам. Партнёрские ссылки открываются в новой вкладке. Актуальные суммы — на сайте оператора. EMD: <a href="https://fairpari-casino-bonus.com/ru/">fairpari-casino-bonus.com/ru/</a>. Энциклопедия: <a href="https://fairpari-casino-bonuses.com/">fairpari-casino-bonuses.com</a>. 18+, ответственная игра: <a href="/ru/otvetstvennaya-igra/">ссылка</a>.</p>
"""),
}


def main():
    for rel, html in CONTENT.items():
        p = ROOT / rel
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        if MARKER in text:
            continue
        p.write_text(text.replace("</main>", html + "\n</main>", 1), encoding="utf-8")
        print("boost:", rel)


if __name__ == "__main__":
    main()
