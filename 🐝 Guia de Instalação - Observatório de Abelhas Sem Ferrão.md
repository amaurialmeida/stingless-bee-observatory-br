# 🐝 Guia de Instalação - Observatório de Abelhas Sem Ferrão

## Pré-requisitos

- **Python 3.8+** (recomendado 3.9 ou superior)
- **pip** (gerenciador de pacotes Python)
- Conexão com a internet (para baixar dados do GBIF)

## Instalação Rápida

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/bee-observatory-br.git
cd bee-observatory-br
```

### 2. Crie um ambiente virtual (recomendado)

```bash
# No Windows
python -m venv venv
venv\Scripts\activate

# No macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Baixe e processe os dados (primeira execução)

```bash
# Baixar dados do GBIF
python download_gbif_data.py

# Processar e enriquecer dados
python process_bee_data.py
```

Isso criará dois arquivos CSV:
- `meliponini_br_occurrences.csv` - Dados brutos do GBIF
- `processed_bee_data.csv` - Dados processados com nomes populares e raios de forrageamento

### 5. Execute o aplicativo

```bash
streamlit run app.py
```

O aplicativo abrirá automaticamente em `http://localhost:8501`

## Instalação Detalhada

### Passo 1: Verificar Python

```bash
python --version
# ou
python3 --version
```

Deve retornar a versão 3.8 ou superior.

### Passo 2: Criar Ambiente Virtual

Um ambiente virtual isola as dependências do projeto:

```bash
# Criar
python -m venv venv

# Ativar (Windows)
venv\Scripts\activate

# Ativar (macOS/Linux)
source venv/bin/activate
```

Você saberá que está ativado quando o terminal mostrar `(venv)` no início.

### Passo 3: Instalar Dependências

Com o ambiente virtual ativado:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Isso instalará:
- **streamlit**: Framework web
- **pandas**: Manipulação de dados
- **folium**: Mapas interativos
- **plotly**: Gráficos interativos
- **numpy**: Computação numérica
- **geopandas**: Análise geoespacial
- **requests**: Requisições HTTP

### Passo 4: Baixar Dados

O primeiro passo é obter os dados do GBIF:

```bash
python download_gbif_data.py
```

Este script:
- Conecta à API do GBIF
- Baixa 1500 registros de Meliponini no Brasil
- Salva em `meliponini_br_occurrences.csv`

**Tempo estimado:** 2-5 minutos

### Passo 5: Processar Dados

Depois, enriqueça os dados com informações adicionais:

```bash
python process_bee_data.py
```

Este script:
- Lê os dados brutos
- Adiciona nomes populares
- Adiciona raios de forrageamento
- Salva em `processed_bee_data.csv`

**Tempo estimado:** Menos de 1 minuto

### Passo 6: Executar o Aplicativo

Finalmente, inicie o Streamlit:

```bash
streamlit run app.py
```

Você verá algo como:

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.100:8501
```

Abra o navegador em `http://localhost:8501`

## Troubleshooting

### Erro: "Python não encontrado"

Certifique-se de que Python está instalado e no PATH:

```bash
python --version
```

Se não funcionar, tente:
```bash
python3 --version
```

### Erro: "ModuleNotFoundError"

Verifique se o ambiente virtual está ativado:

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

Depois reinstale as dependências:

```bash
pip install -r requirements.txt
```

### Erro: "Arquivo não encontrado"

Certifique-se de estar no diretório correto:

```bash
cd bee-observatory-br
ls  # ou 'dir' no Windows
```

Você deve ver os arquivos `app.py`, `requirements.txt`, etc.

### Erro: "Conexão recusada" ao baixar dados

Verifique sua conexão com a internet. Se o problema persistir, você pode usar os dados pré-processados inclusos no repositório.

### Porta 8501 já em uso

Se a porta 8501 estiver em uso, Streamlit usará automaticamente a próxima porta disponível. Verifique a saída do terminal.

Ou especifique uma porta diferente:

```bash
streamlit run app.py --server.port 8502
```

## Próximos Passos

1. **Explore o mapa**: Clique nos marcadores para ver informações detalhadas
2. **Filtre espécies**: Use o painel lateral para selecionar quais espécies visualizar
3. **Analise gráficos**: Veja as distribuições por estado e espécie
4. **Baixe dados**: Exporte os dados em CSV para análise externa

## Deploy no Streamlit Cloud

Para compartilhar seu aplicativo online:

1. Faça push para GitHub:
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. Acesse [streamlit.io](https://streamlit.io)
3. Clique em "New app"
4. Selecione seu repositório GitHub
5. Configure o arquivo principal como `app.py`
6. Clique em "Deploy"

Seu aplicativo estará disponível em: `https://seu-usuario-bee-observatory-br.streamlit.app`

## Suporte

Para dúvidas ou problemas:
- Abra uma issue no GitHub
- Consulte a [documentação do Streamlit](https://docs.streamlit.io)
- Visite [GBIF](https://www.gbif.org) para mais informações sobre dados

## Licença

Este projeto está sob licença MIT.
