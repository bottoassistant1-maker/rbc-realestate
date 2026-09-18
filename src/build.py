#!/usr/bin/env python3
"""Build RBC site: shared nav/footer + per-page content -> ../site/*.html
Change SITE_URL once to move the whole site to a new domain."""
import os, re, json, datetime, importlib, sys
import design
import projects
import projects_v13
import fichas

SITE_URL = os.environ.get("SITE_URL", "https://rbc-realestate.vercel.app")
OUT = os.path.join(os.path.dirname(__file__), "..")
WA = "https://wa.me/524611012474"
TODAY = datetime.date.today().isoformat()

def wa(msg):
    from urllib.parse import quote
    return f"{WA}?text={quote(msg)}"

NAV_ITEMS = [
    ("architecture.html", "Architecture &amp; Design"),
    ("real-estate.html", "Real Estate"),
    ("construction.html", "Construction"),
]
SEC_ITEMS = []

EXTRA_CSS = """
/* ── multi-page nav ── */
nav .links a.on{color:var(--navy);border-bottom:2px solid var(--gold);padding-bottom:2px;}
nav .links a.sec{font-weight:500;text-transform:none;letter-spacing:.04em;font-size:.82rem;color:var(--ink-soft);}
nav .links .sep{width:1px;height:18px;background:var(--line);display:inline-block;}
@media(max-width:860px){nav .links .sep{display:none;}}
.mnav a.msec{font-family:'Figtree',sans-serif;font-size:1rem;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.75);border-bottom:none;padding:8px 0;}
nav .burger{display:none;background:none;border:1.5px solid var(--navy);border-radius:3px;color:var(--navy);width:40px;height:36px;font-size:1.2rem;cursor:pointer;}
@media(max-width:860px){nav .burger{display:inline-flex;align-items:center;justify-content:center;}}
.mnav{position:fixed;inset:0;z-index:120;background:var(--navy-deep);color:#fff;display:none;flex-direction:column;padding:26px 22px;}
.mnav.on{display:flex;}
.mnav .top{display:flex;justify-content:space-between;align-items:center;margin-bottom:26px;}
.mnav .top img{height:34px;filter:brightness(0) invert(1);}
.mnav .x{background:none;border:none;color:#fff;font-size:2rem;cursor:pointer;}
.mnav a{color:#fff;text-decoration:none;font-family:'Fraunces',serif;font-size:1.7rem;padding:12px 0;border-bottom:1px solid rgba(255,255,255,.12);}
.mnav a small{display:block;font-family:'Figtree',sans-serif;font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);margin-bottom:2px;}
.mnav .btn{margin-top:auto;text-align:center;}
/* ── home hero ── */
.hero.home{min-height:92vh;align-items:center;}
.hero.home .in{padding-bottom:80px;padding-top:120px;}
.hero.home h1{max-width:860px;}
.roles{display:flex;gap:10px;flex-wrap:wrap;margin:22px 0 6px;}
.roles span{border:1px solid rgba(255,255,255,.55);color:#fff;font-size:.7rem;letter-spacing:.2em;text-transform:uppercase;padding:8px 14px;border-radius:3px;font-weight:600;background:rgba(22,30,69,.35);backdrop-filter:blur(4px);}
.roles span b{color:var(--gold);margin-right:8px;}
/* ── pillars ── */
.pillars{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:30px;}
@media(max-width:1000px){.pillars{grid-template-columns:repeat(2,1fr);}}
@media(max-width:600px){.pillars{grid-template-columns:1fr;}}
.pillar{position:relative;display:block;text-decoration:none;color:#fff;border-radius:8px;overflow:hidden;min-height:400px;box-shadow:0 20px 50px -28px rgba(26,35,80,.5);}
.pillar img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform .7s;}
.pillar:hover img{transform:scale(1.06);}
.pillar::after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(22,30,69,.1) 0%,rgba(22,30,69,.35) 45%,rgba(22,30,69,.94) 100%);}
.pillar .t{position:absolute;left:0;right:0;bottom:0;padding:22px;z-index:2;}
.pillar .num{font-family:'Fraunces',serif;color:var(--gold);font-size:.95rem;letter-spacing:.2em;}
.pillar h3{color:#fff;font-size:1.5rem;margin:6px 0 6px;line-height:1.1;}
.pillar p{font-size:.86rem;color:rgba(255,255,255,.82);line-height:1.5;}
.pillar .go{display:inline-block;margin-top:12px;font-size:.7rem;letter-spacing:.2em;text-transform:uppercase;font-weight:700;color:var(--gold);}
/* ── page hero (interior) ── */
.phero{position:relative;min-height:62vh;display:flex;align-items:flex-end;overflow:hidden;background:var(--navy-deep);}
.phero .bg{position:absolute;inset:0;background-size:cover;background-position:center;}
.phero::after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(22,30,69,.45) 0%,rgba(22,30,69,.15) 40%,rgba(22,30,69,.88) 100%);}
.phero .in{position:relative;z-index:2;width:100%;max-width:1120px;margin:0 auto;padding:130px 22px 54px;color:#fff;}
.phero .tag{font-size:.72rem;letter-spacing:.32em;text-transform:uppercase;color:var(--gold);font-weight:700;}
.phero h1{color:#fff;font-size:clamp(2.2rem,5vw,3.8rem);line-height:1.05;margin:12px 0 10px;max-width:820px;}
.phero p.sub{font-size:1.05rem;max-width:640px;color:rgba(255,255,255,.9);font-weight:300;}
.crumbs{font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:rgba(255,255,255,.7);margin-bottom:14px;}
.crumbs a{color:var(--gold);text-decoration:none;}
/* ── city tabs / catalog ── */
.cities{display:flex;gap:10px;flex-wrap:wrap;margin-top:22px;}
.cities a{text-decoration:none;font-size:.74rem;letter-spacing:.18em;text-transform:uppercase;font-weight:700;padding:10px 18px;border:1.5px solid var(--navy);border-radius:3px;color:var(--navy);}
.cities a.on,.cities a:hover{background:var(--navy);color:#fff;}
.cityhead{display:flex;align-items:baseline;gap:16px;flex-wrap:wrap;margin-top:54px;border-bottom:1px solid var(--line);padding-bottom:10px;}
.cityhead h3{font-size:1.8rem;}
.cityhead .cnt{font-size:.74rem;letter-spacing:.18em;text-transform:uppercase;color:var(--ink-soft);}
.lcard.feat{grid-column:1/-1;flex-direction:row;}
.lcard.feat .im{height:auto;flex:1.3;min-height:340px;}
.lcard.feat .bd{flex:1;padding:34px;}
@media(max-width:900px){.lcard.feat{flex-direction:column;}.lcard.feat .im{min-height:240px;}}
.soon{background:#fff;border:1px dashed var(--line);border-radius:8px;padding:34px;text-align:center;color:var(--ink-soft);}
.soon h4{font-family:'Fraunces',serif;font-weight:400;color:var(--navy);font-size:1.3rem;margin-bottom:8px;}
/* ── services / steps ── */
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:30px;}
@media(max-width:860px){.steps{grid-template-columns:1fr;}}
.step{background:#fff;border:1px solid var(--line);border-radius:8px;padding:26px;border-top:3px solid var(--gold);}
.step .k{font-family:'Fraunces',serif;font-size:2rem;color:var(--red);line-height:1;}
.step h4{font-family:'Fraunces',serif;font-weight:400;color:var(--navy);font-size:1.2rem;margin:10px 0 6px;}
.step p{font-size:.9rem;color:var(--ink-soft);}
/* ── project grid ── */
.pgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:26px;}
@media(max-width:900px){.pgrid{grid-template-columns:1fr 1fr;}}
@media(max-width:600px){.pgrid{grid-template-columns:1fr;}}
.pj{position:relative;display:block;border-radius:6px;overflow:hidden;height:300px;}
.pj img{width:100%;height:100%;object-fit:cover;transition:transform .6s;}
.pj:hover img{transform:scale(1.05);}
.pj .pc{position:absolute;left:0;right:0;bottom:0;background:linear-gradient(180deg,transparent,rgba(22,30,69,.9));color:#fff;padding:36px 16px 14px;}
.pj .pc b{display:block;font-family:'Fraunces',serif;font-weight:400;font-size:1.15rem;}
.pj .pc span{font-size:.7rem;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);}
/* ── form ── */
.form{background:#fff;border:1px solid var(--line);border-radius:8px;padding:34px;box-shadow:0 18px 45px -25px rgba(26,35,80,.3);}
.form .row{display:grid;grid-template-columns:1fr 1fr;gap:14px;}
@media(max-width:700px){.form .row{grid-template-columns:1fr;}}
.form label{display:block;font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:var(--ink-soft);font-weight:700;margin:12px 0 6px;}
.form input,.form select,.form textarea{width:100%;font-family:'Figtree',sans-serif;font-size:.95rem;padding:12px 14px;border:1px solid var(--line);border-radius:4px;background:var(--paper);color:var(--ink);}
.form input:focus,.form select:focus,.form textarea:focus{outline:2px solid var(--gold);border-color:var(--gold);}
.form textarea{min-height:110px;resize:vertical;}
.form .btn{width:100%;text-align:center;margin-top:18px;border:none;cursor:pointer;font-family:'Figtree',sans-serif;}
.form .note{font-size:.76rem;color:var(--ink-soft);margin-top:10px;text-align:center;}
/* ── about page ── */
.bio{display:grid;grid-template-columns:1fr 1.4fr;gap:44px;align-items:start;}
@media(max-width:860px){.bio{grid-template-columns:1fr;}}
.bio .photo{border-radius:8px;overflow:hidden;box-shadow:0 22px 55px -22px rgba(26,35,80,.45);}
.bio .photo img{width:100%;height:520px;object-fit:cover;}
.quote{font-family:'Fraunces',serif;font-size:1.5rem;line-height:1.35;color:var(--navy);border-left:3px solid var(--gold);padding-left:20px;margin:22px 0;}
.kpis{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:22px;}
.kpis div{background:#fff;border:1px solid var(--line);border-radius:6px;padding:16px;text-align:center;}
.kpis .n{font-family:'Fraunces',serif;font-size:1.8rem;color:var(--red);line-height:1;}
.kpis .l{font-size:.64rem;letter-spacing:.16em;text-transform:uppercase;color:var(--ink-soft);margin-top:6px;}
"""

