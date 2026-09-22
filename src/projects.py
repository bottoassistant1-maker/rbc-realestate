# -*- coding: utf-8 -*-
"""Provisional project index built from @arqrobertobalderas (Instagram). Images are placeholders
until Roberto supplies photos; `ig` links to the original post."""

IG = "https://www.instagram.com/arqrobertobalderas/p/"

# category: res (residential) · hosp (hospitality & commercial) · param (parametric / art) · build (built by us)
PROJECTS = [
  dict(slug="casa-ether", scale="art", name="Casa Ether", note="Construction and design intervened by RBC on an existing siting and scheme", place="Piedras Azules · San Miguel de Allende", year="2025", cat="res", built=True, sale="casa-ether.html", img="img/ph-casa-ether-00.jpg", photos=['img/ph-casa-ether-00.jpg', 'img/ph-casa-ether-01.jpg', 'img/ph-casa-ether-02.jpg', 'img/ph-casa-ether-03.jpg', 'img/ph-casa-ether-04.jpg', 'img/ph-casa-ether-05.jpg', 'img/ph-casa-ether-06.jpg', 'img/ph-casa-ether-07.jpg', 'img/ph-casa-ether-plan-pb.jpg'], ig="DJ-iHIEx2Xi",
       txt="A contemporary country house on a hilltop in Piedras Azules. Construction and design intervened by RBC on an existing siting and scheme: starting from a previous scheme, circulation, proportions and material language were adjusted, and a new spatial reading was developed that prioritises the relationship with the landscape. The construction responds to the topography, integrates into the terrain and takes advantage of its views, combining sober finishes with elements from the site. Sliding glass walls open fully to the landscape; Italian hardwood on floors and ceilings; a Spanish kitchen. Photography: Alejandro Torre."),
  dict(slug="casa-jalpa", scale="art", name="Casa de Colina", place="San Miguel de Allende", year="2022", cat="res", built=False, img="img/ph-colina-01.jpg", photos=['img/ph-casa-jalpa-02.jpg', 'img/ph-casa-jalpa-00.jpg', 'img/ph-casa-jalpa-01.jpg', 'img/ph-casa-jalpa-03.jpg', 'img/ph-casa-jalpa-04.jpg', 'img/ph-casa-jalpa-05.jpg', 'img/ph-casa-jalpa-06.jpg', 'img/ph-casa-jalpa-07.jpg', 'img/ph-casa-jalpa-08.jpg', 'img/ph-casa-jalpa-09.jpg', 'img/ph-casa-jalpa-10.jpg', 'img/ph-colina-01.jpg', 'img/ph-colina-02.jpg', 'img/ph-colina-plan.jpg'], ig="CmIlRhHNyUi",
       txt="Country house project in Jalpa, Guanajuato."),
  dict(slug="casa-horizonte", m2="622", scale="art", name="Casa Horizonte", place="Peñas Arriba · San Miguel de Allende", year="2026", cat="res", built=True, sale="casa-horizonte.html", img="img/pa-hz-r01.jpg", photos=['img/pa-hz-r01.jpg','img/pa-hz-r03.jpg','img/pa-hz-r04.jpg','img/pa-hz-r09.jpg','img/pa-hz-r08.jpg','img/pa-hz-r10.jpg','img/pa-hz-r06.jpg','img/pa-hz-r11.jpg','img/pa-hz-r18.jpg', 'img/pa-hz-plan-section-2.jpg', 'img/pa-hz-plan-pb-2.jpg'], ig="DceaktFmAgJ",
       txt="Casa Horizonte is shaped by two defining elements: views and topography. Set on one of the highest points of Peñas Arriba, the house opens toward long, uninterrupted views of San Miguel de Allende. Rather than altering the land, the project follows the natural slope of the hill, unfolding across levels and opening both floors toward the city. The house is lived from the top down: at the entrance level, the social areas, main bedroom, terraces and pool; below, following the hillside, the secondary bedrooms, the wine cellar and the private garden. On the lower level, natural rock revealed by the excavation was intentionally left exposed, so the hillside itself becomes part of the architecture. 827 m² site · 622 m² built + pool. Currently available for sale."),
  dict(slug="pabellon-arte", scale="art", name="Private art pavilion", place="San Miguel de Allende", year="2026", cat="hosp", built=False, img="img/ph-pabellon-07.jpg", photos=['img/ph-pabellon-07.jpg','img/ph-pabellon-09.jpg','img/ph-pabellon-02.jpg','img/ph-pabellon-08.jpg','img/ph-pabellon-03.jpg','img/ph-pabellon-05.jpg','img/ph-pabellon-01.jpg','img/ph-pabellon-10.jpg'], ig="DZqIB1jmGm_",
       txt="Project for a private art pavilion conceived as a refuge for creation, contemplation and exhibition. The building brings together gallery, studio and private retreat in a single architectural experience: a contemplation courtyard leads to spaces for the permanent collection, temporary shows, sculpture, painting and performance, complemented by areas for creative work and reflection. Rooms, corridors, voids and courtyards of different scales build a carefully choreographed sequence that reveals the architecture gradually — changes of scale, height, light and atmosphere turn movement into discovery, reflection and surprise. The presence of water, natural light and honest materials explores the relationship between art, matter and silence. Born as a personal creative refuge, it is also designed to host exhibitions, gatherings, performances and special events."),
  dict(slug="casa-travertino", scale="art", name="Casa Travertino", place="Club de Golf El Campanario · Querétaro", year="2025", cat="res", built=True, sale="casa-travertino.html", img="img/ph-travertino-r02.jpg", photos=['img/ph-travertino-r02.jpg', 'img/ph-travertino-r01.jpg'], ig="C_3mXTMxFYj",
       txt="Newly built on the last lot of its private street, facing the mountains: double-height living and bar, pool and sun deck, four en-suite bedrooms plus staff quarters. Designed and built by RBC; for sale."),
  dict(slug="hotel-casa-x", scale="art", name="Hotel Casa X", place="San Miguel de Allende", year="2026", cat="hosp", built=False, img="img/ig-DZvx80iGPzt-1.jpg", photos=['img/ig-DZvx80iGPzt-1.jpg', 'img/ig-DZvx80iGPzt-2.jpg', 'img/ig-DZvx80iGPzt-3.jpg', 'img/ig-DZvx80iGPzt-4.jpg', 'img/ig-DZvx80iGPzt-5.jpg', 'img/ig-DZvx80iGPzt-6.jpg'], ig="DZvx80iGPzt",
       txt="Casa X is a proposal for a hotel immersed in the landscape, conceived for rest, contemplation and contact with nature. The project transforms an existing ranch through a master plan that uses the topography, vegetation and pre-existing buildings for a sensitive, low-impact intervention. The architecture seeks to disappear into the landscape: single, double and triple cabins are set into the hillside and oriented toward the mountain views, built with a play of parallel stone walls that give privacy, comfort and a constant relationship with the surroundings. The ensemble is completed by a pool integrated into the terrain and a deck for open-air events, classes and concerts that uses the topography itself as a natural stage. More than a collection of buildings, Casa X builds an integral wellness experience: spaces for ceremonies and wellbeing, a dining room with greenhouse and productive gardens, an existing water reserve integrated into the site, and complementary proposals such as a geodesic henhouse and natural air-cooling systems using water and fired-clay modules."),
  dict(slug="bar-bachus", scale="art", name="Bar Bachus", place="Historic center · San Miguel de Allende", year="2024", cat="hosp", built=True, img="img/ph-bar-bachus-06.jpg", photos=['img/ph-bar-bachus-06.jpg', 'img/ph-bar-bachus-00.jpg', 'img/ph-bar-bachus-01.jpg', 'img/ph-bar-bachus-02.jpg', 'img/ph-bar-bachus-03.jpg', 'img/ph-bar-bachus-04.jpg', 'img/ph-bar-bachus-05.jpg', 'img/ph-bar-bachus-07.jpg', 'img/ph-bar-bachus-08.jpg', 'img/ph-bar-bachus-09.jpg', 'img/ph-bar-bachus-10.jpg', 'img/ph-bar-bachus-11.jpg', 'img/ph-bar-bachus-12.jpg'], ig="C8NS-m5RKyS",
       txt="The design of Bar Bachus centres on fluid curves that create an enveloping, integrated space. Using parametric design principles, volumes unify every area of the bar into a cohesive whole, with the bar counter as the central piece. It adapts to an old house in the centre of San Miguel de Allende, blending modern elements with historical charm; the design elements compensate for the house's uneven levels, creating bars at different heights without interrupting the flow of the space."),
  dict(slug="casa-cuadrante", scale="art", name="Casa Cuadrante — restaurant & residence", place="Historic center · San Miguel de Allende", year="2023", cat="hosp", built=True, img="img/ph-cuad-n03.jpg", photos=['img/ph-cuad-n03.jpg', 'img/ph-musa-n07.jpg', 'img/ph-suite-n19.jpg', 'img/ph-musa-n35.jpg', 'img/ph-musa-n09.jpg', 'img/ph-musa-n23.jpg', 'img/ph-suite-n15.jpg', 'img/ph-suite-n11.jpg', 'img/ph-cuad-n01.jpg', 'img/ph-cuad-n02.jpg', 'img/ph-casa-cuadrante-00.jpg', 'img/ph-casa-cuadrante-02.jpg', 'img/ph-casa-cuadrante-03.jpg', 'img/ph-casa-cuadrante-04.jpg', 'img/ph-casa-cuadrante-05.jpg', 'img/ph-casa-cuadrante-06.jpg', 'img/ph-casa-cuadrante-07.jpg', 'img/ph-casa-cuadrante-08.jpg'], ig="CmIgeQvtivo",
       txt="Restoration, construction, adaptation and interior design of a historic house: the restaurant on the ground floor, and above it Casa Musa and the Panoramic Suite, both available for mid-term stays."),
  dict(slug="amecsa", scale="macro", name="Amecsa dealership", place="Monterrey · Nuevo León", year="2023", cat="hosp", built=False, img="img/ig-CqYldy-JhDi-1.jpg", photos=['img/ig-CqYldy-JhDi-1.jpg', 'img/ig-CqYldy-JhDi-2.jpg', 'img/ig-CqYldy-JhDi-3.jpg', 'img/ig-CqYldy-JhDi-4.jpg'], ig="CqYldy-JhDi",
       txt="Project for Amecsa, a heavy-machinery distributor."),
  dict(slug="condesa", scale="macro", name="Condesa apartment façade", place="Condesa · Mexico City", year="2024", cat="res", built=False, img="img/ig-C36BNy-r7sX-1.jpg", photos=['img/ig-C36BNy-r7sX-1.jpg'], ig="C36BNy-r7sX",
       txt="Project for the remodelling of a building in Condesa, Mexico City."),
  dict(slug="daily-veggies", scale="macro", name="Daily Veggies offices", place="Querétaro", year="2022", cat="hosp", built=False, img="img/ph-daily-veggies-00.jpg", photos=['img/ph-daily-veggies-00.jpg', 'img/ph-daily-veggies-01.jpg', 'img/ph-daily-veggies-02.jpg', 'img/ph-daily-veggies-03.jpg', 'img/ph-daily-veggies-04.jpg', 'img/ph-daily-veggies-05.jpg', 'img/ph-daily-veggies-06.jpg', 'img/ph-daily-veggies-07.jpg', 'img/ph-daily-veggies-08.jpg', 'img/ph-daily-veggies-09.jpg'], ig="CmIiJOeNybF",
       txt="Daily Veggies offices · Querétaro."),
  dict(slug="casa-de-campo-sma", scale="art", name="Casa de Campo, San Miguel", place="San Miguel de Allende", year="2022", cat="res", built=False, img="img/ph-campo-sma-01.jpg", photos=['img/ph-campo-sma-01.jpg', 'img/ph-campo-sma-02.jpg', 'img/ph-campo-sma-plan.jpg', 'img/ig-CmIhSSWNLll-1.jpg', 'img/ig-CmIhSSWNLll-3.jpg'], ig="CmIhSSWNLll",
       txt="Country house project in San Miguel de Allende."),
  dict(slug="restaurantes-sma", scale="macro", name="Restaurants in San Miguel", place="San Miguel de Allende", year="2022–24", cat="hosp", built=False, img="img/ph-restaurantes-sma-00.jpg", photos=['img/ph-restaurantes-sma-00.jpg', 'img/ph-restaurantes-sma-01.jpg', 'img/ph-restaurantes-sma-02.jpg', 'img/ig-CmIhqtPNJ_A-1.jpg', 'img/ig-CmIhqtPNJ_A-3.jpg'], ig="CmIhqtPNJ_A",
       txt="Projects for the San Mezcal rooftop, San Burger and Terraza Quiote · San Miguel de Allende."),
  dict(slug="plaza-qro", scale="macro", name="Commercial & residential plaza", place="Querétaro", year="2021", cat="hosp", built=False, img="img/ph-plaza-qro-01.jpg", photos=['img/ph-plaza-qro-01.jpg', 'img/ph-plaza-qro-00.jpg', 'img/ph-plaza-qro-02.jpg', 'img/ph-plaza-qro-03.jpg', 'img/ph-plaza-qro-04.jpg', 'img/ph-plaza-qro-05.jpg', 'img/ph-plaza-qro-06.jpg', 'img/ph-plaza-qro-07.jpg', 'img/ph-plaza-qro-08.jpg'], ig="CTkeLydL5WN",
       txt="Commercial plaza · Querétaro."),
  dict(slug="tuluminati", scale="macro", name="Tuluminati stores", place="San Miguel de Allende · Los Cabos", year="2022", cat="hosp", built=True, img="img/ph-tuluminati-03.jpg", photos=['img/ph-tuluminati-03.jpg','img/ph-tuluminati-04.jpg','img/ph-tuluminati-02.jpg','img/ph-tuluminati-01.jpg'], ig="CYrS_x8LAfL",
       txt="Design for the Tuluminati stores: Plaza Atrio, San Miguel de Allende, and Plaza Puerto Paraíso, Los Cabos."),
  dict(slug="wellness-merida", scale="art", name="Wellness complex", place="Mérida · Yucatán", year="2022", cat="hosp", built=False, img="img/ph-wellness-merida-00.jpg", photos=['img/ph-wellness-merida-00.jpg', 'img/ph-wellness-merida-01.jpg', 'img/ph-wellness-merida-02.jpg'], ig="CYN5_X2MvbD",
       txt="Project for Reset333, Mérida."),
  dict(slug="depa-jc", scale="art", name="Apartment JC", place="Historic center · San Miguel de Allende", year="2024", cat="res", built=True, img="img/ph-depa-jc-r01.jpg", photos=['img/ph-depa-jc-r01.jpg', 'img/ph-depa-jc-r02.jpg', 'img/ph-depa-jc-r03.jpg', 'img/ph-depa-jc-00.jpg', 'img/ph-depa-jc-01.jpg', 'img/ph-depa-jc-02.jpg', 'img/ph-depa-jc-03.jpg', 'img/ph-depa-jc-04.jpg', 'img/ph-depa-jc-05.jpg', 'img/ph-depa-jc-06.jpg', 'img/ph-depa-jc-07.jpg', 'img/ph-depa-jc-08.jpg', 'img/ph-depa-jc-09.jpg'], ig="C54_iAdg4zh",
       txt="Renovation project of a house in the centre of San Miguel de Allende: an apartment with a panoramic-view terrace, available for rent."),
  dict(slug="casa-cien", scale="art", name="Casa Cien suites", place="San Miguel de Allende", year="2021", cat="hosp", built=False, img="img/gated-entrance-luxury-home.jpg", ig="",
       txt="Guest suites in a house in San Miguel de Allende."),
  dict(slug="origen", scale="art", name="Origen store", place="San Miguel de Allende", year="2023", cat="hosp", built=False, img="img/wine-cellar-natural-stone.jpg", ig="",
       txt="Retail design for Origen in San Miguel de Allende."),
  dict(slug="saiko", scale="macro", name="Saiko", place="San Miguel de Allende", year="2024", cat="hosp", built=False, img="img/community-trails.jpg", ig="",
       txt="Preliminary project for Saiko in San Miguel de Allende."),
  dict(slug="casa-artista", scale="art", name="Casa Artista", place="San Miguel de Allende", year="2026", cat="res", built=False, img="img/stone-villa-garden-pool-mexico.jpg", ig="",
       txt="Preliminary project for the architect's own house."),
  dict(slug="casa-velia", scale="art", name="Casa Velia", place="Historic center · San Miguel de Allende", year="2025", cat="res", built=False, img="img/san-miguel-street-vertical.jpg", ig="",
       txt="A house in the historic center of San Miguel de Allende — restoration and new architecture within the walls of the old town."),
  dict(slug="binary-pavilion", scale="art", name="Binary Code Pavilion & parametric studies", place="Competition · research", year="2021–22", cat="param", built=False, img="img/ph-binary-pavilion-03.jpg", photos=['img/ph-binary-pavilion-03.jpg', 'img/ph-binary-pavilion-00.jpg', 'img/ph-binary-pavilion-01.jpg', 'img/ph-binary-pavilion-02.jpg', 'img/ph-binary-pavilion-04.jpg', 'img/ig-CYN4kfeMIFT-1.jpg'], ig="CYN4kfeMIFT",
       txt="Binary Code Pavilion — competition entry with Ana Laura González for competitions.archi, sited in the Sahara Desert, Egypt. The brief: how to preserve and show the best of our species for a far future, so that other life forms or future civilisations could learn about our achievements. The pavilion preserves a message for posterity on its whole façade, written in binary code that can be translated into text, images or sounds: the outer shell is made of blocks that physically represent the binary system — solid (0) or hollowed-out (1)."),
  dict(slug="casa-jalpa-2", scale="art", name="Casa de León", place="San Miguel de Allende", year="2023", cat="res", built=False, img="img/ph-leon-01.jpg", photos=['img/ph-casa-jalpa-2-00.jpg', 'img/ph-casa-jalpa-2-01.jpg', 'img/ph-casa-jalpa-2-02.jpg', 'img/ph-casa-jalpa-2-03.jpg', 'img/ph-casa-jalpa-2-04.jpg', 'img/ph-casa-jalpa-2-05.jpg', 'img/ph-casa-jalpa-2-06.jpg', 'img/ph-casa-jalpa-2-07.jpg', 'img/ph-leon-01.jpg', 'img/ph-leon-02.jpg', 'img/ph-leon-plan.jpg'], ig="",
       txt="A single-storey country house: one long roof, glass to the landscape, stone base."),
  dict(slug="casa-jalpa-3", scale="art", name="Casa Jalpa", place="Jalpa · Guanajuato", year="2023", cat="res", built=False, img="img/ph-casa-jalpa-r01.jpg", photos=['img/ph-casa-jalpa-r01.jpg', 'img/ph-casa-jalpa-r02.jpg', 'img/ph-casa-jalpa-plan.jpg', 'img/ph-casa-jalpa-3-03.jpg', 'img/ph-casa-jalpa-3-00.jpg', 'img/ph-casa-jalpa-3-01.jpg', 'img/ph-casa-jalpa-3-02.jpg', 'img/ph-casa-jalpa-3-04.jpg', 'img/ph-casa-jalpa-3-05.jpg', 'img/ph-casa-jalpa-3-06.jpg'], ig="",
       txt="Two volumes on a slope: a cantilevered social level over the garage, bedrooms behind."),
  dict(slug="chevrolet", scale="macro", name="Car dealership", place="Bajío", year="2022", cat="hosp", built=False, img="img/ph-chevrolet-00.jpg", photos=['img/ph-chevrolet-00.jpg'], ig="Cage5QBMGA4",
       txt="Proposal for the design of a car dealership."),
  dict(slug="penas-obra", scale="macro", name="Peñas Arriba — site", place="San Miguel de Allende", year="2019–2026", cat="res", built=True, img="img/ph-penas-obra-b-06.jpg", photos=['img/ph-penas-obra-b-06.jpg', 'img/ph-penas-obra-b-07.jpg', 'img/ph-penas-obra-b-03.jpg', 'img/ph-penas-obra-b-01.jpg', 'img/ph-penas-obra-b-02.jpg', 'img/ph-penas-obra-b-00.jpg', 'img/ph-penas-obra-a-06.jpg', 'img/ph-penas-obra-a-05.jpg', 'img/ph-penas-obra-a-04.jpg', 'img/ph-penas-obra-a-03.jpg', 'img/ph-penas-obra-a-02.jpg', 'img/ph-penas-obra-a-07.jpg', 'img/ob-penas-arriba-e-01.jpg', 'img/ob-penas-arriba-e-02.jpg'], ig="",
       txt="Urbanization, stone terracing, amenity buildings and houses on the hillside above San Miguel."),
  dict(slug="casa-valle", scale="art", name="Casa del Valle", place="Jalpa · Guanajuato", year="2024", cat="res", built=False, img="img/ph-valle-01.jpg", photos=['img/ph-valle-01.jpg', 'img/ph-valle-02.jpg', 'img/ph-valle-plan.jpg'], ig="",
       txt="A single-level country house on a steel-roofed platform, open to the valley."),
  dict(slug="casa-pena", scale="art", name="Casa de la Peña", place="Peñas Arriba · San Miguel de Allende", year="2026", cat="res", built=False, img="img/pa-comm-01.jpg", photos=['img/pa-comm-01.jpg','img/ph-casa-pena-plan-pb.jpg','img/ph-casa-pena-plan-p1.jpg','img/ph-casa-pena-plan-p2.jpg'], ig="",
       txt="A large house on the rock at the top of Peñas Arriba: three levels stepping down the slope, terraces with plunge pools, a family wing and a guest wing, and parking for four cars."),
  dict(slug="casa-ventanas", scale="art", name="Casa Ventanas", place="San Miguel de Allende", year="", cat="res", built=True, img="img/ob-casa-ventanas-09.jpg", photos=['img/ob-casa-ventanas-09.jpg', 'img/ob-casa-ventanas-10.jpg', 'img/ob-casa-ventanas-07.jpg', 'img/ob-casa-ventanas-02.jpg', 'img/ob-casa-ventanas-01.jpg'], ig="",
       txt="House by a golf course; stone, wood ceilings and an inner patio with a pool."),
]

