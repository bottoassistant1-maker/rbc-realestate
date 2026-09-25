# -*- coding: utf-8 -*-
"""v13: standardized project reels (title + place only) for Architecture and Construction."""
from projects import PROJECTS, types, code, CSS as _CSS, JS as _JS

def _ph(p):
    return p.get("photos") or [p["img"]]

def reel_card(p, size=""):
    ph = _ph(p)
    slides = "".join(f'<img src="{x}" alt="{p["name"]} — {p["place"]}" loading="lazy">' for x in ph)
    dots = "".join('<i></i>' for _ in ph) if len(ph) > 1 else ""
    arrows = '<button class="fs-arr l" aria-label="Previous">‹</button><button class="fs-arr r" aria-label="Next">›</button>' if len(ph) > 1 else ""
    sheet = ""
    return f"""
      <article class="reel rv {size}" data-types="{' '.join(types(p))}" data-cat="{cat_of(p['slug'])}" data-proj="{p['slug']}" tabindex="0" role="button" aria-label="Open {p['name']}">
        <div class="fs-slider reel-sl" data-n="{len(ph)}"><div class="fs-trk">{slides}</div>{arrows}<div class="fs-dots">{dots}</div></div>
        <div class="reel-cap"><span class="cd">{code(PROJECTS.index(p), p)}</span><b>{p['name']}</b>{sheet}<span>{p['place']}{(' · ' + p['year']) if p.get('year') else ''}</span>{('<em class="reel-note">' + p['note'] + '</em>') if p.get('note') else ''}</div>
      </article>"""

REEL_SIZES = ["big", "", "", "tall", "", "", "wide", "", "", "", ""]

# v18: explicit order + size per project (Roberto, 13-sep-2026).
# big = 2x2 · hero = 3x2 · tall = 1x2 · wide = 2x1 · band = 3x1 · "" = 1x1
LAYOUT = [
  ("casa-jalpa", "xw"), ("casa-horizonte", "t23"),
  ("casa-travertino", "xl"), ("casa-jalpa-3", ""), ("casa-jalpa-2", ""),
  ("xl"), ("casa-de-campo-sma", ""), ("casa-ventanas", ""),
  ("casa-ether", "big"), ("bar-bachus", "big"),
  ("hotel-casa-x", "big"), ("casa-cuadrante", "big"),
  ("casa-valle", "wide"), ("chevrolet", "wide"),
  ("pabellon-arte", "wide"), ("casa-pena", "wide"),
  ("penas-obra", "wide"), ("plaza-qro", "wide"),
  ("amecsa", ""), ("daily-veggies", ""), ("tuluminati", ""), ("condesa", ""),
  ("restaurantes-sma", ""), ("wellness-merida", ""), ("binary-pavilion", ""),
  ("origen", ""), ("saiko", ""), ("casa-artista", ""), ("casa-velia", ""), ("casa-cien", ""),
]
# v22b: one grid (Roberto's arrangement) + category FILTER buttons (Roberto, 18-sep-2026)
CATS = {
  "homes": {"casa-ether","casa-jalpa","casa-pena","casa-jalpa-2","casa-jalpa-3","casa-valle","casa-horizonte","depa-jc","casa-de-campo-sma","condesa","casa-travertino","casa-ventanas","casa-artista","casa-velia"},
  "business": {"hotel-casa-x","amecsa","daily-veggies","casa-cuadrante","bar-bachus","tuluminati","restaurantes-sma","chevrolet","wellness-merida","plaza-qro","origen","saiko","casa-cien"},
}
def cat_of(slug):
    for k, v in CATS.items():
        if slug in v: return k
    return "other"
PENDING = {"saiko", "casa-artista", "casa-velia", "casa-cien", "origen"}

def pending_card(p, size=""):
    return f"""
      <article class="reel rv pend {size}" data-types="{' '.join(types(p))}" data-cat="{cat_of(p['slug'])}">
        <div class="reel-sl reel-pend"><span>Photography pending</span></div>
        <div class="reel-cap"><span class="cd">{code(PROJECTS.index(p), p)}</span><b>{p['name']}</b><span>{p['place']}{(' · ' + p['year']) if p.get('year') else ''}</span></div>
      </article>"""

