# -*- coding: utf-8 -*-
"""v13 — same structure as v12 (Home · Work · Properties · About · Contact), editorial copy.
Rules: no invented figures; architecture first; Espacios y Formas stated plainly, once per page at most."""
import pages as P          # helpers only: phero, form, contact_band
import projects, projects_v13, listings, fichas

HZ = "img/hero-casa-jalpa.jpg"
EYF = "https://www.espaciosyformas.com.mx/"
SEL_WORK = ["casa-horizonte", "casa-ether", "bar-bachus", "casa-travertino", "hotel-casa-x", "casa-cuadrante"]
SEL_PROPS = ("casa-horizonte", "casa-travertino", "casa-mirador")

def shead(num, txt, extra=""):
    return f'<div class="shead rv"{extra}><div class="eyebrow"><b>{num}</b>{txt}</div><i></i></div>'

def dev_card(id_, logo, name, place, status, text, imgs, ctas, auto=4500):
    sl = "".join(f'<div class="sl"><img src="{i}" alt="{name}"></div>' for i in imgs)
    return f"""
      <article class="dev dev2 rv" id="{id_}">
        <div class="dev-car car h520" data-auto="{auto}">
          <div class="trk">{sl}</div>
          <button class="arr l" aria-label="Previous">‹</button><button class="arr r" aria-label="Next">›</button>
          <div class="dots"></div>
        </div>
        <div class="dev-bd">
          <div class="dev-row">
            <div class="dev-brand">{('<img src="'+logo+'" alt="'+name+'">') if logo else '<b>'+name+'</b>'}</div>
            <div><div class="dev-meta"><span>{place}</span><span>{status}</span></div><p>{text}</p><div class="dev-cta">{ctas}</div></div>
          </div>
        </div>
      </article>"""

# ───────────────────────────── HOME ─────────────────────────────
def home(wa, SITE):
    body = f"""
<header class="hero home" id="top">
  <div class="bg" style="background-image:url('{HZ}')"></div>
  <div class="in">
    <div class="rbc">RBC</div>
    <h1>Roberto Balderas Carrillo</h1>
    <div class="role">Arquitecto</div>
    <p class="sub">Architecture and construction, with an architect's perspective on property.</p>
    <div class="meta"><span>San Miguel de Allende · Bajío · México</span><a href="work.html">Work ↓</a></div>
  </div>
</header>

<section id="selected-work">
  <div class="wrap">
    {shead("01","Selected work")}
    {projects.selected(SEL_WORK)}
    <div class="scale rv"><span>Architecture · Interiors · Construction</span><a href="work.html" style="color:var(--navy);text-decoration:none;">All projects →</a></div>
  </div>
</section>

<section class="band" id="areas">
  <div class="wrap">
    {shead("02","RBC")}
    <div class="split rv d1" style="align-items:start;">
      <h2>Each project develops its own architectural language.</h2>
      <p class="lead">RBC is the practice of Roberto Balderas Carrillo, architect. Houses, interiors and buildings, from the first drawing to the finished site — in collaboration with Espacios y Formas, an architecture, construction and development firm with offices in Celaya and San Miguel de Allende.</p>
    </div>
    <div class="doors">
      <a class="door rv" href="work.html"><img src="img/ig-DJ-iHIEx2Xi-1.jpg" alt="Architecture" loading="lazy"><div class="door-t"><small>01</small><b>Architecture</b><span>Houses, interiors, landscape, buildings.</span></div></a>
      <a class="door rv d1" href="properties.html"><img src="img/ig-DceaktFmAgJ-3.jpg" alt="Properties" loading="lazy"><div class="door-t"><small>02</small><b>Properties</b><span>A short selection, read by an architect.</span></div></a>
      <a class="door rv d2" href="work.html#construction"><img src="img/ph-penas-obra-b-06.jpg" alt="Construction" loading="lazy"><div class="door-t"><small>03</small><b>Construction</b><span>Directed personally; built with Espacios y Formas.</span></div></a>
    </div>
  </div>
</section>

<section id="properties">
  <div class="wrap">
    {shead("03","Selected properties")}
    <div class="split rv d1" style="align-items:start;">
      <h2>A few properties, known well.</h2>
      <p class="lead">Houses Roberto designed, built or knows well enough to represent. Each sheet carries plans, an architectural reading and his notes.</p>
    </div>
    """ + fichas.grid([l for l in listings.L if l['slug'] in SEL_PROPS], wa) + f"""
    <div style="margin-top:26px;" class="rv"><a class="btn ghost" href="properties.html">All selected properties</a></div>
  </div>
</section>

<section class="band" id="entry">
  <div class="wrap">
    {shead("04","Contact")}
    <div class="intents">
      <a class="intent" href="contact.html#project"><small>Start a project</small><b>A house, a renovation, a building.</b></a>
      <a class="intent" href="contact.html#buy"><small>Buy</small><b>A selected property, or one you found.</b></a>
      <a class="intent" href="contact.html#sell"><small>Sell</small><b>Have Roberto look at it first.</b></a>
      <a class="intent" href="contact.html#general"><small>General</small><b>Developers, brands, press.</b></a>
    </div>
  </div>
</section>
""" + fichas.modal_data([l for l in listings.L if l['slug'] in SEL_PROPS], wa)
    return ("index",
            "Roberto Balderas Carrillo, Arquitecto — Architecture, Construction and Selected Properties in San Miguel de Allende | RBC",
            "RBC is the architecture practice of Roberto Balderas Carrillo in San Miguel de Allende: architectural design, interiors, construction and a small selection of properties read with an architect's eye. In collaboration with Espacios y Formas.",
            body, HZ, "org", "1.0")