def nav(active):
    ON = ' class="on"'
    DISC = ["d-arch", "d-re", "d-con"]
    links = "".join(
        f'<a href="{h}" class="{DISC[i]}{" on" if h == active else ""}">{t}</a>' for i, (h, t) in enumerate(NAV_ITEMS)
    )
    sec = "".join(f'<a class="sec" href="{h}"{ON if h == active else ""}>{t}</a>' for h, t in SEC_ITEMS)
    m = "".join(
        f'<a href="{h}" class="{DISC[i]}"><small>0{i+1}</small>{t}</a>' for i, (h, t) in enumerate(NAV_ITEMS)
    ) + "".join(f'<a class="msec" href="{h}">{t}</a>' for h, t in SEC_ITEMS)
    return f"""
<nav>
  <div class="in">
    <a class="brand" href="index.html"><img src="img/rbc-mono.png" alt="RBC"><span class="who"><b>Roberto Balderas Carrillo</b><span>Arquitecto</span></span></a>
    <div class="links">
      {links}
      <a class="lang" href="#" title="Versión en español — próximamente"><b>EN</b> / ES</a>
      <a class="cta" href="{wa("Hi Roberto, I found your website and I'd like to talk.")}">WhatsApp</a>
      <button class="burger" aria-label="Menu" onclick="document.getElementById('mnav').classList.add('on')">☰</button>
    </div>
  </div>
</nav>
<div class="mnav" id="mnav">
  <div class="top"><img src="img/rbc-mono.png" alt="RBC"><button class="x" aria-label="Close" onclick="document.getElementById('mnav').classList.remove('on')">×</button></div>
  <a href="index.html"><small>00</small>Home</a>
  {m}
  <a class="msec" href="contact.html">Contact</a>
  <a class="msec" href="https://www.instagram.com/arqrobertobalderas" target="_blank" rel="noopener">Instagram</a>
  <a class="btn red" href="{wa("Hi Roberto, I found your website and I'd like to talk.")}">WhatsApp Roberto</a>
</div>
"""

