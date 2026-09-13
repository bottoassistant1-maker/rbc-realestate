# -*- coding: utf-8 -*-
"""v17: full sheets for the developments (Peñas Arriba, Magno)."""
import pages as P
import listings, fichas
from pages_v12 import shead

DEVS = [
  dict(slug="penas-arriba", name="Peñas Arriba", logo="img/penas-arriba-logo.png", logo_dark=False,
       place="San Miguel de Allende · Guanajuato", role="RBC with Espacios y Formas", status="Houses, shell-built homes and lots",
       hero="img/ig-DceaktFmAgJ-1.jpg",
       intro="A gated community on the hillside above San Miguel de Allende, with views of the Parroquia and the valley. Roberto designs the houses; larger works are built with Espacios y Formas.",
       facts=[("Houses","designed by RBC"),("Shell-built","homes"),("Lots","in the community"),("Gated","hillside community")],
       photos=["img/ig-DceaktFmAgJ-1.jpg","img/ig-DceaktFmAgJ-3.jpg","img/ph-penas-obra-b-06.jpg","img/ig-DceaktFmAgJ-4.jpg","img/ph-penas-obra-b-07.jpg","img/ig-DceaktFmAgJ-5.jpg","img/penas-arriba-map-casa-horizonte.jpg"],
       site="https://penasarriba.vercel.app/", site_label="Community site →",
       msg="Hi Roberto, I would like information about houses and lots in Peñas Arriba, San Miguel de Allende.",
       houses=lambda l: l["kind"] == "sale" and "Peñas Arriba" in l["where"]),
  dict(slug="magno", name="Magno Home &amp; Towers", logo="img/magno-logo-white.png", logo_dark=True,
       place="Celaya · Guanajuato", role="Espacios y Formas", status="Apartments, homes and lots",
       hero="img/magno-4.jpg",
       intro="Residential towers, single-family homes and lots in one gated community in Celaya, with spa, pool, gym and clubhouse. Apartments available for immediate delivery.",
       facts=[("Towers","apartments, immediate delivery"),("Homes","single-family"),("Lots","from MX $2.0M"),("Amenities","spa · pool · gym · clubhouse")],
       photos=["img/magno-4.jpg","img/magno-2.jpg","img/magno-5.jpg","img/magno-8.jpg","img/magno-1.jpg","img/magno-3.jpg","img/magno-6.jpg","img/magno-7.jpg"],
       site="https://magnoresidencial.com/", site_label="Sales site →",
       msg="Hi Roberto, I would like the current inventory of apartments, homes and lots in Magno, Celaya.",
       houses=lambda l: False),
]

def dev_page(d, wa, SITE):
    facts = "".join(f'<div><div class="n">{a}</div><div class="l">{b}</div></div>' for a, b in d["facts"])
    tiles = "".join(f'<a class="lbx cg" href="{x}"><img src="{x}" alt="{d["name"]}" loading="lazy"></a>' for x in d["photos"])
    hs = [l for l in listings.L if d["houses"](l)]
    houses = f"""
<section id="houses"><div class="wrap">
  {shead("02","Available in " + d["name"])}
  {fichas.grid(hs, wa)}
</div></section>""" if hs else ""
    body = f"""
<header class="hero prop dev-hero" id="top">
  <div class="bg" style="background-image:url('{d['hero']}')"></div>
  <div class="in">
    <div class="crumbs"><a href="index.html">Home</a> › <a href="real-estate.html">Real Estate</a> › <a href="real-estate.html#developments">Developments</a></div>
    <div class="tag">Development · {d['place']}</div>
    <img class="dev-logo{' white' if d['logo_dark'] else ''}" src="{d['logo']}" alt="{d['name']}">
    <h1 class="sr">{d['name']}</h1>
    <p class="sub">{d['intro']}</p>
  </div>
</header>
<div class="pp-bar"><div class="in">
  <div class="pp-price" style="font-size:1.1rem;">{d['status']}</div>
  <div class="pp-auth"><small>Developed by</small>{d['role']}</div>
  <div class="pp-auth"><small>Where</small>{d['place']}</div>
  <a class="btn red" href="{wa(d['msg'])}">Request information</a>
  <a class="btn ghost" href="{d['site']}" target="_blank" rel="noopener">{d['site_label']}</a>
</div></div>
<div class="stats"><div class="in">{facts}</div></div>
<section id="photos"><div class="wrap">
  {shead("01","The development")}
  <div class="pgrid">{tiles}</div>
</div></section>
{houses}
""" + P.contact_band(wa, "Contact", "Ask Roberto about " + d["name"].replace("&amp;", "&") + ".", "Availability, prices and plans, answered directly.", d["msg"], "WhatsApp Roberto") + fichas.modal_data(listings.L, wa)
    ld = [{"@context":"https://schema.org","@type":"Place","name":d["name"].replace("&amp;","&"),"address":d["place"],"url":f"{SITE}/{d['slug']}.html"}]
    return (d["slug"], f"{d['name'].replace('&amp;','&')} — {d['place']} | RBC · Roberto Balderas Carrillo",
            d["intro"], body, d["hero"], ld, "0.8")

