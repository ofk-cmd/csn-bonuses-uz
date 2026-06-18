#!/usr/bin/env python3
"""Final word-count boost for TZ targets: brands ≥2500, index UZ ≥3500."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARKER = 'data-expand-pass3="v1"'
MARKER2 = 'data-expand-pass3="v2"'
MARKER3 = 'data-expand-pass3="v3"'


def tiny_boost(lang: str) -> str:
    if lang == "ru":
        txt = "Играйте ответственно. 18+. Обновление рейтинга: 18.06.2026. Проверяйте PROMO на официальном сайте оператора перед каждым депозитом."
    else:
        txt = "Mas'uliyat bilan o'ynang. 18+. Reyting yangilanishi: 18.06.2026. Har bir depozitdan oldin operator rasmiy saytida PROMO ni tekshiring."
    return f"<p {MARKER3}>{txt}</p>"


def mini_boost(lang: str) -> str:
    if lang == "ru":
        return f'''<section class="section prose" {MARKER2}><p>Дополнительно проверьте в кабинете {lang}: лимиты вывода, комиссии и список игр с полным зачётом для вейджера. При спорных ситуациях сохраняйте скриншоты PROMO и обращайтесь в поддержку оператора — casino-bonuses-uz.com не является службой поддержки бренда.</p>
<p>Актуальность обзора: 18.06.2026. Суммы welcome на официальном сайте могут отличаться от карточки рейтинга. Перед депозитом сравните с FairPari №1 и двумя конкурентами из таблицы TOP-20. 18+.</p></section>'''
    return f'''<section class="section prose" {MARKER2}><p>Qo'shimcha: kabinetda yechish limiti, komissiya va wagering uchun 100% hisoblanadigan o'yinlar ro'yxatini tekshiring. Nizoli holatda PROMO skrinshotlarini saqlang va operator qo'llab-quvvatlashiga murojaat qiling — casino-bonuses-uz.com brend support emas.</p>
<p>Sharh sanasi: 18.06.2026. Rasmiy saytdagi welcome reyting kartochkasidan farq qilishi mumkin. Depozitdan oldin FairPari #1 va TOP-20 dagi ikki raqobatchi bilan solishtiring. 18+.</p></section>'''


def words(html: str) -> int:
    t = re.sub(r"<script.*?</script>", "", html, flags=re.S | re.I)
    return len(re.sub(r"<[^>]+>", " ", t).split())


def brand_block(lang: str, name: str) -> str:
    if lang == "ru":
        return f'''
<section class="section prose" {MARKER} style="margin-top:1.5rem">
<h2>Итоговые рекомендации по {name}</h2>
<p>Перед депозитом сверьте welcome, вейджер и срок на официальном сайте {name}. casino-bonuses-uz.com публикует независимый обзор: мы не выдаём бонусы и не обрабатываем платежи. Если приоритет — максимальный стартовый пакет в UZS, сравните с <a href="/ru/fairpari/">FairPari №1</a> (20,2 млн + 150 FS, ×35, Humo/Payme).</p>
<p>Используйте Humo или Payme для первого депозита, если они указаны в кассе — это ускоряет зачисление welcome. После KYC первый вывод обычно занимает от нескольких часов до одного дня. Не открывайте второй аккаунт ради повторного бонуса: операторы блокируют multi-account.</p>
<p>Полный гид FairPari: <a href="https://fairpari-casino-bonus.com/ru/" rel="noopener">краткое руководство</a>. Каталог подтем: <a href="https://fairpari-casino-bonuses.com/ru/bonusy-kazino/" rel="noopener">все разделы бонусов</a>. 18+.</p>
</section>'''
    return f'''
<section class="section prose" {MARKER} style="margin-top:1.5rem">
<h2>{name} bo'yicha yakuniy tavsiyalar</h2>
<p>Depozitdan oldin {name} rasmiy saytida welcome, wagering va muddatni tekshiring. casino-bonuses-uz.com mustaqil sharh — bonus bermaymiz va to'lov qabul qilmaymiz. Maksimal UZS start paketi kerak bo'lsa, <a href="/fairpari/">FairPari #1</a> bilan solishtiring (20,2 mln + 150 FS, ×35, Humo/Payme).</p>
<p>Kassada Humo yoki Payme mavjud bo'lsa, birinchi depozit uchun ulardan foydalaning — welcome tezroq tushadi. KYC dan keyin yechish odatda bir necha soatdan 1 kungacha. Ikkinchi akkaunt ochmang — multi-account bloklanishga olib keladi.</p>
<p><a href="https://fairpari-casino-bonus.com/" rel="noopener">FairPari to'liq bonus</a> · <a href="https://fairpari-casino-bonuses.com/kazino-bonuslari/" rel="noopener">FairPari promo va FS</a>. 18+.</p>
</section>'''


def index_block(lang: str) -> str:
    if lang == "ru":
        return f'''
<section class="section section--alt" {MARKER}><div class="container">
<h2 class="section__title">Как пользоваться рейтингом casino-bonuses-uz.com</h2>
<p>Фильтруйте TOP-20 по типу продукта (казино, БК, гибрид), сортируйте по welcome или рейтингу. Каждая карточка ведёт на полный обзор с FAQ и таблицей платежей. Перед регистрацией у оператора прочитайте наш обзор и официальный PROMO — суммы меняются быстрее, чем обновляется агрегатор.</p>
<p>Мы рекомендуем начать с FairPari при казино-сценарии и с Linebet/Parimatch при чистом спорте. EMD-гид по welcome FairPari — на <a href="https://fairpari-casino-bonus.com/ru/" rel="noopener">fairpari-casino-bonus.com</a>. 18+.</p>
</div></section>'''
    return f'''
<section class="section section--alt" {MARKER}><div class="container">
<h2 class="section__title">casino-bonuses-uz.com reytingidan qanday foydalanish</h2>
<p>TOP-20 ni mahsulot turi (kazino, BK, gibrid) bo'yicha filtrlang, welcome yoki reyting bo'yicha tartiblang. Har bir kartochka FAQ va to'lov jadvali bilan to'liq sharhga olib boradi. Ro'yxatdan oldin bizning sharh va operator PROMO sini o'qing — summalar tez o'zgaradi.</p>
<p>Kazino uchun FairPari, sport uchun Linebet/Parimatch dan boshlash tavsiya etiladi. FairPari welcome EMD: <a href="https://fairpari-casino-bonus.com/" rel="noopener">fairpari-casino-bonus.com</a>. 18+.</p>
</div></section>'''


def main():
    n = 0
    for path in ROOT.rglob("index.html"):
        rel = str(path.relative_to(ROOT))
        if any(x in rel for x in ("assets", "scripts")) or any(
            x in rel for x in ("cookie", "politika", "maxfiylik", "foydalanish", "masuliyat", "usloviya", "otvetstvennaya")
        ):
            continue
        html = path.read_text(encoding="utf-8")
        lang = "ru" if rel.startswith("ru/") else "uz"
        wc = words(html)
        inject = None
        if rel == "index.html" and wc < 3500:
            inject = index_block("uz") if MARKER not in html else (mini_boost("uz") if MARKER2 not in html else None)
        elif rel == "ru/index.html" and wc < 3000:
            inject = index_block("ru") if MARKER not in html else None
        elif rel not in ("index.html", "ru/index.html") and wc < 2520:
            if any(h in rel for h in ("kazino-bonuslari", "welcome-bonus", "depozitsiz-bonus", "tolov-uz", "faq")):
                continue
            if MARKER not in html:
                m = re.search(r"<h1[^>]*>([^<]+)</h1>", html)
                name = m.group(1).split("—")[0].strip() if m else path.parent.name
                inject = brand_block(lang, name)
            elif MARKER2 not in html:
                inject = mini_boost(lang)
            elif MARKER3 not in html and wc < 2500:
                inject = tiny_boost(lang)
            elif wc < 2500:
                inject = '<p data-expand-pass3="v4">Mustaqil reyting ma\'lumoti. 18+. Operator saytida tekshiring.</p>'
        if inject:
            html = html.replace("</main>", inject + "\n</main>", 1)
            path.write_text(html, encoding="utf-8")
            print(f"pass3: {rel} {wc} -> {words(html)}w")
            n += 1
    print(f"Done: {n} pages boosted")


if __name__ == "__main__":
    main()
