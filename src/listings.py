# -*- coding: utf-8 -*-
"""Selected properties (sale & rent) + property page generator.
Only facts supplied by Roberto appear here. Images are provisional placeholders until photography arrives.
Internal names never appear on the site. `notes` are drafts in Roberto's voice, pending his review (NOTES_DRAFT)."""

MXN_PER_USD = 17.0
NOTES_DRAFT = True   # show "draft · pending review" next to Roberto's Notes until he approves the texts

def usd(mxn):  # compact USD string from MXN
    v = mxn / MXN_PER_USD
    return f"US ${v/1e6:.2f}M" if v >= 1e6 else f"US ${round(v/1000)}K"

def mdp(mxn):
    return f"MX ${mxn/1e6:g}M" if mxn >= 1e6 else f"MX ${mxn:,.0f}"

L = []
def add(**k): L.append(k); return k

# ───────── SAN MIGUEL DE ALLENDE · sale ─────────
add(slug="casa-horizonte", page=True, city="sma", kind="sale", name="Casa Horizonte", where="Peñas Arriba · San Miguel de Allende",
    auth="Designed by RBC · built with Espacios y Formas",
    status="Under construction · finishes open", feat=True, price_mxn=32_500_000,
    specs=[("622","m² built · 6,693 sq ft"),("827","m² lot · 8,905 sq ft"),("5","bedrooms"),("5½","baths"),("2","cars")],
    blurb="A house that follows its slope: entered from the top, stepping down the hill so the principal rooms face the historic center. Under construction; finishes still to be chosen.",
    intro="Casa Horizonte is shaped by its topography. Rather than levelling the land, the house follows the slope of the hill: you arrive at the upper level — living, dining, kitchen, terrace and pool — and the house steps down so that every principal room faces the historic center of San Miguel. Rock revealed by the excavation was left exposed inside as the wall of the wine cellar.",
    arch="Section-driven plan on two levels. The social level and pool sit at the top with the entry; the bedrooms step down toward the garden. The principal rooms are oriented to the view of the historic center.",
    site="Lot M4-L7, upper tier of Peñas Arriba, a gated community on the hillside above San Miguel with a protected line of sight to the Parroquia. Excavated rock kept inside the house as the cellar wall.",
    materials="Stone on façades and retaining walls; concrete structure; large glazing toward the view. Flooring, kitchen, baths, stone and lighting still to be selected.",
    condition="Under construction at an advanced stage; elevator-ready. Delivered with finishes selected by the buyer.",
    potential="A view house of this size whose finishes are still open — the buyer defines the final level of the house without waiting for a full build.",
    notes="The house was drawn from the section. The site decided where to enter, where to sleep and where to look; the plan simply followed. Whoever buys it now still gets to decide the materials of every surface they will touch.",
    highlights=["622 m² (6,693 sq ft) built on an 827 m² (8,905 sq ft) lot","5 bedrooms: three on the entry level (one convertible to staff), two below · 5½ baths","Pool and pergola terrace facing the Parroquia","Wine cellar in the excavated rock · elevator-ready","Under construction — finishes chosen by the buyer"],
    program=[("Upper level — entry","Entry court and two-car garage · living-dining with open kitchen · primary suite with two walk-ins and two baths · study with bath · two bedrooms · linen room · covered terrace · sun deck with pool"),("Lower level","Two large en-suite bedrooms · family room · wine cellar in the excavated rock · elevator shaft · private garden facing the center")],
    location="Lot M4-L7, upper tier of Peñas Arriba, San Miguel de Allende — about 7 minutes (1.8 mi) from the Jardín Principal. BJX airport ~1 h 15, QRO ~1 h.",
    img="img/ig-DceaktFmAgJ-1.jpg",
    gallery=["img/ig-DceaktFmAgJ-3.jpg","img/ig-DceaktFmAgJ-5.jpg","img/ig-DceaktFmAgJ-2.jpg","img/ig-DceZkcqmPiU-2.jpg","img/ig-DceaktFmAgJ-6.jpg","img/ig-DceaktFmAgJ-4.jpg","img/ig-DceZkcqmPiU-4.jpg","img/casa-horizonte-garden-facade-day.jpg"],
    plans=["img/ig-DceZkcqmPiU-5.jpg","img/ig-DceZkcqmPiU-6.jpg","img/architecture-section-hillside-home.jpg"])