CSS = r"""
.dev-hero .in .dev-logo{display:block;max-width:300px;max-height:110px;object-fit:contain;margin:14px 0 10px;filter:brightness(0) invert(1);}
.dev-hero h1.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);}
.dev-hero .sub{max-width:620px;}
.dev-hero .in .dev-logo.white{filter:none;}
.pp-bar .btn.ghost{margin-left:8px;}
"""

# ── medium development cards for the Real Estate page (v17) ──
CARDS = [
  dict(id="magno-homes", logo="img/magno-logo-white.png", dark=True, name="Magno Homes", place="Celaya · Guanajuato", status="Single-family homes and lots",
       imgs=["img/magno-4.jpg","img/magno-8.jpg","img/magno-2.jpg","img/magno-5.jpg"], sheet="magno.html", web="https://magnoresidencial.com/", ig="", fb=""),
  dict(id="magno-towers", logo="img/magno-logo-white.png", dark=True, name="Magno Towers", place="Celaya · Guanajuato", status="Apartments · immediate delivery",
       imgs=["img/magno-1.jpg","img/magno-3.jpg","img/magno-6.jpg","img/magno-7.jpg"], sheet="magno.html", web="https://magnoresidencial.com/", ig="", fb=""),
  dict(id="penas-arriba", logo="img/penas-arriba-logo.png", dark=False, name="Peñas Arriba", place="San Miguel de Allende", status="Houses, shell-built homes and lots",
       imgs=["img/ig-DceaktFmAgJ-1.jpg","img/ig-DceaktFmAgJ-3.jpg","img/penas-arriba-map-casa-horizonte.jpg","img/ph-penas-obra-b-06.jpg"], sheet="penas-arriba.html", web="https://penasarriba.vercel.app/", ig="https://instagram.com/penasarribasma", fb=""),
  dict(id="escondida", logo="", dark=False, name="La Escondida", place="San Miguel de Allende", status="In development · details to follow",
       imgs=[], sheet="", web="", ig="", fb=""),
  dict(id="nueva-escondida", logo="", dark=False, name="La Nueva Escondida", place="San Miguel de Allende", status="In development · details to follow",
       imgs=[], sheet="", web="", ig="", fb=""),
]

