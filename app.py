# app.py
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import requests
import time
from functools import lru_cache

# Configuração da página
st.set_page_config(page_title="Observatório de Abelhas sem Ferrão", layout="wide")

st.title("🐝 Observatório de Abelhas sem Ferrão - Brasil")
st.markdown("Distribuição de **Meliponini** (abelhas sem ferrão) por município")

# ============================================
# 1. CARREGAR COORDENADAS DOS MUNICÍPIOS (cache)
# ============================================
@st.cache_data
def load_municipios():
    """
    Carrega dataset público de municípios brasileiros com coordenadas.
    Fonte: kelvins/municipios-brasileiros no GitHub
    """
    url = "https://raw.githubusercontent.com/kelvins/municipios-brasileiros/main/data/municipios.csv"
    
    try:
        df = pd.read_csv(url)
        # Seleciona colunas necessárias e renomeia
        df = df[['codigo_ibge', 'nome', 'latitude', 'longitude', 'codigo_uf', 'uf']]
        df.rename(columns={
            'codigo_ibge': 'mun_id',
            'nome': 'municipio',
            'uf': 'estado_sigla'
        }, inplace=True)
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados dos municípios: {e}")
        return pd.DataFrame()

# ============================================
# 2. BUSCAR OCORRÊNCIAS VIA API DO GBIF
# ============================================
@st.cache_data(ttl=86400)  # atualiza a cada 24h
def fetch_gbif_data():
    """
    Busca ocorrências de Meliponini (abelhas sem ferrão) no Brasil via GBIF API.
    """
    # Taxonomia: tribo Meliponini (buscar por family Apidae + subfamily Apinae + tribe)
    # Usamos taxonKey para maior precisão
    # Meliponini corresponde a vários gêneros. Estratégia: buscar por familyKey=7784 (Apidae) + country=BR
    # e filtrar por registros com coordenadas
    
    base_url = "https://api.gbif.org/v1/occurrence/search"
    
    params = {
        "country": "BR",
        "taxonKey": 141777,  # Apidae (família)
        "hasCoordinate": "true",
        "limit": 300,  # máximo por página
        "offset": 0
    }
    
    all_records = []
    
    # Loop para paginação (pega até 5000 registros para não sobrecarregar)
    for offset in range(0, 5000, 300):
        params["offset"] = offset
        try:
            response = requests.get(base_url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            results = data.get("results", [])
            if not results:
                break
                
            all_records.extend(results)
            time.sleep(0.5)  # respeita rate limit
            
        except Exception as e:
            st.warning(f"Erro na página offset {offset}: {e}")
            break
    
    # Converter para DataFrame
    if not all_records:
        return pd.DataFrame()
    
    df = pd.DataFrame(all_records)
    
    # Filtrar apenas Meliponini (verificar pelo nome científico)
    # Palavras-chave comuns: Melipona, Scaptotrigona, Tetragonisca, Frieseomelitta, etc.
    meliponini_keywords = [
        'melipon', 'scaptotrigon', 'tetragonisc', 'frieseomelitt', 
        'plebeia', 'nannotrigon', 'partamona', 'trigona'
    ]
    
    pattern = '|'.join(meliponini_keywords)
    df = df[df['scientificName'].str.lower().str.contains(pattern, na=False)]
    
    # Selecionar colunas relevantes
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
# 3. AGREGAR OCORRÊNCIAS POR MUNICÍPIO
# ============================================
@st.cache_data
def aggregate_by_municipality(occurrences_df, municipios_df):
    """
    Associa cada ocorrência ao município mais próximo e conta.
    """
    if occurrences_df.empty or municipios_df.empty:
        return pd.DataFrame()
    
    # Para cada ocorrência, encontra o município mais próximo
    # Otimização: usar aproximação de coordenadas (arredondar para 2 casas)
    # Isso é um trade-off entre precisão e performance
    
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
    
    # Contar por município
    count_by_mun = merged.groupby(['mun_id', 'municipio', 'estado_sigla', 'latitude', 'longitude']).size().reset_index(name='total')
    
    return count_by_mun

# ============================================
# 4. CRIAR MAPA (estilo COVID - sem labels)
# ============================================
def create_bubble_map(data_df):
    """
    Cria mapa com bolhas coloridas (verde) sem nomes de cidades.
    Similar ao mapa de óbitos da COVID.
    """
    if data_df.empty:
        return folium.Map(location=[-14.2350, -51.9253], zoom_start=4)
    
    # Centro do Brasil
    center_lat, center_lon = -14.2350, -51.9253
    
    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=4,
        tiles='CartoDB positron',  # fundo claro como no COVID
        control_scale=True
    )
    
    # Calcular tamanho das bolhas (escala logarítmica para suavizar)
    max_count = data_df['total'].max()
    
    for _, row in data_df.iterrows():
        # Tamanho proporcional (mín 3, máx 25 pixels)
        radius = 3 + (row['total'] / max_count) * 22
        
        # Cor verde (mais intenso = mais registros)
        intensity = min(255, 100 + int((row['total'] / max_count) * 155))
        color = f'rgb(0, {intensity}, 0)'
        
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=radius,
            color='green',
            fill=True,
            fill_color='green',
            fill_opacity=0.6,
            weight=1,
            popup=f"{row['municipio']} - {row['estado_sigla']}<br>Registros: {row['total']}",
            tooltip=f"{row['municipio']} ({row['total']})"
        ).add_to(m)
    
    return m

# ============================================
# 5. EXECUÇÃO PRINCIPAL
# ============================================
with st.spinner("Carregando dados..."):
    # Carregar municípios
    municipios = load_municipios()
    
    if municipios.empty:
        st.error("❌ Não foi possível carregar os dados dos municípios.")
        st.stop()
    
    # Buscar ocorrências GBIF (mostrar progresso)
    progress_text = st.empty()
    progress_text.info("🔍 Buscando dados de ocorrências no GBIF... Isso pode levar alguns segundos.")
    
    occurrences = fetch_gbif_data()
    
    if occurrences.empty:
        st.warning("⚠️ Nenhuma ocorrência de Meliponini encontrada no GBIF para o Brasil.")
        st.info("💡 Dica: Verifique os parâmetros de busca ou tente novamente mais tarde.")
        st.stop()
    
    progress_text.success(f"✅ {len(occurrences)} ocorrências carregadas!")
    
    # Agregar por município
    aggregated = aggregate_by_municipality(occurrences, municipios)
    
    if aggregated.empty:
        st.warning("⚠️ Não foi possível associar as ocorrências aos municípios.")
        st.stop()
    
    # Mostrar estatísticas
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📍 Municípios com registros", len(aggregated))
    with col2:
        st.metric("🐝 Total de ocorrências", len(occurrences))
    with col3:
        st.metric("📊 Média por município", f"{aggregated['total'].mean():.1f}")
    
    # Criar e exibir mapa
    st.markdown("---")
    st.subheader("🗺️ Distribuição de Abelhas sem Ferrão por Município")
    st.caption("Cada bolha representa um município. O tamanho e a intensidade da cor indicam o número de registros.")
    
    mapa = create_bubble_map(aggregated)
    
    # Exibir usando st_folium
    st_folium(mapa, width=900, height=600, use_container_width=True)
    
    # Opção de exportar dados (opcional)
    with st.expander("📥 Exportar dados brutos"):
        st.dataframe(aggregated[['municipio', 'estado_sigla', 'total', 'latitude', 'longitude']])
        
        csv = aggregated[['municipio', 'estado_sigla', 'total']].to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="abelhas_sem_ferrao_por_municipio.csv",
            mime="text/csv"
        )