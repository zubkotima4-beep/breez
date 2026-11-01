from site_common import (
    page, img, ADDRESS, ADDRESS_SHORT, PHONE, PHONE_HREF, EMAIL,
    PHONE_EXTRA, PHONE_EXTRA_HREF, MAP_URL, MAP_STATIC, breadcrumb_jsonld,
)
from components import (
    page_hero, section_head, feature_grid, check_list, steps, faq, photo_band,
    page_cta, spec_table, prose,
)


def about():
    hero = page_hero(
        "Не просто поставщик. <em>Производство.</em>",
        "ООО «БРИЗ» — производственная компания из Климовска. С 2010 года выполняем размотку картона, печать, тиснение, высечку, вклейку окон и склейку.",
        "О компании",
        image="facility-tall",
        image_alt="Здание производственной площадки БРИЗ",
        light=True,
        crumbs=[("Главная", "index.html"), ("О компании", None)],
        meta=[("Основано", "в 2010"), ("43", "сотрудника"), ("Климовск", "Московская область")],
    )
    capabilities = [
        ("Размотка картона на первый формат", "Подготовка картона к печати и высечке.", "capabilities.html#razmotka"),
        ("Шестикрасочная печать + ВД лак", "Тиснение фольгой и контроль цвета.", "capabilities.html#pechat"),
        ("Конгрев и высечка", "Первый формат, удаление облоя, любой сложности.", "capabilities.html#vysechka"),
        ("Вклейка окон", "ПЭТ, ПЭВД, ПВХ, ПП под продукт.", "capabilities.html#okna"),
        ("Склейка до 6 точек", "Сложные конструкции с точной геометрией.", "capabilities.html#skleika"),
        ("УФ-лак", "Глянцевая или матовая защита печати.", "capabilities.html#lak"),
    ]
    principles = [
        ("Один договор", "Печать, отделка, высечка и склейка — в одних руках. Меньше согласований, короче путь."),
        ("Расчёт под задачу", "Начинаем с продукта и условий эксплуатации, а не с готового прайса."),
        ("Прозрачные сроки", "Фиксируем этапы. Если что-то меняется, сообщаем заранее."),
        ("Документы в порядке", "Работаем официально. Готовим счёт, УПД и документы для закупок."),
    ]
    principle_html = "".join(
        f'<div class="experience__item"><span class="num">{i:02d}</span>'
        f'<div><h3>{title}</h3><p>{text}</p></div></div>'
        for i, (title, text) in enumerate(principles, 1)
    )
    about_prose = prose("""
<p>ООО «БРИЗ» зарегистрировано 8 июля 2010 года. Основной вид деятельности — производство прочих изделий из бумаги и картона (ОКВЭД 17.29).</p>
<p>Производственная площадка и офис находятся в Климовске, на улице Ленина, 1к13. Здесь расположены производственный участок и коммерческая служба. Поэтому заказ не теряется между подрядчиками: мы видим весь путь — от сырья до отгрузки.</p>
<p>Помимо производства, компания выполняет печать, тиснение фольгой, конгрев, высечку с удалением облоя, вклейку окон и склейку. Шесть операций дополняют друг друга и позволяют собрать для клиента единый заказ.</p>
<p>В компании работают 43 сотрудника. С 2016 года ООО «БРИЗ» включено в реестр малого и среднего предпринимательства.</p>
""")
    content = f"""{hero}
<section class="section section--paper">
<div class="container container--narrow">
{section_head("01 / О компании", "Производство и отделка <em>в одном контуре</em>.", "Мы находимся в Климовске, на улице Ленина, 1к13. Здесь работают производственный участок и коммерческая служба.", "Климовск")}
{about_prose}
</div>
</section>
<section class="section section--tight section--paper">
<div class="container">
{photo_band(
    ("facility-gate", "Въезд на производственную площадку"),
    ("factory-floor", "Производственный участок"),
    ("print-detail", "Печать и отделка"),
)}
</div>
</section>
<section class="section section--cream">
<div class="container">
{section_head("02 / Возможности", "Шесть операций <em>под одной крышей</em>.", "Можно заказать одну операцию. Можно собрать полный цикл — от размотки картона до УФ-лака.", "Полный цикл")}
{feature_grid([(title, text, href) for title, text, href in capabilities], cols=3)}
</div>
</section>
<section class="section section--dark">
<div class="container experience">
<div class="experience__heading" data-reveal>
<p class="eyebrow">03 / Принципы</p>
<h2 class="section-title">Как мы <em>работаем</em>.</h2>
<p class="experience__text">Надёжность складывается из скучных вещей: понятного расчёта, соблюдения сроков и документов, которые не приходится переделывать.</p>
</div>
<div data-reveal><div class="experience__list">{principle_html}</div></div>
</div>
</section>
<section class="section section--paper">
<div class="container">
{section_head("04 / Руководство", "Отвечает за <em>результат</em>.", "", "Генеральный директор")}
<div class="director-card" data-reveal>
<div class="director-card__label"><span class="mono">Генеральный директор</span><span class="mono">01 / 01</span></div>
<div><h3 class="director-card__name">Зубко Руслан Александрович</h3><p class="director-card__text">Отвечает за развитие компании и операционные решения. Ведёт ключевые проекты и контролирует качество поставок.</p></div>
</div>
</div>
</section>
<section class="section section--cream">
<div class="container">
{section_head("05 / Реквизиты", "Компания <em>в цифрах</em>.", "Полные реквизиты — в разделе для договоров и закупок.", "Данные ЕГРЮЛ")}
{spec_table([
    ("Полное наименование", "Общество с ограниченной ответственностью «БРИЗ»", None),
    ("Сокращённое наименование", "ООО «БРИЗ»", None),
    ("Дата регистрации", "8 июля 2010 года", None),
    ("ИНН", "5051321330", "about-inn"),
    ("КПП", "502101001", "about-kpp"),
    ("ОГРН", "1105074006828", "about-ogrn"),
    ("ОКПО", "66174670", "about-okpo"),
    ("ОКВЭД", "17.29 — производство прочих изделий из бумаги и картона", None),
    ("Сотрудники", "43 человека", None),
    ("Адрес", ADDRESS, "about-address"),
    ("Руководитель", "Зубко Руслан Александрович", None),
])}
<p class="requisites-note">Полный комплект документов для договора или закупки предоставим по запросу.</p>
<a class="text-link" href="requisites.html" style="margin-top:14px">Все реквизиты</a>
</div>
</section>
<section class="section section--paper">
<div class="container">{page_cta("Познакомимся <em>с задачей</em>", "Расскажите, что нужно. Предложим решение и посчитаем стоимость.", "Другое")}</div>
</section>"""
    extra = breadcrumb_jsonld([("Главная", "index.html"), ("О компании", "about.html")])
    return page("about", "О компании — производство и отделка в Климовске | БРИЗ",
                "ООО «БРИЗ»: размотка картона, печать, тиснение, высечка, вклейка окон, склейка и УФ-лак. 43 сотрудника, с 2010 года, Климовск, Московская область.",
                content, overlay=False, body_class="page-about", extra_head=extra)