FOOTER = f"""
<footer>
  <div class="in">
    <div class="cols">
      <div><div class="seal"><img src="img/rbc-mono-white.png" alt="RBC" style="height:46px;display:block;margin-bottom:12px;"><span>Roberto Balderas Carrillo · Arquitecto</span></div><p style="margin-top:14px;">Architecture, construction and selected properties.<br>San Miguel de Allende · Bajío · México.<br>In collaboration with <a href="https://www.espaciosyformas.com.mx/" target="_blank" rel="noopener" style="display:inline;padding:0;">Espacios y Formas</a>.</p></div>
      <div><small>Site</small><a href="architecture.html">Architecture &amp; Design</a><a href="real-estate.html">Real Estate</a><a href="real-estate.html#developments">Developments</a><a href="construction.html">Construction</a><a href="contact.html">Contact</a></div>
      <div><small>Start</small><a href="contact.html#project">Start a project</a><a href="contact.html#buy">Buy a property</a><a href="contact.html#sell">Sell a property</a><a href="contact.html#general">General inquiry</a></div>
      <div><small>Direct</small><a href="{wa("Hi Roberto, I found your website and I'd like to talk.")}">WhatsApp Roberto</a><button class="tel-reveal" data-t="KzUyIDQ2MSAxMDEgMjQ3NA==">Show phone number</button><a href="https://www.instagram.com/arqrobertobalderas" target="_blank" rel="noopener">@arqrobertobalderas</a><a href="https://www.espaciosyformas.com.mx/" target="_blank" rel="noopener">espaciosyformas.com.mx</a><a href="privacy.html">Privacy notice</a><a href="terms.html">Terms</a></div>
    </div>
    <div class="row">
      <div>© 2026 RBC · Roberto Balderas Carrillo, Arquitecto</div>
      <div class="code">Offices · San Miguel de Allende / Celaya</div>
    </div>
    <div class="fine">Prices in MXN; USD figures are approximate references. Images may be renders or provisional; specifications, availability and delivery subject to change. This site does not constitute a binding offer.</div>
  </div>
</footer>
<a class="wa-float" href="{wa("Hi Roberto, I found your website and I'd like to talk.")}">WhatsApp</a>
<div class="lb" id="lb"><button class="x" aria-label="Close">×</button><img id="lbimg" src="" alt=""></div>
"""

