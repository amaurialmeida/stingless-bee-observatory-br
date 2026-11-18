import streamlit as st
import folium
from folium.plugins import MarkerCluster, HeatMap
from streamlit_folium import folium_static
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import os
import io

from translations import TRANSLATIONS

st.set_page_config(
    page_title="Observatório Meliponini · Brasil",
    page_icon="🐝",
    layout="wide"
)

# ============================================================
# SISTEMA DE IDIOMAS (10 idiomas) — padrão do projeto do rio
# ============================================================
LANGS = [
    ("pt", "🇧🇷", "PT"), ("en", "🇺🇸", "EN"), ("es", "🇪🇸", "ES"),
    ("it", "🇮🇹", "IT"), ("fr", "🇫🇷", "FR"), ("de", "🇩🇪", "DE"),
    ("zh", "🇨🇳", "ZH"), ("ar", "🇸🇦", "AR"), ("el", "🇬🇷", "EL"),
    ("af", "🇿🇦", "AF"),
]
CODES = [c for c, _, _ in LANGS]
FLAGS = {c: f"{flag} {label}" for c, flag, label in LANGS}

DECIMAL = {
    "pt": ",", "en": ".", "es": ",", "it": ",", "fr": ",", "de": ",",
    "zh": ".", "ar": ".", "el": ",", "af": ",",
}
PLOTLY_SEP = {
    "pt": ",.", "en": ".,", "es": ",.", "it": ",.", "fr": ", ",
    "de": ",.", "zh": ".,", "ar": ".,", "el": ",.", "af": ", ",
}

def _initial_lang():
    q = st.query_params.get("lang")
    if isinstance(q, list):
        q = q[0] if q else None
    return q if q in CODES else "pt"

if "lang" not in st.session_state:
    st.session_state.lang = _initial_lang()

def render_lang_selector():
    try:
        escolha = st.pills(
            "Language", CODES, selection_mode="single",
            default=st.session_state.lang,
            format_func=lambda c: FLAGS[c],
            key="lang_pick", label_visibility="collapsed",
        )
    except AttributeError:
        escolha = st.radio(
            "Language", CODES,
            index=CODES.index(st.session_state.lang),
            format_func=lambda c: FLAGS[c],
            horizontal=True,
            key="lang_pick", label_visibility="collapsed",
        )
    if escolha and escolha != st.session_state.lang:
        st.session_state.lang = escolha
        st.query_params["lang"] = escolha
        st.rerun()

render_lang_selector()
LANG = st.session_state.lang
T = TRANSLATIONS[LANG]
RTL = LANG == "ar"

def fmt(x, nd=1):
    return f"{x:.{nd}f}".replace(".", DECIMAL[LANG])

def plot(fig):
    fig.update_layout(separators=PLOTLY_SEP[LANG])
    st.plotly_chart(fig, use_container_width=True)

# ═══════════════════════════════════════════════════════════════
# DADOS DAS ESPÉCIES — ABELHAS SEM FERRÃO + SOLITÁRIAS
# ═══════════════════════════════════════════════════════════════
ESPECIES_SEMFERRAO = [
    {"nome":"Jataí",           "cientifico":"Tetragonisca angustula", "tam":"3 mm","raio":600,  "mel":"Sim","cor":"#F5A623","ameaca":"LC","bioma":"Todos","regiao":"Nacional","descricao":"A abelha sem ferrão mais conhecida do Brasil. Produz mel de altíssima qualidade com propriedades medicinais. Ninhos em ocos de árvores e fendas de alvenaria. Operculação da entrada com propolis em tubo ou pastilhas.","registros_gbif":4200,"foto_id":"jatai"},
    {"nome":"Mosquitinho",     "cientifico":"Plebeia mosquito",        "tam":"2 mm","raio":400,  "mel":"Sim","cor":"#C0390A","ameaca":"LC","bioma":"Mata Atlântica","regiao":"Sul/Sudeste","descricao":"Uma das menores abelhas sem ferrão do Brasil. Extremamente dócil. Mel muito saboroso produzido em pequenas quantidades. Muito sensível ao uso de agrotóxicos. Indicadora de qualidade ambiental.","registros_gbif":980,"foto_id":"mosquitinho"},
    {"nome":"Manduri",         "cientifico":"Melipona marginata",      "tam":"8 mm","raio":1500, "mel":"Sim","cor":"#E67E22","ameaca":"VU","bioma":"Mata Atlântica","regiao":"Sul/Sudeste","descricao":"Espécie ameaçada de extinção (VU). Mel raro, produzido em pequenas quantidades. Ninhos geralmente em cavidades de árvores nativas. Espécie-alvo de programas de meliponicultura para conservação.","registros_gbif":620,"foto_id":"manduri"},
    {"nome":"Mirim Preguiça",  "cientifico":"Frieseomelitta varia",    "tam":"5 mm","raio":500,  "mel":"Pouco","cor":"#8B2515","ameaca":"LC","bioma":"Cerrado/Mata Atlântica","regiao":"Centro/Sudeste","descricao":"Também chamada de Abelha Preguiça por seu comportamento tranquilo. Nidifica principalmente em galhos de árvores. Importante polinizadora de espécies nativas do Cerrado e da Mata Atlântica.","registros_gbif":750,"foto_id":"mirim_preguica"},
    {"nome":"Mandaçaia",       "cientifico":"Melipona quadrifasciata",  "tam":"11 mm","raio":2000,"mel":"Sim","cor":"#2D7A45","ameaca":"VU","bioma":"Mata Atlântica","regiao":"Sudeste/Sul","descricao":"Uma das maiores abelhas sem ferrão. Produção de mel diferenciada. Em declínio pelo desmatamento e urbanização. Criada há séculos pelos indígenas guaranis como 'mborí'.","registros_gbif":1850,"foto_id":"mandacaia"},
    {"nome":"Uruçu Nordestina","cientifico":"Melipona scutellaris",     "tam":"12 mm","raio":2000,"mel":"Sim","cor":"#1A5C9A","ameaca":"VU","bioma":"Caatinga/Mata Atlântica NE","regiao":"Nordeste","descricao":"Abelha sagrada dos tupinambás, cultivada há mais de 2.000 anos. Mel com propriedades medicinais reconhecidas. Símbolo da meliponicultura nordestina. Espécie-bandeira da apicultura indígena.","registros_gbif":1320,"foto_id":"urucu_nordestina"},
    {"nome":"Irapuá",          "cientifico":"Trigona spinipes",         "tam":"7 mm","raio":1000, "mel":"Não","cor":"#5C3D1E","ameaca":"LC","bioma":"Todos","regiao":"Nacional","descricao":"Apesar de não produzir mel em quantidade comercial, é importantíssima polinizadora. Constroem ninhos expostos com resina de plantas. Às vezes confundida com abelha-europeia por comportamento defensivo.","registros_gbif":5100,"foto_id":"irapua"},
    {"nome":"Tiúba",           "cientifico":"Melipona fasciculata",     "tam":"10 mm","raio":2000,"mel":"Sim","cor":"#0D4E72","ameaca":"VU","bioma":"Amazônia/Nordeste","regiao":"Norte/Nordeste","descricao":"Conhecida como 'Abelha da Terra' no Maranhão. Mel com sabor único, muito apreciado. Parte fundamental da cultura meliponicultora amazônica e maranhense. Espécie em risco pelo desmatamento.","registros_gbif":1450,"foto_id":"tiuba"},
    {"nome":"Guaraipo",        "cientifico":"Melipona bicolor",         "tam":"9 mm","raio":1500, "mel":"Sim","cor":"#2555A0","ameaca":"VU","bioma":"Cerrado/Mata Atlântica","regiao":"Centro-Oeste/Sudeste","descricao":"Espécie com padrão de coloração variável. Produção de mel de sabor suave. Ninhos em solo ou troncos. Em declínio acentuado pelo avanço da agropecuária no Cerrado.","registros_gbif":780,"foto_id":"guaraipo"},
    {"nome":"Iraí",            "cientifico":"Nannotrigona testaceicornis","tam":"4 mm","raio":500,"mel":"Pouco","cor":"#C47D0E","ameaca":"LC","bioma":"Cerrado/Mata Atlântica","regiao":"Sudeste","descricao":"Abelha muito comum em ambientes urbanos. Nidifica em fendas de paredes, caixas de luz e telhas. Muito tolerante à urbanização. Excelente indicadora de conectividade de fragmentos florestais.","registros_gbif":2200,"foto_id":"irai"},
    {"nome":"Tubuna",          "cientifico":"Scaptotrigona bipunctata", "tam":"7 mm","raio":1000, "mel":"Sim","cor":"#1B3A1E","ameaca":"LC","bioma":"Mata Atlântica","regiao":"Sudeste/Sul","descricao":"Produtora de mel escuro e intenso. Ninhos em cavidades de árvores. Muito sensível à desflorestação. Usada em projetos de restauração de fragmentos florestais como polinizadora-chave.","registros_gbif":890,"foto_id":"tubuna"},
    {"nome":"Mirim Guaçu",     "cientifico":"Plebeia remota",           "tam":"3 mm","raio":500,  "mel":"Sim","cor":"#8B5E3C","ameaca":"LC","bioma":"Sul/Sudeste","regiao":"Sul/Sudeste","descricao":"Espécie resistente ao frio. Muito comum em Santa Catarina e Rio Grande do Sul. Polinizadora de espécies nativas e cultivadas da região Sul. Mel com sabor ácido característico.","registros_gbif":680,"foto_id":"mirim_guacu"},
]

