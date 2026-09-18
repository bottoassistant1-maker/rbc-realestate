# -*- coding: utf-8 -*-
"""v11 pages per the RBC master brief: Home · Work · Properties · About · Contact (+ Developments, service landings, property pages)."""
import pages as P          # helpers + legacy pages (casa_horizonte, architecture, construction, development)
import projects, listings, fichas

HZ = "img/casa-horizonte-sunset-facade.jpg"

def shead(num, txt):
    return f'<div class="shead rv"><div class="eyebrow"><b>{num}</b>{txt}</div><i></i></div>'

# ───────────────────────────── HOME ─────────────────────────────
def home(wa, SITE):
    body = f"""
<header class="hero home" id="top">
  <div class="bg" style="background-image:url('{HZ}')"></div>
  <div class="in">
    <div class="tag">RBC · San Miguel de Allende · Celaya · Bajío · México</div>
    <h1>Roberto Balderas Carrillo<br><em>Arquitecto</em></h1>
    <p class="sub">Architecture, construction and real estate — designed, built and represented with one criterion, by one architect.</p>
    <div class="pricebar">
      <a class="btn" href="work.html">See the work</a>
      <a class="btn ghost lt" href="contact.html">Start a conversation</a>
    </div>
  </div>
</header>

<div class="wwww"><div class="in">
  <div><small>Who</small><b>Roberto Balderas Carrillo</b><span>Arquitecto</span></div>
  <div><small>What</small><b>Architecture · Construction · Real Estate</b><span>Design, executive project, building, development, selected properties</span></div>
  <div><small>Where</small><b>San Miguel de Allende</b><span>Celaya · Bajío · México</span></div>
  <div><small>Why</small><b>Personal criterion, real capacity</b><span>In close collaboration with Espacios y Formas — 30+ years of architecture, construction and development</span></div>
</div></div>

<section id="areas">
  <div class="wrap">
    {shead("01","What RBC does")}
    <h2 class="rv d1">Three practices. One architect.</h2>
    <div class="areas" style="margin-top:30px;">
      <a class="area rv" href="architecture.html">
        <div class="n">01 / ARCHITECTURE</div>
        <h3>Design, from the first sketch to the executive project.</h3>
        <div class="im"><img src="img/architecture-section-hillside-home.jpg" alt="Architectural section"></div>
        <p>Houses, interiors, landscape, furniture, renovations and whole developments. No house style: each project answers its site, client, budget and scale. Almost everything is designed in-house.</p>
        <div class="go" style="margin-top:12px;">Architecture →</div>
      </a>
      <a class="area rv d1" href="construction.html">
        <div class="n">02 / CONSTRUCTION</div>
        <h3>Built with the infrastructure of a 30-year firm.</h3>
        <div class="im"><img src="img/projects-custom-build.jpg" alt="Construction"></div>
        <p>From a small renovation to residential towers, gated communities, dealerships and commercial centers. You deal with Roberto; behind him, the crews, engineering and processes of Espacios y Formas.</p>
        <div class="go" style="margin-top:12px;">Construction →</div>
      </a>
      <a class="area rv d2" href="properties.html">
        <div class="n">03 / REAL ESTATE</div>
        <h3>Selected properties, seen by an architect.</h3>
        <div class="im"><img src="img/casa-horizonte-infinity-pool.jpg" alt="Casa Horizonte"></div>
        <p>A short list of properties Roberto knows, understands and confidently represents — read through structure, materials, site and potential, not just square feet.</p>
        <div class="go" style="margin-top:12px;">Properties →</div>
      </a>
    </div>
  </div>
</section>

""" + projects.index_section(title="Recent work.", eyebrow="Work", filters=False, limit=7, note=False, intro=False, num="02") + f"""
<section id="sel" class="band">
  <div class="wrap">
    {shead("03","Selected properties")}
    <h2 class="rv d1">An architect's perspective on real estate.</h2>
    <p class="lead rv d2" style="max-width:720px;">A deliberately small selection: houses Roberto designed or built, and a few he knows deeply enough to represent. Every sheet carries his notes as an architect — structure, materials, orientation, condition, potential.</p>
    """ + fichas.grid([l for l in listings.L if l['slug'] in ('casa-horizonte','casa-travertino','casa-mirador')], wa) + f"""
    <div style="margin-top:26px;" class="rv"><a class="btn ghost" href="properties.html">All selected properties →</a> &nbsp; <a class="btn ghost" href="development.html">Developments →</a></div>
  </div>
</section>

<section id="about-teaser">
  <div class="wrap split" style="align-items:start;">
    <div class="rv">
      {shead("04","The person behind the practice")}
      <h2>Architect first. Everything else follows.</h2>
    </div>
    <div class="rv d1">
      <p class="lead">Roberto Balderas Carrillo is an architect from Celaya, Guanajuato, working mainly in San Miguel de Allende and the Bajío. RBC is his personal practice; it works in close collaboration with Espacios y Formas, the Balderas family's architecture, construction and development firm with more than 30 years of experience — headquarters in Celaya, an office in San Miguel.</p>
      <p class="lead" style="margin-top:12px;">The result is a boutique practice with the execution capacity of a consolidated organization: personal attention and criterion in design, real construction experience, and a working knowledge of the property business.</p>
      <div style="margin-top:20px;display:flex;gap:10px;flex-wrap:wrap;"><a class="btn ghost" href="about.html">About Roberto and RBC</a><a class="btn ghost" href="https://www.espaciosyformas.com.mx/" target="_blank" rel="noopener">Espacios y Formas ↗</a></div>
    </div>
  </div>
</section>

<section id="entry" class="band">
  <div class="wrap">
    {shead("05","Where would you like to start?")}
    <div class="intents">
      <a class="intent" href="contact.html#project"><small>Design &amp; build</small><b>I want to design and build a house.</b><span>A lot, a sketch or just an idea — in San Miguel, the Bajío or elsewhere in Mexico.</span></a>
      <a class="intent" href="contact.html#land"><small>Land</small><b>I have a lot and want to understand what I can do with it.</b><span>A first reading of the site: slope, views, regulations, program, cost.</span></a>
      <a class="intent" href="contact.html#buy"><small>Buy</small><b>I want to buy a house in San Miguel.</b><span>Selected properties, or an architect's evaluation of one you found.</span></a>
      <a class="intent" href="contact.html#sell"><small>Sell</small><b>I have a property I'd like to sell.</b><span>Roberto reviews it first; he represents a short list, not everything.</span></a>
    </div>
  </div>
</section>
""" + fichas.modal_data([l for l in listings.L if l['slug'] in ('casa-horizonte','casa-travertino','casa-mirador')], wa)
    return ("index",
            "Roberto Balderas Carrillo, Arquitecto — Architecture, Construction &amp; Real Estate in San Miguel de Allende | RBC",
            "RBC is the practice of architect Roberto Balderas Carrillo: architecture, construction and selected real estate in San Miguel de Allende, Celaya and the Bajío, in close collaboration with Espacios y Formas (30+ years). Design and build a house, evaluate a lot, buy or sell a property with an architect's perspective.",
            body, HZ, "org", "1.0")

