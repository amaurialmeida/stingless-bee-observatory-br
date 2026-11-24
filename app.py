import streamlit as st
import folium
from folium.plugins import MarkerCluster, HeatMap
from streamlit_folium import st_folium
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import numpy as np
import json
import urllib.request, urllib.parse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import os
import io
from translations import TRANSLATIONS

LANGS=[("pt","🇧🇷","PT"),("en","🇺🇸","EN"),("es","🇪🇸","ES"),("it","🇮🇹","IT"),("fr","🇫🇷","FR"),
       ("de","🇩🇪","DE"),("zh","🇨🇳","中文"),("ar","🇸🇦","AR"),("el","🇬🇷","EL"),("af","🇿🇦","AF")]
CODES=[c for c,_,_ in LANGS]
FLAGS={c:f"{f} {l}" for c,f,l in LANGS}
assert set(CODES)==set(TRANSLATIONS),"idiomas em LANGS e translations.py precisam coincidir"
def _initial_lang():
    q=st.query_params.get("lang")
    return q if q in CODES else "pt"
if "lang" not in st.session_state:
    st.session_state.lang=_initial_lang()

st.set_page_config(
    page_title=TRANSLATIONS[st.session_state.lang]["page_title"],
    page_icon="🐝",
    layout="wide"
)

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

# ═══════════════════════════════════════════════════════════════
# OCORRÊNCIAS — API pública do GBIF (dados reais, sem pontos simulados)
# ═══════════════════════════════════════════════════════════════
GBIF_API="https://api.gbif.org/v1"
OCC_POR_ESPECIE=150
RAIO_MAX_PONTOS=60
OCC_COLS=["lat","lon","especie","taxon","local","ano","fonte","gbif_id"]

def _get_json(url,timeout=20):
    req=urllib.request.Request(url,headers={"User-Agent":"stingless-bee-observatory-br/1.0"})
    with urllib.request.urlopen(req,timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))

def _nome_gbif(cientifico):
    """'Xylocopa sp.' -> 'Xylocopa' (busca no nível do gênero)."""
    return cientifico.replace(" sp.","").strip()

def parse_gbif_results(results,nome):
    """Converte registros do GBIF em linhas; descarta coordenadas fora do Brasil."""
    rows=[]
    for r in results:
        lat,lon=r.get("decimalLatitude"),r.get("decimalLongitude")
        if lat is None or lon is None: continue
        if not (-34<=lat<=6 and -74<=lon<=-34): continue
        rows.append({"lat":float(lat),"lon":float(lon),"especie":nome,
            "taxon":r.get("species") or r.get("scientificName") or "",
            "local":r.get("municipality") or r.get("stateProvince") or r.get("locality") or "",
            "ano":r.get("year"),
            "fonte":r.get("datasetName") or r.get("institutionCode") or "GBIF",
            "gbif_id":r.get("key")})
    return rows

def _baixa_especie(nome,cientifico):
    cn=_nome_gbif(cientifico)
    m=_get_json(f"{GBIF_API}/species/match?name={urllib.parse.quote(cn)}")
    key=m.get("usageKey")
    if not key: return []
    q=urllib.parse.urlencode({"taxonKey":key,"country":"BR","hasCoordinate":"true",
        "hasGeospatialIssue":"false","limit":OCC_POR_ESPECIE})
    return parse_gbif_results(_get_json(f"{GBIF_API}/occurrence/search?{q}").get("results",[]),nome)

@st.cache_data(ttl=86400,show_spinner=False)
def _ocorrencias_gbif():
    todas=ESPECIES_SEMFERRAO+ESPECIES_SOLITARIAS
    rows=[]
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs=[ex.submit(_baixa_especie,e["nome"],e["cientifico"]) for e in todas]
        for f in futs:
            try: rows+=f.result()
            except Exception: pass
    if not rows: raise RuntimeError("GBIF sem resultados")  # exceção não é guardada no cache
    return pd.DataFrame(rows,columns=OCC_COLS),datetime.now().strftime("%d/%m/%Y")

def _ocorrencias_demo():
    """Plano B (GBIF fora do ar): capitais × espécies de bee_map_data.json — ilustrativo, não é dado de campo."""
    caminho=os.path.join(os.path.dirname(os.path.abspath(__file__)),"bee_map_data.json")
    if not os.path.exists(caminho): return pd.DataFrame(columns=OCC_COLS)
    with open(caminho,encoding="utf-8") as f: d=json.load(f)
    return pd.DataFrame([{"lat":x["lat"],"lon":x["lon"],"especie":x["species_name"],"taxon":x.get("scientific_name",""),
        "local":f"{x['city']}/{x['uf']}","ano":None,"fonte":"demo","gbif_id":None} for x in d],columns=OCC_COLS)

try:
    df_occ,OCC_DATA=_ocorrencias_gbif(); OCC_MODO="gbif"
except Exception:
    df_occ=_ocorrencias_demo(); OCC_DATA=""; OCC_MODO="demo" if len(df_occ) else "none"

# Dados por estado
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

# Série temporal de registros GBIF
ANOS_GBIF = list(range(2010, 2025))
GBIF_RECORDS = {
    "Total":       [1200,1580,2100,2800,3500,4200,5100,6300,7800,9200,11500,14000,17200,20800,24500],
    "iNaturalist": [50,  120, 280, 650,1200,2100,3400,5200,7100,8900,11000,13500,16500,19800,23100],
    "Meliponini":  [320, 410, 580, 750, 980,1250,1580,1920,2380,2850, 3420, 4100, 4850, 5700, 6600],
    "Xylocopa":    [180, 220, 310, 420, 550, 720, 920,1180,1450,1720, 2100, 2500, 3000, 3560, 4200],
}

# Parâmetros de cada espécie (valores biológicos)
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

# ═══════════════════════════════════════════════════════════════
# NÚMEROS DO APP — calculados a partir do GBIF (cache 24 h).
# Se o GBIF cair: usa o último snapshot salvo; sem snapshot, valores de referência.
# ═══════════════════════════════════════════════════════════════
import unicodedata
ANOS_GBIF=list(range(2010,2025))
UF_ESTADO={"São Paulo":"SP","Minas Gerais":"MG","Paraná":"PR","Bahia":"BA","Pará":"PA","Santa Catarina":"SC",
    "Rio Grande do Sul":"RS","Ceará":"CE","Mato Grosso":"MT","Amazonas":"AM","Goiás":"GO","Rio de Janeiro":"RJ",
    "Espírito Santo":"ES","Pernambuco":"PE","Maranhão":"MA"}
GENEROS_SOLITARIAS=["Xylocopa","Hylaeus","Megachile","Nomada","Centris"]
INAT_DATASET="50c9509d-22c7-4a22-a47d-8c48425ef4a7"   # iNaturalist Research-grade Observations
SNAP_PATH=os.path.join(os.path.dirname(os.path.abspath(__file__)),"gbif_snapshot.json")