def experience():
    hero = page_hero(
        "Опыт, который <em>можно проверить</em>",
        "С 2010 года работаем с производством и государственными заказчиками. Понимаем, что за каждым тиражом стоят сроки, документы и репутация.",
        "Опыт и государственные заказы",
        image="press",
        image_alt="Печатное оборудование на производстве",
        crumbs=[("Главная", "index.html"), ("Опыт и госзаказ", None)],
        meta=[("С 2010", "года"), ("43", "сотрудника"), ("44-ФЗ", "223-ФЗ")],
    )
    gov_cards = [
        ("Документы", "Счёт, УПД, карточка предприятия, документы на продукцию."),
        ("Сроки", "Фиксируем график поставки и держим связь."),
        ("Качество", "Контролируем партию до отгрузки."),
        ("Цена", "Считаем без лишних позиций."),
    ]
    supply_steps = [
        ("Запрос", "Получаем потребность и требования."),
        ("Предложение", "Считаем стоимость и сроки."),
        ("Договор", "Согласуем условия и документы."),
        ("Поставка", "Производим, контролируем качество и передаём заказ."),
    ]
    trust_cards = [
        ("Производство", "Своя площадка в Климовске."),
        ("Полный цикл", "От размотки картона до готового тиража."),
        ("Опыт", "С 2010 года."),
        ("Люди", "43 сотрудника, которые ведут заказ."),
    ]
    experience_prose = prose("""
<p>ООО «БРИЗ» работает с 2010 года. За это время компания прошла путь до производственной площадки с полным циклом печати и отделки: размотка картона, печать, тиснение, высечка, вклейка окон, склейка и УФ-лак.</p>
<p>Мы работаем с бизнесом и государственными заказчиками. Понимаем, что для закупки важны не только цена, но и документы, сроки и предсказуемость.</p>
""")
    content = f"""{hero}
<section class="section section--paper">
<div class="container container--narrow">
{section_head("01 / Опыт", "Опыт — это способность <em>повторить результат</em>.", "Не презентация, а поставка в срок, в нужном объёме и с правильными документами.", "С 2010 года")}
{experience_prose}
</div>
</section>
<section class="section section--dark">
<div class="container">
{section_head("02 / Госзаказ", "Государственным <em>заказчикам</em>.", "Есть опыт работы с государственными и муниципальными заказчиками. Готовы участвовать в закупках по 44-ФЗ и 223-ФЗ.", "Документы · сроки · качество")}
{feature_grid(gov_cards, cols=2)}
<p class="section-lead" style="color:rgba(240,231,213,.66);margin-top:28px;max-width:720px">Конкретные требования к документам, срокам и качеству согласуем под процедуру. Не обещаем невозможного — фиксируем то, что можем выполнить.</p>
</div>
</section>
<section class="section section--cream">
<div class="container">
<div class="stats" data-reveal>
<div class="stats__item"><span class="stats__num">2010</span><span class="stats__label">год основания</span></div>
<div class="stats__item"><span class="stats__num">43</span><span class="stats__label">сотрудника</span></div>
<div class="stats__item"><span class="stats__num">6</span><span class="stats__label">операций печати и отделки</span></div>
<div class="stats__item"><span class="stats__num">15+</span><span class="stats__label">лет на рынке</span></div>
</div>
</div>
</section>
<section class="section section--paper">
<div class="container">
{section_head("03 / Поставка", "Как проходит <em>поставка</em>.", "Понятный маршрут от запроса до закрывающих документов.", "Процесс")}
{steps(supply_steps)}
</div>
</section>
<section class="section section--cream">
<div class="container">
{section_head("04 / Заказчики", "С кем <em>работаем</em>.", "", "Отрасли")}
{check_list([
    "Производственные компании",
    "Торговые сети и ритейл",
    "Офисы и бизнес-центры",
    "Государственные и муниципальные учреждения",
    "Логистические компании",
    "Образовательные организации",
])}
</div>
</section>
<section class="section section--paper">
<div class="container">
{section_head("05 / Доверие", "Почему нам <em>доверяют</em>.", "", "Факты")}
{feature_grid(trust_cards, cols=2)}
</div>
</section>
<section class="section section--tight section--paper">
<div class="container">
{photo_band(
    ("factory-floor", "Производственный участок"),
    ("press", "Печатный участок"),
    ("facility-tall", "Производственная площадка"),
)}
</div>
</section>
<section class="section section--cream">
<div class="container">{page_cta("Обсудим <em>закупку</em>", "Подготовим предложение и комплект документов под вашу процедуру.", "Другое")}</div>
</section>"""
    extra = breadcrumb_jsonld([("Главная", "index.html"), ("Опыт и госзаказ", "experience.html")])
    return page("experience", "Опыт и государственные заказы | БРИЗ",
                "Опыт работы с государственными заказчиками: документы, сроки, качество. Производство и поставки с 2010 года, 43 сотрудника, Климовск.",
                content, overlay=True, body_class="page-experience", extra_head=extra)


