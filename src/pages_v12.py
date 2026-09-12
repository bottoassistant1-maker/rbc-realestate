# -*- coding: utf-8 -*-
"""v12 — architect first. Home · Work (Architecture · Construction · Developments) · Properties · About · Contact.
Copy rules: no invented figures, no sales language; Roberto = architect; Espacios y Formas = infrastructure and experience."""
import pages as P          # helpers only: phero, form, contact_band
import projects, listings, fichas

HZ = "img/casa-horizonte-sunset-facade.jpg"
EYF = "https://www.espaciosyformas.com.mx/"
SEL_WORK = ["casa-horizonte", "casa-ether", "bar-bachus", "casa-travertino", "hotel-casa-x", "casa-cuadrante"]
SEL_PROPS = ("casa-horizonte", "casa-travertino", "casa-mirador")

def shead(num, txt, extra=""):
    return f'<div class="shead rv"{extra}><div class="eyebrow"><b>{num}</b>{txt}</div><i></i></div>'

EYF_LINE = f'RBC works in close collaboration with <a href="{EYF}" target="_blank" rel="noopener">Espacios y Formas</a>, the Balderas family\'s architecture, construction and development firm with more than three decades of experience.'

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

<section class="band" id="practice">
  <div class="wrap practice">
    <div class="rv">
      {shead("02","The practice")}
      <h2>Architecture first. The rest follows from it.</h2>
    </div>
    <div class="rv d1">
      <p class="lead">RBC is the practice of Roberto Balderas Carrillo, architect. It designs houses, interiors, landscape and buildings, and it carries them through construction. There is no signature style: each project is resolved from its site, its client, its budget and its brief — contemporary, contextual, traditional or colonial as the case requires.</p>
      <div class="caps">
        <div><small>Architecture</small><span>Architectural design from first concept to executive and construction documentation.</span></div>
        <div><small>Interiors</small><span>Interior architecture, furniture and fittings, for new work and existing buildings.</span></div>
        <div><small>Landscape</small><span>Gardens, terraces and outdoor rooms designed with the house, not after it.</span></div>
        <div><small>Construction</small><span>Personal direction of the build; larger works executed with Espacios y Formas.</span></div>
        <div><small>Development</small><span>Planning and coordination of residential developments, with Espacios y Formas.</span></div>
        <div><small>Coordination</small><span>Engineering, specialists and permits coordinated under one architectural criterion.</span></div>
      </div>
      <div class="scale"><span>Small interventions</span><span>Houses</span><span>Commercial</span><span>Towers</span><span>Developments</span></div>
    </div>
  </div>
</section>

<section id="construction">
  <div class="wrap eyf">
    <figure class="rv"><img src="img/projects-custom-build.jpg" alt="Construction — provisional image" loading="lazy"></figure>
    <div class="rv d1">
      {shead("03","Construction · Espacios y Formas")}
      <h2>Architectural attention, with the capacity to build.</h2>
      <p class="lead">Roberto directs his projects personally, from the drawings to the site. Smaller works he manages himself; significant construction is supported and executed through Espacios y Formas — the Balderas family's architecture, construction and development firm, with more than three decades of building in the Bajío.</p>
      <div class="facts">
        <div><small>RBC</small><span>Authorship, architectural judgment, personal attention.</span></div>
        <div><small>Espacios y Formas</small><span>Infrastructure, experience, technical and construction capacity. Principal office in Celaya; presence in San Miguel de Allende; work throughout the Bajío and elsewhere in Mexico.</span></div>
      </div>
      <div style="margin-top:22px;display:flex;gap:10px;flex-wrap:wrap;"><a class="btn ghost" href="work.html#construction">Construction work</a><a class="btn ghost" href="{EYF}" target="_blank" rel="noopener">espaciosyformas.com.mx ↗</a></div>
    </div>
  </div>
</section>

