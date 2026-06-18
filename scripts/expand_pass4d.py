#!/usr/bin/env python3
"""Last mile hub expansion."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EXTRA = {
    "depozitsiz-bonus/index.html": "<p>FairPari, 1win, Mostbet, Melbet va 1xBet — <a href=\"../#rating\">reyting</a>da. Har bir operator PROMO da depozitsiz aksiyalarni alohida e'lon qiladi; doimiy katta paketlar kam. Welcome bilan solishtiring: 20,2 mln UZS + 150 FS FairPari da. Wagering, muddat va max bet — har safar tekshiring. Biz mustaqil portalmiz, 18+.</p>",
    "faq/index.html": "<p>Savol bo'lsa — <a href=\"../fairpari/\">FairPari</a>, <a href=\"../welcome-bonus/\">welcome</a>, <a href=\"../tolov-uz/\">to'lovlar</a> sahifalariga o'ting. Google UZ bo'yicha «kazino bonuslari o'zbekiston», «eng yaxshi kazino bonuslari» — reytingimiz shu so'rovlar uchun optimallashtirilgan. Yangilanish: 2026.</p>",
    "tolov-uz/index.html": "<p>FairPari #1 to'lovlar va welcome bo'yicha. 1win, Mostbet ham Humo qabul qiladi. Kripto — BC.Game. <a href=\"../#rating\">To'liq jadval</a>. 18+.</p>",
    "ru/kazino-bonuslari/index.html": "<p>Обновлено 2026. FairPari, 1win, 1xBet — <a href=\"/ru/#rating\">рейтинг</a>. 18+.</p>",
    "ru/welcome-bonus/index.html": "<p>Сравните welcome у <a href=\"/ru/fairpari/\">FairPari</a>, <a href=\"/ru/1win/\">1win</a>, <a href=\"/ru/mostbet/\">Mostbet</a>. Промокод fa_1635 для казино-пакета FairPari. Не превышайте max bet при отыгрыше. Первый вывод — верификация. Мы не оператор. 18+, <a href=\"/ru/otvetstvennaya-igra/\">ответственная игра</a>.</p>",
    "ru/depozitsiz-bonus/index.html": "<p>В рейтинге TOP-20 сравните welcome-пакеты: FairPari 20,2 млн + 150 FS лидирует над «бесплатными» акциями с жёстким вейджером. 1win, 1xBet, Mostbet иногда дают FS за регистрацию — условия в PROMO. Перед игрой проверьте лицензию и лимиты. <a href=\"/ru/welcome-bonus/\">Welcome-гайд</a>, <a href=\"/ru/kazino-bonuslari/\">типы бонусов</a>, <a href=\"/ru/#rating\">таблица</a>. casino-bonuses-uz.com — информационный портал, 18+.</p>",
    "ru/tolov-uz/index.html": "<p>Для активации welcome: регистрация, промокод при необходимости, депозит Humo/Payme/Click. FairPari поддерживает основные методы UZ. Вывод на ту же систему после KYC. Сравните <a href=\"/ru/fairpari/\">FairPari</a> и <a href=\"/ru/1win/\">1win</a> в рейтинге. Избегайте фишинга — только официальный домен оператора. 18+, играйте ответственно. <a href=\"/ru/welcome-bonus/\">Welcome</a> · <a href=\"/ru/faq/\">FAQ</a>.</p>",
    "ru/faq/index.html": "<p>Дополнительно: wagering ×35 у FairPari — стандарт рынка; слоты 100%, live меньше. Срок отыгрыша 7–30 дней. Спортивный welcome — отдельный пакет. Вопросы по оператору — в поддержку бренда, не на этот сайт. <a href=\"/ru/kazino-bonuslari/\">Типы бонусов</a>, <a href=\"/ru/depozitsiz-bonus/\">без депозита</a>, <a href=\"/ru/tolov-uz/\">платежи</a>. 18+.</p>",
}


def main():
    for rel, para in EXTRA.items():
        p = ROOT / rel
        text = p.read_text(encoding="utf-8")
        if "pass4d-final" in text:
            continue
        block = f'<section class="section prose" id="pass4d-final">{para}</section>'
        p.write_text(text.replace("</main>", block + "\n</main>", 1), encoding="utf-8")
        print(rel)


if __name__ == "__main__":
    main()