def reels(ps=None, sizes=True):
    if ps is None:
        by = {p["slug"]: p for p in PROJECTS}
        out = []
        for slug, size in LAYOUT:
            p = by.get(slug)
            if not p: continue
            out.append(pending_card(p, size) if slug in PENDING else reel_card(p, size))
        seen = {s for s, _ in LAYOUT}
        out += [reel_card(p, "") for p in PROJECTS if p["slug"] not in seen]
        fl = '<div class="pfilters catf rv"><button class="on" data-cat="all">All</button><button data-cat="homes">Homes</button><button data-cat="business">Business</button><button data-cat="other">Other</button></div>'
        return fl + '<div class="reels">' + "".join(out) + '</div>' + proj_data()
    return '<div class="reels">' + "".join(reel_card(p, REEL_SIZES[i % len(REEL_SIZES)] if sizes else "") for i, p in enumerate(ps)) + '</div>'

def arch_section(num="01"):
    fl = """<div class="pfilters"><button class="on" data-cat="all">All</button><button data-cat="architecture">Architecture</button><button data-cat="interiors">Interiors</button><button data-cat="research">Research</button></div>"""
    return f"""
<section id="architecture">
  <div class="wrap">
    <div class="shead rv"><div class="eyebrow"><b>{num}</b>Architecture</div><i></i></div>
    <h2 class="rv d1">Each project develops its own architectural language.</h2>
    {fl}
    {reels()}
  </div>
</section>"""

CONSTRUCTION_SLUGS = ["penas-obra"]

def construction_section(num="02"):
    ps = [next(p for p in PROJECTS if p["slug"] == s) for s in CONSTRUCTION_SLUGS]
    return f"""
<section class="band" id="construction">
  <div class="wrap">
    <div class="shead rv"><div class="eyebrow"><b>{num}</b>Construction</div><i></i></div>
    <h2 class="rv d1">Drawn and built by the same hand.</h2>
    <p class="lead rv d2" style="max-width:600px;">Roberto directs the site personally. Larger works are built with Espacios y Formas.</p>
    {reels(ps, sizes=False)}
    <div class="cap rv" style="margin-top:14px;">Magno Towers · Casa Elo · La Escondida — construction photography to follow.</div>
  </div>
</section>"""

CSS = r"""
/* ── reels (v13) ── */
.catf{margin-top:0;}
.reels{display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:140px;grid-auto-flow:dense;gap:18px;margin-top:28px;}
.reel{grid-row:span 2;}
@media(max-width:1000px){.reels{grid-template-columns:repeat(2,1fr);}}
@media(max-width:600px){.reels{grid-template-columns:1fr;grid-auto-rows:130px;}}
.reel{display:flex;flex-direction:column;min-height:0;}
.reel.big{grid-column:span 2;grid-row:span 4;} .reel.tall{grid-row:span 4;} .reel.wide{grid-column:span 2;}
.reel.xl{grid-column:span 3;grid-row:span 4;} .reel.band{grid-column:span 3;}
.reel.w32{grid-column:span 2;grid-row:span 3;} .reel.t23{grid-row:span 3;} .reel.xw{grid-column:span 3;grid-row:span 3;}
@media(max-width:1000px){.reel.xl,.reel.xw{grid-column:span 2;} .reel.band{grid-column:span 2;}}
@media(max-width:600px){.reel.big,.reel.wide,.reel.xl,.reel.xw,.reel.band,.reel.w32{grid-column:span 1;}.reel.big,.reel.tall,.reel.xl,.reel.xw,.reel.w32,.reel.t23{grid-row:span 2;}}
.reel-pend{display:flex;align-items:flex-end;padding:16px;background:var(--paper-2);border:1px solid var(--line);}
.reel-pend span{font-size:.62rem;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-soft);}
.reel.hide{display:none;}
.reel .reel-sl{flex:1;min-height:0;position:relative;overflow:hidden;background:var(--paper-2);}
.reel .fs-trk{display:flex;height:100%;transition:transform .6s var(--ease);}
.reel .fs-trk img{width:100%;height:100%;flex:0 0 100%;object-fit:cover;display:block;}
.reel .fs-arr{opacity:0;transition:opacity .25s;}
.reel:hover .fs-arr{opacity:1;}
.reel-cap{display:grid;grid-template-columns:auto 1fr auto;gap:3px 12px;align-items:baseline;padding:10px 0 0;}
.reel-cap .cd{font-family:var(--mono);font-size:.58rem;letter-spacing:.14em;color:var(--red);}
.reel-cap b{font-family:var(--sans);font-weight:400;font-size:1.05rem;color:var(--navy);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.reel.big .reel-cap b,.reel.xl .reel-cap b,.reel.xw .reel-cap b{font-size:1.4rem;}
.reel .fs-trk img[src*="-plan"]{object-fit:contain;background:#fff;}
.reel-note{grid-column:2;font-style:normal;font-size:.72rem;line-height:1.4;color:var(--red);margin-top:2px;}
.reel-cap>span:not(.cd){grid-column:2;font-family:var(--mono);font-size:.58rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-soft);}
.reel-cap a{font-family:var(--mono);font-size:.58rem;letter-spacing:.12em;text-transform:uppercase;color:var(--navy);text-decoration:none;}
.reel-cap a:hover{color:var(--red);}
"""

