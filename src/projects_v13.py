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
      <article class="reel rv {size}" data-types="{' '.join(types(p))}">
        <div class="fs-slider reel-sl" data-n="{len(ph)}"><div class="fs-trk">{slides}</div>{arrows}<div class="fs-dots">{dots}</div></div>
        <div class="reel-cap"><span class="cd">{code(PROJECTS.index(p), p)}</span><b>{p['name']}</b>{sheet}<span>{p['place']}{(' · ' + p['year']) if p.get('year') else ''}</span></div>
      </article>"""

REEL_SIZES = ["big", "", "", "tall", "", "", "wide", "", "", "", ""]

# v18: explicit order + size per project (Roberto, 13-sep-2026).
# big = 2x2 · hero = 3x2 · tall = 1x2 · wide = 2x1 · band = 3x1 · "" = 1x1
LAYOUT = [
  ("casa-ether", "big"), ("penas-obra", ""), ("hotel-casa-x", ""), ("amecsa", ""), ("daily-veggies", ""),
  ("casa-horizonte", "wide"), ("depa-jc", "t23"), ("casa-cuadrante", "t23"),
  ("casa-de-campo-sma", "w32"), ("tuluminati", ""), ("condesa", ""),
  ("casa-jalpa", "xl"), ("origen", ""), ("restaurantes-sma", ""),
  ("bar-bachus", "xl"), ("wellness-merida", ""), ("pabellon-arte", ""),
  ("casa-travertino", "big"), ("chevrolet", "big"),
  ("casa-jalpa-2", "band"), ("binary-pavilion", ""),
  ("casa-jalpa-3", "wide"), ("plaza-qro", ""), ("casa-valle", "wide"),
  ("casa-ventanas", ""),
  ("saiko", ""),
  ("casa-artista", ""), ("casa-velia", ""), ("casa-cien", ""),
]
PENDING = {"saiko", "casa-artista", "casa-velia", "casa-cien"}

def pending_card(p, size=""):
    return f"""
      <article class="reel rv pend {size}" data-types="{' '.join(types(p))}">
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
        return '<div class="reels">' + "".join(out) + '</div>'
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
.reels{display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:140px;grid-auto-flow:dense;gap:18px;margin-top:28px;}
.reel{grid-row:span 2;}
@media(max-width:1000px){.reels{grid-template-columns:repeat(2,1fr);}}
@media(max-width:600px){.reels{grid-template-columns:1fr;grid-auto-rows:130px;}}
.reel{display:flex;flex-direction:column;min-height:0;}
.reel.big{grid-column:span 2;grid-row:span 4;} .reel.tall{grid-row:span 4;} .reel.wide{grid-column:span 2;}
.reel.xl{grid-column:span 3;grid-row:span 4;} .reel.band{grid-column:span 3;}
.reel.w32{grid-column:span 2;grid-row:span 3;} .reel.t23{grid-row:span 3;}
@media(max-width:1000px){.reel.xl{grid-column:span 2;} .reel.band{grid-column:span 2;}}
@media(max-width:600px){.reel.big,.reel.wide,.reel.xl,.reel.band,.reel.w32{grid-column:span 1;}.reel.big,.reel.tall,.reel.xl,.reel.w32,.reel.t23{grid-row:span 2;}}
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
.reel.big .reel-cap b,.reel.xl .reel-cap b{font-size:1.4rem;}
.reel .fs-trk img[src$="-plan.jpg"]{object-fit:contain;background:#fff;}
.reel-cap>span:last-child{grid-column:2;font-family:var(--mono);font-size:.58rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-soft);}
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
    const c=b.dataset.cat; grid.querySelectorAll('.reel').forEach(p=>p.classList.toggle('hide', c!=='all' && !(' '+p.dataset.types+' ').includes(' '+c+' ')));
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
  ("La Nueva Escondida", "San Miguel de Allende", "Espacios y Formas", _ob("nueva-escondida", 7)),
]

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
