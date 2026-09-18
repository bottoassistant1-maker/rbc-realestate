# -*- coding: utf-8 -*-
"""The three 'fichas': small card (auto slider) → big modal sheet → PDF technical sheet."""
import json, html

def photos(l):
    return [l["img"]] + [g for g in l.get("gallery", []) if g != l["img"]]

def small_card(l, wa, i=0, md=False):
    ph = photos(l)
    slides = "".join(f'<img src="{p}" alt="{html.escape(l["name"])}" loading="lazy">' for p in ph)
    sp = "".join(f"<span><b>{a}</b> {b}</span>" for a, b in l["specs"][:4])
    from listings import price_line
    d = "d" + str(i % 3) if i % 3 else ""
    return f"""
      <article class="fs rv {d}{' fs-md' if md else ''}" data-slug="{l['slug']}" tabindex="0" role="button" aria-label="Open {html.escape(l['name'])}">
        <div class="fs-slider" data-n="{len(ph)}"><div class="fs-trk">{slides}</div>
          <button class="fs-arr l" aria-label="Previous photo">‹</button><button class="fs-arr r" aria-label="Next photo">›</button>
          <div class="fs-dots">{"".join('<i></i>' for _ in ph)}</div>
          <span class="fs-st{' fs-rent' if l.get('kind')=='rent' else ''}">{l['status']}</span>
        </div>
        <div class="fs-bd">
          <div class="fs-where">{l['where']}</div>
          <h3>{l['name']}{'<img class="fs-brand" src="img/penas-arriba-logo.png" alt="Peñas Arriba" title="Peñas Arriba">' if 'Peñas Arriba' in l['where'] else ''}</h3>
          <div class="fs-pr">{price_line(l)}</div>
          <div class="fs-sp">{sp}</div>
          <span class="fs-open">Open sheet →</span>
        </div>
      </article>"""

def grid(ls, wa, md=False):
    return '<div class="fgrid' + (' fgrid-md' if md else '') + '">' + "".join(small_card(l, wa, i, md) for i, l in enumerate(ls)) + "</div>"

def modal_data(ls, wa):
    """Embed the data every modal needs."""
    from listings import price_line
    out = {}
    for l in ls:
        out[l["slug"]] = dict(
            name=l["name"], where=l["where"], status=l["status"], price=price_line(l, True),
            photos=photos(l), plans=l.get("plans", []), specs=l["specs"],
            intro=l.get("intro") or l.get("blurb", ""), highlights=l.get("highlights", []), units=l.get("units", []),
            sections=[(k, l.get(v, "")) for k, v in (("Architecture","arch"),("Site","site"),("Materials","materials"),("Condition","condition"),("Potential","potential")) if l.get(v) and l.get(v) != "—"], notes=l.get("notes", ""), auth=l.get("auth",""), nlabel=__import__('listings').notes_label(),
            program=l.get("program", []), location=l.get("location", ""),
            page=(l["slug"] + ".html") if l.get("page") else l.get("href", ""),
            pdf=f"pdf/{l['slug']}.pdf" if l.get("pdf", True) else "",
            wa=wa(f"Hi Roberto, I'm interested in {l['name']} ({l['where']}). Could you send me more information?"),
            kind=l.get("kind", "sale"), links=l.get("links", []))
    return f'<script>window.FICHAS=Object.assign(window.FICHAS||{{}},{json.dumps(out, ensure_ascii=False)});</script>'

MODAL_HTML = """
<div class="fbig" id="fbig" aria-hidden="true">
  <div class="fbig-bg"></div>
  <div class="fbig-win" role="dialog" aria-modal="true">
    <button class="fbig-x" aria-label="Close">×</button>
    <div class="fbig-body" id="fbig-body"></div>
  </div>
</div>
"""

