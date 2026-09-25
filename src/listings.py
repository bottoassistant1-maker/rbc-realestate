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
add(slug="casa-horizonte", page=True, city="sma", kind="sale", name="Casa Horizonte · M4-L7", where="Peñas Arriba · San Miguel de Allende",
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
    img="img/pa-hz-r01.jpg",
    gallery=['img/pa-hz-r03.jpg', 'img/pa-hz-r04.jpg', 'img/pa-hz-r09.jpg', 'img/pa-hz-r02.jpg', 'img/pa-hz-r08.jpg', 'img/pa-hz-r07.jpg', 'img/pa-hz-r10.jpg', 'img/pa-hz-r18.jpg', 'img/pa-hz-r11.jpg', 'img/pa-hz-r06.jpg', 'img/pa-hz-r14.jpg', 'img/pa-hz-r15.jpg', 'img/pa-hz-r16.jpg', 'img/pa-hz-r12.jpg'],
    plans=['img/pa-hz-plan-pb-2.jpg', 'img/pa-hz-plan-p1-2.jpg', 'img/pa-hz-plan-section-2.jpg', 'img/pa-hz-plan-pa.jpg', 'img/pa-hz-plan-pb.jpg'])

HIDDEN_MIRADOR = dict(slug="casa-mirador", page=True, city="sma", kind="sale", name="Casa Mirador", where="Historic center · San Miguel de Allende",
    auth="Represented by RBC",
    status="Finished · furnished", price_mxn=None, price_note="Price on request",
    specs=[("4","levels"),("2","bedrooms"),("2½","baths"),("1","car"),("Rooftop","jacuzzi")],
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
    img="img/view-historic-center.jpg", gallery=["img/san-miguel-de-allende-parroquia-view.jpg"])  # hidden for now (Roberto, sep 2026)

add(slug="casa-zafiro", page=False, city="sma", kind="sale", name="Casa Zafiro · M1-L14", where="Peñas Arriba · San Miguel de Allende",
    auth="Peñas Arriba · built with Espacios y Formas",
    status="Shell built · ~6 months to delivery", price_mxn=13_900_000,
    specs=[("343","m² built · 3,692 sq ft"),("418","m² lot · 4,500 sq ft"),("4+s","bedrooms"),("4½","baths"),("2","cars")],
    blurb="On the largest garden lot of the community, built to shell: plan and site are done, every finish is still open.",
    intro="Casa Zafiro sits on the largest garden lot in Peñas Arriba. It is built to shell stage, with delivery in about six months once the finishes are defined together with the practice.",
    arch="Compact plan opening to terrace and garden; master suite on the main level.",
    site="Lot M1-L14, a 418 m² garden lot inside the gated community, with views of the center and the Parroquia.",
    materials="Built to shell — flooring, stone, carpentry and paint still to be chosen.",
    condition="Shell complete; about six months to delivery once finishes are defined.",
    potential="The plan and the site without waiting for a full build, and the level of finish set to the buyer's budget.",
    notes="The garden is the argument. It is the biggest lot in the community and the shell is already there; what remains is the part most owners enjoy deciding.",
    highlights=["Payment plan: 40% at signing, the balance in monthly payments until delivery (~6 months)","343.7 m² (3,700 sq ft) built on a 4,500 sq ft garden lot","4 bedrooms + staff · 4½ baths · 2 cars","Shell built — flooring, stone, carpentry and paint chosen by the buyer","Views of the historic center and the Parroquia","Inside gated Peñas Arriba: pool, gym, restaurant, 24/7 security"],
    program=[("The house","Living-dining and kitchen open to terrace and garden · master suite · three further bedrooms · staff quarters · two-car garage")],
    location="Lot M1-L14, Peñas Arriba, San Miguel de Allende — about 7 minutes from the historic center.",
    img="img/pa-zaf-r01.jpg", wa_msg="Hi Roberto, I'm interested in Casa Zafiro M1-L14.", gallery=['img/pa-zaf-r02.jpg'], plans=['img/pa-zaf-plan-pb-opt1.jpg', 'img/pa-zaf-plan-pb-opt2.jpg', 'img/pa-zaf-plan-pa-2.jpg', 'img/pa-zaf-lote-m1l14.jpg', 'img/pa-zaf-lote-m1l15.jpg', 'img/pa-zaf-plan-master.jpg'])

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
    highlights=["Option to add a pool with a view of the historic center inside the garden","763.55 m² lot (8,219 sq ft) · 592.06 m² built (6,373 sq ft)","Double-height living, dining and bar opening to terrace and garden","Master suite on the social level: walk-in closet, two baths, private sitting room, double view","Upper level: three double bedrooms, each with full bath, and a TV lounge","Kitchen with pantry room, staff quarters, garage and storage","Option to add a pool facing the historic center","Shell built — finishes chosen with the architect"],
    program=[("Ground level","Garage and storage · master suite with walk-in, two baths and sitting room · double-height living, dining and bar · kitchen with pantry · staff room · terrace with dining and lounge · garden"),("Upper level","TV lounge · three double bedrooms with full baths"),("Baths","6 full + 2 guest half-baths")],
    location="Lot M6-L1, the first house of block 6 in Peñas Arriba, San Miguel de Allende — about 7 minutes from the historic center.",
    img="img/pa-cima-r01.jpg", gallery=['img/pa-cima-r05.jpg', 'img/pa-cima-r03.jpg', 'img/pa-cima-r04.jpg'], plans=['img/pa-cima-plan-pb.jpg', 'img/pa-cima-plan-pa.jpg'])

