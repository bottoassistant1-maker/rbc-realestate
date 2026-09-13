# -*- coding: utf-8 -*-
"""v15 — three tabs: Architecture & Design · Real Estate · Construction.
Home = hero + a very short introduction (Roberto + integral work) + the three tabs as large doors."""
import pages as P          # helpers: phero, form, contact_band
import projects, projects_v13, listings, fichas
from pages_v12 import dev_card, shead, EYF, redirect

HERO = "img/hero-casa-jalpa.jpg"

# ───────────────────────────── HOME ─────────────────────────────
def home(wa, SITE):
    body = f"""
<header class="hero home" id="top">
  <div class="bg" style="background-image:url('{HERO}')"></div>
  <div class="in">
    <div class="rbc">RBC</div>
    <h1>Roberto Balderas Carrillo</h1>
    <div class="role">Arquitecto</div>
    <div class="meta"><span>San Miguel de Allende · Bajío · México</span><a href="#intro">↓</a></div>
  </div>
</header>

<section id="intro">
  <div class="wrap split" style="align-items:start;">
    <div class="rv">
      <div class="portrait sm">Portrait pending</div>
    </div>
    <div class="rv d1">
      <p class="lead big">Roberto Balderas Carrillo is an architect based in San Miguel de Allende. His practice, RBC, designs and builds — houses, interiors, hotels, commercial buildings — and represents a small selection of properties he knows well.</p>
      <p class="lead">Each project develops its own architectural language. Larger works are built with Espacios y Formas, architecture, construction and development, with offices in Celaya and San Miguel de Allende.</p>
      <div class="facts" style="margin-top:22px;"><div><small>Contact</small><span><a href="{wa('Hi Roberto, I found your website and I would like to talk.')}" style="color:var(--navy);text-decoration:none;">WhatsApp +52 461 101 2474</a> · <a href="https://www.instagram.com/arqrobertobalderas" target="_blank" rel="noopener" style="color:var(--navy);text-decoration:none;">@arqrobertobalderas</a></span></div></div>
    </div>
  </div>
</section>

<section class="band" id="tabs">
  <div class="wrap">
    <div class="doors doors3">
      <a class="door rv" href="architecture.html"><img src="img/ph-bar-bachus-06.jpg" alt="Architecture & Design" loading="lazy"><div class="door-t"><small>01</small><b>Architecture<br>&amp; Design</b><span>Houses, interiors, hospitality, commercial.</span></div></a>
      <a class="door rv d1" href="real-estate.html"><img src="img/ig-DceaktFmAgJ-5.jpg" alt="Real Estate" loading="lazy"><div class="door-t"><small>02</small><b>Real Estate</b><span>Selected properties and developments.</span></div></a>
      <a class="door rv d2" href="construction.html"><img src="img/ph-penas-obra-a-03.jpg" alt="Construction" loading="lazy"><div class="door-t"><small>03</small><b>Construction</b><span>Directed personally; built with Espacios y Formas.</span></div></a>
    </div>
  </div>
</section>
"""
    return ("index",
            "Roberto Balderas Carrillo, Arquitecto — Architecture, Real Estate and Construction in San Miguel de Allende | RBC",
            "RBC is the practice of architect Roberto Balderas Carrillo in San Miguel de Allende: architecture and design, a selection of properties and developments, and construction with Espacios y Formas.",
            body, HERO, "org", "1.0")