JS = r"""
<script>
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target);}}),{threshold:.14});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));
document.querySelectorAll('.car').forEach(car=>{
  const trk=car.querySelector('.trk'), sls=[...car.querySelectorAll('.sl')], dots=car.querySelector('.dots');
  const multi=car.classList.contains('multi');
  sls.forEach((_,i)=>{const d=document.createElement('i');d.addEventListener('click',()=>go(i));dots.appendChild(d);});
  const ds=[...dots.children];
  function idx(){const w=sls[0].getBoundingClientRect().width+14;return Math.round(trk.scrollLeft/w);}
  function paint(){const i=idx();ds.forEach((d,k)=>d.classList.toggle('on',k===Math.min(i,ds.length-1)));}
  function go(i){const w=sls[0].getBoundingClientRect().width+14;trk.scrollTo({left:i*w,behavior:'smooth'});}
  car.querySelector('.arr.l').addEventListener('click',()=>go(Math.max(0,idx()-1)));
  car.querySelector('.arr.r').addEventListener('click',()=>go((idx()+1)%sls.length));
  trk.addEventListener('scroll',()=>requestAnimationFrame(paint));
  let t=setInterval(auto,parseInt(car.dataset.auto||5000));
  function auto(){const max=sls.length-1;const i=idx();go(i>=max?0:i+1);}
  car.addEventListener('pointerenter',()=>clearInterval(t));
  car.addEventListener('pointerleave',()=>{clearInterval(t);t=setInterval(auto,parseInt(car.dataset.auto||5000));});
  paint();
});
const nv=document.querySelector('nav');
addEventListener('scroll',()=>nv.classList.toggle('scrolled',scrollY>40),{passive:true});
const hbg=document.querySelector('.hero .bg');
if(hbg)addEventListener('scroll',()=>{if(scrollY<innerHeight)hbg.style.transform='translateY('+scrollY*.25+'px) scale(1.04)';},{passive:true});
const fmt=n=>n.toLocaleString('en-US');
const cio=new IntersectionObserver(es=>es.forEach(e=>{
  if(!e.isIntersecting)return;cio.unobserve(e.target);
  const el=e.target,raw=el.textContent.trim();const num=parseInt(raw.replace(/,/g,''));
  if(isNaN(num)||num<10)return;const t0=performance.now(),dur=1400;
  (function tick(t){const p=Math.min(1,(t-t0)/dur);el.textContent=fmt(Math.round(num*(1-Math.pow(1-p,3))));if(p<1)requestAnimationFrame(tick);})(t0);
}),{threshold:.6});
document.querySelectorAll('.stats .n, .kpis .n').forEach(el=>cio.observe(el));
const lb=document.getElementById('lb'), lbimg=document.getElementById('lbimg');
document.querySelectorAll('a.lbx').forEach(a=>a.addEventListener('click',e=>{e.preventDefault();lbimg.src=a.href;lb.classList.add('on');}));
if(lb)lb.addEventListener('click',()=>lb.classList.remove('on'));
// WhatsApp forms: compose a message from the fields and open WhatsApp
document.querySelectorAll('form[data-wa]').forEach(f=>f.addEventListener('submit',e=>{
  e.preventDefault();const d=new FormData(f);let msg=f.dataset.wa+'\n';
  for(const [k,v] of d.entries()){if(v)msg+='\n'+k+': '+v;}
  window.open('https://wa.me/524611012474?text='+encodeURIComponent(msg),'_blank');
}));
</script>
"""