<section class="band" id="properties">
  <div class="wrap">
    {shead("04","Selected properties")}
    <div class="split rv d1" style="align-items:start;">
      <h2>A few properties, known well.</h2>
      <p class="lead">Not a catalog. A short selection of houses Roberto designed, built or knows well enough to represent — each read as an architect reads a building: structure, plan, site, materials, condition, potential. Every sheet carries his notes.</p>
    </div>
    """ + fichas.grid([l for l in listings.L if l['slug'] in SEL_PROPS], wa) + f"""
    <div style="margin-top:26px;" class="rv"><a class="btn ghost" href="properties.html">All selected properties</a></div>
  </div>
</section>

<section id="about-teaser">
  <div class="wrap split" style="align-items:start;">
    <div class="rv">
      {shead("05","Roberto")}
      <h2>An architect based in San Miguel de Allende.</h2>
    </div>
    <div class="rv d1">
      <p class="lead">Roberto Balderas Carrillo is an architect from Celaya, Guanajuato, based in San Miguel de Allende. RBC is his personal practice. {EYF_LINE}</p>
      <div style="margin-top:20px;display:flex;gap:10px;flex-wrap:wrap;"><a class="btn ghost" href="about.html">About</a><a class="btn ghost" href="https://www.instagram.com/arqrobertobalderas" target="_blank" rel="noopener">@arqrobertobalderas</a></div>
    </div>
  </div>
</section>

<section class="band" id="entry">
  <div class="wrap">
    {shead("06","Contact")}
    <div class="intents">
      <a class="intent" href="contact.html#project"><small>Start a project</small><b>Design and build a house, a renovation or a building.</b><span>A lot, a sketch or an idea — in San Miguel, the Bajío or elsewhere in Mexico.</span></a>
      <a class="intent" href="contact.html#buy"><small>Buy</small><b>Buy a property with an architect's reading of it.</b><span>The selected properties, or one you found elsewhere.</span></a>
      <a class="intent" href="contact.html#sell"><small>Sell</small><b>Have Roberto look at a property you want to sell.</b><span>He represents a short list, after a visit.</span></a>
      <a class="intent" href="contact.html#general"><small>General</small><b>Developers, brands, press, collaborations.</b><span>Anything that doesn't fit above.</span></a>
    </div>
  </div>
