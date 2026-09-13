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

def reels(ps=None, sizes=True):
    ps = ps or PROJECTS
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

CONSTRUCTION_SLUGS = ["penas-obra", "casa-horizonte", "casa-ether", "casa-travertino", "bar-bachus", "casa-cuadrante", "depa-jc", "tuluminati"]

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
.reels{display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:250px;grid-auto-flow:dense;gap:18px;margin-top:28px;}
@media(max-width:1000px){.reels{grid-template-columns:repeat(2,1fr);}}
@media(max-width:600px){.reels{grid-template-columns:1fr;grid-auto-rows:260px;}}
.reel{display:flex;flex-direction:column;min-height:0;}
.reel.big{grid-column:span 2;grid-row:span 2;} .reel.tall{grid-row:span 2;} .reel.wide{grid-column:span 2;}
@media(max-width:600px){.reel.big,.reel.wide{grid-column:span 1;}.reel.big,.reel.tall{grid-row:span 1;}}
.reel.hide{display:none;}
.reel .reel-sl{flex:1;min-height:0;position:relative;overflow:hidden;background:var(--paper-2);}
.reel .fs-trk{display:flex;height:100%;transition:transform .6s var(--ease);}
.reel .fs-trk img{width:100%;height:100%;flex:0 0 100%;object-fit:cover;display:block;}
.reel .fs-arr{opacity:0;transition:opacity .25s;}
.reel:hover .fs-arr{opacity:1;}
.reel-cap{display:grid;grid-template-columns:auto 1fr auto;gap:3px 12px;align-items:baseline;padding:10px 0 0;}
.reel-cap .cd{font-family:var(--mono);font-size:.58rem;letter-spacing:.14em;color:var(--red);}
.reel-cap b{font-family:'Fraunces',serif;font-weight:400;font-size:1.05rem;color:var(--navy);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.reel.big .reel-cap b{font-size:1.4rem;}
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
