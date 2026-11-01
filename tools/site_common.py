from pathlib import Path
from html import escape
from urllib.parse import quote
import json

ROOT = Path(__file__).resolve().parent.parent
ASSET_VERSION = "20261101-4"

PHONE = "+7 495 956-20-28"
PHONE_HREF = "tel:+74959562028"
EMAIL = "brizpak@list.ru"
PHONE_EXTRA = "+7 926 140-98-11"
PHONE_EXTRA_HREF = "tel:+79261409811"
ADDRESS = "142180, Московская область, г. Подольск, мкр. Климовск, ул. Ленина, 1к13"
ADDRESS_SHORT = "Климовск, ул. Ленина, 1к13"
MAP_QUERY = "Московская область, Климовск, улица Ленина, 1к13"
MAP_COORDS = "37.52552,55.36352"
MAP_URL = "https://yandex.ru/maps/?text=" + quote(MAP_QUERY)
MAP_STATIC = (
    "https://static-maps.yandex.ru/1.x/?ll=" + quote(MAP_COORDS)
    + "&amp;z=17&amp;l=map&amp;pt=" + quote(MAP_COORDS) + "%2Cpm2rdm&amp;size=650,450"
)

CAPABILITIES = [
    ("razmotka", "Размотка картона на первый формат", "Размотка картона", "на первый формат", "01"),
    ("pechat", "Шестикрасочная печать + ВД лак, тиснение фольгой", "Шестикрасочная печать", "ВД лак &middot; тиснение фольгой", "02"),
    ("vysechka", "Конгрев, высечка первого формата с удалением облоя", "Конгрев и высечка", "с удалением облоя", "03"),
    ("okna", "Вклейка окон ПЭТ, ПЭВД, ПВХ, ПП", "Вклейка окон", "ПЭТ &middot; ПЭВД &middot; ПВХ &middot; ПП", "04"),
    ("skleika", "Склейка до 6 точек", "Склейка", "до 6 точек", "05"),
    ("lak", "УФ-лак", "УФ-лак", "защита и глянец", "06"),
]

IMAGE_META = {
    "hero-facade": (1920, 1200),
    "hero-mobile": (960, 1200),
    "facility-tall": (1200, 1500),
    "facility-gate": (1200, 1500),
    "warehouse-wide": (1600, 1000),
    "factory-floor": (1600, 1000),
    "paper-rolls": (1600, 1000),
    "paper-rolls-tall": (1200, 1500),
    "paper-stack": (1600, 1000),
    "rolls-close": (1600, 1000),
    "finished-goods": (1600, 1000),
    "boxes": (1600, 1000),
    "print-sheets": (1200, 1500),
    "print-detail": (1600, 1000),
    "press": (1600, 1000),
    "diecut": (1600, 1000),
    "bobst": (1600, 1000),
    "gluer": (1600, 1000),
    "labels": (1600, 1000),
    "shrink": (1600, 1000),
}

BRAND_MARK = """<svg viewBox="0 0 64 64" fill="none" aria-hidden="true">
<rect x="1" y="1" width="62" height="62" rx="13" stroke="currentColor" stroke-opacity=".35"/>
<path d="M14 23h22c5.2 0 9 3 9 7s-3.8 7-9 7H18" stroke="currentColor" stroke-width="3.2" stroke-linecap="round"/>
<path d="M14 38h13c3.5 0 6 2.2 6 5s-2.5 5-6 5H17" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" opacity=".58"/>
</svg>"""

COPY_ICON = """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><rect x="9" y="9" width="11" height="11"/><path d="M5 15V4h11"/></svg>"""

ARROW = "&#8599;"