def dev_md(c, wa):
    sl = "".join(f'<div class="sl"><img src="{i}" alt="{c["name"]}" loading="lazy"></div>' for i in c["imgs"])
    brand = f'<img src="{c["logo"]}" alt="{c["name"]}" class="{"white" if c["dark"] else ""}">' if c["logo"] else f'<b>{c["name"]}</b>'
    links = ""
    if c["sheet"]: links += f'<a href="{c["sheet"]}">Sheet →</a>'
    if c["web"]: links += f'<a href="{c["web"]}" target="_blank" rel="noopener">Website</a>'
    if c["ig"]: links += f'<a href="{c["ig"]}" target="_blank" rel="noopener">Instagram</a>'
    if c["fb"]: links += f'<a href="{c["fb"]}" target="_blank" rel="noopener">Facebook</a>'
    if not links: links = f'<a href="{wa("Hi Roberto, please keep me informed about " + c["name"] + " in San Miguel de Allende.")}">Keep me informed</a>'
    multi = len(c["imgs"]) > 1
    arrows = '<button class="arr l" aria-label="Previous">‹</button><button class="arr r" aria-label="Next">›</button>' if multi else ""
    if not c["imgs"]:
        car = '<div class="dm-car pend"><span>Renders and master plan pending</span></div>'
    else:
        car = f'<div class="car dm-car" data-auto="4800"><div class="trk">{sl}</div>{arrows}<div class="dots"></div></div>' if multi else f'<div class="dm-car one"><img src="{c["imgs"][0]}" alt="{c["name"]}" loading="lazy"></div>'
    return f"""
      <article class="dm rv" id="{c['id']}">
        {car}
        <div class="dm-bd">
          <div class="dm-brand{' dark' if c['dark'] else ''}">{brand}</div>
          <div class="dm-tx"><b>{c['name']}</b><span>{c['place']} · {c['status']}</span><div class="dm-links">{links}</div></div>
        </div>
      </article>"""

def dev_cards(wa):
    return '<div class="dms">' + "".join(dev_md(c, wa) for c in CARDS) + '</div>'

CSS += r"""
.dms{display:grid;grid-template-columns:repeat(2,1fr);gap:28px 24px;margin-top:8px;}
@media(max-width:800px){.dms{grid-template-columns:1fr;}}
.dm .dm-car{height:300px;overflow:hidden;background:var(--paper-2);}
.dm .dm-car.pend{display:flex;align-items:flex-end;padding:16px;border:1px solid var(--line);} .dm .dm-car.pend span{font-size:.62rem;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-soft);}
.dm .dm-car.one img{width:100%;height:100%;object-fit:cover;display:block;}
.dm .car .trk{height:100%;padding-bottom:0;gap:0;} .dm .car .sl{height:100%;border-radius:0;} .dm .car .sl img{width:100%;height:100%;object-fit:cover;}
.dm .car .dots{position:absolute;bottom:10px;left:0;right:0;margin:0;}
.dm .car .arr{opacity:0;transition:opacity .25s;} .dm:hover .car .arr{opacity:1;}
@media(max-width:800px){.dm .dm-car{height:230px;}}
.dm-bd{display:grid;grid-template-columns:120px 1fr;gap:18px;align-items:center;padding:14px 0 0;}
.dm-brand{height:56px;display:flex;align-items:center;justify-content:center;padding:6px 10px;background:#fff;border:1px solid var(--line);}
.dm-brand.dark{background:none;border:none;padding:0;justify-content:flex-start;}
.dm-brand img{max-width:100%;max-height:100%;object-fit:contain;display:block;}
.dm-brand b{font-family:var(--sans);font-weight:500;font-size:.8rem;letter-spacing:.02em;color:var(--navy);text-align:center;line-height:1.15;}
.dm-tx b{display:block;font-family:var(--sans);font-weight:500;font-size:1.15rem;letter-spacing:-.01em;color:#161616;}
.dm-tx>span{display:block;font-size:.66rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-soft);margin-top:3px;}
.dm-links{display:flex;flex-wrap:wrap;gap:4px 16px;margin-top:8px;}
.dm-links a{font-size:.66rem;letter-spacing:.1em;text-transform:uppercase;color:var(--navy);text-decoration:none;border-bottom:1px solid var(--c-re);padding-bottom:1px;}
.dm-links a:hover{color:var(--c-arch);border-color:var(--c-arch);}
"""
