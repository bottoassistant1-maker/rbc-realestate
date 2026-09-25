# -*- coding: utf-8 -*-
"""v23 — Spanish version. Exact-string map EN → ES applied to the built HTML (text nodes, alt/title,
meta descriptions, page titles and the FICHAS JSON). Unknown strings fall back to English."""
import re

T = {
# ── nav / chrome ──
"Architecture &amp; Design": "Arquitectura y Diseño", "Architecture & Design": "Arquitectura y Diseño",
"Architecture": "Arquitectura", "Real Estate": "Bienes Raíces", "Construction": "Construcción",
"Home": "Inicio", "Contact": "Contacto", "Menu": "Menú", "Close": "Cerrar",
"Arquitecto": "Arquitecto", "Privacy notice": "Aviso de privacidad", "Terms": "Aviso legal",
"Show phone number": "Mostrar teléfono", "Show number": "Mostrar número", "WhatsApp Roberto": "WhatsApp con Roberto",
"OK": "OK", "Instagram": "Instagram", "Website": "Sitio web", "Offices": "Oficinas",
"Architecture, construction and selected properties.": "Arquitectura, construcción y propiedades seleccionadas.",
"San Miguel de Allende · Bajío · México.": "San Miguel de Allende · Bajío · México.",
"In collaboration with": "En colaboración con",
"© 2026 RBC · Roberto Balderas Carrillo, Arquitecto": "© 2026 RBC · Roberto Balderas Carrillo, Arquitecto",
"This site sets no cookies of its own. Typefaces are served by Google Fonts and the site is hosted by Vercel, which may log technical data.":
 "Este sitio no instala cookies propias. Las tipografías se sirven desde Google Fonts y el sitio se aloja en Vercel, que puede registrar datos técnicos.",
"Prices in MXN; USD figures are approximate references. Images may be renders or provisional; specifications, availability and delivery subject to change. This site does not constitute a binding offer.":
 "Precios en MXN; las cifras en USD son referencias aproximadas. Las imágenes pueden ser renders o provisionales; especificaciones, disponibilidad y entrega sujetas a cambio. Este sitio no constituye una oferta vinculante.",
"Roberto replies personally · Video calls for clients abroad": "Roberto responde personalmente · Videollamadas para clientes en el extranjero",
"Sends your answers to Roberto on WhatsApp. Nothing is stored on this website.": "Envía tus respuestas a Roberto por WhatsApp. Este sitio no almacena nada.",
"Goes to Roberto's WhatsApp.": "Llega al WhatsApp de Roberto.",
"WhatsApp is fastest. English and Spanish.": "WhatsApp es lo más rápido. Español e inglés.",
"English and Spanish. Roberto answers personally.": "Español e inglés. Roberto responde personalmente.",

# ── home ──
"Roberto Balderas Carrillo, Arquitecto — Architecture, Real Estate and Construction in San Miguel de Allende | RBC":
 "Roberto Balderas Carrillo, Arquitecto — Arquitectura, Bienes Raíces y Construcción en San Miguel de Allende | RBC",
"RBC is the practice of architect Roberto Balderas Carrillo in San Miguel de Allende: architecture and design, a selection of properties and developments, and construction with Espacios y Formas.":
 "RBC es el despacho del arquitecto Roberto Balderas Carrillo en San Miguel de Allende: arquitectura y diseño, una selección de propiedades y desarrollos, y construcción con Espacios y Formas.",
"San Miguel de Allende · Bajío · México": "San Miguel de Allende · Bajío · México",
"Roberto Balderas Carrillo is an architect based in San Miguel de Allende. His practice, RBC, designs and builds — houses, interiors, hotels, commercial buildings — and represents a small selection of properties he knows well.":
 "Roberto Balderas Carrillo es un arquitecto con base en San Miguel de Allende. Su despacho, RBC, diseña y construye —casas, interiores, hoteles, edificios comerciales— y representa una pequeña selección de propiedades que conoce bien.",
"Each project develops its own architectural language. Larger works are built with": "Cada proyecto desarrolla su propio lenguaje arquitectónico. Las obras mayores se construyen con",
", architecture, construction and development, with offices in Celaya and San Miguel de Allende.": ", arquitectura, construcción y desarrollo, con oficinas en Celaya y San Miguel de Allende.",
"Espacios y Formas ↗": "Espacios y Formas ↗",
"Houses, interiors, hospitality, commercial.": "Casas, interiores, hospitalidad, comercial.",
"Selected properties and developments.": "Propiedades y desarrollos seleccionados.",
"Directed personally; built with Espacios y Formas.": "Dirigida personalmente; construida con Espacios y Formas.",
"Design and build.": "Diseño y construcción.",

# ── architecture page ──
"Architecture & Design — Roberto Balderas Carrillo, Arquitecto | RBC": "Arquitectura y Diseño — Roberto Balderas Carrillo, Arquitecto | RBC",
"Architecture and interior design projects by Roberto Balderas Carrillo in San Miguel de Allende, Querétaro, Celaya and beyond: houses, hotels, bars, stores and offices.":
 "Proyectos de arquitectura e interiorismo de Roberto Balderas Carrillo en San Miguel de Allende, Querétaro, Celaya y más allá: casas, hoteles, bares, tiendas y oficinas.",
"RBC / Architecture & Design": "RBC / Arquitectura y Diseño", "Architecture & Design.": "Arquitectura y Diseño.",
"Houses, interiors, hotels, bars, stores and offices.": "Casas, interiores, hoteles, bares, tiendas y oficinas.",
"› Architecture & Design": "› Arquitectura y Diseño",
"All": "Todos", "Homes": "Casas", "Business": "Comercial", "Other": "Otros",
"Photography pending": "Fotografía pendiente",
"Start a project": "Iniciar un proyecto", "Tell me about the site.": "Cuéntame del terreno.",
"A lot, a house to renovate, a building to plan. English and Spanish.": "Un terreno, una casa por renovar, un edificio por planear. Español e inglés.",
"Construction and design intervened by RBC on an existing siting and scheme": "Construcción y diseño intervenidos por RBC sobre un sembrado y planteamiento existentes",
"Construction and design intervened by RBC on an existing siting and scheme.": "Construcción y diseño intervenidos por RBC sobre un sembrado y planteamiento existentes.",
# project names / places (only the ones with English words)
"Private art pavilion": "Pabellón de arte privado", "Hotel Casa X": "Hotel Casa X", "Bar Bachus": "Bar Bachus",
"Casa Cuadrante — restaurant & residence": "Casa Cuadrante — restaurante y residencia",
"Amecsa dealership": "Agencia Amecsa", "Condesa apartment façade": "Fachada de departamentos, Condesa",
"Daily Veggies offices": "Oficinas Daily Veggies", "Casa de Campo, San Miguel": "Casa de Campo, San Miguel",
"Restaurants in San Miguel": "Restaurantes en San Miguel", "Commercial & residential plaza": "Plaza comercial y residencial",
"Tuluminati stores": "Tiendas Tuluminati", "Wellness complex": "Complejo wellness", "Apartment JC": "Departamento JC",
"Casa Cien suites": "Suites Casa Cien", "Origen store": "Tienda Origen", "Casa Artista": "Casa Artista",
"Binary Code Pavilion & parametric studies": "Pabellón Binary Code y estudios paramétricos",
"Car dealership": "Agencia de autos", "Peñas Arriba — site": "Peñas Arriba — obra", "Casa de la Peña": "Casa de la Peña",
"Historic center · San Miguel de Allende": "Centro histórico · San Miguel de Allende",
"Historic center · San Miguel de Allende · 2023": "Centro histórico · San Miguel de Allende · 2023",
"Historic center · San Miguel de Allende · 2024": "Centro histórico · San Miguel de Allende · 2024",
"Historic center · San Miguel de Allende · 2025": "Centro histórico · San Miguel de Allende · 2025",
"Condesa · Mexico City · 2024": "Condesa · Ciudad de México · 2024",
"Competition · research · 2021–22": "Concurso · investigación · 2021–22",
"Bajío · 2022": "Bajío · 2022", "Mérida · Yucatán · 2022": "Mérida · Yucatán · 2022",
"Piedras Azules · San Miguel de Allende · 2025": "Piedras Azules · San Miguel de Allende · 2025",
"Peñas Arriba · San Miguel de Allende · 2026": "Peñas Arriba · San Miguel de Allende · 2026",
"El Campanario Residencial & Golf · Querétaro · 2025": "El Campanario Residencial & Golf · Querétaro · 2025",
"San Miguel de Allende · Los Cabos · 2022": "San Miguel de Allende · Los Cabos · 2022",

# ── real estate page ──
"Real Estate — Houses for Sale in San Miguel de Allende and Querétaro, by Architect Roberto Balderas Carrillo | RBC":
 "Bienes Raíces — Casas en venta en San Miguel de Allende y Querétaro, por el arquitecto Roberto Balderas Carrillo | RBC",
"A short selection of houses for sale and rent in San Miguel de Allende, its countryside and Querétaro, plus the developments Peñas Arriba and Magno, presented by architect Roberto Balderas Carrillo.":
 "Una selección breve de casas en venta y renta en San Miguel de Allende, su campo y Querétaro, más los desarrollos Peñas Arriba y Magno, presentados por el arquitecto Roberto Balderas Carrillo.",
"RBC / Real Estate": "RBC / Bienes Raíces", "Real Estate.": "Bienes Raíces.", "› Real Estate": "› Bienes Raíces",
"A short selection of houses, and the developments behind them.": "Una selección breve de casas, y los desarrollos detrás de ellas.",
"San Miguel de Allende": "San Miguel de Allende", "Querétaro": "Querétaro", "Celaya": "Celaya",
"Prices in MXN; USD approximate · Rentals: price on request · Open a sheet for plans, program and the PDF":
 "Precios en MXN; USD aproximado · Rentas: precio a consultar · Abre una ficha para ver plantas, programa y PDF",
"Developments": "Desarrollos", "Sell": "Vender", "Selling": "Vender",
"Open sheet →": "Abrir ficha →", "Full sheet →": "Ficha completa →", "Community site →": "Sitio de la comunidad →",
"Sales site →": "Sitio de ventas →", "Request information": "Solicitar información",
"Request information on WhatsApp": "Solicitar información por WhatsApp", "Full sheet (PDF)": "Ficha completa (PDF)",
"Open full page": "Abrir página completa", "Technical sheet (PDF)": "Ficha técnica (PDF)",
"Prices in MXN; USD approximate. Images provisional where noted.": "Precios en MXN; USD aproximado. Imágenes provisionales donde se indica.",
"Floor plans and the full technical sheet are available on request or in the PDF.": "Plantas y ficha técnica completa disponibles a solicitud o en el PDF.",
"Photographs": "Fotografías", "Plans": "Plantas", "Program": "Programa", "Location": "Ubicación", "Highlights": "Destacados",
"Architecture": "Arquitectura", "Site": "Sitio", "Materials": "Materiales", "Condition": "Estado", "Potential": "Potencial",
"Roberto's Notes": "Notas de Roberto", "draft · pending review": "borrador · pendiente de revisión",
"Authorship": "Autoría", "Units": "Unidades", "Available units": "Unidades disponibles",
"Price on request": "Precio a consultar", "For rent · Historic center": "En renta · Centro histórico",
"For rent · Historic center · San Miguel de Allende": "En renta · Centro histórico · San Miguel de Allende",
"For rent · For rent · Historic center · San Miguel de Allende": "En renta · Centro histórico · San Miguel de Allende",
"For sale · Peñas Arriba · San Miguel de Allende": "En venta · Peñas Arriba · San Miguel de Allende",
"For sale · El Campanario Residencial & Golf · Querétaro": "En venta · El Campanario Residencial & Golf · Querétaro",
"For sale · Piedras Azules · 20 minutes from San Miguel de Allende": "En venta · Piedras Azules · a 20 minutos de San Miguel de Allende",
"Peñas Arriba · San Miguel de Allende": "Peñas Arriba · San Miguel de Allende",
"Piedras Azules · 20 minutes from San Miguel de Allende": "Piedras Azules · a 20 minutos de San Miguel de Allende",
"El Campanario Residencial & Golf · Querétaro": "El Campanario Residencial & Golf · Querétaro",
"Celaya · Guanajuato": "Celaya · Guanajuato",
"Sell a property": "Vender una propiedad", "Buy a property": "Comprar una propiedad",
"RBC represents a short list, after a visit.": "RBC representa una lista corta, después de una visita.",
"A short list, after a visit.": "Una lista corta, después de una visita.",
"Have Roberto look at it first.": "Que Roberto la vea primero.", "Have it looked at first.": "Que la vean primero.",
"With an architect's reading.": "Con la lectura de un arquitecto.", "An architect's reading": "La lectura de un arquitecto",
"An architect's opinion first": "Primero, la opinión de un arquitecto", "An opinion first": "Primero una opinión",
"Ask about availability": "Preguntar disponibilidad", "Ask about your dates.": "Pregunta por tus fechas.",
"Ask about Peñas Arriba": "Preguntar por Peñas Arriba", "Ask about Magno Home & Towers": "Preguntar por Magno Home & Towers",
"Ask about La Nueva Escondida": "Preguntar por La Nueva Escondida", "Ask about La Escondida": "Preguntar por La Escondida",
"Ask Roberto about Peñas Arriba.": "Pregúntale a Roberto por Peñas Arriba.", "Ask Roberto about Magno Home & Towers.": "Pregúntale a Roberto por Magno Home & Towers.",
"Availability, prices and plans, answered directly.": "Disponibilidad, precios y plantas, respondidos directamente.",
"Showroom · virtual tour": "Showroom · recorrido virtual", "Showroom apartment · virtual tour": "Departamento muestra · recorrido virtual",
"Virtual tour of the showroom apartment": "Recorrido virtual del departamento muestra",

# statuses / specs
"Under construction · finishes open": "En construcción · acabados por definir",
"Shell built · ~6 months to delivery": "Obra gris · ~6 meses a la entrega",
"Shell built · finishes open": "Obra gris · acabados por definir",
"Built and under construction": "Construidas y en construcción",
"Built · contemporary country estate": "Construida · casa de campo contemporánea",
"Newly built": "Recién construida", "Immediate delivery": "Entrega inmediata", "Houses and lots": "Casas y lotes",
"Completed · units available": "Terminado · unidades disponibles",
"Completed · a few units available · Espacios y Formas": "Terminado · algunas unidades disponibles · Espacios y Formas",
"In development": "En desarrollo", "In development · details to follow": "En desarrollo · detalles próximamente",
"Under construction · Espacios y Formas": "En construcción · Espacios y Formas",
"Houses, shell-built homes and lots": "Casas, casas en obra gris y lotes",
"Houses, shell-built homes and lots · RBC with Espacios y Formas": "Casas, casas en obra gris y lotes · RBC con Espacios y Formas",
"Apartments, homes and lots": "Departamentos, casas y lotes",
"Apartments, homes and lots · Espacios y Formas": "Departamentos, casas y lotes · Espacios y Formas",
"Apartments · immediate delivery": "Departamentos · entrega inmediata",
"bedrooms": "recámaras", "baths": "baños", "cars": "autos", "levels": "niveles", "floors": "pisos",
"full bath": "baño completo", "full baths": "baños completos", "bedroom · king": "recámara · king", "queen bed": "cama queen",
"m² living": "m² habitables", "m² lots": "m² de lote", "delivery": "entrega", "included": "incluidos", "Services": "Servicios",
"Balcony": "Balcón", "facing the Parroquia": "frente a la Parroquia", "terrace view": "terraza con vista", "Rooftop": "Rooftop",
"Immediate": "Entrega", "to San Miguel": "a San Miguel", "20 min": "20 min", "Spa · pool": "Spa · alberca", "gym · club": "gym · club",
"Single-family": "Casas", "homes": "unifamiliares", "Lots": "Lotes", "Lot": "Lote", "in the community": "en la comunidad",
"units available": "unidades disponibles", "Gated": "Privada", "hillside community": "comunidad en la ladera",
"Shell-built": "Obra gris", "designed by RBC": "diseñadas por RBC", "House": "Casa", "Houses": "Casas", "Tower": "Torre", "apartments": "departamentos",
"bedrooms · all en suite": "recámaras · todas con baño", "m² built · 12,475 sq ft": "m² construidos · 12,475 sq ft",
"m² built · 6,693 sq ft": "m² construidos · 6,693 sq ft", "m² built · 3,692 sq ft": "m² construidos · 3,692 sq ft",
"m² built · 6,373 sq ft": "m² construidos · 6,373 sq ft", "m² lot · 8,905 sq ft": "m² de lote · 8,905 sq ft",
"m² lot · 4,500 sq ft": "m² de lote · 4,500 sq ft", "m² lot · 8,219 sq ft": "m² de lote · 8,219 sq ft",
"m² lot · 1.98 acres": "m² de lote · 1.98 acres", "Double": "Doble", "height": "altura", "Pool": "Alberca", "& sun deck": "y asoleadero",
"Upper residence": "Residencia alta", "Garden residence": "Residencia con jardín",
"Upper residence · M1-L12": "Residencia alta · M1-L12", "Upper residence · M5-L2": "Residencia alta · M5-L2",
"Garden residence · M5-L9": "Residencia con jardín · M5-L9", "Garden residence · M5-L2": "Residencia con jardín · M5-L2",
"≈ 205 m² · single level · already built": "≈ 205 m² · un solo nivel · ya construida",
"≈ 205 m² · single level": "≈ 205 m² · un solo nivel",
"≈ 188 m² · private garden on a 322 m² lot · already built": "≈ 188 m² · jardín privado en lote de 322 m² · ya construida",
"190 m² · private garden on a 363 m² lot": "190 m² · jardín privado en lote de 363 m²",
"Duplex residences": "Residencias dúplex", "Magno Towers · Apartments": "Magno Towers · Departamentos",
"Magno Homes · Houses & lots": "Magno Homes · Casas y lotes", "From MX $6.6M": "Desde MX $6.6M",
"From MX $4.65M · 26 apartments available": "Desde MX $4.65M · 26 departamentos disponibles",
"Homes from MX $5.5M · Lots from MX $2.0M": "Casas desde MX $5.5M · Lotes desde MX $2.0M",
"apartments available · from MX $4.65M": "departamentos disponibles · desde MX $4.65M", "from MX $5.5M": "desde MX $5.5M",
"225–450 m² · from MX $2.0M": "225–450 m² · desde MX $2.0M", "spa · pool · gym · clubhouse": "spa · alberca · gym · casa club",
"2 and 3 bedrooms · 171 to 229 m² of living space": "2 y 3 recámaras · 171 a 229 m² habitables",
"26 apartments available · immediate delivery": "26 departamentos disponibles · entrega inmediata",
"Two parking spaces and a storage room with every apartment": "Dos cajones de estacionamiento y bodega con cada departamento",
"Spa · pool · gym · clubhouse · business center · gardens": "Spa · alberca · gym · casa club · business center · jardines",
"24/7 gated security with double access": "Seguridad 24/7 con doble acceso", "24/7 gated security": "Seguridad 24/7",
"Apartments with immediate delivery": "Departamentos con entrega inmediata",
"Homes and lots inside the same community": "Casas y lotes dentro de la misma comunidad",
"Availability": "Disponibilidad", "Lots · Cluster 1": "Lotes · Clúster 1", "Apartment 1303 (plan shown)": "Departamento 1303 (planta mostrada)",
"Developed by": "Desarrollado por", "Where": "Dónde", "The development": "El desarrollo", "Available in Peñas Arriba": "Disponible en Peñas Arriba",
"Available in Magno Home & Towers": "Disponible en Magno Home & Towers",
"Development · Celaya · Guanajuato": "Desarrollo · Celaya · Guanajuato",
"Development · San Miguel de Allende · Guanajuato": "Desarrollo · San Miguel de Allende · Guanajuato",
"Cover and renders pending": "Portada y renders pendientes", "Mid-term stays": "Estancias medias",
"Short stays also available (Airbnb link pending)": "También estancias cortas (link de Airbnb pendiente)",
"Services included · mid-term stays": "Servicios incluidos · estancias medias",
"Ready; services included.": "Lista; servicios incluidos.", "Ready; services included; short stays also available.": "Lista; servicios incluidos; también estancias cortas.",
"Design + construction": "Diseño + construcción", "Designed and built by RBC": "Diseñada y construida por RBC",
"Designed by RBC · built with Espacios y Formas": "Diseñada por RBC · construida con Espacios y Formas",
"Peñas Arriba · built with Espacios y Formas": "Peñas Arriba · construida con Espacios y Formas",
"Built by RBC · design developed from a prior scheme": "Construida por RBC · diseño desarrollado a partir de un planteamiento previo",
"Casa Cuadrante — restored and designed by RBC": "Casa Cuadrante — restaurada y diseñada por RBC",
"A development by Espacios y Formas": "Un desarrollo de Espacios y Formas", "RBC with Espacios y Formas": "RBC con Espacios y Formas",
"Represented by RBC": "Representada por RBC",
}