# ───────────────────────────── ARCHITECTURE & DESIGN ─────────────────────────────
def architecture(wa, SITE):
    body = P.phero("img/ph-casa-jalpa-02.jpg", "RBC / Architecture &amp; Design", "Architecture &amp; Design.",
        "Houses, interiors, hotels, bars, stores and offices.", '<a href="index.html">Home</a> › Architecture &amp; Design') + f"""
<section id="projects">
  <div class="wrap">
    {projects_v13.reels()}
  </div>
</section>
""" + P.contact_band(wa, "Start a project", "Tell me about the site.",
        "A lot, a house to renovate, a building to plan. English and Spanish.",
        "Hi Roberto, I would like to talk about a project.", "WhatsApp +52 461 101 2474")
    ld = [{"@context":"https://schema.org","@type":"CollectionPage","name":"Architecture & Design — RBC","url":f"{SITE}/architecture.html"},
          {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"},{"@type":"ListItem","position":2,"name":"Architecture & Design","item":f"{SITE}/architecture.html"}]}]
    return ("architecture", "Architecture &amp; Design — Roberto Balderas Carrillo, Arquitecto | RBC",
            "Architecture and interior design projects by Roberto Balderas Carrillo in San Miguel de Allende, Querétaro, Celaya and beyond: houses, hotels, bars, stores and offices.",
            body, "img/ph-casa-jalpa-02.jpg", ld, "0.9")

# ───────────────────────────── REAL ESTATE ─────────────────────────────
def real_estate(wa, SITE):
    sale = [l for l in listings.L if l["kind"] == "sale" and l["slug"] != "magno"]
    rent = [l for l in listings.L if l["kind"] == "rent"]
    devs = dev_card("penas-arriba", "img/penas-arriba-logo.png", "Peñas Arriba", "San Miguel de Allende", "RBC with Espacios y Formas",
        "A gated community on the hillside above San Miguel de Allende, with views of the Parroquia. Houses, shell-built homes and lots.",
        ["img/ph-penas-obra-b-06.jpg","img/ig-DceaktFmAgJ-1.jpg","img/ph-penas-obra-b-07.jpg","img/penas-arriba-map-casa-horizonte.jpg"],
        '<a class="btn red" href="penas-arriba.html">Full sheet →</a><a class="btn ghost" href="https://penasarriba.vercel.app/" target="_blank" rel="noopener">Community site</a>', 4200) + \
    dev_card("magno", "img/magno-logo-white.png", "Magno Home &amp; Towers", "Celaya · Guanajuato", "Espacios y Formas",
        "Residential towers, single-family homes and lots in one gated community, with spa, pool, gym and clubhouse. Apartments available for immediate delivery. Lots from MX $2.0M · apartments from MX $4.3M · homes from MX $5.5M.",
        ["img/magno-4.jpg","img/magno-2.jpg","img/magno-5.jpg","img/magno-8.jpg"],
        f'<a class="btn red" href="magno.html">Full sheet →</a><a class="btn ghost" href="https://magnoresidencial.com/" target="_blank" rel="noopener">Sales site</a><a class="btn ghost" href="{wa("Hi Roberto, I would like the current inventory of apartments, homes and lots in Magno, Celaya.")}">Ask for inventory</a>', 4600) + \
    dev_card("escondida", "", "La Escondida &amp; La Nueva Escondida", "San Miguel de Allende", "In development",
        "Two residential developments in San Miguel de Allende. Details to follow.",
        ["img/community-trails.jpg","img/valley-golden-hour.jpg"],
        f'<a class="btn" href="{wa("Hi Roberto, please keep me informed about La Escondida and La Nueva Escondida in San Miguel.")}">Keep me informed</a>', 5000)

    body = P.phero("img/ig-DceaktFmAgJ-2.jpg", "RBC / Real Estate", "Real Estate.",
        "A short selection of houses, and the developments behind them.", '<a href="index.html">Home</a> › Real Estate') + f"""
<section id="sale">
  <div class="wrap">
    {shead("01","Houses")}
    """ + fichas.grid(sale, wa) + f"""
    <div class="cap rv" style="margin-top:14px;">Prices in MXN; USD approximate · Open a sheet for plans, program, an architect's reading and the PDF</div>
  </div>
</section>

<section class="band" id="developments">
  <div class="wrap">
    {shead("02","Developments")}
    {__import__('devpages').dev_cards(wa)}
  </div>
</section>

<section id="stays">
  <div class="wrap">
    {shead("03","Stays · historic center")}
    """ + fichas.grid(rent, wa, md=True) + f"""
  </div>
</section>

<section class="band" id="sell">
  <div class="wrap split" style="align-items:start;">
    <div class="rv">
      {shead("04","Sell")}
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
      "itemListElement":[{"@type":"ListItem","position":i+1,"name":f"{l['name']} — {l['where']}","url":f"{SITE}/{l['slug']}.html" if l.get('page') else f"{SITE}/real-estate.html#{l['slug']}"} for i,l in enumerate(listings.L)]},
      {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"},{"@type":"ListItem","position":2,"name":"Real Estate","item":f"{SITE}/real-estate.html"}]}]
    return ("real-estate",
            "Real Estate — Houses for Sale in San Miguel de Allende and Querétaro, by Architect Roberto Balderas Carrillo | RBC",
            "A short selection of houses for sale and rent in San Miguel de Allende, its countryside and Querétaro, plus the developments Peñas Arriba and Magno, presented by architect Roberto Balderas Carrillo.",
            body, "img/ig-DceaktFmAgJ-3.jpg", ld, "0.9")

# ───────────────────────────── CONSTRUCTION ─────────────────────────────
def construction(wa, SITE):
    body = P.phero("img/ph-penas-obra-b-06.jpg", "RBC / Construction", "Construction.",
        "Directed personally. Larger works are built with Espacios y Formas.", '<a href="index.html">Home</a> › Construction') + f"""
<section id="built">
  <div class="wrap">
    {shead("01","Peñas Arriba · San Miguel de Allende")}
    {projects_v13.construction_grid()}
  </div>
</section>
""" + P.contact_band(wa, "Build", "From your plans or ours.",
        "Renovations, houses, larger residences and developments. English and Spanish.",
        "Hi Roberto, I would like a construction quote.", "WhatsApp +52 461 101 2474")
    ld = [{"@context":"https://schema.org","@type":"CollectionPage","name":"Construction — RBC","url":f"{SITE}/construction.html"},
          {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"},{"@type":"ListItem","position":2,"name":"Construction","item":f"{SITE}/construction.html"}]}]
    return ("construction", "Construction — Roberto Balderas Carrillo, Arquitecto, with Espacios y Formas | RBC",
            "Residential and commercial construction in San Miguel de Allende and the Bajío, directed by architect Roberto Balderas Carrillo and built with Espacios y Formas.",
            body, "img/ph-penas-obra-b-06.jpg", ld, "0.9")

# ───────────────────────────── CONTACT (kept, reached from footer / mobile menu) ─────────────────────────────
from pages_v12 import contact

REDIRECTS = (("work","architecture.html"),("properties","real-estate.html"),("about","index.html#intro"),
             ("roberto-balderas-carrillo","index.html#intro"),("development","real-estate.html#developments"))

def build(page, wa, ORG, SITE):
    urls = []
    for fn in (home, architecture, real_estate, construction, contact):
        slug, title, desc, body, og, ld, pr = fn(wa, SITE)
        if ld == "org": ld = [ORG]
        urls.append((page(slug, title, desc, body, og, ld, active=slug + ".html"), pr))
    import devpages
    for d in devpages.DEVS:
        slug, title, desc, body, og, ld, pr = devpages.dev_page(d, wa, SITE)
        urls.append((page(slug, title, desc, body, og, ld, active="real-estate.html"), pr))
    for l in listings.pages():
        slug, title, desc, body, og, ld, pr = listings.property_page(l, wa, SITE)
        body = body.replace('href="properties.html"', 'href="real-estate.html"')
        urls.append((page(slug, title, desc, body, og, ld, active="real-estate.html"), pr))
    for slug, to in REDIRECTS:
        s, t, d, b, o, ld, pr = redirect(slug, to)
        page(s, t, d, b, o, ld, active="", extra_head='<meta name="robots" content="noindex">')
    urls.append((f"{SITE}/privacy.html", "0.2")); urls.append((f"{SITE}/terms.html", "0.2"))
    return urls
