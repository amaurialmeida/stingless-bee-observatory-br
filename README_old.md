# 🐝 Observatório de Abelhas Sem Ferrão do Brasil

Um dashboard interativo desenvolvido em Streamlit para visualizar a distribuição de abelhas sem ferrão (Meliponini) no Brasil, com dados obtidos do GBIF (Global Biodiversity Information Facility).

## 📋 Características

- **Mapa Interativo**: Visualização de ocorrências de espécies por município com bolhas proporcionais
- **Círculos de Forrageamento**: Sobreposição de círculos representando o raio de voo de cada espécie
- **Gráficos Dinâmicos**: Distribuição por espécie, estado e heatmaps
- **Tabelas Detalhadas**: Dados completos com opção de download em CSV
- **Painel Informativo**: Informações sobre cada espécie (nome científico, raio de forrageamento, bioma, etc.)
- **Estatísticas**: Análise geográfica e comparativa das espécies

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- pip ou conda

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/bee-observatory-br.git
cd bee-observatory-br
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute o script de download de dados (primeira execução):
```bash
python download_gbif_data.py
python process_bee_data.py
```

5. Execute o aplicativo Streamlit:
```bash
streamlit run app_streamlit.py
```

O aplicativo abrirá automaticamente no navegador em `http://localhost:8501`

## 📊 Funcionalidades Principais

### 1. Mapa Interativo
- Visualização de todas as ocorrências de abelhas sem ferrão no Brasil
- Bolhas proporcionais ao número de registros por município
- Círculos de forrageamento sobrepostos mostrando o raio de voo de cada espécie
- Popup com informações ao clicar nos marcadores

### 2. Gráficos
- Distribuição por espécie (gráfico de barras)
- Distribuição por estado (gráfico de barras)
- Top 5 espécies (gráfico de pizza)
- Matriz de espécies vs estados (heatmap)

### 3. Tabelas
- Dados completos com filtros
- Resumo por município
- Opção de download em CSV

### 4. Informações sobre Espécies
- Nome científico
- Raio de forrageamento
- Descrição
- Biomas de ocorrência
- Distribuição geográfica

## 🐝 Espécies Incluídas

| Espécie | Nome Científico | Raio (m) | Distribuição |
|---------|-----------------|----------|--------------|
| Jataí | *Tetragonisca angustula* | 600 | Brasil inteiro |
| Mandaçaia | *Melipona quadrifasciata* | 2000 | Sudeste e Sul |
| Uruçu Nordestina | *Melipona scutellaris* | 2000 | Nordeste |
| Guaraipo | *Melipona bicolor* | 1500 | Centro-Oeste e Sudeste |
| Iraí | *Nannotrigona testaceicornis* | 500 | Sudeste |
| Irapuá | *Trigona spinipes* | 1000 | Brasil inteiro |
| Tubuna | *Scaptotrigona bipunctata* | 1000 | Sudeste |
| Mirim Guaçu | *Plebeia remota* | 500 | Sul e Sudeste |
| Tiúba | *Melipona fasciculata* | 2000 | Norte |
| Apis (Abelha de Mel) | *Apis mellifera* | 3000 | Brasil inteiro |

## 📈 Raios de Forrageamento

Os raios de forrageamento foram estimados com base em literatura científica:

- **Abelhas pequenas** (Jataí, Mirim, Iraí): 500-600m
- **Abelhas médias** (Irapuá, Tubuna): 1000m
- **Abelhas grandes** (Mandaçaia, Uruçu, Guaraipo, Tiúba): 1500-2000m
- **Apis mellifera**: 3000m

## 🔍 Fonte de Dados

Os dados de ocorrência são obtidos do **GBIF (Global Biodiversity Information Facility)**, que agrega informações de:
- Museus de História Natural
- Herbários
- Plataformas de ciência cidadã (iNaturalist)
- Pesquisadores e instituições

## 📝 Estrutura de Arquivos

```
bee-observatory-br/
├── app_streamlit.py           # Aplicativo principal
├── download_gbif_data.py      # Script para baixar dados do GBIF
├── process_bee_data.py        # Script para processar e enriquecer dados
├── requirements.txt           # Dependências Python
├── README.md                  # Este arquivo
├── meliponini_br_occurrences.csv  # Dados brutos do GBIF
└── processed_bee_data.csv     # Dados processados
```

## 🛠️ Tecnologias Utilizadas

- **Streamlit**: Framework web para data science
- **Folium**: Biblioteca para mapas interativos
- **Plotly**: Gráficos interativos
- **Pandas**: Manipulação de dados
- **GeoPandas**: Análise geoespacial
- **GBIF API**: Fonte de dados de biodiversidade

## 🚀 Deploy no Streamlit Cloud

1. Faça push do repositório para GitHub
2. Acesse [streamlit.io](https://streamlit.io)
3. Clique em "New app" e selecione seu repositório
4. Configure o branch e o arquivo principal (`app_streamlit.py`)
5. Deploy automático!

URL: `https://seu-usuario-bee-observatory-br.streamlit.app`

## 📚 Referências

- [GBIF - Global Biodiversity Information Facility](https://www.gbif.org)
- [A.B.E.L.H.A. - Associação Brasileira de Estudo das Abelhas](https://abelha.org.br)
- [Atlas da Meliponicultura no Brasil](https://abelha.org.br/atlas-da-meliponicultura-no-brasil/)
- [iNaturalist](https://www.inaturalist.org)

## 📄 Licença

Este projeto está sob licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👨‍💻 Autor

Desenvolvido como ferramenta de visualização e análise de dados de biodiversidade.

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor, abra uma issue ou pull request.

## 📞 Contato

Para dúvidas ou sugestões, entre em contato através de:
- Issues do GitHub
- Email: seu-email@exemplo.com

---

**Nota:** Este projeto é uma ferramenta educacional e de pesquisa. Os dados são atualizados regularmente conforme novas observações são registradas no GBIF.
