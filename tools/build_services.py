"""Genera las páginas de detalle de servicios en /servicios a partir de los datos de abajo.

Uso: python3 tools/build_services.py
Para cambiar textos, editá PAGES y volvé a correr el script.
"""
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent


def sel(word):
    return f'<span class="sel"><i></i>{word}<i></i></span>'


# Cada texto va como (español, inglés).
PAGES = [
    {
        "file": "diseno-web.html",
        "title": ("Diseño web · Victorina Carelli UX", "Web design · Victorina Carelli UX"),
        "color": "var(--lila)",
        "eyebrow": ("Servicios · Diseño web", "Services · Web design"),
        "h1": ("Tu web, lista para " + sel("vender"), "A website ready to " + sel("sell")),
        "lead": (
            "Webs diseñadas con criterio UX y construidas con IA. Rápidas, lindas y fáciles de actualizar, sin depender de un programador.",
            "Websites designed with UX thinking and built with AI. Fast, beautiful and easy to update, with no developer needed.",
        ),
        "pains_title": ("Es para vos si…", "It's for you if…"),
        "pains": [
            ("No tenés web o la que tenés quedó vieja", "You don't have a website, or yours is outdated"),
            ("Instagram no alcanza para mostrar lo que hacés", "Instagram isn't enough to show what you do"),
            ("Querés vender un servicio o un lanzamiento", "You want to sell a service or a launch"),
            ("No querés depender de un programador", "You don't want to depend on a developer"),
        ],
        "offers": [
            {
                "id": "marca-personal", "need": "w1",
                "name": ("Web de marca personal", "Personal brand website"),
                "for": ("Para profesionales y emprendedores que quieren mostrar su trabajo y recibir clientes. Como esta web.",
                        "For professionals and founders who want to show their work and get clients. Like this website."),
                "includes": [
                    ("Estructura y textos pensados en UX", "UX-driven structure and copy"),
                    ("Diseño a medida, en uno o dos idiomas", "Custom design, in one or two languages"),
                    ("Formulario de contacto que te avisa por mail", "Contact form that emails you"),
                    ("Publicación con tu dominio", "Published on your own domain"),
                    ("30 días de ajustes después de publicar", "30 days of tweaks after launch"),
                ],
                "meta": [(("Duración", "Timeline"), ("2 a 3 semanas", "2 to 3 weeks")), (("Formato", "Format"), ("Online", "Remote"))],
                "price": (("desde", "from"), "USD —"),
            },
            {
                "id": "landing", "need": "w2",
                "name": ("Landing de conversión", "Conversion landing page"),
                "for": ("Para lanzamientos, campañas o un servicio puntual. Una página con un solo objetivo: que te contacten, se registren o compren.",
                        "For launches, campaigns or a single service. One page with one goal: get people to contact you, sign up or buy."),
                "includes": [
                    ("Un objetivo claro y una sola llamada a la acción", "One clear goal and a single call to action"),
                    ("Textos persuasivos con foco en conversión", "Persuasive copy focused on conversion"),
                    ("Conexión con formulario, WhatsApp o pagos", "Hooked up to a form, WhatsApp or payments"),
                    ("Métricas para medir resultados", "Analytics to measure results"),
                ],
                "meta": [(("Duración", "Timeline"), ("1 a 2 semanas", "1 to 2 weeks")), (("Formato", "Format"), ("Online", "Remote"))],
                "price": (("desde", "from"), "USD —"),
            },
        ],
        "steps": [
            (("Charla inicial", "Kick-off call"), ("Me contás tu negocio, tu público y qué querés lograr.", "You tell me about your business, audience and goals.")),
            (("Estructura y textos", "Structure and copy"), ("Armo el mapa de la web y los mensajes clave.", "I map out the site and its key messages.")),
            (("Diseño y desarrollo", "Design and build"), ("Diseño la web y la construyo con IA. Vos la ves avanzar.", "I design the site and build it with AI. You watch it take shape.")),
            (("Revisión y publicación", "Review and launch"), ("Ajustamos los detalles y la publicamos con tu dominio.", "We polish the details and launch it on your domain.")),
        ],
    },
    {
        "file": "asesorias.html",
        "title": ("Asesorías 1:1 · Victorina Carelli UX", "1:1 sessions · Victorina Carelli UX"),
        "color": "var(--lima)",
        "eyebrow": ("Servicios · Asesorías 1:1", "Services · 1:1 sessions"),
        "h1": ("Una sesión, mucha " + sel("claridad"), "One session, lots of " + sel("clarity")),
        "lead": (
            "Videollamadas personalizadas donde revisamos tu caso y te llevás recomendaciones concretas para aplicar al día siguiente.",
            "Personal video calls where we review your case and you leave with concrete advice to apply the next day.",
        ),
        "pains_title": ("Es para vos si…", "It's for you if…"),
        "pains": [
            ("Tenés una idea y no sabés por dónde arrancar", "You have an idea and don't know where to start"),
            ("Tu web o app no convierte y no sabés por qué", "Your website or app doesn't convert and you don't know why"),
            ("Mandás CVs y no te llaman", "You send out CVs and don't hear back"),
            ("Tu portfolio no muestra cómo pensás", "Your portfolio doesn't show how you think"),
        ],
        "offers": [
            {
                "id": "producto", "need": "a1",
                "name": ("Asesoría de producto digital", "Digital product session"),
                "for": ("Para marcas y emprendedores con una web o app en marcha o por lanzar.",
                        "For brands and founders with a website or app that is live or about to launch."),
                "includes": [
                    ("Revisión previa de tu web o app", "A review of your website or app before we meet"),
                    ("Sesión en vivo con recomendaciones", "A live session with recommendations"),
                    ("Informe con mejoras priorizadas", "A report with prioritized improvements"),
                    ("Una semana de consultas por WhatsApp", "One week of follow-up questions on WhatsApp"),
                ],
                "meta": [(("Duración", "Length"), ("90 minutos", "90 minutes")), (("Formato", "Format"), ("Videollamada", "Video call"))],
                "price": (("desde", "from"), "USD —"),
            },
            {
                "id": "disenadores", "need": "a2",
                "name": ("Asesoría para diseñadores", "Session for designers"),
                "for": ("Para diseñadores UX/UI que buscan su primer trabajo o quieren dar el próximo paso.",
                        "For UX/UI designers looking for their first job or their next step."),
                "includes": [
                    ("Revisión de tu perfil de LinkedIn", "A review of your LinkedIn profile"),
                    ("Feedback sobre tu CV", "Feedback on your CV"),
                    ("Revisión de tu portfolio y tus casos", "A review of your portfolio and case studies"),
                    ("Un plan de mejoras concreto", "A concrete improvement plan"),
                ],
                "meta": [(("Duración", "Length"), ("60 minutos", "60 minutes")), (("Formato", "Format"), ("Videollamada", "Video call"))],
                "price": (("desde", "from"), "USD —"),
            },
        ],
        "steps": [
            (("Reservás tu sesión", "Book your session"), ("Me escribís y elegimos día y horario.", "Message me and we pick a date and time.")),
            (("Me mandás tu material", "Send me your material"), ("Tu web, app, LinkedIn, CV o portfolio, según la asesoría.", "Your website, app, LinkedIn, CV or portfolio, depending on the session.")),
            (("Sesión en vivo", "Live session"), ("Revisamos todo juntos y respondo tus dudas.", "We go through everything together and I answer your questions.")),
            (("Plan de acción", "Action plan"), ("Te llevás los próximos pasos por escrito.", "You leave with your next steps in writing.")),
        ],
    },
    {
        "file": "corporativas.html",
        "title": ("Asesorías corporativas · Victorina Carelli UX", "Corporate consulting · Victorina Carelli UX"),
        "color": "var(--amarillo)",
        "eyebrow": ("Servicios · Para empresas", "Services · For companies"),
        "h1": ("UX para " + sel("equipos"), "UX for " + sel("teams")),
        "lead": (
            "Ayudo a empresas y equipos a diseñar productos más fáciles de usar, con una mirada externa y métodos probados.",
            "I help companies and teams design products that are easier to use, with an outside view and proven methods.",
        ),
        "pains_title": ("Es para tu equipo si…", "It's for your team if…"),
        "pains": [
            ("El producto tiene problemas de usabilidad", "Your product has usability problems"),
            ("No tienen a alguien de UX en el equipo", "There's no UX person on the team"),
            ("Quieren capacitarse en diseño centrado en usuarios", "You want training in user-centered design"),
            ("Necesitan una mirada externa antes de lanzar", "You need an outside view before launch"),
        ],
        "offers": [
            {
                "id": "auditoria", "need": "corp",
                "name": ("Auditoría de producto", "Product audit"),
                "for": ("Para empresas con una web o app en funcionamiento que quieren saber qué mejorar primero.",
                        "For companies with a live website or app who want to know what to fix first."),
                "includes": [
                    ("Evaluación heurística completa", "A full heuristic evaluation"),
                    ("Análisis de los flujos clave", "Analysis of key user flows"),
                    ("Informe ejecutivo con prioridades", "An executive report with priorities"),
                    ("Presentación de resultados al equipo", "A results presentation for the team"),
                ],
                "meta": [(("Duración", "Timeline"), ("2 a 4 semanas", "2 to 4 weeks")), (("Formato", "Format"), ("Online", "Remote"))],
                "price": (("inversión", "investment"), ("Cotización a medida", "Custom quote")),
            },
            {
                "id": "workshops", "need": "corp",
                "name": ("Workshops para equipos", "Team workshops"),
                "for": ("Para equipos de producto, marketing o desarrollo, de 4 personas o más.",
                        "For product, marketing or development teams of 4 people or more."),
                "includes": [
                    ("Workshop a medida de tu equipo", "A workshop tailored to your team"),
                    ("Ejercicios prácticos con su propio producto", "Hands-on exercises with your own product"),
                    ("Material para seguir aplicando", "Materials to keep applying what you learn"),
                ],
                "meta": [(("Duración", "Length"), ("Medio día o jornada completa", "Half or full day")), (("Formato", "Format"), ("Online o presencial", "Remote or on site"))],
                "price": (("inversión", "investment"), ("Cotización a medida", "Custom quote")),
            },
            {
                "id": "acompanamiento", "need": "corp",
                "name": ("Acompañamiento UX", "Ongoing UX support"),
                "for": ("Para equipos que necesitan UX de forma continua sin sumar a alguien full time.",
                        "For teams who need UX on an ongoing basis without a full-time hire."),
                "includes": [
                    ("Horas mensuales de diseño y consultoría", "Monthly design and consulting hours"),
                    ("Research y tests con usuarios", "User research and testing"),
                    ("Seguimiento con métricas", "Follow-up with metrics"),
                ],
                "meta": [(("Duración", "Length"), ("Mensual", "Monthly")), (("Formato", "Format"), ("Online", "Remote"))],
                "price": (("inversión", "investment"), ("Cotización a medida", "Custom quote")),
            },
        ],
        "steps": [
            (("Primera reunión", "Intro meeting"), ("Entiendo el producto, el equipo y los objetivos.", "I learn about the product, the team and the goals.")),
            (("Propuesta", "Proposal"), ("Te envío alcance, tiempos y cotización.", "I send scope, timeline and a quote.")),
            (("Trabajo con el equipo", "Work with the team"), ("Avanzamos con entregas y reuniones de seguimiento.", "We move forward with deliverables and check-ins.")),
            (("Resultados", "Results"), ("Presentamos hallazgos y próximos pasos.", "We present findings and next steps.")),
        ],
    },
]