add(slug="duplex", page=False, city="sma", kind="sale", name="Duplex residences", where="Peñas Arriba · San Miguel de Allende",
    auth="Peñas Arriba · built with Espacios y Formas",
    status="Built and under construction", price_mxn=None, price_note="From MX $6.6M",
    specs=[("4","units available"),("188–205","m²"),("3","bedrooms"),("3","full baths"),("2","cars")],
    blurb="Two-level duplex houses in Peñas Arriba: a garden residence on the ground floor and an upper residence with the view of the historic center. Three units available.",
    intro="The duplex houses of Peñas Arriba pair a ground-floor garden residence with an upper, apartment-style residence, each with its own entrance, kitchen, living-dining, three bedrooms, three bathrooms and two parking spaces. Buy one unit or both. The upper residence has a single price on every lot; the garden residence varies with the size of its garden. Two units are already built; finishes are chosen by the buyer.",
    arch="Two independent residences per building: the garden residence opens to a private garden; the upper residence is a single level facing the view.",
    site="Blocks 1 and 5 of Peñas Arriba; the M5 units sit next to the clubhouse and pool.",
    materials="Stone, wood pergolas and clay tile roofs; finishes chosen with the practice.",
    condition="Built; about six months to delivery.",
    potential="Lock-and-leave living inside a gated community, with the club a few steps away.",
    notes="The garden units are for anyone who wants breakfast outside; the upper unit is for the view.",
    highlights=["Buy the whole duplex (≈ 393 m²) or one unit: upper residence at a single MX $6.6M price on every lot; garden residence from MX $7.433M depending on the garden","3 bedrooms · 3 full baths · 2 parking spaces per unit","Several façades and interior layouts to choose from","Block 5 units sit next to the clubhouse and pool"],
    units=[("Upper residence · M1-L12","≈ 205 m² · single level · already built","MX $6,600,000"),
           ("Garden residence · M5-L9","≈ 188 m² · private garden on a 322 m² lot · already built","MX $7,433,000"),
           ("Garden residence · M5-L2","190 m² · private garden on a 363 m² lot","MX $8,232,000"),
           ("Upper residence · M5-L2","≈ 205 m² · single level","MX $6,600,000")],
    program=[("Garden residence","Living-dining and kitchen opening to the garden · 3 bedrooms · 3 baths · laundry · 1 car"),("Upper residence","Single level: living-dining, kitchen, terrace with the view · 3 bedrooms · 3 baths · laundry · 1 car")],
    location="Peñas Arriba, San Miguel de Allende.",
    img="img/pa-dup-r01.jpg", wa_msg="Hi Roberto, I'm interested in the duplex residences in Peñas Arriba. Which units are available?", gallery=['img/pa-dup-r02.jpg', 'img/pa-dup-r05.jpg'], plans=['img/pa-dup-plan-pb.jpg', 'img/pa-dup-plan-pa.jpg', 'img/pa-dup-plan-m1l12.jpg', 'img/pa-dup-plan-m5l2.jpg', 'img/pa-dup-plan-m5l9.jpg', 'img/pa-dup-lote-m1l12.jpg', 'img/pa-dup-lote-m5l2.jpg', 'img/pa-dup-lote-m5l9.jpg', 'img/pa-dup-plan-master.jpg'])

