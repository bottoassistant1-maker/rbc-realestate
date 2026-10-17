# -*- coding: utf-8 -*-
"""Brand marks rendered as inline images (Roberto, 17-oct-2026).

* "Espacios y Formas" → wordmark image, linked to espaciosyformas.com.mx, wherever
  the name appears as visible text on the site (post-processing of every page).
* In authorship lines, "Peñas Arriba" and "Magno" are also shown as their logos.
"""
import re, html as _h

EYF_URL = "https://www.espaciosyformas.com.mx/"
EYF = "Espacios y Formas"

BRANDS = {
    # name → (image, link, css class)
    "Espacios y Formas": ("img/eyf-wordmark.png", EYF_URL, "brand brand-eyf"),
    "Peñas Arriba":      ("img/penas-arriba-text.png", "penas-arriba.html", "brand brand-pa"),
    "Magno":             ("img/magno-logo-navy.png", "magno.html", "brand brand-magno"),
}

def mark(name, prefix="", link=True):
    img, href, cls = BRANDS[name]
    im = f'<img src="{prefix}{img}" alt="{name}" title="{name}">'
    if not link:
        return f'<span class="{cls}">{im}</span>'
    tgt = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
    return f'<a class="{cls}" href="{prefix}{href}"{tgt}>{im}</a>'

def brand_html(text, prefix="", link=True):
    """Authorship line: replace every brand name with its mark."""
    if not text: return ""
    out = _h.escape(text, quote=False)
    for name in ("Espacios y Formas", "Peñas Arriba", "Magno"):
        out = re.sub(r"(?<![\w-])" + re.escape(name) + r"(?![\w-])", lambda m, n=name: mark(n, prefix, link), out)
    return out

# ── page post-processing ───────────────────────────────────────────────────
_SKIP = {"script", "style", "title", "head", "noscript", "textarea", "option", "img"}

def eyfify(html, prefix=""):
    """Replace visible 'Espacios y Formas' text with the linked wordmark."""
    if EYF not in html: return html
    try:
        from bs4 import BeautifulSoup, NavigableString, Comment
    except ImportError:
        return html
    s = BeautifulSoup(html, "html.parser")
    for t in list(s.find_all(string=True)):
        if isinstance(t, Comment) or EYF not in t: continue
        if any(p.name in _SKIP for p in t.parents): continue
        if any(p.name == "a" and "brand" in (p.get("class") or []) for p in t.parents): continue
        in_link = any(p.name == "a" for p in t.parents)
        dark = any("foot" in " ".join(p.get("class") or []) or p.name == "footer" for p in t.parents)
        parts = str(t).split(EYF)
        frag = []
        for i, part in enumerate(parts):
            if part: frag.append(NavigableString(part))
            if i < len(parts) - 1:
                img = s.new_tag("img", src=prefix + ("img/eyf-wordmark-white.png" if dark else "img/eyf-wordmark.png"), alt=EYF, title=EYF)
                if in_link:
                    sp = s.new_tag("span", **{"class": "brand brand-eyf"}); sp.append(img); frag.append(sp)
                else:
                    a = s.new_tag("a", href=EYF_URL, target="_blank", rel="noopener", **{"class": "brand brand-eyf"}); a.append(img); frag.append(a)
        anchor = t
        for f in frag:
            anchor.insert_after(f); anchor = f
        t.extract()
    return str(s)

CSS = r"""
.brand{display:inline-block;line-height:0;vertical-align:baseline;text-decoration:none!important;border:0;}
.brand img{height:.98em;width:auto;display:inline-block;vertical-align:-0.14em;}
.brand-pa img{height:.9em;vertical-align:-0.1em;}
.brand-magno img{height:1.15em;vertical-align:-0.28em;}
a.brand:hover img{opacity:.75;}
.pp-auth .brand img{height:1.15em;}
.fs-auth .brand img{height:1.7em;vertical-align:-0.45em;} .fs-auth .brand-magno img{height:2.1em;vertical-align:-0.6em;} .fs-auth .brand-pa img{height:1.5em;vertical-align:-0.35em;}
p .brand img,li .brand img{height:1.02em;}
footer .brand img{height:1em;}
.intro-contact .brand img,.facts .brand img{height:1.35em;}
"""