JS = r"""
<script>
// reels: auto-advancing sliders; a manual arrow stops the auto-advance
document.querySelectorAll('.reel-sl').forEach(root=>{
  const trk=root.querySelector('.fs-trk'), n=parseInt(root.dataset.n||1); if(n<2) return;
  const dots=[...root.querySelectorAll('.fs-dots i')]; let i=0, t=null;
  const go=k=>{i=(k+n)%n; trk.style.transform='translateX(-'+(i*100)+'%)'; dots.forEach((d,j)=>d.classList.toggle('on',j===i));};
  const start=()=>{if(!t)t=setInterval(()=>go(i+1),3600+Math.random()*900);}; const stop=()=>{clearInterval(t);t=null;};
  root.querySelector('.fs-arr.l').addEventListener('click',e=>{e.stopPropagation();stop();go(i-1);});
  root.querySelector('.fs-arr.r').addEventListener('click',e=>{e.stopPropagation();stop();go(i+1);});
  dots.forEach((d,j)=>d.addEventListener('click',e=>{e.stopPropagation();stop();go(j);}));
  go(0); new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)start();else stop();}),{threshold:.2}).observe(root);
});
document.querySelectorAll('.pfilters').forEach(f=>{
  const grid=f.parentElement.querySelector('.reels'); if(!grid) return;
  f.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{
    f.querySelectorAll('button').forEach(x=>x.classList.remove('on')); b.classList.add('on');
    const c=b.dataset.cat; grid.querySelectorAll('.reel').forEach(p=>p.classList.toggle('hide', c!=='all' && (f.classList.contains('catf') ? p.dataset.cat!==c : !(' '+p.dataset.types+' ').includes(' '+c+' '))));
  }));
});
</script>
"""


def construction_grid():
    """Construction page: only the photos Roberto filed under construction, as a plain photo grid."""
    p = next(p for p in PROJECTS if p["slug"] == "penas-obra")
    cap = "Peñas Arriba · San Miguel de Allende"
    tiles = "".join(f'<figure class="cg"><a class="lbx" href="{x}"><img src="{x}" alt="{cap} — site works" loading="lazy"></a><figcaption><b>{cap}</b><span>Site works · {i+1:02d}</span></figcaption></figure>' for i, x in enumerate(p["photos"]))
    return f'<div class="pgrid">{tiles}</div>'

CSS += r"""
.pgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:8px;}
@media(max-width:900px){.pgrid{grid-template-columns:repeat(2,1fr);}}
@media(max-width:600px){.pgrid{grid-template-columns:1fr;}}
.pgrid a{display:block;aspect-ratio:3/2;overflow:hidden;background:var(--paper-2);}
.pgrid figure{margin:0;} .pgrid>*:nth-child(6n+1){grid-column:span 2;} .pgrid>*:nth-child(6n+1) a{aspect-ratio:2/1;}
@media(max-width:600px){.pgrid>*:nth-child(6n+1){grid-column:span 1;} .pgrid>*:nth-child(6n+1) a{aspect-ratio:3/2;}}
.pgrid img{width:100%;height:100%;object-fit:cover;display:block;transition:transform 1s var(--ease);}
.pgrid a:hover img{transform:scale(1.03);}
.pgrid img[src$="pa-master-plan.jpg"]{object-fit:contain;background:#fff;}
.pgrid figcaption{display:flex;justify-content:space-between;gap:12px;padding:8px 0 0;font-size:.62rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-soft);}
.pgrid figcaption b{font-weight:500;color:#161616;}
"""


# ── v20: construction organised by site, with captions (photos Roberto sent 14-sep-2026) ──
def _ob(tag, n):
    return [f"img/ob-{tag}-{i:02d}.jpg" for i in range(1, n + 1)]