</section>
""" + fichas.modal_data([l for l in listings.L if l['slug'] in SEL_PROPS], wa)
    return ("index",
            "Roberto Balderas Carrillo, Arquitecto — Architecture, Construction and Selected Properties in San Miguel de Allende | RBC",
            "RBC is the architecture practice of Roberto Balderas Carrillo in San Miguel de Allende: architectural design, interiors, construction and a small selection of properties read with an architect's eye. In collaboration with Espacios y Formas.",
            body, HZ, "org", "1.0")

# ───────────────────────────── WORK ─────────────────────────────
CONSTRUCTION = [
    ("RBC/C-001","Peñas Arriba","San Miguel de Allende · urbanization, amenities and houses","RBC with Espacios y Formas","work.html#penas-arriba"),
    ("RBC/C-002","Magno Towers","Celaya · residential towers","Espacios y Formas","work.html#magno"),
    ("RBC/C-003","Casa Horizonte","Peñas Arriba, San Miguel de Allende · residence","Under construction","casa-horizonte.html"),
    ("RBC/C-004","Casa Travertino","El Campanario, Querétaro · residence","Built","casa-travertino.html"),
    ("RBC/C-005","Casa Ether","Road to Jalpa, San Miguel de Allende · country house","Built","casa-ether.html"),
    ("RBC/C-006","Casa Cuadrante","Historic center, San Miguel de Allende · restoration, restaurant and residence","Built",""),
    ("RBC/C-007","Apartment JC","Historic center, San Miguel de Allende · renovation","Built",""),
    ("RBC/C-008","Golf-club residence","San Miguel de Allende · private","Built · details on request",""),
    ("RBC/C-009","Casa Elo","Details pending","Built",""),
    ("RBC/C-010","La Escondida · La Nueva Escondida","San Miguel de Allende · residential developments","In development",""),
]

def _dev(id_, place, status, name, text, imgs, ctas, auto=4500):
    sl = "".join(f'<div class="sl"><img src="{i}" alt="{name}"><div class="scap">{c}</div></div>' for i, c in imgs)
    return f"""
      <article class="dev rv" id="{id_}">
        <div class="dev-car car h520" data-auto="{auto}">
          <div class="trk">{sl}</div>
          <button class="arr l" aria-label="Previous">‹</button><button class="arr r" aria-label="Next">›</button>
          <div class="dots"></div>
        </div>
        <div class="dev-bd">
          <div class="dev-meta"><span>{place}</span><span>{status}</span></div>
          <h3>{name}</h3>
          <p>{text}</p>
          <div class="dev-cta">{ctas}</div>
        </div>
      </article>"""

def work(wa, SITE):
    ctab = "".join(
        (f'<a href="{h}">' if h else '<div class="r">') + f'<span class="cd">{c}</span><b>{n}</b><span>{p}</span><em>{s}</em>' + ('</a>' if h else '</div>')
        for c, n, p, s, h in CONSTRUCTION)
    devs = _dev("penas-arriba","San Miguel de Allende · Guanajuato","RBC with Espacios y Formas","Peñas Arriba",
        "A gated residential community on the hillside above San Miguel de Allende, with views of the Parroquia and the historic center a few minutes away. Streets, stone terracing and the amenity buildings are built; houses are designed and built inside the community, with lots and shell-built homes also available. Master plan, availability and prices on the community's own site.",
        [("img/parroquia-view-from-community.jpg","View of the Parroquia from the community"),("img/community-club-pool.jpg","Clubhouse and pool"),("img/stone-walls-community.jpg","Terracing in site stone"),("img/casa-horizonte-sunset-facade.jpg","Casa Horizonte"),("img/penas-arriba-map-casa-horizonte.jpg","Master plan")],
        f'<a class="btn red" href="https://penasarriba.vercel.app/" target="_blank" rel="noopener">Community site →</a><a class="btn ghost" href="properties.html">Houses on this site</a>', 4200) + \
    _dev("magno","Celaya · Guanajuato","Espacios y Formas","Magno Home &amp; Towers",
        "Residential towers, single-family homes and lots inside one gated community in Celaya, with spa, pool, gym, clubhouse, business center, gardens and underground parking. Developed and built by Espacios y Formas; apartments available for immediate delivery. Lots from MX $2.0M, apartments from MX $4.3M, homes from MX $5.5M.",
        [("img/community-club-pool.jpg","Provisional image"),("img/community-gym.jpg","Provisional image"),("img/gated-entrance-luxury-home.jpg","Provisional image")],
        f'<a class="btn red" href="https://magnoresidencial.com/" target="_blank" rel="noopener">Sales site →</a><a class="btn ghost" href="{wa("Hi Roberto, I would like the current inventory of apartments, homes and lots in Magno, Celaya.")}">Ask for inventory</a>', 4600) + \
    _dev("escondida","San Miguel de Allende","In development","La Escondida &amp; La Nueva Escondida",
        "Two residential developments in San Miguel de Allende, currently in development. Details will be published when available.",
        [("img/community-trails.jpg","Provisional image"),("img/valley-golden-hour.jpg","Provisional image")],
        f'<a class="btn" href="{wa("Hi Roberto, please keep me informed about La Escondida and La Nueva Escondida in San Miguel.")}">Keep me informed</a>', 5000)

    body = P.phero("img/hero-terrace-sunset.jpg", "RBC / Work", "Work.",
        "Architecture, interiors and construction — houses, hotels, bars, stores, offices and residential developments, mostly in San Miguel de Allende and the Bajío.",
        '<a href="index.html">Home</a> › Work') + projects.index_section(title="Architecture.", eyebrow="Architecture · 2021 – 2026", num="01") + f"""
<section class="band" id="construction">
  <div class="wrap">
    {shead("02","Construction")}
    <div class="split rv d1" style="align-items:start;">
      <h2>Drawn and built with the same criterion.</h2>
      <div>
        <p class="lead">Construction at RBC means the architect stays on the project through the site. Roberto manages smaller works personally; significant construction is supported and executed through Espacios y Formas, whose experience in the Bajío runs from single houses to residential towers, serial housing, urbanization and commercial buildings.</p>
        <p class="lead" style="margin-top:12px;">A selection of built and current work:</p>
      </div>
    </div>
    <div class="ctab rv d2">{ctab}</div>
    <div class="cap rv" style="margin-top:14px;">Photographs of the construction process are being gathered; entries marked pending will be completed with Roberto.</div>
  </div>