def contacts():
    hero = page_hero(
        "Приезжайте. <em>Мы рядом.</em>",
        "Офис и производство — в Климовске. Позвоните, напишите на почту или оставьте заявку: обсудим задачу и предложим решение.",
        "Контакты",
        image="facility-gate",
        image_alt="Въезд на производственную площадку БРИЗ",
        light=True,
        crumbs=[("Главная", "index.html"), ("Контакты", None)],
        meta=[("Климовск", "ул. Ленина, 1к13"), ("Офис", "производство")],
    )
    contacts_prose = prose("""
<p>На автомобиле: удобный подъезд со стороны улицы Ленина. Парковка — по согласованию с менеджером.</p>
<p>На общественном транспорте: от станции Гривно Курского направления — на автобусе или такси. Ближайшая остановка — «Заводоуправление».</p>
<p>График приёма и возможность визита согласуйте по телефону. Мы на месте — в Климовске, на улице Ленина, 1к13.</p>
""")
    content = f"""{hero}
<section class="section section--paper">
<div class="container contact-layout">
<div>
<div class="contact-list" data-reveal>
<div class="contact-item">
<span class="contact-item__label">Адрес</span>
<div><p class="contact-item__value">{ADDRESS}</p><p class="contact-item__note">Офис и производство — на одной площадке. Визит согласуйте с менеджером.</p></div>
</div>
<div class="contact-item">
<span class="contact-item__label">Телефон</span>
<div><p class="contact-item__value"><a href="{PHONE_HREF}">{PHONE}</a></p><p class="contact-item__note">Общие вопросы, заказы, документы.</p></div>
</div>
<div class="contact-item">
<span class="contact-item__label">Почта</span>
<div><p class="contact-item__value"><a href="mailto:brizpak@list.ru">brizpak@list.ru</a></p><p class="contact-item__note">Можно отправить фото, размеры или список позиций.</p></div>
</div>
<div class="contact-item">
<span class="contact-item__label">Дополнительно</span>
<div><p class="contact-item__value"><a href="{PHONE_EXTRA_HREF}">{PHONE_EXTRA}</a></p><p class="contact-item__note">Резервный номер для связи.</p></div>
</div>
<div class="contact-item">
<span class="contact-item__label">Руководитель</span>
<div><p class="contact-item__value">Зубко Руслан Александрович</p><p class="contact-item__note">Генеральный директор ООО «БРИЗ».</p></div>
</div>
<div class="contact-item">
<span class="contact-item__label">Реквизиты</span>
<div><p class="contact-item__value"><a href="requisites.html">ИНН, ОГРН, адрес</a></p><p class="contact-item__note">Полный комплект — для договоров и закупок.</p></div>
</div>
</div>
<div class="contact-cta">
<a class="btn" href="{PHONE_HREF}">Позвонить</a>
<a class="btn btn--ghost" href="mailto:brizpak@list.ru">Почта</a>
<button class="btn btn--ghost" type="button" data-open-request>Оставить заявку</button>
</div>
<a class="text-link" href="assets/briz.vcf" download style="margin-top:24px">Скачать контакт</a>
</div>
<div>
<div class="contact-map" data-reveal>
<a class="contact-map__link" href="{MAP_URL}" target="_blank" rel="noopener" aria-label="Открыть адрес Климовск, ул. Ленина, 1к13 на Яндекс.Картах">
<img src="{MAP_STATIC}" alt="Карта: Климовск, ул. Ленина, 1к13" width="650" height="450" loading="lazy">
<span class="contact-map__open">Открыть карту ↗</span>
</a>
</div>
<p class="map-caption"><span>{ADDRESS_SHORT}</span><a href="{MAP_URL}" target="_blank" rel="noopener">Открыть в Яндекс.Картах ↗</a></p>
<div class="contact-note"><strong>Визит лучше согласовать заранее.</strong> Позвоните по основному номеру — подскажем, как проехать и куда обратиться на территории.</div>
</div>
</div>
</section>
<section class="section section--cream">
<div class="container container--narrow">
{section_head("Как добраться", "Ориентир — <em>Заводоуправление</em>.", "Ближайшая остановка — «Заводоуправление». Ориентир — территория Климовского машиностроительного завода.", "Климовск")}
{contacts_prose}
</div>
</section>
<section class="section section--paper">
<div class="container">{page_cta("Напишите <em>нам</em>", "Позвоните или оставьте заявку — ответим по существу.", "Другое")}</div>
</section>"""
    extra = breadcrumb_jsonld([("Главная", "index.html"), ("Контакты", "contacts.html")])
    return page("contacts", "Контакты — Климовск, ул. Ленина, 1к13 | БРИЗ",
                "Контакты ООО «БРИЗ»: 142180, Московская область, Подольск, мкр. Климовск, ул. Ленина, 1к13. Телефоны, почта, карта и реквизиты.",
                content, overlay=False, body_class="page-contacts", extra_head=extra)


