import pandas as pd
import json

# Dados de espécies e seus raios de forrageamento (em metros)
# Baseado na pesquisa e referências do usuário
bee_species = {
    "Jataí": {"scientific": "Tetragonisca angustula", "radius": 600},
    "Mandaçaia": {"scientific": "Melipona quadrifasciata", "radius": 2000},
    "Uruçu": {"scientific": "Melipona scutellaris", "radius": 2500},
    "Iraí": {"scientific": "Nannotrigona testaceicornis", "radius": 500},
    "Mombucão": {"scientific": "Cephalotrigona capitata", "radius": 1500},
    "Mandaguari": {"scientific": "Scaptotrigona postica", "radius": 1200},
    "Tubuna": {"scientific": "Scaptotrigona bipunctata", "radius": 1200},
    "Mirim": {"scientific": "Plebeia droryana", "radius": 400},
}

# Mapeamento de ocorrência por estado (simplificado para demonstração, baseado no Atlas)
# Em um cenário real, isso viria de um CSV completo.
occurrence = {
    "SP": ["Jataí", "Mandaçaia", "Iraí", "Mirim", "Mandaguari"],
    "PR": ["Jataí", "Mandaçaia", "Iraí", "Tubuna"],
    "SC": ["Jataí", "Mandaçaia", "Iraí"],
    "RS": ["Jataí", "Mirim", "Iraí"],
    "MG": ["Jataí", "Mandaçaia", "Uruçu", "Mombucão"],
    "BA": ["Uruçu", "Mombucão", "Jataí"],
    "AM": ["Mombucão", "Uruçu"],
    "PA": ["Mombucão"],
    "GO": ["Jataí", "Mandaguari"],
    "MT": ["Jataí", "Mombucão"],
    "MS": ["Jataí", "Mandaguari"],
    "RJ": ["Jataí", "Mandaçaia", "Iraí"],
    "ES": ["Jataí", "Mandaçaia", "Uruçu"],
}

# Carregar municípios e estados
municipios = pd.read_csv('municipios.csv')
# O CSV original do repo kelvins tem cabeçalho: codigo_ibge,nome,latitude,longitude,capital,codigo_uf,siafi_id,ddd,fuso_horario
municipios.columns = ['codigo_ibge', 'nome', 'lat', 'lon', 'capital', 'codigo_uf', 'siafi', 'ddd', 'fuso']
estados = pd.read_csv('estados.csv')

# Criar dicionário de UF
uf_map = estados.set_index('codigo_uf')['uf'].to_dict()
municipios['uf'] = municipios['codigo_uf'].map(uf_map)

# Filtrar apenas municípios que temos dados de ocorrência (para não sobrecarregar o mapa inicial)
# Vamos pegar as capitais e algumas cidades importantes para o exemplo
capitais = municipios[municipios['capital'] == 1].copy()

# Adicionar espécies para cada município baseado na UF
def get_species(row):
    return occurrence.get(row['uf'], ["Jataí"]) # Default Jataí se não houver dados

capitais['species'] = capitais.apply(get_species, axis=1)

# Preparar dados para o mapa
map_data = []
for _, row in capitais.iterrows():
    for sp_name in row['species']:
        sp_info = bee_species.get(sp_name, {"scientific": "Unknown", "radius": 500})
        map_data.append({
            "city": row['nome'],
            "uf": row['uf'],
            "lat": row['lat'],
            "lon": row['lon'],
            "species_name": sp_name,
            "scientific_name": sp_info['scientific'],
            "radius": sp_info['radius']
        })

# Salvar como JSON para o Streamlit
with open('bee_map_data.json', 'w', encoding='utf-8') as f:
    json.dump(map_data, f, ensure_ascii=False, indent=4)

print(f"Processados {len(map_data)} registros de ocorrência.")
