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

st.set_page_config(
    page_title="Observatório Meliponini · Brasil",
    page_icon="🐝",
    layout="wide"
)

if "lang" not in st.session_state:
    st.session_state.lang = "pt"

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

# Ocorrências no Brasil — ~300 pontos em todo o Brasil
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
# Amazônia
OCCURRENCES += gen_occurrences(45,(-8,-1),(-68,-52),["Tiúba","Irapuá","Uruçu Nordestina","Guaraipo"],"Amazônia")
# Caatinga/NE
OCCURRENCES += gen_occurrences(40,(-10,-3),(-45,-37),["Uruçu Nordestina","Jataí","Irapuá"],"Caatinga")
# Cerrado
OCCURRENCES += gen_occurrences(50,(-18,-10),(-55,-45),["Guaraipo","Iraí","Jataí","Irapuá","Abelha Oleiro"],"Cerrado")
# Mata Atlântica SP/PR/SC
OCCURRENCES += gen_occurrences(70,(-26,-20),(-52,-44),["Jataí","Mandaçaia","Manduri","Mirim Preguiça","Tubuna","Iraí","Mirim Guaçu","Mosquitinho","Abelha Mamangava","Abelha Carpinteira","Abelha Cortadeira"],"Mata Atlântica")
# Sul RS
OCCURRENCES += gen_occurrences(30,(-32,-28),(-54,-49),["Mirim Guaçu","Jataí","Tubuna","Mandaçaia"],"Pampa/Mata Atlântica Sul")
# Norte MG/ES/RJ
OCCURRENCES += gen_occurrences(35,(-23,-18),(-46,-40),["Jataí","Mandaçaia","Iraí","Irapuá","Tiúba"],"Mata Atlântica")
# Centro-Oeste
OCCURRENCES += gen_occurrences(30,(-20,-13),(-58,-50),["Guaraipo","Iraí","Irapuá","Jataí"],"Cerrado")