add(slug="casa-mirador", page=True, city="sma", kind="sale", name="Casa Mirador", where="Historic center · San Miguel de Allende",
    auth="Represented by RBC",
    status="Finished · furnished", price_mxn=None, price_note="Price on request",
    specs=[("4","levels"),("3","bedrooms"),("3½","baths"),("1","car"),("Rooftop","jacuzzi")],
    blurb="A four-level house in the historic center around a courtyard with a motorised sliding glass dome; rooftop with jacuzzi and outdoor kitchen facing the Parroquia. Delivered furnished.",
    intro="Casa Mirador is organised around a central courtyard covered by a motorised sliding glass dome: open, the patio is an outdoor room; closed, the house keeps its light in any weather. Four levels rise around it, ending in a rooftop with jacuzzi, outdoor kitchen and bar facing the Parroquia. Two fountains, a master bath that opens onto its own garden, and finishes in a style of its own. Delivered furnished and decorated.",
    arch="Vertical house on four levels around a central courtyard; the rooftop works as a fourth façade, oriented to the Parroquia.",
    site="Historic center of San Miguel de Allende, walking distance from the Jardín Principal. Views of the town and the Parroquia from the upper levels and the roof.",
    materials="Finishes in a style of its own; two fountains; master bath opening onto a private garden. Furnished and decorated.",
    condition="Finished, furnished, ready to occupy. Air conditioning and curtains in the bedrooms.",
    potential="Parking, a courtyard that can be closed in the rain and a usable roof are rarely found together in the center. Works as a primary residence or as a rental.",
    notes="Houses in the center rarely solve light and weather at the same time. The sliding dome does both, and it is the reason the courtyard is the best room in the house.",
    highlights=["Views of the historic center and the Parroquia from the rooftop and upper levels","Central courtyard with automatic sliding glass dome","Two full bedrooms with en-suite baths, air conditioning and blackout curtains","Master suite with a private garden inside the bathroom","Rooftop with jacuzzi, outdoor kitchen, bar and lounge","TV room, guest half-bath, garage, two fountains","Delivered furnished and decorated"],
    program=[("Ground level","Garage, entry, central courtyard with the glass dome, two fountains"),("Living levels","Living, dining, kitchen, TV room and guest half-bath around the courtyard"),("Bedroom level","Two en-suite bedrooms with A/C; master suite with garden bath"),("Rooftop","Jacuzzi, outdoor kitchen, bar and terrace facing the Parroquia")],
    location="Historic center of San Miguel de Allende, walking distance from the Jardín Principal.",
    img="img/san-miguel-street-vertical.jpg", gallery=["img/view-historic-center.jpg","img/san-miguel-de-allende-parroquia-view.jpg","img/luxury-home-san-miguel-interior-living.jpg"])

add(slug="casa-zafiro", page=False, city="sma", kind="sale", name="Casa Zafiro · M1-L14", where="Peñas Arriba · San Miguel de Allende",
    auth="Peñas Arriba · built with Espacios y Formas",
    status="Shell built · ~6 months to delivery", price_mxn=13_900_000,
    specs=[("344","m² built · 3,700 sq ft"),("418","m² lot · 4,500 sq ft"),("4+s","bedrooms"),("5½","baths"),("2","cars")],
    blurb="On the largest garden lot of the community, built to shell: plan and site are done, every finish is still open.",
    intro="Casa Zafiro sits on the largest garden lot in Peñas Arriba. It is built to shell stage, with delivery in about six months once the finishes are defined together with the practice.",
    arch="Compact plan opening to terrace and garden; master suite on the main level.",
    site="Lot M1-L14, a 418 m² garden lot inside the gated community, with views of the center and the Parroquia.",
    materials="Built to shell — flooring, stone, carpentry and paint still to be chosen.",
    condition="Shell complete; about six months to delivery once finishes are defined.",
    potential="The plan and the site without waiting for a full build, and the level of finish set to the buyer's budget.",
    notes="The garden is the argument. It is the biggest lot in the community and the shell is already there; what remains is the part most owners enjoy deciding.",
    highlights=["343.7 m² (3,700 sq ft) built on a 4,500 sq ft garden lot","4 bedrooms + staff · 5½ baths · 2 cars","Shell built — flooring, stone, carpentry and paint chosen by the buyer","Views of the historic center and the Parroquia","Inside gated Peñas Arriba: pool, gym, restaurant, 24/7 security"],
    program=[("The house","Living-dining and kitchen open to terrace and garden · master suite · three further bedrooms · staff quarters · two-car garage")],
    location="Lot M1-L14, Peñas Arriba, San Miguel de Allende — about 7 minutes from the historic center.",
    img="img/listing-casa-zafiro-san-miguel.jpg", wa_msg="Hi Roberto, I'm interested in Casa Zafiro M1-L14.", gallery=["img/community-club-pool.jpg","img/parroquia-view-from-community.jpg"])