# ───────── SAN MIGUEL · rent ─────────
add(slug="casa-musa", page=True, city="sma", kind="rent", name="Casa Musa", where="For rent · Historic center · San Miguel de Allende",
    auth="Casa Cuadrante — restored and designed by RBC",
    status="For rent · Historic center", price_mxn=None, price_note="Price on request",
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
    img="img/ph-musa-n07.jpg", gallery=['img/ph-musa-n35.jpg', 'img/ph-musa-n09.jpg', 'img/ph-musa-n05.jpg', 'img/ph-musa-n23.jpg', 'img/ph-musa-n13.jpg', 'img/ph-musa-n14.jpg', 'img/ph-musa-n17.jpg', 'img/ph-musa-n28.jpg', 'img/ph-musa-n29.jpg', 'img/ph-musa-n30.jpg', 'img/ph-musa-n31.jpg', 'img/ph-musa-n33.jpg', 'img/ph-musa-n27.jpg', 'img/ph-musa-n24.jpg', 'img/ph-musa-n01.jpg', 'img/ph-musa-n20.jpg', 'img/ph-cuad-n03.jpg', 'img/ph-cuad-n01.jpg'])

add(slug="panoramic-suite", page=True, city="sma", kind="rent", name="Panoramic Suite", where="For rent · Historic center · San Miguel de Allende",
    auth="Casa Cuadrante — restored and designed by RBC",
    status="For rent · Historic center", price_mxn=None, price_note="Price on request",
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
    img="img/ph-suite-n19.jpg", gallery=['img/ph-suite-n15.jpg', 'img/ph-suite-n16.jpg', 'img/ph-suite-n11.jpg', 'img/ph-suite-n17.jpg', 'img/ph-suite-n18.jpg', 'img/ph-suite-n08.jpg', 'img/ph-suite-n14.jpg', 'img/ph-suite-n10.jpg', 'img/ph-suite-n12.jpg', 'img/ph-suite-n01.jpg', 'img/ph-suite-n20.jpg', 'img/ph-cuad-n02.jpg'])