def img(slug, alt, sizes="100vw", class_name="", eager=False, position=None):
    files = sorted(
        (ROOT / "assets" / "photos" / "optimized").glob(f"{slug}-*.webp"),
        key=lambda p: int(p.stem.split("-")[-1]),
    )
    widths = [int(p.stem.split("-")[-1]) for p in files]
    srcset = ", ".join(f"assets/photos/optimized/{slug}-{w}.webp {w}w" for w in widths)
    base = 960 if 960 in widths else widths[len(widths) // 2]
    w, h = IMAGE_META.get(slug, (1600, 1000))
    loading = "eager" if eager else "lazy"
    priority = ' fetchpriority="high"' if eager else ""
    style = f' style="object-position:{position}"' if position else ""
    cls = f' class="{class_name}"' if class_name else ""
    return (
        f'<img src="assets/photos/optimized/{slug}-{base}.webp" '
        f'srcset="{srcset}" sizes="{sizes}" alt="{escape(alt, quote=True)}" '
        f'width="{w}" height="{h}" loading="{loading}" decoding="async"{priority}{style}{cls}>'
    )


def hero_picture(desktop, mobile, alt):
    files = sorted(
        (ROOT / "assets" / "photos" / "optimized").glob(f"{mobile}-*.webp"),
        key=lambda p: int(p.stem.split("-")[-1]),
    )
    widths = [int(p.stem.split("-")[-1]) for p in files]
    srcset = ", ".join(f"assets/photos/optimized/{mobile}-{w}.webp {w}w" for w in widths)
    return (
        f'<picture><source media="(max-width: 760px)" srcset="{srcset}" sizes="100vw">'
        f'{img(desktop, alt, eager=True, position="58% 48%")}</picture>'
    )


def brand(extra_class=""):
    cls = f"brand {extra_class}".strip()
    return f"""<a class="{cls}" href="index.html" aria-label="БРИЗ — на главную">
<span class="brand__mark">{BRAND_MARK}</span>
<span class="brand__text"><span class="brand__name">БРИЗ</span><span class="brand__sub">Печать и отделка &middot; Климовск</span></span>
</a>"""


def breadcrumbs(items):
    parts = ['<nav class="breadcrumbs" aria-label="Хлебные крошки">']
    for i, (label, href) in enumerate(items):
        if i:
            parts.append("<span>/</span>")
        if href:
            parts.append(f'<a href="{href}">{label}</a>')
        else:
            parts.append(f'<span aria-current="page">{label}</span>')
    parts.append("</nav>")
    return "".join(parts)


def header(active, overlay=True):
    cls = "header header--overlay" if overlay else "header header--solid"
    capability_links = []
    for slug, title, nav_title, short, num in CAPABILITIES:
        current = ' aria-current="page"' if active == "capabilities" else ""
        capability_links.append(
            f'<a href="capabilities.html#{slug}"{current}><span class="num">{num}</span>'
            f"<span><strong>{nav_title}</strong><small>{short}</small></span></a>"
        )
    company_links = [
        ("about", "О компании", "Производство, люди, принципы"),
        ("experience", "Опыт и госзаказ", "Документы, сроки, поставки"),
        ("requisites", "Реквизиты", "ИНН, ОГРН, адрес"),
    ]
    company_parts = []
    for i, (slug, title, short) in enumerate(company_links, 1):
        current = ' aria-current="page"' if active == slug else ""
        company_parts.append(
            f'<a href="{slug}.html"{current}><span class="num">{i:02d}</span>'
            f'<span><strong>{title}</strong><small>{short}</small></span></a>'
        )
    company_html = "".join(company_parts)
    contact_current = ' aria-current="page"' if active == "contacts" else ""
    return f"""<a class="skip-link" href="#main">К содержанию</a>
<header class="{cls}">
<div class="container header__inner">
{brand()}
<nav class="nav" aria-label="Основная навигация">
<ul class="nav__list">
<li class="nav__item nav__item--has-dropdown">
<button class="nav__trigger" type="button" aria-expanded="false" aria-haspopup="true">Возможности <span class="chev"></span></button>
<div class="nav__dropdown">{''.join(capability_links)}</div>
</li>
<li class="nav__item nav__item--has-dropdown">
<button class="nav__trigger" type="button" aria-expanded="false" aria-haspopup="true">Компания <span class="chev"></span></button>
<div class="nav__dropdown">{company_html}</div>
</li>
<li class="nav__item"><a class="nav__link" href="contacts.html"{contact_current}>Контакты</a></li>
</ul>
</nav>
<div class="header__actions">
<a class="header__phone" href="{PHONE_HREF}">{PHONE}</a>
<button class="btn header__cta" type="button" data-open-request>Обсудить задачу</button>
<button class="burger" type="button" data-menu-toggle aria-label="Открыть меню" aria-expanded="false" aria-controls="mobileMenu"><span></span><span></span></button>
</div>
</div>
<div class="scroll-progress" aria-hidden="true"></div>
</header>"""


def mobile_menu(active):
    capability_parts = []
    for slug, title, nav_title, short, num in CAPABILITIES:
        capability_parts.append(
            f'<a href="capabilities.html#{slug}"><span class="num">{num}</span>{nav_title}</a>'
        )
    capability_links = "".join(capability_parts)
    home_current = ' aria-current="page"' if active == "home" else ""
    return f"""<div class="mobile-menu" id="mobileMenu" data-mobile-menu aria-hidden="true">
<nav class="mobile-menu__nav" aria-label="Мобильная навигация">
<a href="index.html"{home_current}>Главная <span>00</span></a>
<div class="mobile-menu__accordion">
<button type="button" aria-expanded="false">Возможности <span>06</span></button>
<div class="mobile-menu__sub">{capability_links}</div>
</div>
<div class="mobile-menu__accordion">
<button type="button" aria-expanded="false">Компания <span>03</span></button>
<div class="mobile-menu__sub">
<a href="about.html"><span class="num">01</span>О компании</a>
<a href="experience.html"><span class="num">02</span>Опыт и госзаказ</a>
<a href="requisites.html"><span class="num">03</span>Реквизиты</a>
</div>
</div>
<a href="contacts.html">Контакты <span>04</span></a>
</nav>
<div class="mobile-menu__foot">
<div class="mobile-menu__contacts">
<a href="{PHONE_HREF}">{PHONE}</a>
<a href="mailto:brizpak@list.ru">Почта &middot; brizpak@list.ru</a>
<small>{ADDRESS_SHORT}. Офис и производство на одной площадке.</small>
</div>
<button class="btn btn--light mobile-menu__cta" type="button" data-open-request>Обсудить задачу</button>
</div>
</div>"""


def footer():
    capability_links = "".join(
        f'<a href="capabilities.html#{slug}">{nav_title}</a>'
        for slug, title, nav_title, short, num in CAPABILITIES
    )
    return f"""<footer class="footer">
<div class="container">
<div class="footer__top">
<div class="footer__brand">
{brand()}
<p class="footer__desc">Размотка картона, печать, тиснение, высечка, вклейка окон и склейка. Климовск, Московская область. С 2010 года.</p>
<a class="text-link" href="contacts.html">Связаться</a>
</div>
<div class="footer__col">
<p class="footer__col-title">Возможности</p>
{capability_links}
</div>
<div class="footer__col">
<p class="footer__col-title">Компания</p>
<a href="about.html">О компании</a>
<a href="experience.html">Опыт и госзаказ</a>
<a href="requisites.html">Реквизиты</a>
<a href="privacy.html">Политика конфиденциальности</a>
</div>
<div class="footer__col">
<p class="footer__col-title">Контакты</p>
<a class="footer__phone" href="{PHONE_HREF}">{PHONE}</a>
<a href="mailto:brizpak@list.ru">Почта &middot; brizpak@list.ru</a>
<a href="{PHONE_EXTRA_HREF}">{PHONE_EXTRA}</a>
<address>{ADDRESS}</address>
</div>
</div>
<div class="footer__bottom">
<span>&copy; <span data-year>2026</span> ООО &laquo;БРИЗ&raquo; &middot; ИНН 5051321330</span>
<div class="footer__legal">
<a href="requisites.html">Реквизиты</a>
<a href="privacy.html">Конфиденциальность</a>
<a href="contacts.html">Контакты</a>
</div>
</div>
</div>
<div class="footer__wordmark" aria-hidden="true">БРИЗ</div>
</footer>"""


def request_dialog():
    options = "".join(f'<option value="{title}">{title}</option>' for slug, title, nav_title, short, num in CAPABILITIES)
    return f"""<dialog id="requestDialog" aria-labelledby="requestTitle">
<div class="dialog__inner">
<button class="dialog__close" type="button" data-close-dialog aria-label="Закрыть">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M5 5l14 14M19 5L5 19"/></svg>
</button>
<p class="dialog__label">Заявка</p>
<h2 class="dialog__title" id="requestTitle">Расскажите, что нужно</h2>
<p class="dialog__lead">Заполните форму &mdash; мы подготовим сообщение и отправим его на почту. Отправить его можно одним нажатием.</p>
<form class="request-form" data-request-form>
<div class="form-row">
<div class="field"><label for="req-name">Имя *</label><input id="req-name" name="name" required autocomplete="name" placeholder="Как к вам обращаться"></div>
<div class="field"><label for="req-company">Компания</label><input id="req-company" name="company" autocomplete="organization" placeholder="Название организации"></div>
</div>
<div class="form-row">
<div class="field"><label for="req-phone">Телефон *</label><input id="req-phone" name="phone" type="tel" required data-phone inputmode="tel" autocomplete="tel" placeholder="+7 (___) ___-__-__"></div>
<div class="field"><label for="req-direction">Что интересует</label><select id="req-direction" name="direction"><option value="">Выберите возможность</option>{options}<option value="Другое">Другое</option></select></div>
</div>
<div class="field"><label for="req-comment">Задача</label><textarea id="req-comment" name="comment" placeholder="Тираж, размеры, сроки &mdash; всё, что важно"></textarea></div>
<label class="form-consent"><input type="checkbox" required><span>Согласен на обработку данных в соответствии с <a href="privacy.html" target="_blank" rel="noopener">политикой конфиденциальности</a>.</span></label>
<div class="form-actions"><button class="btn" type="submit">Подготовить сообщение</button><span class="form-hint">Данные не отправляются на сервер &mdash; вы сами отправите письмо на почту.</span></div>
</form>
<div class="request-success" data-request-success>
<h3>Сообщение готово</h3>
<p id="request-message" data-request-text></p>
<div class="request-success__actions">
<a class="btn btn--sm" data-request-mailto href="mailto:brizpak@list.ru">Открыть почту</a>
<button class="btn btn--sm btn--ghost" type="button" data-copy="#request-message">Скопировать текст</button>
</div>
<p class="form-hint">Если почта не работает, скопируйте текст и отправьте его удобным способом.</p>
</div>
</div>
</dialog>"""


def page(slug, title, description, content, overlay=True, body_class="", extra_head="", noindex=False):
    robots = "noindex,nofollow" if noindex else "index,follow"
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{escape(description, quote=True)}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#212842">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="manifest" href="site.webmanifest">
<link rel="preload" href="assets/fonts/Onest-normal-400-900-cyrillic.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/GolosText-normal-400-700-cyrillic.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="css/fonts.css?v={ASSET_VERSION}">
<link rel="stylesheet" href="css/style.css?v={ASSET_VERSION}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="ООО &laquo;БРИЗ&raquo;">
<meta property="og:title" content="{escape(title, quote=True)}">
<meta property="og:description" content="{escape(description, quote=True)}">
<meta property="og:image" content="assets/og-image.jpg">
<meta property="og:locale" content="ru_RU">
<meta name="twitter:card" content="summary_large_image">
<script>document.documentElement.classList.add('js');</script>
{extra_head}
</head>
<body class="{body_class}">
{header(slug, overlay)}
{mobile_menu(slug)}
<main id="main">
{content}
</main>
{footer()}
{request_dialog()}
<script src="js/main.js?v={ASSET_VERSION}" defer></script>
</body>
</html>"""


def organization_jsonld():
    data = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "ООО «БРИЗ»",
        "legalName": "Общество с ограниченной ответственностью «БРИЗ»",
        "foundingDate": "2010-07-08",
        "taxID": "5051321330",
        "identifier": [
            {"@type": "PropertyValue", "name": "ОГРН", "value": "1105074006828"},
            {"@type": "PropertyValue", "name": "КПП", "value": "502101001"},
        ],
        "address": {
            "@type": "PostalAddress",
            "postalCode": "142180",
            "addressCountry": "RU",
            "addressRegion": "Московская область",
            "addressLocality": "Подольск",
            "streetAddress": "мкр. Климовск, ул. Ленина, 1к13",
        },
        "telephone": PHONE,
        "numberOfEmployees": {"@type": "QuantitativeValue", "value": 43},
        "description": "Размотка картона на первый формат, шестикрасочная печать + ВД лак, тиснение фольгой, конгрев, высечка первого формата с удалением облоя, вклейка окон ПЭТ, ПЭВД, ПВХ, ПП, склейка до 6 точек, УФ-лак.",
    }
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def breadcrumb_jsonld(items):
    data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i, "name": label, "item": href}
            for i, (label, href) in enumerate(items, 1)
            if href
        ],
    }
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"
