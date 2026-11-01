from site_common import img, breadcrumbs, ARROW, COPY_ICON


def section_head(label, title, lead="", note=""):
    note_html = f'<span>{note}</span>' if note else ""
    lead_html = f'<p class="section-lead">{lead}</p>' if lead else ""
    return f"""<div class="section-head" data-reveal>
<div class="section-head__label"><span class="label">{label}</span>{note_html}</div>
<div><h2 class="section-title">{title}</h2>{lead_html}</div>
</div>"""


def feature_grid(items, cols=2):
    cls = "feature-grid feature-grid--3" if cols == 3 else "feature-grid"
    cards = []
    for i, item in enumerate(items, 1):
        title, text = item[0], item[1]
        href = item[2] if len(item) > 2 else None
        tag_open = f'<a class="feature-card" href="{href}">' if href else '<div class="feature-card">'
        tag_close = "</a>" if href else "</div>"
        cards.append(
            f'{tag_open}<div class="feature-card__num"><span>{i:02d}</span></div>'
            f"<h3>{title}</h3><p>{text}</p>{tag_close}"
        )
    return f'<div class="{cls}" data-reveal>{"".join(cards)}</div>'


def check_list(items):
    return '<ul class="check-list" data-reveal>' + "".join(f"<li>{item}</li>" for item in items) + "</ul>"


def steps(items):
    cards = "".join(
        f'<div class="step"><span class="step__num">{i:02d}</span>'
        f'<p class="step__title">{title}</p><p class="step__text">{text}</p></div>'
        for i, (title, text) in enumerate(items, 1)
    )
    return f'<div class="steps" data-reveal>{cards}</div>'


def faq(items):
    blocks = "".join(
        f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items
    )
    return f'<div class="faq" data-reveal>{blocks}</div>'


def gallery(items):
    cards = []
    for i, (slug, caption, alt) in enumerate(items, 1):
        full = f"assets/photos/optimized/{slug}-1600.webp"
        cards.append(
            f'<button class="gallery__item" type="button" data-lightbox data-full="{full}" data-caption="{caption}">'
            f'{img(slug, alt, sizes="(max-width: 760px) 50vw, 50vw")}'
            f'<span class="gallery__caption"><span>{caption}</span><span>{ARROW}</span></span></button>'
        )
    return f'<div class="gallery" data-reveal>{"".join(cards)}</div>'


def photo_band(main, side1, side2):
    return f"""<div class="photo-band" data-reveal>
<div>{img(main[0], main[1], sizes="(max-width: 760px) 100vw, 60vw")}</div>
<div class="photo-band__side">
<div>{img(side1[0], side1[1], sizes="(max-width: 760px) 50vw, 30vw")}</div>
<div>{img(side2[0], side2[1], sizes="(max-width: 760px) 50vw, 30vw")}</div>
</div>
</div>"""


def page_hero(title, lead, label, image=None, image_alt="", light=False, plain=False, short=False, crumbs=None, meta=None):
    classes = ["page-hero"]
    if light:
        classes.append("page-hero--light")
    if plain:
        classes.append("page-hero--plain")
    if short:
        classes.append("page-hero--short")
    media = ""
    if image:
        media = f'<div class="page-hero__media">{img(image, image_alt, eager=True)}</div>'
    crumbs_html = breadcrumbs(crumbs) if crumbs else ""
    meta_html = ""
    if meta:
        meta_html = '<div class="page-hero__meta">' + "".join(
            f"<span><strong>{k}</strong> {v}</span>" for k, v in meta
        ) + "</div>"
    return f"""<section class="{' '.join(classes)}">
{media}
<div class="container page-hero__content">
{crumbs_html}
<p class="page-hero__label">{label}</p>
<h1 class="page-hero__title">{title}</h1>
<p class="page-hero__lead">{lead}</p>
{meta_html}
</div>
</section>"""


def page_cta(title, text, topic="Другое"):
    return f"""<div class="page-cta" data-reveal>
<div><h2 class="page-cta__title">{title}</h2><p class="section-lead" style="color:rgba(240,231,213,.66);margin-top:14px;max-width:460px">{text}</p></div>
<div class="page-cta__side">
<a class="page-cta__phone" href="tel:+74959562028">+7 495 956-20-28</a>
<button class="btn btn--light btn--sm" type="button" data-open-request data-request-topic="{topic}">Оставить заявку</button>
</div>
</div>"""


def side_nav(items, note_title, note_text, topic):
    links = []
    for i, (href, label) in enumerate(items):
        active = ' class="is-active"' if i == 0 else ""
        links.append(f'<a href="{href}"{active}>{label}</a>')
    links = "".join(links)
    return f"""<aside class="content-side">
<nav class="side-nav" aria-label="Содержание страницы">
<p class="side-nav__title">На этой странице</p>
{links}
</nav>
<div class="side-note">
<p class="side-note__title">{note_title}</p>
<p>{note_text}</p>
<button class="btn btn--sm btn--block" type="button" data-open-request data-request-topic="{topic}">Оставить заявку</button>
</div>
</aside>"""


def spec_table(rows):
    html = []
    for i, (label, value, copy_id) in enumerate(rows):
        if copy_id:
            control = (
                f'<button class="copy-btn" type="button" data-copy="#{copy_id}" '
                f'aria-label="Скопировать: {label}">{COPY_ICON}</button>'
            )
            value_html = f'<span class="spec-row__value" id="{copy_id}">{value}</span>'
        else:
            control = '<span aria-hidden="true"></span>'
            value_html = f'<span class="spec-row__value">{value}</span>'
        html.append(
            f'<div class="spec-row"><span class="spec-row__label">{label}</span>{value_html}{control}</div>'
        )
    return f'<div class="spec-table" data-reveal>{"".join(html)}</div>'


def prose(html):
    return f'<div class="prose" data-reveal>{html}</div>'
