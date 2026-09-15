# -*- coding: utf-8 -*-
"""v21: legal pages (privacy notice / aviso de privacidad, terms) and the cookie notice."""
import datetime
TODAY = datetime.date.today().strftime("%B %Y")
EMAIL = "arq.robertbalderas@gmail.com"

def _wrap(title, sub, body_en, body_es):
    return f"""
<header class="phero legal-hero"><div class="in"><div class="tag">RBC / Legal</div><h1>{title}</h1><p class="sub">{sub}</p></div></header>
<section><div class="wrap legal">
  <div class="legal-tabs"><button class="on" data-l="en">English</button><button data-l="es">Español</button></div>
  <div class="legal-body" data-l="en">{body_en}</div>
  <div class="legal-body" data-l="es" hidden>{body_es}</div>
  <p class="cap" style="margin-top:32px;">Last updated · {TODAY}</p>
</div></section>
<script>document.querySelectorAll('.legal-tabs button').forEach(b=>b.addEventListener('click',()=>{{document.querySelectorAll('.legal-tabs button').forEach(x=>x.classList.toggle('on',x===b));document.querySelectorAll('.legal-body').forEach(d=>d.hidden=d.dataset.l!==b.dataset.l);}}));</script>"""

PRIVACY_EN = f"""
<h2>Privacy notice</h2>
<p>In compliance with the Mexican Federal Law on the Protection of Personal Data Held by Private Parties (<i>Ley Federal de Protección de Datos Personales en Posesión de los Particulares</i>, LFPDPPP) and its Regulations, Roberto Balderas Carrillo (“RBC”), with domicile in San Miguel de Allende, Guanajuato, Mexico, is the data controller for the personal data you share through this website and its contact channels.</p>
<h3>1. Data we may receive</h3>
<p>This website does not store your personal data on its own servers and has no user accounts. The forms on this site prepare a message that you send yourself through WhatsApp. When you contact us through WhatsApp, Instagram or e-mail we may receive your name, telephone number, e-mail address, the property or project you are interested in, and the contents of your message. We do not request sensitive personal data or financial data through this website.</p>
<h3>2. Purposes</h3>
<p>Primary purposes: to answer your inquiry, schedule showings or meetings, send information about the properties, developments or services you asked for, and follow up on a purchase, rental, design or construction process. Secondary purposes (you may opt out at any time): to send you information about comparable properties or new projects.</p>
<h3>3. Transfers</h3>
<p>We do not sell or rent your personal data. It may be shared with Espacios y Formas and its sales teams when your inquiry concerns a development they market, with a notary public or legal advisor when a transaction you requested requires it, and with authorities when the law requires it.</p>
<h3>4. ARCO rights and withdrawal of consent</h3>
<p>You may access, rectify, cancel or oppose the processing of your data (ARCO rights), limit its use or withdraw your consent by writing to <a href="mailto:{EMAIL}">{EMAIL}</a>, stating your name, the right you wish to exercise and a means of contact. We answer within the terms set by the LFPDPPP.</p>
<h3>5. Cookies and third-party services</h3>
<p>This website sets no cookies of its own and runs no advertising or analytics trackers. It remembers in your browser only whether you dismissed the cookie notice. Typefaces are served by Google Fonts and the site is hosted by Vercel; both may log technical data such as your IP address under their own privacy policies. WhatsApp and Instagram are governed by Meta’s policies once you leave this site.</p>
<h3>6. Changes</h3>
<p>Updates to this notice are published on this page with the date of the last revision.</p>"""