CSS = r"""
.fb-units{margin:0 0 26px;} .fb-units>div{display:grid;grid-template-columns:1fr auto;gap:2px 16px;padding:10px 0;border-top:1px solid var(--line);}
.fb-units>div b{font-weight:500;color:#161616;}
.fb-units>div span{grid-column:1;font-size:.82rem;color:var(--ink-soft);}
.fb-units>div i{grid-column:2;grid-row:1/3;font-style:normal;color:var(--red);font-weight:500;align-self:center;white-space:nowrap;}

.fs h3{display:flex;align-items:center;gap:10px;}
.fs-st.fs-rent{background:var(--red);color:#fff;font-weight:600;}
.fs h3 .fs-brand{height:32px;width:auto;flex:0 0 auto;}

/* ── ficha chica ── */
.fgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:30px;}
@media(max-width:1000px){.fgrid{grid-template-columns:1fr 1fr;}}
@media(max-width:640px){.fgrid{grid-template-columns:1fr;}}
.fgrid-md{grid-template-columns:repeat(2,1fr);}
@media(max-width:800px){.fgrid-md{grid-template-columns:1fr;}}
.fs{background:transparent;border:none;border-top:1px solid var(--navy);border-radius:0;overflow:hidden;cursor:pointer;display:flex;flex-direction:column;}
.fs:hover,.fs:focus-visible{outline:none;} .fs:hover .fs-open{color:var(--red);}
.fs-slider{position:relative;height:250px;overflow:hidden;background:var(--paper-2);margin-top:14px;}
.fs-md .fs-slider{height:320px;}
.fs-trk{display:flex;height:100%;transition:transform .8s var(--ease);}
.fs-trk img{flex:0 0 100%;width:100%;height:100%;object-fit:cover;}
.fs-arr{position:absolute;top:50%;transform:translateY(-50%);width:36px;height:36px;border-radius:2px;border:none;background:rgba(250,247,241,.92);color:var(--navy);font-size:1.15rem;cursor:pointer;opacity:0;transition:opacity .3s,background .2s;z-index:2;display:flex;align-items:center;justify-content:center;}
.fs:hover .fs-arr{opacity:1;}
.fs-arr:hover{background:var(--red);color:#fff;}
.fs-arr.l{left:10px;}.fs-arr.r{right:10px;}
.fs-dots{position:absolute;left:0;right:0;bottom:10px;display:flex;justify-content:center;gap:5px;z-index:2;}
.fs-dots i{width:6px;height:6px;border-radius:50%;background:rgba(255,255,255,.55);transition:.3s;}
.fs-dots i.on{background:var(--gold);width:16px;border-radius:4px;}
.fs-st{position:absolute;top:12px;left:12px;background:var(--paper);color:var(--navy);font-family:var(--mono);font-size:.58rem;letter-spacing:.14em;text-transform:uppercase;padding:5px 9px;z-index:2;}
.fs-bd{padding:16px 0 18px;display:flex;flex-direction:column;gap:4px;flex:1;}
.fs-where{font-family:var(--mono);font-size:.62rem;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-soft);}
.fs h3{font-size:1.3rem;font-weight:400;margin:2px 0 0;}
.fs-pr{font-family:'Fraunces',serif;font-size:1.3rem;color:var(--red);margin-top:4px;}
.fs-pr small{font-family:'Figtree',sans-serif;font-size:.74rem;color:var(--ink-soft);}
.fs-sp{display:flex;gap:12px;flex-wrap:wrap;font-size:.76rem;color:var(--ink-soft);margin-top:6px;}
.fs-sp b{color:var(--navy);}
.fs-open{margin-top:auto;padding-top:12px;font-family:var(--mono);font-size:.64rem;letter-spacing:.14em;text-transform:uppercase;color:var(--navy);transition:color .3s;}
/* ── ficha grande (modal) ── */
.fbig{position:fixed;inset:0;z-index:300;display:none;}
.fbig.on{display:block;}
.fbig-bg{position:absolute;inset:0;background:rgba(16,20,40,.82);opacity:0;transition:opacity .3s;}
.fbig.on .fbig-bg{opacity:1;}
.fbig-win{position:absolute;left:50%;top:3vh;transform:translate(-50%,30px);width:min(1180px,94vw);height:94vh;background:var(--paper);border-radius:4px;overflow:hidden;box-shadow:0 60px 120px -40px rgba(0,0,0,.6);opacity:0;transition:opacity .5s var(--ease),transform .6s var(--ease);display:flex;flex-direction:column;}
.fbig.on .fbig-win{opacity:1;transform:translate(-50%,0);}
.fbig-x{position:absolute;top:14px;right:14px;z-index:5;width:44px;height:44px;border-radius:3px;border:none;background:rgba(250,247,241,.95);color:var(--navy);font-size:1.7rem;cursor:pointer;box-shadow:0 8px 24px rgba(0,0,0,.25);}
.fbig-x:hover{background:var(--red);color:#fff;}
.fbig-body{overflow-y:auto;flex:1;-webkit-overflow-scrolling:touch;}
.fb-hero{position:relative;height:min(58vh,560px);background:#111;}
.fb-hero .fb-trk{display:flex;height:100%;transition:transform .8s var(--ease);}
.fb-hero img{flex:0 0 100%;width:100%;height:100%;object-fit:cover;}
.fb-hero.plans img{object-fit:contain;background:#fff;}
.fb-hero .fs-arr{opacity:1;width:48px;height:48px;}
.fb-hero .fs-dots{bottom:16px;}
.fb-tabs{position:absolute;top:16px;left:18px;display:flex;gap:6px;z-index:3;}
.fb-tabs button{font-family:var(--mono);font-size:.62rem;letter-spacing:.14em;text-transform:uppercase;padding:8px 12px;border-radius:2px;border:none;background:rgba(250,247,241,.9);color:var(--navy);cursor:pointer;}
.fb-tabs button.on{background:var(--gold);}
.fb-in{padding:34px 40px 44px;max-width:1040px;margin:0 auto;}
@media(max-width:700px){.fb-in{padding:22px 18px 34px;}}
.fb-head{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;align-items:flex-end;border-bottom:1px solid var(--line);padding-bottom:18px;}
.fb-head h2{font-size:clamp(1.8rem,3.4vw,2.6rem);margin:6px 0 4px;}
.fb-head .fs-pr{font-size:1.8rem;margin:0;}
.fb-specs{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:12px;margin:22px 0;}
.fb-specs div{background:transparent;border-top:1px solid var(--navy);padding:12px 0;text-align:left;}
.fb-specs .n{font-family:'Fraunces',serif;font-size:1.5rem;color:var(--navy);line-height:1;}
.fb-specs .l{font-size:.62rem;letter-spacing:.16em;text-transform:uppercase;color:var(--ink-soft);margin-top:5px;}
.fb-grid{display:grid;grid-template-columns:1.2fr 1fr;gap:34px;margin-top:10px;}
@media(max-width:800px){.fb-grid{grid-template-columns:1fr;}}
.fb-grid h4{font-family:'Fraunces',serif;font-weight:400;color:var(--navy);font-size:1.25rem;margin:18px 0 8px;}
.fb-grid .checks li{font-size:.9rem;padding:7px 0 7px 26px;}
.fb-prog{display:grid;gap:10px;}
.fb-prog div{border-top:1px solid var(--hair);padding:10px 0;font-size:.88rem;color:var(--ink-soft);}
.fb-prog b{display:block;color:var(--navy);font-family:'Fraunces',serif;font-weight:400;font-size:1.05rem;margin-bottom:3px;}
.fb-plans{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:8px;}
.fb-plans img{width:100%;border:1px solid var(--hair);background:#fff;}
.fb-cta{margin-top:34px;padding-top:26px;border-top:1px solid var(--line);display:flex;gap:12px;flex-wrap:wrap;align-items:center;}
.fb-cta .note{font-size:.76rem;color:var(--ink-soft);flex-basis:100%;}
body.fbig-open{overflow:hidden;}
"""

