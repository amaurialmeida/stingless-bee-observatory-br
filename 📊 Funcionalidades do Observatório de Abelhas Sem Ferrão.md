# 📊 Funcionalidades do Observatório de Abelhas Sem Ferrão

## Visão Geral

O Observatório de Abelhas Sem Ferrão é um dashboard interativo que permite visualizar, analisar e explorar a distribuição de espécies de abelhas nativas do Brasil. Desenvolvido em Streamlit, oferece uma experiência intuitiva e responsiva.

## 1. 🗺️ Mapa Interativo

### Características Principais

- **Visualização Geográfica**: Mapa do Brasil com todas as ocorrências de abelhas
- **Bolhas Proporcionais**: Tamanho das bolhas indica quantidade de registros por município
- **Interatividade**: Clique nos marcadores para ver informações detalhadas
- **Círculos de Forrageamento**: Sobreposição de círculos mostrando o raio de voo de cada espécie

### Como Usar

1. Selecione as espécies no painel lateral
2. Visualize os marcadores no mapa
3. Clique em qualquer bolha para ver:
   - Nome do município
   - Estado
   - Número de registros
   - Espécies presentes

### Raios de Forrageamento

Os círculos representam a distância máxima que cada espécie pode voar:

| Espécie | Raio |
|---------|------|
| Jataí | 600m |
| Mandaçaia | 2000m |
| Uruçu Nordestina | 2000m |
| Guaraipo | 1500m |
| Iraí | 500m |
| Irapuá | 1000m |
| Tubuna | 1000m |
| Mirim Guaçu | 500m |
| Tiúba | 2000m |
| Apis (Abelha de Mel) | 3000m |

## 2. 📊 Gráficos Dinâmicos

### Distribuição por Espécie

- Gráfico de barras mostrando número de registros por espécie
- Cores codificadas para fácil identificação
- Totalmente interativo com Plotly

### Distribuição por Estado

- Visualização de qual estado tem mais registros
- Identifica hotspots de biodiversidade
- Útil para pesquisa e conservação

### Top 5 Espécies

- Gráfico de pizza com as espécies mais registradas
- Percentual de representação
- Fácil identificação das espécies dominantes

### Heatmap: Espécies vs Estados

- Matriz visual mostrando presença de cada espécie em cada estado
- Cores indicam intensidade de registros
- Identifica padrões de distribuição

## 3. 📋 Tabelas de Dados

### Dados Completos

- Tabela com todos os registros filtrados
- Colunas: Espécie Científica, Nome Popular, Município, Estado, Coordenadas, Data, Raio Forrageamento
- Busca e filtro integrados
- Scroll horizontal para todas as colunas

### Resumo por Município

- Tabela agregada por município
- Mostra número de espécies por localidade
- Coordenadas para referência geográfica
- Ordenação por número de espécies

### Download de Dados

- Botão para baixar dados em formato CSV
- Compatível com Excel, Google Sheets, Python, etc.
- Útil para análise externa

## 4. ℹ️ Painel Informativo sobre Espécies

### Informações Detalhadas

Para cada espécie, o painel mostra:

- **Nome Popular**: Nome comum no Brasil
- **Nome Científico**: Nomenclatura binomial
- **Raio de Forrageamento**: Distância máxima de voo
- **Descrição**: Características e comportamento
- **Biomas**: Ambientes onde ocorrem
- **Distribuição Geográfica**: Estados onde são encontradas

### Exemplos de Espécies

#### Jataí (*Tetragonisca angustula*)
- Abelha muito pequena e dócil
- Excelente para criação em áreas urbanas
- Produz mel de alta qualidade
- Distribuição: Brasil inteiro

#### Mandaçaia (*Melipona quadrifasciata*)
- Abelha robusta e produtiva
- Excelente produtora de mel e pólen
- Resistente a variações climáticas
- Distribuição: Sudeste e Sul do Brasil

#### Uruçu Nordestina (*Melipona scutellaris*)
- Abelha grande e produtiva
- Muito importante para meliponicultura no Nordeste
- Grande potencial econômico
- Distribuição: Nordeste do Brasil

## 5. 📈 Estatísticas Gerais

### Métricas Principais

- **Total de Registros**: Número total de ocorrências
- **Espécies Únicas**: Quantas espécies diferentes foram registradas
- **Estados Cobertos**: Quantos estados têm registros
- **Municípios**: Quantos municípios têm dados
- **Período**: Intervalo de datas dos registros

### Raios de Forrageamento Médios

- Tabela com raio médio de cada espécie
- Ordenação decrescente
- Útil para planejamento de conservação

### Distribuição Geográfica

- Mapa de dispersão global das espécies
- Cada espécie em cor diferente
- Visualização de padrões de distribuição

## 6. 🔍 Filtros e Controles

### Painel Lateral

- **Seleção de Espécies**: Multiselect para escolher quais espécies visualizar
- **Atualização em Tempo Real**: Todos os gráficos e mapas atualizam instantaneamente
- **Pré-seleção**: As 5 primeiras espécies vêm pré-selecionadas

### Abas Principais

- **Mapa Interativo**: Visualização geográfica
- **Gráficos**: Análise visual dos dados
- **Tabelas**: Dados detalhados
- **Espécies**: Informações sobre cada espécie
- **Estatísticas**: Análise agregada

## 7. 🎨 Design e Usabilidade

### Tema Visual

- Paleta de cores verde (tema de biodiversidade)
- Cores harmoniosas e acessíveis
- Ícones intuitivos em cada seção

### Responsividade

- Funciona em desktop, tablet e mobile
- Layout adaptativo
- Mapas e gráficos redimensionam automaticamente

### Performance

- Dados em cache para carregamento rápido
- Renderização otimizada
- Interações fluidas

## 8. 📥 Importação e Exportação

### Dados de Entrada

- Dados obtidos do GBIF (Global Biodiversity Information Facility)
- Atualização regular conforme novas observações são registradas
- 1500+ registros iniciais

### Exportação

- Download em CSV
- Compatível com ferramentas de análise
- Preserva todas as informações

## 9. 🔄 Atualizações de Dados

### Como Atualizar

Para obter novos dados do GBIF:

```bash
python download_gbif_data.py
python process_bee_data.py
streamlit run app.py
```

### Frequência

- Dados podem ser atualizados a qualquer momento
- Recomenda-se atualização mensal
- GBIF recebe novos registros continuamente

## 10. 📚 Fonte de Dados

### GBIF (Global Biodiversity Information Facility)

- Maior repositório de dados de biodiversidade do mundo
- Dados de museus, herbários e observações
- Acesso livre e gratuito
- Qualidade verificada

### Outras Fontes

- iNaturalist: Observações de cidadãos cientistas
- SpeciesLink: Rede de dados biológicos brasileira
- Pesquisas acadêmicas

## Roadmap Futuro

### Versão 2.0

- [ ] Filtro por data
- [ ] Análise temporal (tendências)
- [ ] Comparação entre períodos
- [ ] Previsão de distribuição

### Versão 3.0

- [ ] Integração com dados de conservação
- [ ] Mapa de ameaças
- [ ] Recomendações de proteção
- [ ] API para integração externa

### Versão 4.0

- [ ] Machine Learning para previsão
- [ ] Análise de mudanças climáticas
- [ ] Simulação de cenários
- [ ] Relatórios automáticos

## Suporte e Feedback

Para sugestões de novas funcionalidades:
- Abra uma issue no GitHub
- Envie um email para o desenvolvedor
- Participe das discussões da comunidade

---

**Última atualização**: Maio de 2026
