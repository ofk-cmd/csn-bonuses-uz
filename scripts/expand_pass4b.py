#!/usr/bin/env python3
"""Second pass hub expansion — target 2500+ words on remaining hubs."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKER = 'id="pass4b-expand"'

BLOCK_UZ = {
    "depozitsiz-bonus": '''
<section class="section prose" id="pass4b-expand">
<h2>Operatorlar bo'yicha depozitsiz holat (2026)</h2>
<p>FairPari, 1win, 1xBet, Mostbet va Melbet — reytingimizdagi TOP-5. Depozitsiz takliflar odatda cheklangan: 20–50 FS yoki kichik freebet, wagering ×40–×60. Doimiy «1 mln UZS bepul» kamdan-kam rasmiy PROMO da tasdiqlanadi. Asosiy strategiya — birinchi depozit bilan welcome olish: FairPari 20,2 mln + 150 FS.</p>
<p><a href="../fairpari/">FairPari</a> · <a href="../1win/">1win</a> · <a href="../welcome-bonus/">Welcome</a> · <a href="../kazino-bonuslari/">Bonus turlari</a> · <a href="../#rating">Reyting</a>.</p>
</section>''',
    "tolov-uz": '''
<section class="section prose" id="pass4b-expand">
<h2>Xavfsiz to'lov va KYC</h2>
<p>Birinchi yechishda pasport/ID va ba'zan selfi talab qilinadi — bu normal. Faqat operatorning rasmiy sayti yoki ilovasida to'lov qiling; Telegram-botlarga ishonmang. Humo va Payme orqali depozit qilganda bonus avtomatik tushishi uchun avval promokod fa_1635 ni kiriting.</p>
<p>Mas'uliyatli o'yin: limitlar o'rnating, 18+. <a href="/masuliyatli-oyin/">Mas'uliyatli o'yin</a> · <a href="../fairpari/">FairPari to'lovlar</a>.</p>
</section>''',
    "faq": '''
<section class="section prose" id="pass4b-expand">
<h2>Tez-tez so'raladigan savollar (qo'shimcha)</h2>
<p>Reytingimiz mustaqil — operator emasmiz. Bobaffs hamkor havolalari orqali ro'yxatdan o'tish mumkin; shartlar operator saytida. Wagering, max bet va muddat har bonus uchun alohida — PROMO ni o'qing.</p>
<p>Kross-havolalar: <a href="https://fairpari-casino-bonus.com/">FairPari bonus EMD</a> · <a href="https://fairpari-casino-bonuses.com/">FairPari bonuslar ensiklopediyasi</a> · <a href="../kazino-bonuslari/">UZ bonus turlari</a>.</p>
</section>''',
}

BLOCK_RU = {
    "kazino-bonuslari": '''
<section class="section prose" id="pass4b-expand">
<p>Дополнительно: reload-бонусы обычно 25–50% на второй депозит, VIP — персональный кешбек. Турниры дают призовой фонд в UZS. Сравните <a href="/ru/fairpari/">FairPari</a>, <a href="/ru/pin-up/">Pin-Up</a>, <a href="/ru/linebet/">Linebet</a> в <a href="/ru/#rating">рейтинге</a>.</p>
</section>''',
    "welcome-bonus": '''
<section class="section prose" id="pass4b-expand">
<h2>Ошибки при активации welcome</h2>
<p>Не смешивайте спорт и казино пакеты. Не превышайте max bet. Успейте отыграть в срок. Проверьте, что депозит прошёл тем методом, который принимает бонус. FairPari: промокод fa_1635, четыре этапа welcome.</p>
</section>''',
    "depozitsiz-bonus": '''
<section class="section prose" id="pass4b-expand">
<h2>Сравнение no deposit по операторам</h2>
<p>FairPari — основной welcome с депозитом; без депозита — временные PROMO. 1win и 1xBet иногда дают FS за регистрацию — читайте вейджер. Mostbet и Melbet — акции в приложении. Полный рейтинг: <a href="/ru/#rating">TOP-20</a>.</p>
</section>''',
    "tolov-uz": '''
<section class="section prose" id="pass4b-expand">
<h2>KYC и безопасность платежей</h2>
<p>Первый вывод — верификация паспорта. Используйте только официальный сайт оператора. Humo/Payme — быстрые депозиты для welcome. Не переводите деньги «менеджерам» в мессенджерах.</p>
</section>''',
    "faq": '''
<section class="section prose" id="pass4b-expand">
<h2>Ещё вопросы по бонусам UZ</h2>
<p>Мы не оператор — информационный рейтинг. Ссылки на регистрацию — партнёрские. Актуальные суммы welcome сверяйте на сайте бренда перед депозитом. 18+, играйте ответственно.</p>
<p><a href="/ru/otvetstvennaya-igra/">Ответственная игра</a> · <a href="https://fairpari-casino-bonus.com/ru/">гайд FairPari</a>.</p>
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
    for slug, block in BLOCK_UZ.items():
        p = ROOT / slug / "index.html"
        if p.exists() and inject(p, block):
            print("UZ:", slug)
    for slug, block in BLOCK_RU.items():
        p = ROOT / "ru" / slug / "index.html"
        if p.exists() and inject(p, block):
            print("RU:", slug)


if __name__ == "__main__":
    main()