JS = r"""
<script>
(function(){
  // ── small-card sliders: auto-advance every 3.5 s; a manual click takes control ──
  function slider(root, trkSel, auto){
    const trk=root.querySelector(trkSel); if(!trk) return null;
    const n=trk.children.length; const dots=root.querySelector('.fs-dots'); let i=0, t=null, manual=false;
    const paint=()=>{trk.style.transform='translateX(-'+(i*100)+'%)'; if(dots)[...dots.children].forEach((d,k)=>d.classList.toggle('on',k===i));};
    const go=d=>{i=(i+d+n)%n; paint();};
    const start=()=>{ if(auto&&n>1&&!manual){clearInterval(t); t=setInterval(()=>go(1),3500);} };
    const stop=()=>{clearInterval(t);};
    root.querySelectorAll('.fs-arr').forEach(b=>b.addEventListener('click',e=>{e.stopPropagation();manual=true;stop();go(b.classList.contains('l')?-1:1);}));
    if(dots)[...dots.children].forEach((d,k)=>d.addEventListener('click',e=>{e.stopPropagation();manual=true;stop();i=k;paint();}));
    paint(); start();
    return {stop, go, paint, set:(k)=>{i=k;paint();}};
  }
  const io=new IntersectionObserver(es=>es.forEach(e=>{const s=e.target.__sl; if(!s) return; /* only animate while visible */ }),{threshold:.2});
  document.querySelectorAll('.fs').forEach(card=>{
    card.__sl=slider(card,'.fs-trk',true); io.observe(card);
    const open=()=>openFicha(card.dataset.slug);
    card.addEventListener('click',e=>{ if(e.target.closest('.fs-arr,.fs-dots')) return; open(); });
    card.addEventListener('keydown',e=>{ if(e.key==='Enter'||e.key===' '){e.preventDefault();open();} });
  });
  // ── big sheet ──
  const box=document.getElementById('fbig'), body=document.getElementById('fbig-body');
  if(!box) return;
  let bigSl=null;
  function esc(s){return String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}
  window.openFicha=function(slug){
    const d=(window.FICHAS||{})[slug]; if(!d) return;
    const shots=d.photos, plans=d.plans||[];
    const mk=(arr,alt)=>arr.map(p=>'<img src="'+p+'" alt="'+esc(alt)+'" loading="lazy">').join('');
    body.innerHTML=
      '<div class="fb-hero" id="fb-hero"><div class="fb-trk">'+mk(shots,d.name)+'</div>'+
        (shots.length>1?'<button class="fs-arr l" aria-label="Previous">‹</button><button class="fs-arr r" aria-label="Next">›</button><div class="fs-dots">'+shots.map(()=>'<i></i>').join('')+'</div>':'')+
        (plans.length?'<div class="fb-tabs"><button class="on" data-set="photos">Photos</button><button data-set="plans">Plans</button></div>':'')+
      '</div>'+
      '<div class="fb-in">'+
        '<div class="fb-head"><div><div class="fs-where">'+esc(d.where)+' · '+esc(d.status)+'</div><h2>'+esc(d.name)+'</h2>'+(d.auth?'<div class="fs-auth">'+esc(d.auth)+'</div>':'')+'</div><div class="fs-pr">'+d.price+'</div></div>'+
        '<div class="fb-specs">'+d.specs.map(s=>'<div><div class="n">'+esc(s[0])+'</div><div class="l">'+esc(s[1])+'</div></div>').join('')+'</div>'+
        ((d.units||[]).length?'<div class="fb-units"><h4>Available units</h4>'+d.units.map(u=>'<div><b>'+esc(u[0])+'</b><span>'+esc(u[1])+'</span><i>'+esc(u[2])+'</i></div>').join('')+'</div>':'')+
        '<div class="fb-grid"><div>'+
          '<h4>The '+(d.kind==='rent'?'space':'house')+'</h4><p class="lead" style="font-size:1rem">'+esc(d.intro)+'</p>'+
          (d.sections||[]).map(s=>'<h4>'+esc(s[0])+'</h4><p style="font-size:.92rem;color:var(--ink-soft)">'+esc(s[1])+'</p>').join('')+
          (d.notes?'<div class="notes"><small>'+d.nlabel+'</small><p>'+esc(d.notes)+'</p><div class="sig">— R. Balderas Carrillo, Arquitecto</div></div>':'')+
          (d.highlights.length?'<h4>At a glance</h4><ul class="checks">'+d.highlights.map(h=>'<li>'+esc(h)+'</li>').join('')+'</ul>':'')+
          (d.location?'<h4>Location</h4><p style="font-size:.92rem;color:var(--ink-soft)">'+esc(d.location)+'</p>':'')+
        '</div><div>'+
          (d.program.length?'<h4>Program</h4><div class="fb-prog">'+d.program.map(p=>'<div><b>'+esc(p[0])+'</b>'+esc(p[1])+'</div>').join('')+'</div>':'')+
          (plans.length?'<h4>Plans</h4><div class="fb-plans">'+plans.map(p=>'<a class="lbx2" href="'+p+'"><img src="'+p+'" alt="Plan"></a>').join('')+'</div>':'<h4>Plans</h4><p style="font-size:.88rem;color:var(--ink-soft)">Floor plans and the full technical sheet are available on request or in the PDF.</p>')+
        '</div></div>'+
        '<div class="fb-cta">'+
          '<a class="btn red" href="'+d.wa+'">Request information on WhatsApp</a>'+
          (d.pdf?'<a class="btn ghost" href="'+d.pdf+'" target="_blank" rel="noopener">Full sheet (PDF)</a>':'')+
          (d.page?'<a class="btn ghost" href="'+d.page+'">Open full page</a>':'')+
          (d.links||[]).map(k=>'<a class="btn ghost" href="'+k[1]+'" target="_blank" rel="noopener">'+esc(k[0])+'</a>').join('')+
          '<div class="note">Prices in MXN; USD approximate. Images provisional where noted.</div>'+
        '</div>'+
      '</div>';
    box.classList.add('on'); box.setAttribute('aria-hidden','false'); document.body.classList.add('fbig-open'); body.scrollTop=0;
    const hero=document.getElementById('fb-hero'); bigSl=slider(hero,'.fb-trk',true);
    // photo/plan tabs
    hero.querySelectorAll('.fb-tabs button').forEach(b=>b.addEventListener('click',()=>{
      hero.querySelectorAll('.fb-tabs button').forEach(x=>x.classList.remove('on')); b.classList.add('on'); hero.classList.toggle('plans', b.dataset.set==='plans');
      const set=b.dataset.set==='plans'?plans:shots; hero.querySelector('.fb-trk').innerHTML=mk(set,d.name);
      const dots=hero.querySelector('.fs-dots'); if(dots) dots.innerHTML=set.map(()=>'<i></i>').join('');
      if(bigSl) bigSl.stop(); bigSl=slider(hero,'.fb-trk',b.dataset.set!=='plans');
    }));
    body.querySelectorAll('a.lbx2').forEach(a=>a.addEventListener('click',e=>{e.preventDefault();const lb=document.getElementById('lb');if(lb){document.getElementById('lbimg').src=a.href;lb.classList.add('on');}}));
    history.replaceState(null,'','#'+slug);
  };
  const close=()=>{box.classList.remove('on');box.setAttribute('aria-hidden','true');document.body.classList.remove('fbig-open');if(bigSl)bigSl.stop();history.replaceState(null,'',location.pathname);};
  box.querySelector('.fbig-x').addEventListener('click',close);
  box.querySelector('.fbig-bg').addEventListener('click',close);
  document.addEventListener('keydown',e=>{if(e.key==='Escape'&&box.classList.contains('on'))close();});
  // deep link: real-estate.html#casa-cima opens the sheet
  if(location.hash && (window.FICHAS||{})[location.hash.slice(1)]) setTimeout(()=>openFicha(location.hash.slice(1)),400);
})();
</script>
"""