def cards(cat=None, built=None, limit=None):
    ps = [p for p in PROJECTS if (cat is None or p["cat"] == cat) and (built is None or p["built"] == built)]
    if limit: ps = ps[:limit]
    out = []
    for i, p in enumerate(ps):
        d = "d" + str(i % 3) if i % 3 else ""
        out.append(f"""
      <article class="proj rv {d}" data-cat="{p['cat']}">
        <a class="pim" href="{p.get('sale') or (IG+p['ig']+'/' if p['ig'] else '#')}"{'' if p.get('sale') or not p['ig'] else ' target="_blank" rel="noopener"'}><img src="{p['img']}" alt="{p['name']} — {p['place']}" loading="lazy"><span class="prov">{'For sale' if p.get('sale') else 'Provisional image'}</span></a>
        <div class="pbd">
          <div class="pmeta"><span>{p['place']}</span><span>{p['year']}</span></div>
          <h3>{p['name']}</h3>
          <p>{p['txt']}</p>
          {('<a class="plink" href="'+p['sale']+'">See the listing →</a>') if p.get('sale') else (('<a class="plink" href="'+IG+p['ig']+'/" target="_blank" rel="noopener">View on Instagram →</a>') if p['ig'] else '')}
        </div>
      </article>""")
    return "".join(out)