add(slug="casa-cima", page=True, city="sma", kind="sale", name="Casa Cima · M6-L1", where="Peñas Arriba · San Miguel de Allende",
    auth="Peñas Arriba · built with Espacios y Formas",
    status="Shell built · finishes open", price_mxn=None, price_note="Price on request",
    specs=[("592","m² built · 6,373 sq ft"),("764","m² lot · 8,219 sq ft"),("4+s","bedrooms"),("6+2","baths"),("2","cars")],
    blurb="First house of its block: the side façade rises from the street as one wall of natural stone. Double-height living and an unusually large garden with views of the historic center.",
    intro="Casa Cima is the first house of block 6, so its side façade rises from the street as a single wall of natural stone. The social level opens in double height — living, dining and bar in one room that flows to the terrace and to a large garden looking over the community gardens toward the historic center. The master suite is placed on the social level, with its own sitting room, two baths and a double view. Built to shell; a pool facing the town can be added in the garden.",
    arch="Double-height social level; master suite deliberately on the same level as the garden, with its own sitting room. Three double bedrooms and a TV lounge upstairs.",
    site="Lot M6-L1, 763.55 m², with one of the largest gardens in the community, looking over the community gardens to the historic center.",
    materials="Natural stone; concrete structure. Built to shell — all finishes open.",
    condition="Shell built; ready for flooring, stone, carpentry and paint. Pool with a view of the town can be added.",
    potential="The freedom to define every finish on a house whose structure, plan and garden are already resolved.",
    notes="The master suite is downstairs on purpose: whoever lives here should have the garden and the view without a staircase in between.",
    highlights=["763.55 m² lot (8,219 sq ft) · 592.06 m² built (6,373 sq ft)","Double-height living, dining and bar opening to terrace and garden","Master suite on the social level: walk-in closet, two baths, private sitting room, double view","Upper level: three double bedrooms, each with full bath, and a TV lounge","Kitchen with pantry room, staff quarters, garage and storage","Option to add a pool facing the historic center","Shell built — finishes chosen with the architect"],
    program=[("Ground level","Garage and storage · master suite with walk-in, two baths and sitting room · double-height living, dining and bar · kitchen with pantry · staff room · terrace with dining and lounge · garden"),("Upper level","TV lounge · three double bedrooms with full baths"),("Baths","6 full + 2 guest half-baths")],
    location="Lot M6-L1, the first house of block 6 in Peñas Arriba, San Miguel de Allende — about 7 minutes from the historic center.",
    img="img/luxury-villa-sunset-san-miguel.jpg", gallery=["img/stone-walls-community.jpg","img/parroquia-view-from-community.jpg","img/villa-garden-day.jpg"])