# long texts (listings, sheets)
T.update({
"A house that follows its slope: entered from the top, stepping down the hill so the principal rooms face the historic center. Under construction; finishes still to be chosen.":
 "Una casa que sigue su pendiente: se entra por arriba y baja por la ladera para que las estancias principales miren al centro histórico. En construcción; acabados por elegir.",
"Casa Horizonte is shaped by its topography. Rather than levelling the land, the house follows the slope of the hill: you arrive at the upper level — living, dining, kitchen, terrace and pool — and the house steps down so that every principal room faces the historic center of San Miguel. Rock revealed by the excavation was left exposed inside as the wall of the wine cellar.":
 "Casa Horizonte está formada por su topografía. En lugar de nivelar el terreno, la casa sigue la pendiente del cerro: se llega al nivel superior —sala, comedor, cocina, terraza y alberca— y la casa desciende para que cada estancia principal mire al centro histórico de San Miguel. La roca que reveló la excavación se dejó expuesta como muro de la cava.",
"Section-driven plan on two levels. The social level and pool sit at the top with the entry; the bedrooms step down toward the garden. The principal rooms are oriented to the view of the historic center.":
 "Planta resuelta desde la sección, en dos niveles. El nivel social y la alberca están arriba, con el acceso; las recámaras bajan hacia el jardín. Las estancias principales se orientan a la vista del centro histórico.",
"Lot M4-L7, upper tier of Peñas Arriba, a gated community on the hillside above San Miguel with a protected line of sight to the Parroquia. Excavated rock kept inside the house as the cellar wall.":
 "Lote M4-L7, en la parte alta de Peñas Arriba, comunidad privada en la ladera sobre San Miguel con vista protegida a la Parroquia. La roca excavada se conserva dentro de la casa como muro de la cava.",
"Stone on façades and retaining walls; concrete structure; large glazing toward the view. Flooring, kitchen, baths, stone and lighting still to be selected.":
 "Piedra en fachadas y muros de contención; estructura de concreto; grandes cristales hacia la vista. Pisos, cocina, baños, cantera e iluminación por seleccionar.",
"Under construction at an advanced stage; elevator-ready. Delivered with finishes selected by the buyer.":
 "En construcción en etapa avanzada; preparada para elevador. Se entrega con los acabados que elija el comprador.",
"A view house of this size whose finishes are still open — the buyer defines the final level of the house without waiting for a full build.":
 "Una casa con vista de este tamaño con los acabados aún abiertos: el comprador define el nivel final de la casa sin esperar una construcción completa.",
"The house was drawn from the section. The site decided where to enter, where to sleep and where to look; the plan simply followed. Whoever buys it now still gets to decide the materials of every surface they will touch.":
 "La casa se dibujó desde la sección. El sitio decidió por dónde entrar, dónde dormir y hacia dónde mirar; la planta simplemente siguió. Quien la compre ahora todavía decide los materiales de cada superficie que va a tocar.",
"622 m² (6,693 sq ft) built on an 827 m² (8,905 sq ft) lot": "622 m² (6,693 sq ft) construidos en un lote de 827 m² (8,905 sq ft)",
"5 bedrooms: three on the entry level (one convertible to staff), two below · 5½ baths": "5 recámaras: tres en el nivel de acceso (una convertible a servicio), dos abajo · 5½ baños",
"Pool and pergola terrace facing the Parroquia": "Alberca y terraza con pérgola frente a la Parroquia",
"Wine cellar in the excavated rock · elevator-ready": "Cava en la roca excavada · preparada para elevador",
"Under construction — finishes chosen by the buyer": "En construcción — acabados a elección del comprador",
"Upper level — entry": "Nivel superior — acceso", "Lower level": "Nivel inferior", "Upper level": "Nivel superior", "Ground level": "Planta baja", "Entry level": "Nivel de acceso",
"Entry court and two-car garage · living-dining with open kitchen · primary suite with two walk-ins and two baths · study with bath · two bedrooms · linen room · covered terrace · sun deck with pool":
 "Patio de acceso y cochera para dos autos · sala-comedor con cocina abierta · recámara principal con dos vestidores y dos baños · estudio con baño · dos recámaras · cuarto de blancos · terraza techada · asoleadero con alberca",
"Two large en-suite bedrooms · family room · wine cellar in the excavated rock · elevator shaft · private garden facing the center":
 "Dos recámaras grandes con baño · sala familiar · cava en la roca excavada · cubo de elevador · jardín privado hacia el centro",
"Lot M4-L7, upper tier of Peñas Arriba, San Miguel de Allende — about 7 minutes (1.8 mi) from the Jardín Principal. BJX airport ~1 h 15, QRO ~1 h.":
 "Lote M4-L7, parte alta de Peñas Arriba, San Miguel de Allende — a unos 7 minutos (3 km) del Jardín Principal. Aeropuerto BJX ~1 h 15, QRO ~1 h.",
# Zafiro
"Casa Zafiro sits on the largest garden lot in Peñas Arriba. It is built to shell stage, with delivery in about six months once the finishes are defined together with the practice.":
 "Casa Zafiro ocupa el lote con jardín más grande de Peñas Arriba. Está construida en obra gris, con entrega en unos seis meses una vez definidos los acabados junto con el despacho.",
"Compact plan opening to terrace and garden; master suite on the main level.": "Planta compacta abierta a terraza y jardín; recámara principal en el nivel principal.",
"Lot M1-L14, a 418 m² garden lot inside the gated community, with views of the center and the Parroquia.": "Lote M1-L14, un lote con jardín de 418 m² dentro de la comunidad privada, con vistas al centro y a la Parroquia.",
"Natural stone; concrete structure. Built to shell — all finishes open.": "Piedra natural; estructura de concreto. Obra gris — todos los acabados abiertos.",
"Shell complete; about six months to delivery once finishes are defined.": "Obra gris terminada; unos seis meses a la entrega una vez definidos los acabados.",
"The plan and the site without waiting for a full build, and the level of finish set to the buyer's budget.": "La planta y el sitio sin esperar una construcción completa, y el nivel de acabados ajustado al presupuesto del comprador.",
"The garden is the argument. It is the biggest lot in the community and the shell is already there; what remains is the part most owners enjoy deciding.":
 "El jardín es el argumento. Es el lote más grande de la comunidad y la obra gris ya está; lo que falta es la parte que más disfrutan decidir los dueños.",
"343.7 m² (3,700 sq ft) built on a 4,500 sq ft garden lot": "343.7 m² (3,700 sq ft) construidos en un lote con jardín de 418 m²",
"4 bedrooms + staff · 4½ baths · 2 cars": "4 recámaras + servicio · 4½ baños · 2 autos",
"Shell built — finishes chosen with the architect": "Obra gris — acabados elegidos con el arquitecto",
"Shell built — flooring, stone, carpentry and paint chosen by the buyer": "Obra gris — pisos, cantera, carpintería y pintura a elección del comprador",
"Payment plan: 40% at signing, the balance in monthly payments until delivery (~6 months)": "Plan de pagos: 40% a la firma, el resto en mensualidades hasta la entrega (~6 meses)",
"Inside gated Peñas Arriba: pool, gym, restaurant, 24/7 security": "Dentro de Peñas Arriba: alberca, gym, restaurante, seguridad 24/7",
"Living-dining and kitchen open to terrace and garden · master suite · three further bedrooms · staff quarters · two-car garage":
 "Sala-comedor y cocina abiertas a terraza y jardín · recámara principal · tres recámaras más · cuarto de servicio · cochera para dos autos",
"Lot M1-L14, Peñas Arriba, San Miguel de Allende — about 7 minutes from the historic center.": "Lote M1-L14, Peñas Arriba, San Miguel de Allende — a unos 7 minutos del centro histórico.",
"Shell built — flooring, stone, carpentry and paint still to be chosen.": "Obra gris — pisos, cantera, carpintería y pintura por elegir.",
"Built to shell — flooring, stone, carpentry and paint still to be chosen.": "Obra gris — pisos, cantera, carpintería y pintura por elegir.",
# Cima
"First house of its block: the side façade rises from the street as one wall of natural stone. Double-height living and an unusually large garden with views of the historic center.":
 "Primera casa de su manzana: la fachada lateral sube desde la calle como un solo muro de piedra natural. Sala en doble altura y un jardín inusualmente grande con vistas al centro histórico.",
"Casa Cima is the first house of block 6, so its side façade rises from the street as a single wall of natural stone. The social level opens in double height — living, dining and bar in one room that flows to the terrace and to a large garden looking over the community gardens toward the historic center. The master suite is placed on the social level, with its own sitting room, two baths and a double view. Built to shell; a pool facing the town can be added in the garden.":
 "Casa Cima es la primera casa de la manzana 6, por lo que su fachada lateral sube desde la calle como un solo muro de piedra natural. El nivel social se abre en doble altura —sala, comedor y bar en un solo espacio que fluye a la terraza y a un jardín grande que mira sobre los jardines de la comunidad hacia el centro histórico. La recámara principal está en el nivel social, con su propia sala de estar, dos baños y doble vista. En obra gris; se puede agregar una alberca con vista al pueblo en el jardín.",
"Double-height social level; master suite deliberately on the same level as the garden, with its own sitting room. Three double bedrooms and a TV lounge upstairs.":
 "Nivel social en doble altura; recámara principal deliberadamente al nivel del jardín, con su propia sala de estar. Tres recámaras dobles y sala de TV arriba.",
"Lot M6-L1, 763.55 m², with one of the largest gardens in the community, looking over the community gardens to the historic center.":
 "Lote M6-L1, 763.55 m², con uno de los jardines más grandes de la comunidad, mirando sobre los jardines comunes hacia el centro histórico.",
"Shell built; ready for flooring, stone, carpentry and paint. Pool with a view of the town can be added.": "Obra gris; lista para pisos, cantera, carpintería y pintura. Se puede agregar alberca con vista al pueblo.",
"The freedom to define every finish on a house whose structure, plan and garden are already resolved.": "La libertad de definir cada acabado en una casa cuya estructura, planta y jardín ya están resueltos.",
"The master suite is downstairs on purpose: whoever lives here should have the garden and the view without a staircase in between.":
 "La recámara principal está abajo a propósito: quien viva aquí debe tener el jardín y la vista sin una escalera de por medio.",
"763.55 m² lot (8,219 sq ft) · 592.06 m² built (6,373 sq ft)": "Lote de 763.55 m² (8,219 sq ft) · 592.06 m² construidos (6,373 sq ft)",
"Master suite on the social level: walk-in closet, two baths, private sitting room, double view": "Recámara principal en el nivel social: vestidor, dos baños, sala privada, doble vista",
"Double-height living room with bar, and dining room": "Sala en doble altura con bar, y comedor",
"Kitchen with pantry room, staff quarters, garage and storage": "Cocina con despensa, cuarto de servicio, cochera y bodega",
"TV lounge · three double bedrooms with full baths": "Sala de TV · tres recámaras dobles con baño completo",
"Option to add a pool facing the historic center": "Opción de agregar alberca frente al centro histórico",
"Option to add a pool with a view of the historic center inside the garden": "Opción de agregar en el jardín una alberca con vista al centro histórico",
"Garage and storage · master suite with walk-in, two baths and sitting room · double-height living, dining and bar · kitchen with pantry · staff room · terrace with dining and lounge · garden":
 "Cochera y bodega · recámara principal con vestidor, dos baños y sala de estar · sala, comedor y bar en doble altura · cocina con despensa · cuarto de servicio · terraza con comedor y estar · jardín",
"Upper level: three double bedrooms, each with full bath, and a TV lounge": "Planta alta: tres recámaras dobles, cada una con baño completo, y sala de TV",
"Lot M6-L1, the first house of block 6 in Peñas Arriba, San Miguel de Allende — about 7 minutes from the historic center.": "Lote M6-L1, la primera casa de la manzana 6 de Peñas Arriba, San Miguel de Allende — a unos 7 minutos del centro histórico.",
# Duplex
"Two-level duplex houses in Peñas Arriba: a garden residence on the ground floor and an upper residence with the view of the historic center. Three units available.":
 "Casas dúplex de dos niveles en Peñas Arriba: una residencia con jardín en planta baja y una residencia alta con la vista al centro histórico. Unidades disponibles.",
"The duplex houses of Peñas Arriba pair a ground-floor garden residence with an upper, apartment-style residence, each with its own entrance, kitchen, living-dining, three bedrooms, three bathrooms and two parking spaces. Buy one unit or both. The upper residence has a single price on every lot; the garden residence varies with the size of its garden. Two units are already built; finishes are chosen by the buyer.":
 "Las casas dúplex de Peñas Arriba combinan una residencia con jardín en planta baja con una residencia alta tipo departamento, cada una con su propio acceso, cocina, sala-comedor, tres recámaras, tres baños y dos cajones de estacionamiento. Se compra una unidad o las dos. La residencia alta tiene un precio único en todos los lotes; la de jardín varía con el tamaño de su jardín. Dos unidades ya están construidas; los acabados los elige el comprador.",
"Two independent residences per building: the garden residence opens to a private garden; the upper residence is a single level facing the view.":
 "Dos residencias independientes por edificio: la de jardín se abre a un jardín privado; la alta es un solo nivel frente a la vista.",
"Blocks 1 and 5 of Peñas Arriba; the M5 units sit next to the clubhouse and pool.": "Manzanas 1 y 5 de Peñas Arriba; las unidades de la M5 están junto a la casa club y la alberca.",
"Stone, wood pergolas and clay tile roofs; finishes chosen with the practice.": "Piedra, pérgolas de madera y techos de teja; acabados elegidos con el despacho.",
"Built; about six months to delivery.": "Construidas; unos seis meses a la entrega.",
"Lock-and-leave living inside a gated community, with the club a few steps away.": "Vivir sin preocupaciones dentro de una comunidad privada, con el club a unos pasos.",
"The garden units are for anyone who wants breakfast outside; the upper unit is for the view.": "Las unidades con jardín son para quien quiere desayunar afuera; la alta es para la vista.",
"Buy the whole duplex (≈ 393 m²) or one unit: upper residence at a single MX $6.6M price on every lot; garden residence from MX $7.433M depending on the garden":
 "Compra el dúplex completo (≈ 393 m²) o una unidad: residencia alta a un precio único de MX $6.6M en todos los lotes; residencia con jardín desde MX $7.433M según el jardín",
"3 bedrooms · 3 full baths · 2 parking spaces per unit": "3 recámaras · 3 baños completos · 2 cajones por unidad",
"Several façades and interior layouts to choose from": "Varias fachadas y distribuciones interiores a elegir",
"Block 5 units sit next to the clubhouse and pool": "Las unidades de la manzana 5 están junto a la casa club y la alberca",
"Living-dining and kitchen opening to the garden · 3 bedrooms · 3 baths · laundry · 1 car": "Sala-comedor y cocina abiertas al jardín · 3 recámaras · 3 baños · lavandería · 1 auto",
"Single level: living-dining, kitchen, terrace with the view · 3 bedrooms · 3 baths · laundry · 1 car": "Un solo nivel: sala-comedor, cocina, terraza con la vista · 3 recámaras · 3 baños · lavandería · 1 auto",
"Peñas Arriba, San Miguel de Allende.": "Peñas Arriba, San Miguel de Allende.",
# Musa
"An apartment above Casa Cuadrante: living-dining with fireplace and a view of the Parroquia, private balcony, art on every wall. Furnished; services included.":
 "Un departamento sobre Casa Cuadrante: sala-comedor con chimenea y vista a la Parroquia, balcón privado, arte en cada pared. Amueblado; servicios incluidos.",
"Casa Musa is the apartment above Casa Cuadrante, the restaurant on the ground floor of a historic house that RBC restored, adapted and furnished. It was made for people who like living among art: a living-dining room with a fireplace and a direct view of the Parroquia, a bedroom with a king bed and full bath, a sound system, a private balcony over the street and a laundry room. Water, electricity and internet are included. Available for mid-term stays.":
 "Casa Musa es el departamento sobre Casa Cuadrante, el restaurante en la planta baja de una casa histórica que RBC restauró, adaptó y amuebló. Se hizo para quien disfruta vivir entre arte: una sala-comedor con chimenea y vista directa a la Parroquia, una recámara con cama king y baño completo, sistema de sonido, un balcón privado sobre la calle y cuarto de lavado. Agua, luz e internet incluidos. Disponible para estancias medias.",
"An apartment organised around a living-dining room with a fireplace and a straight view of the Parroquia; private balcony over the street.":
 "Un departamento organizado alrededor de una sala-comedor con chimenea y vista directa a la Parroquia; balcón privado sobre la calle.",
"Inside Casa Cuadrante, historic center — the Jardín Principal on foot.": "Dentro de Casa Cuadrante, centro histórico — el Jardín Principal a pie.",
"Restored historic house; furnished and decorated, with art throughout; sound system.": "Casa histórica restaurada; amueblada y decorada, con arte por todas partes; sistema de sonido.",
"Mid-term stays inside the center rather than next to it.": "Estancias medias dentro del centro, no junto a él.",
"It was designed to be lived in by someone who works surrounded by art. The balcony does the rest.": "Se diseñó para que la viva alguien que trabaja rodeado de arte. El balcón hace el resto.",
"Living-dining room with fireplace and a direct view of the Parroquia": "Sala-comedor con chimenea y vista directa a la Parroquia",
"Bedroom with king bed and full bathroom": "Recámara con cama king y baño completo",
"Private balcony facing the Parroquia": "Balcón privado frente a la Parroquia",
"Furnished and decorated; art throughout; sound system": "Amueblado y decorado; arte por todas partes; sistema de sonido",
"Laundry room · water, electricity and internet included": "Cuarto de lavado · agua, luz e internet incluidos",
"Above Casa Cuadrante, in the historic center": "Sobre Casa Cuadrante, en el centro histórico",
"The apartment": "El departamento",
"Living-dining with fireplace · kitchen · bedroom with full bath · laundry · private balcony": "Sala-comedor con chimenea · cocina · recámara con baño completo · lavado · balcón privado",
"Inside Casa Cuadrante, in the historic center of San Miguel de Allende — restaurants, galleries and the Jardín Principal on foot.": "Dentro de Casa Cuadrante, en el centro histórico de San Miguel de Allende — restaurantes, galerías y el Jardín Principal a pie.",
# Suite
"A suite with a large private terrace directly in front of the Parroquia — a 300-degree view of the town. Queen bed, full bath, mini-fridge.":
 "Una suite con una gran terraza privada justo frente a la Parroquia — una vista de 300 grados del pueblo. Cama queen, baño completo, minirefrigerador.",
"The Panoramic Suite is defined by its terrace: large, private and directly in front of the Parroquia, with the whole of San Miguel around it. Queen bed, full bathroom and mini-fridge; an outdoor kitchenette can be fitted on the terrace if needed. Loungers and tables outside. Services included; also available for short stays.":
 "La Suite Panorámica se define por su terraza: grande, privada y justo frente a la Parroquia, con todo San Miguel alrededor. Cama queen, baño completo y minirefrigerador; se puede instalar una cocineta exterior en la terraza si hace falta. Camastros y mesas afuera. Servicios incluidos; también disponible para estancias cortas.",
"A suite whose main room is outdoors: a large private terrace facing the Parroquia.": "Una suite cuya estancia principal está al aire libre: una gran terraza privada frente a la Parroquia.",
"Roof level of Casa Cuadrante, historic center.": "Azotea de Casa Cuadrante, centro histórico.",
"Queen bed, full bath, mini-fridge; loungers and tables on the terrace; outdoor kitchenette on request.": "Cama queen, baño completo, minirefrigerador; camastros y mesas en la terraza; cocineta exterior a solicitud.",
"Stays with an unobstructed view of the Parroquia, for a weekend or a season.": "Estancias con vista despejada a la Parroquia, por un fin de semana o una temporada.",
"Of the terraces I know in San Miguel, this is the one I would choose.": "De las terrazas que conozco en San Miguel, esta es la que yo elegiría.",
"Large private terrace with a 300° view of San Miguel, facing the Parroquia": "Gran terraza privada con vista de 300° de San Miguel, frente a la Parroquia",
"Queen bed, full bathroom, mini-fridge": "Cama queen, baño completo, minirefrigerador",
"Loungers and tables on the terrace": "Camastros y mesas en la terraza",
"Outdoor kitchenette on the terrace on request": "Cocineta exterior en la terraza a solicitud",
"The suite": "La suite",
"Bedroom with queen bed · full bath · mini-fridge · private panoramic terrace": "Recámara con cama queen · baño completo · minirefrigerador · terraza panorámica privada",
"Casa Cuadrante, historic center of San Miguel de Allende — the terrace faces the Parroquia directly.": "Casa Cuadrante, centro histórico de San Miguel de Allende — la terraza mira directamente a la Parroquia.",
"Inside Casa Cuadrante, restored and designed by RBC": "Dentro de Casa Cuadrante, restaurada y diseñada por RBC",
"Views of the historic center and the Parroquia": "Vistas al centro histórico y a la Parroquia",
# Ether
"A contemporary country estate on a private hilltop: double-height ceilings, oak floors and walls of glass that open to mountain views in every direction. Lap pool, jacuzzi and fire pit.":
 "Una casa de campo contemporánea en una loma privada: dobles alturas, pisos de roble y muros de cristal que se abren a vistas de montaña en todas direcciones. Alberca, jacuzzi y fogatero.",
"Casa Ether sits on a private hilltop of 7,999 m² inside Rancho Piedras Azules, twenty minutes from the center of San Miguel de Allende. Double-height ceilings, Sacarella oak floors and wood-panelled ceilings run through open living and dining spaces that slide open onto a wrap-around deck, a lap pool, a jacuzzi and a gas fire pit with step-down seating. Four en-suite bedrooms, a family TV room, kitchen with marble island and walk-in pantry, cava and bar, a pétanque court and a rooftop terrace; staff room and services. Mountain and valley views in every direction.":
 "Casa Ether se asienta en una loma privada de 7,999 m² dentro de Rancho Piedras Azules, a veinte minutos del centro de San Miguel de Allende. Dobles alturas, pisos de roble Sacarella y plafones de madera recorren la sala y el comedor abiertos, que se deslizan hacia una terraza perimetral, alberca, jacuzzi y un fogatero de gas con asientos escalonados. Cuatro recámaras con baño, sala de TV familiar, cocina con isla de mármol y despensa, cava y bar, cancha de petanca y rooftop; cuarto de servicio y áreas de servicio. Vistas a la montaña y al valle en todas direcciones.",
"Two levels on a hilltop: a long, low volume with a cantilevered roof plane, double-height living spaces and glass walls that dissolve the interior into the landscape.":
 "Dos niveles en una loma: un volumen largo y bajo con un plano de cubierta en voladizo, estancias en doble altura y muros de cristal que disuelven el interior en el paisaje.",
"Lot 15, Rancho Piedras Azules, Palo Blanco, Guanajuato — a gated community with an access road and complete privacy; 20 minutes from San Miguel de Allende centro. Views of the sierra and the valley on every side.":
 "Lote 15, Rancho Piedras Azules, Palo Blanco, Guanajuato — comunidad privada con camino de acceso y privacidad total; a 20 minutos del centro de San Miguel de Allende. Vistas a la sierra y al valle por todos lados.",
"Sacarella oak floors; wood-panelled ceilings; marble island and master bathroom; double-paned windows; stone and concrete outside; agave gardens.":
 "Pisos de roble Sacarella; plafones de madera; isla y baño principal de mármol; ventanas de doble cristal; piedra y concreto al exterior; jardines de agaves.",
"Built and finished; designer furnishings and art. Security system, ample parking.": "Construida y terminada; mobiliario de diseño y arte. Sistema de seguridad, amplio estacionamiento.",
"A finished contemporary house of this scale, on nearly two hectares of private country this close to San Miguel, is rare.": "Una casa contemporánea terminada de esta escala, en casi dos hectáreas de campo privado tan cerca de San Miguel, es rara.",
"1,159 m² (12,475 sq ft) built on a 7,999 m² (1.98 acres) hilltop lot": "1,159 m² (12,475 sq ft) construidos en un lote de 7,999 m² (1.98 acres) en la loma",
"4 bedrooms including the master, each with its own full bath · 2 additional half baths · staff room": "4 recámaras incluyendo la principal, cada una con baño completo · 2 medios baños adicionales · cuarto de servicio",
"Pool, jacuzzi, pétanque court and gas fire pit with step-down seating · rooftop": "Alberca, jacuzzi, cancha de petanca y fogatero de gas con asientos escalonados · rooftop",
"Living room with open kitchen (can be closed off) · family TV room · bar · cava": "Sala con cocina abierta (con opción a cerrarse) · sala de TV familiar · bar · cava",
"Sacarella oak floors · wood-panelled ceilings · marble master bath": "Pisos de roble Sacarella · plafones de madera · baño principal de mármol",
"Staff room · security system · parking for 3 cars": "Cuarto de servicio · sistema de seguridad · estacionamiento para 3 autos",
"Gated community, 20 minutes from San Miguel de Allende centro": "Comunidad privada, a 20 minutos del centro de San Miguel de Allende",
"Master suite with walk-in closet, full bath and terrace · 3 bedrooms with full baths · family TV room · terrace · parking for 3 cars":
 "Recámara principal con vestidor, baño completo y terraza · 3 recámaras con baño completo · sala de TV familiar · terraza · estacionamiento para 3 autos",
"Living and dining with open kitchen (can be closed off) · bar · cava · pantry · half baths · terrace with pool, jacuzzi and fire pit · pétanque court · staff room, laundry and services":
 "Sala y comedor con cocina abierta (con opción a cerrarse) · bar · cava · despensa · medios baños · terraza con alberca, jacuzzi y fogatero · cancha de petanca · cuarto de servicio, lavado y servicios",
"Open roof terrace with mountain and valley views": "Rooftop abierto con vistas a la montaña y al valle",
"Lot 15, Rancho Piedras Azules, Palo Blanco, Guanajuato — 20 minutes from San Miguel de Allende centro. Gated; mountain and valley views in every direction.":
 "Lote 15, Rancho Piedras Azules, Palo Blanco, Guanajuato — a 20 minutos del centro de San Miguel de Allende. Privado; vistas a la montaña y al valle en todas direcciones.",
# Travertino
"Newly built on the last lot of its private street, facing the mountains: double-height living and bar, pool with sun deck, four en-suite bedrooms (three upstairs, one on the ground floor) plus staff quarters.":
 "Recién construida en el último lote de su privada, frente a las montañas: sala y bar en doble altura, alberca con asoleadero, cuatro recámaras con baño (tres arriba y una en planta baja) más cuarto de servicio.",
"Casa Travertino occupies the last lot of its private street inside El Campanario Residencial & Golf, which is why every terrace looks at the mountains. The ground floor is made for gathering: living room with bar and dining in double height, a kitchen with breakfast area, a covered terrace and a sun deck around the pool. Four en-suite bedrooms in all — three upstairs with a family TV room and a lobby that works as a reading room or linen closet, plus one on the ground floor — and full staff quarters. Newly built; never lived in.":
 "Casa Travertino ocupa el último lote de su privada dentro de El Campanario Residencial & Golf, por eso todas las terrazas miran a las montañas. La planta baja está hecha para reunirse: sala con bar y comedor en doble altura, cocina con desayunador, terraza techada y asoleadero alrededor de la alberca. Cuatro recámaras con baño en total — tres arriba con sala de TV familiar y un lobby que funciona como sala de lectura o closet de blancos, más una en planta baja — y cuarto de servicio completo. Recién construida; nunca habitada.",
"Double-height living with bar and dining on the ground floor, terraces to the mountains; four en-suite bedrooms — three upstairs with a family room, one on the ground floor — plus staff quarters.":
 "Sala en doble altura con bar y comedor en planta baja, terrazas hacia las montañas; cuatro recámaras con baño — tres arriba con sala familiar, una en planta baja — más cuarto de servicio.",
"El Campanario Residencial & Golf, Querétaro — the last lot of its private street, with open mountain views.": "El Campanario Residencial & Golf, Querétaro — el último lote de su privada, con vistas abiertas a las montañas.",
"Newly built; stone, concrete and glass; pool with sun deck and covered terrace.": "Recién construida; piedra, concreto y cristal; alberca con asoleadero y terraza techada.",
"New. Never lived in.": "Nueva. Nunca habitada.",
"The ground-floor suite absorbs a gym, an office or a fourth bedroom without touching the rest of the plan.": "La suite de planta baja absorbe un gym, una oficina o una cuarta recámara sin tocar el resto de la planta.",
"The double height was drawn for the mountains. Sit at the bar late in the afternoon and the reason is obvious.": "La doble altura se dibujó para las montañas. Siéntate en el bar al final de la tarde y la razón es obvia.",
"Last lot of its private street — open mountain views": "Último lote de su privada — vistas abiertas a la montaña",
"Double-height living, dining and bar opening to terrace and garden": "Sala, comedor y bar en doble altura abiertos a terraza y jardín",
"Covered terrace, sun deck and pool with outdoor half-bath": "Terraza techada, asoleadero y alberca con medio baño exterior",
"Four en-suite bedrooms + staff quarters": "Cuatro recámaras con baño + cuarto de servicio", "Three bedrooms upstairs with family TV room and reading lobby; a fourth en-suite bedroom on the ground floor (also gym or study)": "Tres recámaras arriba con sala de TV familiar y lobby de lectura; una cuarta recámara con baño en planta baja (también gym o estudio)", "quarters": "de servicio", "Staff": "Cuarto",
"Ground-floor en-suite room for gym, bedroom or study": "Habitación con baño en planta baja para gym, recámara o estudio",
"Three-car garage · guest half-bath": "Cochera para tres autos · medio baño de visitas",
"Kitchen with breakfast area, full staff quarters and service patio, storage": "Cocina con desayunador, cuarto de servicio completo y patio de servicio, bodega",
"Garage for 3 cars · staff room with bath and service patio · kitchen with breakfast area · fourth en-suite bedroom (also gym / study) · living-bar and dining in double height · covered terrace · sun deck and pool · outdoor half-bath · guest half-bath · storage":
 "Cochera para 3 autos · cuarto de servicio con baño y patio de servicio · cocina con desayunador · cuarta recámara con baño (también gym / estudio) · sala-bar y comedor en doble altura · terraza techada · asoleadero y alberca · medio baño exterior · medio baño de visitas · bodega",
"Three bedrooms with baths · family TV room · lobby for reading or linen": "Tres recámaras con baño · sala de TV familiar · lobby para lectura o blancos",
"Last lot of its private street in El Campanario Residencial & Golf, Querétaro — open mountain views with nothing to be built in front.": "Último lote de su privada en El Campanario Residencial & Golf, Querétaro — vistas abiertas a la montaña sin nada por construir enfrente.",
# Magno
"Apartments in the Magno tower in Celaya, developed and built by Espacios y Formas: 2 and 3 bedrooms, 171 to 229 m² of living space plus parking and storage, with spa, pool, gym and clubhouse. 26 apartments available for immediate delivery.":
 "Departamentos en la torre Magno en Celaya, desarrollada y construida por Espacios y Formas: 2 y 3 recámaras, 171 a 229 m² habitables más estacionamiento y bodega, con spa, alberca, gym y casa club. 26 departamentos disponibles para entrega inmediata.",
"Magno Towers is the residential tower of Magno Home & Towers, a gated community in Celaya developed and built by Espacios y Formas. Every apartment comes with two parking spaces and a storage room (about 31–43 m²) on top of its living area, and shares the spa, pool, gym, clubhouse, business center, bar, multipurpose hall and gardens of the community. Twenty-six apartments are available for immediate delivery (price list 2026, list below); the furnished showroom apartment can be visited online.":
 "Magno Towers es la torre residencial de Magno Home & Towers, una comunidad privada en Celaya desarrollada y construida por Espacios y Formas. Cada departamento incluye dos cajones de estacionamiento y una bodega (unos 31–43 m²) además de su área habitable, y comparte el spa, la alberca, el gym, la casa club, el business center, el bar, el salón de usos múltiples y los jardines de la comunidad. Hay veintiséis departamentos disponibles para entrega inmediata (lista de precios 2026, abajo); el departamento muestra amueblado se puede visitar en línea.",
"A single tower of 18 floors, four to five apartments per floor; the larger 228–229 m² units occupy the corners from the seventh floor up.": "Una sola torre de 18 pisos, cuatro o cinco departamentos por piso; las unidades grandes de 228–229 m² ocupan las esquinas del séptimo piso hacia arriba.",
"Magno Home & Towers, Celaya, Guanajuato; about 45 minutes from Querétaro.": "Magno Home & Towers, Celaya, Guanajuato; a unos 45 minutos de Querétaro.",
"Finished; immediate delivery.": "Terminados; entrega inmediata.",
"A furnished apartment inside a community whose amenities are already built — the showroom tour shows the finished standard.": "Un departamento amueblado dentro de una comunidad con las amenidades ya construidas — el recorrido del showroom muestra el estándar terminado.",
"This is Espacios y Formas' project, not mine alone, but I know the floor plans well. Ask me which units I would consider.": "Este es un proyecto de Espacios y Formas, no solo mío, pero conozco bien las plantas. Pregúntame qué unidades consideraría yo.",
"228 m² living + 36 m² parking & storage = 264 m² total · living, dining, kitchen, TV room, terrace · primary suite with walk-in · second bedroom with bath · service room · MX $6,480,904":
 "228 m² habitables + 36 m² de estacionamiento y bodega = 264 m² totales · sala, comedor, cocina, sala de TV, terraza · recámara principal con vestidor · segunda recámara con baño · cuarto de servicio · MX $6,480,904",
"Price list 2026 by Espacios y Formas; units are released as they complete — ask for the current list.": "Lista de precios 2026 de Espacios y Formas; las unidades se liberan conforme se terminan — pide la lista vigente.",
"Celaya, Guanajuato — about 45 minutes from Querétaro and 1 hour from San Miguel de Allende.": "Celaya, Guanajuato — a unos 45 minutos de Querétaro y 1 hora de San Miguel de Allende.",
"Single-family homes and residential lots inside Magno Home & Towers, Celaya, developed by Espacios y Formas. Lots of 225 to 450 m² in Cluster 1, with the spa, pool, gym and clubhouse already built.":
 "Casas unifamiliares y lotes residenciales dentro de Magno Home & Towers, Celaya, desarrollado por Espacios y Formas. Lotes de 225 a 450 m² en el Clúster 1, con spa, alberca, gym y casa club ya construidos.",
"Magno Home & Towers combines residential towers, single-family homes and lots inside one gated community in Celaya, with spa, pool, gym, clubhouse, business center, bar, multipurpose hall, gardens and underground parking. Developed and built by Espacios y Formas; apartments available for immediate delivery.":
 "Magno Home & Towers combina torres residenciales, casas unifamiliares y lotes dentro de una comunidad privada en Celaya, con spa, alberca, gym, casa club, business center, bar, salón de usos múltiples, jardines y estacionamiento subterráneo. Desarrollado y construido por Espacios y Formas; departamentos disponibles para entrega inmediata.",
"Residential towers, single-family homes and lots in one master-planned community.": "Torres residenciales, casas unifamiliares y lotes en una comunidad con plan maestro.",
"Celaya, Guanajuato; about 45 minutes from Querétaro.": "Celaya, Guanajuato; a unos 45 minutos de Querétaro.",
"Apartments with immediate delivery; homes and lots available.": "Departamentos con entrega inmediata; casas y lotes disponibles.",
"One community with three ways in — apartment, house or lot — and amenities already built.": "Una comunidad con tres formas de entrar —departamento, casa o lote— y amenidades ya construidas.",
"Lots of about 225 m² (9 × 25 m), 300 m² (12 × 25 m), 360 m² and 450 m² (15 × 30 m); availability plan of September 2026 shown.": "Lotes de unos 225 m² (9 × 25 m), 300 m² (12 × 25 m), 360 m² y 450 m² (15 × 30 m); se muestra el plano de disponibilidad de septiembre de 2026.",
"Houses built by Espacios y Formas on the community's lots, from MX $5.5M; ask for the current models.": "Casas construidas por Espacios y Formas en los lotes de la comunidad, desde MX $5.5M; pregunta por los modelos vigentes.",
"Residential tower, single-family homes and lots in one gated community, with spa, pool, gym and clubhouse. 26 apartments available for immediate delivery from MX $4.65M; lots of 225–450 m² from MX $2.0M; homes from MX $5.5M.":
 "Torre residencial, casas unifamiliares y lotes en una comunidad privada, con spa, alberca, gym y casa club. 26 departamentos disponibles para entrega inmediata desde MX $4.65M; lotes de 225–450 m² desde MX $2.0M; casas desde MX $5.5M.",
"Residential tower, single-family homes and lots in one gated community in Celaya, with spa, pool, gym and clubhouse. 26 apartments available for immediate delivery; lots in Cluster 1; homes built by Espacios y Formas.":
 "Torre residencial, casas unifamiliares y lotes en una comunidad privada en Celaya, con spa, alberca, gym y casa club. 26 departamentos disponibles para entrega inmediata; lotes en el Clúster 1; casas construidas por Espacios y Formas.",
"Magno Home & Towers — Celaya · Guanajuato | RBC · Roberto Balderas Carrillo": "Magno Home & Towers — Celaya · Guanajuato | RBC · Roberto Balderas Carrillo",
# Peñas / Escondida blocks
"A gated community on the hillside above San Miguel, with views of the Parroquia and the valley. Roberto designs the houses; larger works are built with Espacios y Formas.":
 "Una comunidad privada en la ladera sobre San Miguel, con vistas a la Parroquia y al valle. Roberto diseña las casas; las obras mayores se construyen con Espacios y Formas.",
"A gated community on the hillside above San Miguel de Allende, with views of the Parroquia and the valley. Roberto designs the houses; larger works are built with Espacios y Formas.":
 "Una comunidad privada en la ladera sobre San Miguel de Allende, con vistas a la Parroquia y al valle. Roberto diseña las casas; las obras mayores se construyen con Espacios y Formas.",
"Peñas Arriba — San Miguel de Allende · Guanajuato | RBC · Roberto Balderas Carrillo": "Peñas Arriba — San Miguel de Allende · Guanajuato | RBC · Roberto Balderas Carrillo",
"San Miguel de Allende · Guanajuato": "San Miguel de Allende · Guanajuato",
"A residential community in San Miguel de Allende, now completed. A few units remain available for sale — ask for the current availability.":
 "Una comunidad residencial en San Miguel de Allende, ya terminada. Quedan algunas unidades disponibles para venta — pregunta por la disponibilidad actual.",
"A residential development in San Miguel de Allende. Details to follow.": "Un desarrollo residencial en San Miguel de Allende. Detalles próximamente.",
"San Miguel de Allende · Espacios y Formas": "San Miguel de Allende · Espacios y Formas",
"Celaya · Guanajuato · Espacios y Formas": "Celaya · Guanajuato · Espacios y Formas",
"San Miguel de Allende · RBC with Espacios y Formas": "San Miguel de Allende · RBC con Espacios y Formas",
# construction
"Construction — Roberto Balderas Carrillo, Arquitecto, with Espacios y Formas | RBC": "Construcción — Roberto Balderas Carrillo, Arquitecto, con Espacios y Formas | RBC",
"Residential and commercial construction in San Miguel de Allende and the Bajío, directed by architect Roberto Balderas Carrillo and built with Espacios y Formas.":
 "Construcción residencial y comercial en San Miguel de Allende y el Bajío, dirigida por el arquitecto Roberto Balderas Carrillo y construida con Espacios y Formas.",
"RBC / Construction": "RBC / Construcción", "Construction.": "Construcción.", "› Construction": "› Construcción",
"Directed personally. Larger works are built with Espacios y Formas.": "Dirigida personalmente. Las obras mayores se construyen con Espacios y Formas.",
"Sites": "Obras", "Build": "Construir", "From your plans or ours.": "Con tus planos o los nuestros.",
"Renovations, houses, larger residences and developments. English and Spanish.": "Remodelaciones, casas, residencias grandes y desarrollos. Español e inglés.",
"Built by RBC": "Construida por RBC", "Espacios y Formas": "Espacios y Formas",
"San Miguel de Allende · Built by RBC": "San Miguel de Allende · Construida por RBC",
"Piedras Azules · San Miguel de Allende · Built by RBC": "Piedras Azules · San Miguel de Allende · Construida por RBC",
"El Campanario Residencial & Golf · Querétaro · Built by RBC": "El Campanario Residencial & Golf · Querétaro · Construida por RBC",
"Los Huizaches · San Miguel de Allende · Built by RBC": "Los Huizaches · San Miguel de Allende · Construida por RBC",
"3 photos": "3 fotos", "7 photos": "7 fotos", "9 photos": "9 fotos", "10 photos": "10 fotos", "14 photos": "14 fotos", "17 photos": "17 fotos",
# contact
"Contact — Start a Project, Buy or Sell a Property | RBC · Roberto Balderas Carrillo, Arquitecto": "Contacto — Iniciar un proyecto, comprar o vender una propiedad | RBC · Roberto Balderas Carrillo, Arquitecto",
"Contact architect Roberto Balderas Carrillo in San Miguel de Allende: start a design-and-build project, ask for a reading of your lot, buy a selected property or have a property looked at for sale..":
 "Contacta al arquitecto Roberto Balderas Carrillo en San Miguel de Allende: inicia un proyecto de diseño y construcción, pide una lectura de tu terreno, compra una propiedad seleccionada o que revise una propiedad para venta.",
"RBC / Contact": "RBC / Contacto", "› Contact": "› Contacto",
"Tell me what you have in mind.": "Cuéntame qué tienes en mente.",
"General inquiry": "Consulta general", "Anything else.": "Cualquier otra cosa.",
"Project": "Proyecto", "Buying": "Comprar", "Your name": "Tu nombre", "Best way to reach you": "Mejor forma de contactarte",
"Type": "Tipo", "City": "Ciudad", "Goal": "Objetivo", "When": "Cuándo", "Message": "Mensaje", "Status": "Estado", "Visits": "Visitas",
"Budget (USD)": "Presupuesto (USD)", "Describe it": "Descríbelo", "Describe the property": "Describe la propiedad",
"What you need": "Qué necesitas", "What you'd like": "Qué te gustaría", "Your property": "Tu propiedad", "Where is the property": "Dónde está la propiedad",
"What matters most, or a link to a property": "Lo más importante, o un link a una propiedad",
"Send to Roberto": "Enviar a Roberto", "Tell me about it": "Cuéntame",
"A lot, a sketch or an idea.": "Un terreno, un croquis o una idea.", "A selected property, or one you found elsewhere.": "Una propiedad seleccionada, o una que encontraste en otro lado.",
"Design only": "Solo diseño", "Construction from my plans": "Construcción con mis planos", "Renovation / restoration": "Remodelación / restauración",
"A building / development": "Un edificio / desarrollo", "I don't have a lot yet": "Aún no tengo terreno", "A reading of my lot": "Una lectura de mi terreno",
"Elsewhere in the Bajío": "Otro lugar del Bajío", "Elsewhere in Mexico": "Otro lugar de México", "Not sure yet": "Aún no sé",
"As soon as possible": "Lo antes posible", "3–6 months": "3–6 meses", "6–12 months": "6–12 meses", "Exploring": "Explorando",
"Under $300K": "Menos de $300K", "Under $400K": "Menos de $400K", "Over $1.2M": "Más de $1.2M", "Over $3M": "Más de $3M",
"Rent": "Renta", "Direct": "Directo", "All properties": "Todas las propiedades", "See it in person, or on a video call.": "Verla en persona, o por videollamada.",
"San Miguel de Allende / Celaya": "San Miguel de Allende / Celaya", "Offices · San Miguel de Allende / Celaya": "Oficinas · San Miguel de Allende / Celaya",
"espaciosyformas.com.mx ↗": "espaciosyformas.com.mx ↗",
# property pages
"Casa Horizonte · M4-L7 — For sale in San Miguel de Allende | RBC · Roberto Balderas Carrillo, Arquitecto": "Casa Horizonte · M4-L7 — En venta en San Miguel de Allende | RBC · Roberto Balderas Carrillo, Arquitecto",
"Casa Cima · M6-L1 — For sale in San Miguel de Allende | RBC · Roberto Balderas Carrillo, Arquitecto": "Casa Cima · M6-L1 — En venta en San Miguel de Allende | RBC · Roberto Balderas Carrillo, Arquitecto",
"Casa Musa — For rent in San Miguel de Allende | RBC · Roberto Balderas Carrillo, Arquitecto": "Casa Musa — En renta en San Miguel de Allende | RBC · Roberto Balderas Carrillo, Arquitecto",
"Panoramic Suite — For rent in San Miguel de Allende | RBC · Roberto Balderas Carrillo, Arquitecto": "Suite Panorámica — En renta en San Miguel de Allende | RBC · Roberto Balderas Carrillo, Arquitecto",
"Casa Ether — For sale in near San Miguel de Allende | RBC · Roberto Balderas Carrillo, Arquitecto": "Casa Ether — En venta cerca de San Miguel de Allende | RBC · Roberto Balderas Carrillo, Arquitecto",
"Casa Travertino — For sale in Querétaro | RBC · Roberto Balderas Carrillo, Arquitecto": "Casa Travertino — En venta en Querétaro | RBC · Roberto Balderas Carrillo, Arquitecto",
"Panoramic Suite": "Suite Panorámica", "› Panoramic Suite": "› Suite Panorámica", "The house": "La casa", "The space": "El espacio",
"Casa Horizonte · M4-L7 — plan": "Casa Horizonte · M4-L7 — planta", "Casa Cima · M6-L1 — plan": "Casa Cima · M6-L1 — planta", "Casa Ether — plan": "Casa Ether — planta",
"Provisional images — photography in progress.": "Imágenes provisionales — fotografía en proceso.", "Plans available on request.": "Plantas disponibles a solicitud.",
"Presented by architect Roberto Balderas Carrillo.": "Presentada por el arquitecto Roberto Balderas Carrillo.",
"— R. Balderas Carrillo, Arquitecto": "— R. Balderas Carrillo, Arquitecto",
})

