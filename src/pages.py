# -*- coding: utf-8 -*-
"""Page contents for the RBC site. Each function returns (slug, title, desc, body, og_image, jsonld, priority)."""
import re, os
import projects
import listings
import fichas

HERE = os.path.dirname(__file__)
PA = "https://penasarriba.vercel.app/PE%C3%91AS%20ARRIBA/fotos"
HZ_HERO = f"img/casa-horizonte-sunset-facade.jpg"

def phero(bg, tag, h1, sub, crumbs="", pos=""):
    bgs = bg if isinstance(bg, (list, tuple)) else [bg]
    rot = f' data-rot="{"|".join(bgs)}"' if len(bgs) > 1 else ""
    return f"""
<header class="phero"{rot}>
  <div class="bg" style="background-image:url('{bgs[0]}'){(';background-position:' + pos) if pos else ''}"></div>
  <div class="in">
    {f'<div class="crumbs">{crumbs}</div>' if crumbs else ''}
    <div class="tag">{tag}</div>
    <h1>{h1}</h1>
    <p class="sub">{sub}</p>
  </div>
</header>"""

def listing_card(img, alt, status, name, sub, usd, mxn, specs, href, cta, cls="", green=True):
    sp = "".join(f"<span><b>{a}</b> {b}</span>" for a, b in specs)
    return f"""
      <div class="lcard rv {cls}">
        <div class="im"><span class="st {'green' if green else ''}">{status}</span><img src="{img}" alt="{alt}" loading="lazy"></div>
        <div class="bd">
          <h3>{name}</h3>
          <div class="sub2">{sub}</div>
          <div class="pr">{usd} <small>· {mxn}</small></div>
          <div class="sp">{sp}</div>
          <a class="btn" href="{href}">{cta}</a>
        </div>
      </div>"""

def contact_band(wa, eyebrow, h2, lead, msg, btn):
    return f"""
<section class="contact" id="contact">
  <div class="wrap">
    <div class="eyebrow rv" style="color:var(--gold);">{eyebrow}</div>
    <h2 class="rv d1">{h2}</h2>
    <p class="lead rv d2">{lead}</p>
    <div class="cgrid rv d2">
      <a class="btn red" href="{wa(msg)}">{btn}</a>
      <a class="btn ghost lt" href="https://www.instagram.com/arqrobertobalderas" target="_blank" rel="noopener">@arqrobertobalderas</a>
    </div>
  </div>
</section>"""

def form(title, intro, fields, wa_prefix, btn):
    rows = ""
    for f in fields:
        if f[0] == "row":
            rows += '<div class="row">' + "".join(field(x) for x in f[1]) + "</div>"
        else:
            rows += field(f)
    return f"""
    <div class="form rv">
      <h3 class="serif" style="font-size:1.5rem;margin-bottom:6px;">{title}</h3>
      <p style="font-size:.92rem;color:var(--ink-soft);">{intro}</p>
      <form data-wa="{wa_prefix}">
        {rows}
        <button class="btn red" type="submit">{btn}</button>
        <div class="note">Sends your answers to Roberto on WhatsApp. Nothing is stored on this website.</div>
      </form>
    </div>"""

def field(f):
    kind, name, label = f[0], f[1], f[2]
    if kind == "text":
        return f'<div><label>{label}</label><input name="{name}" type="text" placeholder="{f[3] if len(f)>3 else ""}"></div>'
    if kind == "select":
        opts = "".join(f'<option>{o}</option>' for o in f[3])
        return f'<div><label>{label}</label><select name="{name}">{opts}</select></div>'
    if kind == "area":
        return f'<div><label>{label}</label><textarea name="{name}" placeholder="{f[3] if len(f)>3 else ""}"></textarea></div>'
    return ""