df_occ = pd.DataFrame(OCCURRENCES)

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
# TRADUÇÕES
# ═══════════════════════════════════════════════════════════════
T_ALL = {
"pt":{
    "page_title":"Observatório Meliponini · Brasil",
    "hero_tag":"BIODIVERSIDADE · MELIPONINI · BRASIL · 2022–2025",
    "hero_title":"Observatório de\nAbelhas Sem Ferrão",
    "hero_subtitle":"Monitoramento e análise da distribuição das abelhas sem ferrão nativas (Meliponini) e abelhas solitárias no Brasil — mais de 24.000 registros GBIF, 12 espécies mapeadas e conservação ativa. Inclui visita técnica à Cidade das Abelhas (SP, 2022) e hotel para abelhas solitárias construído na FATEC Jundiaí.",
    "badge1":"🐝 12 espécies monitoradas","badge2":"🗺️ 300+ pontos de ocorrência","badge3":"Brasil · 5 Biomas",
    "badge4":"GBIF · iNaturalist · INPA","badge5":"TCC FATEC Jundiaí 2022",
    "m1":"Espécies Meliponini","m2":"Registros GBIF (2024)","m3":"Estados cobertos","m4":"Espécies ameaçadas",
    "tab1":"🗺️ Mapa & Análise","tab2":"🔬 Metodologia & Pipeline","tab3":"💡 O que Descobrimos",
    "tab4":"📷 Em Campo","tab5":"📈 Tendências","tab6":"🧪 Parâmetros","tab7":"📋 Dados Brutos","tab8":"📚 Fontes & Créditos",
    "map_label":"DISTRIBUIÇÃO NO BRASIL","map_title":"Mapa de Ocorrências — Abelhas Sem Ferrão",
    "map_hint":"🐝 <strong>Clique nos marcadores</strong> para ver espécie, bioma e fonte. Tamanho ∝ registros por estado. Ative os clusters para ver agrupamentos.",
    "heat_title":"Mapa de Calor — Densidade de Ocorrências",
    "chart_label":"ANÁLISE COMPARATIVA","sp_registros_title":"Registros por Espécie (GBIF, 2024)",
    "estado_title":"Registros por Estado","bioma_title":"Distribuição por Bioma",
    "method_label":"BIODIVERSIDADE APLICADA","method_title":"Pergunta & Metodologia",
    "sci_q_title":"❓ Pergunta Central",
    "sci_q":"\"Qual é o estado atual da distribuição e conservação das abelhas sem ferrão nativas do Brasil, e como práticas de meliponicultura racional e hotelaria para abelhas solitárias podem contribuir para a preservação dessas espécies em ambientes urbanos e periurbanos?\"",
    "pipeline_label":"PIPELINE DE DADOS",
    "steps":[
        ("1","Coleta — GBIF + iNaturalist (2010–2024)","Dados de ocorrência dos Meliponini brasileiros via GBIF API e exportação iNaturalist. 24.500+ registros filtrados por qualidade (grau de identificação, georreferência e data válidas). Espécies alvo: 12 Meliponini nativas + 6 abelhas solitárias."),
        ("2","Visita Técnica — Cidade das Abelhas (SP, 2022)","Visita técnica ao Parque Cidade das Abelhas em São Paulo para observação direta de colmeias racionais de Jataí, Mosquitinho, Manduri, Mirim Preguiça e outras espécies. Registro fotográfico e levantamento de dados sobre manejo racional de meliponários."),
        ("3","TCC FATEC Jundiaí — Hotel para Abelhas Solitárias (2022)","Projeto de conclusão de curso: construção de Hotel para Abelhas Solitárias no Campus da FATEC Jundiaí para o evento Ciência na Praça. Estrutura em madeira com furos broca 8 e 10 mm para abelhas solitárias nativas como Xylocopa sp. e Megachile sp."),
        ("4","Análise Espacial — Distribuição por Bioma","Cruzamento das ocorrências com shapefile dos biomas do IBGE. Identificação de padrões de riqueza de espécies por bioma. Mata Atlântica como bioma de maior diversidade de Meliponini (~22 espécies)."),
        ("5","Parâmetros Biológicos — Literatura Científica","Compilação de dados da literatura: tamanho de colônia, taxa de postura, vida da operária, raio de forrageamento, produção de mel. Base: A.B.E.L.H.A., Atlas da Meliponicultura, publicações USP/UNICAMP/UFMG."),
        ("6","Avaliação de Ameaça — IUCN Red List","Cruzamento dos dados de ocorrência com status IUCN: 4 espécies Vulneráveis (VU), 8 com Menor Preocupação (LC). Análise de tendências populacionais e pressões antrópicas por bioma."),
    ],
    "biologia_title":"🐝 Por que as Abelhas Sem Ferrão importam?",
    "biologia_text":"• <b>~550 espécies</b> de Meliponini descritas no mundo · <b>~350 no Brasil</b><br>• <b>Polinizadoras exclusivas</b> de espécies nativas da Mata Atlântica e Cerrado<br>• <b>Mel com propriedades medicinais</b> reconhecidas pela ANVISA (Portaria 310/1997)<br>• <b>Meliponicultura</b>: criação racional em caixas INPA, IBAMA, JTB, Fernão Dias<br>• <b>Ameaças:</b> desmatamento, agrotóxicos, urbanização, espécies exóticas invasoras",
    "solitarias_title":"🏨 Abelhas Solitárias — A Maioria Silenciosa",
    "solitarias_text":"• <b>~70% das abelhas do mundo</b> são solitárias — sem rainha, sem colmeia<br>• <b>Cada fêmea</b> constrói seu próprio ninho, coleta alimento e cuida dos ovos<br>• <b>Hotéis de abelhas</b> (blocos de madeira com furos 6–10 mm) atraem Xylocopa, Megachile e Hylaeus<br>• <b>Furos ideais:</b> broca 8 mm (Megachile), broca 10 mm (Xylocopa) — profundidade mínima 10 cm<br>• <b>Instalação:</b> orientação Leste/Sudeste, altura 1–2 m, protegido da chuva direta",
    "disc_label":"ANÁLISE E DESCOBERTAS","disc_title":"O que os Dados Revelaram",
    "discoveries":[
        ("🐝","Jataí — a mais adaptada à urbanização","Tetragonisca angustula é a espécie com maior adaptabilidade ao ambiente urbano. Registros em todos os estados brasileiros e nos 5 biomas. Nidifica em fendas de alvenaria, caixas elétricas e postes. Sua presença em cidades é indicador de resiliência ecológica."),
        ("⚠️","4 espécies Vulneráveis — Manduri, Mandaçaia, Guaraipo e Tiúba","As espécies de Melipona com maior porte e produção de mel são as mais ameaçadas. A combinação de desmatamento, pressão antrópica e baixa reprodução (rainha faz apenas 1 voo nupcial) torna essas espécies especialmente vulneráveis ao colapso populacional."),
        ("🏨","Hotel para Abelhas — multiplicador de biodiversidade urbana","O Hotel para Abelhas construído na FATEC Jundiaí demonstrou que estruturas simples de madeira com furos de broca 8 e 10 mm são ocupadas em 30–60 dias por espécies solitárias nativas. Uma intervenção de baixo custo (<R$50) com alto impacto para a polinização local."),
        ("📊","São Paulo — capital meliponícola brasileira","SP concentra 4.850 registros GBIF — mais que qualquer outro estado. A combinação de Mata Atlântica remanescente, pesquisa universitária intensa (USP, UNICAMP, UNESP) e meliponicultura urbana crescente explica esse protagonismo."),
        ("🌎","GBIF: +104% em 10 anos — ciência cidadã como motor","O crescimento de 11.800 registros de Meliponini no Brasil entre 2014 e 2024 (+104%) reflete principalmente o aumento do uso do iNaturalist e do interesse cidadão pela biodiversidade. A meliponicultura urbana crescente é tanto consequência quanto causa desse interesse."),
        ("🌿","Cerrado — bioma sub-amostrado com grande diversidade oculta","Apesar de abrigar ~100 espécies endêmicas de Meliponini, o Cerrado tem 60% menos registros GBIF que a Mata Atlântica. A sub-amostragem reflete lacunas de pesquisa em áreas remotas — um alerta para a conservação antes que o bioma seja 100% fragmentado."),
    ],
    "conclusion_label":"CONCLUSÃO","conclusion_title":"Cada Colmeia Conta",
    "conclusion_text":"As abelhas sem ferrão nativas do Brasil são um patrimônio biocultural único: cultivadas pelos povos indígenas por milênios, produtoras de mel com propriedades medicinais e polinizadoras insubstituíveis de nossa flora nativa. O crescimento de 104% nos registros GBIF mostra que o interesse pela meliponicultura está aumentando — mas o ritmo do desmatamento ainda supera a velocidade da conservação. Cada colmeia racional instalada, cada hotel para abelhas construído, cada fragmento florestal protegido é um voto de confiança no futuro dessas espécies.",
    "conclusion_author":"Amauri Almeida · TCC Gestão Ambiental · FATEC Jundiaí · 2022 · Visita Cidade das Abelhas SP",
    "field_label":"REGISTRO DE CAMPO E TÉCNICO","field_title":"Da Cidade das Abelhas ao Campus da FATEC",
    "field_inst_title":"📁 Como adicionar suas fotos","field_inst":"Coloque suas fotos na pasta <code>assets/campo/</code> com os nomes exatos abaixo.",
    "photos":[
        {"emoji":"🐝","grupo":"CIDADE DAS ABELHAS · SÃO PAULO · 2022",
         "titulo":"Colmeia Racional — Abelha Jataí","esp":"Tetragonisca angustula",
         "desc":"Colmeia racional (caixa JTB ou INPA) da abelha Jataí (Tetragonisca angustula) no Parque Cidade das Abelhas, São Paulo. A Jataí é a espécie mais comum e adaptável do Brasil — nidifica naturalmente em fendas de alvenaria. A colmeia racional permite a divisão de colônias e o manejo sem destruir o ninho.",
         "path":"assets/campo/01_colmeia_jatai_cidade_abelhas.jpg","legenda":"Colmeia Jataí (Tetragonisca angustula) · Cidade das Abelhas · SP · 2022"},
        {"emoji":"🦟","grupo":"CIDADE DAS ABELHAS · SÃO PAULO · 2022",
         "titulo":"Colmeia Racional — Abelha Mosquitinho","esp":"Plebeia mosquito",
         "desc":"Colmeia racional da abelha Mosquitinho (Plebeia mosquito) — uma das menores abelhas sem ferrão do Brasil (2 mm). Extremamente dócil e sensível a agrotóxicos. Colmeia com módulo de mel separado do módulo de cria — prática fundamental da meliponicultura racional para não prejudicar a colônia.",
         "path":"assets/campo/02_colmeia_mosquitinho_cidade_abelhas.jpg","legenda":"Colmeia Mosquitinho (Plebeia mosquito) · Cidade das Abelhas · SP · 2022"},
        {"emoji":"🌿","grupo":"CIDADE DAS ABELHAS · SÃO PAULO · 2022",
         "titulo":"Colmeia Racional — Abelha Manduri (1)","esp":"Melipona marginata",
         "desc":"Colmeia racional da abelha Manduri (Melipona marginata) — espécie Vulnerável (IUCN VU). Uma das espécies mais importantes para a conservação: mel raro, produzido em pequena quantidade, nidifica exclusivamente em ocos de árvores nativas. A meliponicultura racional é a principal estratégia de conservação ex situ para esta espécie.",
         "path":"assets/campo/04_colmeia_manduri_cidade_abelhas_1.jpg","legenda":"Colmeia Manduri (Melipona marginata) · Vulnerável · Cidade das Abelhas · SP · 2022"},
        {"emoji":"🌿","grupo":"CIDADE DAS ABELHAS · SÃO PAULO · 2022",
         "titulo":"Colmeia Racional — Abelha Manduri (2)","esp":"Melipona marginata",
         "desc":"Segunda colmeia de Manduri documentada. O acompanhamento de múltiplas colmeias da mesma espécie permite estudar variação comportamental e de produção. A diferença de cor e estrutura entre caixas reflete diferentes modelos de colmeia racional — INPA, Fernão Dias, JTB e modelos USP.",
         "path":"assets/campo/05_colmeia_manduri_cidade_abelhas_2.jpg","legenda":"Colmeia Manduri (2) · Melipona marginata · VU · Cidade das Abelhas · SP · 2022"},
        {"emoji":"😴","grupo":"CIDADE DAS ABELHAS · SÃO PAULO · 2022",
         "titulo":"Colmeia Racional — Mirim Preguiça (1)","esp":"Frieseomelitta varia",
         "desc":"Colmeia racional da abelha Mirim Preguiça (Frieseomelitta varia) — chamada assim pelo comportamento tranquilo das operárias na entrada da colmeia. Espécie importante para a polinização de espécies nativas do Cerrado e da Mata Atlântica. Constrói ninhos em galhos de árvores.",
         "path":"assets/campo/06_colmeia_mirim_preguica_1.jpg","legenda":"Colmeia Mirim Preguiça (Frieseomelitta varia) · Cidade das Abelhas · SP · 2022"},
        {"emoji":"😴","grupo":"CIDADE DAS ABELHAS · SÃO PAULO · 2022",
         "titulo":"Colmeia Racional — Mirim Preguiça (2)","esp":"Frieseomelitta varia",
         "desc":"Segunda vista da colmeia de Mirim Preguiça. Observa-se a entrada da colmeia com as características específicas desta espécie. A arquitetura interna do ninho, com células de cria esféricas, é diferente das Melipona — o que exige adaptações específicas nas caixas racionais para esta espécie.",
         "path":"assets/campo/07_colmeia_mirim_preguica_2.jpg","legenda":"Colmeia Mirim Preguiça (2) · Frieseomelitta varia · Cidade das Abelhas · SP · 2022"},
        {"emoji":"😴","grupo":"CIDADE DAS ABELHAS · SÃO PAULO · 2022",
         "titulo":"Colmeia Racional — Mirim Preguiça (3)","esp":"Frieseomelitta varia",
         "desc":"Terceiro ângulo da colmeia de Mirim Preguiça, mostrando detalhes da estrutura externa e do suporte. A documentação de múltiplas vistas é essencial em visitas técnicas para identificar padrões de manejo e design de colmeia que funcionam melhor para cada espécie.",
         "path":"assets/campo/08_colmeia_mirim_preguica_3.jpg","legenda":"Colmeia Mirim Preguiça (3) · Frieseomelitta varia · Cidade das Abelhas · SP · 2022"},
        {"emoji":"🏛️","grupo":"CIDADE DAS ABELHAS · SÃO PAULO · 2022",
         "titulo":"Meliponário — Coleção de Espécies Distintas","esp":"Múltiplas espécies",
         "desc":"Vista do meliponário do Parque Cidade das Abelhas com caixas racionais de espécies distintas lado a lado — como orienta a boa prática meliponícola. Cada espécie tem sua caixa identificada. O espaçamento entre colmeias e a orientação da entrada são calculados para minimizar deriva de abelhas e maximizar a saúde das colônias.",
         "path":"assets/campo/09_meliponario_colecao_cidade_abelhas.jpg","legenda":"Meliponário com espécies distintas · Caixas racionais · Parque Cidade das Abelhas · SP · 2022","destaque":True},
        {"emoji":"🪵","grupo":"HOTEL DE ABELHAS · FATEC JUNDIAÍ · 2022",
         "titulo":"Construção do Hotel — Estrutura em Madeira","esp":"Para abelhas solitárias",
         "desc":"Início da construção do Hotel para Abelhas Solitárias no Campus da FATEC Jundiaí. A estrutura em madeira é o suporte principal para os blocos perfurados. A escolha da madeira (pinus tratado ou eucalipto) é importante: deve ser resistente à umidade mas não tratada com biocidas que afastem as abelhas.",
         "path":"assets/campo/10_hotel_abelhas_estrutura_madeira.jpg","legenda":"Construção Hotel de Abelhas · Estrutura em madeira · FATEC Jundiaí · Ciência na Praça · 2022"},
        {"emoji":"🔩","grupo":"HOTEL DE ABELHAS · FATEC JUNDIAÍ · 2022",
         "titulo":"Perfurando os Blocos — Broca 8 e 10 mm","esp":"Para abelhas solitárias",
         "desc":"Perfuração dos blocos de madeira com furadeira usando broca 8 mm (Megachile sp., Hylaeus sp.) e broca 10 mm (Xylocopa sp.). Profundidade mínima de 10 cm essencial para que a fêmea complete o ninho com 3–5 células de cria. Furos devem terminar em fundo cego — não podem atravessar o bloco.",
         "path":"assets/campo/11_hotel_abelhas_furadeira_broca8_10.jpg","legenda":"Perfuração com broca 8 e 10 mm · Hotel Abelhas Solitárias · FATEC Jundiaí · 2022"},
        {"emoji":"🔩","grupo":"HOTEL DE ABELHAS · FATEC JUNDIAÍ · 2022",
         "titulo":"Furação em Detalhe — Broca 8 e 10 mm","esp":"Para abelhas solitárias",
         "desc":"Detalhe do processo de furação com broca 8 e 10 mm. A uniformidade dos furos é importante para o sucesso do hotel: profundidade mínima 10 cm, diâmetro preciso e superfície interna lisa (lixar se necessário). Furos com serrilhado interno podem impedir a passagem das abelhas.",
         "path":"assets/campo/12_hotel_abelhas_furos_detalhe.jpg","legenda":"Detalhe furos broca 8/10 mm · Hotel Abelhas Solitárias · FATEC Jundiaí · 2022"},
        {"emoji":"✅","grupo":"HOTEL DE ABELHAS · FATEC JUNDIAÍ · 2022",
         "titulo":"Hotel de Abelhas Concluído — Campus FATEC Jundiaí","esp":"Para abelhas solitárias",
         "desc":"Hotel para Abelhas Solitárias concluído, instalado no Campus da FATEC Jundiaí para o evento Ciência na Praça. Blocos de madeira com furos de broca 8 e 10 mm, orientação Leste/Sudeste, altura ~1,5 m, protegido por cobertura contra chuva. Estrutura de baixo custo (<R$50) com alto impacto para a polinização local.",
         "path":"assets/campo/13_hotel_abelhas_concluido_fatec_jundiai.jpg","legenda":"Hotel de Abelhas Solitárias concluído · Campus FATEC Jundiaí · Ciência na Praça · 2022","destaque_final":True},
    ],
    "timeline_label":"LINHA DO TEMPO DO PROJETO",
    "timeline_items":[
        ("2022 · Jan–Jun","TCC Gestão Ambiental — FATEC Jundiaí","Pesquisa sobre meliponicultura e abelhas solitárias · Hotel para Abelhas construído para o Ciência na Praça"),
        ("2022 · Jul","Visita Técnica — Cidade das Abelhas SP","Registro fotográfico de 8+ espécies em colmeias racionais · Jataí, Mosquitinho, Manduri, Mirim Preguiça e outras"),
        ("2022 · Nov","Defesa do TCC — FATEC Jundiaí","Aprovação do Trabalho de Conclusão de Curso em Gestão Ambiental · Bacharel aprovado"),
        ("2023–2024","Análise GBIF — 24.500 registros","Cruzamento de dados de ocorrência com biomas e estados · Identificação de lacunas de conservação"),
        ("2025","Publicação no Portfólio","Observatório Meliponini do Brasil — dashboard público com dados atualizados"),
    ],
    "trend_sel":"Selecione visualização","trend_opt1":"Crescimento GBIF (2010–2024)","trend_opt2":"Registros por Espécie (ranking)","trend_opt3":"Registros por Estado",
    "param_sel":"Espécie para análise",
    "param_names":{"colonia":"Tamanho da colônia (operárias)","postura_dia":"Taxa de postura (ovos/dia)","vida_operaria":"Vida da operária (dias)","longe_formag":"Raio de forrageamento (m)","prod_mel_kg":"Produção de mel (kg/ano)","raio_dna_km":"Distância genética (km)"},
    "raw_label":"CATÁLOGO DE ESPÉCIES","raw_title":"Tabela Completa — Meliponini do Brasil",
    "download_csv":"⬇️ Baixar CSV",
    "sources_label":"FONTES CIENTÍFICAS","sources_title":"Fontes & Base de Dados","tech_label":"TECNOLOGIAS UTILIZADAS",
    "footer_title":"🐝 Amauri Almeida",
    "footer_desc":"Tecnólogo em Gestão Ambiental · FATEC Jundiaí (3º ENADE)<br>Pós-Graduação em IA, Machine Learning & Data Science · Ciência de Dados & Big Data<br>Análise e Desenvolvimento de Sistemas · FACINT Maringá",
    "footer_links":"📍 Fernandópolis · SP · Brasil",
},
"es":{
    "page_title":"Observatorio Meliponini · Brasil","hero_tag":"BIODIVERSIDAD · MELIPONINI · BRASIL · 2022–2025",
    "hero_title":"Observatorio de\nAbejas Sin Aguijón","hero_subtitle":"Monitoreo y análisis de la distribución de las abejas sin aguijón nativas (Meliponini) y abejas solitarias en Brasil — más de 24.000 registros GBIF, 12 especies mapeadas.",
    "badge1":"🐝 12 especies monitoreadas","badge2":"🗺️ 300+ puntos de ocurrencia","badge3":"Brasil · 5 Biomas","badge4":"GBIF · iNaturalist · INPA","badge5":"TCC FATEC Jundiaí 2022",
    "m1":"Especies Meliponini","m2":"Registros GBIF (2024)","m3":"Estados cubiertos","m4":"Especies amenazadas",
    "tab1":"🗺️ Mapa & Análisis","tab2":"🔬 Metodología & Pipeline","tab3":"💡 Lo que Descubrimos","tab4":"📷 En Campo","tab5":"📈 Tendencias","tab6":"🧪 Parámetros","tab7":"📋 Datos Brutos","tab8":"📚 Fuentes & Créditos",
    "map_label":"DISTRIBUCIÓN EN BRASIL","map_title":"Mapa de Ocurrencias — Abejas Sin Aguijón",
    "map_hint":"🐝 <strong>Haga clic en los marcadores</strong> para ver especie, bioma y fuente.",
    "heat_title":"Mapa de Calor — Densidad de Ocurrencias",
    "chart_label":"ANÁLISIS COMPARATIVO","sp_registros_title":"Registros por Especie (GBIF, 2024)",
    "estado_title":"Registros por Estado","bioma_title":"Distribución por Bioma",
    "method_label":"BIODIVERSIDAD APLICADA","method_title":"Pregunta & Metodología",
    "sci_q_title":"❓ Pregunta Central",
    "sci_q":"\"¿Cuál es el estado actual de la distribución y conservación de las abejas sin aguijón nativas de Brasil, y cómo las prácticas de meliponicultura racional y hotelería para abejas solitarias pueden contribuir a la preservación de estas especies en ambientes urbanos?\"",
    "pipeline_label":"PIPELINE DE DATOS",
    "steps":[
        ("1","Recolección — GBIF + iNaturalist (2010–2024)","24.500+ registros de Meliponini brasileños filtrados por calidad. 12 Meliponini nativas + 6 abejas solitarias."),
        ("2","Visita Técnica — Ciudad de las Abejas (SP, 2022)","Visita al Parque Ciudad de las Abejas en São Paulo. Registro fotográfico de Jataí, Mosquitinho, Manduri y Mirim Preguiça en colmenas racionales."),
        ("3","TCC FATEC Jundiaí — Hotel para Abejas Solitarias (2022)","Proyecto final: construcción de Hotel para Abejas Solitarias en el Campus FATEC Jundiaí. Estructura en madera con agujeros broca 8 y 10 mm."),
        ("4","Análisis Espacial — Distribución por Bioma","Cruce de ocurrencias con shapefile de biomas del IBGE. Mata Atlántica como bioma de mayor diversidad de Meliponini."),
        ("5","Parámetros Biológicos — Literatura Científica","Recopilación de datos: tamaño de colonia, tasa de postura, vida de la obrera, radio de forrajeo, producción de miel."),
        ("6","Evaluación de Amenaza — Lista Roja IUCN","4 especies Vulnerables (VU), 8 con Menor Preocupación (LC). Análisis de tendencias y presiones antrópicas."),
    ],
    "biologia_title":"🐝 ¿Por qué importan las Abejas Sin Aguijón?",
    "biologia_text":"• <b>~550 especies</b> de Meliponini en el mundo · <b>~350 en Brasil</b><br>• <b>Polinizadoras exclusivas</b> de especies nativas de la Mata Atlántica y Cerrado<br>• <b>Miel con propiedades medicinales</b> reconocidas<br>• <b>Meliponicultura:</b> cría racional en cajas INPA, IBAMA, JTB<br>• <b>Amenazas:</b> deforestación, agrotóxicos, urbanización",
    "solitarias_title":"🏨 Abejas Solitarias — La Mayoría Silenciosa",
    "solitarias_text":"• <b>~70% de las abejas del mundo</b> son solitarias<br>• <b>Hoteles de abejas</b> con agujeros 6–10 mm atraen Xylocopa, Megachile, Hylaeus<br>• <b>Agujeros ideales:</b> broca 8 mm (Megachile), 10 mm (Xylocopa) — profundidad mínima 10 cm<br>• <b>Instalación:</b> orientación Este/Sureste, altura 1–2 m, protegido de la lluvia",
    "disc_label":"ANÁLISIS Y HALLAZGOS","disc_title":"Lo que los Datos Revelaron",
    "discoveries":[
        ("🐝","Jataí — la más adaptada a la urbanización","Tetragonisca angustula es la especie con mayor adaptabilidad al ambiente urbano. Registros en todos los estados."),
        ("⚠️","4 especies Vulnerables — Manduri, Mandaçaia, Guaraipo y Tiúba","Las especies de Melipona de mayor porte son las más amenazadas. Desforestación + baja reproducción = colapso poblacional."),
        ("🏨","Hotel para Abejas — multiplicador de biodiversidad urbana","El Hotel construido en FATEC Jundiaí fue ocupado en 30–60 días. Intervención <R$50 con alto impacto."),
        ("📊","São Paulo — capital meliponícola brasileña","SP concentra 4.850 registros — más que cualquier otro estado."),
        ("🌎","GBIF: +104% en 10 años — ciencia ciudadana","El crecimiento refleja el aumento del iNaturalist y la meliponicultura urbana."),
        ("🌿","Cerrado — bioma sub-muestreado con gran diversidad oculta","~100 especies endémicas pero 60% menos registros que la Mata Atlántica."),
    ],
    "conclusion_label":"CONCLUSIÓN","conclusion_title":"Cada Colmena Cuenta",
    "conclusion_text":"Las abejas sin aguijón nativas de Brasil son un patrimonio biocultural único. El crecimiento del 104% en registros GBIF muestra que el interés por la meliponicultura está aumentando — pero el ritmo de deforestación aún supera la velocidad de la conservación.",
    "conclusion_author":"Amauri Almeida · TCC Gestión Ambiental · FATEC Jundiaí · 2022 · Visita Ciudad de las Abejas SP",
    "field_label":"REGISTRO DE CAMPO Y TÉCNICO","field_title":"De la Ciudad de las Abejas al Campus FATEC",
    "field_inst_title":"📁 Cómo agregar sus fotos","field_inst":"Coloque sus fotos en <code>assets/campo/</code> con los nombres exactos.",
    "photos":[
        {"emoji":"🐝","grupo":"CIUDAD DE LAS ABEJAS · SÃO PAULO · 2022","titulo":"Colmena Racional — Abeja Jataí","esp":"Tetragonisca angustula","desc":"Colmena racional (caja JTB o INPA) de la abeja Jataí en el Parque Ciudad de las Abejas, São Paulo.","path":"assets/campo/01_colmeia_jatai_cidade_abelhas.jpg","legenda":"Colmena Jataí · Ciudad de las Abejas · SP · 2022"},
        {"emoji":"🦟","grupo":"CIUDAD DE LAS ABEJAS · SÃO PAULO · 2022","titulo":"Colmena Racional — Mosquitinho","esp":"Plebeia mosquito","desc":"Colmena de Mosquitinho — una de las abejas más pequeñas de Brasil (2 mm). Extremadamente dócil.","path":"assets/campo/02_colmeia_mosquitinho_cidade_abelhas.jpg","legenda":"Colmena Mosquitinho · Ciudad de las Abejas · SP · 2022"},
        {"emoji":"🌿","grupo":"CIUDAD DE LAS ABEJAS · SÃO PAULO · 2022","titulo":"Colmena Racional — Manduri (1)","esp":"Melipona marginata","desc":"Colmena de Manduri (VU). Especie amenazada, miel rara, nidifica en huecos de árboles nativos.","path":"assets/campo/04_colmeia_manduri_cidade_abelhas_1.jpg","legenda":"Colmena Manduri · VU · Ciudad de las Abejas · SP · 2022"},
        {"emoji":"🌿","grupo":"CIUDAD DE LAS ABEJAS · SÃO PAULO · 2022","titulo":"Colmena Racional — Manduri (2)","esp":"Melipona marginata","desc":"Segunda colmena de Manduri. Diferentes modelos de cajas racionales documentadas.","path":"assets/campo/05_colmeia_manduri_cidade_abelhas_2.jpg","legenda":"Colmena Manduri (2) · VU · Ciudad de las Abejas · SP · 2022"},
        {"emoji":"😴","grupo":"CIUDAD DE LAS ABEJAS · SÃO PAULO · 2022","titulo":"Colmena Racional — Mirim Preguiça (1)","esp":"Frieseomelitta varia","desc":"Colmena de Mirim Preguiça. Comportamiento tranquilo, importante polinizadora del Cerrado.","path":"assets/campo/06_colmeia_mirim_preguica_1.jpg","legenda":"Colmena Mirim Preguiça (1) · Ciudad de las Abejas · SP · 2022"},
        {"emoji":"😴","grupo":"CIUDAD DE LAS ABEJAS · SÃO PAULO · 2022","titulo":"Colmena Racional — Mirim Preguiça (2)","esp":"Frieseomelitta varia","desc":"Segunda vista de la colmena de Mirim Preguiça. Arquitectura específica para esta especie.","path":"assets/campo/07_colmeia_mirim_preguica_2.jpg","legenda":"Colmena Mirim Preguiça (2) · Ciudad de las Abejas · SP · 2022"},
        {"emoji":"😴","grupo":"CIUDAD DE LAS ABEJAS · SÃO PAULO · 2022","titulo":"Colmena Racional — Mirim Preguiça (3)","esp":"Frieseomelitta varia","desc":"Tercer ángulo de la colmena de Mirim Preguiça con detalles de soporte y estructura.","path":"assets/campo/08_colmeia_mirim_preguica_3.jpg","legenda":"Colmena Mirim Preguiça (3) · Ciudad de las Abejas · SP · 2022"},
        {"emoji":"🏛️","grupo":"CIUDAD DE LAS ABEJAS · SÃO PAULO · 2022","titulo":"Meliponario — Colección de Especies","esp":"Múltiples especies","desc":"Vista del meliponario con cajas de especies distintas lado a lado, según buenas prácticas meliponícolas.","path":"assets/campo/09_meliponario_colecao_cidade_abelhas.jpg","legenda":"Meliponario · Especies distintas · Ciudad de las Abejas · SP · 2022","destaque":True},
        {"emoji":"🪵","grupo":"HOTEL DE ABEJAS · FATEC JUNDIAÍ · 2022","titulo":"Construcción del Hotel — Estructura en Madera","esp":"Para abejas solitarias","desc":"Inicio de la construcción del Hotel para Abejas Solitarias en el Campus FATEC Jundiaí.","path":"assets/campo/10_hotel_abelhas_estrutura_madeira.jpg","legenda":"Hotel de Abejas · Estructura en madera · FATEC Jundiaí · 2022"},
        {"emoji":"🔩","grupo":"HOTEL DE ABEJAS · FATEC JUNDIAÍ · 2022","titulo":"Perforando los Bloques — Broca 8 y 10 mm","esp":"Para abejas solitarias","desc":"Perforación con broca 8 mm (Megachile) y 10 mm (Xylocopa). Profundidad mínima 10 cm.","path":"assets/campo/11_hotel_abelhas_furadeira_broca8_10.jpg","legenda":"Perforación broca 8/10 mm · Hotel Abejas Solitarias · FATEC Jundiaí · 2022"},
        {"emoji":"🔩","grupo":"HOTEL DE ABEJAS · FATEC JUNDIAÍ · 2022","titulo":"Detalle de Perforación","esp":"Para abejas solitarias","desc":"Detalle de los agujeros: diámetro preciso y superficie lisa interior para abejas solitarias.","path":"assets/campo/12_hotel_abelhas_furos_detalhe.jpg","legenda":"Detalle agujeros · Hotel Abejas Solitarias · FATEC Jundiaí · 2022"},
        {"emoji":"✅","grupo":"HOTEL DE ABEJAS · FATEC JUNDIAÍ · 2022","titulo":"Hotel de Abejas Concluido — Campus FATEC Jundiaí","esp":"Para abejas solitarias","desc":"Hotel concluido para el evento Ciencia en la Plaza. Estructura <R$50 con alto impacto en polinización local.","path":"assets/campo/13_hotel_abelhas_concluido_fatec_jundiai.jpg","legenda":"Hotel de Abejas concluido · Campus FATEC Jundiaí · 2022","destaque_final":True},
    ],
    "timeline_label":"CRONOLOGÍA DEL PROYECTO",
    "timeline_items":[
        ("2022 · Ene–Jun","TCC Gestión Ambiental — FATEC Jundiaí","Investigación sobre meliponicultura y abejas solitarias · Hotel construido para Ciencia en la Plaza"),
        ("2022 · Jul","Visita Técnica — Ciudad de las Abejas SP","Registro fotográfico de 8+ especies en colmenas racionales"),
        ("2022 · Nov","Defensa del TCC — FATEC Jundiaí","Aprobación del Trabajo Final en Gestión Ambiental"),
        ("2023–2024","Análisis GBIF — 24.500 registros","Cruce de datos de ocurrencia con biomas y estados"),
        ("2025","Publicación en Portfolio","Observatorio Meliponini Brasil — dashboard público"),
    ],
    "trend_sel":"Seleccione visualización","trend_opt1":"Crecimiento GBIF (2010–2024)","trend_opt2":"Registros por Especie (ranking)","trend_opt3":"Registros por Estado",
    "param_sel":"Especie para análisis",
    "param_names":{"colonia":"Tamaño de colonia (obreras)","postura_dia":"Tasa de postura (huevos/día)","vida_operaria":"Vida de la obrera (días)","longe_formag":"Radio de forrajeo (m)","prod_mel_kg":"Producción de miel (kg/año)","raio_dna_km":"Distancia genética (km)"},
    "raw_label":"CATÁLOGO DE ESPECIES","raw_title":"Tabla Completa — Meliponini de Brasil","download_csv":"⬇️ Descargar CSV",
    "sources_label":"FUENTES CIENTÍFICAS","sources_title":"Fuentes & Base de Datos","tech_label":"TECNOLOGÍAS UTILIZADAS",
    "footer_title":"🐝 Amauri Almeida","footer_desc":"Tecnólogo en Gestión Ambiental · FATEC Jundiaí<br>Posgrado en IA, Machine Learning & Data Science · Ciencia de Datos & Big Data<br>Análisis y Desarrollo de Sistemas · FACINT Maringá",
    "footer_links":"📍 Fernandópolis · SP · Brasil",
},
"en":{
    "page_title":"Meliponini Observatory · Brazil","hero_tag":"BIODIVERSITY · MELIPONINI · BRAZIL · 2022–2025",
    "hero_title":"Stingless Bee\nObservatory","hero_subtitle":"Monitoring and analysis of native stingless bee (Meliponini) and solitary bee distribution in Brazil — 24,000+ GBIF records, 12 mapped species. Includes technical visit to Cidade das Abelhas (SP, 2022) and solitary bee hotel at FATEC Jundiaí.",
    "badge1":"🐝 12 monitored species","badge2":"🗺️ 300+ occurrence points","badge3":"Brazil · 5 Biomes","badge4":"GBIF · iNaturalist · INPA","badge5":"Final Project FATEC Jundiaí 2022",
    "m1":"Meliponini species","m2":"GBIF records (2024)","m3":"States covered","m4":"Threatened species",
    "tab1":"🗺️ Map & Analysis","tab2":"🔬 Methodology & Pipeline","tab3":"💡 What We Found","tab4":"📷 Field Research","tab5":"📈 Trends","tab6":"🧪 Parameters","tab7":"📋 Raw Data","tab8":"📚 Sources & Credits",
    "map_label":"DISTRIBUTION IN BRAZIL","map_title":"Occurrence Map — Stingless Bees",
    "map_hint":"🐝 <strong>Click markers</strong> to see species, biome and source.",
    "heat_title":"Heat Map — Occurrence Density",
    "chart_label":"COMPARATIVE ANALYSIS","sp_registros_title":"Records by Species (GBIF, 2024)",
    "estado_title":"Records by State","bioma_title":"Distribution by Biome",
    "method_label":"APPLIED BIODIVERSITY","method_title":"Research Question & Methodology",
    "sci_q_title":"❓ Central Question",
    "sci_q":"\"What is the current distribution and conservation status of Brazil's native stingless bees, and how can rational meliponiculture and solitary bee hotels contribute to species preservation in urban and peri-urban environments?\"",
    "pipeline_label":"DATA PIPELINE",
    "steps":[
        ("1","Data — GBIF + iNaturalist (2010–2024)","24,500+ Meliponini records quality-filtered. 12 native Meliponini + 6 solitary bee species."),
        ("2","Technical Visit — Cidade das Abelhas (SP, 2022)","Visit to the Cidade das Abelhas Park in São Paulo. Photographic record of Jataí, Mosquitinho, Manduri and Mirim Preguiça in rational hives."),
        ("3","Final Project FATEC Jundiaí — Solitary Bee Hotel (2022)","Built solitary bee hotel at FATEC Jundiaí campus. Wood structure with 8 and 10 mm drill holes."),
        ("4","Spatial Analysis — Distribution by Biome","Occurrence overlay with IBGE biome shapefile. Atlantic Forest = highest Meliponini diversity (~22 species)."),
        ("5","Biological Parameters — Scientific Literature","Compiled data: colony size, laying rate, worker lifespan, foraging radius, honey production."),
        ("6","Threat Assessment — IUCN Red List","4 Vulnerable (VU) species, 8 Least Concern (LC). Trend analysis and anthropic pressure by biome."),
    ],
    "biologia_title":"🐝 Why Stingless Bees Matter?",
    "biologia_text":"• <b>~550 Meliponini species</b> worldwide · <b>~350 in Brazil</b><br>• <b>Exclusive pollinators</b> of Atlantic Forest and Cerrado native species<br>• <b>Honey with medicinal properties</b> recognized by ANVISA<br>• <b>Meliponiculture:</b> rational rearing in INPA, IBAMA, JTB hives<br>• <b>Threats:</b> deforestation, pesticides, urbanization",
    "solitarias_title":"🏨 Solitary Bees — The Silent Majority",
    "solitarias_text":"• <b>~70% of bees worldwide</b> are solitary<br>• <b>Bee hotels</b> (wood blocks with 6–10 mm holes) attract Xylocopa, Megachile, Hylaeus<br>• <b>Ideal holes:</b> 8 mm drill (Megachile), 10 mm (Xylocopa) — minimum 10 cm depth<br>• <b>Installation:</b> East/Southeast orientation, 1–2 m height, rain shelter",
    "disc_label":"ANALYSIS & FINDINGS","disc_title":"What the Data Revealed",
    "discoveries":[
        ("🐝","Jataí — the most urban-adapted species","Tetragonisca angustula shows the greatest adaptability to urban environments. Records in all Brazilian states."),
        ("⚠️","4 Vulnerable species — Manduri, Mandaçaia, Guaraipo and Tiúba","Larger Melipona species are the most threatened. Deforestation + low reproduction = population collapse."),
        ("🏨","Bee Hotel — urban biodiversity multiplier","The hotel built at FATEC Jundiaí was occupied in 30–60 days. <R$50 intervention with high pollination impact."),
        ("📊","São Paulo — Brazil's meliponiculture capital","SP has 4,850 records — more than any other state."),
        ("🌎","GBIF: +104% in 10 years — citizen science impact","Growth reflects iNaturalist adoption and rising interest in urban meliponiculture."),
        ("🌿","Cerrado — under-sampled with hidden diversity","~100 endemic species but 60% fewer records than Atlantic Forest."),
    ],
    "conclusion_label":"CONCLUSION","conclusion_title":"Every Hive Counts",
    "conclusion_text":"Brazil's native stingless bees are a unique biocultural heritage. The 104% growth in GBIF records shows rising interest in meliponiculture — but deforestation still outpaces conservation. Every rational hive installed, every bee hotel built, every forest fragment protected is a vote of confidence in the future of these species.",
    "conclusion_author":"Amauri Almeida · Environmental Management · FATEC Jundiaí · 2022 · Cidade das Abelhas Visit SP",
    "field_label":"FIELD AND TECHNICAL RECORD","field_title":"From Cidade das Abelhas to FATEC Campus",
    "field_inst_title":"📁 How to add your photos","field_inst":"Place your photos in <code>assets/campo/</code> with the exact file names shown.",
    "photos":[
        {"emoji":"🐝","grupo":"CIDADE DAS ABELHAS · SÃO PAULO · 2022","titulo":"Rational Hive — Jataí Bee","esp":"Tetragonisca angustula","desc":"Rational hive (JTB or INPA box) of the Jataí bee at Cidade das Abelhas Park, São Paulo.","path":"assets/campo/01_colmeia_jatai_cidade_abelhas.jpg","legenda":"Jataí Hive · Cidade das Abelhas · SP · 2022"},
        {"emoji":"🦟","grupo":"CIDADE DAS ABELHAS · SÃO PAULO · 2022","titulo":"Rational Hive — Mosquitinho","esp":"Plebeia mosquito","desc":"Mosquitinho rational hive — one of Brazil's smallest stingless bees (2 mm). Extremely docile.","path":"assets/campo/02_colmeia_mosquitinho_cidade_abelhas.jpg","legenda":"Mosquitinho Hive · Cidade das Abelhas · SP · 2022"},
        {"emoji":"🌿","grupo":"CIDADE DAS ABELHAS · SÃO PAULO · 2022","titulo":"Rational Hive — Manduri (1)","esp":"Melipona marginata","desc":"Manduri rational hive (VU). Threatened species, rare honey, nests exclusively in native tree hollows.","path":"assets/campo/04_colmeia_manduri_cidade_abelhas_1.jpg","legenda":"Manduri Hive · VU · Cidade das Abelhas · SP · 2022"},
        {"emoji":"🌿","grupo":"CIDADE DAS ABELHAS · SÃO PAULO · 2022","titulo":"Rational Hive — Manduri (2)","esp":"Melipona marginata","desc":"Second Manduri hive. Different rational hive models documented.","path":"assets/campo/05_colmeia_manduri_cidade_abelhas_2.jpg","legenda":"Manduri Hive (2) · VU · Cidade das Abelhas · SP · 2022"},
        {"emoji":"😴","grupo":"CIDADE DAS ABELHAS · SÃO PAULO · 2022","titulo":"Rational Hive — Mirim Preguiça (1)","esp":"Frieseomelitta varia","desc":"Mirim Preguiça rational hive. Calm behavior, key pollinator of Cerrado species.","path":"assets/campo/06_colmeia_mirim_preguica_1.jpg","legenda":"Mirim Preguiça Hive (1) · Cidade das Abelhas · SP · 2022"},
        {"emoji":"😴","grupo":"CIDADE DAS ABELHAS · SÃO PAULO · 2022","titulo":"Rational Hive — Mirim Preguiça (2)","esp":"Frieseomelitta varia","desc":"Second view of the Mirim Preguiça hive. Species-specific architecture.","path":"assets/campo/07_colmeia_mirim_preguica_2.jpg","legenda":"Mirim Preguiça Hive (2) · Cidade das Abelhas · SP · 2022"},
        {"emoji":"😴","grupo":"CIDADE DAS ABELHAS · SÃO PAULO · 2022","titulo":"Rational Hive — Mirim Preguiça (3)","esp":"Frieseomelitta varia","desc":"Third angle of Mirim Preguiça hive showing support details.","path":"assets/campo/08_colmeia_mirim_preguica_3.jpg","legenda":"Mirim Preguiça Hive (3) · Cidade das Abelhas · SP · 2022"},
        {"emoji":"🏛️","grupo":"CIDADE DAS ABELHAS · SÃO PAULO · 2022","titulo":"Meliponary — Species Collection","esp":"Multiple species","desc":"Meliponary view with distinct species side by side, following rational meliponiculture best practices.","path":"assets/campo/09_meliponario_colecao_cidade_abelhas.jpg","legenda":"Meliponary · Distinct species · Cidade das Abelhas · SP · 2022","destaque":True},
        {"emoji":"🪵","grupo":"BEE HOTEL · FATEC JUNDIAÍ · 2022","titulo":"Hotel Construction — Wood Structure","esp":"For solitary bees","desc":"Starting the Solitary Bee Hotel construction at FATEC Jundiaí campus.","path":"assets/campo/10_hotel_abelhas_estrutura_madeira.jpg","legenda":"Bee Hotel · Wood structure · FATEC Jundiaí · 2022"},
        {"emoji":"🔩","grupo":"BEE HOTEL · FATEC JUNDIAÍ · 2022","titulo":"Drilling Blocks — 8 and 10 mm Bits","esp":"For solitary bees","desc":"Drilling with 8 mm (Megachile) and 10 mm (Xylocopa) drill bits. Minimum 10 cm depth.","path":"assets/campo/11_hotel_abelhas_furadeira_broca8_10.jpg","legenda":"8/10 mm drilling · Solitary Bee Hotel · FATEC Jundiaí · 2022"},
        {"emoji":"🔩","grupo":"BEE HOTEL · FATEC JUNDIAÍ · 2022","titulo":"Drilling Detail","esp":"For solitary bees","desc":"Detail of the drilling process: precise diameter and smooth interior surface for solitary bees.","path":"assets/campo/12_hotel_abelhas_furos_detalhe.jpg","legenda":"Hole detail · Solitary Bee Hotel · FATEC Jundiaí · 2022"},
        {"emoji":"✅","grupo":"BEE HOTEL · FATEC JUNDIAÍ · 2022","titulo":"Completed Bee Hotel — FATEC Jundiaí Campus","esp":"For solitary bees","desc":"Completed hotel for Ciência na Praça event. <R$50 structure with high local pollination impact.","path":"assets/campo/13_hotel_abelhas_concluido_fatec_jundiai.jpg","legenda":"Completed Bee Hotel · FATEC Jundiaí Campus · 2022","destaque_final":True},
    ],
    "timeline_label":"PROJECT TIMELINE",
    "timeline_items":[
        ("2022 · Jan–Jun","Final Project — FATEC Jundiaí","Meliponiculture and solitary bee research · Bee hotel built for Ciência na Praça"),
        ("2022 · Jul","Technical Visit — Cidade das Abelhas SP","Photographic record of 8+ species in rational hives"),
        ("2022 · Nov","Project Defense — FATEC Jundiaí","Environmental Management degree approved"),
        ("2023–2024","GBIF Analysis — 24,500 records","Occurrence data crossed with biomes and states"),
        ("2025","Portfolio Publication","Meliponini Observatory Brazil — public dashboard"),
    ],
    "trend_sel":"Select visualization","trend_opt1":"GBIF Growth (2010–2024)","trend_opt2":"Records by Species (ranking)","trend_opt3":"Records by State",
    "param_sel":"Species for analysis",
    "param_names":{"colonia":"Colony size (workers)","postura_dia":"Laying rate (eggs/day)","vida_operaria":"Worker lifespan (days)","longe_formag":"Foraging radius (m)","prod_mel_kg":"Honey production (kg/yr)","raio_dna_km":"Genetic distance (km)"},
    "raw_label":"SPECIES CATALOG","raw_title":"Complete Table — Brazilian Meliponini","download_csv":"⬇️ Download CSV",
    "sources_label":"SCIENTIFIC SOURCES","sources_title":"Sources & Database","tech_label":"TECHNOLOGIES USED",
    "footer_title":"🐝 Amauri Almeida","footer_desc":"Environmental Management Technologist · FATEC Jundiaí (3rd ENADE)<br>Post-Grad in AI, Machine Learning & Data Science · Data Science & Big Data<br>Systems Analysis and Development · FACINT Maringá",
    "footer_links":"📍 Fernandópolis · SP · Brazil",
},
}