# ───────── COUNTRYSIDE NEAR SMA ─────────
add(slug="casa-ether", page=True, city="jalpa", kind="sale", name="Casa Ether", where="Piedras Azules · 20 minutes from San Miguel de Allende",
    auth="Built by RBC · design developed from a prior scheme",
    status="Built · contemporary country estate", price_mxn=None, price_usd=2_200_000,
    specs=[("1,159","m² built · 12,475 sq ft"),("7,999","m² lot · 1.98 acres"),("4","bedrooms · all en suite"),("4+2","baths"),("2","levels"),("20 min","to San Miguel")],
    blurb="A contemporary country estate on a private hilltop: double-height ceilings, oak floors and walls of glass that open to mountain views in every direction. Lap pool, jacuzzi and fire pit.",
    intro="Casa Ether sits on a private hilltop of 7,999 m² inside Rancho Piedras Azules, twenty minutes from the center of San Miguel de Allende. Double-height ceilings, Sacarella oak floors and wood-panelled ceilings run through open living and dining spaces that slide open onto a wrap-around deck, a lap pool, a jacuzzi and a gas fire pit with step-down seating. Four en-suite bedrooms, a family TV room, kitchen with marble island and walk-in pantry, cava and bar, a pétanque court and a rooftop terrace; staff room and services. Mountain and valley views in every direction.",
    arch="Two levels on a hilltop: a long, low volume with a cantilevered roof plane, double-height living spaces and glass walls that dissolve the interior into the landscape.",
    site="Lot 15, Rancho Piedras Azules, Palo Blanco, Guanajuato — a gated community with an access road and complete privacy; 20 minutes from San Miguel de Allende centro. Views of the sierra and the valley on every side.",
    materials="Sacarella oak floors; wood-panelled ceilings; marble island and master bathroom; double-paned windows; stone and concrete outside; agave gardens.",
    condition="Built and finished; designer furnishings and art. Security system, ample parking.",
    potential="A finished contemporary house of this scale, on nearly two hectares of private country this close to San Miguel, is rare.",
    notes="Construction and design intervened by RBC on an existing siting and scheme.",
    highlights=["1,159 m² (12,475 sq ft) built on a 7,999 m² (1.98 acres) hilltop lot","4 bedrooms including the master, each with its own full bath · 2 additional half baths · staff room","Pool, jacuzzi, pétanque court and gas fire pit with step-down seating · rooftop","Living room with open kitchen (can be closed off) · family TV room · bar · cava","Sacarella oak floors · wood-panelled ceilings · marble master bath","Staff room · security system · parking for 3 cars","Gated community, 20 minutes from San Miguel de Allende centro"],
    program=[("Entry level","Master suite with walk-in closet, full bath and terrace · 3 bedrooms with full baths · family TV room · terrace · parking for 3 cars"),("Lower level","Living and dining with open kitchen (can be closed off) · bar · cava · pantry · half baths · terrace with pool, jacuzzi and fire pit · pétanque court · staff room, laundry and services"),("Rooftop","Open roof terrace with mountain and valley views")],
    location="Lot 15, Rancho Piedras Azules, Palo Blanco, Guanajuato — 20 minutes from San Miguel de Allende centro. Gated; mountain and valley views in every direction.",
    img="img/ph-casa-ether-00.jpg", gallery=['img/ph-casa-ether-01.jpg', 'img/ph-casa-ether-02.jpg', 'img/ph-casa-ether-03.jpg', 'img/ph-casa-ether-04.jpg', 'img/ph-casa-ether-05.jpg', 'img/ph-casa-ether-06.jpg', 'img/ph-casa-ether-07.jpg', 'img/ph-casa-ether-08.jpg', 'img/ph-casa-ether-09.jpg', 'img/ph-casa-ether-10.jpg', 'img/ph-casa-ether-11.jpg', 'img/ph-casa-ether-12.jpg', 'img/ph-casa-ether-13.jpg', 'img/ph-casa-ether-14.jpg', 'img/ph-casa-ether-15.jpg'], plans=['img/ph-casa-ether-plan-pb.jpg','img/ph-casa-ether-plan-m1.jpg','img/ph-casa-ether-plan-site.jpg'])

# ───────── QUERÉTARO ─────────
add(slug="casa-travertino", page=True, city="qro", kind="sale", name="Casa Travertino", where="El Campanario Residencial & Golf · Querétaro",
    auth="Designed and built by RBC",
    status="Newly built", price_mxn=39_700_000,
    specs=[("731","m² built · 7,868 sq ft"),("1,102","m² lot · 11,858 sq ft"),("4","bedrooms"),("Staff","quarters"),("4+2","baths"),("3","cars"),("Pool","& sun deck")],
    blurb="Newly built on the last lot of its private street, facing the mountains: double-height living and bar, pool with sun deck, four en-suite bedrooms (three upstairs, one on the ground floor) plus staff quarters.",
    intro="Casa Travertino occupies the last lot of its private street inside El Campanario Residencial & Golf, which is why every terrace looks at the mountains. The ground floor is made for gathering: living room with bar and dining in double height, a kitchen with breakfast area, a covered terrace and a sun deck around the pool. Four en-suite bedrooms in all — three upstairs with a family TV room and a lobby that works as a reading room or linen closet, plus one on the ground floor — and full staff quarters. Newly built; never lived in.",
    arch="Double-height living with bar and dining on the ground floor, terraces to the mountains; four en-suite bedrooms — three upstairs with a family room, one on the ground floor — plus staff quarters.",
    site="Last lot of its private street in El Campanario Residencial & Golf, Querétaro — open mountain views with nothing to be built in front.",
    materials="Newly built; stone, concrete and glass; pool with sun deck and covered terrace.",
    condition="New. Never lived in.",
    potential="The ground-floor suite absorbs a gym, an office or a fourth bedroom without touching the rest of the plan.",
    notes="The double height was drawn for the mountains. Sit at the bar late in the afternoon and the reason is obvious.",
    highlights=["731 m² (7,868 sq ft) built on a 1,101.65 m² (11,858 sq ft) lot","Last lot of its private street — open mountain views","Double-height living room with bar, and dining room","Covered terrace, sun deck and pool with outdoor half-bath","Four en-suite bedrooms + staff quarters","Three bedrooms upstairs with family TV room and reading lobby; a fourth en-suite bedroom on the ground floor (also gym or study)","Kitchen with breakfast area, full staff quarters and service patio, storage","Three-car garage · guest half-bath","Designed and built by RBC"],
    program=[("Ground level","Garage for 3 cars · staff room with bath and service patio · kitchen with breakfast area · fourth en-suite bedroom (also gym / study) · living-bar and dining in double height · covered terrace · sun deck and pool · outdoor half-bath · guest half-bath · storage"),("Upper level","Three bedrooms with baths · family TV room · lobby for reading or linen")],
    location="El Campanario Residencial & Golf, Querétaro — the last lot of its private street, with open mountain views.",
    img="img/ph-travertino-r01.jpg", gallery=["img/ph-travertino-r02.jpg","img/ph-travertino-r03.jpg"])