add(slug="duplex-upper", page=False, city="sma", kind="sale", name="Duplex · Upper residence · M1-L12", where="Peñas Arriba · San Miguel de Allende",
    auth="Peñas Arriba · built with Espacios y Formas",
    status="Built · ~6 months to delivery", price_mxn=6_600_000,
    specs=[("≈205","m² · 2,207 sq ft"),("3","bedrooms"),("3½","baths"),("2","cars")],
    blurb="One level on the upper floor of a duplex, with the full view of the historic center and no garden to maintain.",
    intro="The upper residence of a duplex in Peñas Arriba: a single level with the view of the historic center. Built; delivered in about six months with finishes chosen by the buyer.",
    arch="Single-level plan; living, kitchen and terrace on the view side.",
    site="Lot M1-L12, Peñas Arriba.",
    materials="Built; finishes chosen with the practice.",
    condition="Built; about six months to delivery.",
    potential="Lock-and-leave living with a view and no garden upkeep.",
    notes="The right size for two people who want San Miguel without the maintenance of a large house.",
    highlights=["≈ 205 m² (2,207 sq ft) on a single level","3 bedrooms · 3½ baths · 2 cars","Views of the center and the Parroquia","Built — finishes chosen with the architect"],
    program=[("Upper level","Living-dining, kitchen, terrace with the view · master suite · two bedrooms · 3½ baths")],
    location="Lot M1-L12, Peñas Arriba, San Miguel de Allende.",
    img="img/listing-duplex-upper-unit.jpg", wa_msg="Hi Roberto, I'm interested in the Duplex upper residence M1-L12.", gallery=["img/view-historic-center.jpg"])

add(slug="duplex-garden", page=False, city="sma", kind="sale", name="Duplex · Garden residence · M5-L9", where="Peñas Arriba · San Miguel de Allende",
    auth="Peñas Arriba · built with Espacios y Formas",
    status="Built · ~6 months to delivery", price_mxn=7_433_000,
    specs=[("≈188","m² · 2,024 sq ft"),("3","bedrooms"),("3½","baths"),("2","cars")],
    blurb="Ground-floor living with a private garden, next to the clubhouse and pool.",
    intro="The garden residence of a duplex in Peñas Arriba: ground-floor living opening to a private garden, steps from the club. Built; delivered in about six months with finishes chosen by the buyer.",
    arch="Ground-floor plan; living-dining and kitchen open to the garden.",
    site="Lot M5-L9, Peñas Arriba, next to the clubhouse and pool.",
    materials="Built; finishes chosen with the practice.",
    condition="Built; about six months to delivery.",
    potential="A private garden inside a gated community, with the pool and club a few steps away.",
    notes="Closest house to the club. Between the two duplex units, this is the one for anyone who wants to eat breakfast outside.",
    highlights=["≈ 188 m² (2,024 sq ft) with private garden","3 bedrooms · 3½ baths · 2 cars","Steps from the clubhouse and pool","Built — finishes chosen with the architect"],
    program=[("Ground level","Living-dining and kitchen opening to the garden · master suite · two bedrooms · 3½ baths")],
    location="Lot M5-L9, Peñas Arriba, San Miguel de Allende.",
    img="img/listing-duplex-garden-unit.jpg", wa_msg="Hi Roberto, I'm interested in the Duplex garden residence M5-L9.", gallery=["img/community-pool-stone.jpg"])

# ───────── SAN MIGUEL · rent ─────────
add(slug="casa-musa", page=True, city="sma", kind="rent", name="Casa Musa", where="Casa Cuadrante · Historic center · San Miguel de Allende",
    auth="Casa Cuadrante — restored and designed by RBC",
    status="Furnished apartment · mid-term stays", price_mxn=None, price_note="Monthly rate on request · services included",
    specs=[("1","bedroom · king"),("1","full bath"),("Balcony","facing the Parroquia"),("Services","included")],
    blurb="An apartment above Casa Cuadrante: living-dining with fireplace and a view of the Parroquia, private balcony, art on every wall. Furnished; services included.",
    intro="Casa Musa is the apartment above Casa Cuadrante, the restaurant on the ground floor of a historic house that RBC restored, adapted and furnished. It was made for people who like living among art: a living-dining room with a fireplace and a direct view of the Parroquia, a bedroom with a king bed and full bath, a sound system, a private balcony over the street and a laundry room. Water, electricity and internet are included. Available for mid-term stays.",
    arch="An apartment organised around a living-dining room with a fireplace and a straight view of the Parroquia; private balcony over the street.",
    site="Inside Casa Cuadrante, historic center — the Jardín Principal on foot.",
    materials="Restored historic house; furnished and decorated, with art throughout; sound system.",
    condition="Ready; services included.",
    potential="Mid-term stays inside the center rather than next to it.",
    notes="It was designed to be lived in by someone who works surrounded by art. The balcony does the rest.",
    highlights=["Living-dining room with fireplace and a direct view of the Parroquia","Bedroom with king bed and full bathroom","Private balcony facing the Parroquia","Furnished and decorated; art throughout; sound system","Laundry room · water, electricity and internet included","Above Casa Cuadrante, in the historic center","Mid-term stays"],
    program=[("The apartment","Living-dining with fireplace · kitchen · bedroom with full bath · laundry · private balcony")],
    location="Inside Casa Cuadrante, in the historic center of San Miguel de Allende — restaurants, galleries and the Jardín Principal on foot.",
    img="img/ph-casa-cuadrante-01.jpg", gallery=['img/ph-casa-cuadrante-00.jpg', 'img/ph-casa-cuadrante-08.jpg', 'img/ph-casa-cuadrante-02.jpg', 'img/ph-casa-cuadrante-03.jpg', 'img/ph-casa-cuadrante-07.jpg', 'img/ph-casa-cuadrante-05.jpg'])