def requisites():
    hero = page_hero(
        "Всё <em>официально</em>.",
        "Реквизиты ООО «БРИЗ» для договоров, закупок и платёжных документов.",
        "Реквизиты",
        plain=True,
        short=True,
        crumbs=[("Главная", "index.html"), ("Реквизиты", None)],
        meta=[("ИНН", "5051321330"), ("ОГРН", "1105074006828"), ("Климовск", "Московская область")],
    )
    content = f"""{hero}
<section class="section section--paper">
<div class="container container--narrow">
<div class="requisites-block" data-reveal>
<div class="requisites-block__head"><h2 class="requisites-block__title">Организация</h2><span class="mono">01 / 04</span></div>
{spec_table([
    ("Полное наименование", "Общество с ограниченной ответственностью «БРИЗ»", None),
    ("Сокращённое наименование", "ООО «БРИЗ»", None),
    ("ИНН", "5051321330", "req-inn"),
    ("КПП", "502101001", "req-kpp"),
    ("ОГРН", "1105074006828", "req-ogrn"),
    ("ОКПО", "66174670", "req-okpo"),
    ("Дата регистрации", "8 июля 2010 года", None),
    ("ОКВЭД", "17.29 — производство прочих изделий из бумаги и картона", None),
    ("Руководитель", "Зубко Руслан Александрович, генеральный директор", None),
])}
</div>
<div class="requisites-block" data-reveal>
<div class="requisites-block__head"><h2 class="requisites-block__title">Адрес</h2><span class="mono">02 / 04</span></div>
{spec_table([
    ("Юридический адрес", ADDRESS, "req-address"),
    ("Фактический адрес", ADDRESS, "req-address-2"),
    ("Регион", "Московская область, г. Подольск, мкр. Климовск", None),
])}
</div>
<div class="requisites-block" data-reveal>
<div class="requisites-block__head"><h2 class="requisites-block__title">Банковские реквизиты</h2><span class="mono">03 / 04</span></div>
<p class="lead">Банковские реквизиты предоставим по запросу. Позвоните или напишите на почту — отправим карточку предприятия.</p>
<div class="contact-cta">
<a class="btn btn--sm" href="{PHONE_HREF}">{PHONE}</a>
<a class="btn btn--sm btn--ghost" href="mailto:brizpak@list.ru">Почта</a>
</div>
</div>
<div class="requisites-block" data-reveal>
<div class="requisites-block__head"><h2 class="requisites-block__title">Для закупок</h2><span class="mono">04 / 04</span></div>
<p class="lead">Готовы предоставить карточку предприятия, документы на продукцию и закрывающие документы. Работаем с юридическими лицами и государственными заказчиками.</p>
<p class="requisites-note">Информация актуальна на 1 ноября 2026 года. Если заметили расхождение, сообщите нам.</p>
</div>
</div>
</section>
<section class="section section--cream">
<div class="container">{page_cta("Нужны <em>документы?</em>", "Подготовим карточку предприятия и комплект для закупки.", "Другое")}</div>
</section>"""
    extra = breadcrumb_jsonld([("Главная", "index.html"), ("Реквизиты", "requisites.html")])
    return page("requisites", "Реквизиты ООО «БРИЗ» — ИНН, ОГРН, адрес",
                "Реквизиты ООО «БРИЗ»: ИНН 5051321330, КПП 502101001, ОГРН 1105074006828, ОКПО 66174670. Адрес: Климовск, ул. Ленина, 1к13.",
                content, overlay=False, body_class="page-requisites", extra_head=extra)


