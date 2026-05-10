import streamlit as st
import pandas as pd
import folium
from folium import plugins
from streamlit_folium import st_folium
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from collections import Counter
import requests
import json

# Configuração da página
st.set_page_config(
    page_title="Observatório de Abelhas Sem Ferrão - Brasil",
    page_icon="🐝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #2d5016;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 0.5em;
    }
    .subtitle {
        text-align: center;
        color: #5a7c3e;
        font-size: 1.2em;
        margin-bottom: 2em;
    }
    .species-card {
        background-color: #f0f8e8;
        padding: 1.5em;
        border-radius: 10px;
        border-left: 5px solid #2d5016;
        margin-bottom: 1em;
    }
    .metric-box {
        background-color: #e8f5e9;
        padding: 1.5em;
        border-radius: 8px;
        text-align: center;
    }
    .metric-value {
        font-size: 2em;
        font-weight: bold;
        color: #2d5016;
    }
    .metric-label {
        color: #5a7c3e;
        font-size: 0.9em;
    }
</style>
""", unsafe_allow_html=True)

# Carregar dados
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('/home/ubuntu/processed_bee_data.csv')
        return df
    except FileNotFoundError:
        st.error("Arquivo de dados não encontrado. Execute o script de download primeiro.")
        return None

df = load_data()

if df is not None:
    # Título e descrição
    st.markdown('<h1 class="main-title">🐝 Observatório de Abelhas Sem Ferrão do Brasil</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Distribuição de espécies nativas por município e estado</p>', unsafe_allow_html=True)
    
    # Sidebar com filtros
    st.sidebar.title("🔍 Filtros")
    
    especies_unicas = sorted(df['nome_popular'].unique())
    especies_selecionadas = st.sidebar.multiselect(
        "Selecione as espécies:",
        especies_unicas,
        default=especies_unicas[:5]
    )
    
    df_filtrado = df[df['nome_popular'].isin(especies_selecionadas)]
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-value">{len(df_filtrado)}</div>
            <div class="metric-label">Registros de Ocorrência</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-value">{df_filtrado['nome_popular'].nunique()}</div>
            <div class="metric-label">Espécies</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-value">{df_filtrado['stateProvince'].nunique()}</div>
            <div class="metric-label">Estados</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-value">{df_filtrado['municipality'].nunique()}</div>
            <div class="metric-label">Municípios</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Abas principais
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🗺️ Mapa Interativo", "📊 Gráficos", "📋 Tabelas", "ℹ️ Espécies", "📈 Estatísticas"])
    
    # TAB 1: MAPA INTERATIVO
    with tab1:
        st.subheader("Mapa de Distribuição com Círculos de Forrageamento")
        
        # Criar mapa base (centrado no Brasil)
        mapa = folium.Map(
            location=[-14.2350, -51.9253],
            zoom_start=4,
            tiles="OpenStreetMap"
        )
        
        # Cores por espécie
        cores_especies = {
            'Jataí': '#FFD700',
            'Mandaçaia': '#0066CC',
            'Uruçu Nordestina': '#FF8C00',
            'Guaraipo': '#8B4513',
            'Iraí': '#808080',
            'Irapuá': '#000000',
            'Tubuna': '#800080',
            'Mirim Guaçu': '#008000',
            'Tiúba': '#FF0000',
            'Apis (Abelha de Mel)': '#FFD700'
        }
        
        # Agrupar dados por município para criar bolhas
        df_agrupado = df_filtrado.groupby(['municipality', 'stateProvince', 'decimalLatitude', 'decimalLongitude']).agg({
            'nome_popular': 'count',
            'species': lambda x: ', '.join(x.unique())
        }).reset_index()
        df_agrupado.columns = ['municipality', 'stateProvince', 'latitude', 'longitude', 'count', 'species']
        
        # Adicionar marcadores (bolhas) no mapa
        for idx, row in df_agrupado.iterrows():
            tamanho = min(max(row['count'] * 2, 5), 30)  # Tamanho proporcional ao número de registros
            
            popup_text = f"""
            <b>{row['municipality']}, {row['stateProvince']}</b><br>
            Registros: {row['count']}<br>
            Espécies: {row['species'][:100]}...
            """
            
            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=tamanho,
                popup=folium.Popup(popup_text, max_width=300),
                color='#2d5016',
                fill=True,
                fillColor='#5a7c3e',
                fillOpacity=0.7,
                weight=2
            ).add_to(mapa)
        
        # Adicionar círculos de forrageamento para espécies selecionadas
        if len(especies_selecionadas) > 0:
            # Pegar um ponto de cada espécie para mostrar o raio
            for especie in especies_selecionadas:
                df_especie = df_filtrado[df_filtrado['nome_popular'] == especie]
                if len(df_especie) > 0:
                    primeira_ocorrencia = df_especie.iloc[0]
                    raio = primeira_ocorrencia['raio_forrageamento']
                    
                    # Converter raio de metros para graus (aproximado)
                    raio_graus = raio / 111000
                    
                    cor = cores_especies.get(especie, '#808080')
                    
                    folium.Circle(
                        location=[primeira_ocorrencia['decimalLatitude'], primeira_ocorrencia['decimalLongitude']],
                        radius=raio,
                        popup=f"{especie}<br>Raio: {raio}m",
                        color=cor,
                        fill=True,
                        fillColor=cor,
                        fillOpacity=0.1,
                        weight=2,
                        dash_array='5, 5'
                    ).add_to(mapa)
        
        # Adicionar controle de camadas
        folium.LayerControl().add_to(mapa)
        
        st_folium(mapa, width=1400, height=600)
    
    # TAB 2: GRÁFICOS
    with tab2:
        col1, col2 = st.columns(2)
        
        with col1:
            # Gráfico de distribuição por espécie
            st.subheader("Distribuição por Espécie")
            df_especies = df_filtrado['nome_popular'].value_counts().reset_index()
            df_especies.columns = ['Espécie', 'Registros']
            
            fig = px.bar(
                df_especies,
                x='Espécie',
                y='Registros',
                color='Registros',
                color_continuous_scale='Greens',
                title="Número de Registros por Espécie"
            )
            fig.update_layout(height=400, xaxis_tickangle=-45)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Gráfico de distribuição por estado
            st.subheader("Distribuição por Estado")
            df_estados = df_filtrado['stateProvince'].value_counts().reset_index()
            df_estados.columns = ['Estado', 'Registros']
            
            fig = px.bar(
                df_estados,
                x='Estado',
                y='Registros',
                color='Registros',
                color_continuous_scale='Blues',
                title="Número de Registros por Estado"
            )
            fig.update_layout(height=400, xaxis_tickangle=-45)
            st.plotly_chart(fig, use_container_width=True)
        
        col3, col4 = st.columns(2)
        
        with col3:
            # Gráfico de pizza - Top 5 espécies
            st.subheader("Top 5 Espécies")
            top_5 = df_filtrado['nome_popular'].value_counts().head(5)
            
            fig = px.pie(
                values=top_5.values,
                names=top_5.index,
                title="Distribuição das 5 Espécies Mais Registradas"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col4:
            # Gráfico de calor - Espécies por Estado
            st.subheader("Matriz: Espécies vs Estados")
            df_cruzado = pd.crosstab(df_filtrado['nome_popular'], df_filtrado['stateProvince'])
            
            fig = px.imshow(
                df_cruzado,
                labels=dict(x="Estado", y="Espécie", color="Registros"),
                title="Heatmap de Ocorrências",
                color_continuous_scale="YlGn"
            )
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
    
    # TAB 3: TABELAS
    with tab3:
        st.subheader("Dados Detalhados de Ocorrências")
        
        # Tabela completa com filtro
        df_exibir = df_filtrado[['species', 'nome_popular', 'municipality', 'stateProvince', 'decimalLatitude', 'decimalLongitude', 'eventDate', 'raio_forrageamento']].copy()
        df_exibir.columns = ['Espécie Científica', 'Nome Popular', 'Município', 'Estado', 'Latitude', 'Longitude', 'Data', 'Raio Forrageamento (m)']
        
        st.dataframe(df_exibir, use_container_width=True, height=400)
        
        # Opção de download
        csv = df_exibir.to_csv(index=False)
        st.download_button(
            label="📥 Baixar dados em CSV",
            data=csv,
            file_name="abelhas_sem_ferrao_brasil.csv",
            mime="text/csv"
        )
        
        # Resumo por município
        st.subheader("Resumo por Município")
        df_municipios = df_filtrado.groupby('municipality').agg({
            'nome_popular': 'nunique',
            'decimalLatitude': 'first',
            'decimalLongitude': 'first'
        }).reset_index()
        df_municipios.columns = ['Município', 'Espécies', 'Latitude', 'Longitude']
        df_municipios = df_municipios.sort_values('Espécies', ascending=False)
        
        st.dataframe(df_municipios, use_container_width=True, height=400)
    
    # TAB 4: INFORMAÇÕES SOBRE ESPÉCIES
    with tab4:
        st.subheader("Informações sobre as Espécies")
        
        especies_info = {
            'Jataí': {
                'científico': 'Tetragonisca angustula',
                'raio': '500-600m',
                'descrição': 'Abelha muito pequena e dócil. Excelente para criação em áreas urbanas. Produz mel de alta qualidade.',
                'bioma': 'Pantanal, Cerrado, Mata Atlântica',
                'distribuição': 'Brasil inteiro'
            },
            'Mandaçaia': {
                'científico': 'Melipona quadrifasciata',
                'raio': '2000m',
                'descrição': 'Abelha robusta e produtiva. Excelente produtora de mel e pólen. Resistente a variações climáticas.',
                'bioma': 'Mata Atlântica, Cerrado',
                'distribuição': 'Sudeste e Sul do Brasil'
            },
            'Uruçu Nordestina': {
                'científico': 'Melipona scutellaris',
                'raio': '2000m',
                'descrição': 'Abelha grande e produtiva. Muito importante para a meliponicultura no Nordeste.',
                'bioma': 'Caatinga, Cerrado',
                'distribuição': 'Nordeste do Brasil'
            },
            'Guaraipo': {
                'científico': 'Melipona bicolor',
                'raio': '1500m',
                'descrição': 'Abelha de porte médio. Boa produtora de mel. Dócil e fácil de manejar.',
                'bioma': 'Cerrado, Mata Atlântica',
                'distribuição': 'Centro-Oeste e Sudeste'
            },
            'Iraí': {
                'científico': 'Nannotrigona testaceicornis',
                'raio': '500m',
                'descrição': 'Abelha muito pequena. Produz mel em pequenas quantidades mas de excelente qualidade.',
                'bioma': 'Mata Atlântica, Cerrado',
                'distribuição': 'Sudeste do Brasil'
            },
            'Irapuá': {
                'científico': 'Trigona spinipes',
                'raio': '1000m',
                'descrição': 'Abelha generalista e agressiva. Muito comum em áreas urbanas. Produz mel e própolis.',
                'bioma': 'Pantanal, Cerrado, Mata Atlântica',
                'distribuição': 'Brasil inteiro'
            },
            'Tubuna': {
                'científico': 'Scaptotrigona bipunctata',
                'raio': '1000m',
                'descrição': 'Abelha de porte médio. Agressiva e defensiva. Boa produtora de mel.',
                'bioma': 'Mata Atlântica, Cerrado',
                'distribuição': 'Sudeste do Brasil'
            },
            'Mirim Guaçu': {
                'científico': 'Plebeia remota',
                'raio': '500m',
                'descrição': 'Abelha pequena e dócil. Produz mel em pequenas quantidades. Fácil de criar.',
                'bioma': 'Mata Atlântica, Cerrado',
                'distribuição': 'Sul e Sudeste do Brasil'
            },
            'Tiúba': {
                'científico': 'Melipona fasciculata',
                'raio': '2000m',
                'descrição': 'Abelha grande e produtiva. Muito importante para a meliponicultura no Norte.',
                'bioma': 'Floresta Amazônica',
                'distribuição': 'Norte do Brasil'
            },
            'Apis (Abelha de Mel)': {
                'científico': 'Apis mellifera',
                'raio': '3000m',
                'descrição': 'Abelha exótica domesticada. Excelente produtora de mel e pólen. Muito importante economicamente.',
                'bioma': 'Adaptada a todos os biomas',
                'distribuição': 'Brasil inteiro'
            }
        }
        
        especie_selecionada = st.selectbox(
            "Selecione uma espécie para mais informações:",
            list(especies_info.keys())
        )
        
        if especie_selecionada:
            info = especies_info[especie_selecionada]
            
            st.markdown(f"""
            <div class="species-card">
                <h3>{especie_selecionada}</h3>
                <p><b>Nome Científico:</b> <i>{info['científico']}</i></p>
                <p><b>Raio de Forrageamento:</b> {info['raio']}</p>
                <p><b>Descrição:</b> {info['descrição']}</p>
                <p><b>Biomas:</b> {info['bioma']}</p>
                <p><b>Distribuição:</b> {info['distribuição']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Mostrar registros dessa espécie
            df_especie = df_filtrado[df_filtrado['nome_popular'] == especie_selecionada]
            st.write(f"**Registros desta espécie:** {len(df_especie)}")
            st.write(f"**Estados com registros:** {', '.join(df_especie['stateProvince'].unique())}")
            st.write(f"**Municípios:** {df_especie['municipality'].nunique()}")
    
    # TAB 5: ESTATÍSTICAS
    with tab5:
        st.subheader("Estatísticas Gerais")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("### Estatísticas Básicas")
            st.write(f"- **Total de registros:** {len(df_filtrado)}")
            st.write(f"- **Espécies únicas:** {df_filtrado['nome_popular'].nunique()}")
            st.write(f"- **Estados cobertos:** {df_filtrado['stateProvince'].nunique()}")
            st.write(f"- **Municípios:** {df_filtrado['municipality'].nunique()}")
            st.write(f"- **Período:** {df_filtrado['eventDate'].min()} a {df_filtrado['eventDate'].max()}")
        
        with col2:
            st.write("### Raios de Forrageamento (Média)")
            df_raios = df_filtrado.groupby('nome_popular')['raio_forrageamento'].mean().reset_index()
            df_raios.columns = ['Espécie', 'Raio Médio (m)']
            df_raios = df_raios.sort_values('Raio Médio (m)', ascending=False)
            
            for idx, row in df_raios.iterrows():
                st.write(f"- **{row['Espécie']}:** {row['Raio Médio (m)']:.0f}m")
        
        st.divider()
        
        # Gráfico de distribuição geográfica
        st.subheader("Distribuição Geográfica")
        
        fig = go.Figure()
        
        for especie in df_filtrado['nome_popular'].unique():
            df_esp = df_filtrado[df_filtrado['nome_popular'] == especie]
            fig.add_trace(go.Scattergeo(
                lon=df_esp['decimalLongitude'],
                lat=df_esp['decimalLatitude'],
                mode='markers',
                name=especie,
                marker=dict(size=8, opacity=0.7)
            ))
        
        fig.update_layout(
            geo=dict(
                scope='south america',
                projection_type='mercator',
                showland=True,
                landcolor='rgb(243, 243, 243)',
                coastcolor='rgb(204, 204, 204)',
            ),
            height=600,
            title="Distribuição Geográfica das Espécies"
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Informações sobre a fonte de dados
        st.divider()
        st.subheader("Sobre os Dados")
        st.write("""
        **Fonte:** Global Biodiversity Information Facility (GBIF)
        
        Os dados foram obtidos através da API do GBIF, que agrega informações de ocorrência de espécies 
        de diversos museus, herbários e plataformas de ciência cidadã como iNaturalist.
        
        **Raios de Forrageamento:** Os raios foram estimados com base em literatura científica e estudos 
        de comportamento de forrageamento das espécies.
        
        **Atualização:** Os dados são atualizados regularmente conforme novas observações são registradas 
        no GBIF.
        """)

else:
    st.error("Não foi possível carregar os dados. Verifique se os arquivos estão no diretório correto.")