INTERIORS={"bar-bachus","tuluminati","daily-veggies","casa-cuadrante","depa-jc","origen","casa-musa"}
def types(p):
    t=["architecture"]
    if p.get("built"): t.append("construction")
    if p["slug"] in INTERIORS: t.append("interiors")
    if p["cat"]=="param": t.append("research")
    return t

CSS = r"""
/* ── work index ── */
.pfilters{display:flex;gap:0;flex-wrap:wrap;margin-top:26px;border-bottom:1px solid var(--hair);}
.pfilters button{font-family:var(--mono);font-size:.68rem;letter-spacing:.14em;text-transform:uppercase;padding:12px 16px 12px 0;margin-right:18px;border:none;background:transparent;color:var(--ink-soft);cursor:pointer;position:relative;}
.pfilters button.on{color:var(--navy);}
.pfilters button.on::after{content:'';position:absolute;left:0;right:18px;bottom:-1px;height:2px;background:var(--gold);}
.projs{display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:230px;grid-auto-flow:dense;gap:16px;margin-top:28px;}
@media(max-width:1000px){.projs{grid-template-columns:repeat(2,1fr);}}
@media(max-width:600px){.projs{grid-template-columns:1fr;grid-auto-rows:300px;}}
.proj{position:relative;overflow:hidden;background:var(--paper-2);color:#fff;display:block;text-decoration:none;}
.proj.wide{grid-column:span 2;} .proj.tall{grid-row:span 2;} .proj.big{grid-column:span 2;grid-row:span 2;}
@media(max-width:600px){.proj.wide,.proj.big{grid-column:span 1;}.proj.tall,.proj.big{grid-row:span 1;}}
.proj.hide{display:none;}
.proj img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform 1s var(--ease);}
.proj:hover img{transform:scale(1.04);}
.proj::after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(22,30,69,0) 45%,rgba(22,30,69,.85) 100%);}
.proj .pbd{position:absolute;left:0;right:0;bottom:0;padding:16px 18px;z-index:2;}
.proj .pmeta{font-family:var(--mono);font-size:.6rem;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.8);display:flex;gap:12px;flex-wrap:wrap;}
.proj .pmeta .cd{color:var(--gold);}
.proj h3{color:#fff;font-size:1.25rem;font-weight:400;margin:4px 0 0;}
.proj.big h3{font-size:1.9rem;} .proj.wide h3,.proj.tall h3{font-size:1.5rem;}
.proj p{font-size:.84rem;color:rgba(255,255,255,.88);line-height:1.5;max-height:0;overflow:hidden;opacity:0;transition:max-height .5s var(--ease),opacity .4s,margin .4s;margin:0;}
.proj:hover p,.proj:focus-visible p{max-height:6em;opacity:1;margin-top:8px;}
.proj .tag{position:absolute;top:12px;left:12px;z-index:2;font-family:var(--mono);font-size:.58rem;letter-spacing:.14em;text-transform:uppercase;color:#fff;background:rgba(22,30,69,.75);padding:5px 9px;}
.proj .tag.sale{background:var(--red);}
.provnote{margin-top:18px;font-family:var(--mono);font-size:.66rem;letter-spacing:.06em;color:var(--ink-soft);border-left:2px solid var(--gold);padding-left:12px;}
"""

