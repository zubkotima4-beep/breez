from site_common import page, hero_picture, img, organization_jsonld, CAPABILITIES
from components import section_head, gallery, feature_grid


def home():
    marquee_items = [
        "Размотка картона", "Шестикрасочная печать", "ВД лак",
        "Тиснение фольгой", "Конгрев", "Высечка",
        "Вклейка окон", "Склейка до 6 точек", "УФ-лак",
    ]
    group = "".join(f"<span>{item}</span><i></i>" for item in marquee_items)

    capabilities = [
        ("Размотка картона на первый формат", "Подготовка картона к печати и высечке — ровно под формат заказа."),
        ("Шестикрасочная печать + ВД лак, тиснение фольгой", "Полноцветная печать с водно-дисперсионным лаком и металлизированными акцентами."),
        ("Конгрев, высечка первого формата с удалением облоя", "Рельефное тиснение и сложные контуры любой сложности, с удалением лишнего материала."),
        ("Вклейка окон ПЭТ, ПЭВД, ПВХ, ПП", "Прозрачные окна под продукт и тип изделия."),
        ("Склейка до 6 точек", "Сборка конструкций сложной формы с точной геометрией."),
        ("УФ-лак", "Глянцевая или матовая защита и выразительная детализация."),
    ]

    process_steps = [
        ("Запрос", "Размеры, тираж, материал, сроки. Достаточно фото или образца."),
        ("Расчёт", "Считаем стоимость и предлагаем операции. Без лишних позиций в смете."),
        ("Образец", "Согласуем материал и печать до запуска. Правки — до тиража."),
        ("Производство", "Изготавливаем, контролируем качество, комплектуем заказ."),
        ("Отгрузка", "Передаём готовый тираж на ваш адрес или самовывозом."),
    ]
    process_html = "".join(
        f'<div class="process-step"><span class="process-step__num">{i:02d}</span>'
        f'<div><p class="process-step__title">{title}</p><p class="process-step__text">{text}</p></div></div>'
        for i, (title, text) in enumerate(process_steps, 1)
    )

    experience_items = [
        ("С 2010 года", "Более 15 лет в производстве картонной продукции."),
        ("Государственные заказчики", "Опыт работы с требованиями к документам, срокам и качеству."),
        ("Полный цикл", "Печать, отделка, высечка и склейка в одном договоре."),
        ("43 сотрудника", "Команда, которая ведёт заказ от расчёта до отгрузки."),
    ]
    experience_html = "".join(
        f'<div class="experience__item"><span class="num">{i:02d}</span>'
        f'<div><h3>{title}</h3><p>{text}</p></div></div>'
        for i, (title, text) in enumerate(experience_items, 1)
    )

    content = f"""<section class="hero">
<div class="hero__media">{hero_picture("hero-facade", "hero-mobile", "Производственная площадка БРИЗ в Климовске")}</div>
<div class="hero__grain" aria-hidden="true"></div>
<div class="hero__seal" aria-hidden="true">Печать · отделка<br>высечка<br>склейка</div>
<div class="container hero__content">
<div class="hero__eyebrow"><span>Климовск · Московская область</span><span class="dot"></span><span>с 2010 года</span></div>
<h1 class="hero__title"><span class="line">Материя</span><em>упаковки</em></h1>
<div class="hero__bottom">
<div>
<p class="hero__lead">Размотка картона, шестикрасочная печать с ВД лаком и тиснением фольгой, конгрев, высечка с удалением облоя, вклейка окон, склейка до 6 точек и УФ-лак. Шесть операций на одной площадке в Климовске.</p>
<div class="hero__actions">
<a class="btn btn--light" href="#directions">Смотреть возможности</a>
<button class="btn" type="button" data-open-request style="--btn-bg:transparent;--btn-color:#f0e7d5;--btn-border:rgba(240,231,213,.4)">Обсудить задачу</button>
</div>
</div>
<div class="hero__stats">
<div class="hero__stat"><strong>2010</strong><span>год основания</span></div>
<div class="hero__stat"><strong>43</strong><span>сотрудника</span></div>
<div class="hero__stat"><strong>6</strong><span>операций отделки</span></div>
</div>
</div>
</div>
<a class="hero__scroll" href="#intro">Листайте</a>
</section>
<div class="marquee" aria-hidden="true"><div class="marquee__track"><div class="marquee__group">{group}</div><div class="marquee__group">{group}</div></div></div>
<section class="section section--paper" id="intro">
<div class="container intro">
<div class="intro__copy" data-reveal>
<p class="eyebrow">01 / Компания</p>
<h2 class="intro__statement">Одна площадка. <em>Полный цикл.</em></h2>
<p class="intro__text">ООО «БРИЗ» работает с 2010 года. Производственная площадка находится в Климовске — на улице Ленина, 1к13. Здесь мы разматываем картон, печатаем, тисним, высекаем, вклеиваем окна и склеиваем изделия.</p>
<p class="intro__text">Один договор вместо цепочки посредников. Заказ не теряется между подрядчиками: мы видим весь путь — от материала до готового тиража.</p>
<a class="text-link" href="about.html">О компании</a>
</div>
<div class="intro__media" data-reveal="right">{img("facility-tall", "Производственная площадка БРИЗ", sizes="(max-width: 1024px) 100vw, 46vw")}<div class="intro__media-caption">Производственная площадка, Климовск</div></div>
</div>
</section>
<section class="section section--tight section--paper">
<div class="container">
<div class="stats" data-reveal>
<div class="stats__item"><span class="stats__num">2010</span><span class="stats__label">год основания компании</span></div>
<div class="stats__item"><span class="stats__num">43</span><span class="stats__label">сотрудника в штате</span></div>
<div class="stats__item"><span class="stats__num">6</span><span class="stats__label">операций печати и отделки</span></div>
<div class="stats__item"><span class="stats__num">17.29</span><span class="stats__label">основной ОКВЭД — изделия из бумаги и картона</span></div>
</div>
</div>
</section>
<section class="section section--cream" id="directions">
<div class="container">
{section_head("02 / Производственные возможности", "Полный цикл <em>отделки</em>.", "Размотка, печать, тиснение, высечка, вклейка окон и склейка — на одной площадке в Климовске.", "6 операций")}
{feature_grid(capabilities, cols=2)}
<div data-reveal style="margin-top:30px"><a class="text-link" href="capabilities.html">Все возможности и оборудование</a></div>
</div>
</section>
<section class="section section--dark">
<div class="container">
<div class="process-layout">
<div class="process-sticky" data-reveal>
<p class="eyebrow">03 / Процесс</p>
<h2 class="section-title">От запроса до <em>отгрузки</em></h2>
<p class="section-lead">Пять этапов, на каждом из которых понятно, что происходит с заказом.</p>
<a class="text-link" href="capabilities.html">Как мы производим</a>
</div>
<div class="process-list">{process_html}</div>
</div>
<div class="process-media" data-reveal>{img("press", "Печатный участок производства", sizes="(max-width: 760px) 100vw, 90vw")}<div class="process-media__caption">Печать и контроль качества — на одной площадке</div></div>
</div>
</section>
<section class="section section--cream">
<div class="container">
{section_head("04 / Производство", "Так это выглядит <em>вживую</em>.", "Не рендеры и не стоковые картинки. Наши участки, оборудование и готовая продукция.", "Климовск")}
{gallery([
    ("factory-floor", "Производственный участок", "Производственный участок БРИЗ"),
    ("paper-rolls", "Картон в рулонах", "Рулоны картона на производстве"),
    ("diecut", "Высечка", "Высечной участок"),
    ("warehouse-wide", "Готовая продукция", "Готовая продукция после отделки"),
])}
</div>
</section>
<section class="section section--dark section--line">
<div class="container experience">
<div class="experience__heading" data-reveal>
<p class="eyebrow">05 / Опыт</p>
<h2 class="section-title">Опыт, который <em>проверяется делом</em>.</h2>
<p class="experience__text">С 2010 года мы прошли путь до производственной площадки с полным циклом печати и отделки. Работаем с бизнесом и государственными заказчиками — и понимаем, что за каждым тиражом стоят сроки, документы и репутация.</p>
</div>
<div data-reveal>
<div class="experience__list">{experience_html}</div>
<div class="experience__foot"><a class="text-link" href="experience.html">Опыт и госзаказ</a><button class="btn btn--light btn--sm" type="button" data-open-request>Обсудить задачу</button></div>
</div>
</div>
</section>
<section class="cta">
<div class="container cta__inner">
<div data-reveal><p class="eyebrow">Свяжитесь</p><h2 class="cta__title">Обсудим <em>вашу задачу?</em></h2></div>
<div class="cta__side" data-reveal>
<a class="cta__phone" href="tel:+74959562028">+7 495 956-20-28</a>
<p class="cta__note">Позвоните или напишите на почту. Подготовим расчёт и предложим решение.</p>
<button class="btn" type="button" data-open-request>Оставить заявку</button>
</div>
</div>
<div class="cta__deco" aria-hidden="true"></div>
</section>"""

    return page(
        "home",
        "БРИЗ — печать, высечка и отделка в Климовске",
        "ООО «БРИЗ» с 2010 года: размотка картона на первый формат, шестикрасочная печать + ВД лак, тиснение фольгой, конгрев, высечка с удалением облоя, вклейка окон ПЭТ, ПЭВД, ПВХ, ПП, склейка до 6 точек, УФ-лак. Климовск, Московская область.",
        content,
        overlay=True,
        body_class="page-home",
        extra_head=organization_jsonld(),
    )