add(slug="panoramic-suite", page=True, city="sma", kind="rent", name="Panoramic Suite", where="Casa Cuadrante · Historic center · San Miguel de Allende",
    auth="Casa Cuadrante — restored and designed by RBC",
    status="Suite with private terrace · mid-term stays", price_mxn=40_000, price_per="month · services included", price_note=None,
    specs=[("300°","terrace view"),("1","queen bed"),("1","full bath"),("Services","included")],
    blurb="A suite with a large private terrace directly in front of the Parroquia — a 300-degree view of the town. Queen bed, full bath, mini-fridge.",
    intro="The Panoramic Suite is defined by its terrace: large, private and directly in front of the Parroquia, with the whole of San Miguel around it. Queen bed, full bathroom and mini-fridge; an outdoor kitchenette can be fitted on the terrace if needed. Loungers and tables outside. Services included; also available for short stays.",
    arch="A suite whose main room is outdoors: a large private terrace facing the Parroquia.",
    site="Roof level of Casa Cuadrante, historic center.",
    materials="Queen bed, full bath, mini-fridge; loungers and tables on the terrace; outdoor kitchenette on request.",
    condition="Ready; services included; short stays also available.",
    potential="Stays with an unobstructed view of the Parroquia, for a weekend or a season.",
    notes="Of the terraces I know in San Miguel, this is the one I would choose.",
    highlights=["Large private terrace with a 300° view of San Miguel, facing the Parroquia","Queen bed, full bathroom, mini-fridge","Outdoor kitchenette on the terrace on request","Loungers and tables on the terrace","Services included · mid-term stays","Short stays also available (Airbnb link pending)","Inside Casa Cuadrante, restored and designed by RBC"],
    program=[("The suite","Bedroom with queen bed · full bath · mini-fridge · private panoramic terrace")],
    location="Casa Cuadrante, historic center of San Miguel de Allende — the terrace faces the Parroquia directly.",
    img="img/san-miguel-de-allende-parroquia-view.jpg", gallery=["img/view-historic-center.jpg","img/valley-golden-hour.jpg"])

# ───────── COUNTRYSIDE NEAR SMA ─────────
add(slug="casa-ether", page=True, city="jalpa", kind="sale", name="Casa Ether", where="Road to Jalpa · 15 minutes from San Miguel de Allende",
    auth="Built by RBC · design developed from a prior scheme",
    status="Built · contemporary country house", price_mxn=None, price_note="Price on request",
    specs=[("Country","house"),("Italian","wood floors & ceilings"),("Spanish","kitchen"),("15 min","to San Miguel")],
    blurb="A contemporary country house 15 minutes from San Miguel: sliding glass walls that open fully to the landscape, Italian wood on floors and ceilings, a Spanish kitchen.",
    intro="Casa Ether began as a design received from elsewhere. RBC re-read it — circulations, proportions and material language — and built it. Sliding glass walls throughout open the house completely to the countryside, so interior and landscape read as one room. Italian hardwood on floors and ceilings, a Spanish kitchen, and elements taken from the land itself. Full presentation with plans and areas available on request.",
    arch="A country house recomposed from a previous scheme: circulations, proportions and materials were re-read so the plan opens entirely to the landscape.",
    site="Open countryside on the road to Jalpa, 15–20 minutes from the center of San Miguel.",
    materials="Italian hardwood on floors and ceilings; Spanish kitchen; elements from the land itself.",
    condition="Built and finished. Photography by Alejandro Torre.",
    potential="A finished contemporary house in open country this close to San Miguel.",
    notes="We took a design that was not ours and made it belong to the site. The glass walls were the decision that mattered.",
    highlights=["15–20 minutes from the center of San Miguel de Allende, in open countryside","Sliding glass doors throughout, opening completely to the landscape","Italian hardwood floors and ceilings · Spanish kitchen","Built by RBC","Photography by Alejandro Torre"],
    program=[("The house","Full presentation with plans and areas available on request")],
    location="On the road to Jalpa, 15–20 minutes from the center of San Miguel de Allende, in open countryside.",
    img="img/ig-DJ-iHIEx2Xi-1.jpg", gallery=["img/ig-DJ-iHIEx2Xi-4.jpg","img/ig-DJ-iHIEx2Xi-2.jpg","img/ig-DJ-iHIEx2Xi-3.jpg","img/ig-DJ-iHIEx2Xi-5.jpg","img/ig-DJ-iHIEx2Xi-6.jpg"])

