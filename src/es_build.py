# -*- coding: utf-8 -*-
"""v23 — builds the Spanish site into <OUT>/es/ from the English pages already built.
Text nodes, alt/title/placeholder/aria-label, <title>, meta descriptions, the FICHAS JSON and a few
JS literals are translated with es.T; asset paths are re-based to ../; the EN/ES switch links both ways."""
import os, re, json
from bs4 import BeautifulSoup, Comment, NavigableString
import es

ASSET_RE = re.compile(r'^(img|pdf)/')
JS_LITERALS = [
    ('>Photos</button>', '>Fotos</button>'), ('>Plans</button>', '>Plantas</button>'),
    ("<h4>Available units</h4>", "<h4>Unidades disponibles</h4>"),
    ("'<h4>The '+(d.kind==='rent'?'space':'house')+'</h4>", "'<h4>'+(d.kind==='rent'?'El espacio':'La casa')+'</h4>"),
    ("'<h4>At a glance</h4>", "'<h4>De un vistazo</h4>"), ("'<h4>Location</h4>", "'<h4>Ubicación</h4>"),
    ("'<h4>Program</h4>", "'<h4>Programa</h4>"), ("'<h4>Plans</h4>", "'<h4>Plantas</h4>"),
    ("Floor plans and the full technical sheet are available on request or in the PDF.", "Plantas y ficha técnica completa disponibles a solicitud o en el PDF."),
    (">Request information on WhatsApp<", ">Solicitar información por WhatsApp<"),
    (">Full sheet (PDF)<", ">Ficha completa (PDF)<"), (">Open full page<", ">Abrir página completa<"),
    ("Prices in MXN; USD approximate. Images provisional where noted.", "Precios en MXN; USD aproximado. Imágenes provisionales donde se indica."),
    ("'Previous'", "'Anterior'"), ("'Next'", "'Siguiente'"),
    ("<h4>About the project</h4>", "<h4>Sobre el proyecto</h4>"), (">This house is for sale →<", ">Esta casa está en venta →<"),
    (">View on Instagram<", ">Ver en Instagram<"), (">Ask about this project<", ">Preguntar por este proyecto<"),
]
SKIP_KEYS = {"photos", "plans", "wa", "pdf", "page", "links", "ig", "sale", "code", "m2"}

def _tr_json(o):
    if isinstance(o, str): return es.tr(o)
    if isinstance(o, list): return [_tr_json(v) for v in o]
    if isinstance(o, dict):
        out = {}
        for k, v in o.items():
            if k == "photos" or k == "plans": out[k] = ["../" + p if ASSET_RE.match(p) else p for p in v]
            elif k == "pdf": out[k] = ("../" + v) if v else v
            elif k == "links": out[k] = [[es.tr(a), b] for a, b in v]
            elif k in SKIP_KEYS: out[k] = v
            else: out[k] = _tr_json(v)
        return out
    return o

def _fix_url(u):
    if not u or u.startswith(("http", "mailto:", "tel:", "#", "data:")): return u
    if ASSET_RE.match(u): return "../" + u
    return u  # x.html stays relative inside es/