# ───────── CELAYA ─────────
add(slug="magno-apartment", page=False, city="celaya", kind="sale", name="Magno Towers · Apartments", where="Celaya · Guanajuato",
    auth="A development by Espacios y Formas",
    status="Immediate delivery", price_mxn=None, price_note="From MX $4.65M · 26 apartments available",
    specs=[("2–3","bedrooms"),("171–229","m² living"),("18","floors"),("Immediate","delivery")],
    blurb="Apartments in the Magno tower in Celaya, developed and built by Espacios y Formas: 2 and 3 bedrooms, 171 to 229 m² of living space plus parking and storage, with spa, pool, gym and clubhouse. 26 apartments available for immediate delivery.",
    intro="Magno Towers is the residential tower of Magno Home & Towers, a gated community in Celaya developed and built by Espacios y Formas. Every apartment comes with two parking spaces and a storage room (about 31–43 m²) on top of its living area, and shares the spa, pool, gym, clubhouse, business center, bar, multipurpose hall and gardens of the community. Twenty-six apartments are available for immediate delivery (price list 2026, list below); the furnished showroom apartment can be visited online.",
    arch="A single tower of 18 floors, four to five apartments per floor; the larger 228–229 m² units occupy the corners from the seventh floor up.",
    site="Magno Home & Towers, Celaya, Guanajuato; about 45 minutes from Querétaro.",
    condition="Finished; immediate delivery.",
    potential="A furnished apartment inside a community whose amenities are already built — the showroom tour shows the finished standard.",
    notes="This is Espacios y Formas' project, not mine alone, but I know the floor plans well. Ask me which units I would consider.",
    highlights=["26 apartments available · immediate delivery","2 and 3 bedrooms · 171 to 229 m² of living space","Two parking spaces and a storage room with every apartment","Spa · pool · gym · clubhouse · business center · gardens","24/7 gated security with double access"],
    units=[('Apartment 204 · floor 2', '187.84 m² living + 31.69 m² parking & storage · 3 bedrooms', 'MX $5,058,067'),
 ('Apartment 205 · floor 2', '180.8 m² living + 30.78 m² parking & storage · 3 bedrooms', 'MX $4,875,471'),
 ('Apartment 301 · floor 3', '170.88 m² living + 30.88 m² parking & storage · 3 bedrooms', 'MX $4,649,300'),
 ('Apartment 304 · floor 3', '186.75 m² living + 30.64 m² parking & storage · 3 bedrooms', 'MX $5,011,035'),
 ('Apartment 401 · floor 4', '170.88 m² living + 30.94 m² parking & storage · 3 bedrooms', 'MX $4,673,948'),
 ('Apartment 404 · floor 4', '186.75 m² living + 31.11 m² parking & storage · 3 bedrooms', 'MX $5,046,993'),
 ('Apartment 405 · floor 4', '180.8 m² living + 30.88 m² parking & storage · 3 bedrooms', 'MX $4,902,177'),
 ('Apartment 504 · floor 5', '186.75 m² living + 31.14 m² parking & storage · 3 bedrooms', 'MX $5,047,688'),
 ('Apartment 604 · floor 6', '186.75 m² living + 31.01 m² parking & storage · 3 bedrooms', 'MX $5,069,786'),
 ('Apartment 605 · floor 6', '180.8 m² living + 30.74 m² parking & storage · 3 bedrooms', 'MX $4,923,318'),
 ('Apartment 901 · floor 9', '170.88 m² living + 30.98 m² parking & storage · 3 bedrooms', 'MX $4,767,952'),
 ('Apartment 903 · floor 9', '228.34 m² living + 31.3 m² parking & storage · 3 bedrooms', 'MX $6,132,925'),
 ('Apartment 1102 · floor 11', '229.49 m² living + 30.97 m² parking & storage · 3 bedrooms', 'MX $6,271,924'),
 ('Apartment 1201 · floor 12', '170.88 m² living + 30.98 m² parking & storage · 3 bedrooms', 'MX $4,907,569'),
 ('Apartment 1204 · floor 12', '180.8 m² living + 35.72 m² parking & storage · 3 bedrooms', 'MX $5,263,913'),
 ('Apartment 1301 · floor 13', '170.88 m² living + 35.28 m² parking & storage · 3 bedrooms', 'MX $5,059,692'),
 ('Apartment 1303 · floor 13', '228.34 m² living + 35.72 m² parking & storage · 2 bedrooms', 'MX $6,480,904'),
 ('Apartment 1401 · floor 14', '170.88 m² living + 35.28 m² parking & storage · 3 bedrooms', 'MX $5,107,223'),
 ('Apartment 1501 · floor 15', '170.88 m² living + 35.28 m² parking & storage · 3 bedrooms', 'MX $5,154,754'),
 ('Apartment 1504 · floor 15', '180.8 m² living + 35.72 m² parking & storage · 3 bedrooms', 'MX $5,413,667'),
 ('Apartment 1601 · floor 16', '170.88 m² living + 35.28 m² parking & storage · 3 bedrooms', 'MX $5,202,284'),
 ('Apartment 1604 · floor 16', '180.8 m² living + 33.98 m² parking & storage · 3 bedrooms', 'MX $5,368,658'),
 ('Apartment 1701 · floor 17', '170.88 m² living + 37.13 m² parking & storage · 3 bedrooms', 'MX $5,296,948'),
 ('Apartment 1704 · floor 17', '180.8 m² living + 35.78 m² parking & storage · 3 bedrooms', 'MX $5,515,032'),
 ('Apartment 1801 · floor 18', '177.55 m² living + 43.3 m² parking & storage · 2 bedrooms', 'MX $5,945,641'),
 ('Apartment 1802 · floor 18', '173.03 m² living + 40.21 m² parking & storage · 2 bedrooms', 'MX $5,740,767')],
    program=[("Apartment 1303 (plan shown)","228 m² living + 36 m² parking & storage = 264 m² total · living, dining, kitchen, TV room, terrace · primary suite with walk-in · second bedroom with bath · service room · MX $6,480,904"),("Availability","Price list 2026 by Espacios y Formas; units are released as they complete — ask for the current list.")],
    location="Celaya, Guanajuato — about 45 minutes from Querétaro and 1 hour from San Miguel de Allende.",
    img="img/magno-1.jpg", gallery=["img/magno-3.jpg","img/magno-6.jpg","img/ob-magno-towers-a-02.jpg"], plans=["img/magno-plan-1303.jpg"], href="magno.html", pdf=False,
    links=[("Virtual tour of the showroom apartment","https://goo.gl/maps/GToGB8UTHR4UdR3HA")],
    wa_msg="Hi Roberto, I'm interested in an apartment in Magno Towers, Celaya.")