# ───────── QUERÉTARO ─────────
add(slug="casa-travertino", page=True, city="qro", kind="sale", name="Casa Travertino", where="Club de Golf El Campanario · Querétaro",
    auth="Designed and built by RBC",
    status="Newly built", price_mxn=39_700_000,
    specs=[("3+1","bedrooms"),("4+2","baths"),("3","cars"),("Pool","& sun deck"),("Double","height")],
    blurb="Newly built on the last lot of its private street, facing the mountains: double-height living and bar, pool with sun deck, three en-suite bedrooms and a flexible en-suite room downstairs.",
    intro="Casa Travertino occupies the last lot of its private street inside El Campanario, which is why every terrace looks at the mountains. The ground floor is made for gathering: living room with bar and dining in double height, a kitchen with breakfast area, a covered terrace and a sun deck around the pool. Upstairs, three en-suite bedrooms, a family TV room and a lobby that works as a reading room or linen closet. Newly built; never lived in.",
    arch="Double-height living with bar and dining on the ground floor, terraces to the mountains; three en-suite bedrooms and a family room upstairs; a flexible en-suite room below.",
    site="Last lot of its private street in El Campanario golf club, Querétaro — open mountain views with nothing to be built in front.",
    materials="Newly built; stone, concrete and glass; pool with sun deck and covered terrace.",
    condition="New. Never lived in.",
    potential="The ground-floor suite absorbs a gym, an office or a fourth bedroom without touching the rest of the plan.",
    notes="The double height was drawn for the mountains. Sit at the bar late in the afternoon and the reason is obvious.",
    highlights=["Last lot of its private street — open mountain views","Double-height living room with bar, and dining room","Covered terrace, sun deck and pool with outdoor half-bath","Three en-suite bedrooms upstairs + family TV room + reading lobby","Ground-floor en-suite room for gym, bedroom or study","Kitchen with breakfast area, full staff quarters and service patio, storage","Three-car garage · guest half-bath","Designed and built by RBC"],
    program=[("Ground level","Garage for 3 cars · staff room with bath and service patio · kitchen with breakfast area · en-suite room (gym / study / bedroom) · living-bar and dining in double height · covered terrace · sun deck and pool · outdoor half-bath · guest half-bath · storage"),("Upper level","Three bedrooms with baths · family TV room · lobby for reading or linen")],
    location="Club de Golf El Campanario, Querétaro — the last lot of its private street, with open mountain views.",
    img="img/ig-C_3mXTMxFYj-1.jpg", gallery=["img/ig-C_3mXTMxFYj-2.jpg","img/ig-C_3mXTMxFYj-3.jpg"])