def build_es(OUT, SITE_URL, pages):
    os.makedirs(os.path.join(OUT, "es"), exist_ok=True)
    for slug in pages:
        src = os.path.join(OUT, f"{slug}.html")
        if not os.path.exists(src): continue
        html = open(src, encoding="utf-8").read()
        # JS literals inside scripts / JSON
        for a, b in JS_LITERALS: html = html.replace(a, b)
        for var in ("FICHAS", "PROJ"):
            m = re.search(r'window\.' + var + r'=Object\.assign\(window\.' + var + r'\|\|\{\},(\{.*?\})\);</script>', html, re.S)
            if m:
                d = json.loads(m.group(1))
                html = html[:m.start(1)] + json.dumps(_tr_json(d), ensure_ascii=False) + html[m.end(1):]
        # remove the old google-translate hook
        html = re.sub(r"<script>document\.querySelectorAll\('\[data-lang\]'\).*?</script>\n?", "", html, flags=re.S)
        s = BeautifulSoup(html, "html.parser")
        if s.html is None or s.head is None or s.body is None: continue  # not a site page (e.g. verification file)
        s.html["lang"] = "es"
        # text nodes
        for t in list(s.find_all(string=True)):
            if isinstance(t, Comment) or t.parent.name in ("script", "style"): continue
            new = es.tr_text(str(t))
            if new != str(t): t.replace_with(NavigableString(new))
        # attributes
        for tag in s.find_all(True):
            for a in ("alt", "title", "placeholder", "aria-label", "data-cap"):
                if tag.has_attr(a) and tag[a].strip(): tag[a] = es.tr(tag[a].strip())
            if tag.has_attr("href") and tag.name in ("a", "link"): tag["href"] = _fix_url(tag["href"])
            if tag.has_attr("src"): tag["src"] = _fix_url(tag["src"])
            if tag.has_attr("data-rot"): tag["data-rot"] = "|".join(_fix_url(u) for u in tag["data-rot"].split("|"))
            if tag.has_attr("style") and "url(" in tag["style"]:
                tag["style"] = re.sub(r"url\('(img/[^']+)'\)", r"url('../\1')", tag["style"])
            if tag.has_attr("data-t") is False and tag.has_attr("data-set"): pass
        if s.title and s.title.string: s.title.string = es.tr(s.title.string.strip())
        for mt in s.find_all("meta"):
            if mt.get("name") in ("description", "twitter:title") or mt.get("property") in ("og:title", "og:description"):
                mt["content"] = es.tr(mt["content"].strip())
        url_en = f"{SITE_URL}/" if slug == "index" else f"{SITE_URL}/{slug}.html"
        url_es = f"{SITE_URL}/es/{slug}.html"
        for ln in s.find_all("link"):
            if ln.get("rel") == ["canonical"]: ln["href"] = url_es
            if ln.get("hreflang") == "en": ln["href"] = url_en
            if ln.get("hreflang") == "x-default": ln["href"] = url_en
            if ln.get("rel") == ["icon"]: ln["href"] = "../img/favicon.png"
        head = s.head
        alt = s.new_tag("link", rel="alternate", hreflang="es", href=url_es); head.append(alt)
        for mt in s.find_all("meta", property="og:url"): mt["content"] = url_es
        # language switch
        for a in s.select("a.lang"):
            a["href"] = f"../{slug}.html" if slug != "index" else "../index.html"
            a.clear(); a.append("EN / "); b = s.new_tag("b"); b.string = "ES"; a.append(b)
            if a.has_attr("data-lang"): del a["data-lang"]
        # form / mailto lang hint: nothing else
        out = str(s)
        open(os.path.join(OUT, "es", f"{slug}.html"), "w", encoding="utf-8").write(out)

def patch_en(OUT, SITE_URL, pages):
    """EN pages: real EN/ES link → es/<page>.html, hreflang es, no google-translate hook."""
    for slug in pages:
        p = os.path.join(OUT, f"{slug}.html")
        if not os.path.exists(p): continue
        h = open(p, encoding="utf-8").read()
        h = re.sub(r"<script>document\.querySelectorAll\('\[data-lang\]'\).*?</script>\n?", "", h, flags=re.S)
        h = h.replace('<a class="lang" href="#" data-lang><b>EN</b> / ES</a>', f'<a class="lang" href="es/{slug}.html"><b>EN</b> / ES</a>')
        h = h.replace('<link rel="alternate" hreflang="x-default"', f'<link rel="alternate" hreflang="es" href="{SITE_URL}/es/{slug}.html">\n<link rel="alternate" hreflang="x-default"', 1)
        open(p, "w", encoding="utf-8").write(h)
