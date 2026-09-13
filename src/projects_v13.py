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
    sheet = f'<a href="{p["sale"]}">Sheet →</a>' if p.get("sale") else ""
    return f"""
      <article class="reel rv {size}" data-types="{' '.join(types(p))}">
        <div class="fs-slider reel-sl" data-n="{len(ph)}"><div class="fs-trk">{slides}</div>{arrows}<div class="fs-dots">{dots}</div>{'<span class="fs-st">For sale</span>' if p.get('sale') else ''}</div>
        <div class="reel-cap"><span class="cd">{code(PROJECTS.index(p), p)}</span><b>{p['name']}</b>{sheet}<span>{p['place']}{(' · ' + p['year']) if p.get('year') else ''}</span></div>
      </article>"""

REEL_SIZES = ["big", "", "", "tall", "", "", "wide", "", "", "", ""]

# v18: explicit order + size per project (Roberto, 13-sep-2026).
# big = 2x2 · hero = 3x2 · tall = 1x2 · wide = 2x1 · band = 3x1 · "" = 1x1
LAYOUT = [
  ("casa-ether", "big"), ("penas-obra", ""), ("hotel-casa-x", ""), ("amecsa", ""), ("casa-de-campo-sma", ""),
  ("casa-horizonte", "hero"), ("depa-jc", "tall"),
  ("casa-jalpa", "hero"), ("casa-cuadrante", "tall"),
  ("bar-bachus", "hero"), ("condesa", "tall"),
  ("chevrolet", "band"), ("daily-veggies", ""),
  ("pabellon-arte", "wide"), ("tuluminati", ""), ("origen", ""),
  ("casa-jalpa-2", "band"), ("restaurantes-sma", ""),
  ("casa-jalpa-3", "band"), ("wellness-merida", ""),
  ("casa-travertino", "wide"), ("plaza-qro", "wide"),
  ("binary-pavilion", "wide"), ("saiko", ""), ("casa-artista", ""),
  ("casa-velia", ""), ("casa-cien", ""),
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
.reels{display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:280px;grid-auto-flow:dense;gap:18px;margin-top:28px;}
@media(max-width:1000px){.reels{grid-template-columns:repeat(2,1fr);}}
@media(max-width:600px){.reels{grid-template-columns:1fr;grid-auto-rows:260px;}}
.reel{display:flex;flex-direction:column;min-height:0;}
.reel.big{grid-column:span 2;grid-row:span 2;} .reel.tall{grid-row:span 2;} .reel.wide{grid-column:span 2;}
.reel.hero{grid-column:span 3;grid-row:span 2;} .reel.band{grid-column:span 3;}
@media(max-width:1000px){.reel.hero{grid-column:span 2;} .reel.band{grid-column:span 2;}}
@media(max-width:600px){.reel.big,.reel.wide,.reel.hero,.reel.band{grid-column:span 1;}.reel.big,.reel.tall,.reel.hero{grid-row:span 1;}}
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
.reel.big .reel-cap b,.reel.hero .reel-cap b{font-size:1.4rem;}
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
.pgrid figcaption{display:flex;justify-content:space-between;gap:12px;padding:8px 0 0;font-size:.62rem;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-soft);}
.pgrid figcaption b{font-weight:500;color:#161616;}
"""