def _norm(x): return "".join(c for c in unicodedata.normalize("NFD",str(x).lower()) if unicodedata.category(c)!="Mn").strip()
_NOME_PARA_ESTADO={}
for _e,_u in UF_ESTADO.items():
    _NOME_PARA_ESTADO[_norm(_e)]=_e; _NOME_PARA_ESTADO[_norm(_u)]=_e

_BASE={"country":"BR","hasCoordinate":"true","hasGeospatialIssue":"false"}
def _busca(extra,facet=None,facet_limit=0):
    p={**_BASE,**extra,"limit":0}
    if facet: p.update({"facet":facet,"facetLimit":facet_limit})
    j=_get_json(f"{GBIF_API}/occurrence/search?{urllib.parse.urlencode(p,doseq=True)}")
    fac=[(c["name"],c["count"]) for c in (j.get("facets") or [{"counts":[]}])[0]["counts"]] if facet else []
    return j.get("count",0),fac

def _chave(nome):
    m=_get_json(f"{GBIF_API}/species/match?name={urllib.parse.quote(_nome_gbif(nome))}")
    if not m.get("usageKey") or m.get("matchType")=="NONE": raise RuntimeError(f"taxon não encontrado: {nome}")
    return m["usageKey"]

def _serie_ano(extra):
    _,fac=_busca({**extra,"year":f"{ANOS_GBIF[0]},{ANOS_GBIF[-1]}"},"year",50)
    d={int(a):n for a,n in fac}
    return [d.get(a,0) for a in ANOS_GBIF]

def _calcula_dados():
    todas=ESPECIES_SEMFERRAO+ESPECIES_SOLITARIAS
    with ThreadPoolExecutor(max_workers=6) as ex:
        k_trib=ex.submit(_chave,"Meliponini")
        k_esp={e["nome"]:ex.submit(_chave,e["cientifico"]) for e in todas}
        k_gen={g:ex.submit(_chave,g) for g in GENEROS_SOLITARIAS}
        trib=k_trib.result()
        sp_counts={n:ex.submit(lambda k=f.result():_busca({"taxonKey":k})[0]) for n,f in k_esp.items()}
        ser_m=ex.submit(_serie_ano,{"taxonKey":trib})
        ser_i=ex.submit(_serie_ano,{"taxonKey":trib,"datasetKey":INAT_DATASET})
        ser_g={g:ex.submit(lambda k=f.result():_serie_ano({"taxonKey":k})) for g,f in k_gen.items()}
        est_f=ex.submit(_busca,{"taxonKey":trib},"stateProvince",300)
        sp_counts={n:f.result() for n,f in sp_counts.items()}
        mel=ser_m.result(); inat=ser_i.result(); gen={g:f.result() for g,f in ser_g.items()}
        _,est_fac=est_f.result()
        total=[mel[i]+sum(gen[g][i] for g in gen) for i in range(len(ANOS_GBIF))]
        # estados: junta variantes de grafia ("São Paulo", "Sao Paulo", "SP")
        var={}; cont={}
        for nome,n in est_fac:
            e=_NOME_PARA_ESTADO.get(_norm(nome))
            if e: var.setdefault(e,[]).append(nome); cont[e]=cont.get(e,0)+n
        estados={}
        if len(cont)>=10:
            fut={e:ex.submit(lambda v=var[e]:len(_busca({"taxonKey":trib,"stateProvince":v},"speciesKey",1000)[1])) for e in cont}
            estados={e:{"registros":cont[e],"sp_count":fut[e].result()} for e in cont}
    if not sp_counts or sum(mel)==0: raise RuntimeError("GBIF sem dados")
    return {"data":datetime.now().strftime("%d/%m/%Y"),"sp_counts":sp_counts,
            "series":{"Total":total,"iNaturalist":inat,"Meliponini":mel,"Xylocopa":gen["Xylocopa"]},
            "estados":estados}

@st.cache_data(ttl=86400,show_spinner=False)
def _dados_gbif():
    d=_calcula_dados()   # exceção = não vai para o cache
    try:
        with open(SNAP_PATH,"w",encoding="utf-8") as f: json.dump(d,f,ensure_ascii=False)
    except Exception: pass
    return d

try:
    DADOS=_dados_gbif(); DADOS_MODO="live"
except Exception:
    try:
        with open(SNAP_PATH,encoding="utf-8") as f: DADOS=json.load(f); DADOS_MODO="snapshot"
    except Exception:
        DADOS=None; DADOS_MODO="static"

if DADOS:
    for _e in ESPECIES_SEMFERRAO+ESPECIES_SOLITARIAS:
        _e["registros_gbif"]=DADOS["sp_counts"].get(_e["nome"],_e["registros_gbif"])
    GBIF_RECORDS=DADOS["series"]
    if DADOS["estados"]:
        _ord=sorted(DADOS["estados"].items(),key=lambda kv:-kv[1]["registros"])
        _mx=_ord[0][1]["registros"] or 1
        _novo={}
        for _i,(_e,_d) in enumerate(_ord):
            _b=ESTADOS_DATA[_e]
            _novo[_e]={**_b,"registros":_d["registros"],"sp_count":_d["sp_count"],
                "raio":round(1.2+1.8*(_d["registros"]/_mx)**.5,2),
                "status":"Alta" if _i<5 else ("Média" if _i<10 else "Baixa")}
        ESTADOS_DATA=_novo
else:
    GBIF_RECORDS={k:v for k,v in GBIF_RECORDS.items() if k in ("Meliponini","Xylocopa")}   # séries de referência anteriores sem fonte

_SEP={"pt":".","es":".","it":".","de":".","el":".","fr":"\u202f","af":"\u00a0"}   # demais: vírgula
def _fmt(n,lang): return f"{int(n):,}".replace(",",_SEP.get(lang,","))
_mel=GBIF_RECORDS["Meliponini"]; _i14=ANOS_GBIF.index(2014)
_vu=[e["nome"] for e in ESPECIES_SEMFERRAO if e["ameaca"]=="VU"]
_lc=[e for e in ESPECIES_SEMFERRAO if e["ameaca"]=="LC"]
def _lista(nomes,lang): return ", ".join(nomes[:-1])+TRANSLATIONS[lang]["tok_and"]+nomes[-1]
_top=max(ESTADOS_DATA.items(),key=lambda kv:kv[1]["registros"])[0]

def _tokens(lang):
    L=TRANSLATIONS[lang]; live=DADOS is not None
    cres=(_mel[-1]-_mel[_i14]) if live else None
    pct=(cres/_mel[_i14]*100) if live and _mel[_i14] else None
    sp_n=ESTADOS_DATA["São Paulo"]["registros"] if (live and DADOS["estados"]) else None
    if sp_n: sp_sent=L["tok_sp_top" if _top=="São Paulo" else "tok_sp_plain"].format(n=_fmt(sp_n,lang))
    else: sp_sent=L["tok_sp_generic"]
    return {
      "@@TOTAL@@":_fmt(sum(_mel),lang) if live else L["tok_nd"],
      "@@INAT@@":_fmt(sum(GBIF_RECORDS["iNaturalist"]),lang) if live else L["tok_nd"],
      "@@VU@@":str(len(_vu)),"@@LC@@":str(len(_lc)),"@@VU_LIST@@":_lista(_vu,lang),
      "@@VU_TAGS@@":", ".join(f"{n} (VU)" for n in _vu),
      "@@GROWTH@@":f"+{pct:.0f}%" if live else "n/d","@@GROWTH_N@@":f"{pct:.0f}%" if live else "n/d",
      "@@GROWTH_ABS@@":_fmt(cres,lang) if live else "n/d",
      "@@SP_SENT@@":sp_sent,
    }