JS = r"""
<script>
document.querySelectorAll('.pfilters').forEach(f=>{
  const grid=f.parentElement.querySelector('.projs'); if(!grid) return;
  f.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{
    f.querySelectorAll('button').forEach(x=>x.classList.remove('on')); b.classList.add('on');
    const c=b.dataset.cat; grid.querySelectorAll('.proj').forEach(p=>p.classList.toggle('hide', c!=='all' && !(' '+p.dataset.types+' ').includes(' '+c+' ')));
  }));
});
</script>
"""

SIZES = ["big","","tall","","wide","","","tall","","wide","","",""]

def code(i, p):
    return f"RBC/{'A' if 'construction' not in types(p) else 'AC'}-{i+1:03d}"

def cards(cat=None, built=None, limit=None):
    ps = [p for p in PROJECTS if (cat is None or p["cat"] == cat) and (built is None or p["built"] == built)]
    if limit: ps = ps[:limit]
    out = []
    for i, p in enumerate(ps):
        size = SIZES[i % len(SIZES)]
        href = p.get('sale') or (IG + p['ig'] + '/' if p['ig'] else '#')
        ext = '' if p.get('sale') or not p['ig'] else ' target="_blank" rel="noopener"'
        out.append(f"""
      <a class="proj rv {size}" data-types="{' '.join(types(p))}" href="{href}"{ext}>
        <img src="{p['img']}" alt="{p['name']} — {p['place']}" loading="lazy">
        {('<span class="tag sale">For sale</span>' if p.get('sale') else ('' if p.get('photos') else '<span class="tag">Provisional image</span>'))}
        <div class="pbd">
          <div class="pmeta"><span class="cd">{code(i,p)}</span><span>{p['place']}</span><span>{p['year']}</span></div>
          <h3>{p['name']}</h3>
          <p>{p['txt']}</p>
        </div>
      </a>""")
    return "".join(out)