# ───────── CELAYA ─────────
add(slug="magno", page=False, city="celaya", kind="sale", name="Magno Home & Towers", where="Celaya · Guanajuato",
    auth="A development by Espacios y Formas",
    status="Apartments · homes · lots", price_mxn=None, price_note="Lots from MX $2.0M · Apartments from MX $4.3M · Homes from MX $5.5M",
    specs=[("Towers","& homes"),("Spa · pool","gym · club"),("Immediate","delivery units")],
    blurb="Residential towers, single-family homes and lots in one gated community in Celaya, developed by Espacios y Formas. Apartments available for immediate delivery.",
    intro="Magno Home & Towers combines residential towers, single-family homes and lots inside one gated community in Celaya, with spa, pool, gym, clubhouse, business center, bar, multipurpose hall, gardens and underground parking. Developed and built by Espacios y Formas; apartments available for immediate delivery.",
    arch="Residential towers, single-family homes and lots in one master-planned community.",
    site="Celaya, Guanajuato; about 45 minutes from Querétaro.",
    condition="Apartments with immediate delivery; homes and lots available.",
    potential="One community with three ways in — apartment, house or lot — and amenities already built.",
    notes="This is Espacios y Formas' project, not mine alone, but I know the floor plans well. Ask me which units I would consider.",
    highlights=["Apartments with immediate delivery","Homes and lots inside the same community","Spa · pool · gym · clubhouse · business center · gardens","24/7 gated security"],
    program=[("Availability","Ask for the current inventory and floor plans — units are released as they complete.")],
    location="Celaya, Guanajuato — about 45 minutes from Querétaro and 1 hour from San Miguel de Allende.",
    img="img/community-club-pool.jpg", href="work.html#magno", pdf=False,
    wa_msg="Hi Roberto, I'm interested in Magno in Celaya (apartments, homes or lots).")


def by(city, kind=None):
    return [l for l in L if l["city"] == city and (kind is None or l["kind"] == kind)]

def price_line(l, big=False):
    if l.get("price_mxn"):
        if l["kind"] == "rent":
            return f"{mdp(l['price_mxn'])} <small>· ≈ {usd(l['price_mxn'])} per {l.get('price_per','month')}</small>"
        return f"{usd(l['price_mxn'])} <small>· {mdp(l['price_mxn'])}</small>"
    return f"<span style='font-size:{'1.15rem' if big else '1rem'}'>{l.get('price_note','Price on request')}</span>"

SECTIONS = (("Architecture","arch"),("Site","site"),("Materials","materials"),("Condition","condition"),("Potential","potential"))

def notes_label():
    return "Roberto's Notes" + (' <i class="draft">draft · pending review</i>' if NOTES_DRAFT else "")