add(slug="magno-home", page=False, city="celaya", kind="sale", name="Magno Homes · Houses & lots", where="Celaya · Guanajuato",
    auth="A development by Espacios y Formas",
    status="Houses and lots", price_mxn=None, price_note="Homes from MX $5.5M · Lots from MX $2.0M",
    specs=[("Single-family","homes"),("225–450","m² lots"),("Spa · pool","gym · club")],
    blurb="Single-family homes and residential lots inside Magno Home & Towers, Celaya, developed by Espacios y Formas. Lots of 225 to 450 m² in Cluster 1, with the spa, pool, gym and clubhouse already built.",
    intro="Magno Home & Towers combines residential towers, single-family homes and lots inside one gated community in Celaya, with spa, pool, gym, clubhouse, business center, bar, multipurpose hall, gardens and underground parking. Developed and built by Espacios y Formas; apartments available for immediate delivery.",
    arch="Residential towers, single-family homes and lots in one master-planned community.",
    site="Celaya, Guanajuato; about 45 minutes from Querétaro.",
    condition="Apartments with immediate delivery; homes and lots available.",
    potential="One community with three ways in — apartment, house or lot — and amenities already built.",
    notes="This is Espacios y Formas' project, not mine alone, but I know the floor plans well. Ask me which units I would consider.",
    highlights=["Apartments with immediate delivery","Homes and lots inside the same community","Spa · pool · gym · clubhouse · business center · gardens","24/7 gated security"],
    program=[("Lots · Cluster 1","Lots of about 225 m² (9 × 25 m), 300 m² (12 × 25 m), 360 m² and 450 m² (15 × 30 m); availability plan of September 2026 shown."),("Homes","Houses built by Espacios y Formas on the community's lots, from MX $5.5M; ask for the current models.")],
    location="Celaya, Guanajuato — about 45 minutes from Querétaro and 1 hour from San Miguel de Allende.",
    img="img/magno-4.jpg", gallery=["img/magno-8.jpg","img/magno-2.jpg","img/magno-5.jpg"], plans=["img/magno-plan-lots-cluster1.jpg"], href="magno.html", pdf=False,
    wa_msg="Hi Roberto, I'm interested in a house or lot in Magno, Celaya.")