# ── patterns ──
PAT = [
 (re.compile(r'^Apartment (\d+) · floor (\d+)$'), lambda m: f"Departamento {m.group(1)} · piso {m.group(2)}"),
 (re.compile(r'^(\d+) photos$'), lambda m: f"{m.group(1)} fotos"),
 (re.compile(r'^([\d.]+) m² living \+ ([\d.]+) m² parking & storage · (\d) bedrooms?$'), lambda m: f"{m.group(1)} m² habitables + {m.group(2)} m² de estacionamiento y bodega · {m.group(3)} recámara{'s' if m.group(3)!='1' else ''}"),
 (re.compile(r'^(.*) — construction, (.*)$'), lambda m: f"{tr(m.group(1))} — obra, {tr(m.group(2))}"),
 (re.compile(r'^(.*?)… Presented by architect Roberto Balderas Carrillo\.$'), lambda m: f"{tr_prefix(m.group(1))}… Presentada por el arquitecto Roberto Balderas Carrillo."),
 (re.compile(r'^› (.*)$'), lambda m: "› " + tr(m.group(1))),
 (re.compile(r'^(.*) — (.*)$'), lambda m: f"{tr(m.group(1))} — {tr(m.group(2))}"),
]

def tr_prefix(s):
    for k, v in T.items():
        if k.startswith(s): return v[:len(s)]
    return s