def property_page(l, wa, SITE):
    import fichas
    ph = fichas.photos(l)
    sp = "".join(f'<div><div class="n">{a}</div><div class="l">{b}</div></div>' for a, b in l["specs"])
    hl = "".join(f"<li>{h}</li>" for h in l["highlights"])
    prog = "".join(f'<div class="step rv"><h4>{a}</h4><p>{b}</p></div>' for a, b in l["program"])
    gal = "".join(f'<a class="lbx" href="{g}"><img src="{g}" alt="{l["name"]}" loading="lazy"></a>' for g in ph)
    secs = "".join(f'<div class="pp-sec rv"><small>{k}</small><p>{l[v]}</p></div>' for k, v in SECTIONS if l.get(v))
    plans = "".join(f'<a class="lbx" href="{p}"><img src="{p}" alt="{l["name"]} — plan" loading="lazy"></a>' for p in l.get("plans", []))
    rent = l["kind"] == "rent"
    msg = f"Hi Roberto, I'm interested in {l['name']} ({l['where']})."
    body = f"""
<header class="hero prop" id="top">
  <div class="bg" style="background-image:url('{l['img']}')"></div>
  <div class="in">
    <div class="crumbs"><a href="index.html">Home</a> › <a href="real-estate.html">Real Estate</a> › {l['name']}</div>
    <div class="tag">{'For rent' if rent else 'For sale'} · {l['where']}</div>
    <h1>{l['name']}</h1>
    <p class="sub">{l['blurb']}</p>
  </div>
</header>
<div class="pp-bar"><div class="in">
  <div class="pp-price">{price_line(l, True)}</div>
  <div class="pp-auth"><small>Status</small>{l['status']}</div>
  <div class="pp-auth"><small>Authorship</small>{l.get('auth','')}</div>
  <a class="btn red" href="{wa(msg)}">{'Ask about availability' if rent else 'Request information'}</a>
</div></div>
<div class="stats"><div class="in">{sp}</div></div>

<section id="house">
  <div class="wrap split" style="align-items:start;">
    <div class="rv">
      <div class="shead"><div class="eyebrow"><b>01</b>The {'space' if rent else 'house'}</div><i></i></div>
      <p class="lead">{l['intro']}</p>
      <ul class="checks">{hl}</ul>
    </div>
    <div class="rv d1">
      <div class="shead"><div class="eyebrow"><b>02</b>An architect's reading</div><i></i></div>
      {secs}
      <div class="notes"><small>{notes_label()}</small><p>{l.get('notes','')}</p><div class="sig">— R. Balderas Carrillo, Arquitecto</div></div>
    </div>
  </div>
</section>

<section class="band" id="program">
  <div class="wrap">
    <div class="shead rv"><div class="eyebrow"><b>03</b>Program</div><i></i></div>
    <div class="steps" style="grid-template-columns:repeat({min(3,len(l['program']))},1fr);">{prog}</div>
    {('<div class="shead rv" style="margin-top:50px;"><div class="eyebrow"><b>04</b>Plans</div><i></i></div><div class="pp-plans rv">'+plans+'</div>') if plans else '<p class="cap rv" style="margin-top:26px;">Plans available on request.</p>'}
  </div>
</section>

<section id="gallery">
  <div class="wrap">
    <div class="shead rv"><div class="eyebrow"><b>{'05' if plans else '04'}</b>Photographs</div><i></i></div>
    <div class="masonry rv d1">{gal}</div>
    <div class="cap rv" style="margin-top:12px;">Provisional images — photography in progress.</div>
    <div class="shead rv" style="margin-top:50px;"><div class="eyebrow"><b>{'06' if plans else '05'}</b>Location</div><i></i></div>
    <p class="lead rv" style="max-width:720px;">{l.get('location') or l['where']}</p>
  </div>
</section>

<section class="contact" id="contact">
  <div class="wrap">
    <div class="eyebrow rv" style="color:var(--gold);">{'Availability' if rent else 'Visits'}</div>
    <h2 class="rv d1">{'Ask about your dates.' if rent else 'See it in person, or on a video call.'}</h2>
    <p class="lead rv d2">English and Spanish. Roberto answers personally.</p>
    <div class="cgrid rv d2">
      <a class="btn red" href="{wa(msg)}">WhatsApp +52 461 101 2474</a>
      {('<a class="btn ghost lt" href="pdf/'+l['slug']+'.pdf" target="_blank" rel="noopener">Technical sheet (PDF)</a>') if l.get('pdf', True) else ''}
      <a class="btn ghost lt" href="real-estate.html">All properties</a>
    </div>
  </div>
</section>
"""
    city = {"sma":"San Miguel de Allende","qro":"Querétaro","jalpa":"near San Miguel de Allende","celaya":"Celaya"}[l["city"]]
    ld = [{"@context":"https://schema.org","@type":"RealEstateListing","name":f"{l['name']} — {l['where']}","url":f"{SITE}/{l['slug']}.html",
           "about":{"@type":"Accommodation" if rent else "SingleFamilyResidence","name":l["name"],"address":{"@type":"PostalAddress","addressLocality":"Querétaro" if l["city"]=="qro" else ("Celaya" if l["city"]=="celaya" else "San Miguel de Allende"),"addressCountry":"MX"}},
           "offers":{"@type":"Offer","priceCurrency":"MXN","price":str(l["price_mxn"]) if l.get("price_mxn") else "0","availability":"https://schema.org/InStock","seller":{"@type":"Person","name":"Roberto Balderas Carrillo","jobTitle":"Architect","telephone":"+524611012474"}}},
          {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE}/"},{"@type":"ListItem","position":2,"name":"Real Estate","item":f"{SITE}/real-estate.html"},{"@type":"ListItem","position":3,"name":l["name"],"item":f"{SITE}/{l['slug']}.html"}]}]
    title = f"{l['name']} — {'For rent' if rent else 'For sale'} in {city} | RBC · Roberto Balderas Carrillo, Arquitecto"
    desc = (l["blurb"][:150] + "…") if len(l["blurb"]) > 155 else l["blurb"]
    return (l["slug"], title, desc + " Presented by architect Roberto Balderas Carrillo. WhatsApp +52 461 101 2474.", body, l["img"], ld, "0.8")

def pages():
    return [l for l in L if l.get("page")]
