import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import requests
import time
from datetime import datetime

# ============================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================
st.set_page_config(
    page_title="Observatório de Abelhas sem Ferrão - Brasil",
    page_icon="🐝",
    layout="wide"
)

# ============================================
# CABEÇALHO E REFERÊNCIAS
# ============================================
st.title("🐝 Observatório de Abelhas sem Ferrão - Brasil")
st.markdown("""
Distribuição de **Meliponini** (abelhas sem ferrão) por município, integrando dados do 
[GBIF](https://www.gbif.org) e [iNaturalist](https://www.inaturalist.org).
""")

with st.expander("📚 Sobre este observatório e fontes de dados"):
    st.markdown("""
    **Dados e Referências:**
    
    - **🌐 [GBIF - Global Biodiversity Information Facility](https://www.gbif.org)**:  
      Rede internacional que fornece acesso aberto a dados de biodiversidade. As ocorrências de abelhas sem ferrão são obtidas via API oficial.
    
    - **🐝 [A.B.E.L.H.A. - Associação Brasileira de Estudo das Abelhas](https://abelha.org.br)**:  
      Organização que promove a conservação das abelhas nativas. O observatório utiliza o [**Atlas da Meliponicultura no Brasil**](https://abelha.org.br/atlas-da-meliponicultura-no-brasil/) como referência para espécies manejadas por estado.
    
    - **📸 [iNaturalist](https://www.inaturalist.org)**:  
      Rede social de naturalistas e ciência cidadã. As observações de meliponíneos são integradas para complementar os registros do GBIF.
    
    **Metodologia:**
    1. Busca de ocorrências da tribo **Meliponini** (abelhas sem ferrão) no Brasil.
    2. Associação ao município mais próximo via coordenadas geográficas.
    3. Geração de mapa de bolhas (estilo COVID-19) com tamanho proporcional ao número de registros.
    
    *Dados atualizados a cada 24h via cache. O Atlas da A.B.E.L.H.A. lista 93 espécies com manejo no Brasil.*
    """)

# ============================================
# 1. CARREGAR COORDENADAS DOS MUNICÍPIOS
# ============================================
@st.cache_data
def load_municipios():
    """
    Dataset de municípios brasileiros (capitais + principais cidades).
    Fonte: IBGE e dados abertos.
    """
    dados = {
        'mun_id': list(range(1, 28)),
        'municipio': [
            'São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília', 'Salvador',
            'Fortaleza', 'Manaus', 'Curitiba', 'Recife', 'Porto Alegre', 'Belém',
            'Goiânia', 'Campinas', 'São Luís', 'Maceió', 'Natal', 'Campo Grande',
            'Cuiabá', 'João Pessoa', 'Teresina', 'Aracaju', 'Florianópolis',
            'Vitória', 'Porto Velho', 'Macapá', 'Rio Branco', 'Boa Vista'
        ],
        'latitude': [
            -23.5505, -22.9068, -19.9167, -15.8267, -12.9714,
            -3.7172, -3.1190, -25.4244, -8.0476, -30.0346, -1.4558,
            -16.6869, -22.9099, -2.5387, -9.6650, -5.7945, -20.4428,
            -15.5989, -7.1153, -5.0892, -10.9472, -27.5949,
            -20.3155, -8.7619, 0.0349, -9.9743, 2.8235
        ],
        'longitude': [
            -46.6333, -43.1729, -43.9345, -47.9218, -38.5108,
            -38.5434, -60.0217, -49.2473, -34.8770, -51.2177, -48.4902,
            -49.2641, -47.0626, -44.3028, -35.7349, -35.2110, -54.6465,
            -56.0949, -34.8627, -42.8018, -37.0731, -48.5482,
            -40.3122, -63.9020, -51.0522, -67.8100, -60.6758
        ],
        'estado_sigla': [
            'SP', 'RJ', 'MG', 'DF', 'BA', 'CE', 'AM', 'PR', 'PE', 'RS', 'PA',
            'GO', 'SP', 'MA', 'AL', 'RN', 'MS', 'MT', 'PB', 'PI', 'SE', 'SC',
            'ES', 'RO', 'AP', 'AC', 'RR'
        ]
    }
    
    df = pd.DataFrame(dados)
    return df