</section>

<section id="developments">
  <div class="wrap">
    {shead("03","Developments")}
    <div class="split rv d1" style="align-items:start;">
      <h2>Communities, with authorship stated.</h2>
      <p class="lead">Development-scale work is where the collaboration with Espacios y Formas is most visible. Each project below says who planned it, who builds it and where to buy.</p>
    </div>
    <div class="devs">{devs}</div>
  </div>
</section>
""" + P.contact_band(wa, "Start a project", "Tell me about the site.",
        "A lot, a house to renovate, a building to plan. English and Spanish.",
        "Hi Roberto, I would like to talk about a project.", "WhatsApp +52 461 101 2474")
    ld = [{"@context":"https://schema.org","@type":"CollectionPage","name":"Work — RBC Roberto Balderas Carrillo, Arquitecto","url":f"{SITE}/work.html"},
          {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"},{"@type":"ListItem","position":2,"name":"Work","item":f"{SITE}/work.html"}]}]
    return ("work", "Work — Architecture, Interiors and Construction by Roberto Balderas Carrillo | RBC",
            "Architecture, interior and construction projects by architect Roberto Balderas Carrillo in San Miguel de Allende, Querétaro, Celaya and beyond: houses, hotels, bars, stores, offices and residential developments with Espacios y Formas.",
            body, "img/hero-terrace-sunset.jpg", ld, "0.9")

# ───────────────────────────── PROPERTIES ─────────────────────────────
def properties(wa, SITE):
    sma = listings.by('sma','sale'); rent = listings.by('sma','rent')
    body = P.phero("img/luxury-home-san-miguel-de-allende-terrace.jpg", "RBC / Properties", "Selected properties.",
        "Fewer properties, known in more depth: houses Roberto designed, built or knows well enough to represent, read with an architect's eye.",
        '<a href="index.html">Home</a> › Properties') + f"""
<section id="selected">
  <div class="wrap">
    {shead("01","San Miguel de Allende")}
    <div class="split rv d1" style="align-items:start;">
      <h2>Houses for sale.</h2>
      <p class="lead">This is not a catalog and it is not meant to grow into one. The properties here are ones Roberto knows: some he designed, some were built with Espacios y Formas, some belong to clients, a few are simply houses he knows well enough to stand behind. Each sheet states its authorship and carries his notes — what works, what could change, what he sees in it.</p>
    </div>
    """ + fichas.grid(sma, wa) + f"""
    <div class="cap rv" style="margin-top:14px;">Prices in MXN; USD figures approximate · Open any sheet for plans, program, an architect's reading and the PDF</div>

    {shead("02","Countryside near San Miguel · Querétaro · Celaya", ' style="margin-top:60px;"')}
    """ + fichas.grid(listings.by('jalpa','sale') + listings.by('qro','sale') + listings.by('celaya','sale'), wa) + f"""

    {shead("03","Mid-term stays · historic center", ' style="margin-top:60px;"')}
    <p class="lead rv" style="max-width:720px;">Two furnished spaces inside Casa Cuadrante, the historic house Roberto restored and designed, with the Parroquia in front.</p>
    """ + fichas.grid(rent, wa) + f"""
  </div>
</section>

<section class="band" id="reading">
  <div class="wrap split" style="align-items:start;">
    <div class="rv">
      {shead("04","How a property is read here")}
      <h2>Before the transaction, the building.</h2>
    </div>
    <div class="rv d1">
      <p class="lead">A listing shows rooms and square meters. An architect reads the rest: how the structure was built and what condition it is in, how the plan distributes light and privacy, how the house sits on its lot and its slope, which materials will age well, what an intervention would involve and what the property could become. That reading goes into every sheet on this page, and it is what Roberto brings when asked to look at a property found elsewhere.</p>
      <div class="caps">
        <div><small>Architecture</small><span>Plan, proportion, orientation, light.</span></div>
        <div><small>Construction</small><span>Structure, materials, quality of execution, condition.</span></div>
        <div><small>Site</small><span>Lot, topography, views, relationship to context.</span></div>
        <div><small>Potential</small><span>Opportunities for intervention, extension or change of use.</span></div>
        <div><small>Roberto's Notes</small><span>A short personal assessment on each sheet.</span></div>
      </div>
      <div style="margin-top:18px;"><a class="btn" href="contact.html#buy">Ask Roberto to look at a property</a></div>
    </div>
  </div>
