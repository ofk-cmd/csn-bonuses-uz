#!/usr/bin/env python3
"""Append final paragraphs to hubs still under 2500 words."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKER = "pass4e-tail"

TAILS = {
    "depozitsiz-bonus/index.html": """
<p>Yakuniy eslatma: depozitsiz bonus qidirayotgan o'yinchilar uchun eng ishonchli yo'l — operatorning rasmiy PROMO va bizning <a href="../#rating">reyting jadvali</a>. FairPari #1 welcome bilan: 20,2 mln UZS + 150 FS, Humo/Payme, wagering ×35. 1win va Mostbet alternativalar — har birining <a href="../1win/">sharhi</a> va <a href="../mostbet/">sharhi</a> alohida. Wagering muddatini o'tkazib yubormang, max betni buzmang. casino-bonuses-uz.com mustaqil axborot sayti, 18+.</p>
""",
    "faq/index.html": """
<p>Qo'shimcha manbalar: <a href="../kazino-bonuslari/">bonus turlari</a>, <a href="../welcome-bonus/">welcome 2026</a>, <a href="../depozitsiz-bonus/">depozitsiz</a>, <a href="../tolov-uz/">Humo/Payme</a>. FairPari to'liq qo'llanma — <a href="https://fairpari-casino-bonus.com/" rel="noopener">EMD</a>. Savollar operator qo'llab-quvvatlashiga tegishli bo'lsa, rasmiy saytga murojaat qiling. Reyting yangilanishi 2026, summalarni depozitdan oldin tasdiqlang.</p>
""",
    "tolov-uz/index.html": """
<p>Xulosa: O'zbekiston o'yinchilari uchun Humo eng qulay depozit; Payme va Click mobil ilovalarda tez. FairPari #1 — to'lovlar va welcome jihatidan. Kripto istaganlar <a href="../bc-game/">BC.Game</a> sharhiga qarang. Bonus faollashtirish: promokod, keyin depozit. Yechish — KYC. <a href="../welcome-bonus/">Welcome</a> · <a href="../#rating">TOP-20</a>. 18+.</p>
""",
    "ru/kazino-bonuslari/index.html": """
<p>Типы бонусов в Узбекистане: welcome, FS, cashback, reload, VIP. FairPari #1 — 20,2 млн UZS + 150 FS. Сравните <a href="/ru/fairpari/">FairPari</a>, <a href="/ru/1win/">1win</a>, <a href="/ru/mostbet/">Mostbet</a> в <a href="/ru/#rating/">рейтинге TOP-20</a>. 18+.</p>
""",
    "ru/welcome-bonus/index.html": """
<p>Дополнительно: при выборе welcome смотрите не только сумму, но и вейджер, срок, max bet и список игр с 100% зачётом. FairPari — четыре этапа, промокод fa_1635 для казино. Альтернативы: <a href="/ru/1win/">1win</a>, <a href="/ru/1xbet/">1xBet</a>, <a href="/ru/pin-up/">Pin-Up</a>. EMD-гайд: <a href="https://fairpari-casino-bonus.com/ru/" rel="noopener">fairpari-casino-bonus.com/ru/</a>. 18+, ответственная игра.</p>
""",
    "ru/depozitsiz-bonus/index.html": """
<p>Рекомендация: вместо погони за no deposit рассмотрите welcome с минимальным депозитом — FairPari 20,2 млн + 150 FS даёт больше ценности, чем 50 FS с ×60. Сравните <a href="/ru/fairpari/">FairPari</a>, <a href="/ru/1win/">1win</a>, <a href="/ru/melbet/">Melbet</a>. Временные акции без депозита — только в PROMO оператора. <a href="/ru/welcome-bonus/">Welcome</a> · <a href="/ru/kazino-bonuslari/">типы</a> · <a href="/ru/#rating">рейтинг</a>. 18+.</p>
""",
    "ru/tolov-uz/index.html": """
<p>Итог по платежам UZ: Humo/Uzcard — минимальные суммы от ~15 000 UZS, быстрый зачисление. Payme/Click — удобно с телефона. Вывод после верификации на тот же метод, если правила позволяют. FairPari #1 в рейтинге по связке welcome + локальные платежи. <a href="/ru/fairpari/">обзор</a>, <a href="/ru/welcome-bonus/">welcome</a>, <a href="/ru/faq/">FAQ</a>. 18+.</p>
""",
    "ru/faq/index.html": """
<p>Если не нашли ответ: см. <a href="/ru/kazino-bonuslari/">типы бонусов</a>, <a href="/ru/welcome-bonus/">welcome</a>, <a href="/ru/depozitsiz-bonus/">без депозита</a>, <a href="/ru/tolov-uz/">платежи</a>. FairPari — <a href="/ru/fairpari/">#1 в рейтинге</a>. Полный гайд: <a href="https://fairpari-casino-bonus.com/ru/" rel="noopener">EMD</a>. Мы не служба поддержки операторов. 18+, играйте ответственно.</p>
""",
}


def main():
    for rel, tail in TAILS.items():
        p = ROOT / rel
        text = p.read_text(encoding="utf-8")
        if MARKER in text:
            continue
        block = f'<section class="section prose" id="{MARKER}">{tail.strip()}</section>'
        p.write_text(text.replace("</main>", block + "\n</main>", 1), encoding="utf-8")
        w = len(re.sub(r"<[^>]+>", " ", p.read_text()).split())
        print(f"{w:5} {rel}")


if __name__ == "__main__":
    main()