HEAD = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='16' fill='%23CDB8F6'/%3E%3Cpath d='M18 14l12 34 5-14 14-5z' fill='%232F6BFF' stroke='%231D1630' stroke-width='3' stroke-linejoin='round'/%3E%3C/svg%3E">
<meta name="theme-color" content="#FAF7F5">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Instrument+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
<header class="top">
  <div class="wrap">
    <a class="logo" href="/">victo<span>.</span>ux</a>
    <nav class="nav" aria-label="Secciones">
      <a href="/#portfolio" data-i18n="nav_portfolio">Portfolio</a>
      <a href="/#servicios" data-i18n="nav_services">Servicios</a>
      <a href="/#bio" data-i18n="nav_bio">Sobre mí</a>
      <a href="/#contacto" data-i18n="nav_contact">Contacto</a>
    </nav>
    <div class="lang" role="group" aria-label="Idioma / Language">
      <button type="button" id="lang-es" aria-pressed="true" data-lang="es">ES</button>
      <button type="button" id="lang-en" aria-pressed="false" data-lang="en">EN</button>
    </div>
    <a class="btn btn-primary btn-sm" href="/#contacto" data-i18n="cta_short">Presupuesto</a>
  </div>
</header>
"""


def build(page):
    es, en = {}, {}

    def key(k, pair):
        es[k], en[k] = pair
        return k

    def txt(k, pair, tag="span", cls=""):
        key(k, pair)
        c = f' class="{cls}"' if cls else ""
        return f'<{tag}{c} data-i18n="{k}">{html.escape(pair[0])}</{tag}>'

    key("page_title", page["title"])
    out = [HEAD.format(title=html.escape(page["title"][0]), desc=html.escape(page["lead"][0]))]
    out.append('<main>\n  <section class="hero d-hero">\n    <div class="wrap">')
    out.append('      <nav class="crumbs" aria-label="Ruta"><a href="/" data-i18n="crumb_home">Inicio</a><span>/</span>'
               '<a href="/#servicios" data-i18n="crumb_services">Servicios</a></nav>')
    out.append("      " + txt("eyebrow", page["eyebrow"], "p", "eyebrow"))
    key("h1", page["h1"])
    out.append(f'      <h1 data-i18n-html="h1">{page["h1"][0]}</h1>')
    out.append("      " + txt("lead", page["lead"], "p", "lead"))
    jumps = []
    for o in page["offers"]:
        jumps.append(f'<a href="#{o["id"]}" data-i18n="{o["id"]}_n">{html.escape(o["name"][0])}</a>')
    out.append('      <div class="jump">' + "".join(jumps) + "</div>")
    out.append('      <p><span class="sample" data-i18n="sample">Textos de ejemplo</span></p>')
    out.append("    </div>\n  </section>")

    # Pains
    out.append('  <section class="sec" style="padding-bottom:0"><div class="wrap">')
    out.append('    <div class="sec-head">' + txt("pains_t", page["pains_title"], "h2") + "</div>")
    out.append('    <div class="pains">')
    for i, p in enumerate(page["pains"]):
        out.append("      " + txt(f"pain{i}", p, "span", "pain"))
    out.append("    </div>\n  </div></section>")

    # Offers
    out.append('  <section class="sec"><div class="wrap offers">')
    for o in page["offers"]:
        oid = o["id"]
        key(f"{oid}_n", o["name"])
        out.append(f'    <article class="offer" id="{oid}">')
        out.append(f'      <div class="offer-head" style="background:{page["color"]}">')
        out.append(f'        <h2 data-i18n="{oid}_n">{html.escape(o["name"][0])}</h2>')
        out.append("        " + txt(f"{oid}_for", o["for"], "p", "for"))
        out.append("      </div>")
        out.append('      <div class="offer-body">')
        out.append("        " + txt("inc_t", ("Qué incluye", "What's included"), "h3"))
        out.append('        <ul class="checks">')
        for i, it in enumerate(o["includes"]):
            out.append("          " + txt(f"{oid}_i{i}", it, "li"))
        out.append("        </ul>")
        out.append('        <div class="meta">')
        for i, (label, val) in enumerate(o["meta"]):
            out.append(f'          <div>{txt(f"{oid}_ml{i}", label, "small")}{txt(f"{oid}_mv{i}", val, "strong")}</div>')
        out.append("        </div>")
        plabel, pval = o["price"]
        pval = pval if isinstance(pval, tuple) else (pval, pval)
        out.append('        <div class="offer-foot">')
        out.append(f'          <div class="price">{txt(f"{oid}_pl", plabel, "small")}{txt(f"{oid}_pv", pval, "strong")}</div>')
        out.append(f'          <a class="btn btn-primary" href="/#contacto" data-need="{o["need"]}">{txt("want", ("Quiero esta →", "I want this →"))}</a>')
        out.append("        </div>\n      </div>\n    </article>")
    out.append("  </div></section>")

    # Steps
    out.append('  <section class="sec" style="padding-top:0"><div class="wrap">')
    out.append('    <div class="sec-head">' + txt("steps_e", ("Proceso", "Process"), "p", "eyebrow")
               + txt("steps_t", ("¿Cómo trabajamos?", "How we work"), "h2") + "</div>")
    out.append('    <ol class="steps">')
    for i, (title, desc) in enumerate(page["steps"]):
        out.append(f'      <li>{txt(f"st{i}", title, "strong")}{txt(f"sd{i}", desc, "span")}</li>')
    out.append("    </ol>\n  </div></section>")

    # CTA
    out.append('  <section class="sec" style="padding-top:0"><div class="wrap">')
    out.append('    <div class="cta-band">')
    out.append("      " + txt("cta_t", ("¿Tenés dudas? Escribime", "Questions? Message me"), "h2"))
    out.append("      " + txt("cta_d", ("Te respondo en menos de 48 horas y vemos juntos qué opción te conviene.",
                                         "I reply within 48 hours and we'll figure out the best option together."), "p"))
    out.append(f'      <a class="btn" href="/#contacto">{txt("cta_b", ("Pedí tu presupuesto →", "Get a quote →"))}</a>')
    out.append("    </div>")
    out.append('    <footer class="mini-foot"><span>© 2026 Victorina Carelli</span><span data-i18n="foot">Diseñado con amor (y muchos post-its)</span></footer>')
    out.append("  </div></section>\n</main>")

    out.append("<script>window.PAGE_T = " + json.dumps({"es": es, "en": en}, ensure_ascii=False) + ";</script>")
    out.append('<script src="/assets/site.js"></script>\n</body>\n</html>\n')
    (ROOT / "servicios" / page["file"]).write_text("\n".join(out), encoding="utf-8")


if __name__ == "__main__":
    for p in PAGES:
        build(p)
        print("ok", p["file"])
