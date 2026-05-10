# 🤝 Contribuindo para o Observatório de Abelhas Sem Ferrão

Obrigado por considerar contribuir para este projeto! Este documento fornece diretrizes e instruções para contribuir.

## Como Contribuir

### 1. Reportar Bugs

Se encontrar um bug, abra uma issue com:
- Descrição clara do problema
- Passos para reproduzir
- Comportamento esperado vs. atual
- Screenshots se aplicável
- Informações do sistema (Python, OS, etc.)

### 2. Sugerir Melhorias

Sugestões são bem-vindas! Abra uma issue com:
- Descrição clara da melhoria
- Justificativa (por que é útil)
- Exemplos de implementação se possível

### 3. Enviar Pull Requests

#### Preparação

1. Fork o repositório
2. Clone seu fork: `git clone https://github.com/seu-usuario/bee-observatory-br.git`
3. Crie uma branch: `git checkout -b feature/sua-feature`

#### Desenvolvimento

1. Faça suas alterações
2. Teste localmente: `streamlit run app.py`
3. Verifique a sintaxe: `python -m py_compile app.py`

#### Commit e Push

1. Commit com mensagens claras: `git commit -m "Add: descrição clara"`
2. Push para sua branch: `git push origin feature/sua-feature`
3. Abra um Pull Request

### Convenções de Commit

Use prefixos para clareza:
- `Add:` - Nova funcionalidade
- `Fix:` - Correção de bug
- `Docs:` - Documentação
- `Refactor:` - Refatoração de código
- `Test:` - Testes
- `Style:` - Formatação

Exemplo:
```
Add: novo gráfico de tendências temporais
Fix: corrigir erro de carregamento de dados
```

## Diretrizes de Código

### Python

- Siga PEP 8
- Use nomes descritivos para variáveis
- Adicione docstrings em funções
- Comente código complexo

### Exemplo de Função Bem Documentada

```python
def calculate_foraging_radius(species_name):
    """
    Calcula o raio de forrageamento de uma espécie.
    
    Args:
        species_name (str): Nome científico da espécie
        
    Returns:
        int: Raio em metros
        
    Raises:
        ValueError: Se espécie não encontrada
    """
    # Implementação aqui
    pass
```

### Streamlit

- Mantenha componentes modulares
- Use `@st.cache_data` para dados
- Organize código em seções lógicas
- Teste em diferentes tamanhos de tela

## Estrutura do Projeto

```
bee-observatory-br/
├── app.py                      # Aplicativo principal
├── download_gbif_data.py       # Download de dados
├── process_bee_data.py         # Processamento de dados
├── requirements.txt            # Dependências
├── README.md                   # Documentação principal
├── INSTALL.md                  # Guia de instalação
├── FEATURES.md                 # Funcionalidades
├── CONTRIBUTING.md             # Este arquivo
├── .streamlit/
│   └── config.toml            # Configuração do Streamlit
└── data/
    ├── meliponini_br_occurrences.csv
    └── processed_bee_data.csv
```

## Áreas para Contribuição

### Código

- Otimização de performance
- Novas visualizações
- Melhorias na interface
- Testes automatizados

### Dados

- Validação de dados
- Novas fontes de dados
- Correção de coordenadas
- Informações sobre espécies

### Documentação

- Melhorias no README
- Tutoriais
- Exemplos de uso
- Tradução para outros idiomas

### Design

- Melhorias visuais
- Acessibilidade
- Responsividade
- Temas alternativos

## Processo de Review

1. Seu PR será revisado por um mantenedor
2. Podem ser solicitadas alterações
3. Após aprovação, será feito merge
4. Você será creditado nas releases

## Código de Conduta

- Seja respeitoso com outros contribuidores
- Forneça feedback construtivo
- Respeite diferentes opiniões
- Reporte comportamento inapropriado

## Dúvidas?

- Abra uma issue com a tag `question`
- Consulte a documentação existente
- Procure por issues similares

## Reconhecimento

Todos os contribuidores serão reconhecidos em:
- Arquivo CONTRIBUTORS.md
- Release notes
- Página do projeto

Obrigado por contribuir! 🎉
