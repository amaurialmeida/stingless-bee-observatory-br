import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import json

# Configuração da página
st.set_page_config(page_title="Observatório de Abelhas Sem Ferrão", layout="wide")

# Estilo CSS para o visual moderno e minimalista
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    h1, h2, h3 {
        color: #2c3e50;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🐝 Observatório de Abelhas Sem Ferrão do Brasil")
st.subheader("Mapa Interativo de Raios de Forrageamento")

# Carregar dados
@st.cache_data
def load_data():
    with open("bee_map_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

data = load_data()
df = pd.DataFrame(data)

# Sidebar para filtros
st.sidebar.header("Filtros")
selected_species = st.sidebar.multiselect(
    "Selecione as Espécies",
    options=sorted(df["species_name"].unique()),
    default=sorted(df["species_name"].unique())
)

# Filtrar dados
filtered_df = df[df["species_name"].isin(selected_species)]

# Layout principal
col1, col2 = st.columns([3, 1])

with col1:
    # Criar o mapa
    # Coordenadas centrais do Brasil
    m = folium.Map(location=[-15.78, -47.93], zoom_start=4, tiles="cartodbpositron")

    # Adicionar bolhas e círculos de forrageamento
    for _, row in filtered_df.iterrows():
        # Cor baseada na espécie (exemplo simples)
        color_map = {
            "Jataí": "#9b59b6", # Roxo (como no exemplo do COVID)
            "Mandaçaia": "#2ecc71", # Verde
            "Uruçu": "#e67e22", # Laranja
            "Iraí": "#3498db", # Azul
            "Mombucão": "#e74c3c", # Vermelho
        }
        color = color_map.get(row["species_name"], "#7f8c8d")

        # Círculo de Forrageamento (Raio real em metros)
        folium.Circle(
            location=[row["lat"], row["lon"]],
            radius=row["radius"],
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.2,
            popup=f"<b>{row["city"]} - {row["uf"]}</b><br>Espécie: {row["species_name"]}<br>Científico: <i>{row["scientific_name"]}</i><br>Raio: {row["radius"]}m",
            tooltip=f"{row["species_name"]} em {row["city"]}"
        ).add_to(m)

        # Bolha central (estilo COVID)
        folium.CircleMarker(
            location=[row["lat"], row["lon"]],
            radius=5,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.8,
            popup=f"<b>{row["city"]}</b><br>{row["species_name"]}"
        ).add_to(m)

    # Exibir o mapa
    st_folium(m, width="stretch", height=600, use_container_width=True)

with col2:
    st.write("### Informações")
    st.info("""
    Este mapa demonstra as regiões de ocorrência e o **raio de forrageamento** das abelhas sem ferrão.
    
    - **Bolhas:** Localização aproximada.
    - **Círculos:** Área de atuação da espécie (600m a 3km).
    """)
    
    st.write("### Estatísticas")
    st.metric("Espécies Selecionadas", len(selected_species))
    st.metric("Pontos de Observação", len(filtered_df))

    if not filtered_df.empty:
        st.write("### Detalhes")
        st.dataframe(filtered_df[["city", "uf", "species_name", "radius"]].rename(columns={
            "city": "Cidade", "uf": "UF", "species_name": "Espécie", "radius": "Raio (m)"
        }), hide_index=True)

st.markdown("---")
st.caption("Dados baseados no Atlas da Meliponicultura e Catálogo Moure. Estilo inspirado no painel COVID-19 Brasil.")