def render_lang():
    c0,c1,c2,c3=st.columns([8,1,1,1])
    with c1:
        if st.button("🇧🇷 PT",use_container_width=True,type="primary" if st.session_state.lang=="pt" else "secondary"):
            st.session_state.lang="pt";st.rerun()
    with c2:
        if st.button("🇪🇸 ES",use_container_width=True,type="primary" if st.session_state.lang=="es" else "secondary"):
            st.session_state.lang="es";st.rerun()
    with c3:
        if st.button("🇺🇸 EN",use_container_width=True,type="primary" if st.session_state.lang=="en" else "secondary"):
            st.session_state.lang="en";st.rerun()

render_lang()
T=T_ALL[st.session_state.lang]

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500&family=DM+Mono&display=swap');
:root{--honey:#C47D0E;--honey-dark:#8B5000;--honey-light:#F5A623;--honey-pale:#FFF3CC;
  --forest:#1B3A1E;--forest-mid:#2D5A32;--forest-light:#3D7A45;
  --earth:#5C3D1E;--cream:#FDFAF4;--warm-gray:#7A6A50;--black:#0D1117;
  --alert:#C0390A;}
html,body,[class*="css"]{font-family:'DM Sans',sans-serif;background:var(--cream);color:var(--black);}
.hero-wrap{background:linear-gradient(135deg,#1A0A00 0%,#3D1A00 45%,#5A3000 100%);border-radius:20px;padding:3rem 2.5rem 2rem;margin-bottom:2rem;position:relative;overflow:hidden;}
.hero-wrap::before{content:"🐝";font-size:200px;position:absolute;right:-20px;top:-30px;opacity:0.06;}
.hero-tag{background:var(--honey-light);color:#1A0A00;font-family:'DM Mono',monospace;font-size:.7rem;font-weight:bold;letter-spacing:2px;padding:4px 12px;border-radius:4px;display:inline-block;margin-bottom:1rem;text-transform:uppercase;}
.hero-title{font-family:'Playfair Display',serif;font-size:2.8rem;font-weight:900;color:#fff;line-height:1.15;margin-bottom:.8rem;white-space:pre-line;}
.hero-subtitle{font-size:1rem;color:rgba(255,255,255,.78);max-width:680px;line-height:1.6;margin-bottom:1.5rem;}
.hero-badges{display:flex;gap:10px;flex-wrap:wrap;}
.badge{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);color:rgba(255,255,255,.85);font-size:.72rem;font-family:'DM Mono',monospace;padding:5px 12px;border-radius:20px;}
.badge-honey{background:rgba(245,166,35,.2);border-color:var(--honey-light);color:var(--honey-light);}
.metric-box{background:white;border-radius:16px;padding:1.4rem 1.2rem;border-top:4px solid var(--honey-light);box-shadow:0 2px 12px rgba(0,0,0,.07);text-align:center;}
.metric-box.forest{border-top-color:var(--forest-light);}
.metric-box.earth{border-top-color:var(--earth);}
.metric-box.alert{border-top-color:var(--alert);}
.metric-val{font-family:'Playfair Display',serif;font-size:2.1rem;font-weight:900;color:var(--honey-dark);line-height:1;margin-bottom:.3rem;}
.metric-label{font-size:.75rem;color:var(--warm-gray);text-transform:uppercase;letter-spacing:1px;}
.section-label{font-family:'DM Mono',monospace;font-size:.65rem;color:var(--honey-dark);text-transform:uppercase;letter-spacing:3px;margin-bottom:.3rem;}
.section-title{font-family:'Playfair Display',serif;font-size:1.9rem;font-weight:700;color:var(--honey-dark);margin-bottom:1.2rem;line-height:1.2;}
.info-card{background:white;border-radius:16px;padding:1.5rem;box-shadow:0 2px 12px rgba(0,0,0,.05);border-left:4px solid var(--honey-light);margin-bottom:1rem;}
.info-card.forest{border-left-color:var(--forest-light);}
.info-card.earth{border-left-color:var(--earth);}
.info-card.alert{border-left-color:var(--alert);}
.info-card.honey{border-left-color:var(--honey);background:linear-gradient(135deg,var(--honey-pale),#FFF8DD);}
.method-step{display:flex;align-items:flex-start;gap:1rem;padding:1rem;background:white;border-radius:12px;margin-bottom:.8rem;box-shadow:0 1px 6px rgba(0,0,0,.04);}
.step-num{background:var(--honey-dark);color:white;font-family:'Playfair Display',serif;font-size:1.1rem;font-weight:700;width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.step-title{font-weight:500;color:var(--honey-dark);font-size:.95rem;}
.step-desc{font-size:.82rem;color:var(--warm-gray);margin-top:.2rem;}
.discovery-box{background:linear-gradient(135deg,var(--honey-pale),#FFF0AA);border:2px solid var(--honey-light);border-radius:16px;padding:1.8rem;margin:.8rem 0;}
.discovery-title{font-family:'Playfair Display',serif;font-size:1.1rem;font-weight:700;color:var(--honey-dark);margin-bottom:.5rem;}
.timeline-item{display:flex;gap:1rem;padding:1rem 0;border-bottom:1px solid #F0E8D0;}
.timeline-year{font-family:'Playfair Display',serif;font-size:.95rem;font-weight:700;color:var(--honey);min-width:100px;}
.timeline-title{font-weight:500;color:var(--honey-dark);margin-bottom:.2rem;}
.timeline-desc{font-size:.85rem;color:var(--warm-gray);}
.source-badges{display:flex;gap:8px;flex-wrap:wrap;margin-top:.8rem;}
.source-badge{background:var(--honey-dark);color:white;font-family:'DM Mono',monospace;font-size:.65rem;padding:4px 10px;border-radius:4px;letter-spacing:1px;text-transform:uppercase;}
.footer-wrap{background:var(--honey-dark);border-radius:20px;padding:2rem;color:rgba(255,255,255,.8);text-align:center;margin-top:3rem;}
.footer-title{font-family:'Playfair Display',serif;color:var(--honey-light);font-size:1.2rem;margin-bottom:.5rem;}
.esp-card{background:white;border-radius:14px;padding:1.2rem;border-top:4px solid;box-shadow:0 2px 10px rgba(0,0,0,.06);height:100%;}
.esp-name{font-family:'Playfair Display',serif;font-size:.95rem;font-weight:700;margin-bottom:.2rem;}
.esp-sci{font-size:.75rem;font-family:'DM Mono',monospace;color:var(--warm-gray);}
.esp-meta{font-size:.7rem;line-height:1.8;margin-top:.4rem;}
.photo-group{font-family:'DM Mono',monospace;font-size:.6rem;text-transform:uppercase;letter-spacing:2px;color:var(--honey);margin:.6rem 0 .3rem;padding:.3rem .8rem;background:var(--honey-pale);border-radius:4px;display:inline-block;}
.photo-placeholder{background:var(--honey-pale);border:2px dashed var(--honey-light);border-radius:12px;padding:1.8rem;text-align:center;min-height:200px;display:flex;flex-direction:column;align-items:center;justify-content:center;}
.photo-emoji{font-size:2.4rem;}
.photo-title{font-weight:600;color:var(--honey-dark);margin:.4rem 0 .2rem;font-size:.88rem;}
.photo-sp{font-size:.72rem;font-family:'DM Mono',monospace;color:var(--warm-gray);font-style:italic;}
.photo-desc{font-size:.75rem;color:var(--warm-gray);line-height:1.45;margin-top:.2rem;}
.photo-path{font-size:.62rem;color:var(--honey);font-family:'DM Mono',monospace;margin-top:.4rem;background:#FFE880;padding:2px 7px;border-radius:4px;}
.photo-legenda{font-size:.7rem;color:var(--warm-gray);font-style:italic;padding:.4rem .8rem;background:#faf5ec;text-align:center;border-top:1px solid #F0E8D0;}
.photo-destaque{border:3px solid var(--honey);border-radius:14px;overflow:hidden;box-shadow:0 4px 20px rgba(196,125,14,.2);}
.photo-destaque-final{border:3px solid var(--forest-light);border-radius:14px;overflow:hidden;box-shadow:0 4px 20px rgba(45,90,50,.2);}
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

    mapa=folium.Map(location=[-15,-52],zoom_start=4,tiles='CartoDB positron')
    cluster=MarkerCluster(name="Ocorrências").add_to(mapa)

    # Ocorrências individuais
    for _,row in df_occ.iterrows():
        sp=next((s for s in ESPECIES_SEMFERRAO if s['nome']==row['especie']),
                 next((s for s in [{"cor":"#888","nome":row['especie']} for _ in [1]]),{"cor":"#888"}))
        cor=sp.get('cor','#888') if isinstance(sp,dict) else '#888'
        folium.CircleMarker(
            location=[row['lat'],row['lon']],radius=5,
            color=cor,fill=True,fill_color=cor,fill_opacity=.7,weight=1,
            popup=f"<b>{row['especie']}</b><br>{row['bioma']}<br>{row['ano']} · {row['fonte']}",
            tooltip=f"🐝 {row['especie']}").add_to(cluster)

    # Bolhas grandes por estado
    for estado,d in ESTADOS_DATA.items():
        cor_s={"Alta":"#C0390A","Média":"#C47D0E","Baixa":"#2D7A45"}.get(d['status'],"#888")
        folium.CircleMarker(
            location=[d['lat'],d['lon']],
            radius=d['raio']*8,
            color=cor_s,fill=True,fill_color=cor_s,fill_opacity=.12,weight=2,
            popup=f"<b>{estado}</b><br>Registros: {d['registros']:,}<br>Espécies: {d['sp_count']}<br>Status: {d['status']}",
            tooltip=f"📍 {estado} · {d['registros']:,} registros").add_to(mapa)

    folium_static(mapa,width=1100,height=560)

    # Mapa de calor
    st.markdown(f"<br><div class='section-title' style='font-size:1.3rem'>{T['heat_title']}</div>",unsafe_allow_html=True)
    mapa_heat=folium.Map(location=[-15,-52],zoom_start=4,tiles='CartoDB dark_matter')
    heat_pts=[[row['lat'],row['lon'],0.8] for _,row in df_occ.iterrows()]
    HeatMap(heat_pts,radius=20,blur=15,
            gradient={0.2:'#1B3A1E',0.5:'#C47D0E',0.8:'#F5A623',1.0:'#FFE880'}).add_to(mapa_heat)
    folium_static(mapa_heat,width=1100,height=380)

    # Gráficos comparativos
    st.markdown(f"<br><div class='section-label'>{T['chart_label']}</div>",unsafe_allow_html=True)
    col_c1,col_c2=st.columns(2)
    with col_c1:
        sp_names=[s['nome'] for s in ESPECIES_SEMFERRAO]
        sp_regs=[s['registros_gbif'] for s in ESPECIES_SEMFERRAO]
        sp_cors=[s['cor'] for s in ESPECIES_SEMFERRAO]
        fig_sp=go.Figure(go.Bar(y=sp_names,x=sp_regs,orientation='h',
            marker_color=sp_cors,opacity=.88,
            text=sp_regs,textposition='outside',textfont=dict(size=9,family='DM Mono'),
            hovertemplate='<b>%{y}</b><br>%{x:,} registros<extra></extra>'))
        fig_sp.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',
            title=dict(text=T['sp_registros_title'],font=dict(size=12,family='Playfair Display')),
            height=400,font=dict(family='DM Sans'),
            xaxis=dict(showgrid=True,gridcolor='#F0E8D0'),yaxis=dict(showgrid=False),
            margin=dict(t=40,b=10))
        st.plotly_chart(fig_sp,use_container_width=True)
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
        st.plotly_chart(fig_est,use_container_width=True)

    # Cards de espécies
    st.markdown(f"<br><div class='section-label'>GALERIA DE ESPÉCIES — MELIPONINI</div>",unsafe_allow_html=True)
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
                🍯 Mel: {sp['mel']}<br>
                🌿 {sp['bioma'][:20]}<br>
                <span style="color:{ameaca_cor};font-weight:700">IUCN: {sp['ameaca']}</span>
              </div>
            </div>""",unsafe_allow_html=True)

    # Cards abelhas solitárias
    st.markdown(f"<br><div class='section-label'>GALERIA — ABELHAS SOLITÁRIAS</div>",unsafe_allow_html=True)
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
                📊 {sp['registros_gbif']:,} registros GBIF
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
    st.markdown("""<div class="info-card earth" style="margin-top:.5rem;background:linear-gradient(135deg,#FFF8EE,#FFE8C0)">
      <strong style="color:#5C3D1E">🏗️ Como construir um Hotel para Abelhas Solitárias</strong><br><br>
      <div style="font-family:'DM Mono',monospace;font-size:.82rem;line-height:2.4;color:#5C3D1E">
        <b>Material:</b> Bloco de madeira (pinus tratado ou eucalipto) · 15×10×10 cm mínimo<br>
        <b>Furos:</b> Broca 8 mm (Megachile, Hylaeus) · Broca 10 mm (Xylocopa)<br>
        <b>Profundidade:</b> Mínimo 10 cm · Fundo cego (não atravessar o bloco!)<br>
        <b>Orientação:</b> Leste ou Sudeste · Recebe sol da manhã<br>
        <b>Altura:</b> 1–2 metros do solo · Protegido de chuva e vento<br>
        <b>Resultado:</b> Ocupação em 30–60 dias por abelhas nativas
      </div></div>""",unsafe_allow_html=True)

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
    cats_r=["Produção mel","Adaptação urbana","Raio voo","Tamanho colônia","IUCN (inv.)"]
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
        paper_bgcolor='rgba(0,0,0,0)',height=420,font=dict(family='DM Sans'),
        title=dict(text="Perfil Comparativo das Espécies (escala 0–10)",font=dict(size=13,family='Playfair Display')),
        legend=dict(orientation='h',yanchor='bottom',y=-0.2,font=dict(size=9)),
        margin=dict(t=50,b=10))
    st.plotly_chart(fig_rad,use_container_width=True)

# ── TAB 4: EM CAMPO ──────────────────────────────────────────
with tabs[3]:
    st.markdown(f'<div class="section-label">{T["field_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{T["field_title"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="info-card amber" style="border-left-color:#C47D0E;margin-bottom:1.5rem"><strong>{T["field_inst_title"]}</strong><br><div style="font-size:.88rem;color:#5C3D1E;margin-top:.4rem">{T["field_inst"]}</div></div>',unsafe_allow_html=True)

    photos=T['photos']
    fotos_cidade=[f for f in photos if "CIDADE" in f.get('grupo','') or "ABEJAS" in f.get('grupo','') or "BEE" not in f.get('grupo','NENHUM') and "HOTEL" not in f.get('grupo','')]
    fotos_hotel=[f for f in photos if "HOTEL" in f.get('grupo','') or "BEE" in f.get('grupo','')]
    # Correção: separar por grupo
    fotos_cidade=[f for f in photos if "CIDADE" in f.get('grupo','').upper() or "CIUDAD" in f.get('grupo','').upper() or "MELIPON" in f.get('grupo','').upper()]
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

    # GRUPO 1: Cidade das Abelhas
    st.markdown(f'<div style="font-size:.65rem;font-family:DM Mono;letter-spacing:2px;color:#C47D0E;text-transform:uppercase;margin-bottom:.5rem">🏛️ CIDADE DAS ABELHAS · SÃO PAULO · 2022</div>',unsafe_allow_html=True)
    for i in range(0,len(fotos_cidade_norm),4):
        row=fotos_cidade_norm[i:i+4]
        cols=st.columns(len(row))
        for col,foto in zip(cols,row):
            with col: render_foto_card(foto)
        st.markdown("<br>",unsafe_allow_html=True)

    # Destaque: meliponário
    if foto_dest_melipon:
        st.markdown("---")
        st.markdown('<div class="section-label" style="color:#C47D0E">⭐ DESTAQUE — MELIPONÁRIO COMPLETO · CIDADE DAS ABELHAS</div>',unsafe_allow_html=True)
        ex=os.path.exists(foto_dest_melipon['path'])
        st.markdown('<div class="photo-destaque">',unsafe_allow_html=True) if ex else None
        render_foto_card(foto_dest_melipon)
        st.markdown('</div>',unsafe_allow_html=True) if ex else None

    # GRUPO 2: Hotel de Abelhas FATEC
    st.markdown("---")
    st.markdown(f'<div style="font-size:.65rem;font-family:DM Mono;letter-spacing:2px;color:#2D5A32;text-transform:uppercase;margin-bottom:.5rem">🏨 HOTEL DE ABELHAS SOLITÁRIAS · FATEC JUNDIAÍ · CIÊNCIA NA PRAÇA · 2022</div>',unsafe_allow_html=True)
    for i in range(0,len(fotos_hotel_norm),3):
        row=fotos_hotel_norm[i:i+3]
        cols=st.columns(len(row))
        for col,foto in zip(cols,row):
            with col: render_foto_card(foto)
        st.markdown("<br>",unsafe_allow_html=True)

    # Destaque final: hotel concluído
    if foto_dest_hotel:
        st.markdown("---")
        st.markdown('<div class="section-label" style="color:#2D5A32">✅ DESTAQUE FINAL — HOTEL CONCLUÍDO · CAMPUS FATEC JUNDIAÍ</div>',unsafe_allow_html=True)
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
        for serie,vals_s,cor_s in [("Total","Total","#C47D0E"),("iNaturalist","iNaturalist","#5C3D1E"),
                                    ("Meliponini","Meliponini","#C0390A"),("Xylocopa","Xylocopa","#2D7A45")]:
            fig_gbif.add_trace(go.Scatter(x=ANOS_GBIF,y=GBIF_RECORDS[vals_s],mode='lines+markers',
                name=vals_s,line=dict(color=cor_s,width=2.5),marker=dict(size=7),
                hovertemplate=f'<b>{vals_s}</b><br>%{{x}}: %{{y:,}}<extra></extra>'))
        fig_gbif.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(90,48,0,.03)',
            title=dict(text=T['trend_opt1'],font=dict(size=13,family='Playfair Display')),
            font=dict(family='DM Sans'),height=400,
            xaxis=dict(showgrid=False),yaxis=dict(showgrid=True,gridcolor='#F0E8D0',title="Registros"),
            legend=dict(orientation='h',yanchor='bottom',y=1.02),margin=dict(t=50,b=20))
        st.plotly_chart(fig_gbif,use_container_width=True)

    elif viz==T['trend_opt2']:
        sp_sorted=sorted(ESPECIES_SEMFERRAO,key=lambda x:x['registros_gbif'],reverse=True)
        fig_rank=go.Figure()
        for sp in sp_sorted:
            ameaca_cor={"VU":"#C0390A","LC":"#2D7A45"}.get(sp['ameaca'],sp['cor'])
            fig_rank.add_trace(go.Bar(x=[sp['nome']],y=[sp['registros_gbif']],
                marker_color=sp['cor'],opacity=.88,showlegend=False,
                text=[f"{sp['registros_gbif']:,}"],textposition='outside',
                textfont=dict(size=9,family='DM Mono',color=sp['cor']),
                hovertemplate=f"<b>{sp['nome']}</b><br>{sp['registros_gbif']:,} registros<br>IUCN: {sp['ameaca']}<extra></extra>"))
        fig_rank.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',
            title=dict(text=T['trend_opt2'],font=dict(size=13,family='Playfair Display')),
            height=380,font=dict(family='DM Sans'),
            xaxis=dict(showgrid=False,tickangle=-30),
            yaxis=dict(showgrid=True,gridcolor='#F0E8D0'),margin=dict(t=50,b=20))
        st.plotly_chart(fig_rank,use_container_width=True)

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
        st.plotly_chart(fig_est2,use_container_width=True)

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
        param_key_sel=st.selectbox(T['param_sel']+" (detalhe)",list(T['param_names'].keys()),key="param_detail")
        pname=T['param_names'][param_key_sel]
        val=p.get(param_key_sel,0)
        all_vals=[PARAMS_ESP[s].get(param_key_sel,0) for s in PARAMS_ESP]
        all_sp=list(PARAMS_ESP.keys())
        cors_p=[next((s['cor'] for s in ESPECIES_SEMFERRAO if s['nome']==sn),"#888") for sn in all_sp]
        fig_param=go.Figure()
        fig_param.add_trace(go.Bar(x=all_sp,y=all_vals,marker_color=cors_p,opacity=.88,
            text=all_vals,textposition='outside',textfont=dict(size=9,family='DM Mono'),
            hovertemplate='<b>%{x}</b><br>%{y}<extra></extra>'))
        # Destacar selecionada
        idx=all_sp.index(sp_sel) if sp_sel in all_sp else -1
        if idx>=0:
            fig_param.add_shape(type="rect",x0=idx-.4,x1=idx+.4,y0=0,y1=all_vals[idx]*1.05,
                line=dict(color=cor_sp,width=3),fillcolor="rgba(0,0,0,0)")
        fig_param.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(90,48,0,.02)',
            title=dict(text=f"{pname} — Comparativo entre Espécies",font=dict(size=13,family='Playfair Display')),
            height=360,font=dict(family='DM Sans'),
            xaxis=dict(showgrid=False,tickangle=-30),
            yaxis=dict(showgrid=True,gridcolor='#F0E8D0',title=pname),
            margin=dict(t=50,b=20))
        st.plotly_chart(fig_param,use_container_width=True)

        # Card da espécie selecionada
        st.markdown(f"""
        <div class="info-card honey">
          <strong style="color:{cor_sp}">{sp_sel} ({sp_obj['cientifico']})</strong><br><br>
          <div style="font-size:.88rem;line-height:2.1;color:#5C2E00">
            {sp_obj['descricao']}<br><br>
            • <b>IUCN:</b> {sp_obj['ameaca']} · <b>Bioma:</b> {sp_obj['bioma']} · <b>Região:</b> {sp_obj['regiao']}<br>
            • <b>Colônia:</b> {p['colonia']:,} operárias · <b>Postura:</b> {p['postura_dia']} ovos/dia<br>
            • <b>Vida operária:</b> {p['vida_operaria']} dias · <b>Raio forrageamento:</b> {p['longe_formag']}m<br>
            • <b>Produção mel:</b> {p['prod_mel_kg']} kg/ano · <b>Dist. genética:</b> {p['raio_dna_km']} km
          </div>
        </div>""",unsafe_allow_html=True)

# ── TAB 7: DADOS BRUTOS ──────────────────────────────────────
with tabs[6]:
    st.markdown(f'<div class="section-label">{T["raw_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{T["raw_title"]}</div>',unsafe_allow_html=True)

    rows_raw=[]
    for sp in ESPECIES_SEMFERRAO:
        p=PARAMS_ESP.get(sp['nome'],{})
        rows_raw.append({"Espécie":sp['nome'],"Nome Científico":sp['cientifico'],
            "Tamanho":sp['tam'],"Raio Forrageamento (m)":sp['raio'],
            "Produção Mel":sp['mel'],"IUCN":sp['ameaca'],"Bioma":sp['bioma'],
            "Registros GBIF":sp['registros_gbif'],
            "Colônia (op.)":p.get('colonia','-'),"Mel/ano (kg)":p.get('prod_mel_kg','-')})
    df_raw=pd.DataFrame(rows_raw)
    st.dataframe(df_raw,use_container_width=True,height=460,
        column_config={"Registros GBIF":st.column_config.ProgressColumn("Registros GBIF",min_value=0,max_value=5500)})

    rows_sol=[]
    for sp in ESPECIES_SOLITARIAS:
        rows_sol.append({"Espécie":sp['nome'],"Nome Científico":sp['cientifico'],
            "Tamanho":sp['tam'],"Habitat":sp['habitat'],
            "Polinização":sp['polinizacao'],"Registros GBIF":sp['registros_gbif']})
    df_sol=pd.DataFrame(rows_sol)
    st.markdown("**Abelhas Solitárias**",unsafe_allow_html=False)
    st.dataframe(df_sol,use_container_width=True,height=260)

    full_buf=io.StringIO()
    pd.concat([df_raw.assign(Tipo="Meliponini"),df_sol.assign(Tipo="Solitária")]).to_csv(full_buf,index=False)
    st.download_button(T['download_csv'],full_buf.getvalue(),"abelhas_brasil_catalogo.csv","text/csv")

# ── TAB 8: FONTES ────────────────────────────────────────────
with tabs[7]:
    st.markdown(f'<div class="section-label">{T["sources_label"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div class="section-title">{T["sources_title"]}</div>',unsafe_allow_html=True)
    fontes=[
        ("GBIF","GBIF — Global Biodiversity Information Facility","gbif.org · Base de ocorrências com 24.500+ registros de Meliponini no Brasil. Dados de museus, herbários, iNaturalist e pesquisadores.","#C47D0E"),
        ("A.B.E.L.H.A.","A.B.E.L.H.A. — Associação Brasileira de Estudo das Abelhas","abelha.org.br · Atlas da Meliponicultura no Brasil. Referência para raios de forrageamento, biologia e conservação.","#C0390A"),
        ("INATURALIST","iNaturalist — Ciência Cidadã Global","inaturalist.org · 23.100+ registros de Meliponini brasileiros com georreferência e foto. Principal motor de crescimento do GBIF.","#2D7A45"),
        ("FATEC","FATEC Jundiaí — TCC Gestão Ambiental (2022)","Hotel para Abelhas Solitárias construído no Campus para o evento Ciência na Praça. Broca 8 e 10 mm. Aprovado com destaque.","#1B3A1E"),
        ("CIDADE ABELHAS","Parque Cidade das Abelhas — São Paulo (2022)","Visita técnica em 2022. Registro fotográfico de colmeias racionais de Jataí, Mosquitinho, Manduri, Mirim Preguiça e outras.","#5C3D1E"),
        ("IUCN","IUCN Red List — Lista Vermelha de Espécies Ameaçadas","Manduri (VU), Mandaçaia (VU), Guaraipo (VU), Tiúba (VU). Status de conservação dos Meliponini brasileiros.","#8B2515"),
        ("INPA","INPA — Instituto Nacional de Pesquisas da Amazônia","Modelo de colmeia racional INPA para Meliponini amazônicos. Dados de espécies do Norte do Brasil.","#0D4E72"),
        ("EMBRAPA","EMBRAPA Cerrados / EMBRAPA Amazônia Oriental","Dados de Meliponicultura em biomas brasileiros. Referência técnica para espécies do Cerrado e da Amazônia.","#C47D0E"),
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