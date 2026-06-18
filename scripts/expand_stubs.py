#!/usr/bin/env python3
"""Expand 6 stub pages on casino-bonuses-uz.com to full layout + 200+ words."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://casino-bonuses-uz.com"

def shell(slug, title, desc, h1, breadcrumb, schema_json, body_html, schema_type="Article"):
    ru_slug = slug
    canonical = f"{DOMAIN}/{slug}/"
    return f'''<!DOCTYPE html>
<html lang="uz-UZ">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<meta name="theme-color" content="#ffffff"/>
<meta name="robots" content="index, follow, max-image-preview:large"/>
<title>{title}</title>
<meta name="description" content="{desc}"/>
<link rel="icon" href="../assets/favicon.svg" type="image/svg+xml"/>
<link rel="stylesheet" href="../css/style.css?v=20260618"/>
<link rel="stylesheet" href="../css/fairpari-light-theme.css?v=20260618"/>
<link rel="canonical" href="{canonical}"/>
<link rel="alternate" hreflang="uz-UZ" href="{canonical}"/>
<link rel="alternate" hreflang="ru-UZ" href="{DOMAIN}/ru/{ru_slug}/"/>
<link rel="alternate" hreflang="x-default" href="{canonical}"/>
<meta property="og:type" content="website"/>
<meta property="og:site_name" content="Casino Bonuses UZ"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:url" content="{canonical}"/>
<meta property="og:image" content="{DOMAIN}/assets/hero-bonus-light.webp"/>
<meta property="og:locale" content="uz_UZ"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{title}"/>
<meta name="twitter:description" content="{desc}"/>
<script type="application/ld+json">{schema_json}</script>
</head>
<body class="site-fairpari-light">
<a class="skip-link" href="#main">Asosiy kontentga o'tish</a>
<header class="site-header"><div class="site-header__inner">
<a class="brand" href="../"><img class="brand__logo-img" src="../assets/logo-fairpari.svg" alt="Casino Bonuses UZ — kazino bonuslari reytingi" width="132" height="20" loading="eager"/></a>
<nav class="nav-desktop" aria-label="Asosiy menyu">
<a href="../#rating">Reyting</a>
<a href="../kazino-bonuslari/">Bonus turlari</a>
<a href="../welcome-bonus/">Welcome</a>
<a href="../depozitsiz-bonus/">Depozitsiz</a>
<a href="../tolov-uz/">To'lovlar</a>
<a href="../fairpari/">FairPari</a>
<a href="../faq/">FAQ</a>
<a class="lang-switch" href="/ru/{ru_slug}/" hreflang="ru-UZ" style="margin-left:12px;font-weight:600">RU</a>
</nav>
<button type="button" class="btn btn--gold js-go-partner">Bonus olish</button>
</div></header>
<main id="main" class="container" style="padding:2rem 1rem">
<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="../">Bosh sahifa</a> / <span>{breadcrumb}</span></nav>
{body_html}
</main>
<nav class="footer-links footer-links--audit" aria-label="Sayt bo'limlari">
<a href="../">Bosh sahifa</a>
<a href="../kazino-bonuslari/">Kazino bonuslari</a>
<a href="../welcome-bonus/">Welcome bonus</a>
<a href="../depozitsiz-bonus/">Depozitsiz bonus</a>
<a href="../tolov-uz/">To'lovlar UZ</a>
<a href="../fairpari/">FairPari sharhi</a>
<a href="../faq/">FAQ</a>
</nav>
<footer class="site-footer"><div class="container">
<nav class="footer-legal">
<a href="/maxfiylik-siyosati">Maxfiylik</a>
<a href="/foydalanish-shartlari">Shartlar</a>
<a href="/cookie-siyosati">Cookie</a>
<a href="/masuliyatli-oyin">Mas'uliyatli o'yin</a>
</nav>
<p class="footer-disclaimer">18+. casino-bonuses-uz.com — mustaqil reyting portali. Operator emas.</p>
</div></footer>
<script src="../js/partner.js?v=20260618"></script>
<script src="../js/main.js?v=20260618"></script>
<aside class="sticky-cta sticky-cta--dock" id="sticky-cta" role="complementary" aria-label="Birinchi depozit bonusi">
<div class="sticky-cta__panel">
<p class="sticky-cta__text"><span class="sticky-cta__prefix">Start paketi:</span> <strong class="sticky-cta__highlight">20,2 mln UZS + 150 frispin</strong></p>
<button type="button" class="btn btn--gold sticky-cta__btn js-go-partner">Faollashtirish</button>
<button type="button" class="sticky-cta__close" aria-label="Yopish">×</button>
</div>
</aside>
</body></html>'''

PAGES = {}

# Content will be added in the write calls below - using script with inline dict

if __name__ == '__main__':
    print('Use direct file writes')