# ============================================
# 2. BUSCAR OCORRÊNCIAS VIA API DO GBIF
# ============================================
@st.cache_data(ttl=86400)  # atualiza a cada 24h
def fetch_gbif_data():
    """
    Busca ocorrências de Meliponini no Brasil via API do GBIF.
    """
    base_url = "https://api.gbif.org/v1/occurrence/search"
    
    # taxonKey para Apidae (família) - Meliponini é uma tribo dentro de Apidae
    params = {
        "country": "BR",
        "taxonKey": 141777,  # Apidae
        "hasCoordinate": "true",
        "limit": 300,
        "offset": 0
    }
    
    all_records = []
    
    with st.spinner("🔍 Buscando dados no GBIF..."):
        for offset in range(0, 3000, 300):
            params["offset"] = offset
            try:
                response = requests.get(base_url, params=params, timeout=30)
                response.raise_for_status()
                data = response.json()
                
                results = data.get("results", [])
                if not results:
                    break
                    
                all_records.extend(results)
                time.sleep(0.5)  # respeita rate limit da API
                
            except Exception as e:
                st.warning(f"Erro na busca GBIF (offset {offset}): {e}")
                break
    
    if not all_records:
        return pd.DataFrame()
    
    df = pd.DataFrame(all_records)
    
    # Filtrar apenas Meliponini por palavras-chave no nome científico
    meliponini_keywords = [
        'melipona', 'scaptotrigona', 'tetragonisca', 'frieseomelitta', 
        'plebeia', 'nannotrigona', 'partamona', 'trigona', 'meliponini',
        'cephalotrigona', 'leurotrigona', 'paratrigona', 'friesella'
    ]
    
    pattern = '|'.join(meliponini_keywords)
    df = df[df['scientificName'].str.lower().str.contains(pattern, na=False)]
    
    if 'decimalLatitude' in df.columns and 'decimalLongitude' in df.columns:
        df = df[['decimalLatitude', 'decimalLongitude', 'scientificName', 'stateProvince']]
        df.rename(columns={
            'decimalLatitude': 'latitude',
            'decimalLongitude': 'longitude',
            'stateProvince': 'estado'
        }, inplace=True)
        return df
    
    return pd.DataFrame()

# ============================================
# 3. BUSCAR OCORRÊNCIAS VIA iNATURALIST (API)
# ============================================
@st.cache_data(ttl=86400)
def fetch_inaturalist_data():
    """
    Busca observações de Meliponini no Brasil via API do iNaturalist.
    """
    base_url = "https://api.inaturalist.org/v1/observations"
    
    # Taxa ID para a tribo Meliponini (~171115) ou família Apidae (~47200)
    # Usaremos Apidae (47200) + filtro por nome
    params = {
        "taxon_id": 47200,  # Apidae
        "place_id": 703,    # Brasil (ID no iNaturalist)
        "has[]": "geo",
        "per_page": 200,
        "page": 1
    }
    
    all_observations = []
    
    with st.spinner("📸 Buscando dados no iNaturalist..."):
        for page in range(1, 6):  # busca até 5 páginas (1000 observações)
            params["page"] = page
            try:
                response = requests.get(base_url, params=params, timeout=30)
                response.raise_for_status()
                data = response.json()
                
                results = data.get("results", [])
                if not results:
                    break
                    
                for obs in results:
                    if obs.get('location') and obs.get('taxon', {}).get('name'):
                        # Verificar se é Meliponini por nome comum ou científico
                        scientific_name = obs['taxon'].get('name', '').lower()
                        common_name = str(obs['taxon'].get('preferred_common_name', '')).lower()
                        
                        if any(keyword in scientific_name or keyword in common_name 
                               for keyword in ['meliponini', 'melipona', 'scaptotrigona', 
                                              'tetragonisca', 'frieseomelitta', 'sem ferrão',
                                              'jataí', 'mandaguari', 'mandaçaia', 'tubuna']):
                            all_observations.append({
                                'latitude': obs['location'][0],
                                'longitude': obs['location'][1],
                                'scientificName': obs['taxon']['name'],
                                'estado': obs.get('place_guess', '')
                            })
                
                time.sleep(1)  # respeita rate limit
                
            except Exception as e:
                st.warning(f"Erro na busca iNaturalist (página {page}): {e}")
                break
    
    if not all_observations:
        return pd.DataFrame()
    
    df = pd.DataFrame(all_observations)
    return df

# ============================================
# 4. AGREGAR OCORRÊNCIAS POR MUNICÍPIO
# ============================================
@st.cache_data
def aggregate_by_municipality(occurrences_df, municipios_df):
    """
    Associa ocorrências ao município mais próximo via coordenadas arredondadas.
    """
    if occurrences_df.empty or municipios_df.empty:
        return pd.DataFrame()
    
    # Arredondar para 2 casas decimais (aproximadamente 1km de precisão)
    occurrences_df['lat_round'] = occurrences_df['latitude'].round(2)
    occurrences_df['lon_round'] = occurrences_df['longitude'].round(2)
    
    municipios_df['lat_round'] = municipios_df['latitude'].round(2)
    municipios_df['lon_round'] = municipios_df['longitude'].round(2)
    
    # Merge pelas coordenadas arredondadas
    merged = occurrences_df.merge(
        municipios_df,
        on=['lat_round', 'lon_round'],
        how='left'
    )
    
    # Contar ocorrências por município
    count_by_mun = merged.groupby(
        ['mun_id', 'municipio', 'estado_sigla', 'latitude', 'longitude']
    ).size().reset_index(name='total')
    
    return count_by_mun