PRIVACY_ES = f"""
<h2>Aviso de privacidad</h2>
<p>En cumplimiento de la Ley Federal de Protección de Datos Personales en Posesión de los Particulares (LFPDPPP) y su Reglamento, Roberto Balderas Carrillo (“RBC”), con domicilio en San Miguel de Allende, Guanajuato, México, es el responsable del tratamiento de los datos personales que usted proporcione a través de este sitio y de sus medios de contacto.</p>
<h3>1. Datos que podemos recibir</h3>
<p>Este sitio no almacena datos personales en servidores propios ni tiene cuentas de usuario. Los formularios preparan un mensaje que usted mismo envía por WhatsApp. Al contactarnos por WhatsApp, Instagram o correo electrónico podemos recibir su nombre, teléfono, correo electrónico, la propiedad o proyecto de su interés y el contenido de su mensaje. No solicitamos datos personales sensibles ni financieros a través de este sitio.</p>
<h3>2. Finalidades</h3>
<p>Primarias: atender su solicitud, agendar visitas o reuniones, enviarle información de las propiedades, desarrollos o servicios que solicitó y dar seguimiento a un proceso de compra, renta, diseño o construcción. Secundarias (puede oponerse en cualquier momento): enviarle información de propiedades comparables o nuevos proyectos.</p>
<h3>3. Transferencias</h3>
<p>No vendemos ni rentamos sus datos. Pueden compartirse con Espacios y Formas y sus equipos de ventas cuando su solicitud se refiera a un desarrollo que ellos comercializan, con el notario o asesor legal cuando una operación solicitada por usted lo requiera, y con autoridades cuando la ley lo exija.</p>
<h3>4. Derechos ARCO y revocación del consentimiento</h3>
<p>Puede acceder, rectificar, cancelar u oponerse al tratamiento de sus datos (derechos ARCO), limitar su uso o revocar su consentimiento escribiendo a <a href="mailto:{EMAIL}">{EMAIL}</a>, indicando su nombre, el derecho que desea ejercer y un medio de contacto. Respondemos en los plazos que marca la LFPDPPP.</p>
<h3>5. Cookies y servicios de terceros</h3>
<p>Este sitio no instala cookies propias ni usa rastreadores de publicidad o analítica. Solo guarda en su navegador si cerró el aviso de cookies. Las tipografías se sirven desde Google Fonts y el sitio se aloja en Vercel; ambos pueden registrar datos técnicos como su dirección IP conforme a sus propias políticas. WhatsApp e Instagram se rigen por las políticas de Meta al salir de este sitio.</p>
<h3>6. Cambios</h3>
<p>Las actualizaciones a este aviso se publican en esta página con la fecha de la última revisión.</p>"""

TERMS_EN = f"""
<h2>Terms of use and legal notice</h2>
<h3>1. Nature of the information</h3>
<p>This website presents the architectural work of Roberto Balderas Carrillo and a selection of properties and developments he represents or that are marketed by Espacios y Formas. The information is for reference only and does not constitute a binding offer, a promise of sale or lease, professional advice or a technical opinion.</p>
<h3>2. Prices, availability and specifications</h3>
<p>Prices are stated in Mexican pesos unless otherwise indicated; amounts in US dollars are approximate references and depend on the exchange rate on the day of the transaction. Prices, availability, surfaces, specifications, finishes and delivery dates may change without notice and are confirmed only in a written agreement. Some images are renders or provisional photographs, as noted; built results may differ.</p>
<h3>3. Developments and third parties</h3>
<p>Developments such as Peñas Arriba, Magno Home &amp; Towers, La Escondida and La Nueva Escondida are developed and marketed by Espacios y Formas or the entities indicated; their own sales sites, terms and contracts govern any purchase. Links to external websites are provided for convenience.</p>
<h3>4. Intellectual property</h3>
<p>Architectural projects, drawings, renders, photographs, texts and the RBC marks on this site belong to Roberto Balderas Carrillo, Espacios y Formas or their respective authors and may not be reproduced without written permission.</p>
<h3>5. Liability</h3>
<p>We make reasonable efforts to keep the information accurate but do not guarantee that it is free of errors or up to date at all times. Decisions to buy, rent, design or build should be based on the documents delivered in each specific process.</p>
<h3>6. Applicable law</h3>
<p>These terms are governed by the laws of Mexico. Any dispute is subject to the competent courts of San Miguel de Allende, Guanajuato.</p>
<p>Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>. See also our <a href="privacy.html">privacy notice</a>.</p>"""