# ───────────────────────────── HOME ─────────────────────────────
def home(wa, SITE):
    body = f"""
<header class="hero home" id="top">
  <div class="bg" style="background-image:url('{HZ_HERO}')"></div>
  <div class="in">
    <div class="tag">Celaya · Querétaro · San Miguel de Allende, México</div>
    <h1>The person who designs it, builds it — and sells it to you directly.</h1>
    <p class="sub">Roberto Balderas Carrillo. Architect, builder, developer and real estate advisor in the Bajío. 30 years, 2,600+ homes, one point of contact.</p>
    <div class="roles">
      <span><b>01</b>Real Estate Advisor</span><span><b>02</b>Architect &amp; Designer</span><span><b>03</b>Builder</span><span><b>04</b>Developer</span>
    </div>
    <div class="pricebar">
      <a class="btn red" href="real-estate.html">Browse homes for sale</a>
      <a class="btn ghost lt" href="{wa('Hi Roberto, I would like a quote for a project / construction, or help buying a property.')}">Get a quote or buyer help</a>
    </div>
  </div>
  <div class="scrollcue">︾</div>
</header>

<div class="stats">
  <div class="in">
    <div><div class="n">30</div><div class="l">years designing &amp; building</div></div>
    <div><div class="n">2,600</div><div class="l">homes delivered</div></div>
    <div><div class="n">3</div><div class="l">cities · Bajío region</div></div>
    <div><div class="n">0</div><div class="l">middlemen</div></div>
    <div><div class="n">1</div><div class="l">point of contact</div></div>
  </div>
</div>

<section id="services">
  <div class="wrap">
    <div class="eyebrow rv">RBC · Four practices, one architect</div>
    <h2 class="rv d1">Four ways to work with the architect directly.</h2>
    <p class="lead rv d2" style="max-width:700px;">Whether you're buying a finished home, commissioning a design, building on your lot or following a development in progress — you'll be talking to the same person from the first call to the keys.</p>
    <div class="pillars">
      <a class="pillar rv" href="real-estate.html">
        <img src="img/luxury-villa-sunset-san-miguel.jpg" alt="Luxury homes for sale in San Miguel de Allende">
        <div class="t"><div class="num">01</div><h3>Real Estate</h3><p>Luxury homes for sale in San Miguel de Allende, Querétaro and Celaya — sold direct by the architect-developer. Buyer representation for foreigners.</p><span class="go">See the catalog →</span></div>
      </a>
      <a class="pillar rv d1" href="architecture.html">
        <img src="img/hero-terrace-sunset.jpg" alt="Architecture and design projects by Roberto Balderas Carrillo">
        <div class="t"><div class="num">02</div><h3>Architecture &amp; Design</h3><p>Residential architecture that belongs to its site. Tell us about your lot and your life; we design the house around both.</p><span class="go">Design my home →</span></div>
      </a>
      <a class="pillar rv d2" href="construction.html">
        <img src="img/projects-custom-build.jpg" alt="Custom home construction in the Bajío">
        <div class="t"><div class="num">03</div><h3>Construction</h3><p>Our own crews, our own stone. Turnkey construction with transparent budgets — for our designs or yours.</p><span class="go">Quote my build →</span></div>
      </a>
      <a class="pillar rv d3" href="development.html">
        <img src="img/community-club-pool.jpg" alt="Peñas Arriba residential development, San Miguel de Allende">
        <div class="t"><div class="num">04</div><h3>Development</h3><p>Residential communities we plan, build and manage — starting with Peñas Arriba, the highest gated hillside in San Miguel.</p><span class="go">See what's in progress →</span></div>
      </a>
    </div>
  </div>
</section>

<section class="band" id="featured">
  <div class="wrap">
    <div class="eyebrow rv">Featured Listing · San Miguel de Allende</div>
    <h2 class="rv d1">Casa Horizonte — an exceptional opportunity above the world's favorite town.</h2>
    <div class="split" style="margin-top:22px;">
      <div class="rv">
        <a href="casa-horizonte.html"><img class="mapimg" src="img/casa-horizonte-infinity-pool.jpg" alt="Infinity pool of Casa Horizonte overlooking San Miguel de Allende"></a>
      </div>
      <div class="rv d1">
        <p class="lead">6,693 sq ft (622 m²) of architect-designed hillside living with an infinity pool and a front-row, protected view of the Parroquia, inside gated Peñas Arriba. Under construction — you choose every finish.</p>
        <div class="pr" style="font-family:'Fraunces',serif;font-size:1.8rem;color:var(--red);margin:14px 0 4px;">US $1.9M <small style="font-family:'Figtree',sans-serif;font-size:.85rem;color:var(--ink-soft);">· MX $32.5M · ≈ US $284 / built sq ft</small></div>
        <ul class="checks">
          <li>5 bedrooms · 5½ baths · elevator-ready · wine cellar in natural stone</li>
          <li>7 minutes to the historic center · 24/7 gated community</li>
          <li>Direct title for foreign buyers — no bank trust needed inland</li>
        </ul>
        <div style="margin-top:20px;display:flex;gap:10px;flex-wrap:wrap;">
          <a class="btn" href="casa-horizonte.html">See the full listing</a>
          <a class="btn ghost" href="real-estate.html">All homes for sale</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="teaser">
  <div class="wrap">
    <div class="eyebrow rv">Now available · direct from the architect</div>
    <h2 class="rv d1">A few of the homes.</h2>
    """ + fichas.grid([l for l in listings.L if l['slug'] in ('casa-horizonte','casa-travertino','casa-mirador')], wa) + f"""
    <div style="text-align:center;margin-top:26px;" class="rv"><a class="btn ghost" href="real-estate.html">See the full catalog →</a></div>
  </div>
</section>

<section id="why">
  <div class="wrap">
    <div class="eyebrow rv">Why direct from the architect</div>
    <h2 class="rv d1">Transparent pricing. Honest timelines. Finishes chosen together.</h2>
    <div class="steps">
      <div class="step rv"><div class="k">01</div><h4>Buy</h4><p>Every home we list was designed and built by us. No listing commissions priced in, and the person answering your questions is the one who drew the plans. We also represent foreign buyers looking elsewhere in San Miguel and Querétaro.</p></div>
      <div class="step rv d1"><div class="k">02</div><h4>Design &amp; build</h4><p>Bring a lot, a sketch or just an idea. We deliver architecture, engineering, permits and construction under one roof — with a budget you can read and a schedule we keep.</p></div>
      <div class="step rv d2"><div class="k">03</div><h4>Invest</h4><p>Our communities are finished by a single studio that designs, builds and sells — so they complete faster and appreciate sooner. Ask about lots and early-stage homes.</p></div>
    </div>
  </div>
</section>

<section class="band" style="padding-top:0;padding-bottom:0;">
  <div class="marq"><div class="mtrk">
    Architect · Builder · Developer · Real Estate Advisor · <b>San Miguel de Allende</b> · Querétaro · Celaya · Direct from the architect · Finishes by you · <b>30 years · 2,600+ homes</b> · &nbsp;
    Architect · Builder · Developer · Real Estate Advisor · <b>San Miguel de Allende</b> · Querétaro · Celaya · Direct from the architect · Finishes by you · <b>30 years · 2,600+ homes</b> · &nbsp;
  </div></div>
</section>

<section id="about">
  <div class="wrap aboutgrid">
    <div class="rv">
      <div class="eyebrow">Roberto Balderas Carrillo</div>
      <h2>Architect. Builder. Developer. Your direct counterpart.</h2>
      <p class="lead">I'm an architect, builder and developer working across <strong>Celaya, Querétaro and San Miguel de Allende</strong>. RBC is my studio within <strong>Espacios y Formas</strong>, the group that in 30 years has designed, built and delivered more than 2,600 homes — communities like <strong>Peñas Arriba</strong>, the <strong>Magno</strong> towers in Celaya, and custom homes across the Bajío. Working with me means the best of both worlds: the experience, engineering and guarantees of a large firm, with one architect's attention to every detail — from a small renovation to a whole building.</p>
      <div style="margin-top:20px;display:flex;gap:10px;flex-wrap:wrap;">
        <a class="btn ghost" href="roberto-balderas-carrillo.html">About Roberto →</a>
        <a class="btn ghost" href="https://www.espaciosyformas.com.mx/" target="_blank" rel="noopener">Our construction firm — Espacios y Formas</a>
      </div>
    </div>
    <div class="card rv d1" style="background:#fff;border:1px solid var(--line);border-radius:8px;padding:36px;text-align:center;box-shadow:0 18px 45px -25px rgba(26,35,80,.3);">
      <img src="img/rbc-logo.png" alt="RBC — Roberto Balderas Carrillo, Arquitecto" style="height:64px;margin:0 auto 16px;width:auto;">
      <div class="serif" style="font-size:1.25rem;">Roberto Balderas Carrillo</div>
      <div class="cap" style="margin-top:2px;">Architect · Builder · Developer · Real Estate Advisor</div>
      <div class="cap" style="margin-top:8px;">Celaya · Querétaro · San Miguel de Allende</div>
      <div style="margin-top:20px;display:grid;gap:9px;">
        <a class="btn" href="{wa('Hi Roberto, I found your website and I would like to talk.')}">WhatsApp Roberto</a>
        <a class="btn ghost" href="https://www.instagram.com/arqrobertobalderas" target="_blank" rel="noopener">@arqrobertobalderas</a>
      </div>
    </div>
  </div>
</section>
""" + contact_band(wa, "Let's talk", "Buying, designing, building or investing — start with a message.",
        "Tell me what you have in mind and I'll reply personally. English and Spanish spoken.",
        "Hi Roberto, I found your website. I'm interested in: ", "WhatsApp Roberto") + fichas.modal_data([l for l in listings.L if l['slug'] in ('casa-horizonte','casa-travertino','casa-mirador')], wa)
    return ("index",
            "Luxury Homes for Sale in San Miguel de Allende &amp; Querétaro — Direct from the Architect | RBC Roberto Balderas Carrillo",
            "Architect, builder, developer and real estate advisor in San Miguel de Allende, Querétaro and Celaya. Luxury homes for sale direct from the architect-developer, custom home design and construction quotes, and buyer representation for foreigners. WhatsApp +52 461 101 2474.",
            body, HZ_HERO, "org", "1.0")