PGC = {"architecture.html":"pg-arch","real-estate.html":"pg-re","construction.html":"pg-con"}
def page(slug, title, desc, body, og_image, jsonld=None, active=None, extra_head=""):
    url = f"{SITE_URL}/" if slug == "index" else f"{SITE_URL}/{slug}.html"
    og = og_image if og_image.startswith("http") else f"{SITE_URL}/{og_image}"
    ld = "".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>\n' for j in (jsonld or []))
    css = open(os.path.join(os.path.dirname(__file__), "base.css"), encoding="utf-8").read()
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="icon" type="image/png" href="img/favicon.png">
<link rel="alternate" hreflang="en" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="RBC · Roberto Balderas Carrillo, Arquitecto">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{og}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:image" content="{og}">
{extra_head}
{ld}<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<style>{css}{EXTRA_CSS}{design.CSS}{projects.CSS}{projects_v13.CSS}{fichas.CSS}{devpages.CSS}{legal.CSS}</style>
</head>
<body class="{PGC.get(active,'')}">
{nav(active)}
{body}
{FOOTER}
{fichas.MODAL_HTML}
{JS}
{design.JS}
{projects.JS}
{projects_v13.JS}
{fichas.JS}
{fichas.JS_CITY}
{legal.COOKIE}
</body>
</html>
"""
    with open(os.path.join(OUT, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(html)
    return url

ORG = {"@context":"https://schema.org","@type":["ProfessionalService","Organization"],
  "name":"RBC · Roberto Balderas Carrillo, Arquitecto","url":SITE_URL + "/",
  "logo":SITE_URL + "/img/rbc-logo.png",
  "description":"Architecture practice of Roberto Balderas Carrillo in San Miguel de Allende: architectural design, interiors, construction and a selection of properties presented with an architect's perspective. In collaboration with Espacios y Formas.",
  "knowsAbout":["Architecture","Residential architecture","Interior design","Construction","Real estate"],
  "sameAs":["https://www.instagram.com/arqrobertobalderas","https://www.espaciosyformas.com.mx/","https://penasarriba.vercel.app/"],
  "areaServed":[{"@type":"City","name":"San Miguel de Allende"},{"@type":"AdministrativeArea","name":"Bajío"},{"@type":"Country","name":"Mexico"}],
  "founder":{"@type":"Person","name":"Roberto Balderas Carrillo","jobTitle":"Architect"},
  "address":{"@type":"PostalAddress","addressLocality":"San Miguel de Allende","addressRegion":"Guanajuato","addressCountry":"MX"}}

if __name__ == "__main__":
    import pages_v15, devpages, legal
    urls = pages_v15.build(page, wa, ORG, SITE_URL)
    legal.pages(page, SITE_URL)
    # sitemap + robots
    sm = ['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, pr in urls:
        sm.append(f'  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod><changefreq>weekly</changefreq><priority>{pr}</priority></url>')
    sm.append('</urlset>')
    open(os.path.join(OUT,"sitemap.xml"),"w").write("\n".join(sm)+"\n")
    open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
    print("built", len(urls), "pages ->", SITE_URL)
    if "--pdf" in sys.argv:
        import listings
        fichas.build_pdfs(listings.L, OUT, OUT, SITE_URL)