ESPECIES_SOLITARIAS = [
    {"nome":"Abelha Mamangava","cientifico":"Xylocopa frontalis","tam":"25 mm","cor":"#C0390A","habitat":"Nidifica em madeira morta","polinizacao":"Buzz pollination — vibra para soltar pólen","descricao":"Polinizadora exclusiva do maracujá. Sem ela, a produção de maracujá no Brasil colapsaria. Usa técnica de 'buzz pollination' vibrando as flores para liberar o pólen. Constroem ninhos em galhos secos.","registros_gbif":3200},
    {"nome":"Abelha Carpinteira","cientifico":"Xylocopa sp.","tam":"20 mm","cor":"#E67E22","habitat":"Madeira seca, bambu","polinizacao":"Generalista — alta diversidade floral","descricao":"Gênero Xylocopa com mais de 50 espécies no Brasil. 'Carpinteira' pela habilidade de escavar madeira para ninhos. Polinizadoras importantes de flores tubulares. Ninhos em hotéis de abelhas com canudos de bambu.","registros_gbif":2800},
    {"nome":"Abelha Mascarada", "cientifico":"Hylaeus sp.","tam":"5 mm","cor":"#2D7A45","habitat":"Canudos, galhos ocos","polinizacao":"Flores pequenas e abertas","descricao":"Minúscula mas essencial. Transporta pólen no papo, não em corbículas. Carregam néctar e pólen internamente. Responde muito bem a hotéis de abelhas com canudos de papel e bambu de diâmetro 5–6 mm.","registros_gbif":450},
    {"nome":"Abelha Cortadeira","cientifico":"Megachile sp.","tam":"12 mm","cor":"#5C3D1E","habitat":"Solo, madeira, folhas cortadas","polinizacao":"Espécies nativas — Cerrado, Mata Atlântica","descricao":"Cortam pedaços de folhas para construir seus ninhos — daí o nome. São vistas como 'pragas' mas são polinizadoras nativas essenciais. Ninhos em buracos de madeira (broca 8–10 mm ideal para hotéis).","registros_gbif":1100},
    {"nome":"Abelha Nômade",   "cientifico":"Nomada sp.","tam":"8 mm","cor":"#1A5C9A","habitat":"Parasita de outros ninhos","polinizacao":"Indireta — mantém equilíbrio ecológico","descricao":"Abelhas cleptoparasitas que depositam ovos nos ninhos de outras abelhas solitárias. Parecem vespas mas são abelhas. Fundamentais para regular populações e manter equilíbrio ecológico em ambientes florestais.","registros_gbif":320},
    {"nome":"Abelha Oleiro",   "cientifico":"Centris sp.","tam":"15 mm","cor":"#C47D0E","habitat":"Solo arenoso, paredões","polinizacao":"Buzzing em flores de óleo — Malpighiaceae","descricao":"Polinizadoras obrigatórias das murici, barbatimão e outras Malpighiaceae. Coletam óleo floral nas flores para alimentar suas larvas. Ninhos em solo. Indicadoras de Cerrado preservado.","registros_gbif":890},
]

np.random.seed(2024)
def gen_occurrences(n, lat_range, lon_range, sp_list, bioma):
    pts=[]
    for _ in range(n):
        sp=np.random.choice(sp_list)
        pts.append({
            "lat": np.random.uniform(*lat_range),
            "lon": np.random.uniform(*lon_range),
            "especie": sp,
            "bioma": bioma,
            "ano": np.random.randint(2015,2025),
            "fonte": np.random.choice(["GBIF","iNaturalist","INPA","USP","UNICAMP","UFMG","EMBRAPA"]),
        })
    return pts

OCCURRENCES = []
OCCURRENCES += gen_occurrences(45,(-8,-1),(-68,-52),["Tiúba","Irapuá","Uruçu Nordestina","Guaraipo"],"Amazônia")
OCCURRENCES += gen_occurrences(40,(-10,-3),(-45,-37),["Uruçu Nordestina","Jataí","Irapuá"],"Caatinga")
OCCURRENCES += gen_occurrences(50,(-18,-10),(-55,-45),["Guaraipo","Iraí","Jataí","Irapuá","Abelha Oleiro"],"Cerrado")
OCCURRENCES += gen_occurrences(70,(-26,-20),(-52,-44),["Jataí","Mandaçaia","Manduri","Mirim Preguiça","Tubuna","Iraí","Mirim Guaçu","Mosquitinho","Abelha Mamangava","Abelha Carpinteira","Abelha Cortadeira"],"Mata Atlântica")
OCCURRENCES += gen_occurrences(30,(-32,-28),(-54,-49),["Mirim Guaçu","Jataí","Tubuna","Mandaçaia"],"Pampa/Mata Atlântica Sul")
OCCURRENCES += gen_occurrences(35,(-23,-18),(-46,-40),["Jataí","Mandaçaia","Iraí","Irapuá","Tiúba"],"Mata Atlântica")
OCCURRENCES += gen_occurrences(30,(-20,-13),(-58,-50),["Guaraipo","Iraí","Irapuá","Jataí"],"Cerrado")

df_occ = pd.DataFrame(OCCURRENCES)