def privacy():
    hero = page_hero(
        "Политика <em>конфиденциальности</em>",
        "Как обрабатываются данные, которые вы оставляете на сайте.",
        "Документы",
        plain=True,
        short=True,
        crumbs=[("Главная", "index.html"), ("Политика конфиденциальности", None)],
    )
    privacy_prose = prose("""
<p class="mono" style="color:var(--muted)">Редакция от 1 ноября 2026 года</p>
<h2>1. Общие положения</h2>
<p>Настоящая политика описывает, как ООО «БРИЗ» (ИНН 5051321330, ОГРН 1105074006828, адрес: 142180, Московская область, г. Подольск, мкр. Климовск, ул. Ленина, 1к13) обрабатывает персональные данные посетителей сайта.</p>
<p>Политика составлена в соответствии с Федеральным законом от 27.07.2006 № 152-ФЗ «О персональных данных».</p>
<h2>2. Какие данные мы получаем</h2>
<p>Вы можете оставить имя, название компании, телефон, что интересует, и комментарий. Эти данные вы указываете добровольно.</p>
<p>Сайт не использует системы аналитики и рекламные трекеры. Мы не собираем данные о вашем поведении на сайте.</p>
<h2>3. Зачем нужны данные</h2>
<p>Чтобы ответить на обращение, подготовить расчёт, согласовать условия и выполнить договор. Мы не используем данные для рассылок без отдельного согласия.</p>
<h2>4. Как работает форма</h2>
<p>Форма на сайте не отправляет данные на сервер. Она формирует текст сообщения, который вы можете отправить нам на почту. До отправки вы видите итоговый текст.</p>
<p>Обработка данных приёмлема в рамках почтовой переписки. Рекомендуем ознакомиться с регламентом до отправки.</p>
<h2>5. Передача данных</h2>
<p>Мы не передаём данные третьим лицам, кроме случаев, предусмотренных законом, или когда это необходимо для исполнения договора.</p>
<h2>6. Сроки хранения</h2>
<p>Храним данные не дольше, чем нужно для ответа на обращение и исполнения договора, если закон не требует иного.</p>
<h2>7. Ваши права</h2>
<p>Вы можете запросить информацию об обработке, уточнить или удалить данные. Для этого позвоните по телефону <a href="tel:+74959562028">+7 495 956-20-28</a> или напишите на почту <a href="mailto:brizpak@list.ru">brizpak@list.ru</a>.</p>
<h2>8. Карты и внешние сервисы</h2>
<p>На странице контактов встроена карта Яндекс.Карт. При её загрузке Яндекс может обрабатывать технические данные в соответствии со своей политикой конфиденциальности.</p>
<h2>9. Изменения</h2>
<p>Актуальная версия политики размещена на этой странице. Дата последнего обновления — 1 ноября 2026 года.</p>
""")
    content = f"""{hero}
<section class="section section--paper">
<div class="container container--narrow">
{privacy_prose}
</div>
</section>"""
    extra = breadcrumb_jsonld([("Главная", "index.html"), ("Политика конфиденциальности", "privacy.html")])
    return page("privacy", "Политика конфиденциальности | БРИЗ",
                "Политика конфиденциальности сайта ООО «БРИЗ»: какие данные обрабатываются, как работает форма и почта, права посетителя.",
                content, overlay=False, body_class="page-privacy", extra_head=extra)


def error_404():
    content = f"""<section class="error-page">
<div class="error-page__media">{img("factory-floor", "Производственный участок", eager=True)}</div>
<div class="container error-page__content">
<p class="mono" style="color:rgba(240,231,213,.55)">404 / Не найдено</p>
<div class="error-page__code" aria-hidden="true">404</div>
<h1>Страница ушла <em>в тираж</em>.</h1>
<p>Возможно, она переехала, была удалена или вы ошиблись адресом. Начните с главной — или посмотрите, чем мы занимаемся.</p>
<div class="error-page__actions">
<a class="btn btn--light" href="index.html">На главную</a>
<a class="btn" href="capabilities.html" style="--btn-bg:transparent;--btn-color:#f0e7d5;--btn-border:rgba(240,231,213,.4)">Возможности</a>
</div>
</div>
</section>"""
    return page("404", "Страница не найдена | БРИЗ",
                "Страница не найдена. Вернитесь на главную сайта ООО «БРИЗ» или посмотрите производственные возможности компании.",
                content, overlay=True, body_class="page-error", noindex=True)