# ───────────────────────────── WORK ─────────────────────────────
def work(wa, SITE):
    body = P.phero("img/hero-terrace-sunset.jpg", "RBC / Work", "The work.",
        "Architecture, construction and interiors across San Miguel de Allende, Querétaro, Celaya and beyond — houses, hotels, bars, stores, offices, dealerships and whole communities.",
        '<a href="index.html">Home</a> › Work') + projects.index_section(title="Projects, 2021 – 2026.", eyebrow="Index", num="02") + f"""
<section id="developments-teaser">
  <div class="wrap split" style="align-items:center;">
    <div class="rv">
      {shead("03","Developments")}
      <h2>Beyond single houses: planning, urbanization, construction and sales.</h2>
      <p class="lead">Peñas Arriba in San Miguel de Allende (RBC with Espacios y Formas); Magno Home &amp; Towers in Celaya (Espacios y Formas); La Escondida and La Nueva Escondida, coming next.</p>
      <div style="margin-top:18px;"><a class="btn ghost" href="development.html">See the developments →</a></div>
    </div>
    <div class="rv d1"><a class="lbx" href="img/penas-arriba-map-casa-horizonte.jpg"><img class="mapimg" src="img/penas-arriba-map-casa-horizonte.jpg" alt="Peñas Arriba master plan"></a><div class="cap">Peñas Arriba — master plan</div></div>
  </div>
</section>
""" + P.contact_band(wa, "Start a project", "Tell me about the site.",
        "A lot, a house to renovate, a building to plan — the first conversation is free and specific.",
        "Hi Roberto, I would like to talk about a project.", "WhatsApp +52 461 101 2474")
    ld = [{"@context":"https://schema.org","@type":"CollectionPage","name":"Work — RBC Roberto Balderas Carrillo","url":f"{SITE}/work.html"},
          {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"},{"@type":"ListItem","position":2,"name":"Work","item":f"{SITE}/work.html"}]}]
    return ("work", "Work — Architecture, Construction &amp; Interiors by Roberto Balderas Carrillo | RBC",
            "Selected architecture, construction and interior projects by architect Roberto Balderas Carrillo in San Miguel de Allende, Querétaro, Celaya and beyond: houses, hotels, bars, stores, offices and developments.",
            body, "img/hero-terrace-sunset.jpg", ld, "0.9")

# ───────────────────────────── PROPERTIES ─────────────────────────────
def properties(wa, SITE):
    sma = listings.by('sma','sale'); rent = listings.by('sma','rent')
    body = P.phero("img/luxury-home-san-miguel-de-allende-terrace.jpg", "RBC / Properties", "Selected properties.",
        "Properties I know, understand and confidently represent — in San Miguel de Allende, its countryside, Querétaro and Celaya. Read with an architect's eye: structure, materials, site, condition and potential.",
        '<a href="index.html">Home</a> › Properties') + f"""
<section id="selected">
  <div class="wrap">
    {shead("01","Selected properties · San Miguel de Allende")}
    <h2 class="rv d1">Houses I designed, built or know well.</h2>
    <p class="lead rv d2" style="max-width:720px;">Not a portal. A short list: homes in Peñas Arriba that we design, build and sell ourselves; a furnished townhouse in the historic center; a country house on the road to Jalpa; a newly built house in Querétaro. Open any sheet for photos, plans, the program of the house and Roberto's notes — or download the PDF.</p>
    """ + fichas.grid(sma, wa) + f"""
    <div class="cap rv" style="margin-top:14px;">USD figures approximate at prevailing exchange rates · Direct title for foreign buyers in the interior of Mexico (no bank trust) · Every Peñas Arriba home includes finish selection with the studio</div>

    <div class="shead rv" style="margin-top:60px;"><div class="eyebrow"><b>02</b>Countryside near San Miguel · Querétaro · Celaya</div><i></i></div>
    """ + fichas.grid(listings.by('jalpa','sale') + listings.by('qro','sale') + listings.by('celaya','sale'), wa) + f"""

    <div class="shead rv" style="margin-top:60px;"><div class="eyebrow"><b>03</b>Mid-term rentals · historic center</div><i></i></div>
    <p class="lead rv" style="max-width:720px;">Two furnished spaces inside Casa Cuadrante, the house Roberto restored above the restaurant of the same name, with the Parroquia in front of you.</p>
    """ + fichas.grid(rent, wa) + f"""
  </div>
</section>

<section class="band" id="perspective">
  <div class="wrap split" style="align-items:start;">
    <div class="rv">
      {shead("04","Why an architect")}
      <h2>Buying a house is an architectural decision before it is a transaction.</h2>
    </div>
    <div class="rv d1">
      <p class="lead">When Roberto looks at a property he reads what a listing cannot show: the structure and the quality of the build, how the plan distributes light and privacy, the orientation and the slope of the lot, what maintenance it will ask for, what a renovation would cost and what the house could become. That reading is what he puts in writing in every sheet — and what he brings when you ask him to evaluate a property you found elsewhere.</p>
      <ul class="checks">
        <li>Architecture, structure, materials and construction quality</li>
        <li>Plan, orientation, site, topography and context</li>
        <li>Condition, maintenance and realistic renovation costs</li>
        <li>Architectural and development potential</li>
        <li>Title, notary and closing for international buyers</li>
      </ul>
      <div style="margin-top:18px;"><a class="btn" href="contact.html#buy">Ask Roberto to evaluate a property</a></div>
    </div>
  </div>
</section>

<section id="dev">
  <div class="wrap split" style="align-items:center;">
    <div class="rv">
      {shead("05","Developments")}
      <h2>Peñas Arriba, Magno, La Escondida.</h2>
      <p class="lead">Communities planned, built and sold by RBC and Espacios y Formas — with lots, early-stage homes and apartments for immediate delivery.</p>
      <div style="margin-top:18px;"><a class="btn ghost" href="development.html">See the developments →</a></div>
    </div>
    <div class="rv d1"><a class="lbx" href="img/parroquia-view-from-community.jpg"><img class="mapimg" src="img/parroquia-view-from-community.jpg" alt="Peñas Arriba"></a></div>
  </div>
</section>

<section class="band" id="sell">
  <div class="wrap split" style="align-items:start;">
    <div class="rv">
      {shead("06","Sell or represent your property")}
      <h2>Have Roberto look at your property first.</h2>
      <p class="lead">RBC represents a short, curated list — properties Roberto can stand behind and considers intelligent purchases. Send the basics; he will tell you honestly whether it fits, what it is worth architecturally, and what would make it sell better.</p>
    </div>
    <div class="rv d1">
      {P.form("Tell me about your property", "It goes straight to Roberto's WhatsApp. No listing is accepted without a visit.",
        [("row",[("text","Name","Your name","Jane Smith"),("select","Location","Where is the property",["San Miguel de Allende","Querétaro","Celaya","Elsewhere in the Bajío"])]),
         ("row",[("select","Type","Type",["House","Apartment","Lot","Commercial","Other"]),("select","Goal","What you'd like",["Sell","Rent","An architect's evaluation first","Not sure yet"])]),
         ("area","Details","Describe it","Size, year built, condition, price expectation, anything special…")],
        "Hi Roberto, I have a property I'd like you to look at:", "Send to Roberto")}
    </div>
  </div>
</section>
""" + fichas.modal_data(listings.L, wa)
    ld = [{"@context":"https://schema.org","@type":"ItemList","name":"Selected properties — RBC",
      "itemListElement":[{"@type":"ListItem","position":i+1,"name":f"{l['name']} — {l['where']}","url":f"{SITE}/{l['slug']}.html" if l.get('page') else f"{SITE}/properties.html#{l['slug']}"} for i,l in enumerate(listings.L)]},
      {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"},{"@type":"ListItem","position":2,"name":"Properties","item":f"{SITE}/properties.html"}]}]
    return ("properties",
            "Selected Properties in San Miguel de Allende &amp; Querétaro — An Architect's Perspective | RBC",
            "Selected homes for sale and rent represented by architect Roberto Balderas Carrillo: Casa Horizonte, Casa Mirador, Casa Cima and duplexes in San Miguel de Allende; Casa Ether near Jalpa; Casa Travertino in Querétaro; Magno in Celaya. Sheets with plans, Roberto's notes and PDF.",
            body, "img/luxury-home-san-miguel-de-allende-terrace.jpg", ld, "0.9")

# ───────────────────────────── ABOUT ─────────────────────────────
def about(wa, SITE):
    body = P.phero("img/valley-golden-hour.jpg", "RBC / About", "Roberto Balderas Carrillo, Arquitecto.",
        "A personal practice with the capacity of a thirty-year firm.",
        '<a href="index.html">Home</a> › About') + f"""
<section id="bio">
  <div class="wrap bio">
    <div class="rv">
      <div class="photo"><img src="img/luxury-home-san-miguel-interior-living.jpg" alt="Roberto Balderas Carrillo at work"></div>
      <div class="cap" style="margin-top:8px;">Portrait in progress — Roberto at work, on site and at the drawing table.</div>
      <div class="kpis">
        <div><div class="n">30</div><div class="l">years · EyF</div></div>
        <div><div class="n">2,600</div><div class="l">homes delivered</div></div>
        <div><div class="n">2</div><div class="l">offices · CLY · SMA</div></div>
      </div>
    </div>
    <div class="rv d1">
      {shead("01","Roberto")}
      <h2>Architect first.</h2>
      <p class="lead">I am an architect from Celaya, Guanajuato, and most of my work is in San Miguel de Allende and the Bajío. RBC is my personal practice: the projects I author, the houses I build, and a short list of properties I represent because I know them.</p>
      <div class="notes"><small>Criterion</small><p>Every project answers its context, its client, its budget and its scale. I don't have a house style — I have a way of deciding.</p></div>
      <p class="lead">Contemporary, colonial, contextual; a limited budget or a large one; a bar or a tower. What repeats is the criterion: how the plan meets the site, how light enters, which material belongs, what will still be right in twenty years.</p>

      {shead("02","Espacios y Formas")}
      <h2 style="font-size:1.8rem;">Backed by a family firm with more than 30 years.</h2>
      <p class="lead">RBC works in close collaboration with <a href="https://www.espaciosyformas.com.mx/" target="_blank" rel="noopener">Espacios y Formas</a>, the Balderas family's architecture, construction and development firm: headquarters in Celaya, an office in San Miguel de Allende, and three decades of houses, residential communities, towers, dealerships and commercial centers across the Bajío — Magno Towers among them.</p>
      <p class="lead" style="margin-top:12px;">In practice it means this: you talk to me, and when the project needs it — engineering, crews, permits, administration, the capacity to build a tower — the infrastructure is already there. Personal attention, real execution.</p>

      {shead("03","Capabilities")}
      <ul class="checks">
        <li>Architectural design · executive project · engineering coordination</li>
        <li>Interior design · furniture · landscape</li>
        <li>Construction: renovations, houses, high-end residences, serial housing, urbanization, towers, commercial and hospitality</li>
        <li>Real-estate development, sales and advisory</li>
        <li>Property evaluation and buyer representation for international clients</li>
      </ul>

      {shead("04","Where")}
      <p class="lead">San Miguel de Allende · Celaya · Bajío · México. Based in San Miguel, with the firm's headquarters in Celaya; able to take projects elsewhere in Mexico.</p>
      <div style="margin-top:22px;display:flex;gap:10px;flex-wrap:wrap;">
        <a class="btn red" href="{wa('Hi Roberto, I read your About page and I would like to talk.')}">WhatsApp +52 461 101 2474</a>
        <a class="btn ghost" href="https://www.instagram.com/arqrobertobalderas" target="_blank" rel="noopener">@arqrobertobalderas</a>
      </div>
    </div>
  </div>
</section>
""" + P.contact_band(wa, "Let's talk", "Design, build, buy or sell — start with a message.",
        "English and Spanish. I reply personally.", "Hi Roberto, I found your website and I would like to talk.", "WhatsApp +52 461 101 2474")
    ld = [{"@context":"https://schema.org","@type":"Person","name":"Roberto Balderas Carrillo","jobTitle":"Arquitecto","url":f"{SITE}/about.html","worksFor":{"@type":"Organization","name":"Espacios y Formas","url":"https://www.espaciosyformas.com.mx/"},"sameAs":["https://www.instagram.com/arqrobertobalderas"],"address":{"@type":"PostalAddress","addressLocality":"San Miguel de Allende","addressRegion":"Guanajuato","addressCountry":"MX"}},
          {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"},{"@type":"ListItem","position":2,"name":"About","item":f"{SITE}/about.html"}]}]
    return ("about", "About — Roberto Balderas Carrillo, Arquitecto | RBC · Espacios y Formas",
            "Roberto Balderas Carrillo is an architect based in San Miguel de Allende. RBC is his personal practice, in close collaboration with Espacios y Formas, the Balderas family's architecture, construction and development firm with more than 30 years of experience in the Bajío.",
            body, "img/valley-golden-hour.jpg", ld, "0.7")

# ───────────────────────────── CONTACT ─────────────────────────────
def contact(wa, SITE):
    F = P.form
    body = P.phero("img/sunset-terrace-luxury-villa-mexico.jpg", "RBC / Contact", "Tell me what you have in mind.",
        "Four doors, one architect. WhatsApp is the fastest; the forms below send straight to it. English and Spanish.",
        '<a href="index.html">Home</a> › Contact') + f"""
<section id="doors">
  <div class="wrap">
    <div class="intents rv">
      <a class="intent" href="#project"><small>01</small><b>Start a project</b><span>Design and/or build a house, a renovation, a building.</span></a>
      <a class="intent" href="#buy"><small>02</small><b>Buy a property</b><span>Selected properties, or evaluate one you found.</span></a>
      <a class="intent" href="#sell"><small>03</small><b>Sell a property</b><span>Have Roberto review and, if it fits, represent it.</span></a>
      <a class="intent" href="#general"><small>04</small><b>General inquiry</b><span>Press, collaborations, developers, brands, anything else.</span></a>
    </div>
    <div style="margin-top:26px;display:flex;gap:12px;flex-wrap:wrap;align-items:center;" class="rv">
      <a class="btn red" href="{wa('Hi Roberto, I found your website and I would like to talk.')}">WhatsApp +52 461 101 2474</a>
      <span class="code">Replies personally, usually the same day · Video calls for clients abroad</span>
    </div>
  </div>
</section>

<section class="band" id="project">
  <div class="wrap split" style="align-items:start;">
    <div class="rv">{shead("01","Start a project")}<h2>Design &amp; build.</h2><p class="lead">A lot, a sketch or an idea. If you don't have a lot yet, we can help you find the right one. Land owners: ask for a first reading of what your site allows.</p></div>
    <div class="rv d1">{F("Project", "Three questions and a text box.",
        [("row",[("text","Name","Your name","Jane Smith"),("select","Location","Where",["San Miguel de Allende","Querétaro","Celaya","Elsewhere in the Bajío","Elsewhere in Mexico","I don't have a lot yet"])]),
         ("row",[("select","Scope","What you need",["Design + construction","Design only","Construction from my plans","Renovation / restoration","A reading of my lot","A building / development"]),("select","Budget","Budget (USD)",["Under $300K","$300K – $600K","$600K – $1.2M","Over $1.2M","Not sure yet"])]),
         ("area","Details","Tell me about it","")], "Hi Roberto, I'd like to start a project:", "Send to Roberto")}</div>
  </div>
</section>
<div id="land"></div>

<section id="buy">
  <div class="wrap split" style="align-items:start;">
    <div class="rv">{shead("02","Buy a property")}<h2>Buy with an architect's eye.</h2><p class="lead">Selected properties in San Miguel, Querétaro and Celaya — or send a listing you found and Roberto will read it for structure, materials, condition and potential before you commit.</p></div>
    <div class="rv d1">{F("Buying", "What are you looking for?",
        [("row",[("text","Name","Your name","Jane Smith"),("select","City","City",["San Miguel de Allende","Querétaro","Celaya","Not sure yet"])]),
         ("row",[("select","Budget","Budget (USD)",["Under $400K","$400K – $800K","$800K – $1.5M","$1.5M – $3M","Over $3M"]),("select","When","When",["As soon as possible","3–6 months","6–12 months","Exploring"])]),
         ("area","Details","What matters most / a link to a property you'd like evaluated","")], "Hi Roberto, I'm looking to buy:", "Send to Roberto")}</div>
  </div>
</section>

<section class="band" id="sell">
  <div class="wrap split" style="align-items:start;">
    <div class="rv">{shead("03","Sell a property")}<h2>Have it reviewed first.</h2><p class="lead">RBC represents a short list. Send the basics and Roberto will tell you whether it fits and what would make it sell better.</p></div>
    <div class="rv d1">{F("Selling", "No listing is accepted without a visit.",
        [("row",[("text","Name","Your name","Jane Smith"),("select","Location","Where",["San Miguel de Allende","Querétaro","Celaya","Elsewhere in the Bajío"])]),
         ("row",[("select","Type","Type",["House","Apartment","Lot","Commercial","Other"]),("select","Goal","Goal",["Sell","Rent","Evaluation first"])]),
         ("area","Details","Describe the property","")], "Hi Roberto, I have a property I'd like you to look at:", "Send to Roberto")}</div>
  </div>
</section>

<section id="general">
  <div class="wrap split" style="align-items:start;">
    <div class="rv">{shead("04","General inquiry")}<h2>Anything else.</h2><p class="lead">Developers, brands, press, collaborations, or a question that doesn't fit above.</p>
      <ul class="checks"><li>WhatsApp +52 461 101 2474</li><li>Instagram @arqrobertobalderas</li><li>Offices: Celaya (Espacios y Formas HQ) · San Miguel de Allende</li></ul></div>
    <div class="rv d1">{F("Message", "Straight to WhatsApp.",
        [("row",[("text","Name","Your name","Jane Smith"),("text","Contact","Best way to reach you","Phone or email")]),
         ("area","Message","Message","")], "Hi Roberto, I'm writing from your website:", "Send to Roberto")}</div>
  </div>
</section>
"""
    ld = [{"@context":"https://schema.org","@type":"ContactPage","url":f"{SITE}/contact.html","name":"Contact Roberto Balderas Carrillo"},
          {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"},{"@type":"ListItem","position":2,"name":"Contact","item":f"{SITE}/contact.html"}]}]
    return ("contact", "Contact — Start a Project, Buy or Sell a Property | RBC Roberto Balderas Carrillo, Arquitecto",
            "Contact architect Roberto Balderas Carrillo: start a design-and-build project, get a first reading of your lot, buy a selected property in San Miguel de Allende or have your property reviewed for sale. WhatsApp +52 461 101 2474.",
            body, "img/sunset-terrace-luxury-villa-mexico.jpg", ld, "0.6")

# ───────────────────────────── REDIRECTS ─────────────────────────────
def redirect(slug, to):
    body = f'<meta http-equiv="refresh" content="0; url={to}"><div class="wrap" style="padding:140px 32px;"><p class="lead">This page moved to <a href="{to}">{to}</a>.</p></div>'
    return (slug, "Redirecting — RBC", "This page has moved.", body, HZ, [], "0.1")

def build(page, wa, ORG, SITE):
    urls = []
    for fn in (home, work, properties, about, contact, P.casa_horizonte, P.architecture, P.construction, P.development):
        slug, title, desc, body, og, ld, pr = fn(wa, SITE)
        if ld == "org": ld = [ORG]
        active = {"casa-horizonte":"properties.html","architecture":"work.html","construction":"work.html","development":"properties.html"}.get(slug, slug + ".html")
        urls.append((page(slug, title, desc, body, og, ld, active=active), pr))
    for l in listings.pages():
        slug, title, desc, body, og, ld, pr = listings.property_page(l, wa, SITE)
        urls.append((page(slug, title, desc, body, og, ld, active="properties.html"), pr))
    for slug, to in (("real-estate","properties.html"),("roberto-balderas-carrillo","about.html")):
        s, t, d, b, o, ld, pr = redirect(slug, to)
        page(s, t, d, b, o, ld, active="", extra_head='<meta name="robots" content="noindex">')
    urls.append((f"{SITE}/privacy.html", "0.2")); urls.append((f"{SITE}/terms.html", "0.2"))
    return urls
