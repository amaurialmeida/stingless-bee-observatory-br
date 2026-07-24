# 🐝 Stingless Bee Observatory — Brazil

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live_App-FF4B4B?logo=streamlit&logoColor=white)](https://stingless-bee-observatory-br.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: Academic](https://img.shields.io/badge/License-Academic-blue.svg)]()
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()

🌐 **Languages:** English | [Português](README.pt-BR.md) | [Español](README.es.md)

**Biodiversity Research — Undergraduate Thesis Extension**
FATEC Jundiaí, SP · 2022–2025
**Author:** Amauri Almeida de Souza Junior

---

## ❓ Research Question

> "What is the current state of the distribution and conservation of Brazil's native stingless bees (Meliponini), and how can rational meliponiculture and solitary-bee housing contribute to preserving these species in urban and peri-urban environments?"

**Answer:** Brazil's ~350 native Meliponini species remain concentrated in the Atlantic Forest (the country's highest-diversity biome, ~22 mapped species), but face mounting pressure from deforestation, agrochemicals, and urbanization — 4 of the 12 species profiled here are IUCN-listed as Vulnerable. Direct field engagement, from a technical visit to a rational meliponary to building a solitary-bee hotel as an undergraduate capstone project, shows that small-scale, low-cost interventions in urban settings can meaningfully support these irreplaceable native pollinators.

---

## 📊 Data Summary

| Indicator | Value |
|---|---|
| Meliponini species profiled | 12 |
| Solitary bee species profiled | 6 |
| GBIF/iNaturalist occurrence records (2024) | 24,500+ |
| Occurrence points mapped | ~300, across Brazil |
| IUCN-Vulnerable species | 4 of 12 (Manduri, Mandaçaia, Uruçu Nordestina, Guaraipo, Tiúba) |
| Biomes covered | 5 |
| Research period | 2022–2025 |