# ───────────────────────────── REAL ESTATE ─────────────────────────────
def real_estate(wa, SITE):
    body = phero("img/luxury-home-san-miguel-de-allende-terrace.jpg", "01 · Real Estate · Direct from the architect-developer",
        "Luxury homes for sale in San Miguel de Allende, Querétaro and Celaya.",
        "Every home in this catalog was designed and built by our studio — you buy from the architect, not a middleman. Prices in USD and MXN; measurements in sq ft and m².",
        '<a href="index.html">Home</a> › Real Estate') + f"""
<section id="catalog">
  <div class="wrap">
    <div class="eyebrow rv">The catalog · by city</div>
    <h2 class="rv d1">Choose your city.</h2>
    <div class="cities rv d2">
      <a class="on" href="#san-miguel">San Miguel de Allende</a><a href="#countryside">Countryside near San Miguel</a><a href="#queretaro">Querétaro</a><a href="#celaya">Celaya</a><a href="#rentals">Rentals</a>
    </div>

    <div class="cityhead" id="san-miguel"><h3>San Miguel de Allende</h3><span class="cnt">{len(listings.by('sma','sale'))} homes for sale · Peñas Arriba &amp; historic center</span></div>
    <p class="lead rv" style="max-width:720px;margin-top:12px;">Inside Peñas Arriba — the highest gated community in town, with protected Parroquia views, 7 minutes from the historic center — we design, build and sell the homes ourselves: finished residences, shell-built homes ready for your finishes, and lots from 2,150 to 12,900 sq ft. Plus a furnished townhouse in the very center. Direct title for foreign buyers.</p>
    """ + fichas.grid(listings.by('sma','sale'), wa) + f"""
    <div class="cap rv" style="margin-top:14px;">USD figures approximate at prevailing exchange rates · Every Peñas Arriba listing includes finish selection with the architect's studio · <a href="development.html#penas-arriba">Lots and the full community →</a></div>

    <div class="cityhead" id="countryside"><h3>Countryside near San Miguel</h3><span class="cnt">Jalpa road · 15 minutes from town</span></div>
    """ + fichas.grid(listings.by('jalpa','sale'), wa) + f"""

    <div class="cityhead" id="queretaro"><h3>Querétaro</h3><span class="cnt">Club de Golf El Campanario</span></div>
    """ + fichas.grid(listings.by('qro','sale'), wa) + f"""

    <div class="cityhead" id="celaya"><h3>Celaya</h3><span class="cnt">Magno Home &amp; Towers · built by our group</span></div>
    """ + fichas.grid(listings.by('celaya','sale'), wa) + f"""
    <div class="soon rv" style="margin-top:18px;">
      <h4>Apartments with immediate delivery, homes and lots in Magno.</h4>
      <p>Ask for the current inventory and floor plans — units are released as they complete.</p>
      <a class="btn" style="margin-top:16px;" href="{wa('Hi Roberto, I would like the current inventory of apartments, homes and lots in Magno, Celaya.')}">Ask for Magno inventory</a>
    </div>

    <div class="cityhead" id="rentals"><h3>Rentals · San Miguel de Allende</h3><span class="cnt">Mid-term stays · furnished · services included</span></div>
    <p class="lead rv" style="max-width:720px;margin-top:12px;">Two furnished spaces inside Casa Cuadrante — the restored house above the celebrated restaurant of the same name, in the heart of the historic center — with the Parroquia right in front of you.</p>
    """ + fichas.grid(listings.by('sma','rent'), wa) + f"""
  </div>
</section>

<section class="band" id="buyers">
  <div class="wrap split">
    <div class="rv">
      <div class="eyebrow">Buyer representation · Foreign buyers welcome</div>
      <h2>Looking for something not on this list? We'll manage the purchase.</h2>
      <p class="lead">As an architect who has built here for three decades, I can evaluate any property in San Miguel or Querétaro the way a buyer's engineer would — structure, water, permits, resale — and guide you through notary, title and closing in English.</p>
      <ul class="checks">
        <li>Property search and technical evaluation by an architect</li>
        <li>Negotiation, notary coordination and closing support</li>
        <li>Direct title for foreigners in the Mexican interior — no fideicomiso</li>
        <li>Renovation or extension quotes for the home you buy</li>
      </ul>
    </div>
    <div class="rv d1">
      {form("Tell me what you're looking for", "Answer a few questions and the summary goes straight to my WhatsApp.",
        [("row",[("text","Name","Your name","Jane Smith"),("select","City","City",["San Miguel de Allende","Querétaro","Celaya","Not sure yet"])]),
         ("row",[("select","Budget","Budget (USD)",["Under $400K","$400K – $800K","$800K – $1.5M","$1.5M – $3M","Over $3M"]),("select","Timing","When",["As soon as possible","3–6 months","6–12 months","Just exploring"])]),
         ("area","Details","What matters most to you","Views, bedrooms, garden, walkable to centro, rental potential…")],
        "Hi Roberto, I'm looking for a property. Here are my details:", "Send to Roberto on WhatsApp")}
    </div>
  </div>
</section>
""" + contact_band(wa, "Private showings", "See it at sunset. That's when it wins you over.",
        "Private, by appointment — the homes, the community and the view in about an hour. English spoken.",
        "Hi Roberto, I would like to schedule a private showing in San Miguel de Allende.", "WhatsApp Roberto") + fichas.modal_data(listings.L, wa)
    ld = [{"@context":"https://schema.org","@type":"ItemList","name":"Luxury homes for sale and rent by RBC — San Miguel de Allende, Querétaro, Celaya",
      "itemListElement":[{"@type":"ListItem","position":i+1,"name":f"{l['name']} — {l['where']}","url":f"{SITE}/{l['slug']}.html" if l.get('page') else f"{SITE}/real-estate.html"} for i,l in enumerate(listings.L)]},
      {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"},{"@type":"ListItem","position":2,"name":"Real Estate","item":f"{SITE}/real-estate.html"}]}]
    return ("real-estate",
            "Luxury Homes for Sale — San Miguel de Allende, Querétaro &amp; Celaya | RBC Real Estate",
            "Catalog of luxury homes for sale direct from the architect-developer: Casa Horizonte (US $1.9M), Casa Zafiro (US $818K) and duplex residences from US $389K in gated Peñas Arriba, San Miguel de Allende. Querétaro and Celaya inventory on request. Buyer representation for foreigners.",
            body, "img/luxury-home-san-miguel-de-allende-terrace.jpg", ld, "0.9")

# ───────────────────────────── CASA HORIZONTE (template page) ─────────────────────────────
def casa_horizonte(wa, SITE):
    src = open(os.path.join(HERE, "horizonte-src.html"), encoding="utf-8").read()
    body = src.split('<header class="hero" id="top">')[1].split('<footer>')[0]
    body = '<header class="hero" id="top">' + body
    body = body.replace("https://rbc-realestate.netlify.app/img/", "img/")
    # remove the old about/listings sections (now site-wide pages) -> keep listings as "more homes" but link to catalog
    body = re.sub(r'<section style="padding-top:0;" id="about">.*?</section>\n', "", body, flags=re.S)
    body = body.replace('<h2 class="rv d1">Three more residences, ready much sooner.</h2>',
                        '<h2 class="rv d1">Three more residences, ready much sooner.</h2>')
    body = body.replace('<div class="cap rv" style="margin-top:14px;">USD figures approximate',
                        '<div style="text-align:center;margin-top:22px;" class="rv"><a class="btn ghost" href="real-estate.html">See the full catalog — San Miguel · Querétaro · Celaya →</a></div>\n    <div class="cap rv" style="margin-top:14px;">USD figures approximate')
    # inject property sub-nav + breadcrumb under hero
    body = body.replace('<div class="tag">Exclusive Listing · San Miguel de Allende, México</div>',
        '<div class="crumbs"><a href="index.html">Home</a> › <a href="real-estate.html">Real Estate</a> › San Miguel de Allende</div>\n    <div class="tag">Exclusive Listing · San Miguel de Allende, México</div>')
    ld_src = open(os.path.join(HERE, "horizonte-src.html"), encoding="utf-8").read()
    lds = re.findall(r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>', ld_src, flags=re.S)
    import json
    ld = []
    for s in lds:
        j = json.loads(s)
        if j.get("@type") == "ItemList":
            continue
        txt = json.dumps(j).replace("https://rbc-realestate.vercel.app/#listings", f"{SITE}/real-estate.html").replace("https://rbc-realestate.vercel.app/#top", f"{SITE}/casa-horizonte.html").replace("https://rbc-realestate.vercel.app/", f"{SITE}/casa-horizonte.html")
        ld.append(json.loads(txt))
    ld.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"},{"@type":"ListItem","position":2,"name":"Real Estate","item":f"{SITE}/real-estate.html"},{"@type":"ListItem","position":3,"name":"Casa Horizonte","item":f"{SITE}/casa-horizonte.html"}]})
    return ("casa-horizonte",
            "Casa Horizonte — Luxury Home for Sale in San Miguel de Allende, US $1.9M | RBC Real Estate",
            "Casa Horizonte: 6,693 sq ft architect-designed estate under construction in gated Peñas Arriba, San Miguel de Allende. Infinity pool, protected Parroquia views, 5 bedrooms, finishes chosen by you. US $1.9M (MX $32.5M) — direct from the architect. WhatsApp +52 461 101 2474.",
            body, HZ_HERO, ld, "0.9")

# ───────────────────────────── ARCHITECTURE ─────────────────────────────
def architecture(wa, SITE):
    body = phero("img/architecture-section-hillside-home.jpg", "02 · Architecture &amp; Design",
        "Houses designed with the hill, not against it.",
        "RBC is the studio of Roberto Balderas Carrillo within Espacios y Formas — more than 30 years of architecture and construction in the Bajío. From a small renovation or restoration to a residential tower, with the attention of a single architect.",
        '<a href="index.html">Home</a> › Architecture &amp; Design') + f"""
<section id="approach">
  <div class="wrap split">
    <div class="rv">
      <div class="eyebrow">How we design</div>
      <h2>Site first. Light second. Then the plan.</h2>
      <p class="lead">Thirty years of building in this region taught us what lasts here: stone from the site itself, deep terraces facing the view, cross-ventilation instead of machinery, and plans that follow the slope so every principal room gets the light and the vista. Casa Horizonte — entered from the top, stepping down the hillside — is the clearest example.</p>
      <p class="lead" style="margin-top:14px;">RBC works inside <a href="https://www.espaciosyformas.com.mx/" target="_blank" rel="noopener">Espacios y Formas</a>, the group that has designed and built more than 2,600 homes — and Magno Towers in Celaya — so a house designed here comes with the engineering, permits, crews and guarantees of a large firm, and the personal attention of one architect from the first sketch to the keys.</p>
      <ul class="checks">
        <li>Architectural design, executive project and engineering</li>
        <li>Interior design, furniture design and landscaping as one project</li>
        <li>Permits and municipal procedures handled for you</li>
        <li>Construction and real-estate advisory by the same team — or drawings ready for yours</li>
        <li>Renovations and restorations of historic houses; apartment buildings; commercial spaces</li>
      </ul>
    </div>
    <div class="rv d1">
      <a class="lbx" href="img/architecture-section-hillside-home.jpg"><img class="mapimg" src="img/architecture-section-hillside-home.jpg" alt="Architectural section of a hillside home by Roberto Balderas Carrillo"></a>
      <div class="cap">Casa Horizonte — section through the hillside · tap to enlarge</div>
    </div>
  </div>
</section>

""" + projects.index_section() + f"""

<section id="design-form">
  <div class="wrap split">
    <div class="rv">
      <div class="eyebrow">Design your home</div>
      <h2>Let's design yours.</h2>
      <p class="lead">Share the basics — where the lot is, how you live, what budget you're thinking of — and I'll come back with a first conversation, not a sales pitch. If you don't have a lot yet, we'll help you find the right one.</p>
      <div class="steps" style="grid-template-columns:1fr;gap:12px;">
        <div class="step"><div class="k">1</div><h4>Conversation &amp; site visit</h4><p>We walk the lot together and talk about how you want to live in the house.</p></div>
        <div class="step"><div class="k">2</div><h4>Concept &amp; budget</h4><p>Preliminary plans, a 3D model and a realistic construction budget.</p></div>
        <div class="step"><div class="k">3</div><h4>Project &amp; permits</h4><p>Full architectural and engineering drawings, permits, and — if you wish — our crews build it.</p></div>
      </div>
    </div>
    <div class="rv d1">
      {form("Start a design project", "Your answers go straight to my WhatsApp.",
        [("row",[("text","Name","Your name","Jane Smith"),("select","Location","Where is the lot",["San Miguel de Allende","Querétaro","Celaya","Elsewhere in the Bajío","I don't have a lot yet"])]),
         ("row",[("select","Size","Approximate house size",["Under 2,000 sq ft (185 m²)","2,000 – 3,500 sq ft","3,500 – 5,500 sq ft","Over 5,500 sq ft (510 m²)"]),("select","Budget","Construction budget (USD)",["Under $300K","$300K – $600K","$600K – $1.2M","Over $1.2M","Not sure yet"])]),
         ("area","Details","Tell me about the house you imagine","Bedrooms, views, pool, home office, guest house, style references…")],
        "Hi Roberto, I would like to design a home with you. Here are my details:", "Send to Roberto on WhatsApp")}
    </div>
  </div>
</section>
""" + contact_band(wa, "Architecture & Design", "Prefer to talk first?",
        "Send a message and we'll set up a call or a visit. English and Spanish spoken.",
        "Hi Roberto, I would like to talk about designing a house.", "WhatsApp Roberto")
    ld = [{"@context":"https://schema.org","@type":"Service","serviceType":"Residential architecture and design","provider":{"@type":"Organization","name":"RBC · Roberto Balderas Carrillo"},"areaServed":["San Miguel de Allende","Querétaro","Celaya"],"url":f"{SITE}/architecture.html"},
          {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"},{"@type":"ListItem","position":2,"name":"Architecture & Design","item":f"{SITE}/architecture.html"}]}]
    return ("architecture",
            "Residential Architect in San Miguel de Allende &amp; Querétaro — Custom Home Design | Roberto Balderas Carrillo",
            "Custom residential architecture and interior design in San Miguel de Allende, Querétaro and Celaya by architect Roberto Balderas Carrillo. Site-driven hillside homes, engineering and permits in-house, built by our own firm. Request a design consultation.",
            body, "img/architecture-section-hillside-home.jpg", ld, "0.8")

# ───────────────────────────── CONSTRUCTION ─────────────────────────────
def construction(wa, SITE):
    body = phero("img/projects-custom-build.jpg", "03 · Construction · Espacios y Formas",
        "From a small renovation to a complete tower — built the same way.",
        "Turnkey construction in San Miguel de Allende, Querétaro and Celaya, backed by the 30-year infrastructure of Espacios y Formas and led with the architect's personal attention. Houses we design or plans you bring; renovations, restorations, apartment buildings, commercial spaces.",
        '<a href="index.html">Home</a> › Construction') + f"""
<section id="how">
  <div class="wrap">
    <div class="eyebrow rv">How we build</div>
    <h2 class="rv d1">Transparent budgets. Schedules we keep. Stone from the site.</h2>
    <div class="steps">
      <div class="step rv"><div class="k">01</div><h4>Itemized quote, no surprises</h4><p>Every quote is broken down by concept and quantity, so you can compare it line by line. Processes proven over hundreds of deliveries guarantee the house arrives on time and as promised.</p></div>
      <div class="step rv d1"><div class="k">02</div><h4>Own crews &amp; supervision</h4><p>Masons, stone cutters, carpenters and installers who have worked with us for years, supervised daily by our architects.</p></div>
      <div class="step rv d2"><div class="k">03</div><h4>Weekly reporting</h4><p>Photos, progress and spend every week — especially useful if you live abroad while your house is built.</p></div>
    </div>
  </div>
</section>

""" + f"""
<section class="band" id="work">
  <div class="wrap">
    <div class="eyebrow rv">What we build · the large scale</div>
    <h2 class="rv d1">From a single room to a whole tower.</h2>
    <p class="lead rv d2" style="max-width:720px;">Through Espacios y Formas, our group has been building in the Bajío for more than 30 years — residential towers, gated communities, custom homes, dealerships and commercial centers. These are the builds we're proudest of.</p>
    <div class="pgrid">
      <a class="pj rv" href="development.html#magno"><img src="img/community-club-pool.jpg" alt="Magno Towers, Celaya"><div class="pc"><span>Celaya · residential towers</span><b>Magno Towers &amp; Magno Residencial</b></div></a>
      <a class="pj rv d1" href="development.html#penas-arriba"><img src="img/stone-walls-community.jpg" alt="Peñas Arriba, San Miguel de Allende"><div class="pc"><span>San Miguel de Allende · gated community</span><b>Peñas Arriba</b></div></a>
      <a class="pj rv d2" href="casa-ether.html"><img src="img/luxury-home-san-miguel-de-allende-terrace.jpg" alt="Casa Ether"><div class="pc"><span>Jalpa · country home</span><b>Casa Ether</b></div></a>
      <a class="pj rv" href="casa-travertino.html"><img src="img/villa-garden-day.jpg" alt="Casa Travertino"><div class="pc"><span>Querétaro · El Campanario</span><b>Casa Travertino</b></div></a>
      <a class="pj rv d1" href="casa-horizonte.html"><img src="img/casa-horizonte-sunset-facade.jpg" alt="Casa Horizonte"><div class="pc"><span>San Miguel de Allende · in progress</span><b>Casa Horizonte</b></div></a>
      <a class="pj rv d2" href="{wa('Hi Roberto, I would like to know more about Casa Elo.')}"><img src="img/projects-custom-build.jpg" alt="Casa Elo"><div class="pc"><span>Custom home · in progress</span><b>Casa Elo</b></div></a>
      <a class="pj rv" href="{wa('Hi Roberto, I would like to know more about your golf-club residence in San Miguel.')}"><img src="img/gated-entrance-luxury-home.jpg" alt="Golf-club residence"><div class="pc"><span>San Miguel de Allende · golf club · private</span><b>Golf-club residence</b></div></a>
      <a class="pj rv d1" href="{wa('Hi Roberto, I would like to know more about the JC apartment renovation.')}"><img src="img/luxury-home-san-miguel-interior-living.jpg" alt="Apartment JC"><div class="pc"><span>Historic center · renovation</span><b>Apartment JC</b></div></a>
      <a class="pj rv d2" href="development.html#escondida"><img src="img/community-trails.jpg" alt="La Escondida"><div class="pc"><span>San Miguel de Allende · communities</span><b>La Escondida &amp; La Nueva Escondida</b></div></a>
    </div>
    <div class="provnote rv">Provisional images — construction photography is being curated.</div>
    <div style="text-align:center;margin-top:26px;" class="rv">
      <a class="btn ghost" href="https://www.espaciosyformas.com.mx/" target="_blank" rel="noopener">Espacios y Formas — 30+ years, the full scale →</a>
    </div>
  </div>
</section>
""" + f"""

<section id="quote">
  <div class="wrap split">
    <div class="rv">
      <div class="eyebrow">Get a quote</div>
      <h2>Quote my project.</h2>
      <p class="lead">New construction, a full renovation or an extension — send the basics and I'll tell you what it takes. If you already have plans, we'll quote from them; if you don't, our studio can produce them.</p>
      <ul class="checks">
        <li>New homes, renovations, extensions and pools</li>
        <li>Quotes from your plans or ours</li>
        <li>Fixed-scope contracts with itemized budgets</li>
        <li>Remote owners welcome — weekly photo reports</li>
      </ul>
    </div>
    <div class="rv d1">
      {form("Request a construction quote", "Your answers go straight to my WhatsApp.",
        [("row",[("text","Name","Your name","Jane Smith"),("select","Location","Where",["San Miguel de Allende","Querétaro","Celaya","Elsewhere in the Bajío"])]),
         ("row",[("select","Type","Type of work",["New home","Renovation","Extension","Pool / landscape","Commercial"]),("select","Plans","Do you have plans?",["Yes, complete","Preliminary sketches","No, I need design too"])]),
         ("row",[("select","Size","Approximate size",["Under 2,000 sq ft (185 m²)","2,000 – 3,500 sq ft","3,500 – 5,500 sq ft","Over 5,500 sq ft (510 m²)"]),("select","Start","When would you like to start",["As soon as possible","3–6 months","6–12 months","Just budgeting"])]),
         ("area","Details","Anything else","Finishes level, timeline, site conditions…")],
        "Hi Roberto, I would like a construction quote. Here are my details:", "Send to Roberto on WhatsApp")}
    </div>
  </div>
</section>
""" + contact_band(wa, "Construction", "Questions before quoting?",
        "Send a message — we'll set up a call or a site visit.",
        "Hi Roberto, I would like to talk about a construction project.", "WhatsApp Roberto")
    ld = [{"@context":"https://schema.org","@type":"Service","serviceType":"Residential construction","provider":{"@type":"GeneralContractor","name":"Espacios y Formas · Roberto Balderas Carrillo","url":"https://www.espaciosyformas.com.mx/"},"areaServed":["San Miguel de Allende","Querétaro","Celaya"],"url":f"{SITE}/construction.html"},
          {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"},{"@type":"ListItem","position":2,"name":"Construction","item":f"{SITE}/construction.html"}]}]
    return ("construction",
            "Home Builder in San Miguel de Allende &amp; Querétaro — Construction Quotes | Espacios y Formas · RBC",
            "Turnkey residential construction in San Miguel de Allende, Querétaro and Celaya by architect-builder Roberto Balderas Carrillo (Espacios y Formas). Itemized quotes, own crews, weekly reports for remote owners. Request a construction quote.",
            body, "img/projects-custom-build.jpg", ld, "0.8")

# ───────────────────────────── DEVELOPMENT ─────────────────────────────
def development(wa, SITE):
    body = phero("img/parroquia-view-from-community.jpg", "04 · Development · In progress",
        "Communities we plan, build and finish ourselves.",
        "Our group designs, builds and sells — so developments complete faster and appreciate sooner. Peñas Arriba in San Miguel, Magno Home & Towers in Celaya, and La Escondida coming next.",
        '<a href="index.html">Home</a> › Development') + f"""
<section id="brands">
  <div class="wrap">
    <div class="eyebrow rv">Developments · by brand</div>
    <h2 class="rv d1">Whole communities, designed, built and sold by us.</h2>
    <div class="devs">
      <article class="dev rv" id="penas-arriba">
        <div class="dev-car car h520" data-auto="4200">
          <div class="trk">
            <div class="sl"><img src="img/parroquia-view-from-community.jpg" alt="Peñas Arriba — view of the Parroquia"><div class="scap">Protected views of the Parroquia from every lot</div></div>
            <div class="sl"><img src="img/community-club-pool.jpg" alt="Clubhouse and pool"><div class="scap">Clubhouse &amp; pool terrace — built</div></div>
            <div class="sl"><img src="img/stone-walls-community.jpg" alt="Stone terracing"><div class="scap">Terracing in site stone</div></div>
            <div class="sl"><img src="img/casa-horizonte-sunset-facade.jpg" alt="Casa Horizonte"><div class="scap">Homes designed and built by the same studio</div></div>
            <div class="sl"><img src="img/penas-arriba-map-casa-horizonte.jpg" alt="Master plan of Peñas Arriba"><div class="scap">Master plan — 39 lots on 6 blocks</div></div>
          </div>
          <button class="arr l" aria-label="Previous">‹</button><button class="arr r" aria-label="Next">›</button>
          <div class="dots"></div>
        </div>
        <div class="dev-bd">
          <div class="dev-meta"><span>San Miguel de Allende · Guanajuato</span><span>Selling now</span></div>
          <h3>Peñas Arriba</h3>
          <p>The highest gated community in San Miguel de Allende, with protected views of the Parroquia from every lot and the historic center 7 minutes away. 39 lots on 6 blocks (2,150–12,900 sq ft); streets, stone terracing and amenity buildings built — pool with stone deck, gym, panoramic restaurant, trails, staffed gate and 24/7 shuttle. We design, build and sell the homes: finished residences, shell-built homes with finishes by you, and lots. Homes from US $389K; payment plan 30 / 60 / 10.</p>
          <div class="dev-cta"><a class="btn red" href="https://penasarriba.vercel.app/" target="_blank" rel="noopener">Go to the sales site →</a><a class="btn ghost" href="real-estate.html#san-miguel">Homes for sale here</a><a class="btn ghost" href="{wa('Hi Roberto, I would like to visit Peñas Arriba and see the available lots and homes.')}">Visit</a></div>
        </div>
      </article>

      <article class="dev rv d1" id="magno">
        <div class="dev-car car h520" data-auto="4600">
          <div class="trk">
            <div class="sl"><img src="img/community-club-pool.jpg" alt="Magno Home & Towers"><div class="scap">Provisional image — towers, homes and lots in one community</div></div>
            <div class="sl"><img src="img/community-gym.jpg" alt="Amenities"><div class="scap">Spa, pool, gym, clubhouse, business center</div></div>
            <div class="sl"><img src="img/gated-entrance-luxury-home.jpg" alt="Homes"><div class="scap">Single-family homes and lots</div></div>
          </div>
          <button class="arr l" aria-label="Previous">‹</button><button class="arr r" aria-label="Next">›</button>
          <div class="dots"></div>
        </div>
        <div class="dev-bd">
          <div class="dev-meta"><span>Celaya · Guanajuato</span><span>Immediate delivery</span></div>
          <h3>Magno Home &amp; Towers</h3>
          <p>Celaya's most complete residential development, built by our group: residential towers, single-family homes and lots inside one gated community with spa, pool, gym, clubhouse, business center, bar, multipurpose hall, gardens and underground parking. Apartments available for immediate delivery; lots from MX $2.0M, apartments from MX $4.3M, homes from MX $5.5M.</p>
          <div class="dev-cta"><a class="btn red" href="https://magnoresidencial.com/" target="_blank" rel="noopener">Go to the sales site →</a><a class="btn ghost" href="{wa('Hi Roberto, I would like the current inventory of apartments, homes and lots in Magno, Celaya.')}">Ask for inventory</a></div>
        </div>
      </article>

      <article class="dev rv" id="escondida">
        <div class="dev-car car h520" data-auto="5000">
          <div class="trk">
            <div class="sl"><img src="img/community-trails.jpg" alt="La Escondida"><div class="scap">Provisional image</div></div>
            <div class="sl"><img src="img/valley-golden-hour.jpg" alt="Landscape"><div class="scap">Provisional image</div></div>
          </div>
          <button class="arr l" aria-label="Previous">‹</button><button class="arr r" aria-label="Next">›</button>
          <div class="dots"></div>
        </div>
        <div class="dev-bd">
          <div class="dev-meta"><span>San Miguel de Allende</span><span>Coming next</span></div>
          <h3>La Escondida &amp; La Nueva Escondida</h3>
          <p>Two residential communities in San Miguel de Allende now in development by our group. Early-stage opportunities are shared privately before launch.</p>
          <div class="dev-cta"><a class="btn" href="{wa('Hi Roberto, please keep me informed about La Escondida and La Nueva Escondida in San Miguel.')}">Keep me informed</a></div>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="band" id="amenities">
  <div class="wrap">
    <div class="eyebrow rv">Peñas Arriba · built, not promised</div>
    <h2 class="rv d1">The community today.</h2>
    <div class="car multi h430 rv" data-auto="4300">
      <div class="trk">
        <div class="sl"><img src="img/community-club-pool.jpg" alt="Clubhouse and pool of Peñas Arriba"><div class="scap">Clubhouse &amp; pool terrace</div></div>
        <div class="sl"><img src="img/community-gym.jpg" alt="Gym with garden views"><div class="scap">Gym with garden views</div></div>
        <div class="sl"><img src="img/community-gate.jpg" alt="Main gate"><div class="scap">The staffed main gate</div></div>
        <div class="sl"><img src="img/community-trails.jpg" alt="Landscaped trails"><div class="scap">Trails through native planting</div></div>
        <div class="sl"><img src="img/community-pool-stone.jpg" alt="Pool with natural stone deck"><div class="scap">Pool, natural-stone deck</div></div>
        <div class="sl"><img src="img/stone-walls-community.jpg" alt="Stone terracing"><div class="scap">Terracing in site stone</div></div>
        <div class="sl"><img src="img/view-historic-center.jpg" alt="Historic center seen from the community"><div class="scap">The view from the community</div></div>
      </div>
      <button class="arr l" aria-label="Previous">‹</button><button class="arr r" aria-label="Next">›</button>
      <div class="dots"></div>
    </div>
  </div>
</section>

<section id="invest">
  <div class="wrap">
    <div class="eyebrow rv">Why our developments finish</div>
    <h2 class="rv d1">One studio. Design, build, sell.</h2>
    <div class="steps">
      <div class="step rv"><div class="k">01</div><h4>No empty lots left behind</h4><p>We don't sell lots to sit idle — we build on them. The community fills in, and value rises with it.</p></div>
      <div class="step rv d1"><div class="k">02</div><h4>Architecture that belongs</h4><p>Stone from the hill itself, terraces to the view, a coherent language across every home.</p></div>
      <div class="step rv d2"><div class="k">03</div><h4>Managed after delivery</h4><p>The same team that built it runs it: gate, amenities, maintenance, shuttle.</p></div>
    </div>
    <div class="soon rv" style="margin-top:34px;">
      <h4>Lots, early-stage homes and pre-launch opportunities.</h4>
      <p>Peñas Arriba lots, Magno units and the Escondida communities — ask to be on the list.</p>
      <a class="btn" style="margin-top:16px;" href="{wa('Hi Roberto, please keep me informed about your upcoming developments.')}">Keep me informed</a>
    </div>
  </div>
</section>
""" + contact_band(wa, "Development", "Visit Peñas Arriba.",
        "See the community, the amenities and the available homes and lots — private tour, about an hour.",
        "Hi Roberto, I would like to visit Peñas Arriba.", "WhatsApp Roberto")
    ld = [{"@context":"https://schema.org","@type":"Residence","name":"Peñas Arriba","description":"Gated luxury residential community on the highest hillside of San Miguel de Allende. 39 lots, built amenities, 24/7 security.","url":"https://penasarriba.vercel.app/","address":{"@type":"PostalAddress","addressLocality":"San Miguel de Allende","addressRegion":"Guanajuato","addressCountry":"MX"}},
          {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"},{"@type":"ListItem","position":2,"name":"Development","item":f"{SITE}/development.html"}]}]
    return ("development",
            "Peñas Arriba — Gated Luxury Development in San Miguel de Allende | RBC Developer",
            "Residential developments by architect-developer Roberto Balderas Carrillo. Peñas Arriba: the highest gated community in San Miguel de Allende, 39 lots with protected Parroquia views, built amenities, homes from US $389K. New projects in Querétaro and Celaya in planning.",
            body, "img/parroquia-view-from-community.jpg", ld, "0.8")

# ───────────────────────────── ROBERTO ─────────────────────────────
def roberto(wa, SITE):
    body = phero("img/valley-golden-hour.jpg", "Roberto Balderas Carrillo · Arquitecto",
        "Thirty years building in the Bajío. One person on the other end of the line.",
        "Architect, builder, developer and real estate advisor. Celaya, Querétaro, San Miguel de Allende.",
        '<a href="index.html">Home</a> › Roberto') + f"""
<section id="bio">
  <div class="wrap bio">
    <div class="rv">
      <div class="photo"><img src="img/luxury-home-san-miguel-interior-living.jpg" alt="Roberto Balderas Carrillo — architect, San Miguel de Allende"></div>
      <div class="cap" style="margin-top:8px;">Portrait coming soon — for now, a house instead.</div>
      <div class="kpis">
        <div><div class="n">30</div><div class="l">years</div></div>
        <div><div class="n">2,600</div><div class="l">homes</div></div>
        <div><div class="n">3</div><div class="l">cities</div></div>
      </div>
    </div>
    <div class="rv d1">
      <div class="eyebrow">A short introduction</div>
      <h2>I design houses, I build them, and I sell them myself.</h2>
      <p class="lead">I'm an architect from Celaya, Guanajuato. RBC is my personal studio inside <a href="https://www.espaciosyformas.com.mx/" target="_blank" rel="noopener">Espacios y Formas</a>, the family group that has designed, built and delivered more than 2,600 homes across the Bajío over three decades — residential communities, the Magno towers in Celaya, and custom homes in Celaya, Querétaro and San Miguel de Allende. Some of the projects here are mine alone; others I led through the group; all carry its infrastructure and guarantees.</p>
      <div class="quote">"The best of both worlds: the experience and backing of a large firm, with the craft, care and attention of one architect who answers personally."</div>
      <p class="lead">We do everything: architectural and executive project, engineering, construction, real-estate development, sales and advisory, interior and furniture design, landscaping, maintenance — from small renovations and restorations to luxury homes, country houses, modern apartment buildings, dealerships and commercial centers, as well as mid-income housing. What doesn't change is how: responsibly, with processes that guarantee delivery on time and as promised, without surprises. Today most of my time goes to <a href="development.html">Peñas Arriba</a> above San Miguel, and to clients who want a house designed for their lot — or help finding and evaluating the right property. If you write, I answer personally.</p>
      <div style="margin-top:22px;display:flex;gap:10px;flex-wrap:wrap;">
        <a class="btn red" href="{wa('Hi Roberto, I read your introduction and I would like to talk.')}">WhatsApp Roberto</a>
        <a class="btn ghost" href="https://www.instagram.com/arqrobertobalderas" target="_blank" rel="noopener">@arqrobertobalderas</a>
      </div>
      <p class="cap" style="margin-top:26px;">A fuller story — the studio, the projects, the people — is being written for this page.</p>
    </div>
  </div>
</section>
""" + contact_band(wa, "Let's talk", "Buying, designing, building or investing — start with a message.",
        "English and Spanish spoken. I reply personally.",
        "Hi Roberto, I found your website and I would like to talk.", "WhatsApp Roberto")
    ld = [{"@context":"https://schema.org","@type":"Person","name":"Roberto Balderas Carrillo","jobTitle":"Architect, builder, developer and real estate advisor","url":f"{SITE}/roberto-balderas-carrillo.html","worksFor":{"@type":"Organization","name":"Espacios y Formas","url":"https://www.espaciosyformas.com.mx/"},"sameAs":["https://www.instagram.com/arqrobertobalderas"],"address":{"@type":"PostalAddress","addressLocality":"San Miguel de Allende","addressRegion":"Guanajuato","addressCountry":"MX"}},
          {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"},{"@type":"ListItem","position":2,"name":"Roberto Balderas Carrillo","item":f"{SITE}/roberto-balderas-carrillo.html"}]}]
    return ("roberto-balderas-carrillo",
            "Roberto Balderas Carrillo — Architect, Builder &amp; Developer in San Miguel de Allende, Querétaro and Celaya",
            "Roberto Balderas Carrillo is an architect, builder, developer and real estate advisor in the Bajío region of Mexico. 30 years, 2,600+ homes, one point of contact — from design to keys.",
            body, "img/valley-golden-hour.jpg", ld, "0.6")

# ───────────────────────────── CONTACT ─────────────────────────────
def contact(wa, SITE):
    body = phero("img/sunset-terrace-luxury-villa-mexico.jpg", "Contact",
        "Let's talk.",
        "Buying, designing, building or investing — one message and you're talking to the architect. English and Spanish spoken.",
        '<a href="index.html">Home</a> › Contact') + f"""
<section id="ways">
  <div class="wrap split" style="align-items:start;">
    <div class="rv">
      <div class="eyebrow">Direct line</div>
      <h2>Roberto Balderas Carrillo</h2>
      <p class="lead">Architect · Builder · Developer · Real Estate Advisor<br>Celaya · Querétaro · San Miguel de Allende, México</p>
      <div style="margin-top:20px;display:grid;gap:10px;max-width:420px;">
        <a class="btn red" href="{wa('Hi Roberto, I found your website and I would like to talk.')}">WhatsApp Roberto</a>
        <a class="btn ghost" href="https://www.instagram.com/arqrobertobalderas" target="_blank" rel="noopener">Instagram @arqrobertobalderas</a>
        <a class="btn ghost" href="https://www.espaciosyformas.com.mx/" target="_blank" rel="noopener">Espacios y Formas — construction firm</a>
        <a class="btn ghost" href="https://penasarriba.vercel.app/" target="_blank" rel="noopener">Peñas Arriba — development site</a>
      </div>
      <ul class="checks" style="margin-top:26px;">
        <li>Private showings in San Miguel de Allende, by appointment</li>
        <li>Video calls for buyers abroad — US and Canadian time zones welcome</li>
        <li>Replies personally, usually the same day</li>
      </ul>
    </div>
    <div class="rv d1">
      {form("Send a message", "Tell me what you have in mind — it goes straight to my WhatsApp.",
        [("row",[("text","Name","Your name","Jane Smith"),("select","Interest","I'm interested in",["Buying a home","Designing a home","Building / a construction quote","A development / investment","Something else"])]),
         ("row",[("select","City","City",["San Miguel de Allende","Querétaro","Celaya","Other"]),("text","Contact","Best way to reach you","Phone or email")]),
         ("area","Message","Message","")],
        "Hi Roberto, I'm writing from your website:", "Send to Roberto on WhatsApp")}
    </div>
  </div>
</section>
"""
    ld = [{"@context":"https://schema.org","@type":"ContactPage","url":f"{SITE}/contact.html","name":"Contact Roberto Balderas Carrillo"},
          {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"},{"@type":"ListItem","position":2,"name":"Contact","item":f"{SITE}/contact.html"}]}]
    return ("contact",
            "Contact — Roberto Balderas Carrillo, Architect &amp; Real Estate | San Miguel de Allende",
            "Contact architect, builder and real estate advisor Roberto Balderas Carrillo. WhatsApp +52 461 101 2474. Private showings in San Miguel de Allende, design and construction quotes in Querétaro and Celaya.",
            body, "img/sunset-terrace-luxury-villa-mexico.jpg", ld, "0.5")

def build(page, wa, ORG, SITE):
    urls = []
    for fn in (home, real_estate, casa_horizonte, architecture, construction, development, roberto, contact):
        slug, title, desc, body, og, ld, pr = fn(wa, SITE)
        if ld == "org":
            ld = [ORG]
        u = page(slug, title, desc, body, og, ld, active=(slug + ".html"))
        urls.append((u, pr))
    for l in listings.pages():
        slug, title, desc, body, og, ld, pr = listings.property_page(l, wa, SITE)
        u = page(slug, title, desc, body, og, ld, active="real-estate.html")
        urls.append((u, pr))
    urls.append((f"{SITE}/privacy.html", "0.2"))
    urls.append((f"{SITE}/terms.html", "0.2"))
    return urls