SITES = [
  ("Magno Towers", "Celaya · Guanajuato", "Espacios y Formas", _ob("magno-towers-a", 4) + _ob("magno-towers-b", 6)),
  ("Magno", "Celaya · Guanajuato", "Espacios y Formas", _ob("magno", 3)),
  ("Peñas Arriba", "San Miguel de Allende", "RBC with Espacios y Formas", None),
  ("Casa Ether", "Piedras Azules · San Miguel de Allende", "Built by RBC", _ob("casa-ether", 17)),
  ("Casa Travertino", "Club de Golf El Campanario · Querétaro", "Built by RBC", _ob("casa-travertino", 9)),
  ("Casa Ventanas", "San Miguel de Allende", "Built by RBC", _ob("casa-ventanas", 10)),
  ("Quinta Elo", "Los Huizaches · San Miguel de Allende", "Built by RBC", _ob("quinta-elo", 9)),
  ("La Nueva Escondida", "San Miguel de Allende", "Espacios y Formas · completed", ['img/ph-nesc-08.jpg', 'img/ph-nesc-01.jpg', 'img/ph-nesc-03.jpg', 'img/ph-nesc-13.jpg', 'img/ph-nesc-15.jpg', 'img/ph-nesc-21.jpg'] + _ob("nueva-escondida", 7)),
]

def construction_packs():
    """v22: one same-size pack per site — slider with all its photos (Roberto, 18-sep-2026)."""
    out = []
    for i, (name, place, who, photos) in enumerate(SITES):
        if photos is None:
            photos = next(p for p in PROJECTS if p["slug"] == "penas-obra")["photos"]
        slides = "".join(f'<img src="{x}" alt="{name} — construction, {place}" loading="lazy">' for x in photos)
        dots = "".join('<i></i>' for _ in photos)
        out.append(f"""
      <article class="reel rv pack" id="site-{i+1}">
        <div class="fs-slider reel-sl" data-n="{len(photos)}"><div class="fs-trk">{slides}</div><button class="fs-arr l" aria-label="Previous">‹</button><button class="fs-arr r" aria-label="Next">›</button><div class="fs-dots">{dots}</div><span class="pack-n">{len(photos)} photos</span></div>
        <div class="reel-cap"><span class="cd">RBC/C-{i+1:03d}</span><b>{name}</b><span>{place} · {who}</span></div>
      </article>""")
    return '<div class="packs">' + "".join(out) + '</div>'

def construction_sites():
    out = []
    for i, (name, place, who, photos) in enumerate(SITES):
        if photos is None:
            photos = next(p for p in PROJECTS if p["slug"] == "penas-obra")["photos"]
        def _wide(x):
            try:
                from PIL import Image; import os
                base = os.path.dirname(os.path.abspath(__file__))
                for cand in (os.path.join(base, "..", "site", x), os.path.join(base, "..", x)):
                    if os.path.exists(cand):
                        w, h = Image.open(cand).size
                        return w > h
                return False
            except Exception:
                return False
        tiles = "".join(f'<figure class="cg{" wide" if _wide(x) else ""}"><a class="lbx" href="{x}"><img src="{x}" alt="{name} — construction, {place}" loading="lazy"></a><figcaption><b>{name}</b><span>{place} · {k+1:02d}</span></figcaption></figure>' for k, x in enumerate(photos))
        out.append(f"""
<section class="{'band' if i % 2 else ''}" id="site-{i+1}"><div class="wrap">
  <div class="shead rv"><div class="eyebrow"><b>{i+1:02d}</b>{name}</div><i></i></div>
  <div class="site-meta rv"><span>{place}</span><span>{who}</span><span>{len(photos)} photos</span></div>
  <div class="ogrid">{tiles}</div>
</div></section>""")
    return "".join(out)