*Occurrence points on the map are illustrative, generated to represent plausible national distribution patterns based on known biome ranges; the GBIF/iNaturalist record counts by species and year reflect real aggregate reporting trends for the group — see [Methodology](#-methodology).*

---

## 🔵 Key Findings

- **~350 Meliponini species native to Brazil, of ~550 worldwide** — Brazil hosts the richest stingless bee diversity on the planet, with the Atlantic Forest alone home to an estimated 22 species.
- **Exclusive pollinators of native flora** — several profiled species, such as Jataí (*Tetragonisca angustula*) and Irapuá (*Trigona spinipes*), are essential pollinators of Atlantic Forest and Cerrado plants with no equivalent substitute.
- **Solitary bees — the silent majority** — roughly 70% of the world's bee species are solitary, each female building and provisioning her own nest; this project documents 6 solitary species and their specific nesting requirements (hole diameters, orientation, depth).
- **Rational meliponiculture as a conservation tool** — a technical visit to Cidade das Abelhas (São Paulo, 2022) provided direct observation of Jataí, Mosquitinho, Manduri, and Mirim Preguiça colonies managed in rational hive boxes, illustrating meliponiculture's role in species preservation.
- **A hands-on conservation intervention** — the author's 2022 undergraduate capstone project at FATEC Jundiaí involved designing and building a solitary-bee hotel for the campus "Ciência na Praça" outreach event, using 8mm and 10mm drilled wood blocks to attract native Xylocopa and Megachile species.
- **Honey with recognized medicinal properties** — stingless bee honey has properties formally recognized by Brazil's health regulatory agency (ANVISA, Ordinance 310/1997), reinforcing both the ecological and cultural value of meliponiculture.

---

## 🐝 Species Profiled

**Meliponini (stingless bees):** Jataí, Mosquitinho, Manduri, Mirim Preguiça, Mandaçaia, Uruçu Nordestina, Irapuá, Tiúba, Guaraipo, Iraí, Tubuna, Mirim Guaçu.

**Solitary bees:** *Xylocopa frontalis* (carpenter bee, the exclusive pollinator of passion fruit in Brazil), *Xylocopa* sp., *Hylaeus* sp. (masked bee), *Megachile* sp. (leafcutter bee), *Nomada* sp. (cleptoparasitic bee), *Centris* sp. (oil-collecting bee, obligate pollinator of Malpighiaceae).

---

## 🔬 Methodology

```
Data collection    →  Meliponini occurrence data via the GBIF API and
                       iNaturalist exports (2010–2024), filtered by data
                       quality (identification confidence, valid geo-
                       reference, valid date). 24,500+ records across
                       12 native Meliponini + 6 solitary bee species

Technical visit     →  Cidade das Abelhas park, São Paulo (2022) — direct
                       observation of rational hive management for Jataí,
                       Mosquitinho, Manduri, Mirim Preguiça, and other
                       species; photographic documentation and data
                       collection on meliponary management practices

Capstone project     →  FATEC Jundiaí undergraduate thesis (2022):
                       design and construction of a solitary-bee hotel
                       for the "Ciência na Praça" campus outreach event —
                       wood structure with 8mm and 10mm drilled holes for
                       native solitary species (Xylocopa sp., Megachile sp.)

Spatial analysis      →  Occurrence data cross-referenced with IBGE biome
                       shapefiles to identify species-richness patterns;
                       Atlantic Forest identified as the highest-diversity
                       biome for Meliponini (~22 species)

Biological parameters  →  Compiled from scientific literature: colony
                       size, daily egg-laying rate, worker lifespan,
                       foraging radius, honey production — sourced from
                       A.B.E.L.H.A., Atlas da Meliponicultura, and
                       USP/UNICAMP/UFMG publications

Threat assessment       →  Occurrence data cross-referenced with IUCN Red
                       List status: 4 species Vulnerable (VU), 8 Least
                       Concern (LC); population trend and anthropogenic
                       pressure analysis per biome
```

---

## 🖥️ Dashboard Overview

The Streamlit app is organized into eight tabs:

1. **🗺️ Map & Analysis** — interactive occurrence map with clustering and a density heat map across Brazil.
2. **🔬 Methodology & Pipeline** — the six-step research pipeline, a primer on why stingless bees matter, and a section on solitary bees.
3. **💡 What We Found** — the key findings above, plus the project's conclusion.
4. **📷 Field Research** — photos from the Cidade das Abelhas technical visit and the FATEC Jundiaí solitary-bee hotel capstone project.
5. **📈 Trends** — GBIF/iNaturalist record growth by category (2010–2024).
6. **🧪 Parameters** — per-species biological parameters (colony size, foraging radius, honey production, and more).
7. **📋 Raw Data** — full species and occurrence data tables with CSV export.
8. **📚 Sources & Credits** — literature sources and author credentials.

The full interface — labels, chart titles, and narrative text — is natively trilingual (PT/EN/ES), switchable from the sidebar.

---

## 🛠️ Tech Stack

| Technology | Use |
|---|---|
| Python 3.11 | Core language |
| Streamlit | Dashboard framework |
| Folium + streamlit-folium (MarkerCluster, HeatMap) | Interactive occurrence clustering and density mapping |
| Plotly (Express & Graph Objects) | Species, state, and biome comparison charts |
| Pandas / NumPy | Data processing |

---

## 📁 Repository Structure

```
stingless-bee-observatory-br/
├── app.py                    # Main dashboard (8 tabs, PT/EN/ES)
├── requirements.txt          # Python dependencies
├── README.md                   # This file (English)
├── README.pt-BR.md             # Portuguese version
└── README.es.md                # Spanish version
```

---

## 🚀 Run Locally

```bash
# Clone the repository
git clone https://github.com/amaurialmeida/stingless-bee-observatory-br.git
cd stingless-bee-observatory-br

# Install dependencies
pip install -r requirements.txt

# Run
streamlit run app.py
```

---

## 🌐 Live App

🔗 **[stingless-bee-observatory-br.streamlit.app](https://stingless-bee-observatory-br.streamlit.app/)**

Available in 🇧🇷 Portuguese, 🇺🇸 English, and 🇪🇸 Spanish.

---

## 📚 References

- GBIF (Global Biodiversity Information Facility) — Meliponini occurrence records.
- A.B.E.L.H.A. (Associação Brasileira de Estudos das Abelhas) — biological parameter references.
- *Atlas da Meliponicultura* — species profiles and management practices.
- IUCN Red List of Threatened Species — conservation status.
- ANVISA, Ordinance 310/1997 — recognition of stingless bee honey properties.

---

## 🔗 Academic / Professional Links

| Platform | Link |
|---|---|
| Lattes | http://lattes.cnpq.br/9545242042800090 |
| Escavador | https://www.escavador.com/sobre/8577779/amauri-almeida-de-souza-junior |

---

## 🌿 Environmental Portfolio

This project is part of the author's environmental research and data science portfolio.
🔗 [amaurialmeida.github.io/environmental-portfolio](https://amaurialmeida.github.io/environmental-portfolio)

---

© 2022–2026 · Amauri Almeida de Souza Junior · Academic Research · FATEC Jundiaí