# ───────── LA NUEVA ESCONDIDA (completed · units for sale) ─────────
add(slug="nueva-escondida", page=False, city="sma", kind="sale", name="La Nueva Escondida", where="San Miguel de Allende",
    auth="A development by Espacios y Formas",
    status="Completed · a few units available", price_mxn=None, price_note="Price on request",
    specs=[("Completed","community"),("A few","units for sale"),("Pool","& gardens")],
    blurb="A residential community in San Miguel de Allende, now completed. A few units remain available for sale — ask for the current availability.",
    intro="A residential community in San Miguel de Allende, now completed. A few units remain available for sale — ask for the current availability.",
    arch="—", site="—", materials="—", condition="Completed; a few units available.", potential="—",
    notes="", highlights=["Completed community","A few units available for sale","Built by Espacios y Formas"], program=[],
    location="San Miguel de Allende.",
    img="img/ph-nesc-08.jpg", gallery=['img/ph-nesc-01.jpg', 'img/ph-nesc-03.jpg', 'img/ph-nesc-13.jpg', 'img/ph-nesc-15.jpg', 'img/ph-nesc-21.jpg', 'img/ph-nesc-24.jpg', 'img/ph-nesc-05.jpg', 'img/ph-nesc-11.jpg', 'img/ph-nesc-19.jpg', 'img/ph-nesc-23.jpg'],
    href="real-estate.html#nueva-escondida", pdf=False,
    wa_msg="Hi Roberto, I'm interested in the available units at La Nueva Escondida, San Miguel de Allende.")


def by(city, kind=None):
    return [l for l in L if l["city"] == city and (kind is None or l["kind"] == kind)]

def price_line(l, big=False):
    if l.get("price_usd"):
        return f"US ${l['price_usd']:,}"
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
      <a class="btn red" href="{wa(msg)}">WhatsApp Roberto</a>
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
    return (l["slug"], title, desc + " Presented by architect Roberto Balderas Carrillo.", body, l["img"], ld, "0.8")

def pages():
    return [l for l in L if l.get("page")]