def tr(s):
    if s in T: return T[s]
    m = re.match(r"^(<span style='[^']*'>)(.*)(</span>)$", s)
    if m: return m.group(1) + tr(m.group(2)) + m.group(3)
    for p, f in PAT:
        m = p.match(s)
        if m:
            out = f(m)
            if out != s: return out
    return s

def tr_text(s):
    """Translate a text node keeping surrounding whitespace."""
    core = s.strip()
    if not core: return s
    t = tr(core)
    if t == core: return s
    return s.replace(core, t, 1)

# v24 — project sheet (Architecture modal)
T.update({
 "About the project": "Sobre el proyecto", "Built by RBC": "Construido por RBC", "Project": "Proyecto",
 "View on Instagram": "Ver en Instagram", "Ask about this project": "Preguntar por este proyecto", "This house is for sale →": "Esta casa está en venta →",
 "Competition · research": "Concurso · investigación", "Condesa · Mexico City": "Condesa · Ciudad de México", "Mérida · Yucatán": "Mérida · Yucatán",
 "A contemporary country house on a hilltop in Piedras Azules. Construction and design intervened by RBC on an existing siting and scheme: the plan, façades and interiors were reworked and the house was built by RBC. Sliding glass walls open fully to the landscape; Italian hardwood on floors and ceilings; a Spanish kitchen.":
 "Casa de campo contemporánea en lo alto de una colina en Piedras Azules. Construcción y diseño intervenidos por RBC sobre un sembrado y planteamiento existentes: se reelaboraron la planta, las fachadas y los interiores, y la casa fue construida por RBC. Muros de cristal corredizos que se abren por completo al paisaje; madera italiana en pisos y plafones; cocina española.",
 "Country house on open land: long horizontal volumes, deep covered terraces and a plan that opens entirely to the landscape.": "Casa de campo en terreno abierto: volúmenes largos y horizontales, terrazas cubiertas profundas y una planta que se abre por completo al paisaje.",
 "Shaped by its topography: the house follows the slope, unfolding across levels and opening both floors toward San Miguel. Entered from the top; rock from the excavation left exposed inside. Under construction; for sale.": "Moldeada por su topografía: la casa sigue la pendiente, se despliega en niveles y abre ambas plantas hacia San Miguel. Se entra por arriba; la roca de la excavación queda expuesta en el interior. En construcción; en venta.",
 "Gallery, studio and private refuge in one sequence: a contemplation courtyard leads to rooms for permanent and temporary exhibitions, sculpture, painting and performance. Water, natural light and honest materials.": "Galería, taller y refugio privado en una sola secuencia: un patio de contemplación conduce a salas para exposiciones permanentes y temporales, escultura, pintura y performance. Agua, luz natural y materiales honestos.",
 "Newly built on the last lot of its private street, facing the mountains: double-height living and bar, pool and sun deck, four en-suite bedrooms plus staff quarters. Designed and built by RBC; for sale.": "Recién construida en el último lote de su calle privada, frente a las montañas: sala y bar a doble altura, alberca y asoleadero, cuatro recámaras con baño más cuarto de servicio. Diseñada y construida por RBC; en venta.",
 "A hotel immersed in the landscape, transforming an existing ranch through a sensitive master plan: stone-walled cabins set into the hill, an integrated pool, an open-air deck for events, greenhouse and productive gardens.": "Un hotel inmerso en el paisaje que transforma un rancho existente mediante un plan maestro sensible: cabañas de muros de piedra asentadas en la ladera, alberca integrada, deck al aire libre para eventos, invernadero y huertos productivos.",
 "Fluid, parametric curves unify every area of the bar into one enveloping volume, absorbing the uneven levels of an old house in the center without breaking the flow.": "Curvas fluidas y paramétricas unifican todas las áreas del bar en un solo volumen envolvente, absorbiendo los desniveles de una casa antigua del centro sin romper la continuidad.",
 "Restoration, construction, adaptation and interior design of a historic house: the restaurant on the ground floor, and above it Casa Musa and the Panoramic Suite, both available for mid-term stays.": "Restauración, construcción, adaptación y diseño interior de una casa histórica: el restaurante en planta baja y, arriba, Casa Musa y la Panoramic Suite, ambas disponibles para estancias de mediano plazo.",
 "Showroom and service facility for a heavy-machinery distributor.": "Sala de exhibición y taller de servicio para un distribuidor de maquinaria pesada.",
 "Remodelling proposal and new façade for an apartment building in Condesa.": "Propuesta de remodelación y nueva fachada para un edificio de departamentos en la Condesa.",
 "Office interiors: timber, planting and daylight.": "Interiores de oficinas: madera, vegetación y luz natural.",
 "Country residence outside town — stone, timber and glass under one continuous roof plane.": "Residencia de campo a las afueras — piedra, madera y cristal bajo un solo plano de cubierta continuo.",
 "Projects for San Mezcal rooftop, San Burger and Terraza Quiote — terraces, bars and dining rooms over the historic center.": "Proyectos para el rooftop de San Mezcal, San Burger y Terraza Quiote — terrazas, bares y comedores sobre el centro histórico.",
 "Preliminary project for a commercial plaza with a residential tower.": "Anteproyecto de una plaza comercial con torre residencial.",
 "Retail design: Plaza Atrio in San Miguel and Plaza Puerto Paraíso in Los Cabos — parametric timber ribs, natural stone and warm light.": "Diseño de tiendas: Plaza Atrio en San Miguel y Plaza Puerto Paraíso en Los Cabos — costillas paramétricas de madera, piedra natural y luz cálida.",
 "Preliminary project for a wellness complex — bar, yoga and treatment spaces in the Yucatán landscape.": "Anteproyecto de un complejo de bienestar — bar, yoga y espacios de tratamiento en el paisaje yucateco.",
 "Renovation of an apartment in the historic center with a panoramic roof terrace.": "Renovación de un departamento en el centro histórico con roof garden panorámico.",
 "Guest suites in a house in San Miguel de Allende.": "Suites de huéspedes en una casa de San Miguel de Allende.",
 "Retail design for Origen in San Miguel de Allende.": "Diseño de tienda para Origen en San Miguel de Allende.",
 "Preliminary project for Saiko in San Miguel de Allende.": "Anteproyecto para Saiko en San Miguel de Allende.",
 "Preliminary project for the architect's own house.": "Anteproyecto de la casa propia del arquitecto.",
 "A house in the historic center of San Miguel de Allende — restoration and new architecture within the walls of the old town.": "Una casa en el centro histórico de San Miguel de Allende — restauración y arquitectura nueva dentro de los muros del casco antiguo.",
 "With Ana Laura González: a pavilion whose façade preserves a message in binary code. Plus computational studies in Grasshopper/Rhino and the 'NFT Eggs' parametric collection.": "Con Ana Laura González: un pabellón cuya fachada conserva un mensaje en código binario. Además, estudios computacionales en Grasshopper/Rhino y la colección paramétrica 'NFT Eggs'.",
 "A single-storey country house: one long roof, glass to the landscape, stone base.": "Casa de campo de una planta: una cubierta larga, cristal hacia el paisaje, basamento de piedra.",
 "Two volumes on a slope: a cantilevered social level over the garage, bedrooms behind.": "Dos volúmenes sobre una pendiente: un nivel social en voladizo sobre la cochera, recámaras atrás.",
 "Showroom and service facility for a car dealership.": "Sala de exhibición y taller de servicio para una agencia de autos.",
 "Urbanization, stone terracing, amenity buildings and houses on the hillside above San Miguel.": "Urbanización, terrazas de piedra, edificios de amenidades y casas en la ladera sobre San Miguel.",
 "A single-level country house on a steel-roofed platform, open to the valley.": "Casa de campo de un nivel sobre una plataforma con cubierta de acero, abierta al valle.",
 "A large house on the rock at the top of Peñas Arriba: three levels stepping down the slope, terraces with plunge pools, a family wing and a guest wing, and parking for four cars.": "Una casa grande sobre la roca en lo alto de Peñas Arriba: tres niveles que descienden con la pendiente, terrazas con albercas de inmersión, un ala familiar y un ala de huéspedes, y estacionamiento para cuatro autos.",
 "House by a golf course; stone, wood ceilings and an inner patio with a pool.": "Casa junto a un campo de golf; piedra, plafones de madera y un patio interior con alberca.",
})
T.update({
 "Completed · a few units available": "Terminado · algunas unidades disponibles", "Completed": "Terminado", "community": "comunidad",
 "A few": "Algunas", "units for sale": "unidades en venta", "& gardens": "y jardines",
 "Completed community": "Comunidad terminada", "A few units available for sale": "Algunas unidades disponibles en venta", "Built by Espacios y Formas": "Construida por Espacios y Formas",
 "Completed; a few units available.": "Terminada; algunas unidades disponibles.", "San Miguel de Allende.": "San Miguel de Allende.",
 "A development by Espacios y Formas": "Un desarrollo de Espacios y Formas", "Espacios y Formas · completed": "Espacios y Formas · terminada",
})

