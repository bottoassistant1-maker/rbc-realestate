# -*- coding: utf-8 -*-
"""Design layer v11 — editorial / technical system per the RBC master brief.
Restraint: hairlines, grid, numbering, editorial type. Motion only where it helps hierarchy or navigation."""

CSS = r"""
/* ═══════════════ RBC v11 · editorial-technical system ═══════════════ */
:root{--ease:cubic-bezier(.2,.7,.2,1);--hair:rgba(35,47,102,.16);--r:3px;--mono:'IBM Plex Mono',ui-monospace,Menlo,monospace;}
html{scroll-behavior:auto;}
body{overflow-x:hidden;}
/* reset the v6 decoration */
.btn{border-radius:var(--r);box-shadow:none;padding:14px 26px;letter-spacing:.14em;transition:background .25s,color .25s,border-color .25s;}
.btn::after{display:none;}
.btn:hover{transform:none;background:var(--navy-deep);}
.btn.red:hover{background:#C93018;}
.btn.ghost{border-width:1px;}
.btn.ghost:hover{background:var(--navy);color:#fff;}
.btn.ghost.lt:hover{background:#fff;color:var(--navy);}
.rv{transform:translateY(14px);transition:opacity .7s var(--ease),transform .7s var(--ease);}
.rv.d1{transition-delay:.08s;}.rv.d2{transition-delay:.16s;}.rv.d3{transition-delay:.24s;}
::selection{background:var(--gold);color:var(--navy-deep);}
.wrap{max-width:1280px;padding:0 32px;}
@media(max-width:700px){.wrap{padding:0 20px;}}
section{padding:88px 0;}
@media(max-width:700px){section{padding:60px 0;}}
h2{font-weight:300;letter-spacing:-.01em;font-size:clamp(1.9rem,3.4vw,2.8rem);font-variation-settings:"opsz" 144;line-height:1.1;}
h3{font-weight:400;}
.lead{font-size:1.05rem;line-height:1.7;}
.eyebrow{font-family:var(--mono);font-size:.68rem;letter-spacing:.14em;text-transform:uppercase;color:var(--navy);font-weight:500;}
.eyebrow::before{display:none;}
.eyebrow b{color:var(--red);font-weight:500;margin-right:10px;}
/* section header line: "01 / Architecture ————" */
.shead{display:grid;grid-template-columns:auto 1fr;gap:18px;align-items:center;margin-bottom:26px;}
.shead .eyebrow{white-space:nowrap;}
.shead i{display:block;height:1px;background:var(--hair);}
/* ── cross-document transitions: a plain fade, nothing more ── */
@view-transition{navigation:auto;}
::view-transition-old(root){animation:vt-out .25s ease both;}
::view-transition-new(root){animation:vt-in .35s ease both;}
@keyframes vt-out{to{opacity:0;}}
@keyframes vt-in{from{opacity:0;}}
nav{view-transition-name:sitenav;}
::view-transition-old(sitenav),::view-transition-new(sitenav){animation:none;}
/* ── NAV ── */
nav{background:var(--paper);backdrop-filter:none;border-bottom:1px solid var(--hair);box-shadow:none;}
nav.scrolled{box-shadow:none;}
nav .in{padding:14px 32px;max-width:1280px;gap:24px;}
@media(max-width:700px){nav .in{padding:12px 20px;}}
nav .brand{display:flex;align-items:center;gap:14px;text-decoration:none;}
nav .brand img{height:30px;}
nav .brand .who{border-left:1px solid var(--hair);padding-left:14px;line-height:1.15;}
nav .brand .who b{display:block;font-family:'Fraunces',serif;font-weight:400;font-size:.92rem;color:var(--navy);letter-spacing:0;}
nav .brand .who span{font-family:var(--mono);font-size:.62rem;letter-spacing:.16em;text-transform:uppercase;color:var(--ink-soft);}
@media(max-width:860px){nav .brand .who{display:none;}}
nav .links{gap:2px;}
nav .links a:not(.cta):not(.sec){position:relative;padding:10px 12px;border-radius:0;font-family:var(--mono);font-size:.68rem;letter-spacing:.14em;color:var(--ink-soft);transition:color .25s;}
nav .links a:not(.cta):not(.sec):hover{color:var(--navy);}
nav .links a.on{color:var(--navy);border-bottom:none;padding-bottom:10px;}
nav .links a.on::after{content:'';position:absolute;left:12px;right:12px;bottom:4px;height:2px;background:var(--gold);}
nav .links .ind{display:none;}
nav .links .sep{display:none;}
nav .links a.sec{font-family:var(--mono);font-size:.66rem;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-soft);padding:10px 8px;}
nav .links a.sec.on{color:var(--navy);text-decoration:none;}
nav .links a.cta{display:none;margin-left:10px;padding:10px 16px;border-radius:var(--r);box-shadow:none;background:var(--navy);font-family:var(--mono);font-size:.66rem;letter-spacing:.14em;transition:background .25s;}
nav .links a.cta:hover{background:var(--red);transform:none;box-shadow:none;}
nav .links .lang{font-family:var(--mono);font-size:.64rem;letter-spacing:.12em;color:var(--ink-soft);padding:10px 8px;text-decoration:none;}
nav .links .lang b{color:var(--navy);font-weight:500;}
nav .burger{border-radius:var(--r);}
/* ── HERO ── */
.hero{min-height:82vh;align-items:flex-end;}
.hero::before,.phero::before{display:none;}
.hero::after{background:linear-gradient(180deg,rgba(22,30,69,0) 40%,rgba(22,30,69,.72) 100%);}
.hero .bg{animation:none;}
.hero .in{padding:0 32px 44px;max-width:1280px;}
.hero .in>*{opacity:1;transform:none;animation:none;}
.hero .tag{font-family:var(--mono);font-size:.66rem;letter-spacing:.16em;color:#fff;opacity:.85;}
.hero h1{font-weight:300;letter-spacing:-.02em;font-size:clamp(2.2rem,5.2vw,4.4rem);line-height:1.02;margin:10px 0 8px;max-width:900px;}
.hero h1 em{font-style:italic;font-weight:300;color:var(--gold);}
.hero p.sub{max-width:560px;font-size:1rem;}
.hero .pricebar{margin-top:20px;}
.hero .scrollcue{display:none;}
.hero .badge{border-radius:var(--r);font-family:var(--mono);letter-spacing:.14em;}
/* WHO / WHAT / WHERE / WHY strip */
.wwww{border-top:1px solid var(--hair);border-bottom:1px solid var(--hair);background:var(--paper);}
.wwww .in{max-width:1280px;margin:0 auto;padding:0 32px;display:grid;grid-template-columns:repeat(4,1fr);}
@media(max-width:900px){.wwww .in{grid-template-columns:1fr 1fr;}}
@media(max-width:520px){.wwww .in{grid-template-columns:1fr;}}
.wwww div{padding:22px 22px 22px 0;border-right:1px solid var(--hair);margin-right:22px;}
.wwww div:last-child{border-right:none;}
@media(max-width:900px){.wwww div:nth-child(2){border-right:none;}}
.wwww small{display:block;font-family:var(--mono);font-size:.62rem;letter-spacing:.16em;text-transform:uppercase;color:var(--red);margin-bottom:6px;}
.wwww b{display:block;font-family:'Fraunces',serif;font-weight:400;font-size:1.15rem;color:var(--navy);line-height:1.2;}
.wwww span{display:block;font-size:.84rem;color:var(--ink-soft);margin-top:3px;}
/* ── interior page hero ── */
.phero{min-height:54vh;background:var(--navy-deep);}
.phero::after{background:linear-gradient(180deg,rgba(22,30,69,.2) 0%,rgba(22,30,69,.75) 100%);}
.phero .bg{animation:none;}
.phero .in{padding:120px 32px 44px;max-width:1280px;}
.phero .in>*{opacity:1;transform:none;animation:none;}
.phero .tag{font-family:var(--mono);font-size:.66rem;letter-spacing:.16em;color:#fff;opacity:.85;}
.phero h1{font-weight:300;letter-spacing:-.02em;font-size:clamp(2rem,4.4vw,3.6rem);line-height:1.04;}
.crumbs{font-family:var(--mono);font-size:.62rem;letter-spacing:.12em;}
/* ── areas (01/02/03) ── */
.areas{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--hair);}
@media(max-width:860px){.areas{grid-template-columns:1fr;}}
.area{padding:30px 28px 34px 0;border-bottom:1px solid var(--hair);text-decoration:none;color:var(--ink);display:block;position:relative;}
.area+.area{border-left:1px solid var(--hair);padding-left:28px;}
@media(max-width:860px){.area+.area{border-left:none;padding-left:0;}}
.area .n{font-family:var(--mono);font-size:.66rem;letter-spacing:.16em;color:var(--red);}
.area h3{font-family:'Fraunces',serif;font-size:1.8rem;font-weight:300;margin:8px 0 10px;color:var(--navy);}
.area p{font-size:.94rem;color:var(--ink-soft);line-height:1.6;}
.area .im{margin:18px 0 12px;aspect-ratio:4/3;overflow:hidden;background:var(--paper-2);}
.area .im img{width:100%;height:100%;object-fit:cover;transition:transform .9s var(--ease);}
.area:hover .im img{transform:scale(1.04);}
.area .go{font-family:var(--mono);font-size:.66rem;letter-spacing:.16em;text-transform:uppercase;color:var(--navy);}
.area:hover .go{color:var(--red);}
/* ── stats: thin ── */
.stats{background:var(--paper);color:var(--navy);border-bottom:1px solid var(--hair);}
.stats .in{padding:26px 32px;max-width:1280px;gap:0;}
.stats .n{font-size:2rem;font-weight:300;color:var(--navy);}
.stats .l{color:var(--ink-soft);font-family:var(--mono);letter-spacing:.14em;}
.stats>.in>div{border-right:1px solid var(--hair);}
.stats>.in>div:last-child{border-right:none;}
/* ── cards, generic ── */
.lcard,.step,.form,.soon,.dev,.proj,.fs{border-radius:var(--r);box-shadow:none;}
.lcard:hover,.step:hover,.fs:hover,.dev:hover{transform:none;box-shadow:none;}
.step{border-top:1px solid var(--navy);border-left:none;border-right:none;border-bottom:none;background:transparent;padding:18px 0;}
.step .k{font-family:var(--mono);font-size:.7rem;letter-spacing:.14em;color:var(--red);}
.steps{gap:28px;}
.form{border:1px solid var(--hair);}
.form input,.form select,.form textarea{border-radius:var(--r);}
.form label{font-family:var(--mono);letter-spacing:.12em;}
.mapimg{border-radius:var(--r);box-shadow:none;border:1px solid var(--hair);}
a:hover>.mapimg{transform:none;box-shadow:none;}
.checks li::before{content:'—';}
.cap{font-family:var(--mono);letter-spacing:.1em;font-size:.64rem;}
/* ── contact band: flat navy ── */
.contact{background:var(--navy);}
.contact::before{display:none;}
.contact h2{font-size:clamp(1.9rem,3.6vw,3rem);}
/* ── footer ── */
footer{background:var(--navy-deep);padding:56px 0 30px;}
footer .word{display:none;}
footer .cols{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:28px;padding-bottom:28px;border-bottom:1px solid rgba(255,255,255,.1);}
@media(max-width:860px){footer .cols{grid-template-columns:1fr 1fr;}}
@media(max-width:520px){footer .cols{grid-template-columns:1fr;}}
footer .cols small{display:block;font-family:var(--mono);font-size:.62rem;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);margin-bottom:10px;}
footer .cols a{display:block;color:rgba(255,255,255,.75);text-decoration:none;font-size:.86rem;padding:3px 0;}
footer .cols a:hover{color:#fff;}
footer .cols p{font-size:.86rem;color:rgba(255,255,255,.7);line-height:1.6;max-width:360px;}
footer .cols .seal{font-family:'Fraunces',serif;font-size:1.6rem;color:#fff;font-weight:300;line-height:1;}
footer .cols .seal span{display:block;font-family:var(--mono);font-size:.62rem;letter-spacing:.16em;text-transform:uppercase;color:rgba(255,255,255,.55);margin-top:6px;}
footer .row{border-top:none;padding-top:18px;}
/* ── mobile menu: flat ── */
.mnav{background:var(--navy-deep);transform:translateY(-100%);display:flex;transition:transform .45s var(--ease);}
.mnav.on{transform:none;}
.mnav a{font-size:1.9rem;font-weight:300;}
.mnav a small{font-family:var(--mono);color:var(--gold);}
.mnav a.msec{font-family:var(--mono);font-size:.8rem;letter-spacing:.16em;text-transform:uppercase;color:rgba(255,255,255,.75);border-bottom:none;padding:8px 0;}
.mnav a.btn{font-family:var(--mono);font-size:.74rem;font-weight:500;border-bottom:none;padding:16px 28px;}
/* ── project codes ── */
.code{font-family:var(--mono);font-size:.62rem;letter-spacing:.12em;color:var(--ink-soft);}
/* ── WA float: quieter ── */
.wa-float{border-radius:var(--r);box-shadow:none;font-size:.78rem;padding:11px 16px;font-family:var(--mono);letter-spacing:.08em;}
/* ── development brand cards ── */
.devs{display:grid;gap:34px;margin-top:34px;}
.dev{background:transparent;border:none;border-top:1px solid var(--navy);overflow:visible;}
.dev-car{margin:22px 0 0;}
.dev-bd{padding:22px 0 8px;}
.dev-meta{display:flex;justify-content:space-between;font-family:var(--mono);font-size:.64rem;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-soft);}
.dev h3{font-size:2rem;font-weight:300;margin:6px 0 10px;}
.dev p{font-size:.96rem;color:var(--ink-soft);line-height:1.65;max-width:900px;}
.dev-cta{display:flex;gap:10px;flex-wrap:wrap;margin-top:18px;}
.car .sl{border-radius:var(--r);}
.car .arr{border-radius:var(--r);box-shadow:none;width:42px;height:42px;background:var(--paper);}
.car .dots i.on{background:var(--navy);}
/* ── intent tiles (contact) ── */
.intents{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border-top:1px solid var(--hair);border-left:1px solid var(--hair);margin-top:26px;}
@media(max-width:900px){.intents{grid-template-columns:1fr 1fr;}}
@media(max-width:520px){.intents{grid-template-columns:1fr;}}
.intent{border-right:1px solid var(--hair);border-bottom:1px solid var(--hair);padding:24px 22px 26px;text-decoration:none;color:var(--ink);display:block;transition:background .25s;}
.intent:hover{background:#fff;}
.intent small{font-family:var(--mono);font-size:.62rem;letter-spacing:.16em;text-transform:uppercase;color:var(--red);}
.intent b{display:block;font-family:'Fraunces',serif;font-weight:400;font-size:1.35rem;color:var(--navy);margin:8px 0 6px;}
.intent span{font-size:.86rem;color:var(--ink-soft);line-height:1.5;}
/* ── notes block (Roberto's Notes) ── */
.notes{border-left:2px solid var(--gold);padding:6px 0 6px 18px;margin:18px 0;}
.notes small{display:block;font-family:var(--mono);font-size:.62rem;letter-spacing:.16em;text-transform:uppercase;color:var(--navy);margin-bottom:6px;}
.notes p{font-family:'Fraunces',serif;font-size:1.08rem;line-height:1.5;color:var(--ink);font-style:italic;font-weight:300;}
.notes .sig{font-family:var(--mono);font-size:.62rem;letter-spacing:.14em;color:var(--ink-soft);margin-top:8px;font-style:normal;}
/* ═══════════════ v12 · architect-first additions ═══════════════ */
/* home hero: image first, three lines of type */
.hero.home{min-height:86vh;align-items:flex-end;}
.hero.home .bg{background-position:center 58%;}
.hero.home .in{padding:0 32px 56px;max-width:1280px;}
.hero.home .rbc{font-family:var(--mono);font-size:.7rem;letter-spacing:.3em;color:#fff;opacity:.9;}
.hero.home h1{font-size:clamp(2.4rem,6vw,5.2rem);margin:14px 0 4px;letter-spacing:-.025em;max-width:none;}
.hero.home .role{font-family:'Fraunces',serif;font-style:italic;font-weight:300;font-size:clamp(1.5rem,3vw,2.4rem);color:var(--gold);line-height:1.1;}
.hero.home p.sub{margin-top:22px;max-width:520px;font-size:1.02rem;opacity:.95;}
.hero.home .meta{display:flex;justify-content:space-between;gap:18px;flex-wrap:wrap;margin-top:34px;padding-top:16px;border-top:1px solid rgba(255,255,255,.35);font-family:var(--mono);font-size:.64rem;letter-spacing:.16em;text-transform:uppercase;color:rgba(255,255,255,.85);}
.hero.home .meta a{color:#fff;text-decoration:none;}
.hero.home .meta a:hover{color:var(--gold);}
.hero.home::after{background:linear-gradient(180deg,rgba(22,30,69,0) 45%,rgba(22,30,69,.7) 100%);}
@media(max-width:700px){.hero.home{min-height:86vh;}.hero.home .in{padding:0 20px 40px;}}
/* selected work: large images, one line each */
.swgrid{display:grid;grid-template-columns:repeat(6,1fr);gap:22px 22px;margin-top:34px;}
.sw{grid-column:span 2;text-decoration:none;color:var(--ink);display:block;}
.sw.sw-lead{grid-column:span 6;}
.sw:nth-child(2),.sw:nth-child(3){grid-column:span 3;}
.sw figure{margin:0;position:relative;overflow:hidden;background:var(--paper-2);aspect-ratio:4/3;}
.sw.sw-lead figure{aspect-ratio:21/9;}
.sw:nth-child(2) figure,.sw:nth-child(3) figure{aspect-ratio:3/2;}
.sw figure img{width:100%;height:100%;object-fit:cover;display:block;transition:transform 1.2s var(--ease);}
.sw:hover figure img{transform:scale(1.025);}
.sw .prov{position:absolute;top:10px;left:10px;font-family:var(--mono);font-size:.56rem;letter-spacing:.14em;text-transform:uppercase;color:#fff;background:rgba(22,30,69,.7);padding:4px 8px;}
.sw-cap{display:grid;grid-template-columns:auto 1fr;gap:4px 14px;align-items:baseline;padding:12px 0 0;}
.sw.sw-lead .sw-cap,.sw:nth-child(2) .sw-cap,.sw:nth-child(3) .sw-cap{grid-template-columns:auto 1fr auto;}
.sw-cap .cd{font-family:var(--mono);font-size:.62rem;letter-spacing:.14em;color:var(--red);}
.sw-cap b{font-family:'Fraunces',serif;font-weight:400;font-size:1.15rem;color:var(--navy);}
.sw.sw-lead .sw-cap b{font-size:1.6rem;}
.sw-cap span:last-child{font-family:var(--mono);font-size:.62rem;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-soft);text-align:right;}
.sw:nth-child(n+4) .sw-cap span:last-child{grid-column:1/-1;text-align:left;}
@media(max-width:900px){.swgrid{grid-template-columns:1fr 1fr;gap:18px;}.sw,.sw.sw-lead,.sw:nth-child(2),.sw:nth-child(3){grid-column:span 2;}.sw figure,.sw.sw-lead figure,.sw:nth-child(2) figure,.sw:nth-child(3) figure{aspect-ratio:3/2;}}
@media(min-width:901px){.sw:nth-child(n+4){grid-column:span 2;}}
/* practice: definition list */
.practice{display:grid;grid-template-columns:1fr 1.2fr;gap:44px;align-items:start;}
@media(max-width:860px){.practice{grid-template-columns:1fr;}}
.caps{border-top:1px solid var(--navy);margin-top:8px;}
.caps div{display:grid;grid-template-columns:150px 1fr;gap:18px;padding:14px 0;border-bottom:1px solid var(--hair);}
@media(max-width:520px){.caps div{grid-template-columns:1fr;gap:4px;}}
.caps small{font-family:var(--mono);font-size:.64rem;letter-spacing:.16em;text-transform:uppercase;color:var(--navy);padding-top:3px;}
.caps span{font-size:.94rem;color:var(--ink-soft);line-height:1.55;}
.scale{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-top:26px;font-family:var(--mono);font-size:.64rem;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-soft);border-top:1px solid var(--hair);padding-top:12px;}
/* construction / EyF band */
.eyf{display:grid;grid-template-columns:1.1fr 1fr;gap:44px;align-items:center;}
@media(max-width:860px){.eyf{grid-template-columns:1fr;}}
.eyf figure{margin:0;aspect-ratio:4/3;overflow:hidden;background:var(--paper-2);}
.eyf figure img{width:100%;height:100%;object-fit:cover;display:block;}
.facts{border-top:1px solid var(--navy);margin-top:22px;}
.facts div{display:grid;grid-template-columns:170px 1fr;gap:16px;padding:10px 0;border-bottom:1px solid var(--hair);font-size:.9rem;}
.facts small{font-family:var(--mono);font-size:.62rem;letter-spacing:.16em;text-transform:uppercase;color:var(--navy);padding-top:3px;}
@media(max-width:520px){.facts div{grid-template-columns:1fr;gap:2px;}}
/* construction index table */
.ctab{border-top:1px solid var(--navy);margin-top:26px;}
.ctab a,.ctab div.r{display:grid;grid-template-columns:90px 1.4fr 1fr 1fr;gap:16px;padding:14px 0;border-bottom:1px solid var(--hair);text-decoration:none;color:var(--ink);font-size:.94rem;transition:background .2s;}
.ctab a:hover{background:#fff;}
.ctab .cd{font-family:var(--mono);font-size:.62rem;letter-spacing:.14em;color:var(--red);padding-top:4px;}
.ctab b{font-family:'Fraunces',serif;font-weight:400;font-size:1.1rem;color:var(--navy);}
.ctab span{color:var(--ink-soft);}
.ctab em{font-family:var(--mono);font-style:normal;font-size:.62rem;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-soft);text-align:right;padding-top:4px;}
@media(max-width:700px){.ctab a,.ctab div.r{grid-template-columns:1fr;gap:3px;}.ctab em{text-align:left;}}
/* property page */
.hero.prop{min-height:72vh;}
.pp-bar{border-bottom:1px solid var(--hair);background:var(--paper);}
.pp-bar .in{max-width:1280px;margin:0 auto;padding:18px 32px;display:grid;grid-template-columns:1.2fr 1fr 1.4fr auto;gap:22px;align-items:center;}
@media(max-width:900px){.pp-bar .in{grid-template-columns:1fr 1fr;}}
@media(max-width:520px){.pp-bar .in{grid-template-columns:1fr;padding:18px 20px;}}
.pp-price{font-family:'Fraunces',serif;font-size:1.7rem;font-weight:300;color:var(--navy);}
.pp-price small{font-family:var(--mono);font-size:.68rem;letter-spacing:.1em;color:var(--ink-soft);}
.pp-auth{font-size:.9rem;color:var(--ink);}
.pp-auth small{display:block;font-family:var(--mono);font-size:.6rem;letter-spacing:.16em;text-transform:uppercase;color:var(--red);margin-bottom:3px;}
.pp-bar .btn{margin:0;white-space:nowrap;}
.pp-sec{padding:12px 0;border-bottom:1px solid var(--hair);}
.pp-sec small{display:block;font-family:var(--mono);font-size:.62rem;letter-spacing:.16em;text-transform:uppercase;color:var(--navy);margin-bottom:5px;}
.pp-sec p{font-size:.94rem;color:var(--ink-soft);line-height:1.6;}
.pp-plans{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:22px;}
@media(max-width:700px){.pp-plans{grid-template-columns:1fr;}}
.pp-plans img{width:100%;border:1px solid var(--hair);background:#fff;display:block;}
.fs-auth{font-family:var(--mono);font-size:.62rem;letter-spacing:.12em;text-transform:uppercase;color:var(--red);margin-top:6px;}
.notes .draft,.draft{font-family:var(--mono);font-style:normal;font-size:.56rem;letter-spacing:.12em;text-transform:uppercase;color:var(--red);border:1px solid var(--red);padding:2px 6px;margin-left:8px;vertical-align:middle;}
/* about */
.about{display:grid;grid-template-columns:1fr 1.5fr;gap:44px;align-items:start;}
@media(max-width:860px){.about{grid-template-columns:1fr;}}
.portrait{aspect-ratio:4/5;background:var(--paper-2);border:1px solid var(--hair);display:flex;align-items:flex-end;padding:18px;font-family:var(--mono);font-size:.64rem;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-soft);}
.about h2{font-size:clamp(1.7rem,2.8vw,2.4rem);margin-bottom:14px;}
.about .lead+.lead{margin-top:12px;}
/* ── three doors (v13) ── */
.doors{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:40px;}
@media(max-width:860px){.doors{grid-template-columns:1fr;}}
.door{position:relative;display:block;aspect-ratio:4/5;overflow:hidden;background:var(--navy-deep);text-decoration:none;color:#fff;}
@media(max-width:860px){.door{aspect-ratio:16/9;}}
.door img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform 1.2s var(--ease);opacity:.92;}
.door:hover img{transform:scale(1.03);}
.door::after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(22,30,69,0) 45%,rgba(22,30,69,.82) 100%);}
.door-t{position:absolute;left:0;right:0;bottom:0;padding:22px 24px;z-index:2;}
.door-t small{display:block;font-family:var(--mono);font-size:.62rem;letter-spacing:.18em;color:var(--gold);margin-bottom:6px;}
.door-t b{display:block;font-family:'Fraunces',serif;font-weight:300;font-size:2.2rem;line-height:1;letter-spacing:-.01em;}
.door-t span{display:block;margin-top:8px;font-size:.88rem;color:rgba(255,255,255,.85);}
/* ── development brand cards (v13) ── */
.dev2 .dev-row{display:grid;grid-template-columns:200px 1fr;gap:28px;align-items:start;}
@media(max-width:700px){.dev2 .dev-row{grid-template-columns:1fr;}}
.dev2 .dev-brand img{max-width:170px;max-height:80px;object-fit:contain;display:block;}
.dev2 .dev-brand b{font-family:'Fraunces',serif;font-weight:300;font-size:1.6rem;color:var(--navy);line-height:1.1;display:block;}
.dev2 .dev-meta{margin-bottom:8px;}
.dev2 p{font-size:.94rem;}
.dev2 .dev-car.h520{height:420px;overflow:hidden;}
.dev2 .dev-car .trk{height:100%;padding-bottom:0;}
.dev2 .dev-car .sl{height:100%;}
.dev2 .dev-car .dots{position:absolute;bottom:12px;left:0;right:0;margin:0;}
@media(max-width:700px){.dev2 .dev-car.h520{height:260px;}}
.dev2 .car .sl img{width:100%;height:100%;object-fit:cover;}
/* intents: shorter */
.intent b{font-size:1.15rem;}
/* v15 */
.lead.big{font-family:'Fraunces',serif;font-weight:300;font-size:clamp(1.35rem,2.2vw,1.8rem);line-height:1.35;color:var(--navy);margin-bottom:16px;}
.portrait.sm{aspect-ratio:4/5;max-width:360px;}
img.portrait{object-fit:cover;width:100%;display:block;padding:0;border:none;}
.doors3 .door{aspect-ratio:3/4;}
.doors3 .door-t b{font-size:2.6rem;}
@media(max-width:860px){.doors3 .door{aspect-ratio:16/10;}}
nav .links a:not(.cta):not(.sec){font-size:.72rem;}
/* ═══════ v16 · one grotesk, editorial restraint (refs: Reed Hilderbrand · dmb · BIG) ═══════ */
:root{--sans:'Instrument Sans','Helvetica Neue',Helvetica,Arial,sans-serif;--mono:var(--sans);}
html,body,button,input,select,textarea{font-family:var(--sans);}
body{color:#161616;}
h1,h2,h3,h4,.serif,.hero h1,.phero h1,.hero.home .role,.lead.big,.notes p,.sw-cap b,.reel-cap b,.door-t b,.intent b,.dev h3,.dev2 .dev-brand b,.fs h3,.fb-head h2,.pp-price,.stats .n,.area h3,.wwww b,nav .brand .who b,footer .cols .seal,.form h3{font-family:var(--sans);font-style:normal;}
h2{font-weight:400;letter-spacing:-.02em;font-size:clamp(1.6rem,2.6vw,2.2rem);line-height:1.15;}
h3{font-weight:500;}
.hero h1,.phero h1,.hero.home h1{font-weight:500;letter-spacing:-.03em;}
.hero.home h1{font-size:clamp(2.2rem,5vw,4.4rem);}
.hero.home .role{font-weight:400;font-style:normal;color:#fff;opacity:.9;font-size:clamp(1.1rem,1.8vw,1.5rem);letter-spacing:.02em;}
.hero.home .rbc,.hero.home .meta,.eyebrow,.code,.cap,.tag,.crumbs,.sw-cap .cd,.sw-cap span:last-child,.reel-cap .cd,.reel-cap>span:last-child,.reel-cap a,.fs-where,.fs-auth,.fs-open,.fs-st,.dev-meta,.door-t small,.intent small,.caps small,.facts small,.pp-auth small,.pp-sec small,.notes small,.stats .l,.form label,footer .cols small,.scale,.wwww small,nav .brand .who span,.provnote{font-family:var(--sans);font-weight:500;font-size:.66rem;letter-spacing:.1em;text-transform:uppercase;}
.eyebrow b{font-weight:500;}
.lead{font-size:1rem;line-height:1.65;}
.lead.big{font-weight:400;font-size:clamp(1.25rem,2vw,1.6rem);letter-spacing:-.01em;line-height:1.35;color:#161616;}
.notes p{font-style:normal;font-weight:400;font-size:1rem;line-height:1.55;}
.notes{border-left:1px solid #161616;}
nav .links a:not(.cta):not(.sec){font-family:var(--sans);font-weight:500;font-size:.7rem;letter-spacing:.1em;color:#161616;}
nav .links a.on::after{background:#161616;}
nav .links a.cta{font-family:var(--sans);font-weight:500;font-size:.68rem;letter-spacing:.1em;background:#161616;}
nav .links a.cta:hover{background:var(--red);}
nav .brand .who b{font-weight:500;font-size:.88rem;letter-spacing:-.01em;}
.btn{font-family:var(--sans);font-weight:500;font-size:.68rem;letter-spacing:.1em;border-radius:0;padding:13px 22px;}
.btn.ghost{border:1px solid #161616;color:#161616;}
.btn.ghost:hover{background:#161616;color:#fff;}
.btn:not(.ghost):not(.red){background:#161616;}
.btn.red{background:#161616;} .btn.red:hover{background:var(--red);}
.shead i{background:rgba(22,22,22,.18);}
.shead .eyebrow b{color:#161616;margin-right:8px;}
.eyebrow{color:#161616;}
.sw-cap .cd,.reel-cap .cd{color:#8a8a8a;}
.sw-cap b{font-weight:500;font-size:1rem;} .sw.sw-lead .sw-cap b{font-size:1.25rem;}
.reel-cap b{font-weight:500;font-size:.95rem;} .reel.big .reel-cap b{font-size:1.15rem;}
.door-t b{font-weight:500;letter-spacing:-.02em;font-size:2rem;} .doors3 .door-t b{font-size:2.2rem;}
.door-t small{color:#fff;opacity:.7;}
.fs h3{font-weight:500;font-size:1.05rem;} .fs-pr{font-family:var(--sans);font-weight:500;color:#161616;}
.fs-pr small{font-weight:400;color:#8a8a8a;}
.fs-auth{color:#8a8a8a;}
.dev h3,.dev2 .dev-brand b{font-weight:500;font-size:1.4rem;letter-spacing:-.02em;}
.pp-price{font-weight:500;font-size:1.5rem;letter-spacing:-.02em;}
.stats .n{font-weight:500;font-size:1.6rem;letter-spacing:-.02em;}
.fb-head h2{font-weight:500;}
.contact h2{font-weight:400;letter-spacing:-.02em;}
footer .cols .seal{font-weight:500;letter-spacing:-.02em;}
.hero.home .role{font-family:var(--sans);}
.hero .tag,.phero .tag{opacity:.75;}
.wa-float{font-family:var(--sans);font-weight:500;font-size:.68rem;letter-spacing:.1em;border-radius:0;}
.draft{font-family:var(--sans);}
.intents .intent b{font-weight:500;font-size:1rem;letter-spacing:-.01em;}
"""