# ───────────── PDF technical sheet ─────────────
def pdf_html(l, site_url):
    from listings import price_line
    ph = photos(l)
    sp = "".join(f'<div class="s"><b>{a}</b><span>{b}</span></div>' for a, b in l["specs"])
    hl = "".join(f"<li>{h}</li>" for h in l.get("highlights", []))
    prog = "".join(f"<div class='p'><b>{a}</b>{b}</div>" for a, b in l.get("program", []))
    plans = "".join(f'<img class="plan" src="{p}">' for p in l.get("plans", []))
    gal = "".join(f'<img src="{p}">' for p in ph[1:])
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{l['name']} — RBC technical sheet</title>
<style>
@page{{size:A4;margin:14mm 14mm 16mm;}}
body{{font-family:'Figtree','Helvetica Neue',Arial,sans-serif;color:#20242E;font-size:10.5pt;line-height:1.45;}}
h1,h2,h3{{font-family:'Fraunces',Georgia,serif;font-weight:400;color:#232F66;margin:0;}}
.top{{display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #E0D9CA;padding-bottom:8px;}}
.top img{{height:34px;}} .top .r{{font-size:8pt;letter-spacing:.2em;text-transform:uppercase;color:#5A6070;text-align:right;}}
.hero{{margin:12px 0 10px;height:95mm;overflow:hidden;border-radius:6px;background:#eee;}} .hero img{{width:100%;height:100%;object-fit:cover;}}
.eyebrow{{font-size:7.5pt;letter-spacing:.3em;text-transform:uppercase;color:#E8402A;font-weight:700;}}
h1{{font-size:26pt;line-height:1.05;margin:4px 0 2px;}}
.price{{font-family:'Fraunces',Georgia,serif;font-size:18pt;color:#E8402A;margin:4px 0 10px;}} .price small{{font-family:'Figtree',Arial;font-size:9pt;color:#5A6070;}}
.specs{{display:flex;gap:8px;flex-wrap:wrap;margin:8px 0 12px;}} .s{{border:1px solid #E0D9CA;border-radius:6px;padding:6px 10px;min-width:70px;text-align:center;}} .s b{{display:block;font-family:'Fraunces',Georgia,serif;font-weight:400;font-size:14pt;color:#232F66;}} .s span{{font-size:7pt;letter-spacing:.14em;text-transform:uppercase;color:#5A6070;}}
.cols{{display:grid;grid-template-columns:1.15fr 1fr;gap:16px;}}
h3{{font-size:13pt;margin:12px 0 5px;border-bottom:1px solid #E0D9CA;padding-bottom:3px;}}
ul{{padding-left:14px;margin:0;}} li{{margin:2px 0;}}
.p{{border-left:2px solid #F4C020;padding:4px 8px;margin:6px 0;font-size:9.5pt;color:#5A6070;}} .p b{{display:block;color:#232F66;font-family:'Fraunces',Georgia,serif;font-weight:400;font-size:11pt;}}
.pb{{page-break-before:always;}}
.plan{{width:100%;border:1px solid #E0D9CA;border-radius:6px;margin:6px 0 10px;page-break-inside:avoid;}}
.gal{{display:grid;grid-template-columns:1fr 1fr;gap:6px;}} .gal img{{width:100%;height:62mm;object-fit:cover;border-radius:4px;}}
.contact{{margin-top:14px;border-top:1px solid #E0D9CA;padding-top:10px;display:flex;justify-content:space-between;font-size:9pt;}}
.fine{{font-size:7pt;color:#8a8f9c;margin-top:8px;}}
.prov{{font-size:7.5pt;color:#8a8f9c;font-style:italic;}}
.notes{{border-left:2px solid #F4C020;padding:4px 10px;margin:10px 0;}} .notes b{{font-size:7.5pt;letter-spacing:.2em;text-transform:uppercase;color:#232F66;}} .notes p{{font-family:'Fraunces',Georgia,serif;font-size:11pt;margin:3px 0;}} .notes span{{font-size:7.5pt;letter-spacing:.14em;color:#5A6070;}}
</style></head><body>
<div class="top"><img src="img/rbc-logo.png"><div class="r">Technical sheet · {'For rent' if l.get('kind')=='rent' else 'For sale'}<br>{l['where']}</div></div>
<div class="hero"><img src="{ph[0]}"></div>
<div class="eyebrow">{l['status']}{(' · '+l['auth']) if l.get('auth') else ''}</div>
<h1>{l['name']}</h1>
<div class="price">{price_line(l, True)}</div>
<div class="specs">{sp}</div>
<div class="cols">
  <div><h3>The {'space' if l.get('kind')=='rent' else 'house'}</h3><p>{l.get('intro') or l.get('blurb','')}</p>
       {''.join(f"<h3>{k}</h3><p>{l.get(v)}</p>" for k,v in (("Architecture","arch"),("Site","site"),("Materials","materials"),("Condition","condition"),("Potential","potential")) if l.get(v) and l.get(v)!="—")}
       {("<div class='notes'><b>Roberto's Notes</b><p><i>"+l['notes']+"</i></p><span>— R. Balderas Carrillo, Arquitecto</span></div>") if l.get('notes') else ''}
       <h3>At a glance</h3><ul>{hl}</ul></div>
  <div><h3>Program</h3>{prog}
       <h3>Location</h3><p>{l.get('location') or l['where'] + '.'}</p></div>
</div>
<div class="contact"><div><b>Roberto Balderas Carrillo</b> · Arquitecto · RBC, in collaboration with Espacios y Formas<br>WhatsApp +52 461 101 2474 · @arqrobertobalderas · {site_url}</div><div style="text-align:right">{l.get('auth','')}<br>English &amp; Spanish</div></div>
<div class="fine">Prices in MXN; USD figures approximate at prevailing exchange rates. Specifications, availability and delivery subject to change without notice. This sheet is not a binding offer.</div>
<div class="pb"><h2>Plans &amp; gallery</h2>
{plans if plans else '<p class="prov">Floor plans are being prepared for this sheet — request them on WhatsApp.</p>'}
<div class="gal">{gal}</div>
<p class="prov">Provisional images where noted; final photography in progress.</p>
<div class="contact"><div><b>{l['name']}</b> · {l['where']}</div><div>WhatsApp +52 461 101 2474 · {site_url}</div></div>
</div>
</body></html>"""

def build_pdfs(ls, out_dir, site_dir, site_url):
    """Render PDFs with Playwright (Chromium). Skips silently if Playwright is unavailable."""
    import os
    try:
        from playwright.sync_api import sync_playwright
    except Exception:
        print("playwright not available — PDFs skipped"); return
    os.makedirs(os.path.join(out_dir, "pdf"), exist_ok=True)
    tmpdir = os.path.join(site_dir, "_pdfsrc"); os.makedirs(tmpdir, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page()
        for l in ls:
            if not l.get("pdf", True): continue
            src = os.path.join(site_dir, f"_pdf-{l['slug']}.html")
            open(src, "w", encoding="utf-8").write(pdf_html(l, site_url))
            pg.goto("file://" + os.path.abspath(src), wait_until="networkidle")
            pg.pdf(path=os.path.join(out_dir, "pdf", f"{l['slug']}.pdf"), format="A4", print_background=True)
            os.remove(src)
        b.close()
    try: os.rmdir(tmpdir)
    except Exception: pass
    print("pdfs built:", len([l for l in ls if l.get('pdf', True)]))