INTRO = """<div class="split rv" style="align-items:start;margin-top:8px;">
      <p class="lead">There is no house style. A project here may be contemporary, contextual, traditional or colonial, depending on the site, the client, the budget and the brief. The range runs from small interventions and individual houses to larger residences, commercial work, residential towers and development-scale projects.</p>
      <p class="lead">What repeats is the way decisions are made: how the plan meets the site, where the light comes from, which material belongs, what will still be right in twenty years. The common denominator is architectural judgment, not a look.</p>
    </div>"""

def index_section(title="Work.", eyebrow="Selected work", filters=True, cat=None, built=None, limit=None, note=True, intro=True, num="02"):
    fl = ""
    if filters:
        fl = """<div class="pfilters"><button class="on" data-cat="all">All</button><button data-cat="architecture">Architecture</button><button data-cat="construction">Construction</button><button data-cat="interiors">Interiors</button><button data-cat="research">Research</button></div>"""
    n = '<div class="provnote rv">Photography from @arqrobertobalderas; a few projects still carry provisional images. Descriptions and links are real.</div>' if note else ""
    return f"""
<section id="projects">
  <div class="wrap">
    <div class="shead rv"><div class="eyebrow"><b>{num}</b>{eyebrow}</div><i></i></div>
    <h2 class="rv d1">{title}</h2>
    {INTRO if intro else ""}
    {fl}
    <div class="projs">{cards(cat, built, limit)}</div>
    {n}
  </div>
</section>"""


def selected(slugs):
    """Large editorial feature layout for the homepage: big images, one line of text each."""
    ps = [next(p for p in PROJECTS if p["slug"] == sl) for sl in slugs]
    out = []
    for i, p in enumerate(ps):
        href = p.get('sale') or (IG + p['ig'] + '/' if p['ig'] else 'work.html')
        ext = '' if p.get('sale') or not p['ig'] else ' target="_blank" rel="noopener"'
        out.append(f"""
      <a class="sw rv{' sw-lead' if i == 0 else ''}" href="{href}"{ext}>
        <figure><img src="{p['img']}" alt="{p['name']} — {p['place']}" loading="{'eager' if i == 0 else 'lazy'}">{'' if p.get('photos') else '<span class="prov">Provisional image</span>'}</figure>
        <div class="sw-cap"><span class="cd">{code(PROJECTS.index(p), p)}</span><b>{p['name']}</b><span>{p['place']} · {p['year']}</span></div>
      </a>""")
    return '<div class="swgrid">' + "".join(out) + "</div>"