def _aplica(obj,tk):
    if isinstance(obj,str):
        for k,v in tk.items(): obj=obj.replace(k,v)
        return obj
    if isinstance(obj,dict): return {k:_aplica(v,tk) for k,v in obj.items()}
    if isinstance(obj,list): return [_aplica(v,tk) for v in obj]
    if isinstance(obj,tuple): return tuple(_aplica(v,tk) for v in obj)
    return obj

# ═══════════════════════════════════════════════════════════════
# TRADUÇÕES — editar em translations.py (10 idiomas)
# ═══════════════════════════════════════════════════════════════
T_ALL={_l:_aplica(TRANSLATIONS[_l],_tokens(_l)) for _l in TRANSLATIONS}

def render_lang():
    c0,c1=st.columns([2,9])
    with c0:
        st.markdown(f'<a class="back-link" href="https://amaurialmeida.github.io/environmental-portfolio/" target="_blank" rel="noopener">{TRANSLATIONS[st.session_state.lang]["back_link"]}</a>',unsafe_allow_html=True)
    with c1:
        try:
            escolha=st.pills("Language",CODES,selection_mode="single",default=st.session_state.lang,
                format_func=lambda c:FLAGS[c],label_visibility="collapsed",key="lang_pills")
        except AttributeError:   # Streamlit antigo, sem st.pills
            escolha=st.radio("Language",CODES,index=CODES.index(st.session_state.lang),horizontal=True,
                format_func=lambda c:FLAGS[c],label_visibility="collapsed",key="lang_radio")
        if escolha and escolha!=st.session_state.lang:
            st.session_state.lang=escolha
            st.query_params["lang"]=escolha
            st.rerun()

render_lang()
T=T_ALL[st.session_state.lang]
RTL=st.session_state.lang=="ar"
if RTL:   # árabe: texto da direita p/ esquerda; mapas, gráficos e tabelas continuam LTR
    st.markdown("""<style>
    [data-testid="stMain"],[data-testid="stAppViewContainer"] .main{direction:rtl;text-align:right;}
    .js-plotly-plot,iframe,[data-testid="stDataFrame"],[data-testid="stPills"]{direction:ltr;}
    html,body,[class*="css"]{font-family:'Noto Naskh Arabic','DM Sans',sans-serif;}
    .section-label,.hero-tag,.badge,.source-badge,.metric-label,.back-link{letter-spacing:0!important;text-transform:none!important;}
    </style>""",unsafe_allow_html=True)

def sp_t(sp,campo):
    """Texto da espécie no idioma atual (cai no português se faltar)."""
    return T['species_text'].get(sp['nome'],{}).get(campo,sp.get(campo,''))

# Template Plotly único: mesma tipografia/cores em todos os gráficos
PLOT_FONT="DM Sans, Noto Sans, Noto Sans SC, Noto Naskh Arabic, sans-serif"
PLOT_SERIF="Playfair Display, Noto Serif, Noto Sans SC, Noto Naskh Arabic, serif"
PLOT_MONO="DM Mono, Noto Sans, Noto Sans SC, Noto Naskh Arabic, monospace"
pio.templates["bee"]=go.layout.Template(layout=dict(
    font=dict(family=PLOT_FONT,color="#3A1800"),
    paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)",
    colorway=["#C47D0E","#2D7A45","#C0390A","#1A5C9A","#5C3D1E","#F5A623"],
    title=dict(font=dict(family="Playfair Display, serif",size=13,color="#8B5000")),
    hoverlabel=dict(font=dict(family=PLOT_FONT))))