# v24b — project descriptions condensed from Instagram captions (22-sep-2026)
T.update({
 'Casa Horizonte is shaped by two defining elements: views and topography. Set on one of the highest points of Peñas Arriba, the house opens toward long, uninterrupted views of San Miguel de Allende. Rather than altering the land, the project follows the natural slope of the hill, unfolding across levels and opening both floors toward the city. The house is lived from the top down: at the entrance level, the social areas, main bedroom, terraces and pool; below, following the hillside, the secondary bedrooms, the wine cellar and the private garden. On the lower level, natural rock revealed by the excavation was intentionally left exposed, so the hillside itself becomes part of the architecture. 827 m² site · 622 m² built + pool. Currently available for sale.': 'Casa Horizonte está definida por dos elementos: las vistas y la topografía. Ubicada en uno de los puntos más altos de Peñas Arriba, la casa se abre a vistas largas e ininterrumpidas de San Miguel de Allende. En lugar de modificar el terreno, el proyecto sigue la pendiente natural del cerro, se despliega en distintos niveles y abre ambas plantas hacia la ciudad. La casa se vive de arriba hacia abajo: al nivel del acceso, las áreas sociales, la recámara principal, las terrazas y la alberca; abajo, siguiendo la pendiente, las recámaras secundarias, la cava y el jardín privado. En la planta baja, la roca natural revelada por la excavación se dejó expuesta intencionalmente, de modo que el propio cerro forma parte de la arquitectura. 827 m² de terreno · 622 m² de construcción + alberca. Actualmente disponible en venta.',
 'A contemporary country house on a hilltop in Piedras Azules. Construction and design intervened by RBC on an existing siting and scheme: starting from a previous scheme, circulation, proportions and material language were adjusted, and a new spatial reading was developed that prioritises the relationship with the landscape. The construction responds to the topography, integrates into the terrain and takes advantage of its views, combining sober finishes with elements from the site. Sliding glass walls open fully to the landscape; Italian hardwood on floors and ceilings; a Spanish kitchen. Photography: Alejandro Torre.': 'Casa de campo contemporánea en lo alto de una colina en Piedras Azules. Construcción y diseño intervenidos por RBC sobre un sembrado y planteamiento existentes: a partir de un planteamiento previo se ajustaron recorridos, proporciones y lenguaje material, y se desarrolló una nueva lectura espacial que prioriza la relación con el paisaje. La construcción responde a la topografía, se integra al terreno y aprovecha sus vistas, combinando acabados sobrios con elementos del sitio. Muros de cristal corredizos que se abren por completo al paisaje; madera italiana en pisos y plafones; cocina española. Fotografía: Alejandro Torre.',
 'Casa X is a proposal for a hotel immersed in the landscape, conceived for rest, contemplation and contact with nature. The project transforms an existing ranch through a master plan that uses the topography, vegetation and pre-existing buildings for a sensitive, low-impact intervention. The architecture seeks to disappear into the landscape: single, double and triple cabins are set into the hillside and oriented toward the mountain views, built with a play of parallel stone walls that give privacy, comfort and a constant relationship with the surroundings. The ensemble is completed by a pool integrated into the terrain and a deck for open-air events, classes and concerts that uses the topography itself as a natural stage. More than a collection of buildings, Casa X builds an integral wellness experience: spaces for ceremonies and wellbeing, a dining room with greenhouse and productive gardens, an existing water reserve integrated into the site, and complementary proposals such as a geodesic henhouse and natural air-cooling systems using water and fired-clay modules.': 'Casa X es una propuesta para un hotel inmerso en el paisaje, concebido para el descanso, la contemplación y el encuentro con la naturaleza. El proyecto parte de la transformación de un rancho existente mediante un plan maestro que aprovecha la topografía, la vegetación y las construcciones preexistentes para una intervención sensible y de bajo impacto. La arquitectura busca desaparecer dentro del paisaje: cabañas individuales, dobles y triples se incrustan en la topografía y se orientan hacia las vistas de las montañas, construidas mediante un juego de muros de piedra paralelos que ofrecen privacidad, confort y una relación constante con el entorno. El conjunto se complementa con una alberca integrada al terreno y un deck para eventos, clases y conciertos al aire libre que utiliza la propia topografía como escenario natural. Más que una colección de edificios, Casa X construye una experiencia integral de bienestar: espacios para ceremonias y bienestar, un comedor acompañado por invernadero y huertas productivas, una reserva de agua existente integrada al sitio, y propuestas complementarias como un gallinero geodésico y sistemas naturales de enfriamiento de aire mediante agua y módulos de barro cocido.',
 'Project for a private art pavilion conceived as a refuge for creation, contemplation and exhibition. The building brings together gallery, studio and private retreat in a single architectural experience: a contemplation courtyard leads to spaces for the permanent collection, temporary shows, sculpture, painting and performance, complemented by areas for creative work and reflection. Rooms, corridors, voids and courtyards of different scales build a carefully choreographed sequence that reveals the architecture gradually — changes of scale, height, light and atmosphere turn movement into discovery, reflection and surprise. The presence of water, natural light and honest materials explores the relationship between art, matter and silence. Born as a personal creative refuge, it is also designed to host exhibitions, gatherings, performances and special events.': 'Proyecto para un pabellón de arte privado concebido como un refugio para la creación, la contemplación y la exhibición. El edificio reúne galería, estudio y refugio privado en una única experiencia arquitectónica: un patio de contemplación conduce a espacios para la colección permanente, muestras temporales, escultura, pintura y performance, complementados por áreas para el trabajo creativo y la reflexión. Salas, corredores, vacíos y patios de distintas escalas construyen una secuencia cuidadosamente coreografiada que revela la arquitectura gradualmente: los cambios de escala, altura, luz y atmósfera transforman el recorrido en descubrimiento, reflexión y sorpresa. La presencia del agua, la luz natural y los materiales honestos explora la relación entre arte, materia y silencio. Aunque nace como un refugio creativo personal, también está diseñado para albergar exhibiciones, encuentros, performances y eventos especiales.',
 "The design of Bar Bachus centres on fluid curves that create an enveloping, integrated space. Using parametric design principles, volumes unify every area of the bar into a cohesive whole, with the bar counter as the central piece. It adapts to an old house in the centre of San Miguel de Allende, blending modern elements with historical charm; the design elements compensate for the house's uneven levels, creating bars at different heights without interrupting the flow of the space.": 'El diseño de Bar Bachus se centra en curvas fluidas que crean un espacio envolvente e integrado. Con principios de diseño paramétrico, los volúmenes integran todas las áreas del bar como un todo, con la barra como pieza central. Se adapta a una casa antigua en el centro de San Miguel de Allende, combinando elementos modernos con el encanto histórico; los elementos del diseño compensan los desniveles de la casa, creando barras a diferentes alturas sin interrumpir la fluidez del espacio.',
 'Binary Code Pavilion — competition entry with Ana Laura González for competitions.archi, sited in the Sahara Desert, Egypt. The brief: how to preserve and show the best of our species for a far future, so that other life forms or future civilisations could learn about our achievements. The pavilion preserves a message for posterity on its whole façade, written in binary code that can be translated into text, images or sounds: the outer shell is made of blocks that physically represent the binary system — solid (0) or hollowed-out (1).': 'Binary Code Pavilion — propuesta de concurso con Ana Laura González para competitions.archi, situada en el desierto del Sahara, Egipto. El reto: cómo preservar y mostrar lo mejor de nuestra especie para un futuro lejano, de modo que otras formas de vida o civilizaciones futuras puedan conocer nuestros logros. El pabellón conserva un mensaje para la posteridad en toda su fachada, escrito en código binario que puede traducirse en texto, imágenes o sonidos: la envolvente está hecha de bloques que representan físicamente el sistema binario — sólidos (0) o ahuecados (1).',
 'Country house project in Jalpa, Guanajuato.': 'Proyecto de casa de campo en Jalpa, Guanajuato.',
 'Country house project in San Miguel de Allende.': 'Proyecto de casa de campo en San Miguel de Allende.',
 'Renovation project of a house in the centre of San Miguel de Allende: an apartment with a panoramic-view terrace, available for rent.': 'Proyecto de renovación de una casa en el centro de San Miguel de Allende: departamento con terraza con vista panorámica, disponible para renta.',
 'Project for the remodelling of a building in Condesa, Mexico City.': 'Proyecto para la remodelación de un edificio en la Condesa, Ciudad de México.',
 'Project for Reset333, Mérida.': 'Proyecto para Reset333, Mérida.',
 'Projects for the San Mezcal rooftop, San Burger and Terraza Quiote · San Miguel de Allende.': 'Proyectos para el rooftop de San Mezcal, San Burger y Terraza Quiote · San Miguel de Allende.',
 'Design for the Tuluminati stores: Plaza Atrio, San Miguel de Allende, and Plaza Puerto Paraíso, Los Cabos.': 'Diseño para las tiendas Tuluminati: Plaza Atrio, San Miguel de Allende, y Plaza Puerto Paraíso, Los Cabos.',
 'Project for Amecsa, a heavy-machinery distributor.': 'Proyecto para Amecsa, distribuidora de maquinaria pesada.',
 'Proposal for the design of a car dealership.': 'Propuesta para el diseño de una agencia de autos.',
 'Commercial plaza · Querétaro.': 'Plaza comercial · Querétaro.',
 'Daily Veggies offices · Querétaro.': 'Oficinas Daily Veggies · Querétaro.',
})