# ============================================
# 5. CRIAR MAPA DE BOLHAS (ESTILO COVID)
# ============================================
def create_bubble_map(data_df):
    """
    Cria mapa com bolhas verdes, estilo mapa de óbitos da COVID.
    Sem labels de cidades para melhor performance.
    """
    if data_df.empty:
        m = folium.Map(location=[-14.2350, -51.9253], zoom_start=4)
        folium.Marker([-14.2350, -51.9253], popup="Sem dados").add_to(m)
        return m
    
    center_lat, center_lon = -14.2350, -51.9253
    
    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=4,
        tiles='CartoDB positron',  # fundo claro, similar ao COVID
        control_scale=True
    )
    
    max_count = data_df['total'].max()
    if max_count == 0:
        max_count = 1
    
    for _, row in data_df.iterrows():
        # Tamanho da bolha (mínimo 3px, máximo 18px)
        radius = 3 + (row['total'] / max_count) * 15
        
        # Intensidade da cor verde
        intensity = min(200, 100 + int((row['total'] / max_count) * 100))
        
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=radius,
            color='green',
            fill=True,
            fill_color=f'rgb(0, {intensity}, 0)',
            fill_opacity=0.7,
            weight=1,
            popup=f"""
                <b>{row['municipio']} - {row['estado_sigla']}</b><br>
                🐝 Registros: {row['total']}<br>
                📊 {(row['total']/max_count*100):.1f}% do máximo
            """,
            tooltip=f"{row['municipio']} ({row['total']} registros)"
        ).add_to(m)
    
    return m

# ============================================
# 6. ESPÉCIES SUGERIDAS POR ESTADO (ATLAS A.B.E.L.H.A.)
# ============================================
@st.cache_data
def load_atlas_species():
    """
    Dados resumidos do Atlas da Meliponicultura (A.B.E.L.H.A./ICMBio).
    Baseado no Catálogo Nacional de Abelhas-Nativas-Sem-Ferrão.
    """
    # Amostra de espécies com manejo por região (dados de referência)
    atlas_data = {
        'estado': ['SP', 'RJ', 'MG', 'BA', 'AM', 'PA', 'PR', 'SC', 'RS', 'GO', 'MT', 'MS'],
        'especies_principais': [
            'Jataí, Mandaguari, Mandaçaia, Tubuna',
            'Jataí, Iraí, Mirim',
            'Jataí, Mandaguari, Mandaçaia, Tubuna, Uruçu-boca-de-renda',
            'Jataí, Uruçu-amarela, Arapuá',
            'Jataí, Uruçu-boca-de-renda, Mandaçaia, Canudo',
            'Uruçu-amarela, Jandaíra, Tiúba, Mandaçaia',
            'Jataí, Mandaguari, Mandaçaia, Guaraipo',
            'Jataí, Mirim-preguiça, Guaraipo',
            'Jataí, Mandaguari, Guaraipo',
            'Jataí, Mandaçaia, Uruçu-amarela',
            'Jataí, Mandaguari, Uruçu-amarela',
            'Jataí, Mandaguari, Mandaçaia'
        ],
        'fonte': 'ICMBio - Catálogo Nacional de ANSF (Portaria nº 665/2021)'
    }
    
    df = pd.DataFrame(atlas_data)
    return df

# ============================================
# 7. EXECUÇÃO PRINCIPAL
# ============================================

# Carregar municípios
municipios = load_municipios()
if municipios.empty:
    st.error("❌ Não foi possível carregar os dados dos municípios.")
    st.stop()

# Carregar dados do Atlas (apenas para referência)
atlas_df = load_atlas_species()

# Buscar ocorrências (GBIF + iNaturalist)
occurrences_gbif = fetch_gbif_data()
occurrences_inat = fetch_inaturalist_data()

# Combinar fontes
occurrences = pd.concat([occurrences_gbif, occurrences_inat], ignore_index=True) if not occurrences_gbif.empty else occurrences_inat