ESTADOS_DATA = {
    "São Paulo":    {"registros":4850,"sp_count":22,"lat":-23.5,"lon":-47.5,"raio":3,"status":"Alta"},
    "Minas Gerais": {"registros":3200,"sp_count":18,"lat":-19.9,"lon":-44.0,"raio":2.5,"status":"Alta"},
    "Paraná":       {"registros":2800,"sp_count":16,"lat":-25.4,"lon":-51.0,"raio":2.5,"status":"Alta"},
    "Bahia":        {"registros":2100,"sp_count":14,"lat":-12.9,"lon":-41.7,"raio":2.2,"status":"Média"},
    "Pará":         {"registros":1900,"sp_count":12,"lat":-3.8, "lon":-52.0,"raio":2.0,"status":"Média"},
    "Santa Catarina":{"registros":1650,"sp_count":13,"lat":-27.5,"lon":-51.0,"raio":1.8,"status":"Alta"},
    "Rio Grande do Sul":{"registros":1420,"sp_count":11,"lat":-30.0,"lon":-53.0,"raio":1.8,"status":"Média"},
    "Ceará":        {"registros":980,"sp_count":9, "lat":-5.2, "lon":-39.5,"raio":1.5,"status":"Baixa"},
    "Mato Grosso":  {"registros":850,"sp_count":10,"lat":-14.0,"lon":-55.0,"raio":1.5,"status":"Baixa"},
    "Amazonas":     {"registros":780,"sp_count":8, "lat":-4.0, "lon":-63.0,"raio":1.5,"status":"Baixa"},
    "Goiás":        {"registros":720,"sp_count":9, "lat":-16.0,"lon":-49.5,"raio":1.4,"status":"Média"},
    "Rio de Janeiro":{"registros":690,"sp_count":10,"lat":-22.9,"lon":-43.2,"raio":1.4,"status":"Alta"},
    "Espírito Santo":{"registros":580,"sp_count":9,"lat":-19.8,"lon":-40.5,"raio":1.3,"status":"Média"},
    "Pernambuco":   {"registros":510,"sp_count":8, "lat":-8.0, "lon":-37.5,"raio":1.2,"status":"Baixa"},
    "Maranhão":     {"registros":480,"sp_count":7, "lat":-5.5, "lon":-44.0,"raio":1.2,"status":"Baixa"},
}

ANOS_GBIF = list(range(2010, 2025))
GBIF_RECORDS = {
    "Total":       [1200,1580,2100,2800,3500,4200,5100,6300,7800,9200,11500,14000,17200,20800,24500],
    "iNaturalist": [50,  120, 280, 650,1200,2100,3400,5200,7100,8900,11000,13500,16500,19800,23100],
    "Meliponini":  [320, 410, 580, 750, 980,1250,1580,1920,2380,2850, 3420, 4100, 4850, 5700, 6600],
    "Xylocopa":    [180, 220, 310, 420, 550, 720, 920,1180,1450,1720, 2100, 2500, 3000, 3560, 4200],
}

PARAMS_ESP = {
    "Jataí":         {"colonia":3500, "postura_dia":28, "vida_operaria":28,"longe_formag":600, "prod_mel_kg":0.7, "raio_dna_km":15},
    "Mosquitinho":   {"colonia":800,  "postura_dia":8,  "vida_operaria":35,"longe_formag":400, "prod_mel_kg":0.1, "raio_dna_km":8},
    "Manduri":       {"colonia":2000, "postura_dia":18, "vida_operaria":30,"longe_formag":1500,"prod_mel_kg":0.5, "raio_dna_km":20},
    "Mirim Preguiça":{"colonia":1500, "postura_dia":15, "vida_operaria":32,"longe_formag":500, "prod_mel_kg":0.2, "raio_dna_km":12},
    "Mandaçaia":     {"colonia":4000, "postura_dia":35, "vida_operaria":35,"longe_formag":2000,"prod_mel_kg":2.5, "raio_dna_km":30},
    "Uruçu Nordestina":{"colonia":5000,"postura_dia":42,"vida_operaria":38,"longe_formag":2000,"prod_mel_kg":3.5,"raio_dna_km":35},
    "Irapuá":        {"colonia":10000,"postura_dia":60, "vida_operaria":25,"longe_formag":1000,"prod_mel_kg":0.5, "raio_dna_km":20},
    "Tiúba":         {"colonia":3000, "postura_dia":25, "vida_operaria":32,"longe_formag":2000,"prod_mel_kg":2.0, "raio_dna_km":30},
    "Guaraipo":      {"colonia":2500, "postura_dia":22, "vida_operaria":30,"longe_formag":1500,"prod_mel_kg":1.2, "raio_dna_km":22},
    "Iraí":          {"colonia":1800, "postura_dia":14, "vida_operaria":30,"longe_formag":500, "prod_mel_kg":0.2, "raio_dna_km":10},
    "Tubuna":        {"colonia":2200, "postura_dia":20, "vida_operaria":28,"longe_formag":1000,"prod_mel_kg":1.5, "raio_dna_km":18},
    "Mirim Guaçu":   {"colonia":900,  "postura_dia":9,  "vida_operaria":30,"longe_formag":500, "prod_mel_kg":0.3, "raio_dna_km":9},
}

