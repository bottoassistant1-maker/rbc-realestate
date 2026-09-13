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