CSS += r"""
.packs{display:grid;grid-template-columns:repeat(3,1fr);gap:22px 18px;margin-top:8px;}
.packs .reel.pack{grid-row:auto;grid-column:auto;}
.packs .reel.pack .reel-sl{aspect-ratio:4/3;flex:none;}
.pack-n{position:absolute;top:10px;left:10px;z-index:2;background:rgba(255,255,255,.9);color:var(--navy);font-family:var(--mono);font-size:.56rem;letter-spacing:.14em;text-transform:uppercase;padding:4px 8px;}
@media(max-width:900px){.packs{grid-template-columns:repeat(2,1fr);}}
@media(max-width:600px){.packs{grid-template-columns:1fr;}}
.site-meta{display:flex;gap:22px;flex-wrap:wrap;margin:-8px 0 18px;font-size:.66rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-soft);}
.ogrid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;}
@media(max-width:900px){.ogrid{grid-template-columns:repeat(3,1fr);}}
@media(max-width:600px){.ogrid{grid-template-columns:repeat(2,1fr);gap:12px;}}
.ogrid figure{margin:0;}
.ogrid a{display:block;aspect-ratio:3/4;overflow:hidden;background:var(--paper-2);}
.ogrid figure.wide{grid-column:span 2;} .ogrid figure.wide a{aspect-ratio:3/2;}
@media(max-width:600px){.ogrid figure.wide{grid-column:span 2;}}
.ogrid img{width:100%;height:100%;object-fit:cover;display:block;transition:transform 1s var(--ease);}
.ogrid a:hover img{transform:scale(1.03);}
.ogrid figcaption{display:flex;justify-content:space-between;gap:10px;padding:8px 0 0;font-size:.6rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-soft);}
.ogrid figcaption b{font-weight:500;color:#161616;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
"""


# ── v24: project sheet (modal) in Architecture — only data we actually have (Roberto, 22-sep-2026) ──
import json as _json
# only descriptions Roberto dictated or approved (22-sep-2026); the rest wait for his text / Instagram captions
DESC_OK = {"casa-ether", "casa-travertino", "casa-horizonte", "casa-cuadrante", "hotel-casa-x", "pabellon-arte", "bar-bachus", "binary-pavilion", "casa-jalpa", "casa-de-campo-sma", "condesa", "wellness-merida", "restaurantes-sma", "tuluminati", "amecsa", "chevrolet", "plaza-qro", "daily-veggies"}
def proj_data():
    out = {}
    for p in PROJECTS:
        if p["slug"] in PENDING: continue
        ph = _ph(p)
        photos = [x for x in ph if "-plan" not in x and "-section" not in x]
        plans = [x for x in ph if x not in photos]
        out[p["slug"]] = dict(
            code=code(PROJECTS.index(p), p), name=p["name"], place=p["place"], year=p.get("year", ""),
            status="Built by RBC" if p.get("built") else "Project",
            txt=p.get("txt", "") if p["slug"] in DESC_OK else "", note=p.get("note", ""), m2=p.get("m2", ""), long=p.get("long", ""),
            photos=photos, plans=plans,
            ig=f"https://www.instagram.com/p/{p['ig']}/" if p.get("ig") else "",
            sale=p.get("sale", ""))
    return f'<script>window.PROJ=Object.assign(window.PROJ||{{}},{_json.dumps(out, ensure_ascii=False)});</script>'