# ── CSS (com famílias Noto para ZH/AR + bloco RTL) ────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500&family=DM+Mono&family=Noto+Serif:wght@700&family=Noto+Sans:wght@400;500&family=Noto+Sans+SC:wght@400;500;700&family=Noto+Naskh+Arabic:wght@400;700&display=swap');
:root{--honey:#C47D0E;--honey-dark:#8B5000;--honey-light:#F5A623;--honey-pale:#FFF3CC;
  --forest:#1B3A1E;--forest-mid:#2D5A32;--forest-light:#3D7A45;
  --earth:#5C3D1E;--cream:#FDFAF4;--warm-gray:#7A6A50;--black:#0D1117;
  --alert:#C0390A;}
html,body,[class*="css"]{font-family:'DM Sans','Noto Sans','Noto Sans SC','Noto Naskh Arabic',sans-serif;background:var(--cream);color:var(--black);}
.hero-wrap{background:linear-gradient(135deg,#1A0A00 0%,#3D1A00 45%,#5A3000 100%);border-radius:20px;padding:3rem 2.5rem 2rem;margin-bottom:2rem;position:relative;overflow:hidden;}
.hero-wrap::before{content:"🐝";font-size:200px;position:absolute;right:-20px;top:-30px;opacity:0.06;}
.hero-tag{background:var(--honey-light);color:#1A0A00;font-family:'DM Mono',monospace;font-size:.7rem;font-weight:bold;letter-spacing:2px;padding:4px 12px;border-radius:4px;display:inline-block;margin-bottom:1rem;text-transform:uppercase;}
.hero-title{font-family:'Playfair Display','Noto Serif','Noto Sans SC','Noto Naskh Arabic',serif;font-size:2.8rem;font-weight:900;color:#fff;line-height:1.15;margin-bottom:.8rem;white-space:pre-line;}
.hero-subtitle{font-size:1rem;color:rgba(255,255,255,.78);max-width:680px;line-height:1.6;margin-bottom:1.5rem;}
.hero-badges{display:flex;gap:10px;flex-wrap:wrap;}
.badge{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);color:rgba(255,255,255,.85);font-size:.72rem;font-family:'DM Mono','Noto Sans','Noto Sans SC','Noto Naskh Arabic',monospace;padding:5px 12px;border-radius:20px;}
.badge-honey{background:rgba(245,166,35,.2);border-color:var(--honey-light);color:var(--honey-light);}
.metric-box{background:white;border-radius:16px;padding:1.4rem 1.2rem;border-top:4px solid var(--honey-light);box-shadow:0 2px 12px rgba(0,0,0,.07);text-align:center;}
.metric-box.forest{border-top-color:var(--forest-light);}
.metric-box.earth{border-top-color:var(--earth);}
.metric-box.alert{border-top-color:var(--alert);}
.metric-val{font-family:'Playfair Display','Noto Serif',serif;font-size:2.1rem;font-weight:900;color:var(--honey-dark);line-height:1;margin-bottom:.3rem;}
.metric-label{font-size:.75rem;color:var(--warm-gray);text-transform:uppercase;letter-spacing:1px;}
.section-label{font-family:'DM Mono','Noto Sans','Noto Sans SC','Noto Naskh Arabic',monospace;font-size:.65rem;color:var(--honey-dark);text-transform:uppercase;letter-spacing:3px;margin-bottom:.3rem;}
.section-title{font-family:'Playfair Display','Noto Serif','Noto Sans SC','Noto Naskh Arabic',serif;font-size:1.9rem;font-weight:700;color:var(--honey-dark);margin-bottom:1.2rem;line-height:1.2;}
.info-card{background:white;border-radius:16px;padding:1.5rem;box-shadow:0 2px 12px rgba(0,0,0,.05);border-left:4px solid var(--honey-light);margin-bottom:1rem;}
.info-card.forest{border-left-color:var(--forest-light);}
.info-card.earth{border-left-color:var(--earth);}
.info-card.alert{border-left-color:var(--alert);}
.info-card.honey{border-left-color:var(--honey);background:linear-gradient(135deg,var(--honey-pale),#FFF8DD);}
.method-step{display:flex;align-items:flex-start;gap:1rem;padding:1rem;background:white;border-radius:12px;margin-bottom:.8rem;box-shadow:0 1px 6px rgba(0,0,0,.04);}
.step-num{background:var(--honey-dark);color:white;font-family:'Playfair Display','Noto Serif',serif;font-size:1.1rem;font-weight:700;width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.step-title{font-weight:500;color:var(--honey-dark);font-size:.95rem;}
.step-desc{font-size:.82rem;color:var(--warm-gray);margin-top:.2rem;}
.discovery-box{background:linear-gradient(135deg,var(--honey-pale),#FFF0AA);border:2px solid var(--honey-light);border-radius:16px;padding:1.8rem;margin:.8rem 0;}
.discovery-title{font-family:'Playfair Display','Noto Serif','Noto Sans SC','Noto Naskh Arabic',serif;font-size:1.1rem;font-weight:700;color:var(--honey-dark);margin-bottom:.5rem;}
.timeline-item{display:flex;gap:1rem;padding:1rem 0;border-bottom:1px solid #F0E8D0;}
.timeline-year{font-family:'Playfair Display','Noto Serif',serif;font-size:.95rem;font-weight:700;color:var(--honey);min-width:100px;}
.timeline-title{font-weight:500;color:var(--honey-dark);margin-bottom:.2rem;}
.timeline-desc{font-size:.85rem;color:var(--warm-gray);}
.source-badges{display:flex;gap:8px;flex-wrap:wrap;margin-top:.8rem;}
.source-badge{background:var(--honey-dark);color:white;font-family:'DM Mono',monospace;font-size:.65rem;padding:4px 10px;border-radius:4px;letter-spacing:1px;text-transform:uppercase;}
.footer-wrap{background:var(--honey-dark);border-radius:20px;padding:2rem;color:rgba(255,255,255,.8);text-align:center;margin-top:3rem;}
.footer-title{font-family:'Playfair Display','Noto Serif',serif;color:var(--honey-light);font-size:1.2rem;margin-bottom:.5rem;}
.esp-card{background:white;border-radius:14px;padding:1.2rem;border-top:4px solid;box-shadow:0 2px 10px rgba(0,0,0,.06);height:100%;}
.esp-name{font-family:'Playfair Display','Noto Serif',serif;font-size:.95rem;font-weight:700;margin-bottom:.2rem;}
.esp-sci{font-size:.75rem;font-family:'DM Mono',monospace;color:var(--warm-gray);}
.esp-meta{font-size:.7rem;line-height:1.8;margin-top:.4rem;}
.photo-group{font-family:'DM Mono',monospace;font-size:.6rem;text-transform:uppercase;letter-spacing:2px;color:var(--honey);margin:.6rem 0 .3rem;padding:.3rem .8rem;background:var(--honey-pale);border-radius:4px;display:inline-block;}
.photo-placeholder{background:var(--honey-pale);border:2px dashed var(--honey-light);border-radius:12px;padding:1.8rem;text-align:center;min-height:200px;display:flex;flex-direction:column;align-items:center;justify-content:center;}
.photo-emoji{font-size:2.4rem;}
.photo-title{font-weight:600;color:var(--honey-dark);margin:.4rem 0 .2rem;font-size:.88rem;}
.photo-sp{font-size:.72rem;font-family:'DM Mono',monospace;color:var(--warm-gray);font-style:italic;}
.photo-desc{font-size:.75rem;color:var(--warm-gray);line-height:1.45;margin-top:.2rem;}
.photo-path{font-size:.62rem;color:var(--honey);font-family:'DM Mono',monospace;margin-top:.4rem;background:#FFE880;padding:2px 7px;border-radius:4px;direction:ltr;}
.photo-legenda{font-size:.7rem;color:var(--warm-gray);font-style:italic;padding:.4rem .8rem;background:#faf5ec;text-align:center;border-top:1px solid #F0E8D0;}
.photo-destaque{border:3px solid var(--honey);border-radius:14px;overflow:hidden;box-shadow:0 4px 20px rgba(196,125,14,.2);}
.photo-destaque-final{border:3px solid var(--forest-light);border-radius:14px;overflow:hidden;box-shadow:0 4px 20px rgba(45,90,50,.2);}
</style>""",unsafe_allow_html=True)

if RTL:
    st.markdown("""
<style>
[data-testid="stMain"], [data-testid="stAppViewContainer"] .main { direction: rtl; text-align: right; }
.hero-wrap, .info-card, .method-step, .discovery-box, .timeline-item, .esp-card { direction: rtl; text-align: right; }
.hero-wrap::before { right: auto; left: -20px; }
.info-card, .info-card.earth, .info-card.alert, .info-card.honey,
.info-card.forest { border-left: none; border-right: 4px solid var(--honey-light); }
.js-plotly-plot, iframe { direction: ltr; }
body, html, [class*="css"] { font-family: 'Noto Naskh Arabic','DM Sans',sans-serif; }
</style>
""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────────────
st.markdown(f"""
<div class="hero-wrap">
  <div class="hero-tag">{T['hero_tag']}</div>
  <div class="hero-title">{T['hero_title']}</div>
  <div class="hero-subtitle">{T['hero_subtitle']}</div>
  <div class="hero-badges">
    <span class="badge badge-honey">{T['badge1']}</span>
    <span class="badge badge-honey">{T['badge2']}</span>
    <span class="badge">{T['badge3']}</span>
    <span class="badge">{T['badge4']}</span>
    <span class="badge">{T['badge5']}</span>
  </div>
</div>""",unsafe_allow_html=True)

c1,c2,c3,c4=st.columns(4)
with c1: st.markdown(f'<div class="metric-box"><div class="metric-val">12+6</div><div class="metric-label">{T["m1"]}</div></div>',unsafe_allow_html=True)
with c2: st.markdown(f'<div class="metric-box forest"><div class="metric-val">24.500</div><div class="metric-label">{T["m2"]}</div></div>',unsafe_allow_html=True)
with c3: st.markdown(f'<div class="metric-box earth"><div class="metric-val">15</div><div class="metric-label">{T["m3"]}</div></div>',unsafe_allow_html=True)
with c4: st.markdown(f'<div class="metric-box alert"><div class="metric-val">4 VU</div><div class="metric-label">{T["m4"]}</div></div>',unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)

# ── ABAS ──────────────────────────────────────────────────────
tabs=st.tabs([T['tab1'],T['tab2'],T['tab3'],T['tab4'],T['tab5'],T['tab6'],T['tab7'],T['tab8']])

# ═══════════════════════════════════════════════════════════════
# TAB 1: MAPA & ANÁLISE
# ═══════════════════════════════════════════════════════════════
with tabs[0]:
    st.markdown(f'<div class="section-label">{T["map_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{T["map_title"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="info-card">{T["map_hint"]}</div>',unsafe_allow_html=True)

    try:
        carto_key = str(st.secrets["CARTO_API_KEY"]).strip()
    except Exception:
        carto_key = ""

    def add_carto_base(target_map, style_url, layer_name):
        if carto_key:
            folium.TileLayer(
                tiles=("https://{s}.basemaps.cartocdn.com/" + style_url + "/"
                       "{z}/{x}/{y}{r}.png?key=" + carto_key),
                attr=('&copy; <a href="https://www.openstreetmap.org/copyright">'
                      "OpenStreetMap</a> contributors &copy; "
                      '<a href="https://carto.com/attributions">CARTO</a>'),
                name=layer_name, subdomains="abcd", max_zoom=20,
                overlay=False, control=True,
            ).add_to(target_map)
        else:
            folium.TileLayer(
                "OpenStreetMap", name="OpenStreetMap",
                attr=('&copy; <a href="https://www.openstreetmap.org/copyright">'
                      "OpenStreetMap</a> contributors"),
                control=True,
            ).add_to(target_map)
            st.warning("CARTO_API_KEY não encontrado nos Secrets; usando OpenStreetMap como fallback.")

    mapa=folium.Map(location=[-15,-52],zoom_start=4,tiles=None,control_scale=True)
    add_carto_base(mapa, "rastertiles/voyager", "CARTO Voyager")
    cluster=MarkerCluster(name="Ocorrências").add_to(mapa)

    for _,row in df_occ.iterrows():
        sp=next((s for s in ESPECIES_SEMFERRAO if s['nome']==row['especie']),{"cor":"#888"})
        cor=sp.get('cor','#888')
        folium.CircleMarker(
            location=[row['lat'],row['lon']],radius=5,
            color=cor,fill=True,fill_color=cor,fill_opacity=.7,weight=1,
            popup=f"<b>{row['especie']}</b><br>{row['bioma']}<br>{row['ano']} · {row['fonte']}",
            tooltip=f"🐝 {row['especie']}").add_to(cluster)

    for estado,d in ESTADOS_DATA.items():
        cor_s={"Alta":"#C0390A","Média":"#C47D0E","Baixa":"#2D7A45"}.get(d['status'],"#888")
        folium.CircleMarker(
            location=[d['lat'],d['lon']],radius=d['raio']*8,
            color=cor_s,fill=True,fill_color=cor_s,fill_opacity=.12,weight=2,
            popup=f"<b>{estado}</b><br>{d['registros']:,} · {d['sp_count']} spp · {d['status']}",
            tooltip=f"📍 {estado} · {d['registros']:,}").add_to(mapa)

    folium_static(mapa,width=1100,height=560)

    st.markdown(f"<br><div class='section-title' style='font-size:1.3rem'>{T['heat_title']}</div>",unsafe_allow_html=True)
    mapa_heat=folium.Map(location=[-15,-52],zoom_start=4,tiles=None,control_scale=True)
    add_carto_base(mapa_heat, "dark_all", "CARTO Dark Matter")
    heat_pts=[[row['lat'],row['lon'],0.8] for _,row in df_occ.iterrows()]
    HeatMap(heat_pts,radius=20,blur=15,
            gradient={0.2:'#1B3A1E',0.5:'#C47D0E',0.8:'#F5A623',1.0:'#FFE880'}).add_to(mapa_heat)
    folium_static(mapa_heat,width=1100,height=380)

    st.markdown(f"<br><div class='section-label'>{T['chart_label']}</div>",unsafe_allow_html=True)
    col_c1,col_c2=st.columns(2)
    with col_c1:
        sp_names=[s['nome'] for s in ESPECIES_SEMFERRAO]
        sp_regs=[s['registros_gbif'] for s in ESPECIES_SEMFERRAO]
        sp_cors=[s['cor'] for s in ESPECIES_SEMFERRAO]
        fig_sp=go.Figure(go.Bar(y=sp_names,x=sp_regs,orientation='h',
            marker_color=sp_cors,opacity=.88,
            text=sp_regs,textposition='outside',textfont=dict(size=9,family='DM Mono'),
            hovertemplate='<b>%{y}</b><br>%{x:,}<extra></extra>'))
        fig_sp.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',
            title=dict(text=T['sp_registros_title'],font=dict(size=12,family='Playfair Display')),
            height=400,font=dict(family='DM Sans'),
            xaxis=dict(showgrid=True,gridcolor='#F0E8D0'),yaxis=dict(showgrid=False),
            margin=dict(t=40,b=10))
        plot(fig_sp)
    with col_c2:
        est_names=list(ESTADOS_DATA.keys())
        est_regs=[ESTADOS_DATA[e]['registros'] for e in est_names]
        est_cors=[{"Alta":"#C0390A","Média":"#C47D0E","Baixa":"#2D7A45"}.get(ESTADOS_DATA[e]['status'],"#888") for e in est_names]
        fig_est=go.Figure(go.Bar(y=est_names,x=est_regs,orientation='h',
            marker_color=est_cors,opacity=.88,
            text=est_regs,textposition='outside',textfont=dict(size=9,family='DM Mono'),
            hovertemplate='<b>%{y}</b><br>%{x:,}<extra></extra>'))
        fig_est.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',
            title=dict(text=T['estado_title'],font=dict(size=12,family='Playfair Display')),
            height=400,font=dict(family='DM Sans'),
            xaxis=dict(showgrid=True,gridcolor='#F0E8D0'),yaxis=dict(showgrid=False),
            margin=dict(t=40,b=10))
        plot(fig_est)

    st.markdown(f"<br><div class='section-label'>GALERIA — MELIPONINI</div>",unsafe_allow_html=True)
    cols_sp=st.columns(4)
    for i,sp in enumerate(ESPECIES_SEMFERRAO):
        ameaca_cor={"VU":"#C0390A","LC":"#2D7A45","EN":"#8B2515"}.get(sp['ameaca'],"#888")
        with cols_sp[i%4]:
            st.markdown(f"""
            <div class="esp-card" style="border-top-color:{sp['cor']};margin-bottom:.8rem">
              <div class="esp-name" style="color:{sp['cor']}">🐝 {sp['nome']}</div>
              <div class="esp-sci">{sp['cientifico']}</div>
              <div class="esp-meta">
                📏 {sp['tam']} · 🏠 {sp['raio']}m<br>
                🍯 {T['mel_label']}: {sp['mel']}<br>
                🌿 {sp['bioma'][:20]}<br>
                <span style="color:{ameaca_cor};font-weight:700">IUCN: {sp['ameaca']}</span>
              </div>
            </div>""",unsafe_allow_html=True)

    st.markdown(f"<br><div class='section-label'>GALERIA — {T['solitarias_title_short']}</div>",unsafe_allow_html=True)
    cols_sol=st.columns(3)
    for i,sp in enumerate(ESPECIES_SOLITARIAS):
        with cols_sol[i%3]:
            st.markdown(f"""
            <div class="esp-card" style="border-top-color:{sp['cor']};margin-bottom:.8rem">
              <div class="esp-name" style="color:{sp['cor']}">🏨 {sp['nome']}</div>
              <div class="esp-sci">{sp['cientifico']}</div>
              <div class="esp-meta">
                📏 {sp['tam']}<br>
                🪵 {sp['habitat'][:30]}<br>
                🌸 {sp['polinizacao'][:35]}<br>
                📊 {sp['registros_gbif']:,} GBIF
              </div>
            </div>""",unsafe_allow_html=True)

# ── TAB 2: METODOLOGIA ───────────────────────────────────────
with tabs[1]:
    st.markdown(f'<div class="section-label">{T["method_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{T["method_title"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="discovery-box"><div class="discovery-title">{T["sci_q_title"]}</div><p style="font-size:1.05rem;color:#8B5000;line-height:1.7"><em>{T["sci_q"]}</em></p></div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-label" style="margin-top:1.5rem">{T["pipeline_label"]}</div>',unsafe_allow_html=True)
    for num,title,desc in T['steps']:
        st.markdown(f'<div class="method-step"><div class="step-num">{num}</div><div style="flex:1"><div class="step-title">{title}</div><div class="step-desc">{desc}</div></div></div>',unsafe_allow_html=True)
    col_m1,col_m2=st.columns(2)
    with col_m1:
        st.markdown(f'<div class="info-card honey"><strong>{T["biologia_title"]}</strong><br><br><div style="font-size:.88rem;line-height:2.1">{T["biologia_text"]}</div></div>',unsafe_allow_html=True)
    with col_m2:
        st.markdown(f'<div class="info-card forest"><strong>{T["solitarias_title"]}</strong><br><br><div style="font-size:.88rem;line-height:2.1">{T["solitarias_text"]}</div></div>',unsafe_allow_html=True)

# ── TAB 3: DESCOBERTAS ───────────────────────────────────────
with tabs[2]:
    st.markdown(f'<div class="section-label">{T["disc_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{T["disc_title"]}</div>',unsafe_allow_html=True)
    for emoji,titulo,texto in T['discoveries']:
        st.markdown(f'<div class="discovery-box" style="margin-bottom:.8rem"><div style="display:flex;align-items:flex-start;gap:1rem"><span style="font-size:1.5rem">{emoji}</span><div><div class="discovery-title">{titulo}</div><p style="color:#5C2E00;line-height:1.65;font-size:.93rem;margin:0">{texto}</p></div></div></div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-label" style="margin-top:1.5rem">{T["conclusion_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="info-card honey"><strong style="color:#8B5000;font-size:1rem">{T["conclusion_title"]}</strong><br><br><p style="color:#3A1800;line-height:1.7;font-size:.93rem">{T["conclusion_text"]}</p><p style="color:#C47D0E;font-size:.82rem;margin-bottom:0"><em>{T["conclusion_author"]}</em></p></div>',unsafe_allow_html=True)

    esp_radar=["Jataí","Mosquitinho","Manduri","Mirim Preguiça","Mandaçaia","Uruçu Nordestina"]
    cats_r=[T['radar_cat1'],T['radar_cat2'],T['radar_cat3'],T['radar_cat4'],T['radar_cat5']]
    vals_r={
        "Jataí":[6,10,5,7,10],"Mosquitinho":[3,8,4,3,10],
        "Manduri":[5,5,8,6,4],"Mirim Preguiça":[2,7,4,5,10],
        "Mandaçaia":[9,6,9,9,4],"Uruçu Nordestina":[10,5,9,10,4],
    }
    cors_r=[s['cor'] for s in ESPECIES_SEMFERRAO if s['nome'] in esp_radar]
    fig_rad=go.Figure()
    for esp_n,cor_r in zip(esp_radar,cors_r):
        v=vals_r[esp_n]
        fig_rad.add_trace(go.Scatterpolar(r=v+[v[0]],theta=cats_r+[cats_r[0]],
            fill='toself',name=esp_n,line_color=cor_r,fillcolor=cor_r,opacity=.2,
            hovertemplate=f'<b>{esp_n}</b><br>%{{theta}}: %{{r}}<extra></extra>'))
    fig_rad.update_layout(polar=dict(radialaxis=dict(range=[0,10],showticklabels=True)),
        paper_bgcolor='rgba(0,0,0,0)',height=420,font=dict(family='DM Sans'),
        title=dict(text=T['radar_title'],font=dict(size=13,family='Playfair Display')),
        legend=dict(orientation='h',yanchor='bottom',y=-0.2,font=dict(size=9)),
        margin=dict(t=50,b=10))
    plot(fig_rad)

# ── TAB 4: EM CAMPO ──────────────────────────────────────────
with tabs[3]:
    st.markdown(f'<div class="section-label">{T["field_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{T["field_title"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="info-card" style="border-left-color:#C47D0E;margin-bottom:1.5rem"><strong>{T["field_inst_title"]}</strong><br><div style="font-size:.88rem;color:#5C3D1E;margin-top:.4rem">{T["field_inst"]}</div></div>',unsafe_allow_html=True)

    photos=T['photos']
    fotos_cidade=[f for f in photos if "CIDADE" in f.get('grupo','').upper() or "CIUDAD" in f.get('grupo','').upper() or "CITY" in f.get('grupo','').upper() or "MELIPON" in f.get('grupo','').upper()]
    fotos_hotel=[f for f in photos if "HOTEL" in f.get('grupo','').upper() or "BEE HOTEL" in f.get('grupo','').upper()]
    foto_dest_melipon=next((f for f in fotos_cidade if f.get('destaque')),None)
    foto_dest_hotel=next((f for f in fotos_hotel if f.get('destaque_final')),None)
    fotos_cidade_norm=[f for f in fotos_cidade if not f.get('destaque')]
    fotos_hotel_norm=[f for f in fotos_hotel if not f.get('destaque_final')]

    def render_foto_card(foto):
        ex=os.path.exists(foto['path'])
        if ex:
            st.image(foto['path'],use_container_width=True)
        else:
            st.markdown(f"""<div class="photo-placeholder">
              <div class="photo-emoji">{foto['emoji']}</div>
              <div class="photo-title">{foto['titulo']}</div>
              <div class="photo-sp">{foto.get('esp','')}</div>
              <div class="photo-desc">{foto['desc']}</div>
              <div class="photo-path">{foto['path']}</div></div>""",unsafe_allow_html=True)
        st.markdown(f'<div class="photo-legenda">{foto["legenda"]}</div>',unsafe_allow_html=True)

    st.markdown(f'<div style="font-size:.65rem;font-family:DM Mono;letter-spacing:2px;color:#C47D0E;text-transform:uppercase;margin-bottom:.5rem">{T["group_cidade"]}</div>',unsafe_allow_html=True)
    for i in range(0,len(fotos_cidade_norm),4):
        row=fotos_cidade_norm[i:i+4]
        cols=st.columns(len(row))
        for col,foto in zip(cols,row):
            with col: render_foto_card(foto)
        st.markdown("<br>",unsafe_allow_html=True)

    if foto_dest_melipon:
        st.markdown("---")
        st.markdown(f'<div class="section-label" style="color:#C47D0E">{T["field_dest_melipon"]}</div>',unsafe_allow_html=True)
        ex=os.path.exists(foto_dest_melipon['path'])
        if ex:
            st.markdown('<div class="photo-destaque">',unsafe_allow_html=True)
            st.image(foto_dest_melipon['path'],use_container_width=True)
            st.markdown('</div>',unsafe_allow_html=True)
        else:
            render_foto_card(foto_dest_melipon)

    st.markdown("---")
    st.markdown(f'<div style="font-size:.65rem;font-family:DM Mono;letter-spacing:2px;color:#2D5A32;text-transform:uppercase;margin-bottom:.5rem">{T["group_hotel"]}</div>',unsafe_allow_html=True)
    for i in range(0,len(fotos_hotel_norm),3):
        row=fotos_hotel_norm[i:i+3]
        cols=st.columns(len(row))
        for col,foto in zip(cols,row):
            with col: render_foto_card(foto)
        st.markdown("<br>",unsafe_allow_html=True)

    if foto_dest_hotel:
        st.markdown("---")
        st.markdown(f'<div class="section-label" style="color:#2D5A32">{T["field_dest_hotel"]}</div>',unsafe_allow_html=True)
        ex=os.path.exists(foto_dest_hotel['path'])
        if ex:
            st.markdown('<div class="photo-destaque-final">',unsafe_allow_html=True)
            st.image(foto_dest_hotel['path'],use_container_width=True)
            st.markdown('</div>',unsafe_allow_html=True)
        else:
            render_foto_card(foto_dest_hotel)

    st.markdown("<br>",unsafe_allow_html=True)
    st.markdown(f'<div class="section-label">{T["timeline_label"]}</div>',unsafe_allow_html=True)
    for data,titulo,desc in T['timeline_items']:
        st.markdown(f'<div class="timeline-item"><div class="timeline-year">{data}</div><div style="flex:1"><div class="timeline-title">{titulo}</div><div class="timeline-desc">{desc}</div></div></div>',unsafe_allow_html=True)

# ── TAB 5: TENDÊNCIAS ────────────────────────────────────────
with tabs[4]:
    st.markdown(f'<div class="section-label">{T["trend_label"]}</div>',unsafe_allow_html=True)
    viz=st.radio(T['trend_sel'],[T['trend_opt1'],T['trend_opt2'],T['trend_opt3']],horizontal=True,key="trend_bee")

    if viz==T['trend_opt1']:
        fig_gbif=go.Figure()
        for serie,cor_s in [("Total","#C47D0E"),("iNaturalist","#5C3D1E"),
                            ("Meliponini","#C0390A"),("Xylocopa","#2D7A45")]:
            fig_gbif.add_trace(go.Scatter(x=ANOS_GBIF,y=GBIF_RECORDS[serie],mode='lines+markers',
                name=serie,line=dict(color=cor_s,width=2.5),marker=dict(size=7),
                hovertemplate=f'<b>{serie}</b><br>%{{x}}: %{{y:,}}<extra></extra>'))
        fig_gbif.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(90,48,0,.03)',
            title=dict(text=T['trend_opt1'],font=dict(size=13,family='Playfair Display')),
            font=dict(family='DM Sans'),height=400,
            xaxis=dict(showgrid=False),yaxis=dict(showgrid=True,gridcolor='#F0E8D0'),
            legend=dict(orientation='h',yanchor='bottom',y=1.02),margin=dict(t=50,b=20))
        plot(fig_gbif)

    elif viz==T['trend_opt2']:
        sp_sorted=sorted(ESPECIES_SEMFERRAO,key=lambda x:x['registros_gbif'],reverse=True)
        fig_rank=go.Figure()
        for sp in sp_sorted:
            fig_rank.add_trace(go.Bar(x=[sp['nome']],y=[sp['registros_gbif']],
                marker_color=sp['cor'],opacity=.88,showlegend=False,
                text=[f"{sp['registros_gbif']:,}"],textposition='outside',
                textfont=dict(size=9,family='DM Mono',color=sp['cor']),
                hovertemplate=f"<b>{sp['nome']}</b><br>{sp['registros_gbif']:,}<br>IUCN: {sp['ameaca']}<extra></extra>"))
        fig_rank.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',
            title=dict(text=T['trend_opt2'],font=dict(size=13,family='Playfair Display')),
            height=380,font=dict(family='DM Sans'),
            xaxis=dict(showgrid=False,tickangle=-30),
            yaxis=dict(showgrid=True,gridcolor='#F0E8D0'),margin=dict(t=50,b=20))
        plot(fig_rank)

    else:
        states_s=sorted(ESTADOS_DATA.keys(),key=lambda e:ESTADOS_DATA[e]['registros'],reverse=True)
        regs_s=[ESTADOS_DATA[e]['registros'] for e in states_s]
        cors_s=[{"Alta":"#C0390A","Média":"#C47D0E","Baixa":"#2D7A45"}.get(ESTADOS_DATA[e]['status'],"#888") for e in states_s]
        fig_est2=go.Figure(go.Bar(x=states_s,y=regs_s,marker_color=cors_s,opacity=.88,
            text=regs_s,textposition='outside',textfont=dict(size=9,family='DM Mono'),
            hovertemplate='<b>%{x}</b><br>%{y:,}<extra></extra>'))
        fig_est2.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',
            title=dict(text=T['trend_opt3'],font=dict(size=13,family='Playfair Display')),
            height=380,font=dict(family='DM Sans'),
            xaxis=dict(showgrid=False,tickangle=-45),
            yaxis=dict(showgrid=True,gridcolor='#F0E8D0'),margin=dict(t=50,b=20))
        plot(fig_est2)

# ── TAB 6: PARÂMETROS ────────────────────────────────────────
with tabs[5]:
    st.markdown(f'<div class="section-label">{T["param_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{T["param_title"]}</div>',unsafe_allow_html=True)

    sp_sel=st.selectbox(T['param_sel'],[s['nome'] for s in ESPECIES_SEMFERRAO if s['nome'] in PARAMS_ESP],key="param_sp_sel")
    if sp_sel and sp_sel in PARAMS_ESP:
        p=PARAMS_ESP[sp_sel]
        sp_obj=next(s for s in ESPECIES_SEMFERRAO if s['nome']==sp_sel)
        cor_sp=sp_obj['cor']

        param_key_sel=st.selectbox(T['param_sel']+" (detalhe)",list(T['param_names'].keys()),key="param_detail")
        pname=T['param_names'][param_key_sel]
        all_sp=list(PARAMS_ESP.keys())
        all_vals=[PARAMS_ESP[s].get(param_key_sel,0) for s in all_sp]
        cors_p=[next((s['cor'] for s in ESPECIES_SEMFERRAO if s['nome']==sn),"#888") for sn in all_sp]
        fig_param=go.Figure()
        fig_param.add_trace(go.Bar(x=all_sp,y=all_vals,marker_color=cors_p,opacity=.88,
            text=all_vals,textposition='outside',textfont=dict(size=9,family='DM Mono'),
            hovertemplate='<b>%{x}</b><br>%{y}<extra></extra>'))
        idx=all_sp.index(sp_sel) if sp_sel in all_sp else -1
        if idx>=0:
            fig_param.add_shape(type="rect",x0=idx-.4,x1=idx+.4,y0=0,y1=all_vals[idx]*1.05,
                line=dict(color=cor_sp,width=3),fillcolor="rgba(0,0,0,0)")
        fig_param.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(90,48,0,.02)',
            title=dict(text=f"{pname} — {T['param_comparativo']}",font=dict(size=13,family='Playfair Display')),
            height=360,font=dict(family='DM Sans'),
            xaxis=dict(showgrid=False,tickangle=-30),
            yaxis=dict(showgrid=True,gridcolor='#F0E8D0',title=pname),
            margin=dict(t=50,b=20))
        plot(fig_param)

        st.markdown(f"""
        <div class="info-card honey">
          <strong style="color:{cor_sp}">{sp_sel} ({sp_obj['cientifico']})</strong><br><br>
          <div style="font-size:.88rem;line-height:2.1;color:#5C2E00">
            {sp_obj['descricao']}<br><br>
            • <b>IUCN:</b> {sp_obj['ameaca']} · <b>{T['param_bioma']}:</b> {sp_obj['bioma']} · <b>{T['param_regiao']}:</b> {sp_obj['regiao']}<br>
            • <b>{T['param_names']['colonia']}:</b> {p['colonia']:,} · <b>{T['param_names']['postura_dia']}:</b> {p['postura_dia']}<br>
            • <b>{T['param_names']['vida_operaria']}:</b> {p['vida_operaria']} · <b>{T['param_names']['longe_formag']}:</b> {p['longe_formag']} m<br>
            • <b>{T['param_names']['prod_mel_kg']}:</b> {p['prod_mel_kg']} · <b>{T['param_names']['raio_dna_km']}:</b> {p['raio_dna_km']} km
          </div>
        </div>""",unsafe_allow_html=True)

# ── TAB 7: DADOS BRUTOS ──────────────────────────────────────
with tabs[6]:
    st.markdown(f'<div class="section-label">{T["raw_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{T["raw_title"]}</div>',unsafe_allow_html=True)

    rows_raw=[]
    for sp in ESPECIES_SEMFERRAO:
        p=PARAMS_ESP.get(sp['nome'],{})
        rows_raw.append({T['raw_col_esp']:sp['nome'],T['raw_col_cient']:sp['cientifico'],
            T['raw_col_tam']:sp['tam'],T['raw_col_raio']:sp['raio'],
            T['raw_col_mel']:sp['mel'],T['raw_col_iucn']:sp['ameaca'],T['raw_col_bioma']:sp['bioma'],
            T['raw_col_gbif']:sp['registros_gbif'],
            T['raw_col_colonia']:p.get('colonia','-'),T['raw_col_mel_ano']:p.get('prod_mel_kg','-')})
    df_raw=pd.DataFrame(rows_raw)
    st.dataframe(df_raw,use_container_width=True,height=460,
        column_config={T['raw_col_gbif']:st.column_config.ProgressColumn(T['raw_col_gbif'],min_value=0,max_value=5500)})

    rows_sol=[]
    for sp in ESPECIES_SOLITARIAS:
        rows_sol.append({T['raw_col_esp']:sp['nome'],T['raw_col_cient']:sp['cientifico'],
            T['raw_col_tam']:sp['tam'],T['raw_col_habitat']:sp['habitat'],
            T['raw_col_polinizacao']:sp['polinizacao'],T['raw_col_gbif']:sp['registros_gbif']})
    df_sol=pd.DataFrame(rows_sol)
    st.markdown(f"**{T['raw_sol_title']}**",unsafe_allow_html=False)
    st.dataframe(df_sol,use_container_width=True,height=260)

    full_buf=io.StringIO()
    pd.concat([df_raw.assign(Tipo="Meliponini"),df_sol.assign(Tipo="Solitária")]).to_csv(full_buf,index=False)
    st.download_button(T['download_csv'],full_buf.getvalue(),"abelhas_brasil_catalogo.csv","text/csv")

# ── TAB 8: FONTES ────────────────────────────────────────────
with tabs[7]:
    st.markdown(f'<div class="section-label">{T["sources_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{T["sources_title"]}</div>',unsafe_allow_html=True)
    fontes=[
        ("GBIF","GBIF — Global Biodiversity Information Facility","gbif.org · 24.500+ registros de Meliponini no Brasil.","#C47D0E"),
        ("A.B.E.L.H.A.","A.B.E.L.H.A. — Associação Brasileira de Estudo das Abelhas","abelha.org.br · Atlas da Meliponicultura.","#C0390A"),
        ("iNATURALIST","iNaturalist — Ciência Cidadã Global","inaturalist.org · 23.100+ registros de Meliponini.","#2D7A45"),
        ("FATEC","FATEC Jundiaí — TCC Gestão Ambiental (2022)","Hotel para Abelhas Solitárias · Ciência na Praça.","#1B3A1E"),
        ("CIDADE ABELHAS","Parque Cidade das Abelhas — São Paulo (2022)","Visita técnica · Registro fotográfico de colmeias racionais.","#5C3D1E"),
        ("IUCN","IUCN Red List — Lista Vermelha","Manduri, Mandaçaia, Guaraipo, Tiúba (VU).","#8B2515"),
        ("INPA","INPA — Instituto Nacional de Pesquisas da Amazônia","Modelo de colmeia racional INPA.","#0D4E72"),
        ("EMBRAPA","EMBRAPA Cerrados / Amazônia Oriental","Dados de Meliponicultura em biomas brasileiros.","#C47D0E"),
    ]
    for sigla,nome,desc,cor in fontes:
        st.markdown(f"""<div class="info-card" style="border-left-color:{cor}">
          <div style="display:flex;align-items:flex-start;gap:1rem">
            <div style="background:{cor};color:white;font-family:'DM Mono',monospace;font-size:.6rem;padding:4px 7px;border-radius:4px;white-space:nowrap;flex-shrink:0;margin-top:2px;font-weight:bold;text-align:center;min-width:80px">{sigla}</div>
            <div><div style="font-weight:500;font-size:.9rem;color:var(--honey-dark)">{nome}</div>
            <div style="font-size:.82rem;color:var(--warm-gray);margin-top:.2rem">{desc}</div></div>
          </div></div>""",unsafe_allow_html=True)
    st.markdown(f"<br><div class='section-label'>{T['tech_label']}</div>",unsafe_allow_html=True)
    techs=["Python 3.11","Streamlit","Plotly","Folium","Pandas","NumPy","GBIF API","iNaturalist","MarkerCluster","HeatMap"]
    st.markdown(''.join([f'<span class="source-badge">{t}</span>' for t in techs]),unsafe_allow_html=True)
    st.markdown(f"""<div class="footer-wrap" style="margin-top:2rem">
      <div class="footer-title">{T['footer_title']}</div>
      <p style="margin:.5rem 0;font-size:.9rem">{T['footer_desc']}</p>
      <p style="margin:1rem 0 .5rem;font-size:.85rem;opacity:.7">
        {T['footer_links']} &nbsp;|&nbsp;
        🌐 <a href="https://amaurialmeida.github.io/environmental-portfolio/" style="color:var(--honey-light)">Portfólio</a> &nbsp;|&nbsp;
        🐙 <a href="https://github.com/amaurialmeida" style="color:var(--honey-light)">GitHub</a></p>
      <p style="font-size:.75rem;opacity:.5;margin:0">© 2022–2026 · Observatório Meliponini · Brasil</p>
    </div>""",unsafe_allow_html=True)