</section>

<section id="dev">
  <div class="wrap split" style="align-items:center;">
    <div class="rv">
      {shead("05","Developments")}
      <h2>Peñas Arriba · Magno · La Escondida.</h2>
      <p class="lead">Residential communities planned and built with Espacios y Formas, each with its authorship stated and its own sales site.</p>
      <div style="margin-top:18px;"><a class="btn ghost" href="work.html#developments">See the developments</a></div>
    </div>
    <div class="rv d1"><a class="lbx" href="img/parroquia-view-from-community.jpg"><img class="mapimg" src="img/parroquia-view-from-community.jpg" alt="Peñas Arriba"></a></div>
  </div>
</section>

<section class="band" id="sell">
  <div class="wrap split" style="align-items:start;">
    <div class="rv">
      {shead("06","Sell or be represented")}
      <h2>Have Roberto look at it first.</h2>
      <p class="lead">RBC represents a short list, and only after a visit. Send the basics; Roberto will say whether it fits, and what he sees in it as an architect.</p>
    </div>
    <div class="rv d1">
      {P.form("Tell me about your property", "It goes to Roberto's WhatsApp.",
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
        "A personal architecture practice, in collaboration with Espacios y Formas.",
        '<a href="index.html">Home</a> › About') + f"""
<section id="bio">
  <div class="wrap about">
    <div class="rv">
      <div class="portrait">Portrait pending — Roberto at work: site, drawings, materials</div>
    </div>
    <div class="rv d1">
      {shead("01","Roberto")}
      <h2>Architect first.</h2>
      <p class="lead">Roberto Balderas Carrillo is an architect from Celaya, Guanajuato, based in San Miguel de Allende. RBC is his personal practice: the projects he authors, the buildings he directs on site, and a short list of properties he represents because he knows them.</p>
      <div class="notes"><small>Criterion</small><p>Every project answers its site, its client, its budget and its scale. There is no house style; there is a way of deciding.</p></div>
      <p class="lead">Contemporary, colonial, contextual; a bar or a tower; a modest budget or a generous one. What repeats is the judgment: how the plan meets the site, where the light comes from, which material belongs, what will still be right in twenty years.</p>

      {shead("02","Espacios y Formas")}
      <h2>The infrastructure behind the practice.</h2>
      <p class="lead">{EYF_LINE} Its principal office is in Celaya, with a presence in San Miguel de Allende, and it works throughout the Bajío and elsewhere in Mexico: houses, residential communities, towers, serial housing, commercial buildings.</p>
      <p class="lead">In practice it means this: the conversation is with Roberto, and when a project needs engineering, crews, administration or the capacity to build at scale, that capacity is already there.</p>
      <div class="facts">
        <div><small>RBC</small><span>Roberto · authorship · personal attention · architectural judgment</span></div>
        <div><small>Espacios y Formas</small><span>Infrastructure · experience · technical and construction capacity</span></div>
        <div><small>Offices</small><span>San Miguel de Allende / Celaya</span></div>
        <div><small>Work</small><span>San Miguel de Allende · Bajío · México</span></div>
      </div>

      {shead("03","Capabilities")}
      <div class="caps">
        <div><small>Architecture</small><span>Architectural design · executive and construction documentation · multidisciplinary coordination</span></div>
        <div><small>Interiors · Landscape</small><span>Interior architecture · furniture · gardens and outdoor rooms</span></div>
        <div><small>Construction</small><span>Renovations, houses and larger residences directed by Roberto; developments, towers, commercial and hospitality with Espacios y Formas</span></div>
        <div><small>Properties</small><span>A selected list of properties, and an architect's reading of properties found elsewhere</span></div>
      </div>
      <div style="margin-top:26px;display:flex;gap:10px;flex-wrap:wrap;">
        <a class="btn red" href="{wa('Hi Roberto, I read your About page and I would like to talk.')}">WhatsApp +52 461 101 2474</a>
        <a class="btn ghost" href="https://www.instagram.com/arqrobertobalderas" target="_blank" rel="noopener">@arqrobertobalderas</a>
        <a class="btn ghost" href="{EYF}" target="_blank" rel="noopener">espaciosyformas.com.mx ↗</a>
      </div>
    </div>
  </div>
</section>
""" + P.contact_band(wa, "Contact", "Design, build, buy or sell — start with a message.",
        "English and Spanish. Roberto replies personally.", "Hi Roberto, I found your website and I would like to talk.", "WhatsApp +52 461 101 2474")
    ld = [{"@context":"https://schema.org","@type":"Person","name":"Roberto Balderas Carrillo","jobTitle":"Architect","url":f"{SITE}/about.html","worksFor":{"@type":"Organization","name":"RBC · Roberto Balderas Carrillo, Arquitecto","url":f"{SITE}/"},"affiliation":{"@type":"Organization","name":"Espacios y Formas","url":EYF},"sameAs":["https://www.instagram.com/arqrobertobalderas"],"address":{"@type":"PostalAddress","addressLocality":"San Miguel de Allende","addressRegion":"Guanajuato","addressCountry":"MX"}},
          {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"},{"@type":"ListItem","position":2,"name":"About","item":f"{SITE}/about.html"}]}]
    return ("about", "About — Roberto Balderas Carrillo, Arquitecto | RBC",
            "Roberto Balderas Carrillo is an architect based in San Miguel de Allende. RBC is his personal practice, working in close collaboration with Espacios y Formas, the Balderas family's architecture, construction and development firm with more than three decades of experience.",
            body, "img/valley-golden-hour.jpg", ld, "0.7")

# ───────────────────────────── CONTACT ─────────────────────────────
def contact(wa, SITE):
    F = P.form
    body = P.phero("img/sunset-terrace-luxury-villa-mexico.jpg", "RBC / Contact", "Tell me what you have in mind.",
        "WhatsApp is fastest; the forms below send straight to it. English and Spanish.",
        '<a href="index.html">Home</a> › Contact') + f"""
<section id="doors">
  <div class="wrap">
    <div class="intents rv">
      <a class="intent" href="#project"><small>01</small><b>Start a project</b><span>Design and/or build a house, a renovation, a building.</span></a>
      <a class="intent" href="#buy"><small>02</small><b>Buy a property</b><span>The selected properties, or one you found elsewhere.</span></a>
      <a class="intent" href="#sell"><small>03</small><b>Sell a property</b><span>Have Roberto look at it and, if it fits, represent it.</span></a>
      <a class="intent" href="#general"><small>04</small><b>General inquiry</b><span>Developers, brands, press, collaborations.</span></a>
    </div>
    <div style="margin-top:26px;display:flex;gap:12px;flex-wrap:wrap;align-items:center;" class="rv">
      <a class="btn red" href="{wa('Hi Roberto, I found your website and I would like to talk.')}">WhatsApp +52 461 101 2474</a>
      <span class="code">Roberto replies personally · Video calls for clients abroad</span>
    </div>
  </div>
</section>

<section class="band" id="project">
  <div class="wrap split" style="align-items:start;">
    <div class="rv">{shead("01","Start a project")}<h2>Design and build.</h2><p class="lead">A lot, a sketch or an idea. Land owners can ask for a first reading of what their site allows.</p></div>
    <div class="rv d1">{F("Project", "Three questions and a text box.",
        [("row",[("text","Name","Your name","Jane Smith"),("select","Location","Where",["San Miguel de Allende","Querétaro","Celaya","Elsewhere in the Bajío","Elsewhere in Mexico","I don't have a lot yet"])]),
         ("row",[("select","Scope","What you need",["Design + construction","Design only","Construction from my plans","Renovation / restoration","A reading of my lot","A building / development"]),("select","Budget","Budget (USD)",["Under $300K","$300K – $600K","$600K – $1.2M","Over $1.2M","Not sure yet"])]),
         ("area","Details","Tell me about it","")], "Hi Roberto, I'd like to start a project:", "Send to Roberto")}</div>
  </div>
</section>
<div id="land"></div>

<section id="buy">
  <div class="wrap split" style="align-items:start;">
    <div class="rv">{shead("02","Buy a property")}<h2>With an architect's reading.</h2><p class="lead">The selected properties on this site, or a listing you found elsewhere that you would like Roberto to look at before you commit.</p></div>
    <div class="rv d1">{F("Buying", "What are you looking for?",
        [("row",[("text","Name","Your name","Jane Smith"),("select","City","City",["San Miguel de Allende","Querétaro","Celaya","Not sure yet"])]),
         ("row",[("select","Budget","Budget (USD)",["Under $400K","$400K – $800K","$800K – $1.5M","$1.5M – $3M","Over $3M"]),("select","When","When",["As soon as possible","3–6 months","6–12 months","Exploring"])]),
         ("area","Details","What matters most, or a link to a property you'd like looked at","")], "Hi Roberto, I'm looking to buy:", "Send to Roberto")}</div>
  </div>
</section>

<section class="band" id="sell">
  <div class="wrap split" style="align-items:start;">
    <div class="rv">{shead("03","Sell a property")}<h2>Have it looked at first.</h2><p class="lead">RBC represents a short list. Send the basics and Roberto will say whether it fits.</p></div>
    <div class="rv d1">{F("Selling", "A visit comes before any decision.",
        [("row",[("text","Name","Your name","Jane Smith"),("select","Location","Where",["San Miguel de Allende","Querétaro","Celaya","Elsewhere in the Bajío"])]),
         ("row",[("select","Type","Type",["House","Apartment","Lot","Commercial","Other"]),("select","Goal","Goal",["Sell","Rent","An opinion first"])]),
         ("area","Details","Describe the property","")], "Hi Roberto, I have a property I'd like you to look at:", "Send to Roberto")}</div>
  </div>
</section>

<section id="general">
  <div class="wrap split" style="align-items:start;">
    <div class="rv">{shead("04","General inquiry")}<h2>Anything else.</h2><p class="lead">Developers, brands, press, collaborations, or a question that doesn't fit above.</p>
      <div class="facts"><div><small>WhatsApp</small><span>+52 461 101 2474</span></div><div><small>Instagram</small><span>@arqrobertobalderas</span></div><div><small>Offices</small><span>San Miguel de Allende / Celaya (Espacios y Formas)</span></div></div></div>
    <div class="rv d1">{F("Message", "Straight to WhatsApp.",
        [("row",[("text","Name","Your name","Jane Smith"),("text","Contact","Best way to reach you","Phone or email")]),
         ("area","Message","Message","")], "Hi Roberto, I'm writing from your website:", "Send to Roberto")}</div>
  </div>
</section>
"""
    ld = [{"@context":"https://schema.org","@type":"ContactPage","url":f"{SITE}/contact.html","name":"Contact Roberto Balderas Carrillo, Arquitecto"},
          {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"},{"@type":"ListItem","position":2,"name":"Contact","item":f"{SITE}/contact.html"}]}]
    return ("contact", "Contact — Start a Project, Buy or Sell a Property | RBC · Roberto Balderas Carrillo, Arquitecto",
            "Contact architect Roberto Balderas Carrillo in San Miguel de Allende: start a design-and-build project, ask for a reading of your lot, buy a selected property or have a property looked at for sale. WhatsApp +52 461 101 2474.",
            body, "img/sunset-terrace-luxury-villa-mexico.jpg", ld, "0.6")

# ───────────────────────────── REDIRECTS ─────────────────────────────
def redirect(slug, to):
    body = f'<meta http-equiv="refresh" content="0; url={to}"><div class="wrap" style="padding:140px 32px;"><p class="lead">This page moved to <a href="{to}">{to}</a>.</p></div>'
    return (slug, "Redirecting — RBC", "This page has moved.", body, HZ, [], "0.1")

REDIRECTS = (("real-estate","properties.html"),("roberto-balderas-carrillo","about.html"),
             ("architecture","work.html"),("construction","work.html#construction"),("development","work.html#developments"))

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