# ───────────────────────────── WORK ─────────────────────────────
def work(wa, SITE):
    body = P.phero("img/hero-terrace-sunset.jpg", "RBC / Work", "Work.",
        "Houses, hotels, bars, stores, offices and residential developments — San Miguel de Allende, the Bajío and beyond.",
        '<a href="index.html">Home</a> › Work') + projects_v13.arch_section("01") + projects_v13.construction_section("02") + \
        P.contact_band(wa, "Start a project", "Tell me about the site.",
        "A lot, a house to renovate, a building to plan. English and Spanish.",
        "Hi Roberto, I would like to talk about a project.", "WhatsApp Roberto")
    ld = [{"@context":"https://schema.org","@type":"CollectionPage","name":"Work — RBC Roberto Balderas Carrillo, Arquitecto","url":f"{SITE}/work.html"},
          {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"},{"@type":"ListItem","position":2,"name":"Work","item":f"{SITE}/work.html"}]}]
    return ("work", "Work — Architecture, Interiors and Construction by Roberto Balderas Carrillo | RBC",
            "Architecture, interior and construction projects by architect Roberto Balderas Carrillo in San Miguel de Allende, Querétaro, Celaya and beyond: houses, hotels, bars, stores, offices and residential developments.",
            body, "img/hero-terrace-sunset.jpg", ld, "0.9")

# ───────────────────────────── PROPERTIES ─────────────────────────────
def properties(wa, SITE):
    sma = listings.by('sma','sale'); rent = listings.by('sma','rent')
    devs = dev_card("penas-arriba", "img/penas-arriba-logo.png", "Peñas Arriba", "San Miguel de Allende", "RBC with Espacios y Formas",
        "A gated community on the hillside above San Miguel de Allende, with views of the Parroquia. Houses, shell-built homes and lots.",
        ["img/ph-penas-obra-b-06.jpg","img/ig-DceaktFmAgJ-1.jpg","img/ph-penas-obra-b-07.jpg","img/penas-arriba-map-casa-horizonte.jpg"],
        '<a class="btn red" href="https://penasarriba.vercel.app/" target="_blank" rel="noopener">Community site →</a><a class="btn ghost" href="#selected">Houses on this site</a>', 4200) + \
    dev_card("magno", "img/magno-logo-white.png", "Magno Home &amp; Towers", "Celaya · Guanajuato", "Espacios y Formas",
        "Residential towers, single-family homes and lots in one gated community, with spa, pool, gym and clubhouse. Apartments available for immediate delivery. Lots from MX $2.0M · apartments from MX $4.3M · homes from MX $5.5M.",
        ["img/magno-4.jpg","img/magno-2.jpg","img/magno-5.jpg","img/magno-8.jpg"],
        f'<a class="btn red" href="https://magnoresidencial.com/" target="_blank" rel="noopener">Sales site →</a><a class="btn ghost" href="{wa("Hi Roberto, I would like the current inventory of apartments, homes and lots in Magno, Celaya.")}">Ask for inventory</a>', 4600) + \
    dev_card("escondida", "", "La Escondida &amp; La Nueva Escondida", "San Miguel de Allende", "In development",
        "Two residential developments in San Miguel de Allende. Details to follow.",
        ["img/community-trails.jpg","img/valley-golden-hour.jpg"],
        f'<a class="btn" href="{wa("Hi Roberto, please keep me informed about La Escondida and La Nueva Escondida in San Miguel.")}">Keep me informed</a>', 5000)

    body = P.phero("img/luxury-home-san-miguel-de-allende-terrace.jpg", "RBC / Properties", "Selected properties.",
        "Fewer properties, known in more depth.",
        '<a href="index.html">Home</a> › Properties') + f"""
<section id="selected">
  <div class="wrap">
    {shead("01","San Miguel de Allende")}
    <div class="split rv d1" style="align-items:start;">
      <h2>Houses for sale.</h2>
      <p class="lead">Some Roberto designed, some were built with Espacios y Formas, some belong to clients. Each sheet states its authorship, and carries his notes.</p>
    </div>
    """ + fichas.grid(sma, wa) + f"""
    <div class="cap rv" style="margin-top:14px;">Prices in MXN; USD approximate · Open a sheet for plans, program, an architect's reading and the PDF</div>

    {shead("02","Countryside near San Miguel · Querétaro", ' style="margin-top:60px;"')}
    """ + fichas.grid(listings.by('jalpa','sale') + listings.by('qro','sale'), wa) + f"""

    {shead("03","Mid-term stays · historic center", ' style="margin-top:60px;"')}
    """ + fichas.grid(rent, wa) + f"""
  </div>
</section>

<section class="band" id="developments">
  <div class="wrap">
    {shead("04","Developments")}
    <div class="devs">{devs}</div>
  </div>
</section>

<section id="reading">
  <div class="wrap split" style="align-items:start;">
    <div class="rv">
      {shead("05","Roberto's Notes")}
      <h2>Before the transaction, the building.</h2>
    </div>
    <div class="rv d1">
      <p class="lead">Every sheet is read the way an architect reads a house: plan and light, structure and materials, the lot and its slope, what could change. The notes are Roberto's own.</p>
      <div style="margin-top:18px;"><a class="btn" href="contact.html#buy">Ask Roberto to look at a property</a></div>
    </div>
  </div>
</section>

<section class="band" id="sell">
  <div class="wrap split" style="align-items:start;">
    <div class="rv">
      {shead("06","Sell")}
      <h2>Have Roberto look at it first.</h2>
      <p class="lead">RBC represents a short list, after a visit.</p>
    </div>
    <div class="rv d1">
      {P.form("Your property", "Goes to Roberto's WhatsApp.",
        [("row",[("text","Name","Your name","Jane Smith"),("select","Location","Where is the property",["San Miguel de Allende","Querétaro","Celaya","Elsewhere in the Bajío"])]),
         ("row",[("select","Type","Type",["House","Apartment","Lot","Commercial","Other"]),("select","Goal","What you'd like",["Sell","Rent","An architect's opinion first","Not sure yet"])]),
         ("area","Details","Describe it","Size, year built, condition, anything special…")],
        "Hi Roberto, I have a property I'd like you to look at:", "Send to Roberto")}
    </div>
  </div>
</section>
""" + fichas.modal_data(listings.L, wa)
    ld = [{"@context":"https://schema.org","@type":"ItemList","name":"Selected properties — RBC",
      "itemListElement":[{"@type":"ListItem","position":i+1,"name":f"{l['name']} — {l['where']}","url":f"{SITE}/{l['slug']}.html" if l.get('page') else f"{SITE}/properties.html#{l['slug']}"} for i,l in enumerate(listings.L)]},
      {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"},{"@type":"ListItem","position":2,"name":"Properties","item":f"{SITE}/properties.html"}]}]
    return ("properties",
            "Selected Properties in San Miguel de Allende — Homes for Sale, Read by an Architect | RBC",
            "A short selection of houses for sale and rent in San Miguel de Allende, its countryside and Querétaro, presented by architect Roberto Balderas Carrillo with plans, an architectural reading and Roberto's Notes on each property.",
            body, "img/luxury-home-san-miguel-de-allende-terrace.jpg", ld, "0.9")

# ───────────────────────────── ABOUT ─────────────────────────────
def about(wa, SITE):
    body = P.phero("img/valley-golden-hour.jpg", "RBC / About", "Roberto Balderas Carrillo, Arquitecto.",
        "San Miguel de Allende · Bajío · México",
        '<a href="index.html">Home</a> › About') + f"""
<section id="bio">
  <div class="wrap about">
    <div class="rv">
      <img class="portrait" src="img/portrait-roberto-2.jpg" alt="Roberto Balderas Carrillo" loading="lazy">
    </div>
    <div class="rv d1">
      {shead("01","Roberto")}
      <p class="lead">Roberto Balderas Carrillo is an architect from Celaya, Guanajuato, based in San Miguel de Allende. RBC is his practice: the projects he authors, the buildings he directs on site, and a short list of properties he represents because he knows them.</p>
      <div class="notes"><small>Criterion</small><p>Every project answers its site, its client, its budget and its scale. Each one develops its own architectural language.</p></div>

      {shead("02","Espacios y Formas")}
      <p class="lead">RBC works in close collaboration with <a href="{EYF}" target="_blank" rel="noopener">Espacios y Formas</a>, an architecture, construction and development firm with more than three decades of work across the Bajío. Principal office in Celaya; presence in San Miguel de Allende.</p>
      <div class="facts">
        <div><small>Offices</small><span>San Miguel de Allende / Celaya</span></div>
        <div><small>Work</small><span>Architecture · Interiors · Landscape · Construction · Development · Selected properties</span></div>
        <div><small>Contact</small><span>WhatsApp · @arqrobertobalderas</span></div>
      </div>
      <div style="margin-top:26px;display:flex;gap:10px;flex-wrap:wrap;">
        <a class="btn red" href="{wa('Hi Roberto, I read your About page and I would like to talk.')}">WhatsApp</a>
        <a class="btn ghost" href="https://www.instagram.com/arqrobertobalderas" target="_blank" rel="noopener">@arqrobertobalderas</a>
        <a class="btn ghost" href="{EYF}" target="_blank" rel="noopener">espaciosyformas.com.mx ↗</a>
      </div>
    </div>
  </div>
</section>
"""
    ld = [{"@context":"https://schema.org","@type":"Person","name":"Roberto Balderas Carrillo","jobTitle":"Architect","url":f"{SITE}/about.html","worksFor":{"@type":"Organization","name":"RBC · Roberto Balderas Carrillo, Arquitecto","url":f"{SITE}/"},"affiliation":{"@type":"Organization","name":"Espacios y Formas","url":EYF},"sameAs":["https://www.instagram.com/arqrobertobalderas"],"address":{"@type":"PostalAddress","addressLocality":"San Miguel de Allende","addressRegion":"Guanajuato","addressCountry":"MX"}},
          {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"},{"@type":"ListItem","position":2,"name":"About","item":f"{SITE}/about.html"}]}]
    return ("about", "About — Roberto Balderas Carrillo, Arquitecto | RBC",
            "Roberto Balderas Carrillo is an architect based in San Miguel de Allende. RBC is his practice, working in close collaboration with Espacios y Formas, an architecture, construction and development firm.",
            body, "img/valley-golden-hour.jpg", ld, "0.7")

# ───────────────────────────── CONTACT ─────────────────────────────
def contact(wa, SITE):
    F = P.form
    body = P.phero("img/sunset-terrace-luxury-villa-mexico.jpg", "RBC / Contact", "Tell me what you have in mind.",
        "WhatsApp is fastest. English and Spanish.",
        '<a href="index.html">Home</a> › Contact') + f"""
<section id="doors">
  <div class="wrap">
    <div class="intents rv">
      <a class="intent" href="#project"><small>01</small><b>Start a project</b></a>
      <a class="intent" href="#buy"><small>02</small><b>Buy a property</b></a>
      <a class="intent" href="#sell"><small>03</small><b>Sell a property</b></a>
      <a class="intent" href="#general"><small>04</small><b>General inquiry</b></a>
    </div>
    <div style="margin-top:26px;display:flex;gap:12px;flex-wrap:wrap;align-items:center;" class="rv">
      <a class="btn red" href="{wa('Hi Roberto, I found your website and I would like to talk.')}">WhatsApp Roberto</a>
      <span class="code">Roberto replies personally · Video calls for clients abroad</span>
    </div>
  </div>
</section>

<section class="band" id="project">
  <div class="wrap split" style="align-items:start;">
    <div class="rv">{shead("01","Start a project")}<h2>Design and build.</h2><p class="lead">A lot, a sketch or an idea.</p></div>
    <div class="rv d1">{F("Project", "",
        [("row",[("text","Name","Your name","Jane Smith"),("select","Location","Where",["San Miguel de Allende","Querétaro","Celaya","Elsewhere in the Bajío","Elsewhere in Mexico","I don't have a lot yet"])]),
         ("row",[("select","Scope","What you need",["Design + construction","Design only","Construction from my plans","Renovation / restoration","A reading of my lot","A building / development"]),("select","Budget","Budget (USD)",["Under $300K","$300K – $600K","$600K – $1.2M","Over $1.2M","Not sure yet"])]),
         ("area","Details","Tell me about it","")], "Hi Roberto, I'd like to start a project:", "Send to Roberto")}</div>
  </div>
</section>
<div id="land"></div>

<section id="buy">
  <div class="wrap split" style="align-items:start;">
    <div class="rv">{shead("02","Buy a property")}<h2>With an architect's reading.</h2><p class="lead">A selected property, or one you found elsewhere.</p></div>
    <div class="rv d1">{F("Buying", "",
        [("row",[("text","Name","Your name","Jane Smith"),("select","City","City",["San Miguel de Allende","Querétaro","Celaya","Not sure yet"])]),
         ("row",[("select","Budget","Budget (USD)",["Under $400K","$400K – $800K","$800K – $1.5M","$1.5M – $3M","Over $3M"]),("select","When","When",["As soon as possible","3–6 months","6–12 months","Exploring"])]),
         ("area","Details","What matters most, or a link to a property","")], "Hi Roberto, I'm looking to buy:", "Send to Roberto")}</div>
  </div>
</section>

<section class="band" id="sell">
  <div class="wrap split" style="align-items:start;">
    <div class="rv">{shead("03","Sell a property")}<h2>Have it looked at first.</h2><p class="lead">A short list, after a visit.</p></div>
    <div class="rv d1">{F("Selling", "",
        [("row",[("text","Name","Your name","Jane Smith"),("select","Location","Where",["San Miguel de Allende","Querétaro","Celaya","Elsewhere in the Bajío"])]),
         ("row",[("select","Type","Type",["House","Apartment","Lot","Commercial","Other"]),("select","Goal","Goal",["Sell","Rent","An opinion first"])]),
         ("area","Details","Describe the property","")], "Hi Roberto, I have a property I'd like you to look at:", "Send to Roberto")}</div>
  </div>
</section>

<section id="general">
  <div class="wrap split" style="align-items:start;">
    <div class="rv">{shead("04","General inquiry")}<h2>Anything else.</h2>
      <div class="facts"><div><small>WhatsApp</small><span><button class="tel-reveal" data-t="KzUyIDQ2MSAxMDEgMjQ3NA==">Show number</button></span></div><div><small>Instagram</small><span>@arqrobertobalderas</span></div><div><small>Offices</small><span>San Miguel de Allende / Celaya</span></div></div></div>
    <div class="rv d1">{F("Message", "",
        [("row",[("text","Name","Your name","Jane Smith"),("text","Contact","Best way to reach you","Phone or email")]),
         ("area","Message","Message","")], "Hi Roberto, I'm writing from your website:", "Send to Roberto")}</div>
  </div>
</section>
"""
    ld = [{"@context":"https://schema.org","@type":"ContactPage","url":f"{SITE}/contact.html","name":"Contact Roberto Balderas Carrillo, Arquitecto"},
          {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"},{"@type":"ListItem","position":2,"name":"Contact","item":f"{SITE}/contact.html"}]}]
    return ("contact", "Contact — Start a Project, Buy or Sell a Property | RBC · Roberto Balderas Carrillo, Arquitecto",
            "Contact architect Roberto Balderas Carrillo in San Miguel de Allende: start a design-and-build project, ask for a reading of your lot, buy a selected property or have a property looked at for sale..",
            body, "img/sunset-terrace-luxury-villa-mexico.jpg", ld, "0.6")

# ───────────────────────────── REDIRECTS ─────────────────────────────
def redirect(slug, to):
    body = f'<meta http-equiv="refresh" content="0; url={to}"><div class="wrap" style="padding:140px 32px;"><p class="lead">This page moved to <a href="{to}">{to}</a>.</p></div>'
    return (slug, "Redirecting — RBC", "This page has moved.", body, HZ, [], "0.1")

REDIRECTS = (("real-estate","properties.html"),("roberto-balderas-carrillo","about.html"),
             ("architecture","work.html"),("construction","work.html#construction"),("development","properties.html#developments"))

def build(page, wa, ORG, SITE):
    urls = []
    for fn in (home, work, properties, about, contact):
        slug, title, desc, body, og, ld, pr = fn(wa, SITE)
        if ld == "org": ld = [ORG]
        urls.append((page(slug, title, desc, body, og, ld, active=slug + ".html"), pr))
    for l in listings.pages():
        slug, title, desc, body, og, ld, pr = listings.property_page(l, wa, SITE)
        urls.append((page(slug, title, desc, body, og, ld, active="properties.html"), pr))
    for slug, to in REDIRECTS:
        s, t, d, b, o, ld, pr = redirect(slug, to)
        page(s, t, d, b, o, ld, active="", extra_head='<meta name="robots" content="noindex">')
    urls.append((f"{SITE}/privacy.html", "0.2")); urls.append((f"{SITE}/terms.html", "0.2"))
    return urls