if occurrences.empty:
    st.warning("⚠️ Nenhuma ocorrência de Meliponini encontrada nas bases de dados.")
    st.info("""
    💡 **Dica**: As APIs do GBIF e iNaturalist podem estar sobrecarregadas ou sem dados para os filtros atuais.
    
    - Consulte o [Atlas da Meliponicultura no Brasil](https://abelha.org.br/atlas-da-meliponicultura-no-brasil/) para ver a distribuição esperada.
    - Em breve, o observatório incluirá dados do [speciesLink (CRIA)](https://specieslink.net/) e do Sistema de Avaliação do Risco de Extinção (SALVE/ICMBio).
    """)
    
    # Mostrar mapa vazio mesmo sem dados
    mapa_vazio = folium.Map(location=[-14.2350, -51.9253], zoom_start=4)
    st_folium(mapa_vazio, width=900, height=600, use_container_width=True)
    
    # Mostrar dados do Atlas mesmo sem ocorrências
    with st.expander("📖 Espécies sugeridas pelo Atlas da Meliponicultura (A.B.E.L.H.A.)"):
        st.dataframe(atlas_df, use_container_width=True)
        st.caption("Fonte: ICMBio (Portaria nº 665/2021) e Catálogo de Abelhas Moure")
    
    st.stop()

# Remover duplicatas
occurrences = occurrences.drop_duplicates(subset=['latitude', 'longitude', 'scientificName'])

# Agregar por município
aggregated = aggregate_by_municipality(occurrences, municipios)

if aggregated.empty:
    st.warning("⚠️ Não foi possível associar ocorrências aos municípios.")
    st.stop()

# Filtrar apenas municípios com registros
aggregated = aggregated[aggregated['total'] > 0]

# ============================================
# 8. INTERFACE E VISUALIZAÇÕES
# ============================================

# Estatísticas em cards
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("📍 Municípios com registros", len(aggregated))
with col2:
    st.metric("🐝 Total de ocorrências", len(occurrences))
with col3:
    st.metric("🎯 Média por município", f"{aggregated['total'].mean():.1f}")
with col4:
    st.metric("📚 Fontes", "GBIF + iNaturalist")

# Mapa principal
st.markdown("---")
st.subheader("🗺️ Distribuição de Abelhas sem Ferrão por Município")
st.caption("📍 Cada bolha verde representa um município. Tamanho e intensidade indicam número de registros.")

mapa = create_bubble_map(aggregated)
st_folium(mapa, width=1000, height=650, use_container_width=True)

# Tabela de dados
with st.expander("📊 Dados detalhados por município"):
    st.dataframe(
        aggregated[['municipio', 'estado_sigla', 'total']].sort_values('total', ascending=False),
        use_container_width=True,
        column_config={
            'municipio': 'Município',
            'estado_sigla': 'UF',
            'total': 'Registros'
        }
    )
    
    csv = aggregated[['municipio', 'estado_sigla', 'total']].to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Baixar CSV",
        data=csv,
        file_name=f"abelhas_sem_ferrao_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )

# Seção do Atlas da Meliponicultura
with st.expander("📖 Espécies de abelhas sem ferrão por estado (Atlas A.B.E.L.H.A.)"):
    st.markdown("""
    Baseado no **Catálogo Nacional de Abelhas-Nativas-Sem-Ferrão** (ICMBio, Portaria nº 665/2021) e no 
    **Catálogo de Abelhas Moure** (atualizado em 2023).
    
    As espécies listadas abaixo são aquelas **com manejo conhecido** na meliponicultura brasileira, 
    selecionadas pelo Atlas da Meliponicultura da [A.B.E.L.H.A.](https://abelha.org.br/atlas-da-meliponicultura-no-brasil/).
    """)
    st.dataframe(atlas_df, use_container_width=True, hide_index=True)
    
    st.caption("""
    🔍 **Consulta avançada**: Acesse o [Atlas interativo](https://abelha.org.br/atlas-da-meliponicultura-no-brasil/) para:
    - Buscar por espécie (nome científico ou popular)
    - Ver distribuição geográfica por estado (fonte ICMBio ou Catálogo Moure)
    - Obter informações detalhadas via infoA.B.E.L.H.A. (sistema CRIA)
    """)

# Rodapé com referências
st.markdown("---")
st.markdown("""
**Fontes e créditos:**
- 🌐 Dados de ocorrência: [GBIF](https://www.gbif.org) (API) e [iNaturalist](https://www.inaturalist.org) (API)
- 📖 Referência de espécies: [A.B.E.L.H.A.](https://abelha.org.br) / [Atlas da Meliponicultura no Brasil](https://abelha.org.br/atlas-da-meliponicultura-no-brasil/) (ICMBio - Catálogo Nacional de ANSF)
- 🗺️ Municípios: IBGE (via dados abertos)
- 💾 Cache: Dados atualizados a cada 24h

"Pesquisa e investigação feito por Amauri Almeida para a comunidade de meliponicultores e pesquisadores."
""")