JS_PROJ = r"""
<script>
(function(){
  const box=document.getElementById('fbig'), body=document.getElementById('fbig-body');
  if(!box||!window.PROJ) return;
  function esc(s){return String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}
  let timer=null;
  function slider(root,auto){
    const trk=root.querySelector('.fb-trk'), n=trk.children.length, dots=root.querySelector('.fs-dots'); let i=0;
    const paint=()=>{trk.style.transform='translateX(-'+(i*100)+'%)'; if(dots)[...dots.children].forEach((d,k)=>d.classList.toggle('on',k===i));};
    const go=d=>{i=(i+d+n)%n;paint();};
    clearInterval(timer); if(auto&&n>1) timer=setInterval(()=>go(1),4000);
    root.querySelectorAll('.fs-arr').forEach(b=>b.onclick=e=>{e.stopPropagation();clearInterval(timer);go(b.classList.contains('l')?-1:1);});
    if(dots)[...dots.children].forEach((d,k)=>d.onclick=e=>{e.stopPropagation();clearInterval(timer);i=k;paint();});
    paint();
  }
  window.openProj=function(slug){
    const d=window.PROJ[slug]; if(!d) return;
    const mk=arr=>arr.map(p=>'<img src="'+p+'" alt="'+esc(d.name)+'" loading="lazy">').join('');
    const shots=d.photos.length?d.photos:d.plans, plans=d.photos.length?d.plans:[];
    body.innerHTML=
      '<div class="fb-hero pj-hero'+(d.photos.length?'':' plans')+'" id="fb-hero"><div class="fb-trk">'+mk(shots)+'</div>'+
        (shots.length>1?'<button class="fs-arr l" aria-label="Previous">‹</button><button class="fs-arr r" aria-label="Next">›</button><div class="fs-dots">'+shots.map(()=>'<i></i>').join('')+'</div>':'')+
        (plans.length?'<div class="fb-tabs"><button class="on" data-set="photos">Photos</button><button data-set="plans">Plans</button></div>':'')+
      '</div>'+
      '<div class="fb-in pj-in">'+
        '<div class="fb-head"><div><div class="fs-where"><span class="cd">'+esc(d.code)+'</span> · '+esc(d.place)+(d.year?' · '+esc(d.year):'')+'</div><h2>'+esc(d.name)+'</h2><div class="fs-auth">'+esc(d.status)+'</div></div>'+
        (d.m2?'<div class="fs-pr">'+esc(d.m2)+' m²</div>':'')+'</div>'+
        '<div class="fb-grid"><div>'+
          (d.txt?'<h4>About the project</h4><p class="lead" style="font-size:1rem">'+esc(d.txt)+'</p>':'')+
          (d.long?'<p style="font-size:.92rem;color:var(--ink-soft)">'+esc(d.long)+'</p>':'')+
          (d.note?'<p class="reel-note" style="display:block;margin-top:10px">'+esc(d.note)+'</p>':'')+
        '</div><div>'+
          (plans.length?'<h4>Plans</h4><div class="fb-plans">'+plans.map(p=>'<a class="lbx2" href="'+p+'"><img src="'+p+'" alt="Plan"></a>').join('')+'</div>':'')+
        '</div></div>'+
        '<div class="fb-cta">'+
          (d.sale?'<a class="btn red" href="'+d.sale+'">This house is for sale →</a>':'')+
          (d.ig?'<a class="btn ghost" href="'+d.ig+'" target="_blank" rel="noopener">View on Instagram</a>':'')+
          '<a class="btn ghost" href="contact.html">Ask about this project</a>'+
        '</div>'+
      '</div>';
    box.classList.add('on'); box.setAttribute('aria-hidden','false'); document.body.classList.add('fbig-open'); body.scrollTop=0;
    const hero=document.getElementById('fb-hero'); slider(hero,true);
    hero.querySelectorAll('.fb-tabs button').forEach(b=>b.addEventListener('click',()=>{
      hero.querySelectorAll('.fb-tabs button').forEach(x=>x.classList.remove('on')); b.classList.add('on');
      const isP=b.dataset.set==='plans'; hero.classList.toggle('plans',isP); const set=isP?plans:shots;
      hero.querySelector('.fb-trk').innerHTML=mk(set); const dots=hero.querySelector('.fs-dots'); if(dots) dots.innerHTML=set.map(()=>'<i></i>').join('');
      slider(hero,!isP);
    }));
    body.querySelectorAll('a.lbx2').forEach(a=>a.addEventListener('click',e=>{e.preventDefault();const lb=document.getElementById('lb');if(lb){document.getElementById('lbimg').src=a.href;lb.classList.add('on');}}));
    history.replaceState(null,'','#'+slug);
  };
  document.querySelectorAll('.reel[data-proj]').forEach(card=>{
    const open=()=>openProj(card.dataset.proj);
    card.addEventListener('click',e=>{ if(e.target.closest('.fs-arr,.fs-dots')) return; open(); });
    card.addEventListener('keydown',e=>{ if(e.key==='Enter'||e.key===' '){e.preventDefault();open();} });
  });
  const stop=()=>clearInterval(timer);
  box.querySelector('.fbig-x').addEventListener('click',stop); box.querySelector('.fbig-bg').addEventListener('click',stop);
  if(location.hash && window.PROJ[location.hash.slice(1)]) setTimeout(()=>openProj(location.hash.slice(1)),400);
})();
</script>
"""
CSS += r"""
.fb-hero.pj-hero img{object-fit:contain;background:#111;}
.fb-hero.pj-hero{height:min(66vh,640px);}
.reel[data-proj]{cursor:pointer;} .reel[data-proj]:hover .reel-cap b{color:var(--red);}
.pj-in .fs-where .cd{font-family:var(--mono);font-size:.62rem;letter-spacing:.14em;color:var(--red);}
.pj-in .fb-head .fs-pr{font-size:1.5rem;}
"""