pio.templates.default="bee"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500&family=DM+Mono&family=Noto+Sans:wght@400;500;700&family=Noto+Serif:wght@700&family=Noto+Sans+SC:wght@400;500;700&family=Noto+Naskh+Arabic:wght@400;700&display=swap');
:root{--honey:#C47D0E;--honey-dark:#8B5000;--honey-light:#F5A623;--honey-pale:#FFF3CC;
  --forest:#1B3A1E;--forest-mid:#2D5A32;--forest-light:#3D7A45;
  --earth:#5C3D1E;--cream:#FDFAF4;--warm-gray:#7A6A50;--black:#0D1117;
  --alert:#C0390A;}
html,body,[class*="css"]{font-family:'DM Sans','Noto Sans','Noto Sans SC','Noto Naskh Arabic',sans-serif;background:var(--cream);color:var(--black);}
.hero-wrap{background:linear-gradient(135deg,#1A0A00 0%,#3D1A00 45%,#5A3000 100%);border-radius:20px;padding:3rem 2.5rem 2rem;margin-bottom:2rem;position:relative;overflow:hidden;}
.hero-wrap::before{content:"🐝";font-size:200px;position:absolute;right:-20px;top:-30px;opacity:0.06;}
.hero-tag{background:var(--honey-light);color:#1A0A00;font-family:'DM Mono','Noto Sans','Noto Sans SC','Noto Naskh Arabic',monospace;font-size:.7rem;font-weight:bold;letter-spacing:2px;padding:4px 12px;border-radius:4px;display:inline-block;margin-bottom:1rem;text-transform:uppercase;}
.hero-title{font-family:'Playfair Display','Noto Serif','Noto Sans SC','Noto Naskh Arabic',serif;font-size:2.8rem;font-weight:900;color:#fff;line-height:1.15;margin-bottom:.8rem;white-space:pre-line;}
.hero-subtitle{font-size:1rem;color:rgba(255,255,255,.78);max-width:680px;line-height:1.6;margin-bottom:1.5rem;}
.hero-badges{display:flex;gap:10px;flex-wrap:wrap;}
.badge{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);color:rgba(255,255,255,.85);font-size:.72rem;font-family:'DM Mono','Noto Sans','Noto Sans SC','Noto Naskh Arabic',monospace;padding:5px 12px;border-radius:20px;}
.badge-honey{background:rgba(245,166,35,.2);border-color:var(--honey-light);color:var(--honey-light);}
.metric-box{background:white;border-radius:16px;padding:1.4rem 1.2rem;border-top:4px solid var(--honey-light);box-shadow:0 2px 12px rgba(0,0,0,.07);text-align:center;}
.metric-box.forest{border-top-color:var(--forest-light);}
.metric-box.earth{border-top-color:var(--earth);}
.metric-box.alert{border-top-color:var(--alert);}
.metric-val{font-family:'Playfair Display','Noto Serif','Noto Sans SC','Noto Naskh Arabic',serif;font-size:2.1rem;font-weight:900;color:var(--honey-dark);line-height:1;margin-bottom:.3rem;}
.metric-label{font-size:.75rem;color:var(--warm-gray);text-transform:uppercase;letter-spacing:1px;}
.section-label{font-family:'DM Mono','Noto Sans','Noto Sans SC','Noto Naskh Arabic',monospace;font-size:.65rem;color:var(--honey-dark);text-transform:uppercase;letter-spacing:3px;margin-bottom:.3rem;}
.section-title{font-family:'Playfair Display','Noto Serif','Noto Sans SC','Noto Naskh Arabic',serif;font-size:1.9rem;font-weight:700;color:var(--honey-dark);margin-bottom:1.2rem;line-height:1.2;}
.info-card{background:white;border-radius:16px;padding:1.5rem;box-shadow:0 2px 12px rgba(0,0,0,.05);border-left:4px solid var(--honey-light);margin-bottom:1rem;}
.info-card.forest{border-left-color:var(--forest-light);}
.info-card.earth{border-left-color:var(--earth);}
.info-card.alert{border-left-color:var(--alert);}
.info-card.honey{border-left-color:var(--honey);background:linear-gradient(135deg,var(--honey-pale),#FFF8DD);}
.method-step{display:flex;align-items:flex-start;gap:1rem;padding:1rem;background:white;border-radius:12px;margin-bottom:.8rem;box-shadow:0 1px 6px rgba(0,0,0,.04);}
.step-num{background:var(--honey-dark);color:white;font-family:'Playfair Display','Noto Serif','Noto Sans SC','Noto Naskh Arabic',serif;font-size:1.1rem;font-weight:700;width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.step-title{font-weight:500;color:var(--honey-dark);font-size:.95rem;}
.step-desc{font-size:.82rem;color:var(--warm-gray);margin-top:.2rem;}
.discovery-box{background:linear-gradient(135deg,var(--honey-pale),#FFF0AA);border:2px solid var(--honey-light);border-radius:16px;padding:1.8rem;margin:.8rem 0;}
.discovery-title{font-family:'Playfair Display','Noto Serif','Noto Sans SC','Noto Naskh Arabic',serif;font-size:1.1rem;font-weight:700;color:var(--honey-dark);margin-bottom:.5rem;}
.timeline-item{display:flex;gap:1rem;padding:1rem 0;border-bottom:1px solid #F0E8D0;}
.timeline-year{font-family:'Playfair Display','Noto Serif','Noto Sans SC','Noto Naskh Arabic',serif;font-size:.95rem;font-weight:700;color:var(--honey);min-width:100px;}
.timeline-title{font-weight:500;color:var(--honey-dark);margin-bottom:.2rem;}
.timeline-desc{font-size:.85rem;color:var(--warm-gray);}
.source-badges{display:flex;gap:8px;flex-wrap:wrap;margin-top:.8rem;}
.source-badge{background:var(--honey-dark);color:white;font-family:'DM Mono','Noto Sans','Noto Sans SC','Noto Naskh Arabic',monospace;font-size:.65rem;padding:4px 10px;border-radius:4px;letter-spacing:1px;text-transform:uppercase;}
.footer-wrap{background:var(--honey-dark);border-radius:20px;padding:2rem;color:rgba(255,255,255,.8);text-align:center;margin-top:3rem;}
.footer-title{font-family:'Playfair Display','Noto Serif','Noto Sans SC','Noto Naskh Arabic',serif;color:var(--honey-light);font-size:1.2rem;margin-bottom:.5rem;}
.esp-card{background:white;border-radius:14px;padding:1.2rem;border-top:4px solid;box-shadow:0 2px 10px rgba(0,0,0,.06);height:100%;}
.esp-name{font-family:'Playfair Display','Noto Serif','Noto Sans SC','Noto Naskh Arabic',serif;font-size:.95rem;font-weight:700;margin-bottom:.2rem;}
.esp-sci{font-size:.75rem;font-family:'DM Mono','Noto Sans','Noto Sans SC','Noto Naskh Arabic',monospace;color:var(--warm-gray);}
.esp-meta{font-size:.7rem;line-height:1.8;margin-top:.4rem;}
.photo-group{font-family:'DM Mono','Noto Sans','Noto Sans SC','Noto Naskh Arabic',monospace;font-size:.6rem;text-transform:uppercase;letter-spacing:2px;color:var(--honey);margin:.6rem 0 .3rem;padding:.3rem .8rem;background:var(--honey-pale);border-radius:4px;display:inline-block;}
.photo-placeholder{background:var(--honey-pale);border:2px dashed var(--honey-light);border-radius:12px;padding:1.8rem;text-align:center;min-height:200px;display:flex;flex-direction:column;align-items:center;justify-content:center;}
.photo-emoji{font-size:2.4rem;}
.photo-title{font-weight:600;color:var(--honey-dark);margin:.4rem 0 .2rem;font-size:.88rem;}
.photo-sp{font-size:.72rem;font-family:'DM Mono','Noto Sans','Noto Sans SC','Noto Naskh Arabic',monospace;color:var(--warm-gray);font-style:italic;}
.photo-desc{font-size:.75rem;color:var(--warm-gray);line-height:1.45;margin-top:.2rem;}
.photo-path{font-size:.62rem;color:var(--honey);font-family:'DM Mono','Noto Sans','Noto Sans SC','Noto Naskh Arabic',monospace;margin-top:.4rem;background:#FFE880;padding:2px 7px;border-radius:4px;}
.photo-legenda{font-size:.7rem;color:var(--warm-gray);font-style:italic;padding:.4rem .8rem;background:#faf5ec;text-align:center;border-top:1px solid #F0E8D0;}
.st-key-photo-destaque{border:3px solid var(--honey);border-radius:14px;overflow:hidden;box-shadow:0 4px 20px rgba(196,125,14,.2);}
.st-key-photo-destaque-final{border:3px solid var(--forest-light);border-radius:14px;overflow:hidden;box-shadow:0 4px 20px rgba(45,90,50,.2);}
/* Playfair usa números 'old-style' por padrão (12+6, 4VU, anos desalinhados): força números alinhados */
.metric-val,.timeline-year,.step-num,.hero-title,.section-title{font-variant-numeric:lining-nums;font-feature-settings:"lnum" 1;}
.metric-val small{font-family:'DM Mono','Noto Sans','Noto Sans SC','Noto Naskh Arabic',monospace;font-size:.95rem;font-weight:500;margin-left:.3rem;letter-spacing:1px;}
.back-link{font-family:'DM Mono','Noto Sans','Noto Sans SC','Noto Naskh Arabic',monospace;font-size:.72rem;letter-spacing:1.5px;color:var(--honey-dark)!important;text-decoration:none;text-transform:uppercase;display:inline-block;padding:.5rem 0;}
.back-link:hover{color:var(--honey)!important;}
</style>""",unsafe_allow_html=True)

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
_tot24=GBIF_RECORDS["Total"][-1] if "Total" in GBIF_RECORDS else None
with c2: st.markdown(f'<div class="metric-box forest"><div class="metric-val">{_fmt(_tot24,st.session_state.lang) if _tot24 else "—"}</div><div class="metric-label">{T["m2"]}</div></div>',unsafe_allow_html=True)
with c3: st.markdown(f'<div class="metric-box earth"><div class="metric-val">{len(ESTADOS_DATA)}</div><div class="metric-label">{T["m3"]}</div></div>',unsafe_allow_html=True)
with c4: st.markdown(f'<div class="metric-box alert"><div class="metric-val">{len(_vu)}<small>VU</small></div><div class="metric-label">{T["m4"]}</div></div>',unsafe_allow_html=True)
st.caption(T['dados_'+DADOS_MODO].format(d=(DADOS or {}).get("data","")))
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

    # Leia a chave uma única vez no Streamlit Secrets.
    # Nunca coloque a chave diretamente neste arquivo público.
    try:
        carto_key = str(st.secrets["CARTO_API_KEY"]).strip()
    except Exception:
        carto_key = ""

    _carto_warned=[]  # o aviso aparece uma única vez, não uma por mapa
    def add_carto_base(target_map, style_url, layer_name):
        """Adiciona CARTO com a chave; usa OSM apenas se o Secret não existir."""
        if carto_key:
            folium.TileLayer(
                tiles=(
                    "https://{s}.basemaps.cartocdn.com/" + style_url + "/"
                    "{z}/{x}/{y}{r}.png?key=" + carto_key
                ),
                attr=(
                    '&copy; <a href="https://www.openstreetmap.org/copyright">'
                    "OpenStreetMap</a> contributors &copy; "
                    '<a href="https://carto.com/attributions">CARTO</a>'
                ),
                name=layer_name,
                subdomains="abcd", max_zoom=20,
                overlay=False, control=True,
            ).add_to(target_map)
        else:
            folium.TileLayer(
                "OpenStreetMap", name="OpenStreetMap",
                attr=(
                    '&copy; <a href="https://www.openstreetmap.org/copyright">'
                    "OpenStreetMap</a> contributors"
                ),
                control=True,
            ).add_to(target_map)
            if not _carto_warned:
                _carto_warned.append(1)
                st.caption(T['carto_fallback'])

    _raios={e["nome"]:e for e in ESPECIES_SEMFERRAO}
    sel_raio=st.multiselect(T['raio_sel'],list(_raios),default=[],key="raio_sel",
        format_func=lambda n:f"{n} · {_raios[n]['raio']:,} m".replace(",","."))
    if sel_raio: st.caption(T['raio_note'].format(n=RAIO_MAX_PONTOS))
    mapa=folium.Map(location=[-15,-52],zoom_start=4,tiles=None,control_scale=True)
    add_carto_base(mapa, "rastertiles/voyager", "CARTO Voyager")
    cluster=MarkerCluster(name=T['cluster_name']).add_to(mapa)

    # Ocorrências individuais
    COR_ESP={s['nome']:s['cor'] for s in ESPECIES_SEMFERRAO+ESPECIES_SOLITARIAS}
    for _,row in df_occ.iterrows():
        cor=COR_ESP.get(row['especie'],'#888')
        folium.CircleMarker(
            location=[row['lat'],row['lon']],radius=5,
            color=cor,fill=True,fill_color=cor,fill_opacity=.7,weight=1,
            popup=(f"<b>{row['especie']}</b><br><i>{row['taxon']}</i><br>{row['local']}<br>"
                   f"{'' if pd.isna(row['ano']) else str(int(row['ano']))+' · '}{str(row['fonte'])[:48]}"
                   +(f"<br><a href='https://www.gbif.org/occurrence/{row['gbif_id']}' target='_blank'>GBIF #{row['gbif_id']}</a>" if row['gbif_id'] else "")),
            tooltip=f"🐝 {row['especie']}").add_to(cluster)

    # Círculos de forrageamento (raio de voo em METROS ao redor de ocorrências reais)
    if sel_raio:
        grp=folium.FeatureGroup(name=T['raio_layer'],show=True).add_to(mapa)
        for nome in sel_raio:
            sp=_raios[nome]
            for _,row in df_occ[df_occ["especie"]==nome].head(RAIO_MAX_PONTOS).iterrows():
                folium.Circle(location=[row['lat'],row['lon']],radius=sp['raio'],
                    color=sp['cor'],weight=1.5,fill=True,fill_color=sp['cor'],fill_opacity=.18,
                    tooltip=f"{nome} · {sp['raio']:,} m".replace(",",".")).add_to(grp)
        folium.LayerControl(collapsed=True).add_to(mapa)

    # Bolhas grandes por estado
    for estado,d in ESTADOS_DATA.items():
        cor_s={"Alta":"#C0390A","Média":"#C47D0E","Baixa":"#2D7A45"}.get(d['status'],"#888")
        folium.CircleMarker(
            location=[d['lat'],d['lon']],
            radius=d['raio']*8,
            color=cor_s,fill=True,fill_color=cor_s,fill_opacity=.12,weight=2,
            popup=f"<b>{estado}</b><br>{T['pop_records']}: {d['registros']:,}<br>{T['pop_species']}: {d['sp_count']}<br>{T['pop_status']}: {T['status_vals'].get(d['status'],d['status'])}",
            tooltip=f"📍 {estado} · {d['registros']:,} {T['records_hover']}").add_to(mapa)

    st_folium(mapa,use_container_width=True,height=560,returned_objects=[],key="mapa_main")
    if OCC_MODO=="gbif":
        st.caption(T['occ_live'].format(n=f"{len(df_occ):,}".replace(",","."),d=OCC_DATA,k=OCC_POR_ESPECIE))
    elif OCC_MODO=="demo":
        st.caption(T['occ_demo'])
    else:
        st.caption(T['occ_none'])

    # Mapa de calor
    st.markdown(f"<br><div class='section-title' style='font-size:1.3rem'>{T['heat_title']}</div>",unsafe_allow_html=True)
    mapa_heat=folium.Map(location=[-15,-52],zoom_start=4,tiles=None,control_scale=True)
    add_carto_base(mapa_heat, "dark_all", "CARTO Dark Matter")
    heat_pts=[[row['lat'],row['lon'],0.8] for _,row in df_occ.iterrows()]
    HeatMap(heat_pts,radius=20,blur=15,
            gradient={0.2:'#1B3A1E',0.5:'#C47D0E',0.8:'#F5A623',1.0:'#FFE880'}).add_to(mapa_heat)
    st_folium(mapa_heat,use_container_width=True,height=380,returned_objects=[],key="mapa_heat")

    # Gráficos comparativos
    st.markdown(f"<br><div class='section-label'>{T['chart_label']}</div>",unsafe_allow_html=True)
    col_c1,col_c2=st.columns(2)
    with col_c1:
        sp_names=[s['nome'] for s in ESPECIES_SEMFERRAO]
        sp_regs=[s['registros_gbif'] for s in ESPECIES_SEMFERRAO]
        sp_cors=[s['cor'] for s in ESPECIES_SEMFERRAO]
        fig_sp=go.Figure(go.Bar(y=sp_names,x=sp_regs,orientation='h',
            marker_color=sp_cors,opacity=.88,
            text=sp_regs,textposition='outside',textfont=dict(size=9,family=PLOT_MONO),
            hovertemplate='<b>%{y}</b><br>%{x:,} '+T['records_hover']+'<extra></extra>'))
        fig_sp.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',
            title=dict(text=T['sp_registros_title'],font=dict(size=12,family=PLOT_SERIF)),
            height=400,font=dict(family=PLOT_FONT),
            xaxis=dict(showgrid=True,gridcolor='#F0E8D0'),yaxis=dict(showgrid=False),
            margin=dict(t=40,b=10))
        st.plotly_chart(fig_sp,width="stretch")
    with col_c2:
        est_names=list(ESTADOS_DATA.keys())
        est_regs=[ESTADOS_DATA[e]['registros'] for e in est_names]
        est_cors=[{"Alta":"#C0390A","Média":"#C47D0E","Baixa":"#2D7A45"}.get(ESTADOS_DATA[e]['status'],"#888") for e in est_names]
        fig_est=go.Figure(go.Bar(y=est_names,x=est_regs,orientation='h',
            marker_color=est_cors,opacity=.88,
            text=est_regs,textposition='outside',textfont=dict(size=9,family=PLOT_MONO),
            hovertemplate='<b>%{y}</b><br>%{x:,}<extra></extra>'))
        fig_est.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',
            title=dict(text=T['estado_title'],font=dict(size=12,family=PLOT_SERIF)),
            height=400,font=dict(family=PLOT_FONT),
            xaxis=dict(showgrid=True,gridcolor='#F0E8D0'),yaxis=dict(showgrid=False),
            margin=dict(t=40,b=10))
        st.plotly_chart(fig_est,width="stretch")

    # Cards de espécies
    st.markdown(f"<br><div class='section-label'>{T['gal_meli']}</div>",unsafe_allow_html=True)
    cols_sp=st.columns(4)
    for i,sp in enumerate(ESPECIES_SEMFERRAO):
        ameaca_cor={"VU":"#C0390A","LC":"#2D7A45","EN":"#8B2515"}.get(sp['ameaca'],"#888")
        with cols_sp[i%4]:
            st.markdown(f"""
            <div class="esp-card" style="border-top-color:{sp['cor']};margin-bottom:.8rem">
              <div class="esp-name" style="color:{sp['cor']}">{sp['emoji'] if 'emoji' in sp else '🐝'} {sp['nome']}</div>
              <div class="esp-sci">{sp['cientifico']}</div>
              <div class="esp-meta">
                📏 {sp['tam']} · 🏠 {sp['raio']}m<br>
                🍯 {T['honey']}: {T['mel_vals'].get(sp['mel'],sp['mel'])}<br>
                🌿 {sp_t(sp,'bioma')}<br>
                <span style="color:{ameaca_cor};font-weight:700">IUCN: {sp['ameaca']}</span>
              </div>
            </div>""",unsafe_allow_html=True)

    # Cards abelhas solitárias
    st.markdown(f"<br><div class='section-label'>{T['gal_sol']}</div>",unsafe_allow_html=True)
    cols_sol=st.columns(3)
    for i,sp in enumerate(ESPECIES_SOLITARIAS):
        with cols_sol[i%3]:
            st.markdown(f"""
            <div class="esp-card" style="border-top-color:{sp['cor']};margin-bottom:.8rem">
              <div class="esp-name" style="color:{sp['cor']}">🏨 {sp['nome']}</div>
              <div class="esp-sci">{sp['cientifico']}</div>
              <div class="esp-meta">
                📏 {sp['tam']}<br>
                🌳 {sp_t(sp,'habitat')}<br>
                🌸 {sp_t(sp,'polinizacao')}<br>
                📊 {sp['registros_gbif']:,} {T['gbif_records']}
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
    _linhas="<br>".join(f"<b>{k}:</b> {v}" for k,v in T['hotel_build'])
    st.markdown(f"""<div class="info-card earth" style="margin-top:.5rem;background:linear-gradient(135deg,#FFF8EE,#FFE8C0)">
      <strong style="color:#5C3D1E">{T['hotel_build_title']}</strong><br><br>
      <div style="font-family:'DM Mono','Noto Sans','Noto Sans SC','Noto Naskh Arabic',monospace;font-size:.82rem;line-height:2.4;color:#5C3D1E">{_linhas}</div></div>""",unsafe_allow_html=True)

# ── TAB 3: DESCOBERTAS ───────────────────────────────────────
with tabs[2]:
    st.markdown(f'<div class="section-label">{T["disc_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{T["disc_title"]}</div>',unsafe_allow_html=True)
    for emoji,titulo,texto in T['discoveries']:
        st.markdown(f'<div class="discovery-box" style="margin-bottom:.8rem"><div style="display:flex;align-items:flex-start;gap:1rem"><span style="font-size:1.5rem">{emoji}</span><div><div class="discovery-title">{titulo}</div><p style="color:#5C2E00;line-height:1.65;font-size:.93rem;margin:0">{texto}</p></div></div></div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-label" style="margin-top:1.5rem">{T["conclusion_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="info-card honey"><strong style="color:#8B5000;font-size:1rem">{T["conclusion_title"]}</strong><br><br><p style="color:#3A1800;line-height:1.7;font-size:.93rem">{T["conclusion_text"]}</p><p style="color:#C47D0E;font-size:.82rem;margin-bottom:0"><em>{T["conclusion_author"]}</em></p></div>',unsafe_allow_html=True)

    # Radar de características das espécies
    esp_radar=["Jataí","Mosquitinho","Manduri","Mirim Preguiça","Mandaçaia","Uruçu Nordestina"]
    cats_r=T['radar_cats']
    vals_r={
        "Jataí":         [6,10,5,7,10],"Mosquitinho":[3,8,4,3,10],
        "Manduri":       [5,5,8,6,4],"Mirim Preguiça":[2,7,4,5,10],
        "Mandaçaia":     [9,6,9,9,4],"Uruçu Nordestina":[10,5,9,10,4],
    }
    cors_r=[s['cor'] for s in ESPECIES_SEMFERRAO if s['nome'] in esp_radar]
    fig_rad=go.Figure()
    for esp_n,cor_r in zip(esp_radar,cors_r):
        v=vals_r[esp_n]
        fig_rad.add_trace(go.Scatterpolar(r=v+[v[0]],theta=cats_r+[cats_r[0]],
            fill='toself',name=esp_n,line_color=cor_r,fillcolor=cor_r,opacity=.2,
            hovertemplate=f'<b>{esp_n}</b><br>%{{theta}}: %{{r}}<extra></extra>'))
    fig_rad.update_layout(polar=dict(radialaxis=dict(range=[0,10],showticklabels=True)),
        paper_bgcolor='rgba(0,0,0,0)',height=420,font=dict(family=PLOT_FONT),
        title=dict(text=T['radar_title'],font=dict(size=13,family=PLOT_SERIF)),
        legend=dict(orientation='h',yanchor='bottom',y=-0.2,font=dict(size=9)),
        margin=dict(t=50,b=10))
    st.plotly_chart(fig_rad,width="stretch")

# ── TAB 4: EM CAMPO ──────────────────────────────────────────
with tabs[3]:
    st.markdown(f'<div class="section-label">{T["field_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{T["field_title"]}</div>',unsafe_allow_html=True)

    photos=T['photos']
    # separar por grupo (funciona nos 3 idiomas)
    fotos_cidade=[f for f in photos if f.get('gid')=='cidade']
    fotos_hotel=[f for f in photos if f.get('gid')=='hotel']
    foto_dest_melipon=next((f for f in fotos_cidade if f.get('destaque')),None)
    foto_dest_hotel=next((f for f in fotos_hotel if f.get('destaque_final')),None)
    fotos_cidade_norm=[f for f in fotos_cidade if not f.get('destaque')]
    fotos_hotel_norm=[f for f in fotos_hotel if not f.get('destaque_final')]

    def render_foto_card(foto):
        ex=os.path.exists(foto['path'])
        if ex:
            st.image(foto['path'],width="stretch")
        else:
            st.markdown(f"""<div class="photo-placeholder">
              <div class="photo-emoji">{foto['emoji']}</div>
              <div class="photo-title">{foto['titulo']}</div>
              <div class="photo-sp">{foto.get('esp','')}</div>
              <div class="photo-desc">{foto['desc']}</div>
              <div class="photo-path">{foto['path']}</div></div>""",unsafe_allow_html=True)
        st.markdown(f'<div class="photo-legenda">{foto["legenda"]}</div>',unsafe_allow_html=True)

    # GRUPO 1: Cidade das Abelhas
    st.markdown(f'<div style="font-size:.65rem;font-family:DM Mono;letter-spacing:2px;color:#C47D0E;text-transform:uppercase;margin-bottom:.5rem">{T['grp_city']}</div>',unsafe_allow_html=True)
    for i in range(0,len(fotos_cidade_norm),4):
        row=fotos_cidade_norm[i:i+4]
        cols=st.columns(len(row))
        for col,foto in zip(cols,row):
            with col: render_foto_card(foto)
        st.markdown("<br>",unsafe_allow_html=True)

    # Destaque: meliponário
    if foto_dest_melipon:
        st.markdown("---")
        st.markdown(f'<div class="section-label" style="color:#C47D0E">{T["dest_melipon"]}</div>',unsafe_allow_html=True)
        with st.container(key="photo-destaque"):
            render_foto_card(foto_dest_melipon)

    # GRUPO 2: Hotel de Abelhas FATEC
    st.markdown("---")
    st.markdown(f'<div style="font-size:.65rem;font-family:DM Mono;letter-spacing:2px;color:#2D5A32;text-transform:uppercase;margin-bottom:.5rem">{T['grp_hotel']}</div>',unsafe_allow_html=True)
    for i in range(0,len(fotos_hotel_norm),3):
        row=fotos_hotel_norm[i:i+3]
        cols=st.columns(len(row))
        for col,foto in zip(cols,row):
            with col: render_foto_card(foto)
        st.markdown("<br>",unsafe_allow_html=True)

    # Destaque final: hotel concluído
    if foto_dest_hotel:
        st.markdown("---")
        st.markdown(f'<div class="section-label" style="color:#2D5A32">{T["dest_hotel"]}</div>',unsafe_allow_html=True)
        with st.container(key="photo-destaque-final"):
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
        for serie,vals_s,cor_s in [(k,k,c) for k,c in [("Total","#C47D0E"),("iNaturalist","#5C3D1E"),("Meliponini","#C0390A"),("Xylocopa","#2D7A45")] if k in GBIF_RECORDS]:
            fig_gbif.add_trace(go.Scatter(x=ANOS_GBIF,y=GBIF_RECORDS[vals_s],mode='lines+markers',
                name={"Total":T['serie_total'],"iNaturalist":T['serie_inat']}.get(vals_s,vals_s),line=dict(color=cor_s,width=2.5),marker=dict(size=7),
                hovertemplate=f'<b>{vals_s}</b><br>%{{x}}: %{{y:,}}<extra></extra>'))
        fig_gbif.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(90,48,0,.03)',
            title=dict(text=T['trend_opt1'],font=dict(size=13,family=PLOT_SERIF)),
            font=dict(family=PLOT_FONT),height=400,
            xaxis=dict(showgrid=False),yaxis=dict(showgrid=True,gridcolor='#F0E8D0',title=T['records_axis']),
            legend=dict(orientation='h',yanchor='bottom',y=1.02),margin=dict(t=50,b=20))
        st.plotly_chart(fig_gbif,width="stretch")

    elif viz==T['trend_opt2']:
        sp_sorted=sorted(ESPECIES_SEMFERRAO,key=lambda x:x['registros_gbif'],reverse=True)
        fig_rank=go.Figure()
        for sp in sp_sorted:
            ameaca_cor={"VU":"#C0390A","LC":"#2D7A45"}.get(sp['ameaca'],sp['cor'])
            fig_rank.add_trace(go.Bar(x=[sp['nome']],y=[sp['registros_gbif']],
                marker_color=sp['cor'],opacity=.88,showlegend=False,
                text=[f"{sp['registros_gbif']:,}"],textposition='outside',
                textfont=dict(size=9,family=PLOT_MONO,color=sp['cor']),
                hovertemplate=f"<b>{sp['nome']}</b><br>{sp['registros_gbif']:,} {T['records_hover']}<br>IUCN: {sp['ameaca']}<extra></extra>"))
        fig_rank.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',
            title=dict(text=T['trend_opt2'],font=dict(size=13,family=PLOT_SERIF)),
            height=380,font=dict(family=PLOT_FONT),
            xaxis=dict(showgrid=False,tickangle=-30),
            yaxis=dict(showgrid=True,gridcolor='#F0E8D0'),margin=dict(t=50,b=20))
        st.plotly_chart(fig_rank,width="stretch")

    else:
        states_s=sorted(ESTADOS_DATA.keys(),key=lambda e:ESTADOS_DATA[e]['registros'],reverse=True)
        regs_s=[ESTADOS_DATA[e]['registros'] for e in states_s]
        cors_s=[{"Alta":"#C0390A","Média":"#C47D0E","Baixa":"#2D7A45"}.get(ESTADOS_DATA[e]['status'],"#888") for e in states_s]
        fig_est2=go.Figure(go.Bar(x=states_s,y=regs_s,marker_color=cors_s,opacity=.88,
            text=regs_s,textposition='outside',textfont=dict(size=9,family=PLOT_MONO),
            hovertemplate='<b>%{x}</b><br>%{y:,}<extra></extra>'))
        fig_est2.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',
            title=dict(text=T['trend_opt3'],font=dict(size=13,family=PLOT_SERIF)),
            height=380,font=dict(family=PLOT_FONT),
            xaxis=dict(showgrid=False,tickangle=-45),
            yaxis=dict(showgrid=True,gridcolor='#F0E8D0'),margin=dict(t=50,b=20))
        st.plotly_chart(fig_est2,width="stretch")

# ── TAB 6: PARÂMETROS ────────────────────────────────────────
with tabs[5]:
    st.markdown(f'<div class="section-label">{T["param_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{T["param_title"]}</div>',unsafe_allow_html=True)

    sp_sel=st.selectbox(T['param_sel'],[s['nome'] for s in ESPECIES_SEMFERRAO if s['nome'] in PARAMS_ESP],key="param_sp_sel")
    if sp_sel and sp_sel in PARAMS_ESP:
        p=PARAMS_ESP[sp_sel]
        sp_obj=next(s for s in ESPECIES_SEMFERRAO if s['nome']==sp_sel)
        cor_sp=sp_obj['cor']

        fig_param=go.Figure()
        param_key_sel=st.selectbox(T['param_detail'],list(T['param_names'].keys()),key="param_detail")
        pname=T['param_names'][param_key_sel]
        val=p.get(param_key_sel,0)
        all_vals=[PARAMS_ESP[s].get(param_key_sel,0) for s in PARAMS_ESP]
        all_sp=list(PARAMS_ESP.keys())
        cors_p=[next((s['cor'] for s in ESPECIES_SEMFERRAO if s['nome']==sn),"#888") for sn in all_sp]
        fig_param=go.Figure()
        fig_param.add_trace(go.Bar(x=all_sp,y=all_vals,marker_color=cors_p,opacity=.88,
            text=all_vals,textposition='outside',textfont=dict(size=9,family=PLOT_MONO),
            hovertemplate='<b>%{x}</b><br>%{y}<extra></extra>'))
        # Destacar selecionada
        idx=all_sp.index(sp_sel) if sp_sel in all_sp else -1
        if idx>=0:
            fig_param.add_shape(type="rect",x0=idx-.4,x1=idx+.4,y0=0,y1=all_vals[idx]*1.05,
                line=dict(color=cor_sp,width=3),fillcolor="rgba(0,0,0,0)")
        fig_param.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(90,48,0,.02)',
            title=dict(text=f"{pname} — {T['param_cmp']}",font=dict(size=13,family=PLOT_SERIF)),
            height=360,font=dict(family=PLOT_FONT),
            xaxis=dict(showgrid=False,tickangle=-30),
            yaxis=dict(showgrid=True,gridcolor='#F0E8D0',title=pname),
            margin=dict(t=50,b=20))
        st.plotly_chart(fig_param,width="stretch")

        # Card da espécie selecionada
        L=T['card_lbls']
        st.markdown(f"""
        <div class="info-card honey">
          <strong style="color:{cor_sp}">{sp_sel} ({sp_obj['cientifico']})</strong><br><br>
          <div style="font-size:.88rem;line-height:2.1;color:#5C2E00">
            {sp_t(sp_obj,'descricao')}<br><br>
            • <b>IUCN:</b> {sp_obj['ameaca']} · <b>{L['biome']}:</b> {sp_t(sp_obj,'bioma')} · <b>{L['region']}:</b> {sp_t(sp_obj,'regiao')}<br>
            • <b>{L['colony']}:</b> {p['colonia']:,} {L['workers']} · <b>{L['laying']}:</b> {p['postura_dia']} {L['eggs_day']}<br>
            • <b>{L['worker_life']}:</b> {p['vida_operaria']} {L['days']} · <b>{L['forage']}:</b> {p['longe_formag']} m<br>
            • <b>{L['honey']}:</b> {p['prod_mel_kg']} {L['kg_year']} · <b>{L['gen_dist']}:</b> {p['raio_dna_km']} km
          </div>
        </div>""",unsafe_allow_html=True)

# ── TAB 7: DADOS BRUTOS ──────────────────────────────────────
with tabs[6]:
    st.markdown(f'<div class="section-label">{T["raw_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{T["raw_title"]}</div>',unsafe_allow_html=True)

    C=T['raw_cols']
    rows_raw=[]
    for sp in ESPECIES_SEMFERRAO:
        p=PARAMS_ESP.get(sp['nome'],{})
        rows_raw.append({C['especie']:sp['nome'],C['cientifico']:sp['cientifico'],
            C['tamanho']:sp['tam'],C['raio']:sp['raio'],
            C['mel']:T['mel_vals'].get(sp['mel'],sp['mel']),C['iucn']:sp['ameaca'],C['bioma']:sp_t(sp,'bioma'),
            C['registros']:sp['registros_gbif'],
            C['colonia']:p.get('colonia','-'),C['mel_ano']:p.get('prod_mel_kg','-')})
    df_raw=pd.DataFrame(rows_raw)
    _mx=max([x['registros_gbif'] for x in ESPECIES_SEMFERRAO+ESPECIES_SOLITARIAS]+[1])
    st.dataframe(df_raw,width="stretch",height=460,
        column_config={C['registros']:st.column_config.ProgressColumn(C['registros'],min_value=0,max_value=_mx)})

    rows_sol=[]
    for sp in ESPECIES_SOLITARIAS:
        rows_sol.append({C['especie']:sp['nome'],C['cientifico']:sp['cientifico'],
            C['tamanho']:sp['tam'],C['habitat']:sp_t(sp,'habitat'),
            C['polinizacao']:sp_t(sp,'polinizacao'),C['registros']:sp['registros_gbif']})
    df_sol=pd.DataFrame(rows_sol)
    st.markdown(f"**{T['solitary_tbl']}**")
    st.dataframe(df_sol,width="stretch",height=260,
        column_config={C['registros']:st.column_config.ProgressColumn(C['registros'],min_value=0,max_value=_mx)})

    full_buf=io.StringIO()
    pd.concat([df_raw.assign(**{C['tipo']:T['tipo_vals']['meli']}),df_sol.assign(**{C['tipo']:T['tipo_vals']['sol']})]).to_csv(full_buf,index=False)
    st.download_button(T['download_csv'],full_buf.getvalue(),"abelhas_brasil_catalogo.csv","text/csv")

# ── TAB 8: FONTES ────────────────────────────────────────────
with tabs[7]:
    st.markdown(f'<div class="section-label">{T["sources_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{T["sources_title"]}</div>',unsafe_allow_html=True)
    fontes=T['sources']
    for sigla,nome,desc,cor in fontes:
        st.markdown(f"""<div class="info-card" style="border-left-color:{cor}">
          <div style="display:flex;align-items:flex-start;gap:1rem">
            <div style="background:{cor};color:white;font-family:'DM Mono','Noto Sans','Noto Sans SC','Noto Naskh Arabic',monospace;font-size:.6rem;padding:4px 7px;border-radius:4px;white-space:nowrap;flex-shrink:0;margin-top:2px;font-weight:bold;text-align:center;min-width:80px">{sigla}</div>
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
        🌐 <a href="https://amaurialmeida.github.io/environmental-portfolio/" style="color:var(--honey-light)">{T['footer_portfolio']}</a> &nbsp;|&nbsp;
        🐙 <a href="https://github.com/amaurialmeida" style="color:var(--honey-light)">GitHub</a></p>
      <p style="font-size:.75rem;opacity:.5;margin:0">{T['footer_copy']}</p>
    </div>""",unsafe_allow_html=True)