CURTAIN_HTML = ""

JS = r"""
<script>
(function(){
  // Line-break hero headline into rows so the italic emphasis reads cleanly — no animation.
  // Scroll: mark nav when past hero (already handled).
  // Nothing else: motion in v11 is limited to reveal-on-scroll and slider transitions.
})();
</script>
"""

CSS += r"""
/* ── v17: the three disciplines carry the three logo colours ── */
:root{--c-arch:#E8402A;--c-re:#232F66;--c-con:#F4C020;}
nav .links a.d-arch,nav .links a.d-re,nav .links a.d-con{padding-top:12px;}
nav .links a.d-arch::before,nav .links a.d-re::before,nav .links a.d-con::before{content:'';position:absolute;left:12px;right:12px;top:0;height:3px;opacity:.9;}
nav .links a.d-arch::before{background:var(--c-arch);} nav .links a.d-re::before{background:var(--c-re);} nav .links a.d-con::before{background:var(--c-con);}
nav .links a.d-arch.on::after{background:var(--c-arch);} nav .links a.d-re.on::after{background:var(--c-re);} nav .links a.d-con.on::after{background:var(--c-con);}
nav .links a.d-arch:hover{color:var(--c-arch);} nav .links a.d-re:hover{color:var(--c-re);} nav .links a.d-con:hover{color:#b98900;}
.mnav a.d-arch small{color:var(--c-arch);} .mnav a.d-re small{color:#8fa0e6;} .mnav a.d-con small{color:var(--c-con);}
.mnav a.d-arch,.mnav a.d-re,.mnav a.d-con{border-left:4px solid;padding-left:14px;}
.mnav a.d-arch{border-color:var(--c-arch);} .mnav a.d-re{border-color:#8fa0e6;} .mnav a.d-con{border-color:var(--c-con);}
/* home doors */
.doors3 .door::before{content:'';position:absolute;left:0;right:0;top:0;height:8px;z-index:3;}
.doors3 .door:nth-child(1)::before{background:var(--c-arch);} .doors3 .door:nth-child(2)::before{background:var(--c-re);} .doors3 .door:nth-child(3)::before{background:var(--c-con);}
.doors3 .door::after{background:linear-gradient(180deg,rgba(0,0,0,0) 45%,rgba(0,0,0,.72) 100%);}
.doors3 .door-t small{opacity:1;display:inline-block;padding:4px 8px;font-weight:600;}
.doors3 .door:nth-child(1) .door-t small{background:var(--c-arch);color:#fff;} .doors3 .door:nth-child(2) .door-t small{background:var(--c-re);color:#fff;} .doors3 .door:nth-child(3) .door-t small{background:var(--c-con);color:#161616;}
/* section pages: hero tag + section numbers in the discipline colour */
body.pg-arch .phero .tag,body.pg-arch .eyebrow b{color:var(--c-arch);opacity:1;}
body.pg-re .phero .tag,body.pg-re .eyebrow b{color:#8fa0e6;opacity:1;} body.pg-re .eyebrow b{color:var(--c-re);}
body.pg-con .phero .tag,body.pg-con .eyebrow b{color:var(--c-con);opacity:1;} body.pg-con .eyebrow b{color:#b98900;}
body.pg-arch .phero{border-top:8px solid var(--c-arch);} body.pg-re .phero{border-top:8px solid var(--c-re);} body.pg-con .phero{border-top:8px solid var(--c-con);}
"""
CSS += r"""
/* v18: RBC monogram, larger and present */
nav .brand img{height:38px;}
@media(max-width:600px){nav .brand img{height:32px;}}
.hero.home .rbc-mark{display:block;height:64px;width:auto;margin-bottom:22px;}
.mnav .top img{height:40px;}
.phero .in::before{content:'';display:block;width:64px;height:24px;background:url(img/rbc-mono-white.png) left center/contain no-repeat;margin-bottom:14px;opacity:.95;}
"""
CSS += r"""
nav .links a.lang{display:inline-block;}
.mnav a.btn{display:none;}
"""