TERMS_ES = f"""
<h2>Términos de uso y aviso legal</h2>
<h3>1. Naturaleza de la información</h3>
<p>Este sitio presenta la obra arquitectónica de Roberto Balderas Carrillo y una selección de propiedades y desarrollos que él representa o que comercializa Espacios y Formas. La información es de referencia y no constituye una oferta vinculante, promesa de venta o arrendamiento, asesoría profesional ni dictamen técnico.</p>
<h3>2. Precios, disponibilidad y especificaciones</h3>
<p>Los precios se expresan en pesos mexicanos salvo indicación en contrario; los montos en dólares son referencias aproximadas sujetas al tipo de cambio del día de la operación. Precios, disponibilidad, superficies, especificaciones, acabados y fechas de entrega pueden cambiar sin previo aviso y se confirman únicamente en un contrato escrito. Algunas imágenes son renders o fotografías provisionales, según se indica; el resultado construido puede variar.</p>
<h3>3. Desarrollos y terceros</h3>
<p>Desarrollos como Peñas Arriba, Magno Home &amp; Towers, La Escondida y La Nueva Escondida son desarrollados y comercializados por Espacios y Formas o por las entidades indicadas; sus propios sitios de venta, términos y contratos rigen cualquier compra. Los enlaces a sitios externos se ofrecen por conveniencia.</p>
<h3>4. Propiedad intelectual</h3>
<p>Los proyectos, planos, renders, fotografías, textos y marcas RBC de este sitio pertenecen a Roberto Balderas Carrillo, a Espacios y Formas o a sus respectivos autores y no pueden reproducirse sin autorización escrita.</p>
<h3>5. Responsabilidad</h3>
<p>Hacemos esfuerzos razonables por mantener la información correcta, pero no garantizamos que esté libre de errores o actualizada en todo momento. Las decisiones de compra, renta, diseño o construcción deben basarse en los documentos entregados en cada proceso específico.</p>
<h3>6. Ley aplicable</h3>
<p>Estos términos se rigen por las leyes de México. Cualquier controversia se somete a los tribunales competentes de San Miguel de Allende, Guanajuato.</p>
<p>Contacto: <a href="mailto:{EMAIL}">{EMAIL}</a>. Consulte también nuestro <a href="privacy.html">aviso de privacidad</a>.</p>"""

def pages(page, SITE):
    page("privacy", "Privacy notice · Aviso de privacidad | RBC · Roberto Balderas Carrillo",
         "Privacy notice (LFPDPPP) for the website of architect Roberto Balderas Carrillo.",
         _wrap("Privacy notice", "Aviso de privacidad · LFPDPPP", PRIVACY_EN, PRIVACY_ES), "img/hero-casa-jalpa.jpg", None, active="")
    page("terms", "Terms of use · Aviso legal | RBC · Roberto Balderas Carrillo",
         "Terms of use and legal notice for the website of architect Roberto Balderas Carrillo.",
         _wrap("Terms of use", "Aviso legal · Términos de uso", TERMS_EN, TERMS_ES), "img/hero-casa-jalpa.jpg", None, active="")

COOKIE = """
<div class="ck" id="ck" hidden><p>This site sets no cookies of its own. Typefaces are served by Google Fonts and the site is hosted by Vercel, which may log technical data. <a href="privacy.html">Privacy notice</a></p><button class="btn" id="ck-ok">OK</button></div>
<script>(function(){try{if(localStorage.getItem('rbc-ck'))return;}catch(e){}var c=document.getElementById('ck');if(!c)return;c.hidden=false;document.getElementById('ck-ok').addEventListener('click',function(){c.hidden=true;try{localStorage.setItem('rbc-ck','1');}catch(e){}});})();</script>
<script>document.querySelectorAll('.tel-reveal').forEach(function(b){b.addEventListener('click',function(){var n=atob(b.dataset.t);b.outerHTML='<a href="tel:'+n.replace(/\\s/g,'')+'">'+n+'</a>';});});</script>
"""

CSS = r"""
.legal-hero{min-height:40vh;}
.legal{max-width:820px;}
.legal h2{font-size:1.6rem;margin:0 0 18px;} .legal h3{font-size:1rem;margin:26px 0 6px;} .legal p{font-size:.95rem;color:var(--ink-soft);line-height:1.6;}
.legal-tabs{display:flex;gap:4px;margin:0 0 28px;} .legal-tabs button{background:none;border:1px solid var(--line);padding:9px 16px;font-size:.66rem;letter-spacing:.1em;text-transform:uppercase;cursor:pointer;color:var(--ink-soft);}
.legal-tabs button.on{background:#161616;color:#fff;border-color:#161616;}
.ck{position:fixed;left:20px;bottom:20px;z-index:96;max-width:420px;background:#fff;border:1px solid var(--line);padding:16px 18px;box-shadow:0 12px 40px rgba(0,0,0,.14);display:flex;gap:16px;align-items:center;}
.ck p{margin:0;font-size:.78rem;line-height:1.45;color:var(--ink-soft);} .ck p a{color:var(--navy);}
.ck .btn{padding:10px 14px;font-size:.62rem;white-space:nowrap;}
@media(max-width:600px){.ck{left:12px;right:12px;bottom:12px;max-width:none;flex-direction:column;align-items:stretch;}}
.tel-reveal{background:none;border:none;padding:0;font:inherit;color:inherit;text-decoration:underline;cursor:pointer;}
"""