# v24c — RBC presentation text by Roberto (23-sep-2026)
T.update({
 'Roberto Balderas Carrillo is an architect based in San Miguel de Allende. Through his practice, RBC, he works across architecture, interiors and construction, while representing a select number of properties he knows firsthand.': 'Roberto Balderas Carrillo es arquitecto con base en San Miguel de Allende. A través de su práctica, RBC, trabaja en arquitectura, interiores y construcción, además de representar una selección de propiedades que conoce de primera mano.',
 'Each project develops its own architectural language, shaped by its context, scale and purpose. RBC operates within': 'Cada proyecto desarrolla su propio lenguaje arquitectónico, definido por su contexto, escala y propósito. RBC forma parte de',
 ', the Balderas family’s architecture, construction and development firm, with more than 30 years of experience and offices in Celaya and San Miguel de Allende. This allows for a personal, hands-on approach to every project, supported by the experience, team and capabilities of an established firm.': ', la firma familiar de arquitectura, construcción y desarrollo de la familia Balderas, con más de 30 años de experiencia y oficinas en Celaya y San Miguel de Allende. Esto permite ofrecer una atención personal y directa en cada proyecto, respaldada por la experiencia, el equipo y la capacidad de una firma consolidada.',
})

T.update({"Offices in Celaya and San Miguel de Allende": "Oficinas en Celaya y San Miguel de Allende"})

T.update({"m² built · 7,933 sq ft": "m² construidos · 7,933 sq ft", "m² lot · 11,858 sq ft": "m² de lote · 11,858 sq ft", "737 m² (7,933 sq ft) built on a 1,101.65 m² (11,858 sq ft) lot": "737 m² (7,933 sq ft) construidos en un lote de 1,101.65 m² (11,858 sq ft)"})
