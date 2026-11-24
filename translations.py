"""Textos do Observatório de Abelhas Sem Ferrão do Brasil em 10 idiomas.

Edite aqui para corrigir qualquer tradução. Estrutura idêntica em todos os idiomas
(pt, en, es, it, fr, de, zh, ar, el, af). Marcadores @@NOME@@ são substituídos pelo
app com números calculados do GBIF; {n}, {d}, {k} são preenchidos em tempo de execução.
Chaves-de-busca como mel_vals/status_vals ("Sim","Alta"...) ficam em português: só os valores mudam.
"""

TRANSLATIONS = {'pt': {'page_title': 'Observatório Meliponini · Brasil',
        'hero_tag': 'BIODIVERSIDADE · MELIPONINI · BRASIL · 2022–2025',
        'hero_title': 'Observatório de\nAbelhas Sem Ferrão',
        'hero_subtitle': 'Monitoramento e análise da distribuição das abelhas sem ferrão nativas '
                         '(Meliponini) e abelhas solitárias no Brasil — mais de 24.000 registros GBIF, 12 '
                         'espécies mapeadas e conservação ativa. Inclui visita técnica à Cidade das Abelhas '
                         '(SP, 2022) e hotel para abelhas solitárias construído na FATEC Jundiaí.',
        'badge1': '🐝 12 espécies monitoradas',
        'badge2': '🗺️ 300+ pontos de ocorrência',
        'badge3': 'Brasil · 5 Biomas',
        'badge4': 'GBIF · iNaturalist · INPA',
        'badge5': 'TCC FATEC Jundiaí 2022',
        'm1': 'Espécies Meliponini',
        'm2': 'Registros GBIF (2024)',
        'm3': 'Estados cobertos',
        'm4': 'Espécies ameaçadas',
        'tab1': '🗺️ Mapa & Análise',
        'tab2': '🔬 Metodologia & Pipeline',
        'tab3': '💡 O que Descobrimos',
        'tab4': '📷 Em Campo',
        'tab5': '📈 Tendências',
        'tab6': '⚙️ Parâmetros',
        'tab7': '📋 Dados Brutos',
        'tab8': '📚 Fontes & Créditos',
        'map_label': 'DISTRIBUIÇÃO NO BRASIL',
        'map_title': 'Mapa de Ocorrências — Abelhas Sem Ferrão',
        'map_hint': '🐝 <strong>Clique nos marcadores</strong> para ver espécie, bioma e fonte. Tamanho ∝ '
                    'registros por estado. Ative os clusters para ver agrupamentos.',
        'heat_title': 'Mapa de Calor — Densidade de Ocorrências',
        'chart_label': 'ANÁLISE COMPARATIVA',
        'sp_registros_title': 'Registros por Espécie (GBIF, 2024)',
        'estado_title': 'Registros por Estado',
        'bioma_title': 'Distribuição por Bioma',
        'method_label': 'BIODIVERSIDADE APLICADA',
        'method_title': 'Pergunta & Metodologia',
        'sci_q_title': '❓ Pergunta Central',
        'sci_q': '"Qual é o estado atual da distribuição e conservação das abelhas sem ferrão nativas do '
                 'Brasil, e como práticas de meliponicultura racional e hotelaria para abelhas solitárias '
                 'podem contribuir para a preservação dessas espécies em ambientes urbanos e periurbanos?"',
        'pipeline_label': 'PIPELINE DE DADOS',
        'steps': [['1',
                   'Coleta — GBIF + iNaturalist (2010–2024)',
                   'Dados de ocorrência dos Meliponini brasileiros via GBIF API e exportação iNaturalist. '
                   '@@TOTAL@@ registros georreferenciados (2010–2024), filtrados sem problemas geoespaciais. '
                   'Espécies alvo: 12 Meliponini nativas + 6 abelhas solitárias.'],
                  ['2',
                   'Visita Técnica — Cidade das Abelhas (SP, 2022)',
                   'Visita técnica ao Parque Cidade das Abelhas em São Paulo para observação direta de '
                   'colmeias racionais de Jataí, Mosquitinho, Manduri, Mirim Preguiça e outras espécies. '
                   'Registro fotográfico e levantamento de dados sobre manejo racional de meliponários.'],
                  ['3',
                   'TCC FATEC Jundiaí — Hotel para Abelhas Solitárias (2022)',
                   'Projeto de conclusão de curso: construção de Hotel para Abelhas Solitárias no Campus da '
                   'FATEC Jundiaí para o evento Ciência na Praça. Estrutura em madeira com furos broca 8 e '
                   '10 mm para abelhas solitárias nativas como Xylocopa sp. e Megachile sp.'],
                  ['4',
                   'Análise Espacial — Distribuição por Bioma',
                   'Cruzamento das ocorrências com shapefile dos biomas do IBGE. Identificação de padrões de '
                   'riqueza de espécies por bioma. Mata Atlântica como bioma de maior diversidade de '
                   'Meliponini (~22 espécies).'],
                  ['5',
                   'Parâmetros Biológicos — Literatura Científica',
                   'Compilação de dados da literatura: tamanho de colônia, taxa de postura, vida da '
                   'operária, raio de forrageamento, produção de mel. Base: A.B.E.L.H.A., Atlas da '
                   'Meliponicultura, publicações USP/UNICAMP/UFMG.'],
                  ['6',
                   'Avaliação de Ameaça — IUCN Red List',
                   'Cruzamento dos dados de ocorrência com status IUCN: @@VU@@ espécies Vulneráveis (VU), '
                   '@@LC@@ com Menor Preocupação (LC). Análise de tendências populacionais e pressões '
                   'antrópicas por bioma.']],
        'biologia_title': '🐝 Por que as Abelhas Sem Ferrão importam?',
        'biologia_text': '• <b>~550 espécies</b> de Meliponini descritas no mundo · <b>~350 no '
                         'Brasil</b><br>• <b>Polinizadoras exclusivas</b> de espécies nativas da Mata '
                         'Atlântica e Cerrado<br>• <b>Mel com propriedades medicinais</b> reconhecidas pela '
                         'ANVISA (Portaria 310/1997)<br>• <b>Meliponicultura</b>: criação racional em caixas '
                         'INPA, IBAMA, JTB, Fernão Dias<br>• <b>Ameaças:</b> desmatamento, agrotóxicos, '
                         'urbanização, espécies exóticas invasoras',
        'solitarias_title': '🏨 Abelhas Solitárias — A Maioria Silenciosa',
        'solitarias_text': '• <b>~70% das abelhas do mundo</b> são solitárias — sem rainha, sem colmeia<br>• '
                           '<b>Cada fêmea</b> constrói seu próprio ninho, coleta alimento e cuida dos '
                           'ovos<br>• <b>Hotéis de abelhas</b> (blocos de madeira com furos 6–10 mm) atraem '
                           'Xylocopa, Megachile e Hylaeus<br>• <b>Furos ideais:</b> broca 8 mm (Megachile), '
                           'broca 10 mm (Xylocopa) — profundidade mínima 10 cm<br>• <b>Instalação:</b> '
                           'orientação Leste/Sudeste, altura 1–2 m, protegido da chuva direta',
        'disc_label': 'ANÁLISE E DESCOBERTAS',
        'disc_title': 'O que os Dados Revelaram',
        'discoveries': [['🐝',
                         'Jataí — a mais adaptada à urbanização',
                         'Tetragonisca angustula é a espécie com maior adaptabilidade ao ambiente urbano. '
                         'Registros em todos os estados brasileiros e nos 5 biomas. Nidifica em fendas de '
                         'alvenaria, caixas elétricas e postes. Sua presença em cidades é indicador de '
                         'resiliência ecológica.'],
                        ['⚠️',
                         '@@VU@@ espécies Vulneráveis — @@VU_LIST@@',
                         'As espécies de Melipona com maior porte e produção de mel são as mais ameaçadas. A '
                         'combinação de desmatamento, pressão antrópica e baixa reprodução (rainha faz '
                         'apenas 1 voo nupcial) torna essas espécies especialmente vulneráveis ao colapso '
                         'populacional.'],
                        ['🏨',
                         'Hotel para Abelhas — multiplicador de biodiversidade urbana',
                         'O Hotel para Abelhas construído na FATEC Jundiaí demonstrou que estruturas simples '
                         'de madeira com furos de broca 8 e 10 mm são ocupadas em 30–60 dias por espécies '
                         'solitárias nativas. Uma intervenção de baixo custo (<R$50) com alto impacto para a '
                         'polinização local.'],
                        ['📊',
                         'São Paulo — capital meliponícola brasileira',
                         '@@SP_SENT@@ A combinação de Mata Atlântica remanescente, pesquisa universitária '
                         'intensa (USP, UNICAMP, UNESP) e meliponicultura urbana crescente explica esse '
                         'protagonismo.'],
                        ['🌎',
                         'GBIF: @@GROWTH@@ em 10 anos — ciência cidadã como motor',
                         'O crescimento de @@GROWTH_ABS@@ registros georreferenciados de Meliponini no '
                         'Brasil entre 2014 e 2024 (@@GROWTH@@) acompanha o aumento do uso do iNaturalist e '
                         'do interesse cidadão pela biodiversidade. A meliponicultura urbana crescente é '
                         'tanto consequência quanto causa desse interesse.'],
                        ['🌿',
                         'Cerrado — bioma sub-amostrado com grande diversidade oculta',
                         'Apesar de abrigar ~100 espécies endêmicas de Meliponini, o Cerrado é '
                         'historicamente sub-amostrado nos registros de biodiversidade. A sub-amostragem '
                         'reflete lacunas de pesquisa em áreas remotas — um alerta para a conservação antes '
                         'que o bioma seja 100% fragmentado.']],
        'conclusion_label': 'CONCLUSÃO',
        'conclusion_title': 'Cada Colmeia Conta',
        'conclusion_text': 'As abelhas sem ferrão nativas do Brasil são um patrimônio biocultural único: '
                           'cultivadas pelos povos indígenas por milênios, produtoras de mel com '
                           'propriedades medicinais e polinizadoras insubstituíveis de nossa flora nativa. O '
                           'crescimento de @@GROWTH_N@@ nos registros GBIF de Meliponini mostra que o '
                           'interesse pela meliponicultura está aumentando — mas o ritmo do desmatamento '
                           'ainda supera a velocidade da conservação. Cada colmeia racional instalada, cada '
                           'hotel para abelhas construído, cada fragmento florestal protegido é um voto de '
                           'confiança no futuro dessas espécies.',
        'conclusion_author': 'Amauri Almeida · TCC Gestão Ambiental · FATEC Jundiaí · 2022 · Visita Cidade '
                             'das Abelhas SP',
        'field_label': 'REGISTRO DE CAMPO E TÉCNICO',
        'field_title': 'Da Cidade das Abelhas ao Campus da FATEC',
        'field_inst_title': '📁 Como adicionar suas fotos',
        'field_inst': 'Coloque suas fotos na pasta <code>assets/campo/</code> com os nomes exatos abaixo.',
        'photos': [{'emoji': '🐝',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Colmeia Racional — Abelha Jataí',
                    'esp': 'Tetragonisca angustula',
                    'desc': 'Colmeia racional (caixa JTB ou INPA) da abelha Jataí (Tetragonisca angustula) '
                            'no Parque Cidade das Abelhas, São Paulo. A Jataí é a espécie mais comum e '
                            'adaptável do Brasil — nidifica naturalmente em fendas de alvenaria. A colmeia '
                            'racional permite a divisão de colônias e o manejo sem destruir o ninho.',
                    'path': 'assets/campo/01_colmeia_jatai_cidade_abelhas.jpg',
                    'legenda': 'Colmeia Jataí (Tetragonisca angustula) · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🔎',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Colmeia Racional — Abelha Mosquitinho',
                    'esp': 'Plebeia mosquito',
                    'desc': 'Colmeia racional da abelha Mosquitinho (Plebeia mosquito) — uma das menores '
                            'abelhas sem ferrão do Brasil (2 mm). Extremamente dócil e sensível a '
                            'agrotóxicos. Colmeia com módulo de mel separado do módulo de cria — prática '
                            'fundamental da meliponicultura racional para não prejudicar a colônia.',
                    'path': 'assets/campo/02_colmeia_mosquitinho_cidade_abelhas.jpg',
                    'legenda': 'Colmeia Mosquitinho (Plebeia mosquito) · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🌿',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Colmeia Racional — Abelha Manduri (1)',
                    'esp': 'Melipona marginata',
                    'desc': 'Colmeia racional da abelha Manduri (Melipona marginata) — espécie Vulnerável '
                            '(IUCN VU). Uma das espécies mais importantes para a conservação: mel raro, '
                            'produzido em pequena quantidade, nidifica exclusivamente em ocos de árvores '
                            'nativas. A meliponicultura racional é a principal estratégia de conservação ex '
                            'situ para esta espécie.',
                    'path': 'assets/campo/04_colmeia_manduri_cidade_abelhas_1.jpg',
                    'legenda': 'Colmeia Manduri (Melipona marginata) · Vulnerável · Cidade das Abelhas · SP '
                               '· 2022',
                    'gid': 'cidade'},
                   {'emoji': '🌿',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Colmeia Racional — Abelha Manduri (2)',
                    'esp': 'Melipona marginata',
                    'desc': 'Segunda colmeia de Manduri documentada. O acompanhamento de múltiplas colmeias '
                            'da mesma espécie permite estudar variação comportamental e de produção. A '
                            'diferença de cor e estrutura entre caixas reflete diferentes modelos de colmeia '
                            'racional — INPA, Fernão Dias, JTB e modelos USP.',
                    'path': 'assets/campo/05_colmeia_manduri_cidade_abelhas_2.jpg',
                    'legenda': 'Colmeia Manduri (2) · Melipona marginata · VU · Cidade das Abelhas · SP · '
                               '2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Colmeia Racional — Mirim Preguiça (1)',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'Colmeia racional da abelha Mirim Preguiça (Frieseomelitta varia) — chamada '
                            'assim pelo comportamento tranquilo das operárias na entrada da colmeia. Espécie '
                            'importante para a polinização de espécies nativas do Cerrado e da Mata '
                            'Atlântica. Constrói ninhos em galhos de árvores.',
                    'path': 'assets/campo/06_colmeia_mirim_preguica_1.jpg',
                    'legenda': 'Colmeia Mirim Preguiça (Frieseomelitta varia) · Cidade das Abelhas · SP · '
                               '2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Colmeia Racional — Mirim Preguiça (2)',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'Segunda vista da colmeia de Mirim Preguiça. Observa-se a entrada da colmeia com '
                            'as características específicas desta espécie. A arquitetura interna do ninho, '
                            'com células de cria esféricas, é diferente das Melipona — o que exige '
                            'adaptações específicas nas caixas racionais para esta espécie.',
                    'path': 'assets/campo/07_colmeia_mirim_preguica_2.jpg',
                    'legenda': 'Colmeia Mirim Preguiça (2) · Frieseomelitta varia · Cidade das Abelhas · SP '
                               '· 2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Colmeia Racional — Mirim Preguiça (3)',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'Terceiro ângulo da colmeia de Mirim Preguiça, mostrando detalhes da estrutura '
                            'externa e do suporte. A documentação de múltiplas vistas é essencial em visitas '
                            'técnicas para identificar padrões de manejo e design de colmeia que funcionam '
                            'melhor para cada espécie.',
                    'path': 'assets/campo/08_colmeia_mirim_preguica_3.jpg',
                    'legenda': 'Colmeia Mirim Preguiça (3) · Frieseomelitta varia · Cidade das Abelhas · SP '
                               '· 2022',
                    'gid': 'cidade'},
                   {'emoji': '🏛️',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Meliponário — Coleção de Espécies Distintas',
                    'esp': 'Múltiplas espécies',
                    'desc': 'Vista do meliponário do Parque Cidade das Abelhas com caixas racionais de '
                            'espécies distintas lado a lado — como orienta a boa prática meliponícola. Cada '
                            'espécie tem sua caixa identificada. O espaçamento entre colmeias e a orientação '
                            'da entrada são calculados para minimizar deriva de abelhas e maximizar a saúde '
                            'das colônias.',
                    'path': 'assets/campo/09_meliponario_colecao_cidade_abelhas.jpg',
                    'legenda': 'Meliponário com espécies distintas · Caixas racionais · Parque Cidade das '
                               'Abelhas · SP · 2022',
                    'destaque': True,
                    'gid': 'cidade'},
                   {'emoji': '🌳',
                    'grupo': 'HOTEL DE ABELHAS · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Construção do Hotel — Estrutura em Madeira',
                    'esp': 'Para abelhas solitárias',
                    'desc': 'Início da construção do Hotel para Abelhas Solitárias no Campus da FATEC '
                            'Jundiaí. A estrutura em madeira é o suporte principal para os blocos '
                            'perfurados. A escolha da madeira (pinus tratado ou eucalipto) é importante: '
                            'deve ser resistente à umidade mas não tratada com biocidas que afastem as '
                            'abelhas.',
                    'path': 'assets/campo/10_hotel_abelhas_estrutura_madeira.jpg',
                    'legenda': 'Construção Hotel de Abelhas · Estrutura em madeira · FATEC Jundiaí · Ciência '
                               'na Praça · 2022',
                    'gid': 'hotel'},
                   {'emoji': '🔩',
                    'grupo': 'HOTEL DE ABELHAS · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Perfurando os Blocos — Broca 8 e 10 mm',
                    'esp': 'Para abelhas solitárias',
                    'desc': 'Perfuração dos blocos de madeira com furadeira usando broca 8 mm (Megachile '
                            'sp., Hylaeus sp.) e broca 10 mm (Xylocopa sp.). Profundidade mínima de 10 cm '
                            'essencial para que a fêmea complete o ninho com 3–5 células de cria. Furos '
                            'devem terminar em fundo cego — não podem atravessar o bloco.',
                    'path': 'assets/campo/11_hotel_abelhas_furadeira_broca8_10.jpg',
                    'legenda': 'Perfuração com broca 8 e 10 mm · Hotel Abelhas Solitárias · FATEC Jundiaí · '
                               '2022',
                    'gid': 'hotel'},
                   {'emoji': '🔩',
                    'grupo': 'HOTEL DE ABELHAS · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Furação em Detalhe — Broca 8 e 10 mm',
                    'esp': 'Para abelhas solitárias',
                    'desc': 'Detalhe do processo de furação com broca 8 e 10 mm. A uniformidade dos furos é '
                            'importante para o sucesso do hotel: profundidade mínima 10 cm, diâmetro preciso '
                            'e superfície interna lisa (lixar se necessário). Furos com serrilhado interno '
                            'podem impedir a passagem das abelhas.',
                    'path': 'assets/campo/12_hotel_abelhas_furos_detalhe.jpg',
                    'legenda': 'Detalhe furos broca 8/10 mm · Hotel Abelhas Solitárias · FATEC Jundiaí · '
                               '2022',
                    'gid': 'hotel'},
                   {'emoji': '✅',
                    'grupo': 'HOTEL DE ABELHAS · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Hotel de Abelhas Concluído — Campus FATEC Jundiaí',
                    'esp': 'Para abelhas solitárias',
                    'desc': 'Hotel para Abelhas Solitárias concluído, instalado no Campus da FATEC Jundiaí '
                            'para o evento Ciência na Praça. Blocos de madeira com furos de broca 8 e 10 mm, '
                            'orientação Leste/Sudeste, altura ~1,5 m, protegido por cobertura contra chuva. '
                            'Estrutura de baixo custo (<R$50) com alto impacto para a polinização local.',
                    'path': 'assets/campo/13_hotel_abelhas_concluido_fatec_jundiai.jpg',
                    'legenda': 'Hotel de Abelhas Solitárias concluído · Campus FATEC Jundiaí · Ciência na '
                               'Praça · 2022',
                    'destaque_final': True,
                    'gid': 'hotel'}],
        'timeline_label': 'LINHA DO TEMPO DO PROJETO',
        'timeline_items': [['2022 · Jan–Jun',
                            'TCC Gestão Ambiental — FATEC Jundiaí',
                            'Pesquisa sobre meliponicultura e abelhas solitárias · Hotel para Abelhas '
                            'construído para o Ciência na Praça'],
                           ['2022 · Jul',
                            'Visita Técnica — Cidade das Abelhas SP',
                            'Registro fotográfico de 8+ espécies em colmeias racionais · Jataí, Mosquitinho, '
                            'Manduri, Mirim Preguiça e outras'],
                           ['2022 · Nov',
                            'Defesa do TCC — FATEC Jundiaí',
                            'Aprovação do Trabalho de Conclusão de Curso em Gestão Ambiental · Bacharel '
                            'aprovado'],
                           ['2023–2024',
                            'Análise GBIF — @@TOTAL@@ registros',
                            'Cruzamento de dados de ocorrência com biomas e estados · Identificação de '
                            'lacunas de conservação'],
                           ['2025',
                            'Publicação no Portfólio',
                            'Observatório Meliponini do Brasil — dashboard público com dados atualizados']],
        'trend_sel': 'Selecione visualização',
        'trend_opt1': 'Crescimento GBIF (2010–2024)',
        'trend_opt2': 'Registros por Espécie (ranking)',
        'trend_opt3': 'Registros por Estado',
        'param_sel': 'Espécie para análise',
        'param_names': {'colonia': 'Tamanho da colônia (operárias)',
                        'postura_dia': 'Taxa de postura (ovos/dia)',
                        'vida_operaria': 'Vida da operária (dias)',
                        'longe_formag': 'Raio de forrageamento (m)',
                        'prod_mel_kg': 'Produção de mel (kg/ano)',
                        'raio_dna_km': 'Distância genética (km)'},
        'raw_label': 'CATÁLOGO DE ESPÉCIES',
        'raw_title': 'Tabela Completa — Meliponini do Brasil',
        'download_csv': '⬇️ Baixar CSV',
        'sources_label': 'FONTES CIENTÍFICAS',
        'sources_title': 'Fontes & Base de Dados',
        'tech_label': 'TECNOLOGIAS UTILIZADAS',
        'footer_title': '🐝 Amauri Almeida',
        'footer_desc': 'Tecnólogo em Gestão Ambiental · FATEC Jundiaí (3º ENADE)<br>Pós-Graduação em IA, '
                       'Machine Learning & Data Science · Ciência de Dados & Big Data<br>Análise e '
                       'Desenvolvimento de Sistemas · FACINT Maringá',
        'footer_links': '📍 Fernandópolis · SP · Brasil',
        'trend_label': 'EVOLUÇÃO TEMPORAL & RANKINGS',
        'param_label': 'BIOLOGIA COMPARADA',
        'param_title': 'Parâmetros Biológicos das Espécies',
        'param_detail': 'Parâmetro biológico',
        'param_cmp': 'Comparativo entre Espécies',
        'records_axis': 'Registros',
        'records_hover': 'registros',
        'gal_meli': 'GALERIA DE ESPÉCIES — MELIPONINI',
        'gal_sol': 'GALERIA — ABELHAS SOLITÁRIAS',
        'honey': 'Mel',
        'mel_vals': {'Sim': 'Sim', 'Não': 'Não', 'Pouco': 'Pouco'},
        'gbif_records': 'registros GBIF',
        'pop_records': 'Registros',
        'pop_species': 'Espécies',
        'pop_status': 'Status',
        'status_vals': {'Alta': 'Alta', 'Média': 'Média', 'Baixa': 'Baixa'},
        'radar_title': 'Perfil Comparativo das Espécies (escala 0–10)',
        'radar_cats': ['Produção de mel',
                       'Adaptação urbana',
                       'Raio de voo',
                       'Tamanho da colônia',
                       'IUCN (inv.)'],
        'grp_city': '🏛️ CIDADE DAS ABELHAS · SÃO PAULO · 2022',
        'grp_hotel': '🏨 HOTEL DE ABELHAS SOLITÁRIAS · FATEC JUNDIAÍ · CIÊNCIA NA PRAÇA · 2022',
        'dest_melipon': '⭐ DESTAQUE — MELIPONÁRIO COMPLETO · CIDADE DAS ABELHAS',
        'dest_hotel': '✅ DESTAQUE FINAL — HOTEL CONCLUÍDO · CAMPUS FATEC JUNDIAÍ',
        'hotel_build_title': '🏗️ Como construir um Hotel para Abelhas Solitárias',
        'hotel_build': [['Material', 'Bloco de madeira (pinus tratado ou eucalipto) · 15×10×10 cm mínimo'],
                        ['Furos', 'Broca 8 mm (Megachile, Hylaeus) · Broca 10 mm (Xylocopa)'],
                        ['Profundidade', 'Mínimo 10 cm · Fundo cego (não atravessar o bloco!)'],
                        ['Orientação', 'Leste ou Sudeste · Recebe sol da manhã'],
                        ['Altura', '1–2 metros do solo · Protegido de chuva e vento'],
                        ['Resultado', 'Ocupação em 30–60 dias por abelhas nativas']],
        'solitary_tbl': 'Abelhas Solitárias',
        'card_lbls': {'biome': 'Bioma',
                      'region': 'Região',
                      'colony': 'Colônia',
                      'workers': 'operárias',
                      'laying': 'Postura',
                      'eggs_day': 'ovos/dia',
                      'worker_life': 'Vida operária',
                      'days': 'dias',
                      'forage': 'Raio forrageamento',
                      'honey': 'Produção mel',
                      'kg_year': 'kg/ano',
                      'gen_dist': 'Dist. genética'},
        'carto_fallback': 'Mapa base alternativo (OpenStreetMap) em uso.',
        'occ_live': 'Pontos reais do GBIF (api.gbif.org): {n} ocorrências georreferenciadas no Brasil, até '
                    '{k} por espécie, consultadas em {d}. Clique num ponto para abrir o registro original.',
        'occ_demo': 'GBIF indisponível no momento: os pontos mostrados são ILUSTRATIVOS (capitais × '
                    'espécies), não são registros de campo.',
        'occ_none': 'GBIF indisponível no momento e sem dados de reserva: mapa de ocorrências não exibido.',
        'dados_live': 'Números calculados a partir do GBIF (api.gbif.org), consultados em {d}; atualização '
                      'automática a cada 24 h.',
        'dados_snapshot': 'GBIF indisponível agora: números do último snapshot salvo ({d}).',
        'dados_static': 'GBIF indisponível agora: valores de referência de uma compilação anterior, não '
                        'atualizados.',
        'serie_total': 'Total (Meliponini + 5 gêneros solitários)',
        'serie_inat': 'iNaturalist (Meliponini)',
        'raio_sel': 'Mostrar raio de forrageamento (círculos em metros)',
        'raio_note': 'Cada círculo mostra o raio médio de voo da espécie ao redor de ocorrências reais (até '
                     '{n} por espécie). Aproxime o mapa para ver a escala.',
        'raio_layer': 'Raio de forrageamento',
        'footer_portfolio': 'Portfólio',
        'sources': [['GBIF',
                     'GBIF — Global Biodiversity Information Facility',
                     'gbif.org · Base de ocorrências com @@TOTAL@@ registros georreferenciados de Meliponini '
                     'no Brasil (2010–2024). Dados de museus, herbários, iNaturalist e pesquisadores.',
                     '#C47D0E'],
                    ['A.B.E.L.H.A.',
                     'A.B.E.L.H.A. — Associação Brasileira de Estudo das Abelhas',
                     'abelha.org.br · Atlas da Meliponicultura no Brasil. Referência para raios de '
                     'forrageamento, biologia e conservação.',
                     '#C0390A'],
                    ['INATURALIST',
                     'iNaturalist — Ciência Cidadã Global',
                     'inaturalist.org · @@INAT@@ registros de Meliponini brasileiros com georreferência '
                     '(dataset iNaturalist Research-grade no GBIF). Principal motor de crescimento do GBIF.',
                     '#2D7A45'],
                    ['FATEC',
                     'FATEC Jundiaí — TCC Gestão Ambiental (2022)',
                     'Hotel para Abelhas Solitárias construído no Campus para o evento Ciência na Praça. '
                     'Broca 8 e 10 mm. Aprovado com destaque.',
                     '#1B3A1E'],
                    ['CIDADE ABELHAS',
                     'Parque Cidade das Abelhas — São Paulo (2022)',
                     'Visita técnica em 2022. Registro fotográfico de colmeias racionais de Jataí, '
                     'Mosquitinho, Manduri, Mirim Preguiça e outras.',
                     '#5C3D1E'],
                    ['IUCN',
                     'IUCN Red List — Lista Vermelha de Espécies Ameaçadas',
                     '@@VU_TAGS@@. Status de conservação dos Meliponini brasileiros.',
                     '#8B2515'],
                    ['INPA',
                     'INPA — Instituto Nacional de Pesquisas da Amazônia',
                     'Modelo de colmeia racional INPA para Meliponini amazônicos. Dados de espécies do Norte '
                     'do Brasil.',
                     '#0D4E72'],
                    ['EMBRAPA',
                     'EMBRAPA Cerrados / EMBRAPA Amazônia Oriental',
                     'Dados de Meliponicultura em biomas brasileiros. Referência técnica para espécies do '
                     'Cerrado e da Amazônia.',
                     '#C47D0E']],
        'species_text': {'Jataí': {'descricao': 'A abelha sem ferrão mais conhecida do Brasil. Produz mel de '
                                                'altíssima qualidade com propriedades medicinais. Ninhos em '
                                                'ocos de árvores e fendas de alvenaria. Operculação da '
                                                'entrada com propolis em tubo ou pastilhas.',
                                   'bioma': 'Todos',
                                   'regiao': 'Nacional'},
                         'Mosquitinho': {'descricao': 'Uma das menores abelhas sem ferrão do Brasil. '
                                                      'Extremamente dócil. Mel muito saboroso produzido em '
                                                      'pequenas quantidades. Muito sensível ao uso de '
                                                      'agrotóxicos. Indicadora de qualidade ambiental.',
                                         'bioma': 'Mata Atlântica',
                                         'regiao': 'Sul/Sudeste'},
                         'Manduri': {'descricao': 'Espécie ameaçada de extinção (VU). Mel raro, produzido em '
                                                  'pequenas quantidades. Ninhos geralmente em cavidades de '
                                                  'árvores nativas. Espécie-alvo de programas de '
                                                  'meliponicultura para conservação.',
                                     'bioma': 'Mata Atlântica',
                                     'regiao': 'Sul/Sudeste'},
                         'Mirim Preguiça': {'descricao': 'Também chamada de Abelha Preguiça por seu '
                                                         'comportamento tranquilo. Nidifica principalmente '
                                                         'em galhos de árvores. Importante polinizadora de '
                                                         'espécies nativas do Cerrado e da Mata Atlântica.',
                                            'bioma': 'Cerrado/Mata Atlântica',
                                            'regiao': 'Centro/Sudeste'},
                         'Mandaçaia': {'descricao': 'Uma das maiores abelhas sem ferrão. Produção de mel '
                                                    'diferenciada. Em declínio pelo desmatamento e '
                                                    'urbanização. Criada há séculos pelos indígenas guaranis '
                                                    "como 'mborí'.",
                                       'bioma': 'Mata Atlântica',
                                       'regiao': 'Sudeste/Sul'},
                         'Uruçu Nordestina': {'descricao': 'Abelha sagrada dos tupinambás, cultivada há mais '
                                                           'de 2.000 anos. Mel com propriedades medicinais '
                                                           'reconhecidas. Símbolo da meliponicultura '
                                                           'nordestina. Espécie-bandeira da apicultura '
                                                           'indígena.',
                                              'bioma': 'Caatinga/Mata Atlântica NE',
                                              'regiao': 'Nordeste'},
                         'Irapuá': {'descricao': 'Apesar de não produzir mel em quantidade comercial, é '
                                                 'importantíssima polinizadora. Constroem ninhos expostos '
                                                 'com resina de plantas. Às vezes confundida com '
                                                 'abelha-europeia por comportamento defensivo.',
                                    'bioma': 'Todos',
                                    'regiao': 'Nacional'},
                         'Tiúba': {'descricao': "Conhecida como 'Abelha da Terra' no Maranhão. Mel com sabor "
                                                'único, muito apreciado. Parte fundamental da cultura '
                                                'meliponicultora amazônica e maranhense. Espécie em risco '
                                                'pelo desmatamento.',
                                   'bioma': 'Amazônia/Nordeste',
                                   'regiao': 'Norte/Nordeste'},
                         'Guaraipo': {'descricao': 'Espécie com padrão de coloração variável. Produção de '
                                                   'mel de sabor suave. Ninhos em solo ou troncos. Em '
                                                   'declínio acentuado pelo avanço da agropecuária no '
                                                   'Cerrado.',
                                      'bioma': 'Cerrado/Mata Atlântica',
                                      'regiao': 'Centro-Oeste/Sudeste'},
                         'Iraí': {'descricao': 'Abelha muito comum em ambientes urbanos. Nidifica em fendas '
                                               'de paredes, caixas de luz e telhas. Muito tolerante à '
                                               'urbanização. Excelente indicadora de conectividade de '
                                               'fragmentos florestais.',
                                  'bioma': 'Cerrado/Mata Atlântica',
                                  'regiao': 'Sudeste'},
                         'Tubuna': {'descricao': 'Produtora de mel escuro e intenso. Ninhos em cavidades de '
                                                 'árvores. Muito sensível à desflorestação. Usada em '
                                                 'projetos de restauração de fragmentos florestais como '
                                                 'polinizadora-chave.',
                                    'bioma': 'Mata Atlântica',
                                    'regiao': 'Sudeste/Sul'},
                         'Mirim Guaçu': {'descricao': 'Espécie resistente ao frio. Muito comum em Santa '
                                                      'Catarina e Rio Grande do Sul. Polinizadora de '
                                                      'espécies nativas e cultivadas da região Sul. Mel com '
                                                      'sabor ácido característico.',
                                         'bioma': 'Sul/Sudeste',
                                         'regiao': 'Sul/Sudeste'},
                         'Abelha Mamangava': {'descricao': 'Polinizadora exclusiva do maracujá. Sem ela, a '
                                                           'produção de maracujá no Brasil colapsaria. Usa '
                                                           "técnica de 'buzz pollination' vibrando as flores "
                                                           'para liberar o pólen. Constroem ninhos em galhos '
                                                           'secos.',
                                              'habitat': 'Nidifica em madeira morta',
                                              'polinizacao': 'Buzz pollination — vibra para soltar pólen'},
                         'Abelha Carpinteira': {'descricao': 'Gênero Xylocopa com mais de 50 espécies no '
                                                             "Brasil. 'Carpinteira' pela habilidade de "
                                                             'escavar madeira para ninhos. Polinizadoras '
                                                             'importantes de flores tubulares. Ninhos em '
                                                             'hotéis de abelhas com canudos de bambu.',
                                                'habitat': 'Madeira seca, bambu',
                                                'polinizacao': 'Generalista — alta diversidade floral'},
                         'Abelha Mascarada': {'descricao': 'Minúscula mas essencial. Transporta pólen no '
                                                           'papo, não em corbículas. Carregam néctar e pólen '
                                                           'internamente. Responde muito bem a hotéis de '
                                                           'abelhas com canudos de papel e bambu de diâmetro '
                                                           '5–6 mm.',
                                              'habitat': 'Canudos, galhos ocos',
                                              'polinizacao': 'Flores pequenas e abertas'},
                         'Abelha Cortadeira': {'descricao': 'Cortam pedaços de folhas para construir seus '
                                                            "ninhos — daí o nome. São vistas como 'pragas' "
                                                            'mas são polinizadoras nativas essenciais. '
                                                            'Ninhos em buracos de madeira (broca 8–10 mm '
                                                            'ideal para hotéis).',
                                               'habitat': 'Solo, madeira, folhas cortadas',
                                               'polinizacao': 'Espécies nativas — Cerrado, Mata Atlântica'},
                         'Abelha Nômade': {'descricao': 'Abelhas cleptoparasitas que depositam ovos nos '
                                                        'ninhos de outras abelhas solitárias. Parecem vespas '
                                                        'mas são abelhas. Fundamentais para regular '
                                                        'populações e manter equilíbrio ecológico em '
                                                        'ambientes florestais.',
                                           'habitat': 'Parasita de outros ninhos',
                                           'polinizacao': 'Indireta — mantém equilíbrio ecológico'},
                         'Abelha Oleiro': {'descricao': 'Polinizadoras obrigatórias das murici, barbatimão e '
                                                        'outras Malpighiaceae. Coletam óleo floral nas '
                                                        'flores para alimentar suas larvas. Ninhos em solo. '
                                                        'Indicadoras de Cerrado preservado.',
                                           'habitat': 'Solo arenoso, paredões',
                                           'polinizacao': 'Buzzing em flores de óleo — Malpighiaceae'}},
        'back_link': '← Portfólio',
        'lang_label': 'Idioma',
        'cluster_name': 'Ocorrências',
        'footer_copy': '© 2022–2026 · Observatório Meliponini · Brasil',
        'raw_cols': {'especie': 'Espécie',
                     'cientifico': 'Nome Científico',
                     'tamanho': 'Tamanho',
                     'raio': 'Raio Forrageamento (m)',
                     'mel': 'Produção Mel',
                     'iucn': 'IUCN',
                     'bioma': 'Bioma',
                     'registros': 'Registros GBIF',
                     'colonia': 'Colônia (op.)',
                     'mel_ano': 'Mel/ano (kg)',
                     'habitat': 'Habitat',
                     'polinizacao': 'Polinização',
                     'tipo': 'Tipo'},
        'tipo_vals': {'meli': 'Meliponini', 'sol': 'Solitária'},
        'tok_nd': 'milhares de',
        'tok_and': ' e ',
        'tok_sp_top': 'SP concentra {n} registros GBIF — mais que qualquer outro estado.',
        'tok_sp_plain': 'SP concentra {n} registros GBIF.',
        'tok_sp_generic': 'SP está entre os estados mais bem amostrados.'},
 'en': {'page_title': 'Meliponini Observatory · Brazil',
        'hero_tag': 'BIODIVERSITY · MELIPONINI · BRAZIL · 2022–2025',
        'hero_title': 'Stingless Bee\nObservatory',
        'hero_subtitle': 'Monitoring and analysis of native stingless bee (Meliponini) and solitary bee '
                         'distribution in Brazil — 24,000+ GBIF records, 12 mapped species. Includes '
                         'technical visit to Cidade das Abelhas (SP, 2022) and solitary bee hotel at FATEC '
                         'Jundiaí.',
        'badge1': '🐝 12 monitored species',
        'badge2': '🗺️ 300+ occurrence points',
        'badge3': 'Brazil · 5 Biomes',
        'badge4': 'GBIF · iNaturalist · INPA',
        'badge5': 'Final Project FATEC Jundiaí 2022',
        'm1': 'Meliponini species',
        'm2': 'GBIF records (2024)',
        'm3': 'States covered',
        'm4': 'Threatened species',
        'tab1': '🗺️ Map & Analysis',
        'tab2': '🔬 Methodology & Pipeline',
        'tab3': '💡 What We Found',
        'tab4': '📷 Field Research',
        'tab5': '📈 Trends',
        'tab6': '⚙️ Parameters',
        'tab7': '📋 Raw Data',
        'tab8': '📚 Sources & Credits',
        'map_label': 'DISTRIBUTION IN BRAZIL',
        'map_title': 'Occurrence Map — Stingless Bees',
        'map_hint': '🐝 <strong>Click markers</strong> to see species, biome and source.',
        'heat_title': 'Heat Map — Occurrence Density',
        'chart_label': 'COMPARATIVE ANALYSIS',
        'sp_registros_title': 'Records by Species (GBIF, 2024)',
        'estado_title': 'Records by State',
        'bioma_title': 'Distribution by Biome',
        'method_label': 'APPLIED BIODIVERSITY',
        'method_title': 'Research Question & Methodology',
        'sci_q_title': '❓ Central Question',
        'sci_q': '"What is the current distribution and conservation status of Brazil\'s native stingless '
                 'bees, and how can rational meliponiculture and solitary bee hotels contribute to species '
                 'preservation in urban and peri-urban environments?"',
        'pipeline_label': 'DATA PIPELINE',
        'steps': [['1',
                   'Data — GBIF + iNaturalist (2010–2024)',
                   '@@TOTAL@@ georeferenced Meliponini records (2010–2024). 12 native Meliponini + 6 '
                   'solitary bee species.'],
                  ['2',
                   'Technical Visit — Cidade das Abelhas (SP, 2022)',
                   'Visit to the Cidade das Abelhas Park in São Paulo. Photographic record of Jataí, '
                   'Mosquitinho, Manduri and Mirim Preguiça in rational hives.'],
                  ['3',
                   'Final Project FATEC Jundiaí — Solitary Bee Hotel (2022)',
                   'Built solitary bee hotel at FATEC Jundiaí campus. Wood structure with 8 and 10 mm drill '
                   'holes.'],
                  ['4',
                   'Spatial Analysis — Distribution by Biome',
                   'Occurrence overlay with IBGE biome shapefile. Atlantic Forest = highest Meliponini '
                   'diversity (~22 species).'],
                  ['5',
                   'Biological Parameters — Scientific Literature',
                   'Compiled data: colony size, laying rate, worker lifespan, foraging radius, honey '
                   'production.'],
                  ['6',
                   'Threat Assessment — IUCN Red List',
                   '@@VU@@ Vulnerable (VU) species, @@LC@@ Least Concern (LC). Trend analysis and anthropic '
                   'pressure by biome.']],
        'biologia_title': '🐝 Why Stingless Bees Matter?',
        'biologia_text': '• <b>~550 Meliponini species</b> worldwide · <b>~350 in Brazil</b><br>• '
                         '<b>Exclusive pollinators</b> of Atlantic Forest and Cerrado native species<br>• '
                         '<b>Honey with medicinal properties</b> recognized by ANVISA<br>• '
                         '<b>Meliponiculture:</b> rational rearing in INPA, IBAMA, JTB hives<br>• '
                         '<b>Threats:</b> deforestation, pesticides, urbanization',
        'solitarias_title': '🏨 Solitary Bees — The Silent Majority',
        'solitarias_text': '• <b>~70% of bees worldwide</b> are solitary<br>• <b>Bee hotels</b> (wood blocks '
                           'with 6–10 mm holes) attract Xylocopa, Megachile, Hylaeus<br>• <b>Ideal '
                           'holes:</b> 8 mm drill (Megachile), 10 mm (Xylocopa) — minimum 10 cm depth<br>• '
                           '<b>Installation:</b> East/Southeast orientation, 1–2 m height, rain shelter',
        'disc_label': 'ANALYSIS & FINDINGS',
        'disc_title': 'What the Data Revealed',
        'discoveries': [['🐝',
                         'Jataí — the most urban-adapted species',
                         'Tetragonisca angustula shows the greatest adaptability to urban environments. '
                         'Records in all Brazilian states.'],
                        ['⚠️',
                         '@@VU@@ Vulnerable species — @@VU_LIST@@',
                         'Larger Melipona species are the most threatened. Deforestation + low reproduction '
                         '= population collapse.'],
                        ['🏨',
                         'Bee Hotel — urban biodiversity multiplier',
                         'The hotel built at FATEC Jundiaí was occupied in 30–60 days. <R$50 intervention '
                         'with high pollination impact.'],
                        ['📊', "São Paulo — Brazil's meliponiculture capital", '@@SP_SENT@@'],
                        ['🌎',
                         'GBIF: @@GROWTH@@ in 10 years — citizen science impact',
                         'Meliponini records grew @@GROWTH@@ between 2014 and 2024, alongside iNaturalist '
                         'adoption and rising interest in urban meliponiculture.'],
                        ['🌿',
                         'Cerrado — under-sampled with hidden diversity',
                         '~100 endemic species, but historically under-sampled in biodiversity records.']],
        'conclusion_label': 'CONCLUSION',
        'conclusion_title': 'Every Hive Counts',
        'conclusion_text': "Brazil's native stingless bees are a unique biocultural heritage. The "
                           '@@GROWTH_N@@ growth in GBIF Meliponini records shows rising interest in '
                           'meliponiculture — but deforestation still outpaces conservation. Every rational '
                           'hive installed, every bee hotel built, every forest fragment protected is a vote '
                           'of confidence in the future of these species.',
        'conclusion_author': 'Amauri Almeida · Environmental Management · FATEC Jundiaí · 2022 · Cidade das '
                             'Abelhas Visit SP',
        'field_label': 'FIELD AND TECHNICAL RECORD',
        'field_title': 'From Cidade das Abelhas to FATEC Campus',
        'field_inst_title': '📁 How to add your photos',
        'field_inst': 'Place your photos in <code>assets/campo/</code> with the exact file names shown.',
        'photos': [{'emoji': '🐝',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Rational Hive — Jataí Bee',
                    'esp': 'Tetragonisca angustula',
                    'desc': 'Rational hive (JTB or INPA box) of the Jataí bee at Cidade das Abelhas Park, '
                            'São Paulo.',
                    'path': 'assets/campo/01_colmeia_jatai_cidade_abelhas.jpg',
                    'legenda': 'Jataí Hive · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🔎',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Rational Hive — Mosquitinho',
                    'esp': 'Plebeia mosquito',
                    'desc': "Mosquitinho rational hive — one of Brazil's smallest stingless bees (2 mm). "
                            'Extremely docile.',
                    'path': 'assets/campo/02_colmeia_mosquitinho_cidade_abelhas.jpg',
                    'legenda': 'Mosquitinho Hive · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🌿',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Rational Hive — Manduri (1)',
                    'esp': 'Melipona marginata',
                    'desc': 'Manduri rational hive (VU). Threatened species, rare honey, nests exclusively '
                            'in native tree hollows.',
                    'path': 'assets/campo/04_colmeia_manduri_cidade_abelhas_1.jpg',
                    'legenda': 'Manduri Hive · VU · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🌿',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Rational Hive — Manduri (2)',
                    'esp': 'Melipona marginata',
                    'desc': 'Second Manduri hive. Different rational hive models documented.',
                    'path': 'assets/campo/05_colmeia_manduri_cidade_abelhas_2.jpg',
                    'legenda': 'Manduri Hive (2) · VU · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Rational Hive — Mirim Preguiça (1)',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'Mirim Preguiça rational hive. Calm behavior, key pollinator of Cerrado species.',
                    'path': 'assets/campo/06_colmeia_mirim_preguica_1.jpg',
                    'legenda': 'Mirim Preguiça Hive (1) · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Rational Hive — Mirim Preguiça (2)',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'Second view of the Mirim Preguiça hive. Species-specific architecture.',
                    'path': 'assets/campo/07_colmeia_mirim_preguica_2.jpg',
                    'legenda': 'Mirim Preguiça Hive (2) · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Rational Hive — Mirim Preguiça (3)',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'Third angle of Mirim Preguiça hive showing support details.',
                    'path': 'assets/campo/08_colmeia_mirim_preguica_3.jpg',
                    'legenda': 'Mirim Preguiça Hive (3) · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🏛️',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Meliponary — Species Collection',
                    'esp': 'Multiple species',
                    'desc': 'Meliponary view with distinct species side by side, following rational '
                            'meliponiculture best practices.',
                    'path': 'assets/campo/09_meliponario_colecao_cidade_abelhas.jpg',
                    'legenda': 'Meliponary · Distinct species · Cidade das Abelhas · SP · 2022',
                    'destaque': True,
                    'gid': 'cidade'},
                   {'emoji': '🌳',
                    'grupo': 'BEE HOTEL · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Hotel Construction — Wood Structure',
                    'esp': 'For solitary bees',
                    'desc': 'Starting the Solitary Bee Hotel construction at FATEC Jundiaí campus.',
                    'path': 'assets/campo/10_hotel_abelhas_estrutura_madeira.jpg',
                    'legenda': 'Bee Hotel · Wood structure · FATEC Jundiaí · 2022',
                    'gid': 'hotel'},
                   {'emoji': '🔩',
                    'grupo': 'BEE HOTEL · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Drilling Blocks — 8 and 10 mm Bits',
                    'esp': 'For solitary bees',
                    'desc': 'Drilling with 8 mm (Megachile) and 10 mm (Xylocopa) drill bits. Minimum 10 cm '
                            'depth.',
                    'path': 'assets/campo/11_hotel_abelhas_furadeira_broca8_10.jpg',
                    'legenda': '8/10 mm drilling · Solitary Bee Hotel · FATEC Jundiaí · 2022',
                    'gid': 'hotel'},
                   {'emoji': '🔩',
                    'grupo': 'BEE HOTEL · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Drilling Detail',
                    'esp': 'For solitary bees',
                    'desc': 'Detail of the drilling process: precise diameter and smooth interior surface '
                            'for solitary bees.',
                    'path': 'assets/campo/12_hotel_abelhas_furos_detalhe.jpg',
                    'legenda': 'Hole detail · Solitary Bee Hotel · FATEC Jundiaí · 2022',
                    'gid': 'hotel'},
                   {'emoji': '✅',
                    'grupo': 'BEE HOTEL · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Completed Bee Hotel — FATEC Jundiaí Campus',
                    'esp': 'For solitary bees',
                    'desc': 'Completed hotel for Ciência na Praça event. <R$50 structure with high local '
                            'pollination impact.',
                    'path': 'assets/campo/13_hotel_abelhas_concluido_fatec_jundiai.jpg',
                    'legenda': 'Completed Bee Hotel · FATEC Jundiaí Campus · 2022',
                    'destaque_final': True,
                    'gid': 'hotel'}],
        'timeline_label': 'PROJECT TIMELINE',
        'timeline_items': [['2022 · Jan–Jun',
                            'Final Project — FATEC Jundiaí',
                            'Meliponiculture and solitary bee research · Bee hotel built for Ciência na '
                            'Praça'],
                           ['2022 · Jul',
                            'Technical Visit — Cidade das Abelhas SP',
                            'Photographic record of 8+ species in rational hives'],
                           ['2022 · Nov',
                            'Project Defense — FATEC Jundiaí',
                            'Environmental Management degree approved'],
                           ['2023–2024',
                            'GBIF Analysis — @@TOTAL@@ records',
                            'Occurrence data crossed with biomes and states'],
                           ['2025',
                            'Portfolio Publication',
                            'Meliponini Observatory Brazil — public dashboard']],
        'trend_sel': 'Select visualization',
        'trend_opt1': 'GBIF Growth (2010–2024)',
        'trend_opt2': 'Records by Species (ranking)',
        'trend_opt3': 'Records by State',
        'param_sel': 'Species for analysis',
        'param_names': {'colonia': 'Colony size (workers)',
                        'postura_dia': 'Laying rate (eggs/day)',
                        'vida_operaria': 'Worker lifespan (days)',
                        'longe_formag': 'Foraging radius (m)',
                        'prod_mel_kg': 'Honey production (kg/yr)',
                        'raio_dna_km': 'Genetic distance (km)'},
        'raw_label': 'SPECIES CATALOG',
        'raw_title': 'Complete Table — Brazilian Meliponini',
        'download_csv': '⬇️ Download CSV',
        'sources_label': 'SCIENTIFIC SOURCES',
        'sources_title': 'Sources & Database',
        'tech_label': 'TECHNOLOGIES USED',
        'footer_title': '🐝 Amauri Almeida',
        'footer_desc': 'Environmental Management Technologist · FATEC Jundiaí (3rd ENADE)<br>Post-Grad in '
                       'AI, Machine Learning & Data Science · Data Science & Big Data<br>Systems Analysis '
                       'and Development · FACINT Maringá',
        'footer_links': '📍 Fernandópolis · SP · Brazil',
        'trend_label': 'TIME TRENDS & RANKINGS',
        'param_label': 'COMPARATIVE BIOLOGY',
        'param_title': 'Biological Parameters by Species',
        'param_detail': 'Biological parameter',
        'param_cmp': 'Species Comparison',
        'records_axis': 'Records',
        'records_hover': 'records',
        'gal_meli': 'SPECIES GALLERY — MELIPONINI',
        'gal_sol': 'GALLERY — SOLITARY BEES',
        'honey': 'Honey',
        'mel_vals': {'Sim': 'Yes', 'Não': 'No', 'Pouco': 'Little'},
        'gbif_records': 'GBIF records',
        'pop_records': 'Records',
        'pop_species': 'Species',
        'pop_status': 'Status',
        'status_vals': {'Alta': 'High', 'Média': 'Medium', 'Baixa': 'Low'},
        'radar_title': 'Species Comparison Profile (0–10 scale)',
        'radar_cats': ['Honey production', 'Urban adaptation', 'Flight range', 'Colony size', 'IUCN (inv.)'],
        'grp_city': '🏛️ CIDADE DAS ABELHAS (BEE CITY) · SÃO PAULO · 2022',
        'grp_hotel': '🏨 SOLITARY BEE HOTEL · FATEC JUNDIAÍ · CIÊNCIA NA PRAÇA · 2022',
        'dest_melipon': '⭐ HIGHLIGHT — COMPLETE MELIPONARY · CIDADE DAS ABELHAS',
        'dest_hotel': '✅ FINAL HIGHLIGHT — COMPLETED HOTEL · FATEC JUNDIAÍ CAMPUS',
        'hotel_build_title': '🏗️ How to build a Solitary Bee Hotel',
        'hotel_build': [['Material', 'Wood block (treated pine or eucalyptus) · 15×10×10 cm minimum'],
                        ['Holes', '8 mm bit (Megachile, Hylaeus) · 10 mm bit (Xylocopa)'],
                        ['Depth', 'At least 10 cm · Blind end (do not drill through the block!)'],
                        ['Orientation', 'East or Southeast · Gets morning sun'],
                        ['Height', '1–2 m above ground · Sheltered from rain and wind'],
                        ['Result', 'Occupied within 30–60 days by native bees']],
        'solitary_tbl': 'Solitary Bees',
        'card_lbls': {'biome': 'Biome',
                      'region': 'Region',
                      'colony': 'Colony',
                      'workers': 'workers',
                      'laying': 'Laying rate',
                      'eggs_day': 'eggs/day',
                      'worker_life': 'Worker lifespan',
                      'days': 'days',
                      'forage': 'Foraging radius',
                      'honey': 'Honey yield',
                      'kg_year': 'kg/year',
                      'gen_dist': 'Genetic distance'},
        'carto_fallback': 'Fallback basemap (OpenStreetMap) in use.',
        'occ_live': 'Real GBIF points (api.gbif.org): {n} georeferenced occurrences in Brazil, up to {k} per '
                    'species, queried on {d}. Click a point to open the original record.',
        'occ_demo': 'GBIF currently unavailable: the points shown are ILLUSTRATIVE (capital cities × '
                    'species), not field records.',
        'occ_none': 'GBIF currently unavailable and no fallback data: occurrence map not shown.',
        'dados_live': 'Figures computed from GBIF (api.gbif.org), queried on {d}; refreshed automatically '
                      'every 24 h.',
        'dados_snapshot': 'GBIF unavailable right now: figures from the last saved snapshot ({d}).',
        'dados_static': 'GBIF unavailable right now: reference values from an earlier compilation, not '
                        'updated.',
        'serie_total': 'Total (Meliponini + 5 solitary genera)',
        'serie_inat': 'iNaturalist (Meliponini)',
        'raio_sel': 'Show foraging radius (circles in meters)',
        'raio_note': "Each circle shows the species' mean flight radius around real occurrences (up to {n} "
                     'per species). Zoom in to see the scale.',
        'raio_layer': 'Foraging radius',
        'footer_portfolio': 'Portfolio',
        'sources': [['GBIF',
                     'GBIF — Global Biodiversity Information Facility',
                     'gbif.org · Occurrence database with @@TOTAL@@ georeferenced Meliponini records in '
                     'Brazil (2010–2024). Data from museums, herbaria, iNaturalist and researchers.',
                     '#C47D0E'],
                    ['A.B.E.L.H.A.',
                     'A.B.E.L.H.A. — Brazilian Association for Bee Studies',
                     'abelha.org.br · Atlas of Stingless Beekeeping in Brazil. Reference for foraging radii, '
                     'biology and conservation.',
                     '#C0390A'],
                    ['INATURALIST',
                     'iNaturalist — Global Citizen Science',
                     'inaturalist.org · @@INAT@@ georeferenced Brazilian Meliponini records (iNaturalist '
                     'Research-grade dataset on GBIF). Main driver of GBIF growth.',
                     '#2D7A45'],
                    ['FATEC',
                     'FATEC Jundiaí — Environmental Management Thesis (2022)',
                     'Solitary Bee Hotel built on campus for the Ciência na Praça event. 8 and 10 mm drill '
                     'bits. Approved with distinction.',
                     '#1B3A1E'],
                    ['CIDADE ABELHAS',
                     'Cidade das Abelhas Park — São Paulo (2022)',
                     'Technical visit in 2022. Photo record of rational hives of Jataí, Mosquitinho, '
                     'Manduri, Mirim Preguiça and others.',
                     '#5C3D1E'],
                    ['IUCN',
                     'IUCN Red List — Threatened Species',
                     '@@VU_TAGS@@. Conservation status of Brazilian Meliponini.',
                     '#8B2515'],
                    ['INPA',
                     'INPA — National Institute for Amazonian Research',
                     'INPA rational hive model for Amazonian Meliponini. Species data from northern Brazil.',
                     '#0D4E72'],
                    ['EMBRAPA',
                     'EMBRAPA Cerrados / EMBRAPA Amazônia Oriental',
                     'Stingless beekeeping data across Brazilian biomes. Technical reference for Cerrado and '
                     'Amazon species.',
                     '#C47D0E']],
        'species_text': {'Jataí': {'descricao': "Brazil's best-known stingless bee. Produces extremely "
                                                'high-quality honey with medicinal properties. Nests in tree '
                                                'hollows and masonry crevices. Seals the entrance with '
                                                'propolis, as a tube or in pellets.',
                                   'bioma': 'All',
                                   'regiao': 'National'},
                         'Mosquitinho': {'descricao': 'One of the smallest stingless bees in Brazil. '
                                                      'Extremely docile. Produces a very tasty honey in '
                                                      'small quantities. Highly sensitive to pesticides. An '
                                                      'indicator of environmental quality.',
                                         'bioma': 'Atlantic Forest',
                                         'regiao': 'South/Southeast'},
                         'Manduri': {'descricao': 'Species threatened with extinction (VU). Rare honey, '
                                                  'produced in small quantities. Nests are usually in '
                                                  'cavities of native trees. A target species of '
                                                  'meliponiculture programs for conservation.',
                                     'bioma': 'Atlantic Forest',
                                     'regiao': 'South/Southeast'},
                         'Mirim Preguiça': {'descricao': "Also called the 'Abelha Preguiça' (lazy bee) for "
                                                         'its calm behavior. Nests mainly on tree branches. '
                                                         'An important pollinator of native species of the '
                                                         'Cerrado and the Atlantic Forest.',
                                            'bioma': 'Cerrado/Atlantic Forest',
                                            'regiao': 'Center/Southeast'},
                         'Mandaçaia': {'descricao': 'One of the largest stingless bees. Distinctive honey '
                                                    'production. In decline due to deforestation and '
                                                    'urbanization. Kept for centuries by the Guarani '
                                                    "Indigenous people as 'mborí'.",
                                       'bioma': 'Atlantic Forest',
                                       'regiao': 'Southeast/South'},
                         'Uruçu Nordestina': {'descricao': 'Sacred bee of the Tupinambá, cultivated for over '
                                                           '2,000 years. Honey with recognized medicinal '
                                                           'properties. A symbol of Northeastern '
                                                           'meliponiculture. Flagship species of Indigenous '
                                                           'beekeeping.',
                                              'bioma': 'Caatinga/Atlantic Forest NE',
                                              'regiao': 'Northeast'},
                         'Irapuá': {'descricao': 'Although it does not produce honey in commercial '
                                                 'quantities, it is a highly important pollinator. Builds '
                                                 'exposed nests from plant resin. Sometimes mistaken for the '
                                                 'European honey bee because of its defensive behavior.',
                                    'bioma': 'All',
                                    'regiao': 'National'},
                         'Tiúba': {'descricao': "Known as 'Abelha da Terra' (earth bee) in Maranhão. Honey "
                                                'with a unique, much-appreciated flavor. A fundamental part '
                                                'of the meliponiculture culture of the Amazon and Maranhão. '
                                                'A species at risk from deforestation.',
                                   'bioma': 'Amazon/Northeast',
                                   'regiao': 'North/Northeast'},
                         'Guaraipo': {'descricao': 'Species with a variable color pattern. Produces honey '
                                                   'with a mild flavor. Nests in the ground or in trunks. In '
                                                   'marked decline due to the expansion of agriculture and '
                                                   'livestock in the Cerrado.',
                                      'bioma': 'Cerrado/Atlantic Forest',
                                      'regiao': 'Central-West/Southeast'},
                         'Iraí': {'descricao': 'A bee very common in urban environments. Nests in wall '
                                               'crevices, electrical boxes and roof tiles. Highly tolerant '
                                               'of urbanization. An excellent indicator of connectivity '
                                               'between forest fragments.',
                                  'bioma': 'Cerrado/Atlantic Forest',
                                  'regiao': 'Southeast'},
                         'Tubuna': {'descricao': 'Producer of dark, intense honey. Nests in tree cavities. '
                                                 'Highly sensitive to deforestation. Used in forest-fragment '
                                                 'restoration projects as a key pollinator.',
                                    'bioma': 'Atlantic Forest',
                                    'regiao': 'Southeast/South'},
                         'Mirim Guaçu': {'descricao': 'Cold-resistant species. Very common in Santa Catarina '
                                                      'and Rio Grande do Sul. Pollinator of native and '
                                                      'cultivated species in the South region. Honey with a '
                                                      'characteristic tangy flavor.',
                                         'bioma': 'South/Southeast',
                                         'regiao': 'South/Southeast'},
                         'Abelha Mamangava': {'descricao': 'Exclusive pollinator of passion fruit. Without '
                                                           'it, passion fruit production in Brazil would '
                                                           "collapse. Uses 'buzz pollination', vibrating the "
                                                           'flowers to release pollen. Builds nests in dry '
                                                           'branches.',
                                              'habitat': 'Nests in dead wood',
                                              'polinizacao': 'Buzz pollination — vibrates to release pollen'},
                         'Abelha Carpinteira': {'descricao': 'Genus Xylocopa, with more than 50 species in '
                                                             "Brazil. Called 'carpenter' bees for their "
                                                             'skill at excavating wood for nests. Important '
                                                             'pollinators of tubular flowers. Nests in bee '
                                                             'hotels with bamboo straws.',
                                                'habitat': 'Dry wood, bamboo',
                                                'polinizacao': 'Generalist — high floral diversity'},
                         'Abelha Mascarada': {'descricao': 'Tiny but essential. Carries pollen in its crop, '
                                                           'not in pollen baskets (corbiculae). Transports '
                                                           'nectar and pollen internally. Responds very well '
                                                           'to bee hotels with paper and bamboo straws 5–6 '
                                                           'mm in diameter.',
                                              'habitat': 'Straws, hollow twigs',
                                              'polinizacao': 'Small, open flowers'},
                         'Abelha Cortadeira': {'descricao': 'They cut pieces of leaves to build their nests '
                                                            "— hence the name. They are seen as 'pests' but "
                                                            'are essential native pollinators. Nests in '
                                                            'holes in wood (an 8–10 mm drill bit is ideal '
                                                            'for bee hotels).',
                                               'habitat': 'Soil, wood, cut leaves',
                                               'polinizacao': 'Native species — Cerrado, Atlantic Forest'},
                         'Abelha Nômade': {'descricao': 'Cleptoparasitic bees that lay their eggs in the '
                                                        'nests of other solitary bees. They look like wasps '
                                                        'but are bees. Fundamental for regulating '
                                                        'populations and maintaining ecological balance in '
                                                        'forest environments.',
                                           'habitat': 'Parasite of other nests',
                                           'polinizacao': 'Indirect — maintains ecological balance'},
                         'Abelha Oleiro': {'descricao': 'Obligate pollinators of murici, barbatimão and '
                                                        'other Malpighiaceae. They collect floral oil from '
                                                        'flowers to feed their larvae. Nests in the ground. '
                                                        'Indicators of preserved Cerrado.',
                                           'habitat': 'Sandy soil, cliff faces',
                                           'polinizacao': 'Buzzing on oil flowers — Malpighiaceae'}},
        'back_link': '← Portfolio',
        'lang_label': 'Language',
        'cluster_name': 'Occurrences',
        'footer_copy': '© 2022–2026 · Observatório Meliponini · Brasil',
        'raw_cols': {'especie': 'Species',
                     'cientifico': 'Scientific Name',
                     'tamanho': 'Size',
                     'raio': 'Foraging Radius (m)',
                     'mel': 'Honey Production',
                     'iucn': 'IUCN',
                     'bioma': 'Biome',
                     'registros': 'GBIF Records',
                     'colonia': 'Colony (op.)',
                     'mel_ano': 'Honey/year (kg)',
                     'habitat': 'Habitat',
                     'polinizacao': 'Pollination',
                     'tipo': 'Type'},
        'tipo_vals': {'meli': 'Meliponini', 'sol': 'Solitary'},
        'tok_nd': 'thousands of',
        'tok_and': ' and ',
        'tok_sp_top': 'SP accounts for {n} GBIF records — more than any other state.',
        'tok_sp_plain': 'SP accounts for {n} GBIF records.',
        'tok_sp_generic': 'SP is among the best-sampled states.'},
 'es': {'page_title': 'Observatorio Meliponini · Brasil',
        'hero_tag': 'BIODIVERSIDAD · MELIPONINI · BRASIL · 2022–2025',
        'hero_title': 'Observatorio de\nAbejas Sin Aguijón',
        'hero_subtitle': 'Monitoreo y análisis de la distribución de las abejas sin aguijón nativas '
                         '(Meliponini) y abejas solitarias en Brasil — más de 24.000 registros GBIF, 12 '
                         'especies mapeadas.',
        'badge1': '🐝 12 especies monitoreadas',
        'badge2': '🗺️ 300+ puntos de ocurrencia',
        'badge3': 'Brasil · 5 Biomas',
        'badge4': 'GBIF · iNaturalist · INPA',
        'badge5': 'TCC FATEC Jundiaí 2022',
        'm1': 'Especies Meliponini',
        'm2': 'Registros GBIF (2024)',
        'm3': 'Estados cubiertos',
        'm4': 'Especies amenazadas',
        'tab1': '🗺️ Mapa & Análisis',
        'tab2': '🔬 Metodología & Pipeline',
        'tab3': '💡 Lo que Descubrimos',
        'tab4': '📷 En Campo',
        'tab5': '📈 Tendencias',
        'tab6': '⚙️ Parámetros',
        'tab7': '📋 Datos Brutos',
        'tab8': '📚 Fuentes & Créditos',
        'map_label': 'DISTRIBUCIÓN EN BRASIL',
        'map_title': 'Mapa de Ocurrencias — Abejas Sin Aguijón',
        'map_hint': '🐝 <strong>Haga clic en los marcadores</strong> para ver especie, bioma y fuente.',
        'heat_title': 'Mapa de Calor — Densidad de Ocurrencias',
        'chart_label': 'ANÁLISIS COMPARATIVO',
        'sp_registros_title': 'Registros por Especie (GBIF, 2024)',
        'estado_title': 'Registros por Estado',
        'bioma_title': 'Distribución por Bioma',
        'method_label': 'BIODIVERSIDAD APLICADA',
        'method_title': 'Pregunta & Metodología',
        'sci_q_title': '❓ Pregunta Central',
        'sci_q': '"¿Cuál es el estado actual de la distribución y conservación de las abejas sin aguijón '
                 'nativas de Brasil, y cómo las prácticas de meliponicultura racional y hotelería para '
                 'abejas solitarias pueden contribuir a la preservación de estas especies en ambientes '
                 'urbanos?"',
        'pipeline_label': 'PIPELINE DE DATOS',
        'steps': [['1',
                   'Recolección — GBIF + iNaturalist (2010–2024)',
                   '@@TOTAL@@ registros georreferenciados de Meliponini brasileños (2010–2024). 12 '
                   'Meliponini nativas + 6 abejas solitarias.'],
                  ['2',
                   'Visita Técnica — Ciudad de las Abejas (SP, 2022)',
                   'Visita al Parque Ciudad de las Abejas en São Paulo. Registro fotográfico de Jataí, '
                   'Mosquitinho, Manduri y Mirim Preguiça en colmenas racionales.'],
                  ['3',
                   'TCC FATEC Jundiaí — Hotel para Abejas Solitarias (2022)',
                   'Proyecto final: construcción de Hotel para Abejas Solitarias en el Campus FATEC Jundiaí. '
                   'Estructura en madera con agujeros broca 8 y 10 mm.'],
                  ['4',
                   'Análisis Espacial — Distribución por Bioma',
                   'Cruce de ocurrencias con shapefile de biomas del IBGE. Mata Atlántica como bioma de '
                   'mayor diversidad de Meliponini.'],
                  ['5',
                   'Parámetros Biológicos — Literatura Científica',
                   'Recopilación de datos: tamaño de colonia, tasa de postura, vida de la obrera, radio de '
                   'forrajeo, producción de miel.'],
                  ['6',
                   'Evaluación de Amenaza — Lista Roja IUCN',
                   '@@VU@@ especies Vulnerables (VU), @@LC@@ con Menor Preocupación (LC). Análisis de '
                   'tendencias y presiones antrópicas.']],
        'biologia_title': '🐝 ¿Por qué importan las Abejas Sin Aguijón?',
        'biologia_text': '• <b>~550 especies</b> de Meliponini en el mundo · <b>~350 en Brasil</b><br>• '
                         '<b>Polinizadoras exclusivas</b> de especies nativas de la Mata Atlántica y '
                         'Cerrado<br>• <b>Miel con propiedades medicinales</b> reconocidas<br>• '
                         '<b>Meliponicultura:</b> cría racional en cajas INPA, IBAMA, JTB<br>• '
                         '<b>Amenazas:</b> deforestación, agrotóxicos, urbanización',
        'solitarias_title': '🏨 Abejas Solitarias — La Mayoría Silenciosa',
        'solitarias_text': '• <b>~70% de las abejas del mundo</b> son solitarias<br>• <b>Hoteles de '
                           'abejas</b> con agujeros 6–10 mm atraen Xylocopa, Megachile, Hylaeus<br>• '
                           '<b>Agujeros ideales:</b> broca 8 mm (Megachile), 10 mm (Xylocopa) — profundidad '
                           'mínima 10 cm<br>• <b>Instalación:</b> orientación Este/Sureste, altura 1–2 m, '
                           'protegido de la lluvia',
        'disc_label': 'ANÁLISIS Y HALLAZGOS',
        'disc_title': 'Lo que los Datos Revelaron',
        'discoveries': [['🐝',
                         'Jataí — la más adaptada a la urbanización',
                         'Tetragonisca angustula es la especie con mayor adaptabilidad al ambiente urbano. '
                         'Registros en todos los estados.'],
                        ['⚠️',
                         '@@VU@@ especies Vulnerables — @@VU_LIST@@',
                         'Las especies de Melipona de mayor porte son las más amenazadas. Desforestación + '
                         'baja reproducción = colapso poblacional.'],
                        ['🏨',
                         'Hotel para Abejas — multiplicador de biodiversidad urbana',
                         'El Hotel construido en FATEC Jundiaí fue ocupado en 30–60 días. Intervención <R$50 '
                         'con alto impacto.'],
                        ['📊', 'São Paulo — capital meliponícola brasileña', '@@SP_SENT@@'],
                        ['🌎',
                         'GBIF: @@GROWTH@@ en 10 años — ciencia ciudadana',
                         'El crecimiento de Meliponini entre 2014 y 2024 (@@GROWTH@@) acompaña el aumento '
                         'del iNaturalist y la meliponicultura urbana.'],
                        ['🌿',
                         'Cerrado — bioma sub-muestreado con gran diversidad oculta',
                         '~100 especies endémicas, pero históricamente sub-muestreado en los registros de '
                         'biodiversidad.']],
        'conclusion_label': 'CONCLUSIÓN',
        'conclusion_title': 'Cada Colmena Cuenta',
        'conclusion_text': 'Las abejas sin aguijón nativas de Brasil son un patrimonio biocultural único. El '
                           'crecimiento del @@GROWTH_N@@ en registros GBIF de Meliponini muestra que el '
                           'interés por la meliponicultura está aumentando — pero el ritmo de deforestación '
                           'aún supera la velocidad de la conservación.',
        'conclusion_author': 'Amauri Almeida · TCC Gestión Ambiental · FATEC Jundiaí · 2022 · Visita Ciudad '
                             'de las Abejas SP',
        'field_label': 'REGISTRO DE CAMPO Y TÉCNICO',
        'field_title': 'De la Ciudad de las Abejas al Campus FATEC',
        'field_inst_title': '📁 Cómo agregar sus fotos',
        'field_inst': 'Coloque sus fotos en <code>assets/campo/</code> con los nombres exactos.',
        'photos': [{'emoji': '🐝',
                    'grupo': 'CIUDAD DE LAS ABEJAS · SÃO PAULO · 2022',
                    'titulo': 'Colmena Racional — Abeja Jataí',
                    'esp': 'Tetragonisca angustula',
                    'desc': 'Colmena racional (caja JTB o INPA) de la abeja Jataí en el Parque Ciudad de las '
                            'Abejas, São Paulo.',
                    'path': 'assets/campo/01_colmeia_jatai_cidade_abelhas.jpg',
                    'legenda': 'Colmena Jataí · Ciudad de las Abejas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🔎',
                    'grupo': 'CIUDAD DE LAS ABEJAS · SÃO PAULO · 2022',
                    'titulo': 'Colmena Racional — Mosquitinho',
                    'esp': 'Plebeia mosquito',
                    'desc': 'Colmena de Mosquitinho — una de las abejas más pequeñas de Brasil (2 mm). '
                            'Extremadamente dócil.',
                    'path': 'assets/campo/02_colmeia_mosquitinho_cidade_abelhas.jpg',
                    'legenda': 'Colmena Mosquitinho · Ciudad de las Abejas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🌿',
                    'grupo': 'CIUDAD DE LAS ABEJAS · SÃO PAULO · 2022',
                    'titulo': 'Colmena Racional — Manduri (1)',
                    'esp': 'Melipona marginata',
                    'desc': 'Colmena de Manduri (VU). Especie amenazada, miel rara, nidifica en huecos de '
                            'árboles nativos.',
                    'path': 'assets/campo/04_colmeia_manduri_cidade_abelhas_1.jpg',
                    'legenda': 'Colmena Manduri · VU · Ciudad de las Abejas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🌿',
                    'grupo': 'CIUDAD DE LAS ABEJAS · SÃO PAULO · 2022',
                    'titulo': 'Colmena Racional — Manduri (2)',
                    'esp': 'Melipona marginata',
                    'desc': 'Segunda colmena de Manduri. Diferentes modelos de cajas racionales '
                            'documentadas.',
                    'path': 'assets/campo/05_colmeia_manduri_cidade_abelhas_2.jpg',
                    'legenda': 'Colmena Manduri (2) · VU · Ciudad de las Abejas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIUDAD DE LAS ABEJAS · SÃO PAULO · 2022',
                    'titulo': 'Colmena Racional — Mirim Preguiça (1)',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'Colmena de Mirim Preguiça. Comportamiento tranquilo, importante polinizadora '
                            'del Cerrado.',
                    'path': 'assets/campo/06_colmeia_mirim_preguica_1.jpg',
                    'legenda': 'Colmena Mirim Preguiça (1) · Ciudad de las Abejas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIUDAD DE LAS ABEJAS · SÃO PAULO · 2022',
                    'titulo': 'Colmena Racional — Mirim Preguiça (2)',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'Segunda vista de la colmena de Mirim Preguiça. Arquitectura específica para '
                            'esta especie.',
                    'path': 'assets/campo/07_colmeia_mirim_preguica_2.jpg',
                    'legenda': 'Colmena Mirim Preguiça (2) · Ciudad de las Abejas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIUDAD DE LAS ABEJAS · SÃO PAULO · 2022',
                    'titulo': 'Colmena Racional — Mirim Preguiça (3)',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'Tercer ángulo de la colmena de Mirim Preguiça con detalles de soporte y '
                            'estructura.',
                    'path': 'assets/campo/08_colmeia_mirim_preguica_3.jpg',
                    'legenda': 'Colmena Mirim Preguiça (3) · Ciudad de las Abejas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🏛️',
                    'grupo': 'CIUDAD DE LAS ABEJAS · SÃO PAULO · 2022',
                    'titulo': 'Meliponario — Colección de Especies',
                    'esp': 'Múltiples especies',
                    'desc': 'Vista del meliponario con cajas de especies distintas lado a lado, según buenas '
                            'prácticas meliponícolas.',
                    'path': 'assets/campo/09_meliponario_colecao_cidade_abelhas.jpg',
                    'legenda': 'Meliponario · Especies distintas · Ciudad de las Abejas · SP · 2022',
                    'destaque': True,
                    'gid': 'cidade'},
                   {'emoji': '🌳',
                    'grupo': 'HOTEL DE ABEJAS · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Construcción del Hotel — Estructura en Madera',
                    'esp': 'Para abejas solitarias',
                    'desc': 'Inicio de la construcción del Hotel para Abejas Solitarias en el Campus FATEC '
                            'Jundiaí.',
                    'path': 'assets/campo/10_hotel_abelhas_estrutura_madeira.jpg',
                    'legenda': 'Hotel de Abejas · Estructura en madera · FATEC Jundiaí · 2022',
                    'gid': 'hotel'},
                   {'emoji': '🔩',
                    'grupo': 'HOTEL DE ABEJAS · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Perforando los Bloques — Broca 8 y 10 mm',
                    'esp': 'Para abejas solitarias',
                    'desc': 'Perforación con broca 8 mm (Megachile) y 10 mm (Xylocopa). Profundidad mínima '
                            '10 cm.',
                    'path': 'assets/campo/11_hotel_abelhas_furadeira_broca8_10.jpg',
                    'legenda': 'Perforación broca 8/10 mm · Hotel Abejas Solitarias · FATEC Jundiaí · 2022',
                    'gid': 'hotel'},
                   {'emoji': '🔩',
                    'grupo': 'HOTEL DE ABEJAS · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Detalle de Perforación',
                    'esp': 'Para abejas solitarias',
                    'desc': 'Detalle de los agujeros: diámetro preciso y superficie lisa interior para '
                            'abejas solitarias.',
                    'path': 'assets/campo/12_hotel_abelhas_furos_detalhe.jpg',
                    'legenda': 'Detalle agujeros · Hotel Abejas Solitarias · FATEC Jundiaí · 2022',
                    'gid': 'hotel'},
                   {'emoji': '✅',
                    'grupo': 'HOTEL DE ABEJAS · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Hotel de Abejas Concluido — Campus FATEC Jundiaí',
                    'esp': 'Para abejas solitarias',
                    'desc': 'Hotel concluido para el evento Ciencia en la Plaza. Estructura <R$50 con alto '
                            'impacto en polinización local.',
                    'path': 'assets/campo/13_hotel_abelhas_concluido_fatec_jundiai.jpg',
                    'legenda': 'Hotel de Abejas concluido · Campus FATEC Jundiaí · 2022',
                    'destaque_final': True,
                    'gid': 'hotel'}],
        'timeline_label': 'CRONOLOGÍA DEL PROYECTO',
        'timeline_items': [['2022 · Ene–Jun',
                            'TCC Gestión Ambiental — FATEC Jundiaí',
                            'Investigación sobre meliponicultura y abejas solitarias · Hotel construido para '
                            'Ciencia en la Plaza'],
                           ['2022 · Jul',
                            'Visita Técnica — Ciudad de las Abejas SP',
                            'Registro fotográfico de 8+ especies en colmenas racionales'],
                           ['2022 · Nov',
                            'Defensa del TCC — FATEC Jundiaí',
                            'Aprobación del Trabajo Final en Gestión Ambiental'],
                           ['2023–2024',
                            'Análisis GBIF — @@TOTAL@@ registros',
                            'Cruce de datos de ocurrencia con biomas y estados'],
                           ['2025',
                            'Publicación en Portfolio',
                            'Observatorio Meliponini Brasil — dashboard público']],
        'trend_sel': 'Seleccione visualización',
        'trend_opt1': 'Crecimiento GBIF (2010–2024)',
        'trend_opt2': 'Registros por Especie (ranking)',
        'trend_opt3': 'Registros por Estado',
        'param_sel': 'Especie para análisis',
        'param_names': {'colonia': 'Tamaño de colonia (obreras)',
                        'postura_dia': 'Tasa de postura (huevos/día)',
                        'vida_operaria': 'Vida de la obrera (días)',
                        'longe_formag': 'Radio de forrajeo (m)',
                        'prod_mel_kg': 'Producción de miel (kg/año)',
                        'raio_dna_km': 'Distancia genética (km)'},
        'raw_label': 'CATÁLOGO DE ESPECIES',
        'raw_title': 'Tabla Completa — Meliponini de Brasil',
        'download_csv': '⬇️ Descargar CSV',
        'sources_label': 'FUENTES CIENTÍFICAS',
        'sources_title': 'Fuentes & Base de Datos',
        'tech_label': 'TECNOLOGÍAS UTILIZADAS',
        'footer_title': '🐝 Amauri Almeida',
        'footer_desc': 'Tecnólogo en Gestión Ambiental · FATEC Jundiaí<br>Posgrado en IA, Machine Learning & '
                       'Data Science · Ciencia de Datos & Big Data<br>Análisis y Desarrollo de Sistemas · '
                       'FACINT Maringá',
        'footer_links': '📍 Fernandópolis · SP · Brasil',
        'trend_label': 'EVOLUCIÓN TEMPORAL Y RANKINGS',
        'param_label': 'BIOLOGÍA COMPARADA',
        'param_title': 'Parámetros Biológicos de las Especies',
        'param_detail': 'Parámetro biológico',
        'param_cmp': 'Comparativo entre Especies',
        'records_axis': 'Registros',
        'records_hover': 'registros',
        'gal_meli': 'GALERÍA DE ESPECIES — MELIPONINI',
        'gal_sol': 'GALERÍA — ABEJAS SOLITARIAS',
        'honey': 'Miel',
        'mel_vals': {'Sim': 'Sí', 'Não': 'No', 'Pouco': 'Poco'},
        'gbif_records': 'registros GBIF',
        'pop_records': 'Registros',
        'pop_species': 'Especies',
        'pop_status': 'Estado',
        'status_vals': {'Alta': 'Alta', 'Média': 'Media', 'Baixa': 'Baja'},
        'radar_title': 'Perfil Comparativo de las Especies (escala 0–10)',
        'radar_cats': ['Producción de miel',
                       'Adaptación urbana',
                       'Radio de vuelo',
                       'Tamaño de la colonia',
                       'IUCN (inv.)'],
        'grp_city': '🏛️ CIUDAD DE LAS ABEJAS · SÃO PAULO · 2022',
        'grp_hotel': '🏨 HOTEL DE ABEJAS SOLITARIAS · FATEC JUNDIAÍ · CIENCIA EN LA PLAZA · 2022',
        'dest_melipon': '⭐ DESTACADO — MELIPONARIO COMPLETO · CIUDAD DE LAS ABEJAS',
        'dest_hotel': '✅ DESTACADO FINAL — HOTEL CONCLUIDO · CAMPUS FATEC JUNDIAÍ',
        'hotel_build_title': '🏗️ Cómo construir un Hotel para Abejas Solitarias',
        'hotel_build': [['Material', 'Bloque de madera (pino tratado o eucalipto) · mínimo 15×10×10 cm'],
                        ['Agujeros', 'Broca 8 mm (Megachile, Hylaeus) · Broca 10 mm (Xylocopa)'],
                        ['Profundidad', 'Mínimo 10 cm · Fondo ciego (¡no atravesar el bloque!)'],
                        ['Orientación', 'Este o Sureste · Recibe sol de la mañana'],
                        ['Altura', '1–2 metros del suelo · Protegido de lluvia y viento'],
                        ['Resultado', 'Ocupación en 30–60 días por abejas nativas']],
        'solitary_tbl': 'Abejas Solitarias',
        'card_lbls': {'biome': 'Bioma',
                      'region': 'Región',
                      'colony': 'Colonia',
                      'workers': 'obreras',
                      'laying': 'Postura',
                      'eggs_day': 'huevos/día',
                      'worker_life': 'Vida de la obrera',
                      'days': 'días',
                      'forage': 'Radio de forrajeo',
                      'honey': 'Producción de miel',
                      'kg_year': 'kg/año',
                      'gen_dist': 'Dist. genética'},
        'carto_fallback': 'Mapa base alternativo (OpenStreetMap) en uso.',
        'occ_live': 'Puntos reales de GBIF (api.gbif.org): {n} ocurrencias georreferenciadas en Brasil, '
                    'hasta {k} por especie, consultadas el {d}. Haga clic en un punto para abrir el registro '
                    'original.',
        'occ_demo': 'GBIF no disponible por ahora: los puntos mostrados son ILUSTRATIVOS (capitales × '
                    'especies), no registros de campo.',
        'occ_none': 'GBIF no disponible y sin datos de respaldo: mapa de ocurrencias no mostrado.',
        'dados_live': 'Números calculados a partir de GBIF (api.gbif.org), consultados el {d}; actualización '
                      'automática cada 24 h.',
        'dados_snapshot': 'GBIF no disponible ahora: números del último snapshot guardado ({d}).',
        'dados_static': 'GBIF no disponible ahora: valores de referencia de una compilación anterior, sin '
                        'actualizar.',
        'serie_total': 'Total (Meliponini + 5 géneros solitarios)',
        'serie_inat': 'iNaturalist (Meliponini)',
        'raio_sel': 'Mostrar radio de forrajeo (círculos en metros)',
        'raio_note': 'Cada círculo muestra el radio medio de vuelo de la especie alrededor de ocurrencias '
                     'reales (hasta {n} por especie). Acerque el mapa para ver la escala.',
        'raio_layer': 'Radio de forrajeo',
        'footer_portfolio': 'Portafolio',
        'sources': [['GBIF',
                     'GBIF — Global Biodiversity Information Facility',
                     'gbif.org · Base de ocurrencias con @@TOTAL@@ registros georreferenciados de Meliponini '
                     'en Brasil (2010–2024). Datos de museos, herbarios, iNaturalist e investigadores.',
                     '#C47D0E'],
                    ['A.B.E.L.H.A.',
                     'A.B.E.L.H.A. — Asociación Brasileña de Estudio de las Abejas',
                     'abelha.org.br · Atlas de la Meliponicultura en Brasil. Referencia para radios de '
                     'forrajeo, biología y conservación.',
                     '#C0390A'],
                    ['INATURALIST',
                     'iNaturalist — Ciencia Ciudadana Global',
                     'inaturalist.org · @@INAT@@ registros de Meliponini brasileños con georreferencia '
                     '(dataset iNaturalist Research-grade en GBIF). Principal motor del crecimiento de GBIF.',
                     '#2D7A45'],
                    ['FATEC',
                     'FATEC Jundiaí — TCC Gestión Ambiental (2022)',
                     'Hotel para Abejas Solitarias construido en el Campus para el evento Ciência na Praça. '
                     'Brocas de 8 y 10 mm. Aprobado con distinción.',
                     '#1B3A1E'],
                    ['CIDADE ABELHAS',
                     'Parque Cidade das Abelhas — São Paulo (2022)',
                     'Visita técnica en 2022. Registro fotográfico de colmenas racionales de Jataí, '
                     'Mosquitinho, Manduri, Mirim Preguiça y otras.',
                     '#5C3D1E'],
                    ['IUCN',
                     'IUCN Red List — Lista Roja de Especies Amenazadas',
                     '@@VU_TAGS@@. Estado de conservación de los Meliponini brasileños.',
                     '#8B2515'],
                    ['INPA',
                     'INPA — Instituto Nacional de Investigaciones de la Amazonía',
                     'Modelo de colmena racional INPA para Meliponini amazónicos. Datos de especies del '
                     'norte de Brasil.',
                     '#0D4E72'],
                    ['EMBRAPA',
                     'EMBRAPA Cerrados / EMBRAPA Amazônia Oriental',
                     'Datos de meliponicultura en biomas brasileños. Referencia técnica para especies del '
                     'Cerrado y la Amazonía.',
                     '#C47D0E']],
        'species_text': {'Jataí': {'descricao': 'La abeja sin aguijón más conocida de Brasil. Produce miel '
                                                'de altísima calidad con propiedades medicinales. Nidifica '
                                                'en huecos de árboles y grietas de mampostería. Sella la '
                                                'entrada con propóleo, en forma de tubo o de pastillas.',
                                   'bioma': 'Todos',
                                   'regiao': 'Nacional'},
                         'Mosquitinho': {'descricao': 'Una de las abejas sin aguijón más pequeñas de Brasil. '
                                                      'Extremadamente dócil. Produce una miel muy sabrosa, '
                                                      'en pequeñas cantidades. Muy sensible al uso de '
                                                      'agrotóxicos. Indicadora de calidad ambiental.',
                                         'bioma': 'Mata Atlántica',
                                         'regiao': 'Sur/Sudeste'},
                         'Manduri': {'descricao': 'Especie amenazada de extinción (VU). Miel rara, producida '
                                                  'en pequeñas cantidades. Sus nidos suelen estar en '
                                                  'cavidades de árboles nativos. Especie objetivo de '
                                                  'programas de meliponicultura para la conservación.',
                                     'bioma': 'Mata Atlántica',
                                     'regiao': 'Sur/Sudeste'},
                         'Mirim Preguiça': {'descricao': 'También llamada Abelha Preguiça (abeja perezosa) '
                                                         'por su comportamiento tranquilo. Nidifica '
                                                         'principalmente en ramas de árboles. Importante '
                                                         'polinizadora de especies nativas del Cerrado y de '
                                                         'la Mata Atlántica.',
                                            'bioma': 'Cerrado/Mata Atlántica',
                                            'regiao': 'Centro/Sudeste'},
                         'Mandaçaia': {'descricao': 'Una de las abejas sin aguijón más grandes. Produce una '
                                                    'miel diferenciada. En declive por la deforestación y la '
                                                    'urbanización. Criada desde hace siglos por los pueblos '
                                                    "indígenas guaraníes con el nombre de 'mborí'.",
                                       'bioma': 'Mata Atlántica',
                                       'regiao': 'Sudeste/Sur'},
                         'Uruçu Nordestina': {'descricao': 'Abeja sagrada de los tupinambás, cultivada desde '
                                                           'hace más de 2.000 años. Miel con propiedades '
                                                           'medicinales reconocidas. Símbolo de la '
                                                           'meliponicultura del Nordeste. Especie '
                                                           'emblemática de la apicultura indígena.',
                                              'bioma': 'Caatinga/Mata Atlántica NE',
                                              'regiao': 'Nordeste'},
                         'Irapuá': {'descricao': 'Aunque no produce miel en cantidad comercial, es una '
                                                 'polinizadora importantísima. Construye nidos expuestos con '
                                                 'resina de plantas. A veces se la confunde con la abeja '
                                                 'europea por su comportamiento defensivo.',
                                    'bioma': 'Todos',
                                    'regiao': 'Nacional'},
                         'Tiúba': {'descricao': "Conocida como 'Abelha da Terra' (abeja de la tierra) en "
                                                'Maranhão. Miel de sabor único, muy apreciada. Parte '
                                                'fundamental de la cultura meliponicultora amazónica y '
                                                'maranhense. Especie en riesgo por la deforestación.',
                                   'bioma': 'Amazonía/Nordeste',
                                   'regiao': 'Norte/Nordeste'},
                         'Guaraipo': {'descricao': 'Especie con patrón de coloración variable. Produce una '
                                                   'miel de sabor suave. Nidifica en el suelo o en troncos. '
                                                   'En marcado declive por el avance de la agropecuaria en '
                                                   'el Cerrado.',
                                      'bioma': 'Cerrado/Mata Atlántica',
                                      'regiao': 'Centro-Oeste/Sudeste'},
                         'Iraí': {'descricao': 'Abeja muy común en ambientes urbanos. Nidifica en grietas de '
                                               'paredes, cajas de luz y tejas. Muy tolerante a la '
                                               'urbanización. Excelente indicadora de la conectividad entre '
                                               'fragmentos forestales.',
                                  'bioma': 'Cerrado/Mata Atlántica',
                                  'regiao': 'Sudeste'},
                         'Tubuna': {'descricao': 'Productora de miel oscura e intensa. Nidifica en cavidades '
                                                 'de árboles. Muy sensible a la deforestación. Se usa en '
                                                 'proyectos de restauración de fragmentos forestales como '
                                                 'polinizadora clave.',
                                    'bioma': 'Mata Atlántica',
                                    'regiao': 'Sudeste/Sur'},
                         'Mirim Guaçu': {'descricao': 'Especie resistente al frío. Muy común en Santa '
                                                      'Catarina y Rio Grande do Sul. Polinizadora de '
                                                      'especies nativas y cultivadas de la región Sur. Miel '
                                                      'de sabor ácido característico.',
                                         'bioma': 'Sur/Sudeste',
                                         'regiao': 'Sur/Sudeste'},
                         'Abelha Mamangava': {'descricao': 'Polinizadora exclusiva del maracuyá. Sin ella, '
                                                           'la producción de maracuyá en Brasil colapsaría. '
                                                           "Usa la técnica de 'buzz pollination', haciendo "
                                                           'vibrar las flores para liberar el polen. '
                                                           'Construye sus nidos en ramas secas.',
                                              'habitat': 'Nidifica en madera muerta',
                                              'polinizacao': 'Buzz pollination — vibra para liberar el '
                                                             'polen'},
                         'Abelha Carpinteira': {'descricao': 'Género Xylocopa, con más de 50 especies en '
                                                             "Brasil. Se llama 'carpintera' por su habilidad "
                                                             'para excavar madera y hacer sus nidos. '
                                                             'Polinizadoras importantes de flores tubulares. '
                                                             'Anidan en hoteles de abejas con cañas de '
                                                             'bambú.',
                                                'habitat': 'Madera seca, bambú',
                                                'polinizacao': 'Generalista — alta diversidad floral'},
                         'Abelha Mascarada': {'descricao': 'Diminuta pero esencial. Transporta el polen en '
                                                           'el buche, no en corbículas. Lleva néctar y polen '
                                                           'internamente. Responde muy bien a los hoteles de '
                                                           'abejas con cañitas de papel y bambú de 5–6 mm de '
                                                           'diámetro.',
                                              'habitat': 'Cañitas, ramas huecas',
                                              'polinizacao': 'Flores pequeñas y abiertas'},
                         'Abelha Cortadeira': {'descricao': 'Cortan trozos de hojas para construir sus '
                                                            'nidos, de ahí su nombre. Se las ve como '
                                                            "'plagas', pero son polinizadoras nativas "
                                                            'esenciales. Anidan en agujeros en la madera '
                                                            '(una broca de 8–10 mm es ideal para los '
                                                            'hoteles).',
                                               'habitat': 'Suelo, madera, hojas cortadas',
                                               'polinizacao': 'Especies nativas — Cerrado, Mata Atlántica'},
                         'Abelha Nômade': {'descricao': 'Abejas cleptoparásitas que depositan sus huevos en '
                                                        'los nidos de otras abejas solitarias. Parecen '
                                                        'avispas, pero son abejas. Fundamentales para '
                                                        'regular las poblaciones y mantener el equilibrio '
                                                        'ecológico en ambientes forestales.',
                                           'habitat': 'Parásita de otros nidos',
                                           'polinizacao': 'Indirecta — mantiene el equilibrio ecológico'},
                         'Abelha Oleiro': {'descricao': 'Polinizadoras obligadas del murici, el barbatimão y '
                                                        'otras Malpighiaceae. Recolectan aceite floral de '
                                                        'las flores para alimentar a sus larvas. Anidan en '
                                                        'el suelo. Indicadoras de Cerrado preservado.',
                                           'habitat': 'Suelo arenoso, paredones',
                                           'polinizacao': 'Buzzing en flores de aceite — Malpighiaceae'}},
        'back_link': '← Portafolio',
        'lang_label': 'Idioma',
        'cluster_name': 'Ocurrencias',
        'footer_copy': '© 2022–2026 · Observatório Meliponini · Brasil',
        'raw_cols': {'especie': 'Especie',
                     'cientifico': 'Nombre científico',
                     'tamanho': 'Tamaño',
                     'raio': 'Radio de forrajeo (m)',
                     'mel': 'Producción de miel',
                     'iucn': 'IUCN',
                     'bioma': 'Bioma',
                     'registros': 'Registros GBIF',
                     'colonia': 'Colonia (op.)',
                     'mel_ano': 'Miel/año (kg)',
                     'habitat': 'Hábitat',
                     'polinizacao': 'Polinización',
                     'tipo': 'Tipo'},
        'tipo_vals': {'meli': 'Meliponini', 'sol': 'Solitaria'},
        'tok_nd': 'miles de',
        'tok_and': ' y ',
        'tok_sp_top': 'SP concentra {n} registros GBIF — más que cualquier otro estado.',
        'tok_sp_plain': 'SP concentra {n} registros GBIF.',
        'tok_sp_generic': 'SP está entre los estados mejor muestreados.'},
 'it': {'page_title': 'Osservatorio Meliponini · Brasile',
        'hero_tag': 'BIODIVERSITÀ · MELIPONINI · BRASILE · 2022–2025',
        'hero_title': 'Osservatorio delle\nApi Senza Pungiglione',
        'hero_subtitle': 'Monitoraggio e analisi della distribuzione delle api senza pungiglione native '
                         '(Meliponini) e delle api solitarie in Brasile — oltre 24.000 registrazioni GBIF, '
                         '12 specie mappate e conservazione attiva. Comprende la visita tecnica alla Cidade '
                         "das Abelhas (SP, 2022) e l'hotel per api solitarie costruito alla FATEC Jundiaí.",
        'badge1': '🐝 12 specie monitorate',
        'badge2': '🗺️ 300+ punti di presenza',
        'badge3': 'Brasile · 5 Biomi',
        'badge4': 'GBIF · iNaturalist · INPA',
        'badge5': 'Tesi FATEC Jundiaí 2022',
        'm1': 'Specie di Meliponini',
        'm2': 'Registrazioni GBIF (2024)',
        'm3': 'Stati coperti',
        'm4': 'Specie minacciate',
        'tab1': '🗺️ Mappa e Analisi',
        'tab2': '🔬 Metodo e Pipeline',
        'tab3': '💡 Cosa Abbiamo Scoperto',
        'tab4': '📷 Sul Campo',
        'tab5': '📈 Tendenze',
        'tab6': '⚙️ Parametri',
        'tab7': '📋 Dati Grezzi',
        'tab8': '📚 Fonti e Crediti',
        'map_label': 'DISTRIBUZIONE IN BRASILE',
        'map_title': 'Mappa delle Presenze — Api Senza Pungiglione',
        'map_hint': '🐝 <strong>Clicca sui marcatori</strong> per vedere specie, bioma e fonte. Dimensione ∝ '
                    'registrazioni per stato. Attiva i cluster per vedere i raggruppamenti.',
        'heat_title': 'Mappa di Calore — Densità delle Presenze',
        'chart_label': 'ANALISI COMPARATIVA',
        'sp_registros_title': 'Registrazioni per Specie (GBIF, 2024)',
        'estado_title': 'Registrazioni per Stato',
        'bioma_title': 'Distribuzione per Bioma',
        'method_label': 'BIODIVERSITÀ APPLICATA',
        'method_title': 'Domanda e Metodologia',
        'sci_q_title': '❓ Domanda Centrale',
        'sci_q': '"Qual è lo stato attuale della distribuzione e della conservazione delle api senza '
                 'pungiglione native del Brasile, e come possono la meliponicoltura razionale e gli hotel '
                 'per api solitarie contribuire alla tutela di queste specie in ambienti urbani e '
                 'periurbani?"',
        'pipeline_label': 'PIPELINE DEI DATI',
        'steps': [['1',
                   'Raccolta — GBIF + iNaturalist (2010–2024)',
                   'Dati di presenza dei Meliponini brasiliani tramite API GBIF ed esportazione iNaturalist. '
                   '@@TOTAL@@ registrazioni georeferenziate (2010–2024), filtrate escludendo quelle con '
                   'problemi geospaziali. Specie target: 12 Meliponini native + 6 api solitarie.'],
                  ['2',
                   'Visita Tecnica — Cidade das Abelhas (SP, 2022)',
                   "Visita tecnica al Parco Cidade das Abelhas a San Paolo per l'osservazione diretta di "
                   'arnie razionali di Jataí, Mosquitinho, Manduri, Mirim Preguiça e altre specie. '
                   'Documentazione fotografica e raccolta di dati sulla gestione razionale dei meliponari.'],
                  ['3',
                   'Tesi FATEC Jundiaí — Hotel per Api Solitarie (2022)',
                   'Progetto di tesi: costruzione di un Hotel per Api Solitarie nel Campus della FATEC '
                   "Jundiaí in occasione dell'evento Ciência na Praça. Struttura in legno con fori praticati "
                   'con punta da 8 e 10 mm per api solitarie native come Xylocopa sp. e Megachile sp.'],
                  ['4',
                   'Analisi Spaziale — Distribuzione per Bioma',
                   "Incrocio delle presenze con lo shapefile dei biomi dell'IBGE. Individuazione di pattern "
                   'di ricchezza di specie per bioma. La Mata Atlantica è il bioma con la maggiore diversità '
                   'di Meliponini (~22 specie).'],
                  ['5',
                   'Parametri Biologici — Letteratura Scientifica',
                   'Raccolta di dati dalla letteratura: dimensione della colonia, tasso di ovideposizione, '
                   'vita delle operaie, raggio di foraggiamento, produzione di miele. Base: A.B.E.L.H.A., '
                   'Atlas della Meliponicoltura, pubblicazioni USP/UNICAMP/UFMG.'],
                  ['6',
                   'Valutazione della Minaccia — IUCN Red List',
                   'Incrocio dei dati di presenza con lo stato IUCN: @@VU@@ specie Vulnerabili (VU), @@LC@@ '
                   'a Minore Preoccupazione (LC). Analisi delle tendenze demografiche e delle pressioni '
                   'antropiche per bioma.']],
        'biologia_title': '🐝 Perché le Api Senza Pungiglione sono importanti?',
        'biologia_text': '• <b>~550 specie</b> di Meliponini descritte nel mondo · <b>~350 in '
                         'Brasile</b><br>• <b>Impollinatrici esclusive</b> di specie native della Mata '
                         'Atlantica e del Cerrado<br>• <b>Miele con proprietà medicinali</b> riconosciute '
                         "dall'ANVISA (Portaria 310/1997)<br>• <b>Meliponicoltura</b>: allevamento razionale "
                         'in arnie INPA, IBAMA, JTB, Fernão Dias<br>• <b>Minacce:</b> deforestazione, '
                         'pesticidi, urbanizzazione, specie esotiche invasive',
        'solitarias_title': '🏨 Api Solitarie — La Maggioranza Silenziosa',
        'solitarias_text': '• <b>~70% delle api del mondo</b> sono solitarie — senza regina, senza '
                           'alveare<br>• <b>Ogni femmina</b> costruisce il proprio nido, raccoglie il cibo e '
                           'si prende cura delle uova<br>• <b>Gli hotel per api</b> (blocchi di legno con '
                           'fori da 6–10 mm) attirano Xylocopa, Megachile e Hylaeus<br>• <b>Fori ideali:</b> '
                           'punta da 8 mm (Megachile), punta da 10 mm (Xylocopa) — profondità minima 10 '
                           'cm<br>• <b>Installazione:</b> esposizione a Est/Sud-Est, altezza 1–2 m, riparato '
                           'dalla pioggia diretta',
        'disc_label': 'ANALISI E SCOPERTE',
        'disc_title': 'Cosa Hanno Rivelato i Dati',
        'discoveries': [['🐝',
                         "Jataí — la più adattata all'urbanizzazione",
                         "Tetragonisca angustula è la specie con la maggiore adattabilità all'ambiente "
                         'urbano. Registrazioni in tutti gli stati brasiliani e in tutti e 5 i biomi. '
                         'Nidifica in fessure di muratura, quadri elettrici e pali. La sua presenza nelle '
                         'città è un indicatore di resilienza ecologica.'],
                        ['⚠️',
                         '@@VU@@ specie Vulnerabili — @@VU_LIST@@',
                         'Le specie di Melipona di maggiori dimensioni e con maggiore produzione di miele '
                         'sono le più minacciate. La combinazione di deforestazione, pressione antropica e '
                         'bassa riproduzione (la regina compie un solo volo nuziale) rende queste specie '
                         'particolarmente esposte al collasso demografico.'],
                        ['🏨',
                         'Hotel per Api — moltiplicatore di biodiversità urbana',
                         "L'Hotel per Api costruito alla FATEC Jundiaí ha dimostrato che semplici strutture "
                         'in legno con fori praticati con punta da 8 e 10 mm vengono occupate in 30–60 '
                         'giorni da specie solitarie native. Un intervento a basso costo (<R$50) con grande '
                         "impatto sull'impollinazione locale."],
                        ['📊',
                         'San Paolo — capitale brasiliana della meliponicoltura',
                         '@@SP_SENT@@ La combinazione di Mata Atlantica residua, intensa ricerca '
                         'universitaria (USP, UNICAMP, UNESP) e meliponicoltura urbana in crescita spiega '
                         'questo ruolo di primo piano.'],
                        ['🌎',
                         'GBIF: @@GROWTH@@ in 10 anni — la scienza partecipata come motore',
                         'La crescita di @@GROWTH_ABS@@ registrazioni georeferenziate di Meliponini in '
                         'Brasile tra il 2014 e il 2024 (@@GROWTH@@) accompagna la diffusione di iNaturalist '
                         "e l'interesse dei cittadini per la biodiversità. La crescente meliponicoltura "
                         'urbana è al tempo stesso conseguenza e causa di questo interesse.'],
                        ['🌿',
                         'Cerrado — bioma sottocampionato con grande diversità nascosta',
                         'Pur ospitando ~100 specie endemiche di Meliponini, il Cerrado è storicamente '
                         'sottocampionato nei registri di biodiversità. Il sottocampionamento riflette '
                         "lacune di ricerca nelle aree remote — un campanello d'allarme per la conservazione "
                         'prima che il bioma sia frammentato al 100%.']],
        'conclusion_label': 'CONCLUSIONE',
        'conclusion_title': 'Ogni Alveare Conta',
        'conclusion_text': 'Le api senza pungiglione native del Brasile sono un patrimonio biologico e '
                           'culturale unico: allevate dai popoli indigeni per millenni, produttrici di miele '
                           'con proprietà medicinali e impollinatrici insostituibili della nostra flora '
                           'nativa. La crescita di @@GROWTH_N@@ nelle registrazioni GBIF di Meliponini '
                           "mostra che l'interesse per la meliponicoltura sta aumentando — ma il ritmo della "
                           'deforestazione supera ancora la velocità della conservazione. Ogni arnia '
                           'razionale installata, ogni hotel per api costruito, ogni frammento di foresta '
                           'protetto è un voto di fiducia nel futuro di queste specie.',
        'conclusion_author': 'Amauri Almeida · Tesi in Gestione Ambientale · FATEC Jundiaí · 2022 · Visita '
                             'alla Cidade das Abelhas SP',
        'field_label': 'DOCUMENTAZIONE DI CAMPO E TECNICA',
        'field_title': 'Dalla Cidade das Abelhas al Campus della FATEC',
        'field_inst_title': '📁 Come aggiungere le tue foto',
        'field_inst': 'Inserisci le tue foto nella cartella <code>assets/campo/</code> con i nomi esatti '
                      'indicati qui sotto.',
        'photos': [{'emoji': '🐝',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Arnia Razionale — Ape Jataí',
                    'esp': 'Tetragonisca angustula',
                    'desc': "Arnia razionale (cassetta JTB o INPA) dell'ape Jataí (Tetragonisca angustula) "
                            'nel Parco Cidade das Abelhas, a San Paolo. La Jataí è la specie più comune e '
                            "adattabile del Brasile — nidifica naturalmente in fessure di muratura. L'arnia "
                            'razionale permette la divisione delle colonie e la gestione senza distruggere '
                            'il nido.',
                    'path': 'assets/campo/01_colmeia_jatai_cidade_abelhas.jpg',
                    'legenda': 'Arnia Jataí (Tetragonisca angustula) · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🔎',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Arnia Razionale — Ape Mosquitinho',
                    'esp': 'Plebeia mosquito',
                    'desc': "Arnia razionale dell'ape Mosquitinho (Plebeia mosquito) — una delle più piccole "
                            'api senza pungiglione del Brasile (2 mm). Estremamente docile e sensibile ai '
                            'pesticidi. Arnia con modulo del miele separato dal modulo della covata — '
                            'pratica fondamentale della meliponicoltura razionale per non danneggiare la '
                            'colonia.',
                    'path': 'assets/campo/02_colmeia_mosquitinho_cidade_abelhas.jpg',
                    'legenda': 'Arnia Mosquitinho (Plebeia mosquito) · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🌿',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Arnia Razionale — Ape Manduri (1)',
                    'esp': 'Melipona marginata',
                    'desc': "Arnia razionale dell'ape Manduri (Melipona marginata) — specie Vulnerabile "
                            '(IUCN VU). Una delle specie più importanti per la conservazione: miele raro, '
                            'prodotto in piccola quantità, nidifica esclusivamente in cavità di alberi '
                            'nativi. La meliponicoltura razionale è la principale strategia di conservazione '
                            'ex situ per questa specie.',
                    'path': 'assets/campo/04_colmeia_manduri_cidade_abelhas_1.jpg',
                    'legenda': 'Arnia Manduri (Melipona marginata) · Vulnerabile · Cidade das Abelhas · SP · '
                               '2022',
                    'gid': 'cidade'},
                   {'emoji': '🌿',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Arnia Razionale — Ape Manduri (2)',
                    'esp': 'Melipona marginata',
                    'desc': 'Seconda arnia di Manduri documentata. Il monitoraggio di più arnie della stessa '
                            'specie permette di studiare la variazione comportamentale e produttiva. La '
                            'differenza di colore e di struttura tra le cassette riflette diversi modelli di '
                            'arnia razionale — INPA, Fernão Dias, JTB e modelli USP.',
                    'path': 'assets/campo/05_colmeia_manduri_cidade_abelhas_2.jpg',
                    'legenda': 'Arnia Manduri (2) · Melipona marginata · VU · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Arnia Razionale — Mirim Preguiça (1)',
                    'esp': 'Frieseomelitta varia',
                    'desc': "Arnia razionale dell'ape Mirim Preguiça (Frieseomelitta varia) — chiamata così "
                            "per il comportamento tranquillo delle operaie all'ingresso dell'arnia. Specie "
                            "importante per l'impollinazione di specie native del Cerrado e della Mata "
                            'Atlantica. Costruisce i nidi sui rami degli alberi.',
                    'path': 'assets/campo/06_colmeia_mirim_preguica_1.jpg',
                    'legenda': 'Arnia Mirim Preguiça (Frieseomelitta varia) · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Arnia Razionale — Mirim Preguiça (2)',
                    'esp': 'Frieseomelitta varia',
                    'desc': "Seconda veduta dell'arnia di Mirim Preguiça. Si osserva l'ingresso dell'arnia "
                            "con le caratteristiche specifiche di questa specie. L'architettura interna del "
                            'nido, con celle di covata sferiche, è diversa da quella delle Melipona — il che '
                            'richiede adattamenti specifici nelle cassette razionali per questa specie.',
                    'path': 'assets/campo/07_colmeia_mirim_preguica_2.jpg',
                    'legenda': 'Arnia Mirim Preguiça (2) · Frieseomelitta varia · Cidade das Abelhas · SP · '
                               '2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Arnia Razionale — Mirim Preguiça (3)',
                    'esp': 'Frieseomelitta varia',
                    'desc': "Terza angolazione dell'arnia di Mirim Preguiça, con dettagli della struttura "
                            'esterna e del supporto. La documentazione da più punti di vista è essenziale '
                            'nelle visite tecniche per individuare i modelli di gestione e di design '
                            "dell'arnia che funzionano meglio per ogni specie.",
                    'path': 'assets/campo/08_colmeia_mirim_preguica_3.jpg',
                    'legenda': 'Arnia Mirim Preguiça (3) · Frieseomelitta varia · Cidade das Abelhas · SP · '
                               '2022',
                    'gid': 'cidade'},
                   {'emoji': '🏛️',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Meliponario — Collezione di Specie Diverse',
                    'esp': 'Specie multiple',
                    'desc': 'Veduta del meliponario del Parco Cidade das Abelhas con cassette razionali di '
                            'specie diverse affiancate — come prescrive la buona pratica meliponicola. Ogni '
                            'specie ha la propria cassetta identificata. La distanza tra le arnie e '
                            "l'orientamento dell'ingresso sono calcolati per ridurre al minimo la deriva "
                            'delle api e massimizzare la salute delle colonie.',
                    'path': 'assets/campo/09_meliponario_colecao_cidade_abelhas.jpg',
                    'legenda': 'Meliponario con specie diverse · Cassette razionali · Parco Cidade das '
                               'Abelhas · SP · 2022',
                    'destaque': True,
                    'gid': 'cidade'},
                   {'emoji': '🌳',
                    'grupo': 'HOTEL PER API · FATEC JUNDIAÍ · 2022',
                    'titulo': "Costruzione dell'Hotel — Struttura in Legno",
                    'esp': 'Per api solitarie',
                    'desc': "Inizio della costruzione dell'Hotel per Api Solitarie nel Campus della FATEC "
                            'Jundiaí. La struttura in legno è il supporto principale per i blocchi forati. '
                            'La scelta del legno (pino trattato o eucalipto) è importante: deve resistere '
                            "all'umidità ma non essere trattato con biocidi che allontanino le api.",
                    'path': 'assets/campo/10_hotel_abelhas_estrutura_madeira.jpg',
                    'legenda': "Costruzione dell'Hotel per Api · Struttura in legno · FATEC Jundiaí · "
                               'Ciência na Praça · 2022',
                    'gid': 'hotel'},
                   {'emoji': '🔩',
                    'grupo': 'HOTEL PER API · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Foratura dei Blocchi — Punta da 8 e 10 mm',
                    'esp': 'Per api solitarie',
                    'desc': 'Foratura dei blocchi di legno con il trapano usando una punta da 8 mm '
                            '(Megachile sp., Hylaeus sp.) e una da 10 mm (Xylocopa sp.). Una profondità '
                            'minima di 10 cm è essenziale perché la femmina completi il nido con 3–5 celle '
                            'di covata. I fori devono terminare a fondo cieco — non devono attraversare il '
                            'blocco.',
                    'path': 'assets/campo/11_hotel_abelhas_furadeira_broca8_10.jpg',
                    'legenda': 'Foratura con punta da 8 e 10 mm · Hotel per Api Solitarie · FATEC Jundiaí · '
                               '2022',
                    'gid': 'hotel'},
                   {'emoji': '🔩',
                    'grupo': 'HOTEL PER API · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Foratura nel Dettaglio — Punta da 8 e 10 mm',
                    'esp': 'Per api solitarie',
                    'desc': "Dettaglio del processo di foratura con punta da 8 e 10 mm. L'uniformità dei "
                            "fori è importante per il successo dell'hotel: profondità minima 10 cm, diametro "
                            'preciso e superficie interna liscia (carteggiare se necessario). I fori con '
                            'bordi interni seghettati possono impedire il passaggio delle api.',
                    'path': 'assets/campo/12_hotel_abelhas_furos_detalhe.jpg',
                    'legenda': 'Dettaglio dei fori con punta da 8/10 mm · Hotel per Api Solitarie · FATEC '
                               'Jundiaí · 2022',
                    'gid': 'hotel'},
                   {'emoji': '✅',
                    'grupo': 'HOTEL PER API · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Hotel per Api Completato — Campus FATEC Jundiaí',
                    'esp': 'Per api solitarie',
                    'desc': 'Hotel per Api Solitarie completato, installato nel Campus della FATEC Jundiaí '
                            "in occasione dell'evento Ciência na Praça. Blocchi di legno con fori praticati "
                            'con punta da 8 e 10 mm, esposizione a Est/Sud-Est, altezza ~1,5 m, protetto da '
                            'una copertura contro la pioggia. Struttura a basso costo (<R$50) con grande '
                            "impatto sull'impollinazione locale.",
                    'path': 'assets/campo/13_hotel_abelhas_concluido_fatec_jundiai.jpg',
                    'legenda': 'Hotel per Api Solitarie completato · Campus FATEC Jundiaí · Ciência na Praça '
                               '· 2022',
                    'destaque_final': True,
                    'gid': 'hotel'}],
        'timeline_label': 'CRONOLOGIA DEL PROGETTO',
        'timeline_items': [['2022 · Jan–Jun',
                            'Tesi in Gestione Ambientale — FATEC Jundiaí',
                            'Ricerca sulla meliponicoltura e sulle api solitarie · Hotel per Api costruito '
                            'per Ciência na Praça'],
                           ['2022 · Jul',
                            'Visita Tecnica — Cidade das Abelhas SP',
                            'Documentazione fotografica di 8+ specie in arnie razionali · Jataí, '
                            'Mosquitinho, Manduri, Mirim Preguiça e altre'],
                           ['2022 · Nov',
                            'Discussione della Tesi — FATEC Jundiaí',
                            'Approvazione del Lavoro di Conclusione del Corso in Gestione Ambientale · '
                            'Laurea conseguita'],
                           ['2023–2024',
                            'Analisi GBIF — @@TOTAL@@ registrazioni',
                            'Incrocio dei dati di presenza con biomi e stati · Individuazione di lacune di '
                            'conservazione'],
                           ['2025',
                            'Pubblicazione nel Portfolio',
                            'Osservatorio Meliponini del Brasile — dashboard pubblica con dati aggiornati']],
        'trend_sel': 'Seleziona la visualizzazione',
        'trend_opt1': 'Crescita GBIF (2010–2024)',
        'trend_opt2': 'Registrazioni per Specie (classifica)',
        'trend_opt3': 'Registrazioni per Stato',
        'param_sel': 'Specie da analizzare',
        'param_names': {'colonia': 'Dimensione della colonia (operaie)',
                        'postura_dia': 'Tasso di ovideposizione (uova/giorno)',
                        'vida_operaria': "Vita dell'operaia (giorni)",
                        'longe_formag': 'Raggio di foraggiamento (m)',
                        'prod_mel_kg': 'Produzione di miele (kg/anno)',
                        'raio_dna_km': 'Distanza genetica (km)'},
        'raw_label': 'CATALOGO DELLE SPECIE',
        'raw_title': 'Tabella Completa — Meliponini del Brasile',
        'download_csv': '⬇️ Scarica CSV',
        'sources_label': 'FONTI SCIENTIFICHE',
        'sources_title': 'Fonti e Banche Dati',
        'tech_label': 'TECNOLOGIE UTILIZZATE',
        'footer_title': '🐝 Amauri Almeida',
        'footer_desc': 'Tecnologo in Gestione Ambientale · FATEC Jundiaí (3º ENADE)<br>Post-laurea in IA, '
                       'Machine Learning e Data Science · Scienza dei Dati e Big Data<br>Analisi e Sviluppo '
                       'di Sistemi · FACINT Maringá',
        'footer_links': '📍 Fernandópolis · SP · Brasile',
        'trend_label': 'EVOLUZIONE TEMPORALE E CLASSIFICHE',
        'param_label': 'BIOLOGIA COMPARATA',
        'param_title': 'Parametri Biologici delle Specie',
        'param_detail': 'Parametro biologico',
        'param_cmp': 'Confronto tra Specie',
        'records_axis': 'Registrazioni',
        'records_hover': 'registrazioni',
        'gal_meli': 'GALLERIA DELLE SPECIE — MELIPONINI',
        'gal_sol': 'GALLERIA — API SOLITARIE',
        'honey': 'Miele',
        'mel_vals': {'Sim': 'Sì', 'Não': 'No', 'Pouco': 'Poco'},
        'gbif_records': 'registrazioni GBIF',
        'pop_records': 'Registrazioni',
        'pop_species': 'Specie',
        'pop_status': 'Stato',
        'status_vals': {'Alta': 'Alta', 'Média': 'Media', 'Baixa': 'Bassa'},
        'radar_title': 'Profilo Comparativo delle Specie (scala 0–10)',
        'radar_cats': ['Produzione di miele',
                       'Adattamento urbano',
                       'Raggio di volo',
                       'Dimensione della colonia',
                       'IUCN (inv.)'],
        'grp_city': '🏛️ CIDADE DAS ABELHAS · SÃO PAULO · 2022',
        'grp_hotel': '🏨 HOTEL PER API SOLITARIE · FATEC JUNDIAÍ · CIÊNCIA NA PRAÇA · 2022',
        'dest_melipon': '⭐ IN EVIDENZA — MELIPONARIO COMPLETO · CIDADE DAS ABELHAS',
        'dest_hotel': '✅ EVIDENZA FINALE — HOTEL COMPLETATO · CAMPUS FATEC JUNDIAÍ',
        'hotel_build_title': '🏗️ Come costruire un Hotel per Api Solitarie',
        'hotel_build': [['Materiale', 'Blocco di legno (pino trattato o eucalipto) · minimo 15×10×10 cm'],
                        ['Fori', 'Punta da 8 mm (Megachile, Hylaeus) · Punta da 10 mm (Xylocopa)'],
                        ['Profondità', 'Minimo 10 cm · Fondo cieco (non attraversare il blocco!)'],
                        ['Esposizione', 'Est o Sud-Est · Riceve il sole del mattino'],
                        ['Altezza', '1–2 metri da terra · Riparato da pioggia e vento'],
                        ['Risultato', 'Occupazione in 30–60 giorni da parte di api native']],
        'solitary_tbl': 'Api Solitarie',
        'card_lbls': {'biome': 'Bioma',
                      'region': 'Regione',
                      'colony': 'Colonia',
                      'workers': 'operaie',
                      'laying': 'Ovideposizione',
                      'eggs_day': 'uova/giorno',
                      'worker_life': 'Vita operaia',
                      'days': 'giorni',
                      'forage': 'Raggio foraggiamento',
                      'honey': 'Produzione miele',
                      'kg_year': 'kg/anno',
                      'gen_dist': 'Dist. genetica'},
        'carto_fallback': 'Mappa di base alternativa (OpenStreetMap) in uso.',
        'occ_live': 'Punti reali di GBIF (api.gbif.org): {n} presenze georeferenziate in Brasile, fino a {k} '
                    'per specie, consultate il {d}. Clicca su un punto per aprire la registrazione '
                    'originale.',
        'occ_demo': 'GBIF al momento non disponibile: i punti mostrati sono ILLUSTRATIVI (capitali × '
                    'specie), non sono registrazioni di campo.',
        'occ_none': 'GBIF al momento non disponibile e nessun dato di riserva: mappa delle presenze non '
                    'visualizzata.',
        'dados_live': 'Numeri calcolati a partire da GBIF (api.gbif.org), consultato il {d}; aggiornamento '
                      'automatico ogni 24 h.',
        'dados_snapshot': "GBIF non disponibile al momento: numeri dell'ultimo snapshot salvato ({d}).",
        'dados_static': 'GBIF non disponibile al momento: valori di riferimento di una compilazione '
                        'precedente, non aggiornati.',
        'serie_total': 'Totale (Meliponini + 5 generi solitari)',
        'serie_inat': 'iNaturalist (Meliponini)',
        'raio_sel': 'Mostra il raggio di foraggiamento (cerchi in metri)',
        'raio_note': 'Ogni cerchio mostra il raggio medio di volo della specie attorno a presenze reali '
                     '(fino a {n} per specie). Ingrandisci la mappa per vedere la scala.',
        'raio_layer': 'Raggio di foraggiamento',
        'footer_portfolio': 'Portfolio',
        'sources': [['GBIF',
                     'GBIF — Global Biodiversity Information Facility',
                     'gbif.org · Banca dati di presenze con @@TOTAL@@ registrazioni georeferenziate di '
                     'Meliponini in Brasile (2010–2024). Dati di musei, erbari, iNaturalist e ricercatori.',
                     '#C47D0E'],
                    ['A.B.E.L.H.A.',
                     'A.B.E.L.H.A. — Associazione Brasiliana per lo Studio delle Api',
                     'abelha.org.br · Atlas della Meliponicoltura in Brasile. Riferimento per raggi di '
                     'foraggiamento, biologia e conservazione.',
                     '#C0390A'],
                    ['INATURALIST',
                     'iNaturalist — Scienza Partecipata Globale',
                     'inaturalist.org · @@INAT@@ registrazioni di Meliponini brasiliani con '
                     'georeferenziazione (dataset iNaturalist Research-grade su GBIF). Principale motore '
                     'della crescita di GBIF.',
                     '#2D7A45'],
                    ['FATEC',
                     'FATEC Jundiaí — Tesi in Gestione Ambientale (2022)',
                     "Hotel per Api Solitarie costruito nel Campus in occasione dell'evento Ciência na "
                     'Praça. Punta da 8 e 10 mm. Approvato con lode.',
                     '#1B3A1E'],
                    ['CIDADE ABELHAS',
                     'Parco Cidade das Abelhas — San Paolo (2022)',
                     'Visita tecnica nel 2022. Documentazione fotografica di arnie razionali di Jataí, '
                     'Mosquitinho, Manduri, Mirim Preguiça e altre.',
                     '#5C3D1E'],
                    ['IUCN',
                     'IUCN Red List — Lista Rossa delle Specie Minacciate',
                     '@@VU_TAGS@@. Stato di conservazione dei Meliponini brasiliani.',
                     '#8B2515'],
                    ['INPA',
                     "INPA — Istituto Nazionale di Ricerche dell'Amazzonia",
                     'Modello di arnia razionale INPA per i Meliponini amazzonici. Dati sulle specie del '
                     'Nord del Brasile.',
                     '#0D4E72'],
                    ['EMBRAPA',
                     'EMBRAPA Cerrados / EMBRAPA Amazônia Oriental',
                     'Dati di meliponicoltura nei biomi brasiliani. Riferimento tecnico per le specie del '
                     "Cerrado e dell'Amazzonia.",
                     '#C47D0E']],
        'species_text': {'Jataí': {'descricao': "L'ape senza pungiglione più conosciuta del Brasile. Produce "
                                                'un miele di altissima qualità con proprietà medicinali. '
                                                'Nidi in cavità di alberi e fessure di muratura. Chiusura '
                                                "dell'ingresso con propoli, a forma di tubo o di pastiglie.",
                                   'bioma': 'Tutti',
                                   'regiao': 'Nazionale'},
                         'Mosquitinho': {'descricao': 'Una delle più piccole api senza pungiglione del '
                                                      'Brasile. Estremamente docile. Miele molto saporito '
                                                      "prodotto in piccole quantità. Molto sensibile all'uso "
                                                      'di pesticidi. Indicatrice della qualità ambientale.',
                                         'bioma': 'Mata Atlantica',
                                         'regiao': 'Sud/Sud-Est'},
                         'Manduri': {'descricao': 'Specie minacciata di estinzione (VU). Miele raro, '
                                                  'prodotto in piccole quantità. Nidi generalmente in cavità '
                                                  'di alberi nativi. Specie bersaglio dei programmi di '
                                                  'meliponicoltura per la conservazione.',
                                     'bioma': 'Mata Atlantica',
                                     'regiao': 'Sud/Sud-Est'},
                         'Mirim Preguiça': {'descricao': 'Chiamata anche Ape Pigra per il suo comportamento '
                                                         'tranquillo. Nidifica principalmente sui rami degli '
                                                         'alberi. Importante impollinatrice di specie native '
                                                         'del Cerrado e della Mata Atlantica.',
                                            'bioma': 'Cerrado/Mata Atlantica',
                                            'regiao': 'Centro/Sud-Est'},
                         'Mandaçaia': {'descricao': 'Una delle più grandi api senza pungiglione. Produzione '
                                                    'di miele distintiva. In declino a causa della '
                                                    "deforestazione e dell'urbanizzazione. Allevata da "
                                                    "secoli dagli indigeni guaraní come 'mborí'.",
                                       'bioma': 'Mata Atlantica',
                                       'regiao': 'Sud-Est/Sud'},
                         'Uruçu Nordestina': {'descricao': 'Ape sacra dei tupinambá, allevata da più di '
                                                           '2.000 anni. Miele con proprietà medicinali '
                                                           'riconosciute. Simbolo della meliponicoltura del '
                                                           "Nordeste. Specie-bandiera dell'apicoltura "
                                                           'indigena.',
                                              'bioma': 'Caatinga/Mata Atlantica NE',
                                              'regiao': 'Nordeste'},
                         'Irapuá': {'descricao': 'Pur non producendo miele in quantità commerciale, è '
                                                 "un'impollinatrice importantissima. Costruisce nidi esposti "
                                                 "con resina vegetale. A volte scambiata per l'ape europea a "
                                                 'causa del comportamento difensivo.',
                                    'bioma': 'Tutti',
                                    'regiao': 'Nazionale'},
                         'Tiúba': {'descricao': "Conosciuta come 'Ape della Terra' nel Maranhão. Miele dal "
                                                'sapore unico, molto apprezzato. Parte fondamentale della '
                                                'cultura meliponicola amazzonica e maranhense. Specie a '
                                                'rischio a causa della deforestazione.',
                                   'bioma': 'Amazzonia/Nordeste',
                                   'regiao': 'Nord/Nordeste'},
                         'Guaraipo': {'descricao': 'Specie con colorazione variabile. Produzione di miele '
                                                   'dal sapore delicato. Nidi nel suolo o nei tronchi. In '
                                                   "forte declino per l'avanzata dell'agropecuaria nel "
                                                   'Cerrado.',
                                      'bioma': 'Cerrado/Mata Atlantica',
                                      'regiao': 'Centro-Ovest/Sud-Est'},
                         'Iraí': {'descricao': 'Ape molto comune negli ambienti urbani. Nidifica in fessure '
                                               'di pareti, quadri elettrici e tegole. Molto tollerante '
                                               "all'urbanizzazione. Eccellente indicatrice della "
                                               'connettività dei frammenti forestali.',
                                  'bioma': 'Cerrado/Mata Atlantica',
                                  'regiao': 'Sud-Est'},
                         'Tubuna': {'descricao': 'Produttrice di miele scuro e intenso. Nidi in cavità di '
                                                 'alberi. Molto sensibile alla deforestazione. Usata nei '
                                                 'progetti di ripristino di frammenti forestali come '
                                                 'impollinatrice chiave.',
                                    'bioma': 'Mata Atlantica',
                                    'regiao': 'Sud-Est/Sud'},
                         'Mirim Guaçu': {'descricao': 'Specie resistente al freddo. Molto comune a Santa '
                                                      'Catarina e nel Rio Grande do Sul. Impollinatrice di '
                                                      'specie native e coltivate della regione Sud. Miele '
                                                      'dal caratteristico sapore acidulo.',
                                         'bioma': 'Sud/Sud-Est',
                                         'regiao': 'Sud/Sud-Est'},
                         'Abelha Mamangava': {'descricao': 'Impollinatrice esclusiva del frutto della '
                                                           'passione. Senza di lei, la produzione di '
                                                           'maracujá in Brasile collasserebbe. Usa la '
                                                           "tecnica della 'buzz pollination', facendo "
                                                           'vibrare i fiori per liberare il polline. '
                                                           'Costruisce nidi su rami secchi.',
                                              'habitat': 'Nidifica nel legno morto',
                                              'polinizacao': 'Buzz pollination — vibra per liberare il '
                                                             'polline'},
                         'Abelha Carpinteira': {'descricao': 'Genere Xylocopa con più di 50 specie in '
                                                             "Brasile. 'Carpinteira' (carpentiera) per la "
                                                             'capacità di scavare il legno per i nidi. '
                                                             'Impollinatrici importanti dei fiori tubolari. '
                                                             'Nidi in hotel per api con cannucce di bambù.',
                                                'habitat': 'Legno secco, bambù',
                                                'polinizacao': 'Generalista — elevata diversità floreale'},
                         'Abelha Mascarada': {'descricao': 'Minuscola ma essenziale. Trasporta il polline '
                                                           'nel gozzo, non nelle corbicole. Trasporta '
                                                           'nettare e polline internamente. Risponde molto '
                                                           'bene agli hotel per api con cannucce di carta e '
                                                           'di bambù di diametro 5–6 mm.',
                                              'habitat': 'Cannucce, rami cavi',
                                              'polinizacao': 'Fiori piccoli e aperti'},
                         'Abelha Cortadeira': {'descricao': 'Taglia pezzi di foglie per costruire i propri '
                                                            'nidi — da qui il nome. Viene vista come '
                                                            "'parassita' ma è un'impollinatrice nativa "
                                                            'essenziale. Nidi in buchi nel legno (punta da '
                                                            '8–10 mm ideale per gli hotel).',
                                               'habitat': 'Suolo, legno, foglie tagliate',
                                               'polinizacao': 'Specie native — Cerrado, Mata Atlantica'},
                         'Abelha Nômade': {'descricao': 'Api cleptoparassite che depongono le uova nei nidi '
                                                        'di altre api solitarie. Sembrano vespe ma sono api. '
                                                        'Fondamentali per regolare le popolazioni e '
                                                        "mantenere l'equilibrio ecologico negli ambienti "
                                                        'forestali.',
                                           'habitat': 'Parassita di altri nidi',
                                           'polinizacao': "Indiretta — mantiene l'equilibrio ecologico"},
                         'Abelha Oleiro': {'descricao': 'Impollinatrici obbligate di murici, barbatimão e '
                                                        "altre Malpighiaceae. Raccolgono l'olio floreale dai "
                                                        'fiori per nutrire le larve. Nidi nel suolo. '
                                                        'Indicatrici di Cerrado ben conservato.',
                                           'habitat': 'Suolo sabbioso, pareti scoscese',
                                           'polinizacao': 'Buzzing su fiori oleiferi — Malpighiaceae'}},
        'back_link': '← Portfolio',
        'lang_label': 'Lingua',
        'cluster_name': 'Presenze',
        'footer_copy': '© 2022–2026 · Osservatorio Meliponini · Brasile',
        'raw_cols': {'especie': 'Specie',
                     'cientifico': 'Nome Scientifico',
                     'tamanho': 'Dimensione',
                     'raio': 'Raggio Foraggiamento (m)',
                     'mel': 'Produzione Miele',
                     'iucn': 'IUCN',
                     'bioma': 'Bioma',
                     'registros': 'Registrazioni GBIF',
                     'colonia': 'Colonia (op.)',
                     'mel_ano': 'Miele/anno (kg)',
                     'habitat': 'Habitat',
                     'polinizacao': 'Impollinazione',
                     'tipo': 'Tipo'},
        'tipo_vals': {'meli': 'Meliponini', 'sol': 'Solitaria'},
        'tok_nd': 'migliaia di',
        'tok_and': ' e ',
        'tok_sp_top': 'SP concentra {n} registrazioni GBIF — più di qualsiasi altro stato.',
        'tok_sp_plain': 'SP concentra {n} registrazioni GBIF.',
        'tok_sp_generic': 'SP è tra gli stati meglio campionati.'},
 'fr': {'page_title': 'Observatoire Meliponini · Brésil',
        'hero_tag': 'BIODIVERSITÉ · MELIPONINI · BRÉSIL · 2022–2025',
        'hero_title': 'Observatoire des\nAbeilles sans Dard',
        'hero_subtitle': 'Suivi et analyse de la répartition des abeilles sans dard indigènes (Meliponini) '
                         'et des abeilles solitaires au Brésil — plus de 24 000 enregistrements GBIF, 12 '
                         'espèces cartographiées et conservation active. Comprend une visite technique à la '
                         'Cidade das Abelhas (SP, 2022) et un hôtel à abeilles solitaires construit à la '
                         'FATEC Jundiaí.',
        'badge1': '🐝 12 espèces suivies',
        'badge2': "🗺️ 300+ points d'occurrence",
        'badge3': 'Brésil · 5 biomes',
        'badge4': 'GBIF · iNaturalist · INPA',
        'badge5': 'Mémoire FATEC Jundiaí 2022',
        'm1': 'Espèces Meliponini',
        'm2': 'Données GBIF (2024)',
        'm3': 'États couverts',
        'm4': 'Espèces menacées',
        'tab1': '🗺️ Carte & Analyse',
        'tab2': '🔬 Méthode & Pipeline',
        'tab3': '💡 Nos Découvertes',
        'tab4': '📷 Sur le Terrain',
        'tab5': '📈 Tendances',
        'tab6': '⚙️ Paramètres',
        'tab7': '📋 Données Brutes',
        'tab8': '📚 Sources & Crédits',
        'map_label': 'RÉPARTITION AU BRÉSIL',
        'map_title': 'Carte des Occurrences — Abeilles sans Dard',
        'map_hint': "🐝 <strong>Cliquez sur les marqueurs</strong> pour voir l'espèce, le biome et la source. "
                    'Taille ∝ enregistrements par État. Activez les clusters pour voir les regroupements.',
        'heat_title': 'Carte de Chaleur — Densité des Occurrences',
        'chart_label': 'ANALYSE COMPARATIVE',
        'sp_registros_title': 'Enregistrements par Espèce (GBIF, 2024)',
        'estado_title': 'Enregistrements par État',
        'bioma_title': 'Répartition par Biome',
        'method_label': 'BIODIVERSITÉ APPLIQUÉE',
        'method_title': 'Question & Méthodologie',
        'sci_q_title': '❓ Question Centrale',
        'sci_q': "« Quel est l'état actuel de la répartition et de la conservation des abeilles sans dard "
                 'indigènes du Brésil, et comment la méliponiculture raisonnée et les hôtels à abeilles '
                 'solitaires peuvent-ils contribuer à la préservation de ces espèces en milieu urbain et '
                 'périurbain ? »',
        'pipeline_label': 'PIPELINE DE DONNÉES',
        'steps': [['1',
                   'Collecte — GBIF + iNaturalist (2010–2024)',
                   "Données d'occurrence des Meliponini brésiliens via l'API GBIF et l'export iNaturalist. "
                   '@@TOTAL@@ enregistrements géoréférencés (2010–2024), filtrés pour écarter les problèmes '
                   'géospatiaux. Espèces cibles : 12 Meliponini indigènes + 6 abeilles solitaires.'],
                  ['2',
                   'Visite Technique — Cidade das Abelhas (SP, 2022)',
                   'Visite technique du parc Cidade das Abelhas à São Paulo pour observer directement des '
                   "ruches rationnelles de Jataí, Mosquitinho, Manduri, Mirim Preguiça et d'autres espèces. "
                   'Documentation photographique et relevé de données sur la gestion raisonnée des '
                   'méliponaires.'],
                  ['3',
                   'Mémoire FATEC Jundiaí — Hôtel à Abeilles Solitaires (2022)',
                   "Projet de fin d'études : construction d'un hôtel à abeilles solitaires sur le campus de "
                   "la FATEC Jundiaí pour l'événement Ciência na Praça. Structure en bois percée de trous de "
                   '8 et 10 mm pour des abeilles solitaires indigènes comme Xylocopa sp. et Megachile sp.'],
                  ['4',
                   'Analyse Spatiale — Répartition par Biome',
                   "Croisement des occurrences avec le shapefile des biomes de l'IBGE. Identification des "
                   'schémas de richesse spécifique par biome. La forêt atlantique est le biome le plus riche '
                   'en Meliponini (~22 espèces).'],
                  ['5',
                   'Paramètres Biologiques — Littérature Scientifique',
                   'Compilation de données issues de la littérature : taille de la colonie, taux de ponte, '
                   'durée de vie des ouvrières, rayon de butinage, production de miel. Base : A.B.E.L.H.A., '
                   'Atlas de la Méliponiculture, publications USP/UNICAMP/UFMG.'],
                  ['6',
                   "Évaluation des Menaces — Liste rouge de l'IUCN",
                   "Croisement des données d'occurrence avec le statut IUCN : @@VU@@ espèces Vulnérables "
                   '(VU), @@LC@@ de Préoccupation mineure (LC). Analyse des tendances des populations et des '
                   'pressions anthropiques par biome.']],
        'biologia_title': '🐝 Pourquoi les Abeilles sans Dard sont-elles importantes ?',
        'biologia_text': '• <b>~550 espèces</b> de Meliponini décrites dans le monde · <b>~350 au '
                         "Brésil</b><br>• <b>Pollinisatrices exclusives</b> d'espèces indigènes de la forêt "
                         'atlantique et du Cerrado<br>• <b>Miel aux propriétés médicinales</b> reconnues par '
                         "l'ANVISA (Portaria 310/1997)<br>• <b>Méliponiculture</b> : élevage raisonné dans "
                         'des ruches INPA, IBAMA, JTB, Fernão Dias<br>• <b>Menaces :</b> déforestation, '
                         'pesticides, urbanisation, espèces exotiques envahissantes',
        'solitarias_title': '🏨 Abeilles Solitaires — La Majorité Silencieuse',
        'solitarias_text': '• <b>~70 % des abeilles du monde</b> sont solitaires — sans reine, sans '
                           'ruche<br>• <b>Chaque femelle</b> construit son propre nid, récolte la nourriture '
                           "et s'occupe des œufs<br>• <b>Les hôtels à abeilles</b> (blocs de bois percés de "
                           'trous de 6–10 mm) attirent Xylocopa, Megachile et Hylaeus<br>• <b>Trous idéaux '
                           ':</b> foret de 8 mm (Megachile), foret de 10 mm (Xylocopa) — profondeur minimale '
                           '10 cm<br>• <b>Installation :</b> orientation Est/Sud-Est, hauteur 1–2 m, à '
                           "l'abri de la pluie directe",
        'disc_label': 'ANALYSE ET DÉCOUVERTES',
        'disc_title': 'Ce que les Données ont Révélé',
        'discoveries': [['🐝',
                         "Jataí — la mieux adaptée à l'urbanisation",
                         "Tetragonisca angustula est l'espèce la plus adaptable au milieu urbain. Présente "
                         'dans tous les États brésiliens et dans les 5 biomes. Elle niche dans les fissures '
                         'de maçonnerie, les boîtiers électriques et les poteaux. Sa présence en ville est '
                         'un indicateur de résilience écologique.'],
                        ['⚠️',
                         '@@VU@@ espèces Vulnérables — @@VU_LIST@@',
                         'Les espèces de Melipona les plus grandes et les plus productrices de miel sont les '
                         'plus menacées. La combinaison de déforestation, de pression anthropique et de '
                         "faible reproduction (la reine ne fait qu'un seul vol nuptial) rend ces espèces "
                         "particulièrement vulnérables à l'effondrement des populations."],
                        ['🏨',
                         'Hôtel à Abeilles — multiplicateur de biodiversité urbaine',
                         "L'hôtel à abeilles construit à la FATEC Jundiaí a montré que de simples structures "
                         'en bois percées de trous de 8 et 10 mm sont occupées en 30–60 jours par des '
                         'espèces solitaires indigènes. Une intervention peu coûteuse (<R$50) à fort impact '
                         'pour la pollinisation locale.'],
                        ['📊',
                         'São Paulo — capitale brésilienne de la méliponiculture',
                         "@@SP_SENT@@ La combinaison de forêt atlantique résiduelle, d'une recherche "
                         "universitaire intense (USP, UNICAMP, UNESP) et d'une méliponiculture urbaine en "
                         'plein essor explique ce rôle de premier plan.'],
                        ['🌎',
                         'GBIF : @@GROWTH@@ en 10 ans — la science citoyenne comme moteur',
                         'La croissance de @@GROWTH_ABS@@ enregistrements géoréférencés de Meliponini au '
                         "Brésil entre 2014 et 2024 (@@GROWTH@@) accompagne l'essor d'iNaturalist et de "
                         "l'intérêt des citoyens pour la biodiversité. La méliponiculture urbaine croissante "
                         'est à la fois conséquence et cause de cet intérêt.'],
                        ['🌿',
                         'Cerrado — biome sous-échantillonné à la grande diversité cachée',
                         "Bien qu'il abrite ~100 espèces endémiques de Meliponini, le Cerrado est "
                         'historiquement sous-échantillonné dans les données de biodiversité. Ce '
                         'sous-échantillonnage reflète des lacunes de recherche dans les zones reculées — un '
                         "signal d'alarme pour la conservation avant que le biome ne soit fragmenté à 100 "
                         '%.']],
        'conclusion_label': 'CONCLUSION',
        'conclusion_title': 'Chaque Ruche Compte',
        'conclusion_text': 'Les abeilles sans dard indigènes du Brésil constituent un patrimoine biologique '
                           'et culturel unique : élevées par les peuples autochtones depuis des millénaires, '
                           "productrices d'un miel aux propriétés médicinales et pollinisatrices "
                           'irremplaçables de notre flore indigène. La croissance de @@GROWTH_N@@ des '
                           "enregistrements GBIF de Meliponini montre que l'intérêt pour la méliponiculture "
                           'augmente — mais le rythme de la déforestation dépasse encore celui de la '
                           'conservation. Chaque ruche rationnelle installée, chaque hôtel à abeilles '
                           "construit, chaque fragment de forêt protégé est un vote de confiance en l'avenir "
                           'de ces espèces.',
        'conclusion_author': 'Amauri Almeida · Mémoire Gestion Environnementale · FATEC Jundiaí · 2022 · '
                             'Visite Cidade das Abelhas SP',
        'field_label': 'RELEVÉ DE TERRAIN ET TECHNIQUE',
        'field_title': 'De la Cidade das Abelhas au Campus de la FATEC',
        'field_inst_title': '📁 Comment ajouter vos photos',
        'field_inst': 'Placez vos photos dans le dossier <code>assets/campo/</code> avec les noms exacts '
                      'indiqués ci-dessous.',
        'photos': [{'emoji': '🐝',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Ruche Rationnelle — Abeille Jataí',
                    'esp': 'Tetragonisca angustula',
                    'desc': "Ruche rationnelle (caisse JTB ou INPA) de l'abeille Jataí (Tetragonisca "
                            "angustula) au parc Cidade das Abelhas, à São Paulo. La Jataí est l'espèce la "
                            'plus commune et la plus adaptable du Brésil — elle niche naturellement dans les '
                            'fissures de maçonnerie. La ruche rationnelle permet de diviser les colonies et '
                            'de les gérer sans détruire le nid.',
                    'path': 'assets/campo/01_colmeia_jatai_cidade_abelhas.jpg',
                    'legenda': 'Ruche Jataí (Tetragonisca angustula) · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🔎',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Ruche Rationnelle — Abeille Mosquitinho',
                    'esp': 'Plebeia mosquito',
                    'desc': "Ruche rationnelle de l'abeille Mosquitinho (Plebeia mosquito) — l'une des plus "
                            'petites abeilles sans dard du Brésil (2 mm). Extrêmement docile et sensible aux '
                            'pesticides. Ruche dont le module à miel est séparé du module de couvain — '
                            'pratique fondamentale de la méliponiculture raisonnée pour ne pas nuire à la '
                            'colonie.',
                    'path': 'assets/campo/02_colmeia_mosquitinho_cidade_abelhas.jpg',
                    'legenda': 'Ruche Mosquitinho (Plebeia mosquito) · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🌿',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Ruche Rationnelle — Abeille Manduri (1)',
                    'esp': 'Melipona marginata',
                    'desc': "Ruche rationnelle de l'abeille Manduri (Melipona marginata) — espèce Vulnérable "
                            "(IUCN VU). L'une des espèces les plus importantes pour la conservation : miel "
                            'rare, produit en faible quantité, nidification exclusivement dans des creux '
                            "d'arbres indigènes. La méliponiculture raisonnée est la principale stratégie de "
                            'conservation ex situ pour cette espèce.',
                    'path': 'assets/campo/04_colmeia_manduri_cidade_abelhas_1.jpg',
                    'legenda': 'Ruche Manduri (Melipona marginata) · Vulnérable · Cidade das Abelhas · SP · '
                               '2022',
                    'gid': 'cidade'},
                   {'emoji': '🌿',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Ruche Rationnelle — Abeille Manduri (2)',
                    'esp': 'Melipona marginata',
                    'desc': 'Deuxième ruche de Manduri documentée. Le suivi de plusieurs ruches de la même '
                            "espèce permet d'étudier les variations de comportement et de production. La "
                            'différence de couleur et de structure entre les caisses reflète différents '
                            'modèles de ruches rationnelles — INPA, Fernão Dias, JTB et modèles USP.',
                    'path': 'assets/campo/05_colmeia_manduri_cidade_abelhas_2.jpg',
                    'legenda': 'Ruche Manduri (2) · Melipona marginata · VU · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Ruche Rationnelle — Mirim Preguiça (1)',
                    'esp': 'Frieseomelitta varia',
                    'desc': "Ruche rationnelle de l'abeille Mirim Preguiça (Frieseomelitta varia) — ainsi "
                            "nommée pour le comportement tranquille des ouvrières à l'entrée de la ruche. "
                            "Espèce importante pour la pollinisation d'espèces indigènes du Cerrado et de la "
                            "forêt atlantique. Elle construit ses nids sur des branches d'arbres.",
                    'path': 'assets/campo/06_colmeia_mirim_preguica_1.jpg',
                    'legenda': 'Ruche Mirim Preguiça (Frieseomelitta varia) · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Ruche Rationnelle — Mirim Preguiça (2)',
                    'esp': 'Frieseomelitta varia',
                    'desc': "Deuxième vue de la ruche de Mirim Preguiça. On observe l'entrée de la ruche "
                            "avec les caractéristiques propres à cette espèce. L'architecture interne du "
                            'nid, avec ses cellules de couvain sphériques, diffère de celle des Melipona — '
                            'ce qui exige des adaptations spécifiques des caisses rationnelles pour cette '
                            'espèce.',
                    'path': 'assets/campo/07_colmeia_mirim_preguica_2.jpg',
                    'legenda': 'Ruche Mirim Preguiça (2) · Frieseomelitta varia · Cidade das Abelhas · SP · '
                               '2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Ruche Rationnelle — Mirim Preguiça (3)',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'Troisième angle de la ruche de Mirim Preguiça, montrant des détails de la '
                            'structure externe et du support. Documenter plusieurs vues est essentiel lors '
                            'des visites techniques pour repérer les pratiques de gestion et les modèles de '
                            'ruche qui conviennent le mieux à chaque espèce.',
                    'path': 'assets/campo/08_colmeia_mirim_preguica_3.jpg',
                    'legenda': 'Ruche Mirim Preguiça (3) · Frieseomelitta varia · Cidade das Abelhas · SP · '
                               '2022',
                    'gid': 'cidade'},
                   {'emoji': '🏛️',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': "Méliponaire — Collection d'Espèces Distinctes",
                    'esp': 'Espèces multiples',
                    'desc': 'Vue du méliponaire du parc Cidade das Abelhas avec des caisses rationnelles '
                            "d'espèces distinctes côte à côte — comme le recommandent les bonnes pratiques "
                            "de méliponiculture. Chaque espèce a sa caisse identifiée. L'espacement entre "
                            "les ruches et l'orientation de l'entrée sont calculés pour minimiser la dérive "
                            'des abeilles et maximiser la santé des colonies.',
                    'path': 'assets/campo/09_meliponario_colecao_cidade_abelhas.jpg',
                    'legenda': "Méliponaire d'espèces distinctes · Caisses rationnelles · Parc Cidade das "
                               'Abelhas · SP · 2022',
                    'destaque': True,
                    'gid': 'cidade'},
                   {'emoji': '🌳',
                    'grupo': 'HÔTEL À ABEILLES · FATEC JUNDIAÍ · 2022',
                    'titulo': "Construction de l'Hôtel — Structure en Bois",
                    'esp': 'Pour abeilles solitaires',
                    'desc': "Début de la construction de l'hôtel à abeilles solitaires sur le campus de la "
                            'FATEC Jundiaí. La structure en bois est le support principal des blocs percés. '
                            'Le choix du bois (pin traité ou eucalyptus) est important : il doit résister à '
                            "l'humidité sans être traité avec des biocides qui éloigneraient les abeilles.",
                    'path': 'assets/campo/10_hotel_abelhas_estrutura_madeira.jpg',
                    'legenda': "Construction de l'hôtel à abeilles · Structure en bois · FATEC Jundiaí · "
                               'Ciência na Praça · 2022',
                    'gid': 'hotel'},
                   {'emoji': '🔩',
                    'grupo': 'HÔTEL À ABEILLES · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Perçage des Blocs — Forets de 8 et 10 mm',
                    'esp': 'Pour abeilles solitaires',
                    'desc': 'Perçage des blocs de bois à la perceuse avec un foret de 8 mm (Megachile sp., '
                            'Hylaeus sp.) et un foret de 10 mm (Xylocopa sp.). Une profondeur minimale de 10 '
                            'cm est indispensable pour que la femelle puisse achever son nid de 3–5 cellules '
                            'de couvain. Les trous doivent se terminer en cul-de-sac — ils ne doivent pas '
                            'traverser le bloc.',
                    'path': 'assets/campo/11_hotel_abelhas_furadeira_broca8_10.jpg',
                    'legenda': 'Perçage avec forets de 8 et 10 mm · Hôtel à abeilles solitaires · FATEC '
                               'Jundiaí · 2022',
                    'gid': 'hotel'},
                   {'emoji': '🔩',
                    'grupo': 'HÔTEL À ABEILLES · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Perçage en Détail — Forets de 8 et 10 mm',
                    'esp': 'Pour abeilles solitaires',
                    'desc': "Détail du processus de perçage avec des forets de 8 et 10 mm. L'uniformité des "
                            "trous est importante pour la réussite de l'hôtel : profondeur minimale de 10 "
                            'cm, diamètre précis et surface interne lisse (poncer si nécessaire). Des trous '
                            'aux parois dentelées peuvent empêcher le passage des abeilles.',
                    'path': 'assets/campo/12_hotel_abelhas_furos_detalhe.jpg',
                    'legenda': 'Détail des trous de 8/10 mm · Hôtel à abeilles solitaires · FATEC Jundiaí · '
                               '2022',
                    'gid': 'hotel'},
                   {'emoji': '✅',
                    'grupo': 'HÔTEL À ABEILLES · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Hôtel à Abeilles Terminé — Campus FATEC Jundiaí',
                    'esp': 'Pour abeilles solitaires',
                    'desc': 'Hôtel à abeilles solitaires terminé, installé sur le campus de la FATEC Jundiaí '
                            "pour l'événement Ciência na Praça. Blocs de bois percés de trous de 8 et 10 mm, "
                            'orientation Est/Sud-Est, hauteur ~1,5 m, protégé de la pluie par un toit. '
                            'Structure peu coûteuse (<R$50) à fort impact pour la pollinisation locale.',
                    'path': 'assets/campo/13_hotel_abelhas_concluido_fatec_jundiai.jpg',
                    'legenda': 'Hôtel à abeilles solitaires terminé · Campus FATEC Jundiaí · Ciência na '
                               'Praça · 2022',
                    'destaque_final': True,
                    'gid': 'hotel'}],
        'timeline_label': 'CHRONOLOGIE DU PROJET',
        'timeline_items': [['2022 · Jan–Jun',
                            'Mémoire Gestion Environnementale — FATEC Jundiaí',
                            'Recherche sur la méliponiculture et les abeilles solitaires · Hôtel à abeilles '
                            'construit pour Ciência na Praça'],
                           ['2022 · Jul',
                            'Visite Technique — Cidade das Abelhas SP',
                            'Documentation photographique de 8+ espèces dans des ruches rationnelles · '
                            "Jataí, Mosquitinho, Manduri, Mirim Preguiça et d'autres"],
                           ['2022 · Nov',
                            'Soutenance du Mémoire — FATEC Jundiaí',
                            "Validation du mémoire de fin d'études en Gestion Environnementale · Diplôme "
                            'obtenu'],
                           ['2023–2024',
                            'Analyse GBIF — @@TOTAL@@ enregistrements',
                            "Croisement des données d'occurrence avec les biomes et les États · "
                            'Identification des lacunes de conservation'],
                           ['2025',
                            'Publication dans le Portfolio',
                            'Observatoire Meliponini du Brésil — tableau de bord public avec données '
                            'actualisées']],
        'trend_sel': 'Choisir la visualisation',
        'trend_opt1': 'Croissance GBIF (2010–2024)',
        'trend_opt2': 'Enregistrements par Espèce (classement)',
        'trend_opt3': 'Enregistrements par État',
        'param_sel': 'Espèce à analyser',
        'param_names': {'colonia': 'Taille de la colonie (ouvrières)',
                        'postura_dia': 'Taux de ponte (œufs/jour)',
                        'vida_operaria': "Durée de vie de l'ouvrière (jours)",
                        'longe_formag': 'Rayon de butinage (m)',
                        'prod_mel_kg': 'Production de miel (kg/an)',
                        'raio_dna_km': 'Distance génétique (km)'},
        'raw_label': 'CATALOGUE DES ESPÈCES',
        'raw_title': 'Tableau Complet — Meliponini du Brésil',
        'download_csv': '⬇️ Télécharger le CSV',
        'sources_label': 'SOURCES SCIENTIFIQUES',
        'sources_title': 'Sources & Bases de Données',
        'tech_label': 'TECHNOLOGIES UTILISÉES',
        'footer_title': '🐝 Amauri Almeida',
        'footer_desc': 'Technologue en Gestion Environnementale · FATEC Jundiaí (3e ENADE)<br>Troisième '
                       'cycle en IA, Machine Learning & Data Science · Science des Données & Big '
                       'Data<br>Analyse et Développement de Systèmes · FACINT Maringá',
        'footer_links': '📍 Fernandópolis · SP · Brésil',
        'trend_label': 'ÉVOLUTION TEMPORELLE & CLASSEMENTS',
        'param_label': 'BIOLOGIE COMPARÉE',
        'param_title': 'Paramètres Biologiques des Espèces',
        'param_detail': 'Paramètre biologique',
        'param_cmp': 'Comparaison entre Espèces',
        'records_axis': 'Enregistrements',
        'records_hover': 'enregistrements',
        'gal_meli': "GALERIE D'ESPÈCES — MELIPONINI",
        'gal_sol': 'GALERIE — ABEILLES SOLITAIRES',
        'honey': 'Miel',
        'mel_vals': {'Sim': 'Oui', 'Não': 'Non', 'Pouco': 'Peu'},
        'gbif_records': 'enregistrements GBIF',
        'pop_records': 'Enregistrements',
        'pop_species': 'Espèces',
        'pop_status': 'Statut',
        'status_vals': {'Alta': 'Élevée', 'Média': 'Moyenne', 'Baixa': 'Faible'},
        'radar_title': 'Profil Comparatif des Espèces (échelle 0–10)',
        'radar_cats': ['Production de miel',
                       'Adaptation urbaine',
                       'Rayon de vol',
                       'Taille de la colonie',
                       'IUCN (inv.)'],
        'grp_city': '🏛️ CIDADE DAS ABELHAS (CITÉ DES ABEILLES) · SÃO PAULO · 2022',
        'grp_hotel': '🏨 HÔTEL À ABEILLES SOLITAIRES · FATEC JUNDIAÍ · CIÊNCIA NA PRAÇA · 2022',
        'dest_melipon': '⭐ À LA UNE — MÉLIPONAIRE COMPLET · CIDADE DAS ABELHAS',
        'dest_hotel': '✅ À LA UNE — HÔTEL TERMINÉ · CAMPUS FATEC JUNDIAÍ',
        'hotel_build_title': '🏗️ Comment construire un Hôtel à Abeilles Solitaires',
        'hotel_build': [['Matériau', 'Bloc de bois (pin traité ou eucalyptus) · 15×10×10 cm minimum'],
                        ['Trous', 'Foret de 8 mm (Megachile, Hylaeus) · Foret de 10 mm (Xylocopa)'],
                        ['Profondeur', 'Minimum 10 cm · Cul-de-sac (ne pas traverser le bloc !)'],
                        ['Orientation', 'Est ou Sud-Est · Reçoit le soleil du matin'],
                        ['Hauteur', '1–2 mètres du sol · Protégé de la pluie et du vent'],
                        ['Résultat', 'Occupation en 30–60 jours par des abeilles indigènes']],
        'solitary_tbl': 'Abeilles Solitaires',
        'card_lbls': {'biome': 'Biome',
                      'region': 'Région',
                      'colony': 'Colonie',
                      'workers': 'ouvrières',
                      'laying': 'Ponte',
                      'eggs_day': 'œufs/jour',
                      'worker_life': "Vie de l'ouvrière",
                      'days': 'jours',
                      'forage': 'Rayon de butinage',
                      'honey': 'Production de miel',
                      'kg_year': 'kg/an',
                      'gen_dist': 'Dist. génétique'},
        'carto_fallback': 'Fond de carte alternatif (OpenStreetMap) utilisé.',
        'occ_live': "Points réels du GBIF (api.gbif.org) : {n} occurrences géoréférencées au Brésil, jusqu'à "
                    "{k} par espèce, consultées le {d}. Cliquez sur un point pour ouvrir l'enregistrement "
                    "d'origine.",
        'occ_demo': 'GBIF indisponible pour le moment : les points affichés sont ILLUSTRATIFS (capitales × '
                    'espèces), ce ne sont pas des relevés de terrain.',
        'occ_none': 'GBIF indisponible pour le moment et aucune donnée de secours : carte des occurrences '
                    'non affichée.',
        'dados_live': 'Chiffres calculés à partir du GBIF (api.gbif.org), consultés le {d} ; mise à jour '
                      'automatique toutes les 24 h.',
        'dados_snapshot': 'GBIF indisponible actuellement : chiffres du dernier instantané enregistré ({d}).',
        'dados_static': "GBIF indisponible actuellement : valeurs de référence d'une compilation antérieure, "
                        'non actualisées.',
        'serie_total': 'Total (Meliponini + 5 genres solitaires)',
        'serie_inat': 'iNaturalist (Meliponini)',
        'raio_sel': 'Afficher le rayon de butinage (cercles en mètres)',
        'raio_note': "Chaque cercle montre le rayon de vol moyen de l'espèce autour d'occurrences réelles "
                     "(jusqu'à {n} par espèce). Zoomez sur la carte pour voir l'échelle.",
        'raio_layer': 'Rayon de butinage',
        'footer_portfolio': 'Portfolio',
        'sources': [['GBIF',
                     'GBIF — Global Biodiversity Information Facility',
                     "gbif.org · Base d'occurrences avec @@TOTAL@@ enregistrements géoréférencés de "
                     "Meliponini au Brésil (2010–2024). Données de musées, d'herbiers, d'iNaturalist et de "
                     'chercheurs.',
                     '#C47D0E'],
                    ['A.B.E.L.H.A.',
                     "A.B.E.L.H.A. — Association brésilienne d'étude des abeilles",
                     'abelha.org.br · Atlas de la Méliponiculture au Brésil. Référence pour les rayons de '
                     'butinage, la biologie et la conservation.',
                     '#C0390A'],
                    ['INATURALIST',
                     'iNaturalist — Science citoyenne mondiale',
                     'inaturalist.org · @@INAT@@ enregistrements géoréférencés de Meliponini brésiliens (jeu '
                     'de données iNaturalist Research-grade sur le GBIF). Principal moteur de la croissance '
                     'du GBIF.',
                     '#2D7A45'],
                    ['FATEC',
                     'FATEC Jundiaí — Mémoire de Gestion Environnementale (2022)',
                     "Hôtel à abeilles solitaires construit sur le campus pour l'événement Ciência na Praça. "
                     'Forets de 8 et 10 mm. Validé avec mention.',
                     '#1B3A1E'],
                    ['CIDADE ABELHAS',
                     'Parc Cidade das Abelhas — São Paulo (2022)',
                     'Visite technique en 2022. Documentation photographique de ruches rationnelles de '
                     "Jataí, Mosquitinho, Manduri, Mirim Preguiça et d'autres.",
                     '#5C3D1E'],
                    ['IUCN',
                     'IUCN Red List — Liste rouge des espèces menacées',
                     '@@VU_TAGS@@. Statut de conservation des Meliponini brésiliens.',
                     '#8B2515'],
                    ['INPA',
                     'INPA — Institut national de recherches amazoniennes',
                     'Modèle de ruche rationnelle INPA pour les Meliponini amazoniens. Données sur les '
                     'espèces du nord du Brésil.',
                     '#0D4E72'],
                    ['EMBRAPA',
                     'EMBRAPA Cerrados / EMBRAPA Amazônia Oriental',
                     'Données de méliponiculture dans les biomes brésiliens. Référence technique pour les '
                     "espèces du Cerrado et de l'Amazonie.",
                     '#C47D0E']],
        'species_text': {'Jataí': {'descricao': "L'abeille sans dard la plus connue du Brésil. Elle produit "
                                                'un miel de très haute qualité aux propriétés médicinales. '
                                                "Nids dans les creux d'arbres et les fissures de maçonnerie. "
                                                'Entrée operculée de propolis, en tube ou en pastilles.',
                                   'bioma': 'Tous',
                                   'regiao': 'National'},
                         'Mosquitinho': {'descricao': "L'une des plus petites abeilles sans dard du Brésil. "
                                                      'Extrêmement docile. Miel très savoureux produit en '
                                                      "petites quantités. Très sensible à l'usage de "
                                                      'pesticides. Indicatrice de la qualité de '
                                                      "l'environnement.",
                                         'bioma': 'Forêt atlantique',
                                         'regiao': 'Sud/Sud-Est'},
                         'Manduri': {'descricao': "Espèce menacée d'extinction (VU). Miel rare, produit en "
                                                  'petites quantités. Nids généralement dans des cavités '
                                                  "d'arbres indigènes. Espèce cible des programmes de "
                                                  'méliponiculture pour la conservation.',
                                     'bioma': 'Forêt atlantique',
                                     'regiao': 'Sud/Sud-Est'},
                         'Mirim Preguiça': {'descricao': 'Aussi appelée abeille Preguiça (« paresseuse ») '
                                                         'pour son comportement tranquille. Niche '
                                                         "principalement sur les branches d'arbres. "
                                                         "Pollinisatrice importante d'espèces indigènes du "
                                                         'Cerrado et de la forêt atlantique.',
                                            'bioma': 'Cerrado/Forêt atlantique',
                                            'regiao': 'Centre/Sud-Est'},
                         'Mandaçaia': {'descricao': "L'une des plus grandes abeilles sans dard. Production "
                                                    'de miel remarquable. En déclin à cause de la '
                                                    "déforestation et de l'urbanisation. Élevée depuis des "
                                                    'siècles par les Guaranis sous le nom de « mborí ».',
                                       'bioma': 'Forêt atlantique',
                                       'regiao': 'Sud-Est/Sud'},
                         'Uruçu Nordestina': {'descricao': 'Abeille sacrée des Tupinambás, élevée depuis '
                                                           'plus de 2 000 ans. Miel aux propriétés '
                                                           'médicinales reconnues. Symbole de la '
                                                           'méliponiculture du Nordeste. Espèce emblématique '
                                                           "de l'apiculture autochtone.",
                                              'bioma': 'Caatinga/Forêt atlantique du Nordeste',
                                              'regiao': 'Nordeste'},
                         'Irapuá': {'descricao': "Bien qu'elle ne produise pas de miel en quantité "
                                                 "commerciale, c'est une pollinisatrice très importante. "
                                                 'Elle construit des nids exposés avec de la résine '
                                                 "végétale. Parfois confondue avec l'abeille européenne en "
                                                 'raison de son comportement défensif.',
                                    'bioma': 'Tous',
                                    'regiao': 'National'},
                         'Tiúba': {'descricao': 'Connue comme « Abelha da Terra » (abeille de la terre) dans '
                                                'le Maranhão. Miel au goût unique, très apprécié. Élément '
                                                'fondamental de la culture méliponicole amazonienne et du '
                                                'Maranhão. Espèce menacée par la déforestation.',
                                   'bioma': 'Amazonie/Nordeste',
                                   'regiao': 'Nord/Nordeste'},
                         'Guaraipo': {'descricao': "Espèce à la coloration variable. Production d'un miel au "
                                                   'goût doux. Nids dans le sol ou dans les troncs. En net '
                                                   "déclin à cause de l'avancée de l'agriculture et de "
                                                   "l'élevage dans le Cerrado.",
                                      'bioma': 'Cerrado/Forêt atlantique',
                                      'regiao': 'Centre-Ouest/Sud-Est'},
                         'Iraí': {'descricao': 'Abeille très commune en milieu urbain. Elle niche dans les '
                                               'fissures des murs, les boîtiers électriques et les tuiles. '
                                               "Très tolérante à l'urbanisation. Excellente indicatrice de "
                                               'la connectivité des fragments forestiers.',
                                  'bioma': 'Cerrado/Forêt atlantique',
                                  'regiao': 'Sud-Est'},
                         'Tubuna': {'descricao': "Productrice d'un miel sombre et intense. Nids dans les "
                                                 "cavités d'arbres. Très sensible à la déforestation. "
                                                 'Utilisée dans les projets de restauration de fragments '
                                                 'forestiers comme pollinisatrice clé.',
                                    'bioma': 'Forêt atlantique',
                                    'regiao': 'Sud-Est/Sud'},
                         'Mirim Guaçu': {'descricao': 'Espèce résistante au froid. Très commune à Santa '
                                                      'Catarina et au Rio Grande do Sul. Pollinisatrice '
                                                      "d'espèces indigènes et cultivées de la région Sud. "
                                                      'Miel au goût acide caractéristique.',
                                         'bioma': 'Sud/Sud-Est',
                                         'regiao': 'Sud/Sud-Est'},
                         'Abelha Mamangava': {'descricao': 'Pollinisatrice exclusive du fruit de la passion. '
                                                           'Sans elle, la production de fruits de la passion '
                                                           "s'effondrerait au Brésil. Elle utilise la "
                                                           'technique de la « buzz pollination », faisant '
                                                           'vibrer les fleurs pour libérer le pollen. Elle '
                                                           'construit ses nids dans des branches sèches.',
                                              'habitat': 'Niche dans le bois mort',
                                              'polinizacao': 'Buzz pollination — vibre pour libérer le '
                                                             'pollen'},
                         'Abelha Carpinteira': {'descricao': 'Genre Xylocopa, avec plus de 50 espèces au '
                                                             'Brésil. Appelée « charpentière » pour sa '
                                                             "capacité à creuser le bois afin d'y faire son "
                                                             'nid. Pollinisatrices importantes des fleurs '
                                                             'tubulaires. Nids dans les hôtels à abeilles '
                                                             'avec des tiges de bambou.',
                                                'habitat': 'Bois sec, bambou',
                                                'polinizacao': 'Généraliste — grande diversité florale'},
                         'Abelha Mascarada': {'descricao': 'Minuscule mais essentielle. Elle transporte le '
                                                           'pollen dans son jabot, et non dans des '
                                                           'corbeilles. Elle transporte nectar et pollen à '
                                                           "l'intérieur de son corps. Elle répond très bien "
                                                           'aux hôtels à abeilles dotés de tiges en papier '
                                                           'et en bambou de 5–6 mm de diamètre.',
                                              'habitat': 'Tiges, branches creuses',
                                              'polinizacao': 'Fleurs petites et ouvertes'},
                         'Abelha Cortadeira': {'descricao': 'Elles découpent des morceaux de feuilles pour '
                                                            "construire leurs nids — d'où leur nom. "
                                                            'Considérées comme des « nuisibles », ce sont '
                                                            'pourtant des pollinisatrices indigènes '
                                                            'essentielles. Nids dans des trous dans le bois '
                                                            '(foret de 8–10 mm idéal pour les hôtels).',
                                               'habitat': 'Sol, bois, feuilles découpées',
                                               'polinizacao': 'Espèces indigènes — Cerrado, forêt '
                                                              'atlantique'},
                         'Abelha Nômade': {'descricao': 'Abeilles cleptoparasites qui pondent leurs œufs '
                                                        "dans les nids d'autres abeilles solitaires. Elles "
                                                        'ressemblent à des guêpes, mais ce sont bien des '
                                                        'abeilles. Fondamentales pour réguler les '
                                                        "populations et maintenir l'équilibre écologique "
                                                        'dans les milieux forestiers.',
                                           'habitat': "Parasite d'autres nids",
                                           'polinizacao': "Indirecte — maintient l'équilibre écologique"},
                         'Abelha Oleiro': {'descricao': 'Pollinisatrices obligatoires du murici, du '
                                                        "barbatimão et d'autres Malpighiaceae. Elles "
                                                        "récoltent l'huile florale des fleurs pour nourrir "
                                                        "leurs larves. Nids dans le sol. Indicatrices d'un "
                                                        'Cerrado préservé.',
                                           'habitat': 'Sol sableux, parois',
                                           'polinizacao': 'Buzzing sur fleurs à huile — Malpighiaceae'}},
        'back_link': '← Portfolio',
        'lang_label': 'Langue',
        'cluster_name': 'Occurrences',
        'footer_copy': '© 2022–2026 · Observatoire Meliponini · Brésil',
        'raw_cols': {'especie': 'Espèce',
                     'cientifico': 'Nom Scientifique',
                     'tamanho': 'Taille',
                     'raio': 'Rayon de Butinage (m)',
                     'mel': 'Production de Miel',
                     'iucn': 'IUCN',
                     'bioma': 'Biome',
                     'registros': 'Données GBIF',
                     'colonia': 'Colonie (ouvr.)',
                     'mel_ano': 'Miel/an (kg)',
                     'habitat': 'Habitat',
                     'polinizacao': 'Pollinisation',
                     'tipo': 'Type'},
        'tipo_vals': {'meli': 'Meliponini', 'sol': 'Solitaire'},
        'tok_nd': 'milliers de',
        'tok_and': ' et ',
        'tok_sp_top': 'SP concentre {n} enregistrements GBIF — plus que tout autre État.',
        'tok_sp_plain': 'SP concentre {n} enregistrements GBIF.',
        'tok_sp_generic': 'SP figure parmi les États les mieux échantillonnés.'},
 'de': {'page_title': 'Meliponini-Observatorium · Brasilien',
        'hero_tag': 'BIODIVERSITÄT · MELIPONINI · BRASILIEN · 2022–2025',
        'hero_title': 'Observatorium der\nStachellosen Bienen',
        'hero_subtitle': 'Monitoring und Analyse der Verbreitung einheimischer Stachelloser Bienen '
                         '(Meliponini) und Solitärbienen in Brasilien — mehr als 24.000 GBIF-Datensätze, 12 '
                         'kartierte Arten und aktiver Artenschutz. Mit Fachexkursion zur Cidade das Abelhas '
                         '(SP, 2022) und einem Solitärbienen-Hotel, das an der FATEC Jundiaí gebaut wurde.',
        'badge1': '🐝 12 überwachte Arten',
        'badge2': '🗺️ 300+ Fundpunkte',
        'badge3': 'Brasilien · 5 Biome',
        'badge4': 'GBIF · iNaturalist · INPA',
        'badge5': 'Abschlussarbeit FATEC Jundiaí 2022',
        'm1': 'Meliponini-Arten',
        'm2': 'GBIF-Datensätze (2024)',
        'm3': 'Abgedeckte Staaten',
        'm4': 'Gefährdete Arten',
        'tab1': '🗺️ Karte & Analyse',
        'tab2': '🔬 Methodik & Pipeline',
        'tab3': '💡 Erkenntnisse',
        'tab4': '📷 Im Feld',
        'tab5': '📈 Trends',
        'tab6': '⚙️ Parameter',
        'tab7': '📋 Rohdaten',
        'tab8': '📚 Quellen & Dank',
        'map_label': 'VERBREITUNG IN BRASILIEN',
        'map_title': 'Fundkarte — Stachellose Bienen',
        'map_hint': '🐝 <strong>Klicken Sie auf die Marker</strong>, um Art, Biom und Quelle zu sehen. Größe '
                    '∝ Datensätze pro Bundesstaat. Aktivieren Sie die Cluster, um Gruppierungen zu sehen.',
        'heat_title': 'Heatmap — Dichte der Funde',
        'chart_label': 'VERGLEICHENDE ANALYSE',
        'sp_registros_title': 'Datensätze pro Art (GBIF, 2024)',
        'estado_title': 'Datensätze pro Bundesstaat',
        'bioma_title': 'Verteilung nach Biom',
        'method_label': 'ANGEWANDTE BIODIVERSITÄT',
        'method_title': 'Fragestellung & Methodik',
        'sci_q_title': '❓ Zentrale Frage',
        'sci_q': '„Wie steht es aktuell um die Verbreitung und den Schutz der einheimischen Stachellosen '
                 'Bienen Brasiliens, und wie können eine rationelle Meliponikultur und Hotels für '
                 'Solitärbienen zum Erhalt dieser Arten in städtischen und stadtnahen Lebensräumen '
                 'beitragen?“',
        'pipeline_label': 'DATEN-PIPELINE',
        'steps': [['1',
                   'Datenerhebung — GBIF + iNaturalist (2010–2024)',
                   'Fundangaben brasilianischer Meliponini über die GBIF-API und den iNaturalist-Export. '
                   '@@TOTAL@@ georeferenzierte Datensätze (2010–2024), gefiltert ohne geografische Probleme. '
                   'Zielarten: 12 einheimische Meliponini + 6 Solitärbienen.'],
                  ['2',
                   'Fachexkursion — Cidade das Abelhas (SP, 2022)',
                   'Fachexkursion in den Park Cidade das Abelhas in São Paulo zur direkten Beobachtung '
                   'rationeller Beuten von Jataí, Mosquitinho, Manduri, Mirim Preguiça und weiteren Arten. '
                   'Fotodokumentation und Erhebung von Daten zur rationellen Haltung in Meliponarien.'],
                  ['3',
                   'Abschlussarbeit FATEC Jundiaí — Hotel für Solitärbienen (2022)',
                   'Abschlussprojekt: Bau eines Hotels für Solitärbienen auf dem Campus der FATEC Jundiaí '
                   'für die Veranstaltung Ciência na Praça. Holzkonstruktion mit Bohrungen von 8 und 10 mm '
                   'für einheimische Solitärbienen wie Xylocopa sp. und Megachile sp.'],
                  ['4',
                   'Räumliche Analyse — Verteilung nach Biom',
                   'Verschneidung der Funde mit dem Shapefile der IBGE-Biome. Identifizierung von Mustern '
                   'des Artenreichtums je Biom. Die Mata Atlântica ist das Biom mit der größten '
                   'Meliponini-Vielfalt (~22 Arten).'],
                  ['5',
                   'Biologische Parameter — Wissenschaftliche Literatur',
                   'Zusammenstellung von Literaturdaten: Koloniegröße, Legerate, Lebensdauer der '
                   'Arbeiterinnen, Sammelradius, Honigproduktion. Grundlage: A.B.E.L.H.A., Atlas da '
                   'Meliponicultura, Veröffentlichungen von USP/UNICAMP/UFMG.'],
                  ['6',
                   'Gefährdungsbewertung — IUCN Red List',
                   'Abgleich der Fundangaben mit dem IUCN-Status: @@VU@@ gefährdete Arten (VU), @@LC@@ nicht '
                   'gefährdet (LC). Analyse von Bestandstrends und menschlichen Belastungen je Biom.']],
        'biologia_title': '🐝 Warum sind Stachellose Bienen wichtig?',
        'biologia_text': '• <b>~550 Arten</b> von Meliponini weltweit beschrieben · <b>~350 in '
                         'Brasilien</b><br>• <b>Exklusive Bestäuber</b> einheimischer Arten der Mata '
                         'Atlântica und des Cerrado<br>• <b>Honig mit medizinischen Eigenschaften</b>, '
                         'anerkannt von der ANVISA (Portaria 310/1997)<br>• <b>Meliponikultur</b>: '
                         'rationelle Haltung in Beuten der Typen INPA, IBAMA, JTB, Fernão Dias<br>• '
                         '<b>Bedrohungen:</b> Entwaldung, Pestizide, Urbanisierung, invasive gebietsfremde '
                         'Arten',
        'solitarias_title': '🏨 Solitärbienen — Die stille Mehrheit',
        'solitarias_text': '• <b>~70 % der Bienen weltweit</b> leben solitär — ohne Königin, ohne '
                           'Bienenvolk<br>• <b>Jedes Weibchen</b> baut sein eigenes Nest, sammelt Nahrung '
                           'und versorgt die Eier<br>• <b>Bienenhotels</b> (Holzblöcke mit 6–10 mm '
                           'Bohrungen) ziehen Xylocopa, Megachile und Hylaeus an<br>• <b>Ideale '
                           'Bohrungen:</b> 8-mm-Bohrer (Megachile), 10-mm-Bohrer (Xylocopa) — Mindesttiefe '
                           '10 cm<br>• <b>Aufstellung:</b> Ausrichtung Ost/Südost, Höhe 1–2 m, vor direktem '
                           'Regen geschützt',
        'disc_label': 'ANALYSE UND ERKENNTNISSE',
        'disc_title': 'Was die Daten gezeigt haben',
        'discoveries': [['🐝',
                         'Jataí — die am besten an die Urbanisierung angepasste Art',
                         'Tetragonisca angustula ist die Art mit der größten Anpassungsfähigkeit an urbane '
                         'Räume. Nachweise in allen brasilianischen Bundesstaaten und in allen 5 Biomen. Sie '
                         'nistet in Mauerritzen, Stromkästen und Masten. Ihre Präsenz in Städten gilt als '
                         'Indikator ökologischer Resilienz.'],
                        ['⚠️',
                         '@@VU@@ gefährdete Arten — @@VU_LIST@@',
                         'Die größeren und honigreichsten Melipona-Arten sind am stärksten bedroht. Die '
                         'Kombination aus Entwaldung, menschlichem Druck und geringer Fortpflanzung (die '
                         'Königin unternimmt nur einen Hochzeitsflug) macht diese Arten besonders anfällig '
                         'für einen Zusammenbruch der Bestände.'],
                        ['🏨',
                         'Bienenhotel — Multiplikator urbaner Biodiversität',
                         'Das an der FATEC Jundiaí gebaute Bienenhotel hat gezeigt, dass einfache '
                         'Holzstrukturen mit 8- und 10-mm-Bohrungen innerhalb von 30–60 Tagen von '
                         'einheimischen Solitärbienen besiedelt werden. Ein kostengünstiger Eingriff (<R$50) '
                         'mit großer Wirkung für die lokale Bestäubung.'],
                        ['📊',
                         'São Paulo — die brasilianische Hauptstadt der Meliponikultur',
                         '@@SP_SENT@@ Die Kombination aus verbliebener Mata Atlântica, intensiver '
                         'universitärer Forschung (USP, UNICAMP, UNESP) und wachsender urbaner '
                         'Meliponikultur erklärt diese Vorreiterrolle.'],
                        ['🌎',
                         'GBIF: @@GROWTH@@ in 10 Jahren — Citizen Science als Motor',
                         'Der Zuwachs von @@GROWTH_ABS@@ georeferenzierten Meliponini-Datensätzen in '
                         'Brasilien zwischen 2014 und 2024 (@@GROWTH@@) geht einher mit der zunehmenden '
                         'Nutzung von iNaturalist und dem wachsenden Interesse der Bevölkerung an '
                         'Biodiversität. Die wachsende urbane Meliponikultur ist zugleich Folge und Ursache '
                         'dieses Interesses.'],
                        ['🌿',
                         'Cerrado — unterbeprobtes Biom mit großer verborgener Vielfalt',
                         'Obwohl der Cerrado ~100 endemische Meliponini-Arten beherbergt, ist er in den '
                         'Biodiversitätsdaten historisch unterbeprobt. Die Unterbeprobung spiegelt '
                         'Forschungslücken in abgelegenen Gebieten wider — eine Mahnung zum Schutz, bevor '
                         'das Biom zu 100 % fragmentiert ist.']],
        'conclusion_label': 'FAZIT',
        'conclusion_title': 'Jede Beute zählt',
        'conclusion_text': 'Die einheimischen Stachellosen Bienen Brasiliens sind ein einzigartiges '
                           'biokulturelles Erbe: seit Jahrtausenden von indigenen Völkern gehalten, Erzeuger '
                           'von Honig mit medizinischen Eigenschaften und unersetzliche Bestäuber unserer '
                           'einheimischen Flora. Der Zuwachs von @@GROWTH_N@@ bei den GBIF-Datensätzen zu '
                           'Meliponini zeigt, dass das Interesse an der Meliponikultur wächst — doch das '
                           'Tempo der Entwaldung übersteigt weiterhin die Geschwindigkeit des Naturschutzes. '
                           'Jede aufgestellte rationelle Beute, jedes gebaute Bienenhotel, jedes geschützte '
                           'Waldfragment ist ein Vertrauensbeweis in die Zukunft dieser Arten.',
        'conclusion_author': 'Amauri Almeida · Abschlussarbeit Umweltmanagement · FATEC Jundiaí · 2022 · '
                             'Besuch der Cidade das Abelhas SP',
        'field_label': 'FELD- UND FACHDOKUMENTATION',
        'field_title': 'Von der Cidade das Abelhas zum FATEC-Campus',
        'field_inst_title': '📁 So fügen Sie Ihre Fotos hinzu',
        'field_inst': 'Legen Sie Ihre Fotos mit den untenstehenden exakten Dateinamen im Ordner '
                      '<code>assets/campo/</code> ab.',
        'photos': [{'emoji': '🐝',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Rationelle Beute — Jataí-Biene',
                    'esp': 'Tetragonisca angustula',
                    'desc': 'Rationelle Beute (JTB- oder INPA-Kasten) der Jataí-Biene (Tetragonisca '
                            'angustula) im Park Cidade das Abelhas, São Paulo. Die Jataí ist die häufigste '
                            'und anpassungsfähigste Art Brasiliens — sie nistet natürlicherweise in '
                            'Mauerritzen. Die rationelle Beute ermöglicht die Teilung von Völkern und die '
                            'Haltung, ohne das Nest zu zerstören.',
                    'path': 'assets/campo/01_colmeia_jatai_cidade_abelhas.jpg',
                    'legenda': 'Jataí-Beute (Tetragonisca angustula) · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🔎',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Rationelle Beute — Mosquitinho-Biene',
                    'esp': 'Plebeia mosquito',
                    'desc': 'Rationelle Beute der Mosquitinho-Biene (Plebeia mosquito) — eine der kleinsten '
                            'Stachellosen Bienen Brasiliens (2 mm). Äußerst friedlich und empfindlich '
                            'gegenüber Pestiziden. Die Beute hat ein Honigmodul, das vom Brutmodul getrennt '
                            'ist — eine grundlegende Praxis der rationellen Meliponikultur, um das Volk '
                            'nicht zu schädigen.',
                    'path': 'assets/campo/02_colmeia_mosquitinho_cidade_abelhas.jpg',
                    'legenda': 'Mosquitinho-Beute (Plebeia mosquito) · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🌿',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Rationelle Beute — Manduri-Biene (1)',
                    'esp': 'Melipona marginata',
                    'desc': 'Rationelle Beute der Manduri-Biene (Melipona marginata) — gefährdete Art (IUCN '
                            'VU). Eine der wichtigsten Arten für den Artenschutz: seltener Honig in geringer '
                            'Menge, nistet ausschließlich in Hohlräumen einheimischer Bäume. Die rationelle '
                            'Meliponikultur ist die wichtigste Ex-situ-Schutzstrategie für diese Art.',
                    'path': 'assets/campo/04_colmeia_manduri_cidade_abelhas_1.jpg',
                    'legenda': 'Manduri-Beute (Melipona marginata) · Gefährdet · Cidade das Abelhas · SP · '
                               '2022',
                    'gid': 'cidade'},
                   {'emoji': '🌿',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Rationelle Beute — Manduri-Biene (2)',
                    'esp': 'Melipona marginata',
                    'desc': 'Zweite dokumentierte Manduri-Beute. Die Begleitung mehrerer Beuten derselben '
                            'Art ermöglicht es, Unterschiede im Verhalten und in der Produktion zu '
                            'untersuchen. Die Unterschiede in Farbe und Aufbau zwischen den Kästen spiegeln '
                            'verschiedene Modelle rationeller Beuten wider — INPA, Fernão Dias, JTB und '
                            'USP-Modelle.',
                    'path': 'assets/campo/05_colmeia_manduri_cidade_abelhas_2.jpg',
                    'legenda': 'Manduri-Beute (2) · Melipona marginata · VU · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Rationelle Beute — Mirim Preguiça (1)',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'Rationelle Beute der Mirim-Preguiça-Biene (Frieseomelitta varia) — benannt nach '
                            'dem ruhigen Verhalten der Arbeiterinnen am Beuteneingang. Wichtige Art für die '
                            'Bestäubung einheimischer Arten des Cerrado und der Mata Atlântica. Baut Nester '
                            'an Baumästen.',
                    'path': 'assets/campo/06_colmeia_mirim_preguica_1.jpg',
                    'legenda': 'Mirim-Preguiça-Beute (Frieseomelitta varia) · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Rationelle Beute — Mirim Preguiça (2)',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'Zweite Ansicht der Mirim-Preguiça-Beute. Zu sehen ist der Beuteneingang mit den '
                            'artspezifischen Merkmalen. Die innere Nestarchitektur mit kugelförmigen '
                            'Brutzellen unterscheidet sich von der der Melipona — daher sind für diese Art '
                            'besondere Anpassungen an den rationellen Kästen nötig.',
                    'path': 'assets/campo/07_colmeia_mirim_preguica_2.jpg',
                    'legenda': 'Mirim-Preguiça-Beute (2) · Frieseomelitta varia · Cidade das Abelhas · SP · '
                               '2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Rationelle Beute — Mirim Preguiça (3)',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'Dritte Perspektive der Mirim-Preguiça-Beute mit Details der äußeren Struktur '
                            'und der Halterung. Die Dokumentation mehrerer Ansichten ist bei Fachexkursionen '
                            'unerlässlich, um Haltungsmuster und Beutendesigns zu erkennen, die für jede Art '
                            'am besten funktionieren.',
                    'path': 'assets/campo/08_colmeia_mirim_preguica_3.jpg',
                    'legenda': 'Mirim-Preguiça-Beute (3) · Frieseomelitta varia · Cidade das Abelhas · SP · '
                               '2022',
                    'gid': 'cidade'},
                   {'emoji': '🏛️',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Meliponarium — Sammlung verschiedener Arten',
                    'esp': 'Mehrere Arten',
                    'desc': 'Ansicht des Meliponariums im Park Cidade das Abelhas mit rationellen Kästen '
                            'verschiedener Arten nebeneinander — so, wie es die gute meliponikulturelle '
                            'Praxis empfiehlt. Jede Art hat ihren gekennzeichneten Kasten. Der Abstand '
                            'zwischen den Beuten und die Ausrichtung des Eingangs sind so berechnet, dass '
                            'das Abdriften von Bienen minimiert und die Gesundheit der Völker maximiert '
                            'wird.',
                    'path': 'assets/campo/09_meliponario_colecao_cidade_abelhas.jpg',
                    'legenda': 'Meliponarium mit verschiedenen Arten · Rationelle Kästen · Park Cidade das '
                               'Abelhas · SP · 2022',
                    'destaque': True,
                    'gid': 'cidade'},
                   {'emoji': '🌳',
                    'grupo': 'BIENENHOTEL · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Bau des Hotels — Holzkonstruktion',
                    'esp': 'Für Solitärbienen',
                    'desc': 'Beginn des Baus des Hotels für Solitärbienen auf dem Campus der FATEC Jundiaí. '
                            'Die Holzkonstruktion ist der Hauptträger für die gebohrten Blöcke. Die Wahl des '
                            'Holzes (behandelte Kiefer oder Eukalyptus) ist wichtig: Es muss '
                            'feuchtigkeitsbeständig sein, darf aber nicht mit Bioziden behandelt sein, die '
                            'Bienen vertreiben.',
                    'path': 'assets/campo/10_hotel_abelhas_estrutura_madeira.jpg',
                    'legenda': 'Bau des Bienenhotels · Holzkonstruktion · FATEC Jundiaí · Ciência na Praça · '
                               '2022',
                    'gid': 'hotel'},
                   {'emoji': '🔩',
                    'grupo': 'BIENENHOTEL · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Bohren der Blöcke — Bohrer 8 und 10 mm',
                    'esp': 'Für Solitärbienen',
                    'desc': 'Bohren der Holzblöcke mit der Bohrmaschine, mit 8-mm-Bohrer (Megachile sp., '
                            'Hylaeus sp.) und 10-mm-Bohrer (Xylocopa sp.). Eine Mindesttiefe von 10 cm ist '
                            'wichtig, damit das Weibchen das Nest mit 3–5 Brutzellen fertigstellen kann. Die '
                            'Bohrungen müssen blind enden — sie dürfen den Block nicht durchdringen.',
                    'path': 'assets/campo/11_hotel_abelhas_furadeira_broca8_10.jpg',
                    'legenda': 'Bohren mit 8- und 10-mm-Bohrer · Solitärbienen-Hotel · FATEC Jundiaí · 2022',
                    'gid': 'hotel'},
                   {'emoji': '🔩',
                    'grupo': 'BIENENHOTEL · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Bohrungen im Detail — Bohrer 8 und 10 mm',
                    'esp': 'Für Solitärbienen',
                    'desc': 'Detail des Bohrvorgangs mit 8- und 10-mm-Bohrer. Gleichmäßige Bohrungen sind '
                            'für den Erfolg des Hotels wichtig: Mindesttiefe 10 cm, exakter Durchmesser und '
                            'glatte Innenfläche (bei Bedarf schleifen). Bohrungen mit ausgefransten '
                            'Innenwänden können den Bienen den Zugang erschweren.',
                    'path': 'assets/campo/12_hotel_abelhas_furos_detalhe.jpg',
                    'legenda': 'Detail der Bohrungen 8/10 mm · Solitärbienen-Hotel · FATEC Jundiaí · 2022',
                    'gid': 'hotel'},
                   {'emoji': '✅',
                    'grupo': 'BIENENHOTEL · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Fertiggestelltes Bienenhotel — Campus FATEC Jundiaí',
                    'esp': 'Für Solitärbienen',
                    'desc': 'Fertiggestelltes Hotel für Solitärbienen, aufgestellt auf dem Campus der FATEC '
                            'Jundiaí für die Veranstaltung Ciência na Praça. Holzblöcke mit Bohrungen von 8 '
                            'und 10 mm, Ausrichtung Ost/Südost, Höhe ~1,5 m, durch ein Dach vor Regen '
                            'geschützt. Kostengünstige Konstruktion (<R$50) mit großer Wirkung für die '
                            'lokale Bestäubung.',
                    'path': 'assets/campo/13_hotel_abelhas_concluido_fatec_jundiai.jpg',
                    'legenda': 'Fertiggestelltes Solitärbienen-Hotel · Campus FATEC Jundiaí · Ciência na '
                               'Praça · 2022',
                    'destaque_final': True,
                    'gid': 'hotel'}],
        'timeline_label': 'PROJEKTZEITLEISTE',
        'timeline_items': [['2022 · Jan–Jun',
                            'Abschlussarbeit Umweltmanagement — FATEC Jundiaí',
                            'Forschung zu Meliponikultur und Solitärbienen · Bienenhotel für Ciência na '
                            'Praça gebaut'],
                           ['2022 · Jul',
                            'Fachexkursion — Cidade das Abelhas SP',
                            'Fotodokumentation von 8+ Arten in rationellen Beuten · Jataí, Mosquitinho, '
                            'Manduri, Mirim Preguiça und weitere'],
                           ['2022 · Nov',
                            'Verteidigung der Abschlussarbeit — FATEC Jundiaí',
                            'Abschlussarbeit im Studiengang Umweltmanagement bestanden · Bachelor-Abschluss '
                            'erteilt'],
                           ['2023–2024',
                            'GBIF-Analyse — @@TOTAL@@ Datensätze',
                            'Verschneidung der Fundangaben mit Biomen und Bundesstaaten · Identifizierung '
                            'von Schutzlücken'],
                           ['2025',
                            'Veröffentlichung im Portfolio',
                            'Meliponini-Observatorium Brasilien — öffentliches Dashboard mit aktuellen '
                            'Daten']],
        'trend_sel': 'Darstellung auswählen',
        'trend_opt1': 'GBIF-Wachstum (2010–2024)',
        'trend_opt2': 'Datensätze pro Art (Ranking)',
        'trend_opt3': 'Datensätze pro Bundesstaat',
        'param_sel': 'Art für die Analyse',
        'param_names': {'colonia': 'Koloniegröße (Arbeiterinnen)',
                        'postura_dia': 'Legerate (Eier/Tag)',
                        'vida_operaria': 'Lebensdauer der Arbeiterin (Tage)',
                        'longe_formag': 'Sammelradius (m)',
                        'prod_mel_kg': 'Honigproduktion (kg/Jahr)',
                        'raio_dna_km': 'Genetische Distanz (km)'},
        'raw_label': 'ARTENKATALOG',
        'raw_title': 'Vollständige Tabelle — Meliponini Brasiliens',
        'download_csv': '⬇️ CSV herunterladen',
        'sources_label': 'WISSENSCHAFTLICHE QUELLEN',
        'sources_title': 'Quellen & Datenbasis',
        'tech_label': 'VERWENDETE TECHNOLOGIEN',
        'footer_title': '🐝 Amauri Almeida',
        'footer_desc': 'Technologe für Umweltmanagement · FATEC Jundiaí (3. Platz im '
                       'ENADE)<br>Postgraduiertenstudium in KI, Machine Learning & Data Science · '
                       'Datenwissenschaft & Big Data<br>Systemanalyse und -entwicklung · FACINT Maringá',
        'footer_links': '📍 Fernandópolis · SP · Brasilien',
        'trend_label': 'ZEITLICHE ENTWICKLUNG & RANKINGS',
        'param_label': 'VERGLEICHENDE BIOLOGIE',
        'param_title': 'Biologische Parameter der Arten',
        'param_detail': 'Biologischer Parameter',
        'param_cmp': 'Vergleich der Arten',
        'records_axis': 'Datensätze',
        'records_hover': 'Datensätze',
        'gal_meli': 'ARTENGALERIE — MELIPONINI',
        'gal_sol': 'GALERIE — SOLITÄRBIENEN',
        'honey': 'Honig',
        'mel_vals': {'Sim': 'Ja', 'Não': 'Nein', 'Pouco': 'Wenig'},
        'gbif_records': 'GBIF-Datensätze',
        'pop_records': 'Datensätze',
        'pop_species': 'Arten',
        'pop_status': 'Status',
        'status_vals': {'Alta': 'Hoch', 'Média': 'Mittel', 'Baixa': 'Niedrig'},
        'radar_title': 'Vergleichsprofil der Arten (Skala 0–10)',
        'radar_cats': ['Honigproduktion', 'Urbane Anpassung', 'Flugradius', 'Koloniegröße', 'IUCN (inv.)'],
        'grp_city': '🏛️ CIDADE DAS ABELHAS (BIENENSTADT) · SÃO PAULO · 2022',
        'grp_hotel': '🏨 SOLITÄRBIENEN-HOTEL · FATEC JUNDIAÍ · CIÊNCIA NA PRAÇA · 2022',
        'dest_melipon': '⭐ HIGHLIGHT — VOLLSTÄNDIGES MELIPONARIUM · CIDADE DAS ABELHAS',
        'dest_hotel': '✅ FINALES HIGHLIGHT — FERTIGES HOTEL · CAMPUS FATEC JUNDIAÍ',
        'hotel_build_title': '🏗️ So baut man ein Hotel für Solitärbienen',
        'hotel_build': [['Material',
                         'Holzblock (behandelte Kiefer oder Eukalyptus) · mindestens 15×10×10 cm'],
                        ['Bohrungen', '8-mm-Bohrer (Megachile, Hylaeus) · 10-mm-Bohrer (Xylocopa)'],
                        ['Tiefe', 'Mindestens 10 cm · Blind endend (den Block nicht durchbohren!)'],
                        ['Ausrichtung', 'Ost oder Südost · Morgensonne'],
                        ['Höhe', '1–2 Meter über dem Boden · Vor Regen und Wind geschützt'],
                        ['Ergebnis', 'Besiedlung durch einheimische Bienen innerhalb von 30–60 Tagen']],
        'solitary_tbl': 'Solitärbienen',
        'card_lbls': {'biome': 'Biom',
                      'region': 'Region',
                      'colony': 'Kolonie',
                      'workers': 'Arbeiterinnen',
                      'laying': 'Legerate',
                      'eggs_day': 'Eier/Tag',
                      'worker_life': 'Lebensdauer Arbeiterin',
                      'days': 'Tage',
                      'forage': 'Sammelradius',
                      'honey': 'Honigproduktion',
                      'kg_year': 'kg/Jahr',
                      'gen_dist': 'Genet. Distanz'},
        'carto_fallback': 'Alternative Basiskarte (OpenStreetMap) in Verwendung.',
        'occ_live': 'Echte GBIF-Punkte (api.gbif.org): {n} georeferenzierte Funde in Brasilien, bis zu {k} '
                    'pro Art, abgefragt am {d}. Klicken Sie auf einen Punkt, um den Originaldatensatz zu '
                    'öffnen.',
        'occ_demo': 'GBIF derzeit nicht verfügbar: Die gezeigten Punkte sind ILLUSTRATIV (Hauptstädte × '
                    'Arten) und keine Felddatensätze.',
        'occ_none': 'GBIF derzeit nicht verfügbar und keine Ersatzdaten vorhanden: Fundkarte wird nicht '
                    'angezeigt.',
        'dados_live': 'Zahlen berechnet aus GBIF (api.gbif.org), abgefragt am {d}; automatische '
                      'Aktualisierung alle 24 h.',
        'dados_snapshot': 'GBIF derzeit nicht verfügbar: Zahlen des zuletzt gespeicherten Snapshots ({d}).',
        'dados_static': 'GBIF derzeit nicht verfügbar: Referenzwerte aus einer früheren Zusammenstellung, '
                        'nicht aktualisiert.',
        'serie_total': 'Gesamt (Meliponini + 5 solitäre Gattungen)',
        'serie_inat': 'iNaturalist (Meliponini)',
        'raio_sel': 'Sammelradius anzeigen (Kreise in Metern)',
        'raio_note': 'Jeder Kreis zeigt den mittleren Flugradius der Art um reale Fundpunkte (bis zu {n} pro '
                     'Art). Zoomen Sie in die Karte, um den Maßstab zu sehen.',
        'raio_layer': 'Sammelradius',
        'footer_portfolio': 'Portfolio',
        'sources': [['GBIF',
                     'GBIF — Global Biodiversity Information Facility',
                     'gbif.org · Fundortdatenbank mit @@TOTAL@@ georeferenzierten Datensätzen zu Meliponini '
                     'in Brasilien (2010–2024). Daten von Museen, Herbarien, iNaturalist und Forschenden.',
                     '#C47D0E'],
                    ['A.B.E.L.H.A.',
                     'A.B.E.L.H.A. — Brasilianische Vereinigung für Bienenforschung',
                     'abelha.org.br · Atlas der Meliponikultur in Brasilien. Referenz für Sammelradien, '
                     'Biologie und Artenschutz.',
                     '#C0390A'],
                    ['INATURALIST',
                     'iNaturalist — Globale Citizen Science',
                     'inaturalist.org · @@INAT@@ georeferenzierte Datensätze brasilianischer Meliponini '
                     '(iNaturalist-Research-Grade-Datensatz in GBIF). Hauptmotor des GBIF-Wachstums.',
                     '#2D7A45'],
                    ['FATEC',
                     'FATEC Jundiaí — Abschlussarbeit Umweltmanagement (2022)',
                     'Hotel für Solitärbienen, auf dem Campus für die Veranstaltung Ciência na Praça gebaut. '
                     'Bohrer 8 und 10 mm. Mit Auszeichnung bestanden.',
                     '#1B3A1E'],
                    ['CIDADE ABELHAS',
                     'Park Cidade das Abelhas — São Paulo (2022)',
                     'Fachexkursion 2022. Fotodokumentation rationeller Beuten von Jataí, Mosquitinho, '
                     'Manduri, Mirim Preguiça und weiteren.',
                     '#5C3D1E'],
                    ['IUCN',
                     'IUCN Red List — Rote Liste gefährdeter Arten',
                     '@@VU_TAGS@@. Schutzstatus der brasilianischen Meliponini.',
                     '#8B2515'],
                    ['INPA',
                     'INPA — Nationales Institut für Amazonasforschung',
                     'INPA-Modell der rationellen Beute für amazonische Meliponini. Artdaten aus dem Norden '
                     'Brasiliens.',
                     '#0D4E72'],
                    ['EMBRAPA',
                     'EMBRAPA Cerrados / EMBRAPA Amazônia Oriental',
                     'Daten zur Meliponikultur in den brasilianischen Biomen. Fachliche Referenz für Arten '
                     'des Cerrado und des Amazonas.',
                     '#C47D0E']],
        'species_text': {'Jataí': {'descricao': 'Die bekannteste Stachellose Biene Brasiliens. Liefert Honig '
                                                'von höchster Qualität mit medizinischen Eigenschaften. '
                                                'Nester in Baumhöhlen und Mauerritzen. Der Nesteingang wird '
                                                'mit Propolis zu einer Röhre oder zu Plättchen verschlossen.',
                                   'bioma': 'Alle',
                                   'regiao': 'Landesweit'},
                         'Mosquitinho': {'descricao': 'Eine der kleinsten Stachellosen Bienen Brasiliens. '
                                                      'Äußerst friedlich. Sehr schmackhafter Honig in '
                                                      'kleinen Mengen. Sehr empfindlich gegenüber '
                                                      'Pestiziden. Indikator für Umweltqualität.',
                                         'bioma': 'Mata Atlântica',
                                         'regiao': 'Süd/Südost'},
                         'Manduri': {'descricao': 'Vom Aussterben bedrohte Art (VU). Seltener Honig in '
                                                  'kleinen Mengen. Nester meist in Hohlräumen einheimischer '
                                                  'Bäume. Zielart von Meliponikultur-Programmen zum '
                                                  'Artenschutz.',
                                     'bioma': 'Mata Atlântica',
                                     'regiao': 'Süd/Südost'},
                         'Mirim Preguiça': {'descricao': 'Wegen ihres ruhigen Verhaltens auch „Faulbiene“ '
                                                         '(Abelha Preguiça) genannt. Nistet hauptsächlich an '
                                                         'Baumästen. Wichtiger Bestäuber einheimischer Arten '
                                                         'des Cerrado und der Mata Atlântica.',
                                            'bioma': 'Cerrado/Mata Atlântica',
                                            'regiao': 'Mitte/Südost'},
                         'Mandaçaia': {'descricao': 'Eine der größten Stachellosen Bienen. Besondere '
                                                    'Honigproduktion. Rückgang durch Entwaldung und '
                                                    'Urbanisierung. Seit Jahrhunderten von den indigenen '
                                                    'Guaraní als „mborí“ gehalten.',
                                       'bioma': 'Mata Atlântica',
                                       'regiao': 'Südost/Süd'},
                         'Uruçu Nordestina': {'descricao': 'Heilige Biene der Tupinambá, seit über 2.000 '
                                                           'Jahren gehalten. Honig mit anerkannten '
                                                           'medizinischen Eigenschaften. Symbol der '
                                                           'Meliponikultur im Nordosten. Leitart der '
                                                           'indigenen Bienenhaltung.',
                                              'bioma': 'Caatinga/Mata Atlântica NO',
                                              'regiao': 'Nordost'},
                         'Irapuá': {'descricao': 'Obwohl sie keinen Honig in kommerziellen Mengen '
                                                 'produziert, ist sie eine äußerst wichtige Bestäuberin. '
                                                 'Baut freiliegende Nester aus Pflanzenharz. Wird wegen '
                                                 'ihres Verteidigungsverhaltens manchmal mit der '
                                                 'Europäischen Honigbiene verwechselt.',
                                    'bioma': 'Alle',
                                    'regiao': 'Landesweit'},
                         'Tiúba': {'descricao': 'In Maranhão als „Abelha da Terra“ („Erdbiene“) bekannt. '
                                                'Honig mit einzigartigem, sehr geschätztem Geschmack. '
                                                'Grundlegender Bestandteil der Meliponikultur-Kultur in '
                                                'Amazonien und Maranhão. Durch Entwaldung gefährdete Art.',
                                   'bioma': 'Amazonien/Nordosten',
                                   'regiao': 'Nord/Nordost'},
                         'Guaraipo': {'descricao': 'Art mit variabler Färbung. Honigproduktion von mildem '
                                                   'Geschmack. Nester im Boden oder in Baumstämmen. Starker '
                                                   'Rückgang durch das Vordringen der Landwirtschaft im '
                                                   'Cerrado.',
                                      'bioma': 'Cerrado/Mata Atlântica',
                                      'regiao': 'Mittelwesten/Südost'},
                         'Iraí': {'descricao': 'Sehr häufige Biene in urbanen Lebensräumen. Nistet in '
                                               'Wandritzen, Stromkästen und Dachziegeln. Sehr tolerant '
                                               'gegenüber Urbanisierung. Hervorragender Indikator für die '
                                               'Vernetzung von Waldfragmenten.',
                                  'bioma': 'Cerrado/Mata Atlântica',
                                  'regiao': 'Südost'},
                         'Tubuna': {'descricao': 'Erzeugt dunklen, intensiven Honig. Nester in Baumhöhlen. '
                                                 'Sehr empfindlich gegenüber Entwaldung. Wird in Projekten '
                                                 'zur Wiederherstellung von Waldfragmenten als zentrale '
                                                 'Bestäuberin eingesetzt.',
                                    'bioma': 'Mata Atlântica',
                                    'regiao': 'Südost/Süd'},
                         'Mirim Guaçu': {'descricao': 'Kälteresistente Art. Sehr häufig in Santa Catarina '
                                                      'und Rio Grande do Sul. Bestäuberin einheimischer und '
                                                      'kultivierter Arten der Südregion. Honig mit '
                                                      'charakteristisch saurem Geschmack.',
                                         'bioma': 'Süd/Südost',
                                         'regiao': 'Süd/Südost'},
                         'Abelha Mamangava': {'descricao': 'Exklusive Bestäuberin der Passionsfrucht. Ohne '
                                                           'sie würde die Passionsfruchtproduktion in '
                                                           'Brasilien zusammenbrechen. Nutzt die Technik der '
                                                           '„Buzz Pollination“, indem sie die Blüten in '
                                                           'Schwingung versetzt, um den Pollen freizusetzen. '
                                                           'Baut Nester in trockenen Ästen.',
                                              'habitat': 'Nistet in Totholz',
                                              'polinizacao': 'Buzz Pollination — Vibration löst den Pollen'},
                         'Abelha Carpinteira': {'descricao': 'Gattung Xylocopa mit über 50 Arten in '
                                                             'Brasilien. „Carpinteira“ (Holzbiene) wegen '
                                                             'ihrer Fähigkeit, Holz für Nester auszuhöhlen. '
                                                             'Wichtige Bestäuber röhrenförmiger Blüten. '
                                                             'Nester in Bienenhotels mit Bambusröhrchen.',
                                                'habitat': 'Trockenes Holz, Bambus',
                                                'polinizacao': 'Generalistin — hohe Blütenvielfalt'},
                         'Abelha Mascarada': {'descricao': 'Winzig, aber unverzichtbar. Transportiert Pollen '
                                                           'im Kropf, nicht in Pollenkörbchen. Trägt Nektar '
                                                           'und Pollen im Körperinneren. Nimmt Bienenhotels '
                                                           'mit Papier- und Bambusröhrchen von 5–6 mm '
                                                           'Durchmesser sehr gut an.',
                                              'habitat': 'Röhrchen, hohle Zweige',
                                              'polinizacao': 'Kleine, offene Blüten'},
                         'Abelha Cortadeira': {'descricao': 'Schneidet Blattstücke zum Nestbau aus — daher '
                                                            'der Name. Wird als „Schädling“ angesehen, ist '
                                                            'aber eine wichtige einheimische Bestäuberin. '
                                                            'Nester in Bohrlöchern im Holz (8–10-mm-Bohrer '
                                                            'ideal für Hotels).',
                                               'habitat': 'Boden, Holz, geschnittene Blätter',
                                               'polinizacao': 'Einheimische Arten — Cerrado, Mata Atlântica'},
                         'Abelha Nômade': {'descricao': 'Kleptoparasitische Bienen, die ihre Eier in die '
                                                        'Nester anderer Solitärbienen legen. Sehen aus wie '
                                                        'Wespen, sind aber Bienen. Wichtig für die '
                                                        'Regulierung von Beständen und das ökologische '
                                                        'Gleichgewicht in Waldlebensräumen.',
                                           'habitat': 'Parasit in fremden Nestern',
                                           'polinizacao': 'Indirekt — erhält das ökologische Gleichgewicht'},
                         'Abelha Oleiro': {'descricao': 'Obligate Bestäuber von Murici, Barbatimão und '
                                                        'anderen Malpighiaceae. Sammeln Blütenöl, um ihre '
                                                        'Larven zu füttern. Nester im Boden. Indikatoren für '
                                                        'intakten Cerrado.',
                                           'habitat': 'Sandboden, Steilwände',
                                           'polinizacao': 'Buzzing an Ölblüten — Malpighiaceae'}},
        'back_link': '← Portfolio',
        'lang_label': 'Sprache',
        'cluster_name': 'Funde',
        'footer_copy': '© 2022–2026 · Meliponini-Observatorium · Brasilien',
        'raw_cols': {'especie': 'Art',
                     'cientifico': 'Wissenschaftlicher Name',
                     'tamanho': 'Größe',
                     'raio': 'Sammelradius (m)',
                     'mel': 'Honigproduktion',
                     'iucn': 'IUCN',
                     'bioma': 'Biom',
                     'registros': 'GBIF-Datensätze',
                     'colonia': 'Kolonie (Arb.)',
                     'mel_ano': 'Honig/Jahr (kg)',
                     'habitat': 'Lebensraum',
                     'polinizacao': 'Bestäubung',
                     'tipo': 'Typ'},
        'tipo_vals': {'meli': 'Meliponini', 'sol': 'Solitär'},
        'tok_nd': 'Tausende',
        'tok_and': ' und ',
        'tok_sp_top': 'SP vereint {n} GBIF-Datensätze — mehr als jeder andere Bundesstaat.',
        'tok_sp_plain': 'SP vereint {n} GBIF-Datensätze.',
        'tok_sp_generic': 'SP gehört zu den am besten erfassten Bundesstaaten.'},
 'zh': {'page_title': 'Meliponini 观测站 · 巴西',
        'hero_tag': '生物多样性 · MELIPONINI · 巴西 · 2022–2025',
        'hero_title': '无刺蜂\n观测站',
        'hero_subtitle': '监测并分析巴西本土无刺蜂（Meliponini）与独居蜂的分布——超过24,000条GBIF记录，绘制12个物种，并开展积极保护。内容包括2022年对Cidade '
                         'das Abelhas（圣保罗州）的技术考察，以及在FATEC Jundiaí建造的独居蜂旅馆。',
        'badge1': '🐝 监测12个物种',
        'badge2': '🗺️ 300+个分布点',
        'badge3': '巴西 · 5大生物群系',
        'badge4': 'GBIF · iNaturalist · INPA',
        'badge5': 'FATEC Jundiaí毕业设计 2022',
        'm1': 'Meliponini物种',
        'm2': 'GBIF记录（2024）',
        'm3': '覆盖州数',
        'm4': '受威胁物种',
        'tab1': '🗺️ 地图与分析',
        'tab2': '🔬 方法与流程',
        'tab3': '💡 研究发现',
        'tab4': '📷 实地记录',
        'tab5': '📈 趋势',
        'tab6': '⚙️ 参数',
        'tab7': '📋 原始数据',
        'tab8': '📚 来源与致谢',
        'map_label': '巴西分布',
        'map_title': '分布记录地图——无刺蜂',
        'map_hint': '🐝 <strong>点击标记</strong>可查看物种、生物群系和数据来源。圆点大小与各州记录数成正比。开启聚类可查看聚合分组。',
        'heat_title': '热力图——分布记录密度',
        'chart_label': '对比分析',
        'sp_registros_title': '各物种记录数（GBIF，2024）',
        'estado_title': '各州记录数',
        'bioma_title': '生物群系分布',
        'method_label': '应用生物多样性',
        'method_title': '研究问题与方法',
        'sci_q_title': '❓ 核心问题',
        'sci_q': '“巴西本土无刺蜂的分布与保护现状如何？合理的无刺蜂养殖（meliponicultura）以及独居蜂旅馆，又能如何帮助这些物种在城市和城市周边环境中得到保护？”',
        'pipeline_label': '数据流程',
        'steps': [['1',
                   '数据采集——GBIF + iNaturalist（2010–2024）',
                   '通过GBIF '
                   'API和iNaturalist导出数据，获取巴西Meliponini的分布记录。共@@TOTAL@@条带地理坐标的记录（2010–2024），已剔除存在地理空间问题的数据。目标物种：12种本土Meliponini和6种独居蜂。'],
                  ['2',
                   '技术考察——Cidade das Abelhas（圣保罗州，2022）',
                   '前往圣保罗的Cidade das Abelhas公园，直接观察Jataí、Mosquitinho、Manduri、Mirim '
                   'Preguiça等物种的合理化蜂箱，并拍摄记录、收集无刺蜂养殖场管理方面的资料。'],
                  ['3',
                   'FATEC Jundiaí毕业设计——独居蜂旅馆（2022）',
                   '毕业设计项目：为“广场上的科学”（Ciência na Praça）活动，在FATEC Jundiaí校园建造独居蜂旅馆。木质结构，钻有8和10 mm的孔，面向Xylocopa '
                   'sp.和Megachile sp.等本土独居蜂。'],
                  ['4',
                   '空间分析——生物群系分布',
                   '将分布记录与IBGE的生物群系矢量图（shapefile）叠加，识别各生物群系的物种丰富度格局。大西洋森林是Meliponini多样性最高的生物群系（约22个物种）。'],
                  ['5',
                   '生物学参数——科学文献',
                   '整理文献数据：蜂群规模、产卵率、工蜂寿命、觅食半径、蜂蜜产量。依据：A.B.E.L.H.A.、《无刺蜂养殖图谱》（Atlas da '
                   'Meliponicultura），以及USP/UNICAMP/UFMG的出版物。'],
                  ['6',
                   '威胁评估——IUCN红色名录',
                   '将分布数据与IUCN状态对照：@@VU@@个易危（VU）物种，@@LC@@个无危（LC）物种。分析各生物群系的种群趋势与人类活动压力。']],
        'biologia_title': '🐝 无刺蜂为何重要？',
        'biologia_text': '• 全球已描述的Meliponini<b>约550种</b> · 巴西<b>约350种</b><br>• '
                         '大西洋森林和塞拉多本土植物的<b>专属传粉者</b><br>• <b>具有药用价值的蜂蜜</b>，获ANVISA认可（第310/1997号法令）<br>• '
                         '<b>无刺蜂养殖</b>：使用INPA、IBAMA、JTB、Fernão Dias等蜂箱进行合理化饲养<br>• '
                         '<b>威胁：</b>毁林、农药、城市化、外来入侵物种',
        'solitarias_title': '🏨 独居蜂——沉默的大多数',
        'solitarias_text': '• <b>全球约70%的蜜蜂</b>是独居的——没有蜂王，没有蜂巢<br>• <b>每只雌蜂</b>独自筑巢、采集食物并照料卵<br>• '
                           '<b>蜂旅馆</b>（钻有6–10 mm孔洞的木块）可吸引Xylocopa、Megachile和Hylaeus<br>• <b>理想孔径：</b>8 '
                           'mm钻头（Megachile）、10 mm钻头（Xylocopa）——深度至少10 cm<br>• <b>安装方式：</b>朝向东或东南，高度1–2 '
                           'm，避免雨水直接淋到',
        'disc_label': '分析与发现',
        'disc_title': '数据揭示了什么',
        'discoveries': [['🐝',
                         'Jataí——最适应城市化的物种',
                         'Tetragonisca '
                         'angustula是对城市环境适应力最强的物种，在巴西所有州和全部5个生物群系中都有记录。它在砖石墙缝、电表箱和电线杆中筑巢。它在城市中的存在，是生态韧性的指示。'],
                        ['⚠️',
                         '@@VU@@个易危物种——@@VU_LIST@@',
                         '体型较大、蜂蜜产量较高的Melipona物种受威胁程度最高。毁林、人类活动压力以及繁殖率低（蜂王只进行1次婚飞），使这些物种特别容易发生种群崩溃。'],
                        ['🏨',
                         '蜂旅馆——城市生物多样性的放大器',
                         '在FATEC Jundiaí建造的蜂旅馆表明，钻有8和10 '
                         'mm孔的简易木质结构，在30–60天内就会被本土独居蜂入住。这是一项低成本（不到50雷亚尔）的举措，却对本地传粉有很大影响。'],
                        ['📊',
                         '圣保罗——巴西的无刺蜂养殖之都',
                         '@@SP_SENT@@ 残存的大西洋森林、密集的高校研究（USP、UNICAMP、UNESP）以及日益兴起的城市无刺蜂养殖，共同造就了这一领先地位。'],
                        ['🌎',
                         'GBIF：10年间@@GROWTH@@——公民科学是推动力',
                         '2014至2024年间，巴西Meliponini的地理坐标记录增加了@@GROWTH_ABS@@条（@@GROWTH@@），这与iNaturalist使用量的上升以及公众对生物多样性兴趣的提高同步。日益兴起的城市无刺蜂养殖既是这种兴趣的结果，也是其成因。'],
                        ['🌿',
                         '塞拉多——被低估、隐藏着巨大多样性的生物群系',
                         '尽管塞拉多拥有约100种Meliponini特有种，但它在生物多样性记录中一直存在采样不足的问题。这种采样不足反映出偏远地区研究上的空白——在该生物群系被彻底碎片化之前，这是一个保护警示。']],
        'conclusion_label': '结论',
        'conclusion_title': '每一个蜂巢都很重要',
        'conclusion_text': '巴西本土无刺蜂是独一无二的生物文化遗产：原住民对它们的养殖已有数千年，它们产出具有药用价值的蜂蜜，也是本土植物区系中不可替代的传粉者。GBIF中Meliponini记录@@GROWTH_N@@的增长表明，人们对无刺蜂养殖的兴趣正在上升——但毁林的速度仍然超过保护的步伐。每安装一个合理化蜂箱、每建一座蜂旅馆、每保护一片森林斑块，都是对这些物种未来投下的一张信任票。',
        'conclusion_author': 'Amauri Almeida · 环境管理毕业设计 · FATEC Jundiaí · 2022 · 参访圣保罗Cidade das Abelhas',
        'field_label': '实地与技术记录',
        'field_title': '从Cidade das Abelhas到FATEC校园',
        'field_inst_title': '📁 如何添加你的照片',
        'field_inst': '请将照片放入<code>assets/campo/</code>文件夹，并使用下方所示的准确文件名。',
        'photos': [{'emoji': '🐝',
                    'grupo': 'CIDADE DAS ABELHAS · 圣保罗 · 2022',
                    'titulo': '合理化蜂箱——Jataí蜂',
                    'esp': 'Tetragonisca angustula',
                    'desc': '位于圣保罗Cidade das Abelhas公园的Jataí蜂（Tetragonisca '
                            'angustula）合理化蜂箱（JTB或INPA型）。Jataí是巴西最常见、适应力最强的物种，天然在砖石墙缝中筑巢。合理化蜂箱便于分群，并且可以在不破坏巢穴的情况下进行管理。',
                    'path': 'assets/campo/01_colmeia_jatai_cidade_abelhas.jpg',
                    'legenda': 'Jataí蜂箱（Tetragonisca angustula）· Cidade das Abelhas · 圣保罗州 · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🔎',
                    'grupo': 'CIDADE DAS ABELHAS · 圣保罗 · 2022',
                    'titulo': '合理化蜂箱——Mosquitinho蜂',
                    'esp': 'Plebeia mosquito',
                    'desc': 'Mosquitinho蜂（Plebeia mosquito）的合理化蜂箱——巴西最小的无刺蜂之一（2 '
                            'mm）。性情极为温顺，对农药非常敏感。蜂箱的蜜层与育幼层分开，这是合理化无刺蜂养殖中避免伤害蜂群的基本做法。',
                    'path': 'assets/campo/02_colmeia_mosquitinho_cidade_abelhas.jpg',
                    'legenda': 'Mosquitinho蜂箱（Plebeia mosquito）· Cidade das Abelhas · 圣保罗州 · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🌿',
                    'grupo': 'CIDADE DAS ABELHAS · 圣保罗 · 2022',
                    'titulo': '合理化蜂箱——Manduri蜂（1）',
                    'esp': 'Melipona marginata',
                    'desc': 'Manduri蜂（Melipona marginata）的合理化蜂箱——易危物种（IUCN '
                            'VU）。它是保护意义最重要的物种之一：蜂蜜稀有、产量很少，只在本土树木的树洞中筑巢。合理化无刺蜂养殖是这一物种最主要的迁地保护策略。',
                    'path': 'assets/campo/04_colmeia_manduri_cidade_abelhas_1.jpg',
                    'legenda': 'Manduri蜂箱（Melipona marginata）· 易危 · Cidade das Abelhas · 圣保罗州 · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🌿',
                    'grupo': 'CIDADE DAS ABELHAS · 圣保罗 · 2022',
                    'titulo': '合理化蜂箱——Manduri蜂（2）',
                    'esp': 'Melipona marginata',
                    'desc': '记录的第二个Manduri蜂箱。持续观察同一物种的多个蜂箱，有助于研究行为和产量的差异。不同蜂箱在颜色和结构上的差别，反映了合理化蜂箱的不同型号——INPA、Fernão '
                            'Dias、JTB以及USP型号。',
                    'path': 'assets/campo/05_colmeia_manduri_cidade_abelhas_2.jpg',
                    'legenda': 'Manduri蜂箱（2）· Melipona marginata · VU · Cidade das Abelhas · 圣保罗州 · 2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · 圣保罗 · 2022',
                    'titulo': '合理化蜂箱——Mirim Preguiça蜂（1）',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'Mirim Preguiça蜂（Frieseomelitta '
                            'varia）的合理化蜂箱——因工蜂在巢门口悠闲平静的行为而得名。该物种对塞拉多和大西洋森林本土植物的传粉十分重要，在树枝上筑巢。',
                    'path': 'assets/campo/06_colmeia_mirim_preguica_1.jpg',
                    'legenda': 'Mirim Preguiça蜂箱（Frieseomelitta varia）· Cidade das Abelhas · 圣保罗州 · 2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · 圣保罗 · 2022',
                    'titulo': '合理化蜂箱——Mirim Preguiça蜂（2）',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'Mirim '
                            'Preguiça蜂箱的第二个视角，可以看到具有该物种特征的巢门。巢内结构的育幼室呈球形，与Melipona不同，因此合理化蜂箱需要针对该物种做专门调整。',
                    'path': 'assets/campo/07_colmeia_mirim_preguica_2.jpg',
                    'legenda': 'Mirim Preguiça蜂箱（2）· Frieseomelitta varia · Cidade das Abelhas · 圣保罗州 · 2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · 圣保罗 · 2022',
                    'titulo': '合理化蜂箱——Mirim Preguiça蜂（3）',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'Mirim Preguiça蜂箱的第三个角度，展示外部结构和支架的细节。在技术考察中从多个角度记录，对于找出最适合各物种的管理方式和蜂箱设计至关重要。',
                    'path': 'assets/campo/08_colmeia_mirim_preguica_3.jpg',
                    'legenda': 'Mirim Preguiça蜂箱（3）· Frieseomelitta varia · Cidade das Abelhas · 圣保罗州 · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🏛️',
                    'grupo': 'CIDADE DAS ABELHAS · 圣保罗 · 2022',
                    'titulo': '无刺蜂养殖场——不同物种的收藏',
                    'esp': '多个物种',
                    'desc': 'Cidade das '
                            'Abelhas公园无刺蜂养殖场一景，不同物种的合理化蜂箱并排摆放——这是无刺蜂养殖的良好做法。每个物种的蜂箱都有标识。蜂箱间距和巢门朝向经过精心计算，以尽量减少蜜蜂迷巢，并最大限度保障蜂群健康。',
                    'path': 'assets/campo/09_meliponario_colecao_cidade_abelhas.jpg',
                    'legenda': '多物种无刺蜂养殖场 · 合理化蜂箱 · Cidade das Abelhas公园 · 圣保罗州 · 2022',
                    'destaque': True,
                    'gid': 'cidade'},
                   {'emoji': '🌳',
                    'grupo': '蜂旅馆 · FATEC JUNDIAÍ · 2022',
                    'titulo': '旅馆建造——木质结构',
                    'esp': '面向独居蜂',
                    'desc': '开始在FATEC '
                            'Jundiaí校园建造独居蜂旅馆。木质结构是承载钻孔木块的主要支架。木材的选择（防腐处理的松木或桉木）很重要：既要耐潮，又不能用会驱离蜜蜂的杀生物剂处理。',
                    'path': 'assets/campo/10_hotel_abelhas_estrutura_madeira.jpg',
                    'legenda': '蜂旅馆建造 · 木质结构 · FATEC Jundiaí · 广场上的科学 · 2022',
                    'gid': 'hotel'},
                   {'emoji': '🔩',
                    'grupo': '蜂旅馆 · FATEC JUNDIAÍ · 2022',
                    'titulo': '给木块钻孔——8和10 mm钻头',
                    'esp': '面向独居蜂',
                    'desc': '用电钻在木块上钻孔，使用8 mm钻头（Megachile sp.、Hylaeus sp.）和10 mm钻头（Xylocopa sp.）。孔深至少10 '
                            'cm，雌蜂才能筑成含3–5个育幼室的巢。孔必须是盲孔——不能打穿木块。',
                    'path': 'assets/campo/11_hotel_abelhas_furadeira_broca8_10.jpg',
                    'legenda': '8和10 mm钻孔 · 独居蜂旅馆 · FATEC Jundiaí · 2022',
                    'gid': 'hotel'},
                   {'emoji': '🔩',
                    'grupo': '蜂旅馆 · FATEC JUNDIAÍ · 2022',
                    'titulo': '钻孔细节——8和10 mm钻头',
                    'esp': '面向独居蜂',
                    'desc': '8和10 mm钻头钻孔过程的细节。孔的一致性对蜂旅馆能否成功很重要：深度至少10 cm，直径精确，内壁光滑（必要时打磨）。内壁有毛刺的孔可能会妨碍蜜蜂进出。',
                    'path': 'assets/campo/12_hotel_abelhas_furos_detalhe.jpg',
                    'legenda': '8/10 mm钻孔细节 · 独居蜂旅馆 · FATEC Jundiaí · 2022',
                    'gid': 'hotel'},
                   {'emoji': '✅',
                    'grupo': '蜂旅馆 · FATEC JUNDIAÍ · 2022',
                    'titulo': '蜂旅馆落成——FATEC Jundiaí校园',
                    'esp': '面向独居蜂',
                    'desc': '独居蜂旅馆建成，安装在FATEC Jundiaí校园，用于“广场上的科学”（Ciência na Praça）活动。木块钻有8和10 '
                            'mm的孔，朝向东或东南，高度约1.5 m，顶部设有防雨罩。这是一座低成本（不到50雷亚尔）的设施，对本地传粉有很大影响。',
                    'path': 'assets/campo/13_hotel_abelhas_concluido_fatec_jundiai.jpg',
                    'legenda': '独居蜂旅馆落成 · FATEC Jundiaí校园 · 广场上的科学 · 2022',
                    'destaque_final': True,
                    'gid': 'hotel'}],
        'timeline_label': '项目时间线',
        'timeline_items': [['2022 · Jan–Jun', '环境管理毕业设计——FATEC Jundiaí', '研究无刺蜂养殖与独居蜂 · 为“广场上的科学”建造蜂旅馆'],
                           ['2022 · Jul',
                            '技术考察——圣保罗Cidade das Abelhas',
                            '拍摄记录合理化蜂箱中的8+个物种 · Jataí、Mosquitinho、Manduri、Mirim Preguiça等'],
                           ['2022 · Nov', '毕业设计答辩——FATEC Jundiaí', '环境管理毕业设计通过 · 获得学位'],
                           ['2023–2024', 'GBIF分析——@@TOTAL@@条记录', '将分布数据与生物群系和各州叠加 · 识别保护空白'],
                           ['2025', '发布至作品集', '巴西Meliponini观测站——数据持续更新的公开仪表板']],
        'trend_sel': '选择可视化方式',
        'trend_opt1': 'GBIF增长（2010–2024）',
        'trend_opt2': '各物种记录数（排名）',
        'trend_opt3': '各州记录数',
        'param_sel': '选择分析物种',
        'param_names': {'colonia': '蜂群规模（工蜂）',
                        'postura_dia': '产卵率（卵/天）',
                        'vida_operaria': '工蜂寿命（天）',
                        'longe_formag': '觅食半径（m）',
                        'prod_mel_kg': '蜂蜜产量（kg/年）',
                        'raio_dna_km': '遗传距离（km）'},
        'raw_label': '物种目录',
        'raw_title': '完整表格——巴西Meliponini',
        'download_csv': '⬇️ 下载CSV',
        'sources_label': '科学来源',
        'sources_title': '来源与数据库',
        'tech_label': '使用的技术',
        'footer_title': '🐝 Amauri Almeida',
        'footer_desc': '环境管理技术员 · FATEC Jundiaí（ENADE第3名）<br>人工智能、机器学习与数据科学研究生 · 数据科学与大数据<br>系统分析与开发 · '
                       'FACINT Maringá',
        'footer_links': '📍 Fernandópolis · SP · 巴西',
        'trend_label': '时间演变与排名',
        'param_label': '比较生物学',
        'param_title': '各物种的生物学参数',
        'param_detail': '生物学参数',
        'param_cmp': '物种对比',
        'records_axis': '记录数',
        'records_hover': '条记录',
        'gal_meli': '物种图库——MELIPONINI',
        'gal_sol': '图库——独居蜂',
        'honey': '蜂蜜',
        'mel_vals': {'Sim': '有', 'Não': '无', 'Pouco': '少量'},
        'gbif_records': 'GBIF记录',
        'pop_records': '记录数',
        'pop_species': '物种',
        'pop_status': '状态',
        'status_vals': {'Alta': '高', 'Média': '中', 'Baixa': '低'},
        'radar_title': '物种对比概况（0–10分）',
        'radar_cats': ['蜂蜜产量', '城市适应力', '飞行半径', '蜂群规模', 'IUCN（反向）'],
        'grp_city': '🏛️ CIDADE DAS ABELHAS · 圣保罗 · 2022',
        'grp_hotel': '🏨 独居蜂旅馆 · FATEC JUNDIAÍ · 广场上的科学 · 2022',
        'dest_melipon': '⭐ 亮点——完整的无刺蜂养殖场 · CIDADE DAS ABELHAS',
        'dest_hotel': '✅ 压轴亮点——蜂旅馆落成 · FATEC JUNDIAÍ校园',
        'hotel_build_title': '🏗️ 如何建造独居蜂旅馆',
        'hotel_build': [['材料', '木块（防腐处理的松木或桉木）· 至少15×10×10 cm'],
                        ['孔洞', '8 mm钻头（Megachile、Hylaeus）· 10 mm钻头（Xylocopa）'],
                        ['深度', '至少10 cm · 盲孔（不要打穿木块！）'],
                        ['朝向', '东或东南 · 可照到晨光'],
                        ['高度', '距地面1–2米 · 避雨避风'],
                        ['结果', '30–60天内即有本土蜜蜂入住']],
        'solitary_tbl': '独居蜂',
        'card_lbls': {'biome': '生物群系',
                      'region': '地区',
                      'colony': '蜂群',
                      'workers': '只工蜂',
                      'laying': '产卵',
                      'eggs_day': '卵/天',
                      'worker_life': '工蜂寿命',
                      'days': '天',
                      'forage': '觅食半径',
                      'honey': '蜂蜜产量',
                      'kg_year': 'kg/年',
                      'gen_dist': '遗传距离'},
        'carto_fallback': '正在使用备用底图（OpenStreetMap）。',
        'occ_live': 'GBIF（api.gbif.org）的真实数据点：巴西境内{n}条带地理坐标的分布记录，每个物种最多{k}条，查询日期{d}。点击某个点可打开原始记录。',
        'occ_demo': 'GBIF暂时无法访问：所示数据点仅为示意（首府城市×物种），并非实地记录。',
        'occ_none': 'GBIF暂时无法访问，且没有备用数据：不显示分布记录地图。',
        'dados_live': '数据根据GBIF（api.gbif.org）计算，查询日期{d}；每24小时自动更新。',
        'dados_snapshot': 'GBIF目前无法访问：数据来自最近一次保存的快照（{d}）。',
        'dados_static': 'GBIF目前无法访问：数据为早期汇编的参考值，未更新。',
        'serie_total': '总计（Meliponini + 5个独居蜂属）',
        'serie_inat': 'iNaturalist（Meliponini）',
        'raio_sel': '显示觅食半径（圆圈单位为米）',
        'raio_note': '每个圆圈表示该物种围绕真实分布记录（每个物种最多{n}条）的平均飞行半径。放大地图可查看比例。',
        'raio_layer': '觅食半径',
        'footer_portfolio': '作品集',
        'sources': [['GBIF',
                     'GBIF——全球生物多样性信息设施',
                     'gbif.org · '
                     '分布记录数据库，包含巴西Meliponini的@@TOTAL@@条带地理坐标的记录（2010–2024）。数据来自博物馆、植物标本馆、iNaturalist和研究人员。',
                     '#C47D0E'],
                    ['A.B.E.L.H.A.',
                     'A.B.E.L.H.A.——巴西蜜蜂研究协会',
                     'abelha.org.br · 《巴西无刺蜂养殖图谱》。觅食半径、生物学与保护方面的参考资料。',
                     '#C0390A'],
                    ['INATURALIST',
                     'iNaturalist——全球公民科学',
                     'inaturalist.org · '
                     '@@INAT@@条带地理坐标的巴西Meliponini记录（GBIF上的iNaturalist研究级数据集）。GBIF数据增长的主要推动力。',
                     '#2D7A45'],
                    ['FATEC',
                     'FATEC Jundiaí——环境管理毕业设计（2022）',
                     '为“广场上的科学”活动在校园内建造的独居蜂旅馆。8和10 mm钻头。以优异成绩通过。',
                     '#1B3A1E'],
                    ['CIDADE ABELHAS',
                     'Cidade das Abelhas公园——圣保罗（2022）',
                     '2022年技术考察。拍摄记录Jataí、Mosquitinho、Manduri、Mirim Preguiça等物种的合理化蜂箱。',
                     '#5C3D1E'],
                    ['IUCN', 'IUCN红色名录——受威胁物种', '@@VU_TAGS@@。巴西Meliponini的保护状态。', '#8B2515'],
                    ['INPA', 'INPA——国家亚马孙研究所', '适用于亚马孙Meliponini的INPA合理化蜂箱型号。巴西北部的物种数据。', '#0D4E72'],
                    ['EMBRAPA',
                     'EMBRAPA Cerrados / EMBRAPA Amazônia Oriental',
                     '巴西各生物群系的无刺蜂养殖数据。塞拉多和亚马孙物种的技术参考。',
                     '#C47D0E']],
        'species_text': {'Jataí': {'descricao': '巴西最广为人知的无刺蜂。产出品质极高、具有药用价值的蜂蜜。在树洞和砖石墙缝中筑巢，并用蜂胶将巢门封成管状或小片状。',
                                   'bioma': '所有',
                                   'regiao': '全国'},
                         'Mosquitinho': {'descricao': '巴西最小的无刺蜂之一。性情极为温顺。蜂蜜味道鲜美，但产量很少。对农药非常敏感，是环境质量的指示物种。',
                                         'bioma': '大西洋森林',
                                         'regiao': '南部/东南部'},
                         'Manduri': {'descricao': '濒危物种（VU）。蜂蜜稀有，产量很少。巢通常位于本土树木的树洞中。是以保护为目的的无刺蜂养殖项目的目标物种。',
                                     'bioma': '大西洋森林',
                                     'regiao': '南部/东南部'},
                         'Mirim Preguiça': {'descricao': '因行为悠闲平静，也被称为“懒蜂”（Abelha '
                                                         'Preguiça）。主要在树枝上筑巢。是塞拉多和大西洋森林本土植物的重要传粉者。',
                                            'bioma': '塞拉多/大西洋森林',
                                            'regiao': '中部/东南部'},
                         'Mandaçaia': {'descricao': '体型最大的无刺蜂之一。蜂蜜产量出众。因毁林和城市化而数量下降。瓜拉尼原住民数百年来将其作为“mborí”饲养。',
                                       'bioma': '大西洋森林',
                                       'regiao': '东南部/南部'},
                         'Uruçu Nordestina': {'descricao': '图皮南巴人的神圣之蜂，已被养殖2,000多年。蜂蜜具有公认的药用价值。是东北部无刺蜂养殖的象征，也是原住民养蜂的旗舰物种。',
                                              'bioma': '卡廷加/东北部大西洋森林',
                                              'regiao': '东北部'},
                         'Irapuá': {'descricao': '虽然不产商业量的蜂蜜，却是极其重要的传粉者。用植物树脂建造外露的巢。因防御行为，有时会被误认为欧洲蜜蜂。',
                                    'bioma': '所有',
                                    'regiao': '全国'},
                         'Tiúba': {'descricao': '在马拉尼昂被称为“大地之蜂”（Abelha da '
                                                'Terra）。蜂蜜风味独特，深受喜爱。是亚马孙和马拉尼昂无刺蜂养殖文化的重要组成部分。因毁林而面临风险。',
                                   'bioma': '亚马孙/东北部',
                                   'regiao': '北部/东北部'},
                         'Guaraipo': {'descricao': '体色模式多变的物种。蜂蜜味道柔和。在地下或树干中筑巢。因塞拉多农牧业的扩张而数量明显下降。',
                                      'bioma': '塞拉多/大西洋森林',
                                      'regiao': '中西部/东南部'},
                         'Iraí': {'descricao': '在城市环境中十分常见的蜜蜂。在墙缝、电表箱和瓦片中筑巢。对城市化的耐受性很强。是森林斑块连通性的优良指示物种。',
                                  'bioma': '塞拉多/大西洋森林',
                                  'regiao': '东南部'},
                         'Tubuna': {'descricao': '产出色深味浓的蜂蜜。在树洞中筑巢。对毁林非常敏感。在森林斑块修复项目中被用作关键传粉者。',
                                    'bioma': '大西洋森林',
                                    'regiao': '东南部/南部'},
                         'Mirim Guaçu': {'descricao': '耐寒的物种。在圣卡塔琳娜州和南里奥格兰德州非常常见。为南部地区的本土植物和栽培作物传粉。蜂蜜带有特有的酸味。',
                                         'bioma': '南部/东南部',
                                         'regiao': '南部/东南部'},
                         'Abelha Mamangava': {'descricao': '百香果的专属传粉者。没有它，巴西的百香果产量将会崩溃。它采用“振动授粉”（buzz '
                                                           'pollination）的技术，通过振动花朵来释放花粉。在枯枝中筑巢。',
                                              'habitat': '在枯木中筑巢',
                                              'polinizacao': '振动授粉——振动以释放花粉'},
                         'Abelha Carpinteira': {'descricao': 'Xylocopa属在巴西有50多个物种。因善于在木头上凿洞筑巢而得名“木匠蜂”。是管状花的重要传粉者。会在用竹管制成的蜂旅馆中筑巢。',
                                                'habitat': '干木、竹子',
                                                'polinizacao': '广谱传粉——访花种类繁多'},
                         'Abelha Mascarada': {'descricao': '体型微小却不可或缺。用嗉囊而不是花粉篮运送花粉，在体内携带花蜜和花粉。对用纸管和直径5–6 '
                                                           'mm竹管制成的蜂旅馆反应非常好。',
                                              'habitat': '管子、中空的树枝',
                                              'polinizacao': '小而开放的花'},
                         'Abelha Cortadeira': {'descricao': '切割叶片来筑巢——名称由此而来。常被视为“害虫”，其实是重要的本土传粉者。在木头孔洞中筑巢（蜂旅馆的理想钻头为8–10 '
                                                            'mm）。',
                                               'habitat': '土壤、木头、被切下的叶片',
                                               'polinizacao': '本土物种——塞拉多、大西洋森林'},
                         'Abelha Nômade': {'descricao': '盗寄生蜂，把卵产在其他独居蜂的巢中。外形像胡蜂，但其实是蜜蜂。对调节种群数量、维持森林环境的生态平衡至关重要。',
                                           'habitat': '寄生于其他蜂的巢',
                                           'polinizacao': '间接——维持生态平衡'},
                         'Abelha Oleiro': {'descricao': '是murici、barbatimão等金虎尾科（Malpighiaceae）植物的专性传粉者。从花中采集花油来喂养幼虫。在土壤中筑巢。是塞拉多保存完好的指示物种。',
                                           'habitat': '沙质土壤、陡壁',
                                           'polinizacao': '在油花上振动采集——金虎尾科'}},
        'back_link': '← 作品集',
        'lang_label': '语言',
        'cluster_name': '分布记录',
        'footer_copy': '© 2022–2026 · Meliponini观测站 · 巴西',
        'raw_cols': {'especie': '物种',
                     'cientifico': '学名',
                     'tamanho': '体型',
                     'raio': '觅食半径（m）',
                     'mel': '蜂蜜产量',
                     'iucn': 'IUCN',
                     'bioma': '生物群系',
                     'registros': 'GBIF记录',
                     'colonia': '蜂群（工蜂）',
                     'mel_ano': '蜂蜜/年（kg）',
                     'habitat': '栖息地',
                     'polinizacao': '传粉',
                     'tipo': '类型'},
        'tipo_vals': {'meli': 'Meliponini', 'sol': '独居蜂'},
        'tok_nd': '数千',
        'tok_and': '和',
        'tok_sp_top': 'SP共有{n}条GBIF记录——居各州之首。',
        'tok_sp_plain': 'SP共有{n}条GBIF记录。',
        'tok_sp_generic': 'SP是采样最充分的州之一。'},
 'ar': {'page_title': 'مرصد Meliponini · البرازيل',
        'hero_tag': 'التنوع الحيوي · MELIPONINI · البرازيل · 2022–2025',
        'hero_title': 'مرصد النحل\nعديم اللسع',
        'hero_subtitle': 'رصد وتحليل توزيع النحل عديم اللسع المحلي (Meliponini) والنحل المنفرد في البرازيل — '
                         'أكثر من 24.000 سجل في GBIF، و12 نوعًا مرسومًا على الخريطة، وحماية فاعلة. يشمل '
                         'زيارة ميدانية تقنية إلى Cidade das Abelhas (ساو باولو، 2022) وفندقًا للنحل المنفرد '
                         'أُنشئ في FATEC Jundiaí.',
        'badge1': '🐝 12 نوعًا قيد الرصد',
        'badge2': '🗺️ أكثر من 300 نقطة رصد',
        'badge3': 'البرازيل · 5 بيئات حيوية',
        'badge4': 'GBIF · iNaturalist · INPA',
        'badge5': 'مشروع التخرج FATEC Jundiaí 2022',
        'm1': 'أنواع Meliponini',
        'm2': 'سجلات GBIF (2024)',
        'm3': 'الولايات المشمولة',
        'm4': 'الأنواع المهددة',
        'tab1': '🗺️ الخريطة والتحليل',
        'tab2': '🔬 المنهجية والمسار',
        'tab3': '💡 ما اكتشفناه',
        'tab4': '📷 في الميدان',
        'tab5': '📈 الاتجاهات',
        'tab6': '⚙️ المعاملات',
        'tab7': '📋 البيانات الخام',
        'tab8': '📚 المصادر والشكر',
        'map_label': 'التوزيع في البرازيل',
        'map_title': 'خريطة الرصد — النحل عديم اللسع',
        'map_hint': '🐝 <strong>انقر على العلامات</strong> لمعرفة النوع والبيئة الحيوية والمصدر. الحجم يتناسب '
                    'مع عدد السجلات في كل ولاية. فعّل التجمعات لعرض المجموعات.',
        'heat_title': 'خريطة حرارية — كثافة الرصد',
        'chart_label': 'تحليل مقارن',
        'sp_registros_title': 'السجلات حسب النوع (GBIF، 2024)',
        'estado_title': 'السجلات حسب الولاية',
        'bioma_title': 'التوزيع حسب البيئة الحيوية',
        'method_label': 'التنوع الحيوي التطبيقي',
        'method_title': 'السؤال والمنهجية',
        'sci_q_title': '❓ السؤال المحوري',
        'sci_q': '"ما الوضع الحالي لتوزيع النحل عديم اللسع المحلي في البرازيل وحمايته، وكيف يمكن لممارسات '
                 'تربية النحل عديم اللسع الرشيدة وفنادق النحل المنفرد أن تسهم في الحفاظ على هذه الأنواع في '
                 'البيئات الحضرية وشبه الحضرية؟"',
        'pipeline_label': 'مسار البيانات',
        'steps': [['1',
                   'الجمع — GBIF + iNaturalist (2010–2024)',
                   'بيانات رصد Meliponini البرازيلية عبر واجهة GBIF البرمجية وبيانات iNaturalist المُصدَّرة. '
                   '@@TOTAL@@ سجل محدد الإحداثيات (2010–2024)، رُشّحت لاستبعاد المشكلات الجغرافية المكانية. '
                   'الأنواع المستهدفة: 12 نوعًا محليًا من Meliponini و6 أنواع من النحل المنفرد.'],
                  ['2',
                   'زيارة تقنية — Cidade das Abelhas (ساو باولو، 2022)',
                   'زيارة تقنية إلى متنزه Cidade das Abelhas في ساو باولو للمشاهدة المباشرة لخلايا رشيدة من '
                   'Jataí وMosquitinho وManduri وMirim Preguiça وأنواع أخرى. توثيق فوتوغرافي وجمع بيانات عن '
                   'الإدارة الرشيدة لمناحل النحل عديم اللسع.'],
                  ['3',
                   'مشروع التخرج FATEC Jundiaí — فندق للنحل المنفرد (2022)',
                   'مشروع نهاية الدراسة: بناء فندق للنحل المنفرد في حرم FATEC Jundiaí لفعالية «العلم في '
                   'الساحة». هيكل خشبي بثقوب بمثقاب 8 و10 mm للنحل المنفرد المحلي مثل Xylocopa sp. '
                   'وMegachile sp.'],
                  ['4',
                   'التحليل المكاني — التوزيع حسب البيئة الحيوية',
                   'مطابقة نقاط الرصد مع ملف الأشكال (shapefile) الخاص بالبيئات الحيوية من IBGE. تحديد أنماط '
                   'ثراء الأنواع في كل بيئة حيوية. الغابة الأطلسية هي البيئة الأعلى تنوعًا في Meliponini '
                   '(~22 نوعًا).'],
                  ['5',
                   'المعاملات البيولوجية — الأدبيات العلمية',
                   'تجميع بيانات من الأدبيات: حجم المستعمرة، ومعدل وضع البيض، وعمر الشغالة، ونصف قطر البحث '
                   'عن الغذاء، وإنتاج العسل. المرجع: A.B.E.L.H.A.، وأطلس تربية النحل عديم اللسع، ومنشورات '
                   'USP/UNICAMP/UFMG.'],
                  ['6',
                   'تقييم التهديد — IUCN Red List',
                   'مطابقة بيانات الرصد مع وضع IUCN: @@VU@@ نوعًا معرضًا للخطر (VU)، و@@LC@@ نوعًا من أقل '
                   'الأنواع إثارة للقلق (LC). تحليل اتجاهات المجموعات السكانية والضغوط البشرية في كل بيئة '
                   'حيوية.']],
        'biologia_title': '🐝 لماذا يهمّ النحل عديم اللسع؟',
        'biologia_text': '• <b>~550 نوعًا</b> من Meliponini موصوفة في العالم · <b>~350 في البرازيل</b><br>• '
                         '<b>ملقِّحات حصرية</b> لأنواع نباتية محلية في الغابة الأطلسية والسيرادو<br>• <b>عسل '
                         'ذو خصائص طبية</b> معترف بها من ANVISA (اللائحة 310/1997)<br>• <b>تربية النحل عديم '
                         'اللسع</b>: تربية رشيدة في صناديق INPA وIBAMA وJTB وFernão Dias<br>• '
                         '<b>التهديدات:</b> إزالة الغابات، والمبيدات الزراعية، والتحضر، والأنواع الغريبة '
                         'الغازية',
        'solitarias_title': '🏨 النحل المنفرد — الأغلبية الصامتة',
        'solitarias_text': '• <b>~70% من نحل العالم</b> منفرد — بلا ملكة ولا خلية<br>• <b>كل أنثى</b> تبني '
                           'عشها بنفسها وتجمع الغذاء وتعتني بالبيض<br>• <b>فنادق النحل</b> (كتل خشبية بثقوب '
                           '6–10 mm) تجذب Xylocopa وMegachile وHylaeus<br>• <b>الثقوب المثالية:</b> مثقاب 8 '
                           'mm (Megachile)، ومثقاب 10 mm (Xylocopa) — بعمق لا يقل عن 10 cm<br>• '
                           '<b>التركيب:</b> اتجاه الشرق/الجنوب الشرقي، وارتفاع 1–2 m، ومحمي من المطر المباشر',
        'disc_label': 'التحليل والاكتشافات',
        'disc_title': 'ما كشفته البيانات',
        'discoveries': [['🐝',
                         'Jataí — الأكثر تكيفًا مع التحضر',
                         'Tetragonisca angustula هو النوع الأقدر على التكيف مع البيئة الحضرية. سُجّل في جميع '
                         'الولايات البرازيلية وفي البيئات الحيوية الخمس. يعشش في شقوق البناء والصناديق '
                         'الكهربائية والأعمدة. ووجوده في المدن مؤشر على المرونة البيئية.'],
                        ['⚠️',
                         '@@VU@@ نوعًا معرضًا للخطر — @@VU_LIST@@',
                         'أنواع Melipona الأكبر حجمًا والأعلى إنتاجًا للعسل هي الأكثر تعرضًا للتهديد. ويجعل '
                         'اجتماع إزالة الغابات والضغط البشري وضعف التكاثر (إذ تقوم الملكة برحلة تزاوج واحدة '
                         'فقط) هذه الأنواع شديدة الهشاشة أمام الانهيار السكاني.'],
                        ['🏨',
                         'فندق النحل — مضاعِف للتنوع الحيوي الحضري',
                         'أثبت فندق النحل الذي أُنشئ في FATEC Jundiaí أن الهياكل الخشبية البسيطة ذات الثقوب '
                         'بمثقاب 8 و10 mm تشغلها الأنواع المنفردة المحلية خلال 30–60 يومًا. تدخل منخفض '
                         'التكلفة (أقل من 50 ريالًا) وذو أثر كبير في التلقيح المحلي.'],
                        ['📊',
                         'ساو باولو — عاصمة تربية النحل عديم اللسع في البرازيل',
                         '@@SP_SENT@@ ويفسّر هذا الدور الريادي اجتماعُ ما تبقى من الغابة الأطلسية، والبحث '
                         'الجامعي المكثف (USP وUNICAMP وUNESP)، وتنامي تربية النحل عديم اللسع في المدن.'],
                        ['🌎',
                         'GBIF: @@GROWTH@@ في 10 سنوات — العلم المواطِن محرّكًا',
                         'إن نمو سجلات Meliponini محددة الإحداثيات في البرازيل بمقدار @@GROWTH_ABS@@ بين '
                         '2014 و2024 (@@GROWTH@@) يواكب تزايد استخدام iNaturalist واهتمام المواطنين بالتنوع '
                         'الحيوي. وتنامي تربية النحل عديم اللسع في المدن نتيجة لهذا الاهتمام وسبب له في آن '
                         'واحد.'],
                        ['🌿',
                         'السيرادو — بيئة حيوية قليلة الرصد ذات تنوع خفي كبير',
                         'رغم أن السيرادو يضم نحو 100 نوع متوطن من Meliponini، فإنه قليل الرصد تاريخيًا في '
                         'سجلات التنوع الحيوي. ويعكس نقص الرصد فجوات بحثية في المناطق النائية — وهو إنذار '
                         'بضرورة الحماية قبل أن تتجزأ هذه البيئة بنسبة 100%.']],
        'conclusion_label': 'الخلاصة',
        'conclusion_title': 'كل خلية لها أهميتها',
        'conclusion_text': 'النحل عديم اللسع المحلي في البرازيل تراث حيوي ثقافي فريد: ربّته الشعوب الأصلية '
                           'آلاف السنين، وينتج عسلًا ذا خصائص طبية، وهو ملقِّح لا يمكن الاستعاضة عنه '
                           'لنباتاتنا المحلية. ونموّ @@GROWTH_N@@ في سجلات Meliponini على GBIF يُظهر أن '
                           'الاهتمام بتربية النحل عديم اللسع في ازدياد — لكن وتيرة إزالة الغابات ما زالت '
                           'تفوق سرعة الحماية. كل خلية رشيدة تُركَّب، وكل فندق نحل يُبنى، وكل جزء غابي يُحمى '
                           'هو تصويت بالثقة في مستقبل هذه الأنواع.',
        'conclusion_author': 'Amauri Almeida · مشروع التخرج في الإدارة البيئية · FATEC Jundiaí · 2022 · '
                             'زيارة Cidade das Abelhas SP',
        'field_label': 'السجل الميداني والتقني',
        'field_title': 'من Cidade das Abelhas إلى حرم FATEC',
        'field_inst_title': '📁 كيف تضيف صورك',
        'field_inst': 'ضع صورك في المجلد <code>assets/campo/</code> بالأسماء المطابقة تمامًا الواردة أدناه.',
        'photos': [{'emoji': '🐝',
                    'grupo': 'CIDADE DAS ABELHAS · ساو باولو · 2022',
                    'titulo': 'خلية رشيدة — نحلة Jataí',
                    'esp': 'Tetragonisca angustula',
                    'desc': 'خلية رشيدة (صندوق JTB أو INPA) لنحلة Jataí (Tetragonisca angustula) في متنزه '
                            'Cidade das Abelhas بساو باولو. Jataí هو النوع الأكثر شيوعًا وتكيفًا في البرازيل '
                            '— يعشش طبيعيًا في شقوق البناء. وتتيح الخلية الرشيدة تقسيم المستعمرات وإدارتها '
                            'دون تدمير العش.',
                    'path': 'assets/campo/01_colmeia_jatai_cidade_abelhas.jpg',
                    'legenda': 'خلية Jataí (Tetragonisca angustula) · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🔎',
                    'grupo': 'CIDADE DAS ABELHAS · ساو باولو · 2022',
                    'titulo': 'خلية رشيدة — نحلة Mosquitinho',
                    'esp': 'Plebeia mosquito',
                    'desc': 'خلية رشيدة لنحلة Mosquitinho (Plebeia mosquito) — من أصغر أنواع النحل عديم '
                            'اللسع في البرازيل (2 mm). شديدة الوداعة وحساسة جدًا للمبيدات الزراعية. خلية '
                            'بوحدة عسل منفصلة عن وحدة الحضنة — ممارسة أساسية في تربية النحل عديم اللسع '
                            'الرشيدة كي لا تتضرر المستعمرة.',
                    'path': 'assets/campo/02_colmeia_mosquitinho_cidade_abelhas.jpg',
                    'legenda': 'خلية Mosquitinho (Plebeia mosquito) · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🌿',
                    'grupo': 'CIDADE DAS ABELHAS · ساو باولو · 2022',
                    'titulo': 'خلية رشيدة — نحلة Manduri (1)',
                    'esp': 'Melipona marginata',
                    'desc': 'خلية رشيدة لنحلة Manduri (Melipona marginata) — نوع معرض للخطر (IUCN VU). من '
                            'أهم الأنواع للحماية: عسل نادر بكميات صغيرة، ويعشش حصرًا في تجاويف الأشجار '
                            'المحلية. وتُعدّ تربية النحل عديم اللسع الرشيدة الاستراتيجية الرئيسة للحماية '
                            'خارج الموطن (ex situ) لهذا النوع.',
                    'path': 'assets/campo/04_colmeia_manduri_cidade_abelhas_1.jpg',
                    'legenda': 'خلية Manduri (Melipona marginata) · معرض للخطر · Cidade das Abelhas · SP · '
                               '2022',
                    'gid': 'cidade'},
                   {'emoji': '🌿',
                    'grupo': 'CIDADE DAS ABELHAS · ساو باولو · 2022',
                    'titulo': 'خلية رشيدة — نحلة Manduri (2)',
                    'esp': 'Melipona marginata',
                    'desc': 'الخلية الثانية الموثقة من Manduri. إن متابعة عدة خلايا من النوع نفسه تتيح دراسة '
                            'التباين السلوكي والإنتاجي. ويعكس اختلاف اللون والبنية بين الصناديق نماذج مختلفة '
                            'من الخلايا الرشيدة — INPA وFernão Dias وJTB ونماذج USP.',
                    'path': 'assets/campo/05_colmeia_manduri_cidade_abelhas_2.jpg',
                    'legenda': 'خلية Manduri (2) · Melipona marginata · VU · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · ساو باولو · 2022',
                    'titulo': 'خلية رشيدة — Mirim Preguiça (1)',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'خلية رشيدة لنحلة Mirim Preguiça (Frieseomelitta varia) — سُمّيت بذلك لهدوء سلوك '
                            'الشغالات عند مدخل الخلية. نوع مهم لتلقيح الأنواع النباتية المحلية في السيرادو '
                            'والغابة الأطلسية. يبني أعشاشه على أغصان الأشجار.',
                    'path': 'assets/campo/06_colmeia_mirim_preguica_1.jpg',
                    'legenda': 'خلية Mirim Preguiça (Frieseomelitta varia) · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · ساو باولو · 2022',
                    'titulo': 'خلية رشيدة — Mirim Preguiça (2)',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'منظر ثانٍ لخلية Mirim Preguiça. يُلاحظ مدخل الخلية بخصائصه المميزة لهذا النوع. '
                            'والبنية الداخلية للعش، بخلايا حضنة كروية، تختلف عن Melipona — مما يستلزم '
                            'تعديلات خاصة في الصناديق الرشيدة لهذا النوع.',
                    'path': 'assets/campo/07_colmeia_mirim_preguica_2.jpg',
                    'legenda': 'خلية Mirim Preguiça (2) · Frieseomelitta varia · Cidade das Abelhas · SP · '
                               '2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · ساو باولو · 2022',
                    'titulo': 'خلية رشيدة — Mirim Preguiça (3)',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'زاوية ثالثة لخلية Mirim Preguiça تُظهر تفاصيل البنية الخارجية والحامل. والتوثيق '
                            'من زوايا متعددة ضروري في الزيارات التقنية لتحديد أنماط الإدارة وتصاميم الخلايا '
                            'الأنسب لكل نوع.',
                    'path': 'assets/campo/08_colmeia_mirim_preguica_3.jpg',
                    'legenda': 'خلية Mirim Preguiça (3) · Frieseomelitta varia · Cidade das Abelhas · SP · '
                               '2022',
                    'gid': 'cidade'},
                   {'emoji': '🏛️',
                    'grupo': 'CIDADE DAS ABELHAS · ساو باولو · 2022',
                    'titulo': 'منحل النحل عديم اللسع — مجموعة أنواع متنوعة',
                    'esp': 'أنواع متعددة',
                    'desc': 'منظر لمنحل متنزه Cidade das Abelhas بصناديق رشيدة لأنواع مختلفة جنبًا إلى جنب — '
                            'كما تقتضي الممارسة الجيدة في تربية النحل عديم اللسع. لكل نوع صندوقه المعرَّف. '
                            'وتُحسب المسافات بين الخلايا واتجاه المدخل لتقليل انجراف النحل وتعظيم صحة '
                            'المستعمرات.',
                    'path': 'assets/campo/09_meliponario_colecao_cidade_abelhas.jpg',
                    'legenda': 'منحل بأنواع متنوعة · صناديق رشيدة · متنزه Cidade das Abelhas · SP · 2022',
                    'destaque': True,
                    'gid': 'cidade'},
                   {'emoji': '🌳',
                    'grupo': 'فندق النحل · FATEC JUNDIAÍ · 2022',
                    'titulo': 'بناء الفندق — الهيكل الخشبي',
                    'esp': 'للنحل المنفرد',
                    'desc': 'بداية بناء فندق النحل المنفرد في حرم FATEC Jundiaí. الهيكل الخشبي هو الدعامة '
                            'الأساسية للكتل المثقوبة. واختيار الخشب (صنوبر معالج أو أوكالبتوس) مهم: يجب أن '
                            'يقاوم الرطوبة دون أن يُعالج بمبيدات حيوية تنفّر النحل.',
                    'path': 'assets/campo/10_hotel_abelhas_estrutura_madeira.jpg',
                    'legenda': 'بناء فندق النحل · الهيكل الخشبي · FATEC Jundiaí · «العلم في الساحة» · 2022',
                    'gid': 'hotel'},
                   {'emoji': '🔩',
                    'grupo': 'فندق النحل · FATEC JUNDIAÍ · 2022',
                    'titulo': 'ثقب الكتل — مثقاب 8 و10 mm',
                    'esp': 'للنحل المنفرد',
                    'desc': 'ثقب الكتل الخشبية بالمثقاب الكهربائي باستخدام رأس 8 mm (Megachile sp. وHylaeus '
                            'sp.) ورأس 10 mm (Xylocopa sp.). عمق لا يقل عن 10 cm ضروري كي تُكمل الأنثى عشها '
                            'بـ3–5 خلايا حضنة. ويجب أن تنتهي الثقوب بقاع مسدود — فلا تنفذ عبر الكتلة.',
                    'path': 'assets/campo/11_hotel_abelhas_furadeira_broca8_10.jpg',
                    'legenda': 'الثقب بمثقاب 8 و10 mm · فندق النحل المنفرد · FATEC Jundiaí · 2022',
                    'gid': 'hotel'},
                   {'emoji': '🔩',
                    'grupo': 'فندق النحل · FATEC JUNDIAÍ · 2022',
                    'titulo': 'تفصيل الثقوب — مثقاب 8 و10 mm',
                    'esp': 'للنحل المنفرد',
                    'desc': 'تفصيل لعملية الثقب بمثقاب 8 و10 mm. انتظام الثقوب مهم لنجاح الفندق: عمق لا يقل '
                            'عن 10 cm، وقطر دقيق، وسطح داخلي أملس (يُصنفر عند الحاجة). فالثقوب ذات الحواف '
                            'الداخلية المسننة قد تمنع مرور النحل.',
                    'path': 'assets/campo/12_hotel_abelhas_furos_detalhe.jpg',
                    'legenda': 'تفصيل ثقوب 8/10 mm · فندق النحل المنفرد · FATEC Jundiaí · 2022',
                    'gid': 'hotel'},
                   {'emoji': '✅',
                    'grupo': 'فندق النحل · FATEC JUNDIAÍ · 2022',
                    'titulo': 'اكتمال فندق النحل — حرم FATEC Jundiaí',
                    'esp': 'للنحل المنفرد',
                    'desc': 'اكتمل فندق النحل المنفرد وتم تركيبه في حرم FATEC Jundiaí لفعالية «العلم في '
                            'الساحة». كتل خشبية بثقوب بمثقاب 8 و10 mm، باتجاه الشرق/الجنوب الشرقي، وبارتفاع '
                            '~1,5 m، ومحمية بغطاء من المطر. هيكل منخفض التكلفة (أقل من 50 ريالًا) وذو أثر '
                            'كبير في التلقيح المحلي.',
                    'path': 'assets/campo/13_hotel_abelhas_concluido_fatec_jundiai.jpg',
                    'legenda': 'فندق النحل المنفرد مكتملًا · حرم FATEC Jundiaí · «العلم في الساحة» · 2022',
                    'destaque_final': True,
                    'gid': 'hotel'}],
        'timeline_label': 'الجدول الزمني للمشروع',
        'timeline_items': [['2022 · Jan–Jun',
                            'مشروع التخرج في الإدارة البيئية — FATEC Jundiaí',
                            'بحث حول تربية النحل عديم اللسع والنحل المنفرد · بناء فندق النحل لفعالية «العلم '
                            'في الساحة»'],
                           ['2022 · Jul',
                            'زيارة تقنية — Cidade das Abelhas SP',
                            'توثيق فوتوغرافي لأكثر من 8 أنواع في خلايا رشيدة · Jataí وMosquitinho وManduri '
                            'وMirim Preguiça وغيرها'],
                           ['2022 · Nov',
                            'مناقشة المشروع — FATEC Jundiaí',
                            'إجازة مشروع التخرج في الإدارة البيئية · نيل الدرجة'],
                           ['2023–2024',
                            'تحليل GBIF — @@TOTAL@@ سجل',
                            'مطابقة بيانات الرصد مع البيئات الحيوية والولايات · تحديد فجوات الحماية'],
                           ['2025',
                            'النشر في المحفظة',
                            'مرصد Meliponini في البرازيل — لوحة بيانات عامة ببيانات محدّثة']],
        'trend_sel': 'اختر طريقة العرض',
        'trend_opt1': 'نمو GBIF (2010–2024)',
        'trend_opt2': 'السجلات حسب النوع (الترتيب)',
        'trend_opt3': 'السجلات حسب الولاية',
        'param_sel': 'النوع المراد تحليله',
        'param_names': {'colonia': 'حجم المستعمرة (الشغالات)',
                        'postura_dia': 'معدل وضع البيض (بيضة/يوم)',
                        'vida_operaria': 'عمر الشغالة (أيام)',
                        'longe_formag': 'نصف قطر البحث عن الغذاء (m)',
                        'prod_mel_kg': 'إنتاج العسل (kg/سنة)',
                        'raio_dna_km': 'المسافة الوراثية (km)'},
        'raw_label': 'فهرس الأنواع',
        'raw_title': 'الجدول الكامل — Meliponini في البرازيل',
        'download_csv': '⬇️ تنزيل CSV',
        'sources_label': 'المصادر العلمية',
        'sources_title': 'المصادر وقواعد البيانات',
        'tech_label': 'التقنيات المستخدمة',
        'footer_title': '🐝 Amauri Almeida',
        'footer_desc': 'تقني في الإدارة البيئية · FATEC Jundiaí (المرتبة الثالثة في ENADE)<br>دراسات عليا في '
                       'الذكاء الاصطناعي وتعلّم الآلة وعلم البيانات · علم البيانات والبيانات الضخمة<br>تحليل '
                       'النظم وتطويرها · FACINT Maringá',
        'footer_links': '📍 Fernandópolis · SP · البرازيل',
        'trend_label': 'التطور الزمني والتصنيفات',
        'param_label': 'علم الأحياء المقارن',
        'param_title': 'المعاملات البيولوجية للأنواع',
        'param_detail': 'المعامل البيولوجي',
        'param_cmp': 'مقارنة بين الأنواع',
        'records_axis': 'السجلات',
        'records_hover': 'سجل',
        'gal_meli': 'معرض الأنواع — MELIPONINI',
        'gal_sol': 'معرض — النحل المنفرد',
        'honey': 'العسل',
        'mel_vals': {'Sim': 'نعم', 'Não': 'لا', 'Pouco': 'قليل'},
        'gbif_records': 'سجلات GBIF',
        'pop_records': 'السجلات',
        'pop_species': 'النوع',
        'pop_status': 'الحالة',
        'status_vals': {'Alta': 'عالية', 'Média': 'متوسطة', 'Baixa': 'منخفضة'},
        'radar_title': 'الملف المقارن للأنواع (مقياس 0–10)',
        'radar_cats': ['إنتاج العسل', 'التكيف الحضري', 'مدى الطيران', 'حجم المستعمرة', 'IUCN (معكوس)'],
        'grp_city': '🏛️ CIDADE DAS ABELHAS (مدينة النحل) · ساو باولو · 2022',
        'grp_hotel': '🏨 فندق النحل المنفرد · FATEC JUNDIAÍ · «العلم في الساحة» · 2022',
        'dest_melipon': '⭐ أبرز ما في المعرض — منحل متكامل · CIDADE DAS ABELHAS',
        'dest_hotel': '✅ الخاتمة البارزة — الفندق مكتملًا · حرم FATEC JUNDIAÍ',
        'hotel_build_title': '🏗️ كيف تبني فندقًا للنحل المنفرد',
        'hotel_build': [['المادة', 'كتلة خشبية (صنوبر معالج أو أوكالبتوس) · 15×10×10 cm كحد أدنى'],
                        ['الثقوب', 'مثقاب 8 mm (Megachile وHylaeus) · مثقاب 10 mm (Xylocopa)'],
                        ['العمق', '10 cm كحد أدنى · قاع مسدود (لا تثقب الكتلة من طرف إلى طرف!)'],
                        ['الاتجاه', 'الشرق أو الجنوب الشرقي · يتلقى شمس الصباح'],
                        ['الارتفاع', '1–2 m عن الأرض · محمي من المطر والرياح'],
                        ['النتيجة', 'تشغله النحلات المحلية خلال 30–60 يومًا']],
        'solitary_tbl': 'النحل المنفرد',
        'card_lbls': {'biome': 'البيئة الحيوية',
                      'region': 'المنطقة',
                      'colony': 'المستعمرة',
                      'workers': 'شغالة',
                      'laying': 'وضع البيض',
                      'eggs_day': 'بيضة/يوم',
                      'worker_life': 'عمر الشغالة',
                      'days': 'يومًا',
                      'forage': 'نصف قطر الغذاء',
                      'honey': 'إنتاج العسل',
                      'kg_year': 'kg/سنة',
                      'gen_dist': 'المسافة الوراثية'},
        'carto_fallback': 'يجري استخدام خريطة أساس بديلة (OpenStreetMap).',
        'occ_live': 'نقاط حقيقية من GBIF (api.gbif.org): {n} رصدًا محدد الإحداثيات في البرازيل، بحد أقصى {k} '
                    'لكل نوع، جرى الاستعلام عنها في {d}. انقر على نقطة لفتح السجل الأصلي.',
        'occ_demo': 'GBIF غير متاح حاليًا: النقاط المعروضة توضيحية (عواصم × أنواع) وليست سجلات ميدانية.',
        'occ_none': 'GBIF غير متاح حاليًا ولا توجد بيانات احتياطية: خريطة الرصد غير معروضة.',
        'dados_live': 'أرقام محسوبة من GBIF (api.gbif.org)، جرى الاستعلام عنها في {d}؛ وتُحدَّث تلقائيًا كل '
                      '24 ساعة.',
        'dados_snapshot': 'GBIF غير متاح الآن: الأرقام من آخر لقطة محفوظة ({d}).',
        'dados_static': 'GBIF غير متاح الآن: قيم مرجعية من تجميع سابق، غير محدّثة.',
        'serie_total': 'الإجمالي (Meliponini + 5 أجناس منفردة)',
        'serie_inat': 'iNaturalist (Meliponini)',
        'raio_sel': 'إظهار نصف قطر البحث عن الغذاء (دوائر بالأمتار)',
        'raio_note': 'تُظهر كل دائرة متوسط نصف قطر طيران النوع حول نقاط رصد حقيقية (حتى {n} لكل نوع). قرّب '
                     'الخريطة لترى المقياس.',
        'raio_layer': 'نصف قطر البحث عن الغذاء',
        'footer_portfolio': 'المحفظة',
        'sources': [['GBIF',
                     'GBIF — مرفق معلومات التنوع الحيوي العالمي',
                     'gbif.org · قاعدة بيانات رصد تضم @@TOTAL@@ سجل محدد الإحداثيات لـ Meliponini في '
                     'البرازيل (2010–2024). بيانات من المتاحف والمعاشب وiNaturalist والباحثين.',
                     '#C47D0E'],
                    ['A.B.E.L.H.A.',
                     'A.B.E.L.H.A. — الجمعية البرازيلية لدراسة النحل',
                     'abelha.org.br · أطلس تربية النحل عديم اللسع في البرازيل. مرجع لأنصاف أقطار البحث عن '
                     'الغذاء وعلم الأحياء والحماية.',
                     '#C0390A'],
                    ['INATURALIST',
                     'iNaturalist — العلم المواطِن العالمي',
                     'inaturalist.org · @@INAT@@ سجل لـ Meliponini البرازيلية محددة الإحداثيات (مجموعة '
                     'بيانات iNaturalist Research-grade على GBIF). المحرك الرئيس لنمو GBIF.',
                     '#2D7A45'],
                    ['FATEC',
                     'FATEC Jundiaí — مشروع التخرج في الإدارة البيئية (2022)',
                     'فندق للنحل المنفرد بُني في الحرم الجامعي لفعالية «العلم في الساحة». مثقاب 8 و10 mm. '
                     'نال تقدير الامتياز.',
                     '#1B3A1E'],
                    ['CIDADE ABELHAS',
                     'متنزه Cidade das Abelhas — ساو باولو (2022)',
                     'زيارة تقنية في 2022. توثيق فوتوغرافي لخلايا رشيدة من Jataí وMosquitinho وManduri '
                     'وMirim Preguiça وغيرها.',
                     '#5C3D1E'],
                    ['IUCN',
                     'IUCN Red List — القائمة الحمراء للأنواع المهددة',
                     '@@VU_TAGS@@. حالة حماية Meliponini البرازيلية.',
                     '#8B2515'],
                    ['INPA',
                     'INPA — المعهد الوطني لأبحاث الأمازون',
                     'نموذج الخلية الرشيدة INPA لـ Meliponini الأمازونية. بيانات أنواع شمال البرازيل.',
                     '#0D4E72'],
                    ['EMBRAPA',
                     'EMBRAPA Cerrados / EMBRAPA Amazônia Oriental',
                     'بيانات تربية النحل عديم اللسع في البيئات الحيوية البرازيلية. مرجع تقني لأنواع السيرادو '
                     'والأمازون.',
                     '#C47D0E']],
        'species_text': {'Jataí': {'descricao': 'أشهر نحل عديم اللسع في البرازيل. ينتج عسلًا فائق الجودة ذا '
                                                'خصائص طبية. أعشاشه في تجاويف الأشجار وشقوق البناء. يسدّ '
                                                'المدخل بالبروبوليس على شكل أنبوب أو أقراص.',
                                   'bioma': 'الجميع',
                                   'regiao': 'وطني'},
                         'Mosquitinho': {'descricao': 'من أصغر أنواع النحل عديم اللسع في البرازيل. شديد '
                                                      'الوداعة. عسله لذيذ جدًا ويُنتج بكميات صغيرة. شديد '
                                                      'الحساسية لاستخدام المبيدات الزراعية. مؤشر على جودة '
                                                      'البيئة.',
                                         'bioma': 'الغابة الأطلسية',
                                         'regiao': 'الجنوب/الجنوب الشرقي'},
                         'Manduri': {'descricao': 'نوع مهدد بالانقراض (VU). عسل نادر يُنتج بكميات صغيرة. '
                                                  'أعشاشه غالبًا في تجاويف الأشجار المحلية. نوع مستهدف في '
                                                  'برامج تربية النحل عديم اللسع لأغراض الحماية.',
                                     'bioma': 'الغابة الأطلسية',
                                     'regiao': 'الجنوب/الجنوب الشرقي'},
                         'Mirim Preguiça': {'descricao': 'تُسمى أيضًا «النحلة الكسولة» لهدوء سلوكها. تعشش '
                                                         'أساسًا على أغصان الأشجار. ملقِّح مهم للأنواع '
                                                         'النباتية المحلية في السيرادو والغابة الأطلسية.',
                                            'bioma': 'السيرادو/الغابة الأطلسية',
                                            'regiao': 'الوسط/الجنوب الشرقي'},
                         'Mandaçaia': {'descricao': 'من أكبر أنواع النحل عديم اللسع. إنتاج عسل متميز. في '
                                                    'تراجع بسبب إزالة الغابات والتحضر. ربّاها شعب الغواراني '
                                                    'الأصلي قرونًا باسم «mborí».',
                                       'bioma': 'الغابة الأطلسية',
                                       'regiao': 'الجنوب الشرقي/الجنوب'},
                         'Uruçu Nordestina': {'descricao': 'نحلة مقدسة عند شعب التوبينامبا، تُربّى منذ أكثر '
                                                           'من 2.000 عام. عسلها ذو خصائص طبية معترف بها. رمز '
                                                           'لتربية النحل عديم اللسع في الشمال الشرقي. نوع '
                                                           'رمزي في تربية النحل لدى الشعوب الأصلية.',
                                              'bioma': 'الكاتينغا/الغابة الأطلسية في الشمال الشرقي',
                                              'regiao': 'الشمال الشرقي'},
                         'Irapuá': {'descricao': 'مع أنها لا تنتج العسل بكميات تجارية، فهي ملقِّح بالغ '
                                                 'الأهمية. تبني أعشاشًا مكشوفة براتنج النباتات. يُخلط بينها '
                                                 'أحيانًا وبين نحل العسل الأوروبي بسبب سلوكها الدفاعي.',
                                    'bioma': 'الجميع',
                                    'regiao': 'وطني'},
                         'Tiúba': {'descricao': 'تُعرف بـ«نحلة الأرض» في ماراньяو. عسل بنكهة فريدة ومحبوب '
                                                'كثيرًا. جزء أساسي من ثقافة تربية النحل عديم اللسع في '
                                                'الأمازون وماراньяو. نوع مهدد بسبب إزالة الغابات.',
                                   'bioma': 'الأمازون/الشمال الشرقي',
                                   'regiao': 'الشمال/الشمال الشرقي'},
                         'Guaraipo': {'descricao': 'نوع بنمط ألوان متغير. إنتاج عسل بنكهة لطيفة. أعشاشه في '
                                                   'التربة أو الجذوع. في تراجع حاد بسبب توسع الزراعة وتربية '
                                                   'المواشي في السيرادو.',
                                      'bioma': 'السيرادو/الغابة الأطلسية',
                                      'regiao': 'الغرب الأوسط/الجنوب الشرقي'},
                         'Iraí': {'descricao': 'نحلة شائعة جدًا في البيئات الحضرية. تعشش في شقوق الجدران '
                                               'وصناديق الكهرباء والقرميد. شديدة التحمل للتحضر. مؤشر ممتاز '
                                               'على اتصال الأجزاء الغابية ببعضها.',
                                  'bioma': 'السيرادو/الغابة الأطلسية',
                                  'regiao': 'الجنوب الشرقي'},
                         'Tubuna': {'descricao': 'تنتج عسلًا داكنًا ومركزًا. أعشاشها في تجاويف الأشجار. '
                                                 'شديدة الحساسية لإزالة الغابات. تُستخدم في مشاريع إعادة '
                                                 'تأهيل الأجزاء الغابية بوصفها ملقِّحًا رئيسًا.',
                                    'bioma': 'الغابة الأطلسية',
                                    'regiao': 'الجنوب الشرقي/الجنوب'},
                         'Mirim Guaçu': {'descricao': 'نوع مقاوم للبرد. شائع جدًا في سانتا كاتارينا وريو '
                                                      'غراندي دو سول. ملقِّح لأنواع نباتية محلية ومزروعة في '
                                                      'المنطقة الجنوبية. عسله ذو نكهة حامضة مميزة.',
                                         'bioma': 'الجنوب/الجنوب الشرقي',
                                         'regiao': 'الجنوب/الجنوب الشرقي'},
                         'Abelha Mamangava': {'descricao': 'ملقِّح حصري للباسيفلورا (فاكهة الآلام). ومن دونه '
                                                           'ينهار إنتاج فاكهة الآلام في البرازيل. يستخدم '
                                                           'تقنية «التلقيح الاهتزازي» (buzz pollination) '
                                                           'بهزّ الأزهار لإطلاق حبوب اللقاح. يبني أعشاشه في '
                                                           'الأغصان الجافة.',
                                              'habitat': 'يعشش في الخشب الميت',
                                              'polinizacao': 'تلقيح اهتزازي — يهتز لإطلاق حبوب اللقاح'},
                         'Abelha Carpinteira': {'descricao': 'جنس Xylocopa يضم أكثر من 50 نوعًا في البرازيل. '
                                                             'سُمّي «النجار» لمهارته في حفر الخشب لبناء '
                                                             'الأعشاش. ملقِّحات مهمة للأزهار الأنبوبية. تعشش '
                                                             'في فنادق النحل ذات قصبات الخيزران.',
                                                'habitat': 'الخشب الجاف، الخيزران',
                                                'polinizacao': 'عامّ — تنوع زهري واسع'},
                         'Abelha Mascarada': {'descricao': 'صغيرة جدًا لكنها أساسية. تنقل حبوب اللقاح في '
                                                           'حوصلتها لا في السلال اللقاحية. تحمل الرحيق وحبوب '
                                                           'اللقاح داخليًا. تستجيب جيدًا لفنادق النحل ذات '
                                                           'القصبات الورقية والخيزران بقطر 5–6 mm.',
                                              'habitat': 'القصبات، الأغصان المجوفة',
                                              'polinizacao': 'الأزهار الصغيرة المفتوحة'},
                         'Abelha Cortadeira': {'descricao': 'تقتطع قطعًا من الأوراق لبناء أعشاشها — ومن هنا '
                                                            'جاء اسمها. يراها البعض «آفات» لكنها ملقِّحات '
                                                            'محلية أساسية. أعشاشها في ثقوب الخشب (مثقاب 8–10 '
                                                            'mm مثالي لفنادق النحل).',
                                               'habitat': 'التربة، الخشب، الأوراق المقتطعة',
                                               'polinizacao': 'أنواع محلية — السيرادو، الغابة الأطلسية'},
                         'Abelha Nômade': {'descricao': 'نحل متطفل سرقي يضع بيضه في أعشاش نحل منفرد آخر. '
                                                        'يشبه الدبابير لكنه نحل. أساسي لتنظيم المجموعات '
                                                        'السكانية والحفاظ على التوازن البيئي في البيئات '
                                                        'الغابية.',
                                           'habitat': 'متطفل على أعشاش أخرى',
                                           'polinizacao': 'غير مباشر — يحافظ على التوازن البيئي'},
                         'Abelha Oleiro': {'descricao': 'ملقِّحات إلزامية لشجرة muricí والباربايتيماو وسائر '
                                                        'Malpighiaceae. تجمع الزيت الزهري من الأزهار لتغذية '
                                                        'يرقاتها. أعشاشها في التربة. مؤشر على سيرادو محفوظ.',
                                           'habitat': 'تربة رملية، جدران صخرية',
                                           'polinizacao': 'اهتزاز على أزهار الزيت — Malpighiaceae'}},
        'back_link': '← المحفظة',
        'lang_label': 'اللغة',
        'cluster_name': 'نقاط الرصد',
        'footer_copy': '© 2022–2026 · مرصد Meliponini · البرازيل',
        'raw_cols': {'especie': 'النوع',
                     'cientifico': 'الاسم العلمي',
                     'tamanho': 'الحجم',
                     'raio': 'نصف قطر الغذاء (m)',
                     'mel': 'إنتاج العسل',
                     'iucn': 'IUCN',
                     'bioma': 'البيئة الحيوية',
                     'registros': 'سجلات GBIF',
                     'colonia': 'المستعمرة (شغالات)',
                     'mel_ano': 'العسل/سنة (kg)',
                     'habitat': 'الموطن',
                     'polinizacao': 'التلقيح',
                     'tipo': 'النوع الحيوي'},
        'tipo_vals': {'meli': 'Meliponini', 'sol': 'منفردة'},
        'tok_nd': 'آلاف',
        'tok_and': ' و',
        'tok_sp_top': 'تستحوذ SP على {n} سجل في GBIF — أكثر من أي ولاية أخرى.',
        'tok_sp_plain': 'تستحوذ SP على {n} سجل في GBIF.',
        'tok_sp_generic': 'تُعدّ SP من أفضل الولايات رصدًا.'},
 'el': {'page_title': 'Παρατηρητήριο Meliponini · Βραζιλία',
        'hero_tag': 'ΒΙΟΠΟΙΚΙΛΟΤΗΤΑ · MELIPONINI · ΒΡΑΖΙΛΙΑ · 2022–2025',
        'hero_title': 'Παρατηρητήριο\nΜελισσών χωρίς Κεντρί',
        'hero_subtitle': 'Παρακολούθηση και ανάλυση της κατανομής των ιθαγενών μελισσών χωρίς κεντρί '
                         '(Meliponini) και των μοναχικών μελισσών στη Βραζιλία — περισσότερες από 24.000 '
                         'καταγραφές GBIF, 12 χαρτογραφημένα είδη και ενεργός προστασία. Περιλαμβάνει '
                         'τεχνική επίσκεψη στη Cidade das Abelhas (SP, 2022) και ξενοδοχείο για μοναχικές '
                         'μέλισσες που κατασκευάστηκε στη FATEC Jundiaí.',
        'badge1': '🐝 12 είδη υπό παρακολούθηση',
        'badge2': '🗺️ 300+ σημεία εμφάνισης',
        'badge3': 'Βραζιλία · 5 Βιότοποι',
        'badge4': 'GBIF · iNaturalist · INPA',
        'badge5': 'Πτυχιακή FATEC Jundiaí 2022',
        'm1': 'Είδη Meliponini',
        'm2': 'Καταγραφές GBIF (2024)',
        'm3': 'Πολιτείες που καλύπτονται',
        'm4': 'Απειλούμενα είδη',
        'tab1': '🗺️ Χάρτης & Ανάλυση',
        'tab2': '🔬 Μεθοδολογία & Ροή',
        'tab3': '💡 Τι ανακαλύψαμε',
        'tab4': '📷 Στο πεδίο',
        'tab5': '📈 Τάσεις',
        'tab6': '⚙️ Παράμετροι',
        'tab7': '📋 Ακατέργαστα δεδομένα',
        'tab8': '📚 Πηγές & Εύσημα',
        'map_label': 'ΚΑΤΑΝΟΜΗ ΣΤΗ ΒΡΑΖΙΛΙΑ',
        'map_title': 'Χάρτης εμφανίσεων — Μέλισσες χωρίς κεντρί',
        'map_hint': '🐝 <strong>Κάντε κλικ στους δείκτες</strong> για να δείτε είδος, βιότοπο και πηγή. '
                    'Μέγεθος ∝ καταγραφές ανά πολιτεία. Ενεργοποιήστε τις ομάδες για να δείτε συγκεντρώσεις.',
        'heat_title': 'Θερμικός χάρτης — Πυκνότητα εμφανίσεων',
        'chart_label': 'ΣΥΓΚΡΙΤΙΚΗ ΑΝΑΛΥΣΗ',
        'sp_registros_title': 'Καταγραφές ανά είδος (GBIF, 2024)',
        'estado_title': 'Καταγραφές ανά πολιτεία',
        'bioma_title': 'Κατανομή ανά βιότοπο',
        'method_label': 'ΕΦΑΡΜΟΣΜΕΝΗ ΒΙΟΠΟΙΚΙΛΟΤΗΤΑ',
        'method_title': 'Ερώτημα & Μεθοδολογία',
        'sci_q_title': '❓ Κεντρικό ερώτημα',
        'sci_q': '"Ποια είναι η σημερινή κατάσταση της κατανομής και της διατήρησης των ιθαγενών μελισσών '
                 'χωρίς κεντρί της Βραζιλίας και πώς μπορούν η ορθολογική μελισσοκομία Meliponini και τα '
                 'ξενοδοχεία για μοναχικές μέλισσες να συμβάλουν στη διατήρηση αυτών των ειδών σε αστικά και '
                 'περιαστικά περιβάλλοντα;"',
        'pipeline_label': 'ΡΟΗ ΔΕΔΟΜΕΝΩΝ',
        'steps': [['1',
                   'Συλλογή — GBIF + iNaturalist (2010–2024)',
                   'Δεδομένα εμφάνισης των βραζιλιανών Meliponini μέσω του API του GBIF και εξαγωγής από το '
                   'iNaturalist. @@TOTAL@@ γεωαναφερμένες καταγραφές (2010–2024), φιλτραρισμένες ώστε να μην '
                   'έχουν γεωχωρικά προβλήματα. Είδη-στόχοι: 12 ιθαγενή Meliponini + 6 μοναχικές μέλισσες.'],
                  ['2',
                   'Τεχνική επίσκεψη — Cidade das Abelhas (SP, 2022)',
                   'Τεχνική επίσκεψη στο πάρκο Cidade das Abelhas στο Σάο Πάολο για άμεση παρατήρηση '
                   'ορθολογικών κυψελών των Jataí, Mosquitinho, Manduri, Mirim Preguiça και άλλων ειδών. '
                   'Φωτογραφική τεκμηρίωση και συλλογή δεδομένων για την ορθολογική διαχείριση των '
                   'μελισσοκομείων.'],
                  ['3',
                   'Πτυχιακή FATEC Jundiaí — Ξενοδοχείο για μοναχικές μέλισσες (2022)',
                   'Πτυχιακή εργασία: κατασκευή Ξενοδοχείου για μοναχικές μέλισσες στην πανεπιστημιούπολη '
                   'της FATEC Jundiaí για την εκδήλωση Ciência na Praça. Ξύλινη κατασκευή με οπές τρυπανιού '
                   '8 και 10 mm για ιθαγενείς μοναχικές μέλισσες όπως οι Xylocopa sp. και Megachile sp.'],
                  ['4',
                   'Χωρική ανάλυση — Κατανομή ανά βιότοπο',
                   'Διασταύρωση των εμφανίσεων με το shapefile των βιοτόπων του IBGE. Εντοπισμός προτύπων '
                   'πλούτου ειδών ανά βιότοπο. Ο Ατλαντικός Δρυμός ως ο βιότοπος με τη μεγαλύτερη '
                   'ποικιλότητα Meliponini (~22 είδη).'],
                  ['5',
                   'Βιολογικές παράμετροι — Επιστημονική βιβλιογραφία',
                   'Συγκέντρωση δεδομένων από τη βιβλιογραφία: μέγεθος αποικίας, ρυθμός ωοτοκίας, διάρκεια '
                   'ζωής εργάτριας, ακτίνα τροφοσυλλογής, παραγωγή μελιού. Βάση: A.B.E.L.H.A., Atlas της '
                   'Μελισσοκομίας Meliponini, δημοσιεύσεις USP/UNICAMP/UFMG.'],
                  ['6',
                   'Αξιολόγηση απειλής — IUCN Red List',
                   'Διασταύρωση των δεδομένων εμφάνισης με το καθεστώς IUCN: @@VU@@ είδη Τρωτά (VU), @@LC@@ '
                   'Ελάχιστης Ανησυχίας (LC). Ανάλυση πληθυσμιακών τάσεων και ανθρωπογενών πιέσεων ανά '
                   'βιότοπο.']],
        'biologia_title': '🐝 Γιατί έχουν σημασία οι μέλισσες χωρίς κεντρί;',
        'biologia_text': '• <b>~550 είδη</b> Meliponini περιγράφονται παγκοσμίως · <b>~350 στη '
                         'Βραζιλία</b><br>• <b>Αποκλειστικοί επικονιαστές</b> ιθαγενών ειδών του Ατλαντικού '
                         'Δρυμού και του Cerrado<br>• <b>Μέλι με φαρμακευτικές ιδιότητες</b> που '
                         'αναγνωρίζονται από την ANVISA (Portaria 310/1997)<br>• <b>Μελισσοκομία '
                         'Meliponini</b>: ορθολογική εκτροφή σε κυψέλες INPA, IBAMA, JTB, Fernão Dias<br>• '
                         '<b>Απειλές:</b> αποδάσωση, γεωργικά φάρμακα, αστικοποίηση, χωροκατακτητικά ξενικά '
                         'είδη',
        'solitarias_title': '🏨 Μοναχικές μέλισσες — Η σιωπηλή πλειονότητα',
        'solitarias_text': '• <b>~70% των μελισσών του κόσμου</b> είναι μοναχικές — χωρίς βασίλισσα, χωρίς '
                           'κυψέλη<br>• <b>Κάθε θηλυκό</b> χτίζει τη δική του φωλιά, συλλέγει τροφή και '
                           'φροντίζει τα αυγά<br>• <b>Τα ξενοδοχεία μελισσών</b> (ξύλινοι κύβοι με οπές 6–10 '
                           'mm) προσελκύουν Xylocopa, Megachile και Hylaeus<br>• <b>Ιδανικές οπές:</b> '
                           'τρυπάνι 8 mm (Megachile), τρυπάνι 10 mm (Xylocopa) — ελάχιστο βάθος 10 cm<br>• '
                           '<b>Τοποθέτηση:</b> προσανατολισμός Ανατολικός/Νοτιοανατολικός, ύψος 1–2 m, '
                           'προστασία από την άμεση βροχή',
        'disc_label': 'ΑΝΑΛΥΣΗ ΚΑΙ ΕΥΡΗΜΑΤΑ',
        'disc_title': 'Τι αποκάλυψαν τα δεδομένα',
        'discoveries': [['🐝',
                         'Jataí — η πιο προσαρμοσμένη στην αστικοποίηση',
                         'Η Tetragonisca angustula είναι το είδος με τη μεγαλύτερη προσαρμοστικότητα στο '
                         'αστικό περιβάλλον. Καταγραφές σε όλες τις πολιτείες της Βραζιλίας και στους 5 '
                         'βιότοπους. Φωλιάζει σε ρωγμές τοιχοποιίας, ηλεκτρικούς πίνακες και στύλους. Η '
                         'παρουσία της στις πόλεις αποτελεί δείκτη οικολογικής ανθεκτικότητας.'],
                        ['⚠️',
                         '@@VU@@ Τρωτά είδη — @@VU_LIST@@',
                         'Τα είδη Melipona με το μεγαλύτερο μέγεθος και την υψηλότερη παραγωγή μελιού είναι '
                         'τα πιο απειλούμενα. Ο συνδυασμός αποδάσωσης, ανθρωπογενούς πίεσης και χαμηλής '
                         'αναπαραγωγής (η βασίλισσα κάνει μόνο 1 γαμήλια πτήση) καθιστά αυτά τα είδη '
                         'ιδιαίτερα ευάλωτα σε πληθυσμιακή κατάρρευση.'],
                        ['🏨',
                         'Ξενοδοχείο μελισσών — πολλαπλασιαστής της αστικής βιοποικιλότητας',
                         'Το Ξενοδοχείο μελισσών που κατασκευάστηκε στη FATEC Jundiaí έδειξε ότι απλές '
                         'ξύλινες κατασκευές με οπές τρυπανιού 8 και 10 mm κατοικούνται σε 30–60 ημέρες από '
                         'ιθαγενή μοναχικά είδη. Μια παρέμβαση χαμηλού κόστους (<R$50) με μεγάλο αντίκτυπο '
                         'για την τοπική επικονίαση.'],
                        ['📊',
                         'Σάο Πάολο — η πρωτεύουσα της μελισσοκομίας Meliponini στη Βραζιλία',
                         '@@SP_SENT@@ Ο συνδυασμός του εναπομείναντος Ατλαντικού Δρυμού, της έντονης '
                         'πανεπιστημιακής έρευνας (USP, UNICAMP, UNESP) και της αυξανόμενης αστικής '
                         'μελισσοκομίας Meliponini εξηγεί αυτόν τον πρωταγωνιστικό ρόλο.'],
                        ['🌎',
                         'GBIF: @@GROWTH@@ σε 10 χρόνια — η συμμετοχική επιστήμη ως κινητήρας',
                         'Η αύξηση κατά @@GROWTH_ABS@@ των γεωαναφερμένων καταγραφών Meliponini στη Βραζιλία '
                         'μεταξύ 2014 και 2024 (@@GROWTH@@) συμβαδίζει με την αυξανόμενη χρήση του '
                         'iNaturalist και το ενδιαφέρον των πολιτών για τη βιοποικιλότητα. Η αυξανόμενη '
                         'αστική μελισσοκομία Meliponini είναι συγχρόνως συνέπεια και αιτία αυτού του '
                         'ενδιαφέροντος.'],
                        ['🌿',
                         'Cerrado — βιότοπος με ανεπαρκή δειγματοληψία και μεγάλη κρυμμένη ποικιλότητα',
                         'Παρότι φιλοξενεί ~100 ενδημικά είδη Meliponini, το Cerrado παραδοσιακά '
                         'υποδειγματοληπτείται στις καταγραφές βιοποικιλότητας. Η ανεπαρκής δειγματοληψία '
                         'αντικατοπτρίζει κενά της έρευνας σε απομακρυσμένες περιοχές — μια προειδοποίηση '
                         'για τη διατήρηση προτού ο βιότοπος κατακερματιστεί κατά 100%.']],
        'conclusion_label': 'ΣΥΜΠΕΡΑΣΜΑ',
        'conclusion_title': 'Κάθε κυψέλη μετράει',
        'conclusion_text': 'Οι ιθαγενείς μέλισσες χωρίς κεντρί της Βραζιλίας αποτελούν μια μοναδική '
                           'βιοπολιτισμική κληρονομιά: καλλιεργούνται από τους αυτόχθονες λαούς εδώ και '
                           'χιλιετίες, παράγουν μέλι με φαρμακευτικές ιδιότητες και είναι αναντικατάστατοι '
                           'επικονιαστές της ιθαγενούς χλωρίδας μας. Η αύξηση κατά @@GROWTH_N@@ στις '
                           'καταγραφές Meliponini του GBIF δείχνει ότι το ενδιαφέρον για τη μελισσοκομία '
                           'Meliponini αυξάνεται — όμως ο ρυθμός της αποδάσωσης εξακολουθεί να ξεπερνά την '
                           'ταχύτητα της διατήρησης. Κάθε ορθολογική κυψέλη που τοποθετείται, κάθε '
                           'ξενοδοχείο μελισσών που χτίζεται, κάθε τμήμα δάσους που προστατεύεται είναι ένα '
                           'ψήφος εμπιστοσύνης στο μέλλον αυτών των ειδών.',
        'conclusion_author': 'Amauri Almeida · Πτυχιακή Περιβαλλοντικής Διαχείρισης · FATEC Jundiaí · 2022 · '
                             'Επίσκεψη Cidade das Abelhas SP',
        'field_label': 'ΚΑΤΑΓΡΑΦΗ ΠΕΔΙΟΥ ΚΑΙ ΤΕΧΝΙΚΗ ΤΕΚΜΗΡΙΩΣΗ',
        'field_title': 'Από τη Cidade das Abelhas στην πανεπιστημιούπολη της FATEC',
        'field_inst_title': '📁 Πώς να προσθέσετε τις φωτογραφίες σας',
        'field_inst': 'Τοποθετήστε τις φωτογραφίες σας στον φάκελο <code>assets/campo/</code> με τα ακριβή '
                      'ονόματα που φαίνονται παρακάτω.',
        'photos': [{'emoji': '🐝',
                    'grupo': 'CIDADE DAS ABELHAS · ΣΑΟ ΠΑΟΛΟ · 2022',
                    'titulo': 'Ορθολογική κυψέλη — Μέλισσα Jataí',
                    'esp': 'Tetragonisca angustula',
                    'desc': 'Ορθολογική κυψέλη (κουτί JTB ή INPA) της μέλισσας Jataí (Tetragonisca '
                            'angustula) στο πάρκο Cidade das Abelhas, Σάο Πάολο. Η Jataí είναι το πιο κοινό '
                            'και προσαρμοστικό είδος της Βραζιλίας — φωλιάζει φυσικά σε ρωγμές τοιχοποιίας. '
                            'Η ορθολογική κυψέλη επιτρέπει τη διαίρεση των αποικιών και τη διαχείριση χωρίς '
                            'καταστροφή της φωλιάς.',
                    'path': 'assets/campo/01_colmeia_jatai_cidade_abelhas.jpg',
                    'legenda': 'Κυψέλη Jataí (Tetragonisca angustula) · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🔎',
                    'grupo': 'CIDADE DAS ABELHAS · ΣΑΟ ΠΑΟΛΟ · 2022',
                    'titulo': 'Ορθολογική κυψέλη — Μέλισσα Mosquitinho',
                    'esp': 'Plebeia mosquito',
                    'desc': 'Ορθολογική κυψέλη της μέλισσας Mosquitinho (Plebeia mosquito) — μία από τις '
                            'μικρότερες μέλισσες χωρίς κεντρί της Βραζιλίας (2 mm). Εξαιρετικά ήρεμη και '
                            'ευαίσθητη στα γεωργικά φάρμακα. Κυψέλη με χωριστή μονάδα μελιού από τη μονάδα '
                            'γόνου — βασική πρακτική της ορθολογικής μελισσοκομίας Meliponini για να μη '
                            'βλάπτεται η αποικία.',
                    'path': 'assets/campo/02_colmeia_mosquitinho_cidade_abelhas.jpg',
                    'legenda': 'Κυψέλη Mosquitinho (Plebeia mosquito) · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🌿',
                    'grupo': 'CIDADE DAS ABELHAS · ΣΑΟ ΠΑΟΛΟ · 2022',
                    'titulo': 'Ορθολογική κυψέλη — Μέλισσα Manduri (1)',
                    'esp': 'Melipona marginata',
                    'desc': 'Ορθολογική κυψέλη της μέλισσας Manduri (Melipona marginata) — Τρωτό είδος (IUCN '
                            'VU). Ένα από τα σημαντικότερα είδη για τη διατήρηση: σπάνιο μέλι, που παράγεται '
                            'σε μικρή ποσότητα, και φωλιάζει αποκλειστικά σε κουφάλες ιθαγενών δέντρων. Η '
                            'ορθολογική μελισσοκομία είναι η κύρια στρατηγική διατήρησης ex situ για αυτό το '
                            'είδος.',
                    'path': 'assets/campo/04_colmeia_manduri_cidade_abelhas_1.jpg',
                    'legenda': 'Κυψέλη Manduri (Melipona marginata) · Τρωτό · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🌿',
                    'grupo': 'CIDADE DAS ABELHAS · ΣΑΟ ΠΑΟΛΟ · 2022',
                    'titulo': 'Ορθολογική κυψέλη — Μέλισσα Manduri (2)',
                    'esp': 'Melipona marginata',
                    'desc': 'Δεύτερη τεκμηριωμένη κυψέλη Manduri. Η παρακολούθηση πολλών κυψελών του ίδιου '
                            'είδους επιτρέπει τη μελέτη της συμπεριφορικής και παραγωγικής μεταβλητότητας. Η '
                            'διαφορά χρώματος και δομής μεταξύ των κουτιών αντανακλά διαφορετικά μοντέλα '
                            'ορθολογικής κυψέλης — INPA, Fernão Dias, JTB και μοντέλα USP.',
                    'path': 'assets/campo/05_colmeia_manduri_cidade_abelhas_2.jpg',
                    'legenda': 'Κυψέλη Manduri (2) · Melipona marginata · VU · Cidade das Abelhas · SP · '
                               '2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · ΣΑΟ ΠΑΟΛΟ · 2022',
                    'titulo': 'Ορθολογική κυψέλη — Mirim Preguiça (1)',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'Ορθολογική κυψέλη της μέλισσας Mirim Preguiça (Frieseomelitta varia) — '
                            'ονομάστηκε έτσι από την ήρεμη συμπεριφορά των εργατριών στην είσοδο της '
                            'κυψέλης. Σημαντικό είδος για την επικονίαση ιθαγενών ειδών του Cerrado και του '
                            'Ατλαντικού Δρυμού. Χτίζει φωλιές σε κλαδιά δέντρων.',
                    'path': 'assets/campo/06_colmeia_mirim_preguica_1.jpg',
                    'legenda': 'Κυψέλη Mirim Preguiça (Frieseomelitta varia) · Cidade das Abelhas · SP · '
                               '2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · ΣΑΟ ΠΑΟΛΟ · 2022',
                    'titulo': 'Ορθολογική κυψέλη — Mirim Preguiça (2)',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'Δεύτερη όψη της κυψέλης Mirim Preguiça. Παρατηρείται η είσοδος της κυψέλης με '
                            'τα ιδιαίτερα χαρακτηριστικά αυτού του είδους. Η εσωτερική αρχιτεκτονική της '
                            'φωλιάς, με σφαιρικά κελιά γόνου, διαφέρει από εκείνη των Melipona — κάτι που '
                            'απαιτεί ειδικές προσαρμογές στα ορθολογικά κουτιά για αυτό το είδος.',
                    'path': 'assets/campo/07_colmeia_mirim_preguica_2.jpg',
                    'legenda': 'Κυψέλη Mirim Preguiça (2) · Frieseomelitta varia · Cidade das Abelhas · SP · '
                               '2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · ΣΑΟ ΠΑΟΛΟ · 2022',
                    'titulo': 'Ορθολογική κυψέλη — Mirim Preguiça (3)',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'Τρίτη γωνία της κυψέλης Mirim Preguiça, που δείχνει λεπτομέρειες της εξωτερικής '
                            'δομής και της βάσης στήριξης. Η τεκμηρίωση με πολλαπλές όψεις είναι απαραίτητη '
                            'στις τεχνικές επισκέψεις, ώστε να εντοπίζονται πρότυπα διαχείρισης και '
                            'σχεδιασμοί κυψέλης που λειτουργούν καλύτερα για κάθε είδος.',
                    'path': 'assets/campo/08_colmeia_mirim_preguica_3.jpg',
                    'legenda': 'Κυψέλη Mirim Preguiça (3) · Frieseomelitta varia · Cidade das Abelhas · SP · '
                               '2022',
                    'gid': 'cidade'},
                   {'emoji': '🏛️',
                    'grupo': 'CIDADE DAS ABELHAS · ΣΑΟ ΠΑΟΛΟ · 2022',
                    'titulo': 'Μελισσοκομείο — Συλλογή διαφορετικών ειδών',
                    'esp': 'Πολλαπλά είδη',
                    'desc': 'Άποψη του μελισσοκομείου του πάρκου Cidade das Abelhas με ορθολογικά κουτιά '
                            'διαφορετικών ειδών το ένα δίπλα στο άλλο — όπως υπαγορεύει η καλή πρακτική της '
                            'μελισσοκομίας Meliponini. Κάθε είδος έχει το δικό του επισημασμένο κουτί. Η '
                            'απόσταση μεταξύ των κυψελών και ο προσανατολισμός της εισόδου υπολογίζονται '
                            'ώστε να ελαχιστοποιείται η παρέκκλιση των μελισσών και να μεγιστοποιείται η '
                            'υγεία των αποικιών.',
                    'path': 'assets/campo/09_meliponario_colecao_cidade_abelhas.jpg',
                    'legenda': 'Μελισσοκομείο με διαφορετικά είδη · Ορθολογικά κουτιά · Πάρκο Cidade das '
                               'Abelhas · SP · 2022',
                    'destaque': True,
                    'gid': 'cidade'},
                   {'emoji': '🌳',
                    'grupo': 'ΞΕΝΟΔΟΧΕΙΟ ΜΕΛΙΣΣΩΝ · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Κατασκευή του ξενοδοχείου — Ξύλινη δομή',
                    'esp': 'Για μοναχικές μέλισσες',
                    'desc': 'Έναρξη της κατασκευής του Ξενοδοχείου για μοναχικές μέλισσες στην '
                            'πανεπιστημιούπολη της FATEC Jundiaí. Η ξύλινη δομή είναι το κύριο στήριγμα για '
                            'τους διάτρητους κύβους. Η επιλογή του ξύλου (επεξεργασμένο πεύκο ή ευκάλυπτος) '
                            'είναι σημαντική: πρέπει να αντέχει στην υγρασία αλλά να μην έχει υποστεί '
                            'επεξεργασία με βιοκτόνα που απωθούν τις μέλισσες.',
                    'path': 'assets/campo/10_hotel_abelhas_estrutura_madeira.jpg',
                    'legenda': 'Κατασκευή Ξενοδοχείου μελισσών · Ξύλινη δομή · FATEC Jundiaí · Ciência na '
                               'Praça · 2022',
                    'gid': 'hotel'},
                   {'emoji': '🔩',
                    'grupo': 'ΞΕΝΟΔΟΧΕΙΟ ΜΕΛΙΣΣΩΝ · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Διάτρηση των κύβων — Τρυπάνι 8 και 10 mm',
                    'esp': 'Για μοναχικές μέλισσες',
                    'desc': 'Διάτρηση των ξύλινων κύβων με δράπανο, με τρυπάνι 8 mm (Megachile sp., Hylaeus '
                            'sp.) και τρυπάνι 10 mm (Xylocopa sp.). Το ελάχιστο βάθος των 10 cm είναι '
                            'απαραίτητο ώστε το θηλυκό να ολοκληρώσει τη φωλιά με 3–5 κελιά γόνου. Οι οπές '
                            'πρέπει να καταλήγουν σε τυφλό πυθμένα — δεν πρέπει να διαπερνούν τον κύβο.',
                    'path': 'assets/campo/11_hotel_abelhas_furadeira_broca8_10.jpg',
                    'legenda': 'Διάτρηση με τρυπάνι 8 και 10 mm · Ξενοδοχείο μοναχικών μελισσών · FATEC '
                               'Jundiaí · 2022',
                    'gid': 'hotel'},
                   {'emoji': '🔩',
                    'grupo': 'ΞΕΝΟΔΟΧΕΙΟ ΜΕΛΙΣΣΩΝ · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Λεπτομέρεια της διάτρησης — Τρυπάνι 8 και 10 mm',
                    'esp': 'Για μοναχικές μέλισσες',
                    'desc': 'Λεπτομέρεια της διαδικασίας διάτρησης με τρυπάνι 8 και 10 mm. Η ομοιομορφία των '
                            'οπών είναι σημαντική για την επιτυχία του ξενοδοχείου: ελάχιστο βάθος 10 cm, '
                            'ακριβής διάμετρος και λεία εσωτερική επιφάνεια (τρίψιμο αν χρειαστεί). Οπές με '
                            'οδοντωτό εσωτερικό μπορεί να εμποδίζουν τη διέλευση των μελισσών.',
                    'path': 'assets/campo/12_hotel_abelhas_furos_detalhe.jpg',
                    'legenda': 'Λεπτομέρεια οπών τρυπανιού 8/10 mm · Ξενοδοχείο μοναχικών μελισσών · FATEC '
                               'Jundiaí · 2022',
                    'gid': 'hotel'},
                   {'emoji': '✅',
                    'grupo': 'ΞΕΝΟΔΟΧΕΙΟ ΜΕΛΙΣΣΩΝ · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Ολοκληρωμένο ξενοδοχείο μελισσών — Πανεπιστημιούπολη FATEC Jundiaí',
                    'esp': 'Για μοναχικές μέλισσες',
                    'desc': 'Το Ξενοδοχείο για μοναχικές μέλισσες ολοκληρώθηκε και τοποθετήθηκε στην '
                            'πανεπιστημιούπολη της FATEC Jundiaí για την εκδήλωση Ciência na Praça. Ξύλινοι '
                            'κύβοι με οπές τρυπανιού 8 και 10 mm, προσανατολισμός '
                            'Ανατολικός/Νοτιοανατολικός, ύψος ~1,5 m, προστατευμένο με στέγαστρο από τη '
                            'βροχή. Κατασκευή χαμηλού κόστους (<R$50) με μεγάλο αντίκτυπο για την τοπική '
                            'επικονίαση.',
                    'path': 'assets/campo/13_hotel_abelhas_concluido_fatec_jundiai.jpg',
                    'legenda': 'Ολοκληρωμένο Ξενοδοχείο μοναχικών μελισσών · Πανεπιστημιούπολη FATEC Jundiaí '
                               '· Ciência na Praça · 2022',
                    'destaque_final': True,
                    'gid': 'hotel'}],
        'timeline_label': 'ΧΡΟΝΟΛΟΓΙΟ ΤΟΥ ΕΡΓΟΥ',
        'timeline_items': [['2022 · Jan–Jun',
                            'Πτυχιακή Περιβαλλοντικής Διαχείρισης — FATEC Jundiaí',
                            'Έρευνα για τη μελισσοκομία Meliponini και τις μοναχικές μέλισσες · Κατασκευή '
                            'Ξενοδοχείου μελισσών για το Ciência na Praça'],
                           ['2022 · Jul',
                            'Τεχνική επίσκεψη — Cidade das Abelhas SP',
                            'Φωτογραφική καταγραφή 8+ ειδών σε ορθολογικές κυψέλες · Jataí, Mosquitinho, '
                            'Manduri, Mirim Preguiça και άλλα'],
                           ['2022 · Nov',
                            'Υποστήριξη της πτυχιακής — FATEC Jundiaí',
                            'Έγκριση της πτυχιακής εργασίας στην Περιβαλλοντική Διαχείριση · Επιτυχής '
                            'ολοκλήρωση σπουδών'],
                           ['2023–2024',
                            'Ανάλυση GBIF — @@TOTAL@@ καταγραφές',
                            'Διασταύρωση δεδομένων εμφάνισης με βιοτόπους και πολιτείες · Εντοπισμός κενών '
                            'διατήρησης'],
                           ['2025',
                            'Δημοσίευση στο Portfolio',
                            'Παρατηρητήριο Meliponini της Βραζιλίας — δημόσιος πίνακας ελέγχου με '
                            'ενημερωμένα δεδομένα']],
        'trend_sel': 'Επιλέξτε οπτικοποίηση',
        'trend_opt1': 'Αύξηση GBIF (2010–2024)',
        'trend_opt2': 'Καταγραφές ανά είδος (κατάταξη)',
        'trend_opt3': 'Καταγραφές ανά πολιτεία',
        'param_sel': 'Είδος προς ανάλυση',
        'param_names': {'colonia': 'Μέγεθος αποικίας (εργάτριες)',
                        'postura_dia': 'Ρυθμός ωοτοκίας (αυγά/ημέρα)',
                        'vida_operaria': 'Διάρκεια ζωής εργάτριας (ημέρες)',
                        'longe_formag': 'Ακτίνα τροφοσυλλογής (m)',
                        'prod_mel_kg': 'Παραγωγή μελιού (kg/έτος)',
                        'raio_dna_km': 'Γενετική απόσταση (km)'},
        'raw_label': 'ΚΑΤΑΛΟΓΟΣ ΕΙΔΩΝ',
        'raw_title': 'Πλήρης πίνακας — Meliponini της Βραζιλίας',
        'download_csv': '⬇️ Λήψη CSV',
        'sources_label': 'ΕΠΙΣΤΗΜΟΝΙΚΕΣ ΠΗΓΕΣ',
        'sources_title': 'Πηγές & Βάση δεδομένων',
        'tech_label': 'ΤΕΧΝΟΛΟΓΙΕΣ ΠΟΥ ΧΡΗΣΙΜΟΠΟΙΗΘΗΚΑΝ',
        'footer_title': '🐝 Amauri Almeida',
        'footer_desc': 'Τεχνολόγος Περιβαλλοντικής Διαχείρισης · FATEC Jundiaí (3ος στο '
                       'ENADE)<br>Μεταπτυχιακό στην ΤΝ, τη Μηχανική Μάθηση & την Επιστήμη Δεδομένων · '
                       'Επιστήμη Δεδομένων & Big Data<br>Ανάλυση και Ανάπτυξη Συστημάτων · FACINT Maringá',
        'footer_links': '📍 Fernandópolis · SP · Βραζιλία',
        'trend_label': 'ΧΡΟΝΙΚΗ ΕΞΕΛΙΞΗ & ΚΑΤΑΤΑΞΕΙΣ',
        'param_label': 'ΣΥΓΚΡΙΤΙΚΗ ΒΙΟΛΟΓΙΑ',
        'param_title': 'Βιολογικές παράμετροι των ειδών',
        'param_detail': 'Βιολογική παράμετρος',
        'param_cmp': 'Σύγκριση ειδών',
        'records_axis': 'Καταγραφές',
        'records_hover': 'καταγραφές',
        'gal_meli': 'ΓΚΑΛΕΡΙ ΕΙΔΩΝ — MELIPONINI',
        'gal_sol': 'ΓΚΑΛΕΡΙ — ΜΟΝΑΧΙΚΕΣ ΜΕΛΙΣΣΕΣ',
        'honey': 'Μέλι',
        'mel_vals': {'Sim': 'Ναι', 'Não': 'Όχι', 'Pouco': 'Λίγο'},
        'gbif_records': 'καταγραφές GBIF',
        'pop_records': 'Καταγραφές',
        'pop_species': 'Είδη',
        'pop_status': 'Κατάσταση',
        'status_vals': {'Alta': 'Υψηλή', 'Média': 'Μέτρια', 'Baixa': 'Χαμηλή'},
        'radar_title': 'Συγκριτικό προφίλ των ειδών (κλίμακα 0–10)',
        'radar_cats': ['Παραγωγή μελιού',
                       'Αστική προσαρμογή',
                       'Ακτίνα πτήσης',
                       'Μέγεθος αποικίας',
                       'IUCN (αντίστρ.)'],
        'grp_city': '🏛️ CIDADE DAS ABELHAS · ΣΑΟ ΠΑΟΛΟ · 2022',
        'grp_hotel': '🏨 ΞΕΝΟΔΟΧΕΙΟ ΜΟΝΑΧΙΚΩΝ ΜΕΛΙΣΣΩΝ · FATEC JUNDIAÍ · CIÊNCIA NA PRAÇA · 2022',
        'dest_melipon': '⭐ ΕΠΙΛΕΓΜΕΝΟ — ΟΛΟΚΛΗΡΟ ΜΕΛΙΣΣΟΚΟΜΕΙΟ · CIDADE DAS ABELHAS',
        'dest_hotel': '✅ ΤΕΛΙΚΟ ΕΠΙΛΕΓΜΕΝΟ — ΟΛΟΚΛΗΡΩΜΕΝΟ ΞΕΝΟΔΟΧΕΙΟ · ΠΑΝΕΠΙΣΤΗΜΙΟΥΠΟΛΗ FATEC JUNDIAÍ',
        'hotel_build_title': '🏗️ Πώς να χτίσετε ένα Ξενοδοχείο για μοναχικές μέλισσες',
        'hotel_build': [['Υλικό',
                         'Ξύλινος κύβος (επεξεργασμένο πεύκο ή ευκάλυπτος) · τουλάχιστον 15×10×10 cm'],
                        ['Οπές', 'Τρυπάνι 8 mm (Megachile, Hylaeus) · Τρυπάνι 10 mm (Xylocopa)'],
                        ['Βάθος', 'Τουλάχιστον 10 cm · Τυφλός πυθμένας (μη διαπερνάτε τον κύβο!)'],
                        ['Προσανατολισμός', 'Ανατολικός ή Νοτιοανατολικός · Δέχεται πρωινό ήλιο'],
                        ['Ύψος', '1–2 μέτρα από το έδαφος · Προστατευμένο από βροχή και άνεμο'],
                        ['Αποτέλεσμα', 'Κατοίκηση σε 30–60 ημέρες από ιθαγενείς μέλισσες']],
        'solitary_tbl': 'Μοναχικές μέλισσες',
        'card_lbls': {'biome': 'Βιότοπος',
                      'region': 'Περιοχή',
                      'colony': 'Αποικία',
                      'workers': 'εργάτριες',
                      'laying': 'Ωοτοκία',
                      'eggs_day': 'αυγά/ημέρα',
                      'worker_life': 'Ζωή εργάτριας',
                      'days': 'ημέρες',
                      'forage': 'Ακτίνα τροφοσυλλογής',
                      'honey': 'Παραγωγή μελιού',
                      'kg_year': 'kg/έτος',
                      'gen_dist': 'Γενετ. απόσταση'},
        'carto_fallback': 'Χρησιμοποιείται εναλλακτικός χάρτης βάσης (OpenStreetMap).',
        'occ_live': 'Πραγματικά σημεία του GBIF (api.gbif.org): {n} γεωαναφερμένες εμφανίσεις στη Βραζιλία, '
                    'έως {k} ανά είδος, με ερώτημα στις {d}. Κάντε κλικ σε ένα σημείο για να ανοίξετε την '
                    'αρχική καταγραφή.',
        'occ_demo': 'Το GBIF δεν είναι διαθέσιμο αυτή τη στιγμή: τα σημεία που εμφανίζονται είναι '
                    'ΕΙΚΟΝΙΣΤΙΚΑ (πρωτεύουσες × είδη) και δεν αποτελούν καταγραφές πεδίου.',
        'occ_none': 'Το GBIF δεν είναι διαθέσιμο αυτή τη στιγμή και δεν υπάρχουν εφεδρικά δεδομένα: ο χάρτης '
                    'εμφανίσεων δεν εμφανίζεται.',
        'dados_live': 'Αριθμοί που υπολογίστηκαν από το GBIF (api.gbif.org), με ερώτημα στις {d}· αυτόματη '
                      'ενημέρωση κάθε 24 ώρες.',
        'dados_snapshot': 'Το GBIF δεν είναι διαθέσιμο αυτή τη στιγμή: αριθμοί από το τελευταίο αποθηκευμένο '
                          'στιγμιότυπο ({d}).',
        'dados_static': 'Το GBIF δεν είναι διαθέσιμο αυτή τη στιγμή: τιμές αναφοράς από προγενέστερη '
                        'συλλογή, χωρίς ενημέρωση.',
        'serie_total': 'Σύνολο (Meliponini + 5 μοναχικά γένη)',
        'serie_inat': 'iNaturalist (Meliponini)',
        'raio_sel': 'Εμφάνιση ακτίνας τροφοσυλλογής (κύκλοι σε μέτρα)',
        'raio_note': 'Κάθε κύκλος δείχνει τη μέση ακτίνα πτήσης του είδους γύρω από πραγματικές εμφανίσεις '
                     '(έως {n} ανά είδος). Κάντε ζουμ στον χάρτη για να δείτε την κλίμακα.',
        'raio_layer': 'Ακτίνα τροφοσυλλογής',
        'footer_portfolio': 'Portfolio',
        'sources': [['GBIF',
                     'GBIF — Global Biodiversity Information Facility',
                     'gbif.org · Βάση εμφανίσεων με @@TOTAL@@ γεωαναφερμένες καταγραφές Meliponini στη '
                     'Βραζιλία (2010–2024). Δεδομένα από μουσεία, χερμπάρια, το iNaturalist και ερευνητές.',
                     '#C47D0E'],
                    ['A.B.E.L.H.A.',
                     'A.B.E.L.H.A. — Βραζιλιάνικη Ένωση Μελέτης των Μελισσών',
                     'abelha.org.br · Atlas της Μελισσοκομίας Meliponini στη Βραζιλία. Σημείο αναφοράς για '
                     'ακτίνες τροφοσυλλογής, βιολογία και διατήρηση.',
                     '#C0390A'],
                    ['INATURALIST',
                     'iNaturalist — Παγκόσμια συμμετοχική επιστήμη',
                     'inaturalist.org · @@INAT@@ γεωαναφερμένες καταγραφές βραζιλιανών Meliponini (σύνολο '
                     'δεδομένων iNaturalist Research-grade στο GBIF). Βασικός κινητήρας της αύξησης του '
                     'GBIF.',
                     '#2D7A45'],
                    ['FATEC',
                     'FATEC Jundiaí — Πτυχιακή Περιβαλλοντικής Διαχείρισης (2022)',
                     'Ξενοδοχείο για μοναχικές μέλισσες που κατασκευάστηκε στην πανεπιστημιούπολη για την '
                     'εκδήλωση Ciência na Praça. Τρυπάνι 8 και 10 mm. Εγκρίθηκε με διάκριση.',
                     '#1B3A1E'],
                    ['CIDADE ABELHAS',
                     'Πάρκο Cidade das Abelhas — Σάο Πάολο (2022)',
                     'Τεχνική επίσκεψη το 2022. Φωτογραφική καταγραφή ορθολογικών κυψελών των Jataí, '
                     'Mosquitinho, Manduri, Mirim Preguiça και άλλων.',
                     '#5C3D1E'],
                    ['IUCN',
                     'IUCN Red List — Κόκκινος Κατάλογος Απειλούμενων Ειδών',
                     '@@VU_TAGS@@. Καθεστώς διατήρησης των βραζιλιανών Meliponini.',
                     '#8B2515'],
                    ['INPA',
                     'INPA — Εθνικό Ινστιτούτο Ερευνών του Αμαζονίου',
                     'Μοντέλο ορθολογικής κυψέλης INPA για τα Meliponini του Αμαζονίου. Δεδομένα ειδών της '
                     'Βόρειας Βραζιλίας.',
                     '#0D4E72'],
                    ['EMBRAPA',
                     'EMBRAPA Cerrados / EMBRAPA Amazônia Oriental',
                     'Δεδομένα μελισσοκομίας Meliponini στους βιοτόπους της Βραζιλίας. Τεχνική αναφορά για '
                     'είδη του Cerrado και του Αμαζονίου.',
                     '#C47D0E']],
        'species_text': {'Jataí': {'descricao': 'Η πιο γνωστή μέλισσα χωρίς κεντρί της Βραζιλίας. Παράγει '
                                                'μέλι εξαιρετικά υψηλής ποιότητας με φαρμακευτικές '
                                                'ιδιότητες. Φωλιές σε κουφάλες δέντρων και ρωγμές '
                                                'τοιχοποιίας. Σφράγιση της εισόδου με πρόπολη, σε σωλήνα ή '
                                                'σε μικρές πλάκες.',
                                   'bioma': 'Όλοι',
                                   'regiao': 'Εθνικό'},
                         'Mosquitinho': {'descricao': 'Μία από τις μικρότερες μέλισσες χωρίς κεντρί της '
                                                      'Βραζιλίας. Εξαιρετικά ήρεμη. Πολύ γευστικό μέλι που '
                                                      'παράγεται σε μικρές ποσότητες. Πολύ ευαίσθητη στη '
                                                      'χρήση γεωργικών φαρμάκων. Δείκτης περιβαλλοντικής '
                                                      'ποιότητας.',
                                         'bioma': 'Ατλαντικός Δρυμός',
                                         'regiao': 'Νότος/Νοτιοανατολικά'},
                         'Manduri': {'descricao': 'Είδος υπό εξαφάνιση (VU). Σπάνιο μέλι, που παράγεται σε '
                                                  'μικρές ποσότητες. Φωλιές συνήθως σε κοιλότητες ιθαγενών '
                                                  'δέντρων. Είδος-στόχος προγραμμάτων μελισσοκομίας '
                                                  'Meliponini για τη διατήρηση.',
                                     'bioma': 'Ατλαντικός Δρυμός',
                                     'regiao': 'Νότος/Νοτιοανατολικά'},
                         'Mirim Preguiça': {'descricao': 'Λέγεται και Μέλισσα Preguiça (νωθρή) λόγω της '
                                                         'ήρεμης συμπεριφοράς της. Φωλιάζει κυρίως σε κλαδιά '
                                                         'δέντρων. Σημαντικός επικονιαστής ιθαγενών ειδών '
                                                         'του Cerrado και του Ατλαντικού Δρυμού.',
                                            'bioma': 'Cerrado/Ατλαντικός Δρυμός',
                                            'regiao': 'Κέντρο/Νοτιοανατολικά'},
                         'Mandaçaia': {'descricao': 'Μία από τις μεγαλύτερες μέλισσες χωρίς κεντρί. Μέλι '
                                                    'ξεχωριστής παραγωγής. Σε παρακμή λόγω αποδάσωσης και '
                                                    'αστικοποίησης. Εκτρέφεται εδώ και αιώνες από τους '
                                                    "αυτόχθονες Guaraní ως 'mborí'.",
                                       'bioma': 'Ατλαντικός Δρυμός',
                                       'regiao': 'Νοτιοανατολικά/Νότος'},
                         'Uruçu Nordestina': {'descricao': 'Ιερή μέλισσα των Tupinambá, που καλλιεργείται '
                                                           'εδώ και πάνω από 2.000 χρόνια. Μέλι με '
                                                           'αναγνωρισμένες φαρμακευτικές ιδιότητες. Σύμβολο '
                                                           'της μελισσοκομίας Meliponini της '
                                                           'Βορειοανατολικής Βραζιλίας. Είδος-σημαία της '
                                                           'αυτόχθονης μελισσοκομίας.',
                                              'bioma': 'Caatinga/Ατλαντικός Δρυμός ΒΑ',
                                              'regiao': 'Βορειοανατολικά'},
                         'Irapuá': {'descricao': 'Αν και δεν παράγει μέλι σε εμπορική ποσότητα, είναι πολύ '
                                                 'σημαντικός επικονιαστής. Χτίζει εκτεθειμένες φωλιές με '
                                                 'φυτική ρητίνη. Μερικές φορές συγχέεται με την ευρωπαϊκή '
                                                 'μέλισσα λόγω της αμυντικής συμπεριφοράς της.',
                                    'bioma': 'Όλοι',
                                    'regiao': 'Εθνικό'},
                         'Tiúba': {'descricao': "Γνωστή ως 'Abelha da Terra' (μέλισσα της γης) στο Maranhão. "
                                                'Μέλι με μοναδική γεύση, πολύ αγαπητό. Θεμελιώδες μέρος του '
                                                'μελισσοκομικού πολιτισμού του Αμαζονίου και του Maranhão. '
                                                'Είδος σε κίνδυνο λόγω της αποδάσωσης.',
                                   'bioma': 'Αμαζόνιος/Βορειοανατολικά',
                                   'regiao': 'Βορράς/Βορειοανατολικά'},
                         'Guaraipo': {'descricao': 'Είδος με μεταβλητό πρότυπο χρωματισμού. Παραγωγή μελιού '
                                                   'ήπιας γεύσης. Φωλιές στο έδαφος ή σε κορμούς. Σε έντονη '
                                                   'παρακμή λόγω της προέλασης της γεωργοκτηνοτροφίας στο '
                                                   'Cerrado.',
                                      'bioma': 'Cerrado/Ατλαντικός Δρυμός',
                                      'regiao': 'Κεντροδυτικά/Νοτιοανατολικά'},
                         'Iraí': {'descricao': 'Μέλισσα πολύ συνηθισμένη σε αστικά περιβάλλοντα. Φωλιάζει σε '
                                               'ρωγμές τοίχων, ηλεκτρικούς πίνακες και κεραμίδια. Πολύ '
                                               'ανθεκτική στην αστικοποίηση. Εξαιρετικός δείκτης της '
                                               'συνδεσιμότητας των δασικών τμημάτων.',
                                  'bioma': 'Cerrado/Ατλαντικός Δρυμός',
                                  'regiao': 'Νοτιοανατολικά'},
                         'Tubuna': {'descricao': 'Παραγωγός σκούρου και έντονου μελιού. Φωλιές σε κοιλότητες '
                                                 'δέντρων. Πολύ ευαίσθητη στην αποψίλωση. Χρησιμοποιείται σε '
                                                 'έργα αποκατάστασης δασικών τμημάτων ως βασικός '
                                                 'επικονιαστής.',
                                    'bioma': 'Ατλαντικός Δρυμός',
                                    'regiao': 'Νοτιοανατολικά/Νότος'},
                         'Mirim Guaçu': {'descricao': 'Είδος ανθεκτικό στο κρύο. Πολύ συνηθισμένο στη Santa '
                                                      'Catarina και στο Rio Grande do Sul. Επικονιαστής '
                                                      'ιθαγενών και καλλιεργούμενων ειδών της νότιας '
                                                      'περιοχής. Μέλι με χαρακτηριστική όξινη γεύση.',
                                         'bioma': 'Νότος/Νοτιοανατολικά',
                                         'regiao': 'Νότος/Νοτιοανατολικά'},
                         'Abelha Mamangava': {'descricao': 'Αποκλειστικός επικονιαστής του πάσιφλορα. Χωρίς '
                                                           'αυτήν, η παραγωγή πάσιφλορα στη Βραζιλία θα '
                                                           "κατέρρεε. Χρησιμοποιεί την τεχνική 'buzz "
                                                           "pollination', δονώντας τα άνθη για να "
                                                           'απελευθερώσει τη γύρη. Χτίζει φωλιές σε ξερά '
                                                           'κλαδιά.',
                                              'habitat': 'Φωλιάζει σε νεκρό ξύλο',
                                              'polinizacao': 'Buzz pollination — δονεί για να απελευθερώσει '
                                                             'γύρη'},
                         'Abelha Carpinteira': {'descricao': 'Γένος Xylocopa με πάνω από 50 είδη στη '
                                                             "Βραζιλία. 'Carpinteira' (ξυλουργός) λόγω της "
                                                             'ικανότητάς της να σκάβει το ξύλο για φωλιές. '
                                                             'Σημαντικοί επικονιαστές σωληνωτών ανθέων. '
                                                             'Φωλιές σε ξενοδοχεία μελισσών με καλαμάκια από '
                                                             'μπαμπού.',
                                                'habitat': 'Ξερό ξύλο, μπαμπού',
                                                'polinizacao': 'Γενικός επικονιαστής — μεγάλη ανθική '
                                                               'ποικιλότητα'},
                         'Abelha Mascarada': {'descricao': 'Μικροσκοπική αλλά ουσιώδης. Μεταφέρει γύρη στον '
                                                           'πρόλοβο και όχι σε καλαθάκια γύρης. Μεταφέρουν '
                                                           'νέκταρ και γύρη στο εσωτερικό του σώματος. '
                                                           'Ανταποκρίνεται πολύ καλά σε ξενοδοχεία μελισσών '
                                                           'με καλαμάκια από χαρτί και μπαμπού διαμέτρου 5–6 '
                                                           'mm.',
                                              'habitat': 'Καλαμάκια, κούφια κλαδιά',
                                              'polinizacao': 'Μικρά και ανοιχτά άνθη'},
                         'Abelha Cortadeira': {'descricao': 'Κόβουν κομμάτια φύλλων για να χτίσουν τις '
                                                            'φωλιές τους — εξ ου και το όνομα. Θεωρούνται '
                                                            "'παράσιτα' αλλά είναι ουσιώδεις ιθαγενείς "
                                                            'επικονιαστές. Φωλιές σε τρύπες ξύλου (τρυπάνι '
                                                            '8–10 mm ιδανικό για ξενοδοχεία).',
                                               'habitat': 'Έδαφος, ξύλο, κομμένα φύλλα',
                                               'polinizacao': 'Ιθαγενή είδη — Cerrado, Ατλαντικός Δρυμός'},
                         'Abelha Nômade': {'descricao': 'Κλεπτοπαρασιτικές μέλισσες που γεννούν αυγά στις '
                                                        'φωλιές άλλων μοναχικών μελισσών. Μοιάζουν με σφήκες '
                                                        'αλλά είναι μέλισσες. Θεμελιώδεις για τη ρύθμιση των '
                                                        'πληθυσμών και τη διατήρηση της οικολογικής '
                                                        'ισορροπίας σε δασικά περιβάλλοντα.',
                                           'habitat': 'Παράσιτο σε φωλιές άλλων',
                                           'polinizacao': 'Έμμεση — διατηρεί την οικολογική ισορροπία'},
                         'Abelha Oleiro': {'descricao': 'Υποχρεωτικοί επικονιαστές των murici, barbatimão '
                                                        'και άλλων Malpighiaceae. Συλλέγουν ανθικό έλαιο από '
                                                        'τα άνθη για να τροφοδοτήσουν τις προνύμφες τους. '
                                                        'Φωλιές στο έδαφος. Δείκτες διατηρημένου Cerrado.',
                                           'habitat': 'Αμμώδες έδαφος, πρανή',
                                           'polinizacao': 'Buzzing σε άνθη με έλαιο — Malpighiaceae'}},
        'back_link': '← Portfolio',
        'lang_label': 'Γλώσσα',
        'cluster_name': 'Εμφανίσεις',
        'footer_copy': '© 2022–2026 · Παρατηρητήριο Meliponini · Βραζιλία',
        'raw_cols': {'especie': 'Είδος',
                     'cientifico': 'Επιστημονικό όνομα',
                     'tamanho': 'Μέγεθος',
                     'raio': 'Ακτίνα τροφοσυλλογής (m)',
                     'mel': 'Παραγωγή μελιού',
                     'iucn': 'IUCN',
                     'bioma': 'Βιότοπος',
                     'registros': 'Καταγραφές GBIF',
                     'colonia': 'Αποικία (εργ.)',
                     'mel_ano': 'Μέλι/έτος (kg)',
                     'habitat': 'Οικότοπος',
                     'polinizacao': 'Επικονίαση',
                     'tipo': 'Τύπος'},
        'tipo_vals': {'meli': 'Meliponini', 'sol': 'Μοναχική'},
        'tok_nd': 'χιλιάδες',
        'tok_and': ' και ',
        'tok_sp_top': 'Το SP συγκεντρώνει {n} καταγραφές GBIF — περισσότερες από οποιαδήποτε άλλη πολιτεία.',
        'tok_sp_plain': 'Το SP συγκεντρώνει {n} καταγραφές GBIF.',
        'tok_sp_generic': 'Το SP συγκαταλέγεται στις πολιτείες με την καλύτερη δειγματοληψία.'},
 'af': {'page_title': 'Meliponini-waarnemingsentrum · Brasilië',
        'hero_tag': 'BIODIVERSITEIT · MELIPONINI · BRASILIË · 2022–2025',
        'hero_title': 'Waarnemingsentrum vir\nAngellose Bye',
        'hero_subtitle': 'Monitering en ontleding van die verspreiding van inheemse angellose bye '
                         '(Meliponini) en solitêre bye in Brasilië — meer as 24.000 GBIF-rekords, 12 '
                         "gekarteerde spesies en aktiewe bewaring. Sluit 'n tegniese besoek aan Cidade das "
                         "Abelhas (SP, 2022) en 'n hotel vir solitêre bye by FATEC Jundiaí in.",
        'badge1': '🐝 12 gemonitorde spesies',
        'badge2': '🗺️ 300+ voorkomspunte',
        'badge3': 'Brasilië · 5 Biome',
        'badge4': 'GBIF · iNaturalist · INPA',
        'badge5': 'Eindprojek FATEC Jundiaí 2022',
        'm1': 'Meliponini-spesies',
        'm2': 'GBIF-rekords (2024)',
        'm3': 'Deelstate gedek',
        'm4': 'Bedreigde spesies',
        'tab1': '🗺️ Kaart & Ontleding',
        'tab2': '🔬 Metodologie & Pyplyn',
        'tab3': '💡 Ons Bevindings',
        'tab4': '📷 In die Veld',
        'tab5': '📈 Tendense',
        'tab6': '⚙️ Parameters',
        'tab7': '📋 Rou Data',
        'tab8': '📚 Bronne & Erkenning',
        'map_label': 'VERSPREIDING IN BRASILIË',
        'map_title': 'Voorkomskaart — Angellose Bye',
        'map_hint': '🐝 <strong>Klik op die merkers</strong> om spesie, bioom en bron te sien. Grootte ∝ '
                    'rekords per deelstaat. Skakel die trosse aan om groeperings te sien.',
        'heat_title': 'Hittekaart — Voorkomsdigtheid',
        'chart_label': 'VERGELYKENDE ONTLEDING',
        'sp_registros_title': 'Rekords per Spesie (GBIF, 2024)',
        'estado_title': 'Rekords per Deelstaat',
        'bioma_title': 'Verspreiding per Bioom',
        'method_label': 'TOEGEPASTE BIODIVERSITEIT',
        'method_title': 'Vraag & Metodologie',
        'sci_q_title': '❓ Sentrale Vraag',
        'sci_q': '"Wat is die huidige stand van die verspreiding en bewaring van Brasilië se inheemse '
                 'angellose bye, en hoe kan rasionele meliponikultuur en hotelle vir solitêre bye bydra tot '
                 'die behoud van hierdie spesies in stedelike en buitestedelike omgewings?"',
        'pipeline_label': 'DATAPYPLYN',
        'steps': [['1',
                   'Insameling — GBIF + iNaturalist (2010–2024)',
                   'Voorkomsdata van Brasiliaanse Meliponini via die GBIF-API en iNaturalist-uitvoer. '
                   '@@TOTAL@@ georeferensieerde rekords (2010–2024), gefiltreer sonder georuimtelike '
                   'probleme. Teikenspesies: 12 inheemse Meliponini + 6 solitêre bye.'],
                  ['2',
                   'Tegniese Besoek — Cidade das Abelhas (SP, 2022)',
                   'Tegniese besoek aan die Cidade das Abelhas-park in São Paulo vir direkte waarneming van '
                   'rasionele korwe van Jataí, Mosquitinho, Manduri, Mirim Preguiça en ander spesies. '
                   'Fotografiese rekord en dataversameling oor rasionele bestuur van meliponaria.'],
                  ['3',
                   'Eindprojek FATEC Jundiaí — Hotel vir Solitêre Bye (2022)',
                   "Studie-afsluitingsprojek: bou van 'n Hotel vir Solitêre Bye op die FATEC Jundiaí-kampus "
                   'vir die geleentheid Ciência na Praça. Houtstruktuur met 8 en 10 mm boorgate vir inheemse '
                   'solitêre bye soos Xylocopa sp. en Megachile sp.'],
                  ['4',
                   'Ruimtelike Ontleding — Verspreiding per Bioom',
                   'Kruising van die voorkomste met die IBGE-bioomvormlêer. Identifisering van patrone in '
                   'spesierykheid per bioom. Atlantiese Woud as die bioom met die grootste '
                   'Meliponini-diversiteit (~22 spesies).'],
                  ['5',
                   'Biologiese Parameters — Wetenskaplike Literatuur',
                   'Samestelling van data uit die literatuur: koloniegrootte, eierleggingsyfer, werkerlewe, '
                   'voedselsoekradius, heuningproduksie. Basis: A.B.E.L.H.A., Atlas da Meliponicultura, '
                   'publikasies van USP/UNICAMP/UFMG.'],
                  ['6',
                   'Bedreigingsassessering — IUCN Rooi Lys',
                   'Kruising van voorkomsdata met IUCN-status: @@VU@@ Kwesbare (VU) spesies, @@LC@@ met '
                   'Minste Kommer (LC). Ontleding van populasietendense en menslike druk per bioom.']],
        'biologia_title': '🐝 Waarom is Angellose Bye belangrik?',
        'biologia_text': '• <b>~550 spesies</b> Meliponini wêreldwyd beskryf · <b>~350 in Brasilië</b><br>• '
                         '<b>Eksklusiewe bestuiwers</b> van inheemse spesies van die Atlantiese Woud en '
                         'Cerrado<br>• <b>Heuning met medisinale eienskappe</b> erken deur ANVISA (Portaria '
                         '310/1997)<br>• <b>Meliponikultuur</b>: rasionele teling in INPA-, IBAMA-, JTB- en '
                         'Fernão Dias-kaste<br>• <b>Bedreigings:</b> ontbossing, plaagdoders, '
                         'verstedeliking, indringerspesies',
        'solitarias_title': '🏨 Solitêre Bye — Die Stille Meerderheid',
        'solitarias_text': '• <b>~70% van die wêreld se bye</b> is solitêr — sonder koningin, sonder '
                           'korf<br>• <b>Elke wyfie</b> bou haar eie nes, versamel kos en versorg die '
                           'eiers<br>• <b>Byehotelle</b> (houtblokke met gate van 6–10 mm) lok Xylocopa, '
                           'Megachile en Hylaeus<br>• <b>Ideale gate:</b> 8 mm-boor (Megachile), 10 mm-boor '
                           '(Xylocopa) — minimum diepte 10 cm<br>• <b>Installasie:</b> oriëntasie '
                           'Oos/Suidoos, hoogte 1–2 m, beskut teen direkte reën',
        'disc_label': 'ONTLEDING EN BEVINDINGS',
        'disc_title': 'Wat die Data Onthul Het',
        'discoveries': [['🐝',
                         'Jataí — die bes aangepas by verstedeliking',
                         'Tetragonisca angustula is die spesie met die grootste aanpasbaarheid by stedelike '
                         'omgewings. Rekords in alle Brasiliaanse deelstate en in al 5 biome. Nes in spleet '
                         "in messelwerk, elektriese kaste en pale. Haar teenwoordigheid in stede is 'n "
                         'aanduider van ekologiese veerkragtigheid.'],
                        ['⚠️',
                         '@@VU@@ Kwesbare spesies — @@VU_LIST@@',
                         'Die Melipona-spesies met die grootste liggaamsgrootte en heuningproduksie is die '
                         'meeste bedreig. Die kombinasie van ontbossing, menslike druk en lae voortplanting '
                         '(die koningin onderneem net 1 paringsvlug) maak hierdie spesies besonder kwesbaar '
                         'vir populasie-ineenstorting.'],
                        ['🏨',
                         'Byehotel — vermenigvuldiger van stedelike biodiversiteit',
                         'Die Byehotel wat by FATEC Jundiaí gebou is, het getoon dat eenvoudige '
                         'houtstrukture met boorgate van 8 en 10 mm binne 30–60 dae deur inheemse solitêre '
                         "spesies beset word. 'n Lae-koste-ingreep (<R$50) met groot impak op plaaslike "
                         'bestuiwing.'],
                        ['📊',
                         'São Paulo — Brasilië se meliponikultuurhoofstad',
                         '@@SP_SENT@@ Die kombinasie van oorblywende Atlantiese Woud, intensiewe '
                         'universiteitsnavorsing (USP, UNICAMP, UNESP) en groeiende stedelike '
                         'meliponikultuur verklaar hierdie vooraanstaande rol.'],
                        ['🌎',
                         'GBIF: @@GROWTH@@ in 10 jaar — burgerwetenskap as dryfkrag',
                         'Die groei van @@GROWTH_ABS@@ georeferensieerde Meliponini-rekords in Brasilië '
                         'tussen 2014 en 2024 (@@GROWTH@@) loop gelyk met die toenemende gebruik van '
                         'iNaturalist en burgers se belangstelling in biodiversiteit. Die groeiende '
                         'stedelike meliponikultuur is sowel gevolg as oorsaak van hierdie belangstelling.'],
                        ['🌿',
                         'Cerrado — onderbemonsterde bioom met groot verskuilde diversiteit',
                         'Ofskoon dit ~100 endemiese Meliponini-spesies huisves, is die Cerrado histories '
                         'onderbemonster in biodiversiteitsrekords. Die onderbemonstering weerspieël '
                         "navorsingsleemtes in afgeleë gebiede — 'n waarskuwing vir bewaring voordat die "
                         'bioom 100% gefragmenteer is.']],
        'conclusion_label': 'GEVOLGTREKKING',
        'conclusion_title': 'Elke Korf Tel',
        'conclusion_text': "Brasilië se inheemse angellose bye is 'n unieke biokulturele erfenis: duisende "
                           'jare lank deur inheemse volke gekweek, produseerders van heuning met medisinale '
                           'eienskappe en onvervangbare bestuiwers van ons inheemse flora. Die groei van '
                           '@@GROWTH_N@@ in die GBIF-rekords van Meliponini wys dat die belangstelling in '
                           'meliponikultuur toeneem — maar die tempo van ontbossing oortref steeds die spoed '
                           'van bewaring. Elke rasionele korf wat opgerig word, elke byehotel wat gebou '
                           "word, elke woudfragment wat beskerm word, is 'n vertrouensstem in die toekoms "
                           'van hierdie spesies.',
        'conclusion_author': 'Amauri Almeida · Eindprojek Omgewingsbestuur · FATEC Jundiaí · 2022 · Besoek '
                             'aan Cidade das Abelhas SP',
        'field_label': 'VELD- EN TEGNIESE REKORD',
        'field_title': 'Van Cidade das Abelhas tot die FATEC-kampus',
        'field_inst_title': "📁 Hoe om jou foto's by te voeg",
        'field_inst': "Plaas jou foto's in die gids <code>assets/campo/</code> met die presiese name "
                      'hieronder.',
        'photos': [{'emoji': '🐝',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Rasionele Korf — Jataí-by',
                    'esp': 'Tetragonisca angustula',
                    'desc': 'Rasionele korf (JTB- of INPA-kas) van die Jataí-by in die Cidade das '
                            'Abelhas-park, São Paulo. Die Jataí is die algemeenste en aanpasbaarste spesie '
                            'in Brasilië — sy nes natuurlik in spleet in messelwerk. Die rasionele korf maak '
                            'die verdeling van kolonies en bestuur moontlik sonder om die nes te vernietig.',
                    'path': 'assets/campo/01_colmeia_jatai_cidade_abelhas.jpg',
                    'legenda': 'Jataí-korf (Tetragonisca angustula) · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🔎',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Rasionele Korf — Mosquitinho-by',
                    'esp': 'Plebeia mosquito',
                    'desc': 'Rasionele korf van die Mosquitinho-by (Plebeia mosquito) — een van die kleinste '
                            'angellose bye in Brasilië (2 mm). Uiters mak en sensitief vir plaagdoders. Korf '
                            "met 'n heuningmodule geskei van die broeimodule — 'n fundamentele praktyk van "
                            'rasionele meliponikultuur om die kolonie nie te benadeel nie.',
                    'path': 'assets/campo/02_colmeia_mosquitinho_cidade_abelhas.jpg',
                    'legenda': 'Mosquitinho-korf (Plebeia mosquito) · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '🌿',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Rasionele Korf — Manduri-by (1)',
                    'esp': 'Melipona marginata',
                    'desc': 'Rasionele korf van die Manduri-by (Melipona marginata) — Kwesbare spesie (IUCN '
                            'VU). Een van die belangrikste spesies vir bewaring: skaars heuning, in klein '
                            'hoeveelhede geproduseer, nes uitsluitlik in holtes van inheemse bome. Rasionele '
                            'meliponikultuur is die vernaamste ex situ-bewaringstrategie vir hierdie spesie.',
                    'path': 'assets/campo/04_colmeia_manduri_cidade_abelhas_1.jpg',
                    'legenda': 'Manduri-korf (Melipona marginata) · Kwesbaar · Cidade das Abelhas · SP · '
                               '2022',
                    'gid': 'cidade'},
                   {'emoji': '🌿',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Rasionele Korf — Manduri-by (2)',
                    'esp': 'Melipona marginata',
                    'desc': 'Tweede gedokumenteerde Manduri-korf. Die opvolg van verskeie korwe van '
                            'dieselfde spesie maak dit moontlik om variasie in gedrag en produksie te '
                            'bestudeer. Die verskil in kleur en struktuur tussen kaste weerspieël '
                            'verskillende modelle van rasionele korwe — INPA, Fernão Dias, JTB en '
                            'USP-modelle.',
                    'path': 'assets/campo/05_colmeia_manduri_cidade_abelhas_2.jpg',
                    'legenda': 'Manduri-korf (2) · Melipona marginata · VU · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Rasionele Korf — Mirim Preguiça (1)',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'Rasionele korf van die Mirim Preguiça-by (Frieseomelitta varia) — so genoem '
                            'vanweë die rustige gedrag van die werkers by die korfingang. Belangrike spesie '
                            'vir die bestuiwing van inheemse spesies van die Cerrado en die Atlantiese Woud. '
                            'Bou neste in boomtakke.',
                    'path': 'assets/campo/06_colmeia_mirim_preguica_1.jpg',
                    'legenda': 'Mirim Preguiça-korf (Frieseomelitta varia) · Cidade das Abelhas · SP · 2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Rasionele Korf — Mirim Preguiça (2)',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'Tweede aansig van die Mirim Preguiça-korf. Die korfingang met die spesifieke '
                            'kenmerke van hierdie spesie is sigbaar. Die interne argitektuur van die nes, '
                            'met sferiese broeisels, verskil van dié van Melipona — wat spesifieke '
                            'aanpassings in die rasionele kaste vir hierdie spesie vereis.',
                    'path': 'assets/campo/07_colmeia_mirim_preguica_2.jpg',
                    'legenda': 'Mirim Preguiça-korf (2) · Frieseomelitta varia · Cidade das Abelhas · SP · '
                               '2022',
                    'gid': 'cidade'},
                   {'emoji': '😴',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Rasionele Korf — Mirim Preguiça (3)',
                    'esp': 'Frieseomelitta varia',
                    'desc': 'Derde hoek van die Mirim Preguiça-korf, wat besonderhede van die buitestruktuur '
                            'en die steun toon. Die dokumentering van veelvuldige aansigte is noodsaaklik by '
                            'tegniese besoeke om bestuurspatrone en korfontwerpe te identifiseer wat vir '
                            'elke spesie die beste werk.',
                    'path': 'assets/campo/08_colmeia_mirim_preguica_3.jpg',
                    'legenda': 'Mirim Preguiça-korf (3) · Frieseomelitta varia · Cidade das Abelhas · SP · '
                               '2022',
                    'gid': 'cidade'},
                   {'emoji': '🏛️',
                    'grupo': 'CIDADE DAS ABELHAS · SÃO PAULO · 2022',
                    'titulo': 'Meliponarium — Versameling van Verskillende Spesies',
                    'esp': 'Veelvuldige spesies',
                    'desc': 'Aansig van die meliponarium van die Cidade das Abelhas-park met rasionele kaste '
                            'van verskillende spesies langs mekaar — soos goeie meliponikultuurpraktyk '
                            'voorskryf. Elke spesie het sy eie geïdentifiseerde kas. Die tussenruimte tussen '
                            'korwe en die oriëntasie van die ingang is bereken om byedrywing te minimeer en '
                            'die gesondheid van die kolonies te maksimeer.',
                    'path': 'assets/campo/09_meliponario_colecao_cidade_abelhas.jpg',
                    'legenda': 'Meliponarium met verskillende spesies · Rasionele kaste · Cidade das '
                               'Abelhas-park · SP · 2022',
                    'destaque': True,
                    'gid': 'cidade'},
                   {'emoji': '🌳',
                    'grupo': 'BYEHOTEL · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Bou van die Hotel — Houtstruktuur',
                    'esp': 'Vir solitêre bye',
                    'desc': 'Begin van die bou van die Hotel vir Solitêre Bye op die FATEC Jundiaí-kampus. '
                            'Die houtstruktuur is die hoofsteun vir die geboorde blokke. Die keuse van hout '
                            '(behandelde dennehout of bloekom) is belangrik: dit moet bestand wees teen vog, '
                            'maar nie met biosiede behandel wees wat die bye wegjaag nie.',
                    'path': 'assets/campo/10_hotel_abelhas_estrutura_madeira.jpg',
                    'legenda': 'Bou van Byehotel · Houtstruktuur · FATEC Jundiaí · Ciência na Praça · 2022',
                    'gid': 'hotel'},
                   {'emoji': '🔩',
                    'grupo': 'BYEHOTEL · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Boor van die Blokke — 8 en 10 mm Boorpunte',
                    'esp': 'Vir solitêre bye',
                    'desc': "Boor van die houtblokke met 'n elektriese boor met 'n 8 mm-boorpunt (Megachile "
                            "sp., Hylaeus sp.) en 'n 10 mm-boorpunt (Xylocopa sp.). 'n Minimum diepte van 10 "
                            'cm is noodsaaklik sodat die wyfie die nes met 3–5 broeisels kan voltooi. Gate '
                            "moet in 'n blinde einde eindig — hulle mag nie deur die blok gaan nie.",
                    'path': 'assets/campo/11_hotel_abelhas_furadeira_broca8_10.jpg',
                    'legenda': 'Boor met 8 en 10 mm-boorpunte · Hotel vir Solitêre Bye · FATEC Jundiaí · '
                               '2022',
                    'gid': 'hotel'},
                   {'emoji': '🔩',
                    'grupo': 'BYEHOTEL · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Boorwerk in Besonderhede — 8 en 10 mm Boorpunte',
                    'esp': 'Vir solitêre bye',
                    'desc': 'Besonderhede van die boorproses met 8 en 10 mm-boorpunte. Eenvormige gate is '
                            'belangrik vir die sukses van die hotel: minimum diepte 10 cm, presiese deursnee '
                            "en gladde binneoppervlak (skuur indien nodig). Gate met 'n gekerfde binnekant "
                            'kan die deurgang van die bye verhinder.',
                    'path': 'assets/campo/12_hotel_abelhas_furos_detalhe.jpg',
                    'legenda': 'Besonderhede van gate 8/10 mm · Hotel vir Solitêre Bye · FATEC Jundiaí · '
                               '2022',
                    'gid': 'hotel'},
                   {'emoji': '✅',
                    'grupo': 'BYEHOTEL · FATEC JUNDIAÍ · 2022',
                    'titulo': 'Byehotel Voltooi — FATEC Jundiaí-kampus',
                    'esp': 'Vir solitêre bye',
                    'desc': 'Hotel vir Solitêre Bye voltooi en op die FATEC Jundiaí-kampus geïnstalleer vir '
                            'die geleentheid Ciência na Praça. Houtblokke met boorgate van 8 en 10 mm, '
                            "oriëntasie Oos/Suidoos, hoogte ~1,5 m, beskerm deur 'n dak teen reën. "
                            'Lae-koste-struktuur (<R$50) met groot impak op plaaslike bestuiwing.',
                    'path': 'assets/campo/13_hotel_abelhas_concluido_fatec_jundiai.jpg',
                    'legenda': 'Hotel vir Solitêre Bye voltooi · FATEC Jundiaí-kampus · Ciência na Praça · '
                               '2022',
                    'destaque_final': True,
                    'gid': 'hotel'}],
        'timeline_label': 'PROJEKTYDLYN',
        'timeline_items': [['2022 · Jan–Jun',
                            'Eindprojek Omgewingsbestuur — FATEC Jundiaí',
                            'Navorsing oor meliponikultuur en solitêre bye · Byehotel gebou vir Ciência na '
                            'Praça'],
                           ['2022 · Jul',
                            'Tegniese Besoek — Cidade das Abelhas SP',
                            'Fotografiese rekord van 8+ spesies in rasionele korwe · Jataí, Mosquitinho, '
                            'Manduri, Mirim Preguiça en ander'],
                           ['2022 · Nov',
                            'Verdediging van die Projek — FATEC Jundiaí',
                            'Goedkeuring van die eindwerkstuk in Omgewingsbestuur · Graad goedgekeur'],
                           ['2023–2024',
                            'GBIF-ontleding — @@TOTAL@@ rekords',
                            'Kruising van voorkomsdata met biome en deelstate · Identifisering van '
                            'bewaringsleemtes'],
                           ['2025',
                            'Publikasie in die Portefeulje',
                            'Meliponini-waarnemingsentrum van Brasilië — openbare dashboard met opgedateerde '
                            'data']],
        'trend_sel': 'Kies visualisering',
        'trend_opt1': 'GBIF-groei (2010–2024)',
        'trend_opt2': 'Rekords per Spesie (ranglys)',
        'trend_opt3': 'Rekords per Deelstaat',
        'param_sel': 'Spesie vir ontleding',
        'param_names': {'colonia': 'Koloniegrootte (werkers)',
                        'postura_dia': 'Eierleggingsyfer (eiers/dag)',
                        'vida_operaria': 'Werkerlewe (dae)',
                        'longe_formag': 'Voedselsoekradius (m)',
                        'prod_mel_kg': 'Heuningproduksie (kg/jaar)',
                        'raio_dna_km': 'Genetiese afstand (km)'},
        'raw_label': 'SPESIEKATALOGUS',
        'raw_title': 'Volledige Tabel — Meliponini van Brasilië',
        'download_csv': '⬇️ Laai CSV af',
        'sources_label': 'WETENSKAPLIKE BRONNE',
        'sources_title': 'Bronne & Databasis',
        'tech_label': 'TEGNOLOGIEË GEBRUIK',
        'footer_title': '🐝 Amauri Almeida',
        'footer_desc': 'Tegnoloog in Omgewingsbestuur · FATEC Jundiaí (3de ENADE)<br>Nagraadse studie in KI, '
                       'Masjienleer & Datawetenskap · Datawetenskap & Grootdata<br>Stelselontleding en '
                       '-ontwikkeling · FACINT Maringá',
        'footer_links': '📍 Fernandópolis · SP · Brasilië',
        'trend_label': 'TYDSONTWIKKELING & RANGLYSTE',
        'param_label': 'VERGELYKENDE BIOLOGIE',
        'param_title': 'Biologiese Parameters van die Spesies',
        'param_detail': 'Biologiese parameter',
        'param_cmp': 'Vergelyking tussen Spesies',
        'records_axis': 'Rekords',
        'records_hover': 'rekords',
        'gal_meli': 'SPESIEGALERY — MELIPONINI',
        'gal_sol': 'GALERY — SOLITÊRE BYE',
        'honey': 'Heuning',
        'mel_vals': {'Sim': 'Ja', 'Não': 'Nee', 'Pouco': 'Min'},
        'gbif_records': 'GBIF-rekords',
        'pop_records': 'Rekords',
        'pop_species': 'Spesies',
        'pop_status': 'Status',
        'status_vals': {'Alta': 'Hoog', 'Média': 'Medium', 'Baixa': 'Laag'},
        'radar_title': 'Vergelykende Profiel van die Spesies (skaal 0–10)',
        'radar_cats': ['Heuningproduksie',
                       'Stedelike aanpassing',
                       'Vlugradius',
                       'Koloniegrootte',
                       'IUCN (omgekeer)'],
        'grp_city': '🏛️ CIDADE DAS ABELHAS (BYESTAD) · SÃO PAULO · 2022',
        'grp_hotel': '🏨 HOTEL VIR SOLITÊRE BYE · FATEC JUNDIAÍ · CIÊNCIA NA PRAÇA · 2022',
        'dest_melipon': '⭐ UITLIG — VOLLEDIGE MELIPONARIUM · CIDADE DAS ABELHAS',
        'dest_hotel': '✅ SLOTUITLIG — HOTEL VOLTOOI · FATEC JUNDIAÍ-KAMPUS',
        'hotel_build_title': "🏗️ Hoe om 'n Hotel vir Solitêre Bye te bou",
        'hotel_build': [['Materiaal', 'Houtblok (behandelde dennehout of bloekom) · 15×10×10 cm minimum'],
                        ['Gate', '8 mm-boorpunt (Megachile, Hylaeus) · 10 mm-boorpunt (Xylocopa)'],
                        ['Diepte', 'Minimum 10 cm · Blinde einde (moenie deur die blok boor nie!)'],
                        ['Oriëntasie', 'Oos of Suidoos · Ontvang oggendson'],
                        ['Hoogte', '1–2 meter bo die grond · Beskut teen reën en wind'],
                        ['Resultaat', 'Besetting binne 30–60 dae deur inheemse bye']],
        'solitary_tbl': 'Solitêre Bye',
        'card_lbls': {'biome': 'Bioom',
                      'region': 'Streek',
                      'colony': 'Kolonie',
                      'workers': 'werkers',
                      'laying': 'Eierlegging',
                      'eggs_day': 'eiers/dag',
                      'worker_life': 'Werkerlewe',
                      'days': 'dae',
                      'forage': 'Voedselsoekradius',
                      'honey': 'Heuningproduksie',
                      'kg_year': 'kg/jaar',
                      'gen_dist': 'Genet. afstand'},
        'carto_fallback': 'Alternatiewe basiskaart (OpenStreetMap) in gebruik.',
        'occ_live': 'Werklike GBIF-punte (api.gbif.org): {n} georeferensieerde voorkomste in Brasilië, tot '
                    "{k} per spesie, nagevra op {d}. Klik op 'n punt om die oorspronklike rekord oop te "
                    'maak.',
        'occ_demo': 'GBIF is tans nie beskikbaar nie: die punte wat getoon word is ILLUSTRATIEF (hoofstede × '
                    'spesies) en nie veldrekords nie.',
        'occ_none': 'GBIF is tans nie beskikbaar nie en daar is geen rugsteundata nie: voorkomskaart word '
                    'nie vertoon nie.',
        'dados_live': 'Syfers bereken uit GBIF (api.gbif.org), nagevra op {d}; word elke 24 uur outomaties '
                      'opgedateer.',
        'dados_snapshot': 'GBIF is nou nie beskikbaar nie: syfers uit die laaste gestoorde momentopname '
                          '({d}).',
        'dados_static': "GBIF is nou nie beskikbaar nie: verwysingswaardes uit 'n vroeëre samestelling, nie "
                        'opgedateer nie.',
        'serie_total': 'Totaal (Meliponini + 5 solitêre genera)',
        'serie_inat': 'iNaturalist (Meliponini)',
        'raio_sel': 'Wys voedselsoekradius (sirkels in meter)',
        'raio_note': 'Elke sirkel toon die spesie se gemiddelde vlugradius rondom werklike voorkomste (tot '
                     '{n} per spesie). Zoem die kaart in om die skaal te sien.',
        'raio_layer': 'Voedselsoekradius',
        'footer_portfolio': 'Portefeulje',
        'sources': [['GBIF',
                     'GBIF — Global Biodiversity Information Facility',
                     'gbif.org · Voorkomsdatabasis met @@TOTAL@@ georeferensieerde Meliponini-rekords in '
                     'Brasilië (2010–2024). Data van museums, herbaria, iNaturalist en navorsers.',
                     '#C47D0E'],
                    ['A.B.E.L.H.A.',
                     'A.B.E.L.H.A. — Brasiliaanse Vereniging vir die Studie van Bye',
                     'abelha.org.br · Atlas van Angellose Byeboerdery in Brasilië. Verwysing vir '
                     'voedselsoekradiusse, biologie en bewaring.',
                     '#C0390A'],
                    ['INATURALIST',
                     'iNaturalist — Wêreldwye Burgerwetenskap',
                     'inaturalist.org · @@INAT@@ georeferensieerde rekords van Brasiliaanse Meliponini '
                     '(iNaturalist Research-grade-datastel op GBIF). Vernaamste dryfkrag van die groei van '
                     'GBIF.',
                     '#2D7A45'],
                    ['FATEC',
                     'FATEC Jundiaí — Eindprojek Omgewingsbestuur (2022)',
                     'Hotel vir Solitêre Bye op die kampus gebou vir die geleentheid Ciência na Praça. 8 en '
                     '10 mm-boorpunte. Met lof goedgekeur.',
                     '#1B3A1E'],
                    ['CIDADE ABELHAS',
                     'Cidade das Abelhas-park — São Paulo (2022)',
                     'Tegniese besoek in 2022. Fotografiese rekord van rasionele korwe van Jataí, '
                     'Mosquitinho, Manduri, Mirim Preguiça en ander.',
                     '#5C3D1E'],
                    ['IUCN',
                     'IUCN Rooi Lys — Lys van Bedreigde Spesies',
                     '@@VU_TAGS@@. Bewaringstatus van die Brasiliaanse Meliponini.',
                     '#8B2515'],
                    ['INPA',
                     'INPA — Nasionale Instituut vir Amasone-navorsing',
                     'INPA-model van rasionele korf vir Amasone-Meliponini. Spesiedata uit Noord-Brasilië.',
                     '#0D4E72'],
                    ['EMBRAPA',
                     'EMBRAPA Cerrados / EMBRAPA Amazônia Oriental',
                     'Data oor angellose byeboerdery in Brasiliaanse biome. Tegniese verwysing vir spesies '
                     'van die Cerrado en die Amasone.',
                     '#C47D0E']],
        'species_text': {'Jataí': {'descricao': 'Die bekendste angellose by in Brasilië. Produseer heuning '
                                                'van uitsonderlike gehalte met medisinale eienskappe. Neste '
                                                'in boomholtes en spleet in messelwerk. Die ingang word met '
                                                "propolis in 'n buis of pastilles verseël.",
                                   'bioma': 'Almal',
                                   'regiao': 'Nasionaal'},
                         'Mosquitinho': {'descricao': 'Een van die kleinste angellose bye in Brasilië. '
                                                      'Uiters mak. Baie smaaklike heuning, in klein '
                                                      'hoeveelhede geproduseer. Baie sensitief vir die '
                                                      'gebruik van plaagdoders. Aanduider van '
                                                      'omgewingsgehalte.',
                                         'bioma': 'Atlantiese Woud',
                                         'regiao': 'Suid/Suidoos'},
                         'Manduri': {'descricao': 'Spesie wat met uitsterwing bedreig word (VU). Skaars '
                                                  'heuning, in klein hoeveelhede geproduseer. Neste '
                                                  'gewoonlik in holtes van inheemse bome. Teikenspesie van '
                                                  'meliponikultuurprogramme vir bewaring.',
                                     'bioma': 'Atlantiese Woud',
                                     'regiao': 'Suid/Suidoos'},
                         'Mirim Preguiça': {'descricao': 'Word ook die Luiaardby genoem vanweë haar rustige '
                                                         'gedrag. Nes hoofsaaklik in boomtakke. Belangrike '
                                                         'bestuiwer van inheemse spesies van die Cerrado en '
                                                         'die Atlantiese Woud.',
                                            'bioma': 'Cerrado/Atlantiese Woud',
                                            'regiao': 'Sentraal/Suidoos'},
                         'Mandaçaia': {'descricao': 'Een van die grootste angellose bye. Onderskeidende '
                                                    'heuningproduksie. In afname weens ontbossing en '
                                                    'verstedeliking. Al eeue lank deur die '
                                                    "Guarani-inboorlinge as 'mborí' aangehou.",
                                       'bioma': 'Atlantiese Woud',
                                       'regiao': 'Suidoos/Suid'},
                         'Uruçu Nordestina': {'descricao': 'Heilige by van die Tupinambá, al meer as 2.000 '
                                                           'jaar lank gekweek. Heuning met erkende '
                                                           'medisinale eienskappe. Simbool van '
                                                           'meliponikultuur in die Noordooste. '
                                                           'Vlagskipspesie van inheemse byeboerdery.',
                                              'bioma': 'Caatinga/Atlantiese Woud NO',
                                              'regiao': 'Noordoos'},
                         'Irapuá': {'descricao': 'Ofskoon sy nie heuning in kommersiële hoeveelhede '
                                                 "produseer nie, is sy 'n uiters belangrike bestuiwer. Bou "
                                                 'oop neste met plantharse. Word soms weens haar '
                                                 'verdedigende gedrag met die Europese heuningby verwar.',
                                    'bioma': 'Almal',
                                    'regiao': 'Nasionaal'},
                         'Tiúba': {'descricao': "Bekend as 'Abelha da Terra' (Grondby) in Maranhão. Heuning "
                                                "met 'n unieke geur, hoog op prys gestel. Fundamentele deel "
                                                'van die meliponikultuur van die Amasone en Maranhão. Spesie '
                                                'onder bedreiging weens ontbossing.',
                                   'bioma': 'Amasone/Noordoos',
                                   'regiao': 'Noord/Noordoos'},
                         'Guaraipo': {'descricao': "Spesie met 'n wisselende kleurpatroon. Heuningproduksie "
                                                   "met 'n sagte geur. Neste in die grond of in stamme. In "
                                                   'skerp afname weens die uitbreiding van landbou en '
                                                   'veeteelt in die Cerrado.',
                                      'bioma': 'Cerrado/Atlantiese Woud',
                                      'regiao': 'Sentraal-Wes/Suidoos'},
                         'Iraí': {'descricao': 'By wat baie algemeen in stedelike omgewings voorkom. Nes in '
                                               'spleet in mure, kragkaste en dakteëls. Baie verdraagsaam '
                                               'teenoor verstedeliking. Uitstekende aanduider van die '
                                               'konnektiwiteit van woudfragmente.',
                                  'bioma': 'Cerrado/Atlantiese Woud',
                                  'regiao': 'Suidoos'},
                         'Tubuna': {'descricao': 'Produseerder van donker, intense heuning. Neste in '
                                                 'boomholtes. Baie sensitief vir ontbossing. Word in '
                                                 'restourasieprojekte van woudfragmente as sleutelbestuiwer '
                                                 'gebruik.',
                                    'bioma': 'Atlantiese Woud',
                                    'regiao': 'Suidoos/Suid'},
                         'Mirim Guaçu': {'descricao': 'Koueweerstandige spesie. Baie algemeen in Santa '
                                                      'Catarina en Rio Grande do Sul. Bestuiwer van inheemse '
                                                      'en gekweekte spesies van die Suidelike streek. '
                                                      "Heuning met 'n kenmerkende suur geur.",
                                         'bioma': 'Suid/Suidoos',
                                         'regiao': 'Suid/Suidoos'},
                         'Abelha Mamangava': {'descricao': 'Eksklusiewe bestuiwer van die grenadella. Sonder '
                                                           'haar sou grenadellaproduksie in Brasilië '
                                                           "ineenstort. Gebruik die tegniek van 'buzz "
                                                           "pollination' deur die blomme te laat vibreer om "
                                                           'die stuifmeel los te maak. Bou neste in droë '
                                                           'takke.',
                                              'habitat': 'Nes in dooie hout',
                                              'polinizacao': 'Buzz pollination — vibreer om stuifmeel los te '
                                                             'maak'},
                         'Abelha Carpinteira': {'descricao': 'Genus Xylocopa met meer as 50 spesies in '
                                                             "Brasilië. 'Timmerman' vanweë haar vermoë om "
                                                             'hout vir neste uit te grawe. Belangrike '
                                                             'bestuiwers van buisvormige blomme. Neste in '
                                                             'byehotelle met bamboesstrooitjies.',
                                                'habitat': 'Droë hout, bamboes',
                                                'polinizacao': 'Generalis — hoë blomdiversiteit'},
                         'Abelha Mascarada': {'descricao': 'Piepklein maar noodsaaklik. Dra stuifmeel in die '
                                                           'krop, nie in korbikulas nie. Dra nektar en '
                                                           'stuifmeel intern. Reageer baie goed op '
                                                           'byehotelle met papier- en bamboesstrooitjies met '
                                                           "'n deursnee van 5–6 mm.",
                                              'habitat': 'Strooitjies, hol takke',
                                              'polinizacao': 'Klein, oop blomme'},
                         'Abelha Cortadeira': {'descricao': 'Sny stukkies blare af om hul neste te bou — '
                                                            "vandaar die naam. Word as 'plae' beskou, maar "
                                                            'is noodsaaklike inheemse bestuiwers. Neste in '
                                                            'gate in hout (8–10 mm-boor ideaal vir hotelle).',
                                               'habitat': 'Grond, hout, afgesnyde blare',
                                               'polinizacao': 'Inheemse spesies — Cerrado, Atlantiese Woud'},
                         'Abelha Nômade': {'descricao': 'Kleptoparasitiese bye wat eiers in die neste van '
                                                        'ander solitêre bye lê. Lyk soos wespe, maar is bye. '
                                                        'Fundamenteel om populasies te reguleer en '
                                                        'ekologiese balans in woudomgewings te handhaaf.',
                                           'habitat': 'Parasiet in ander neste',
                                           'polinizacao': 'Indirek — handhaaf ekologiese balans'},
                         'Abelha Oleiro': {'descricao': 'Verpligte bestuiwers van murici, barbatimão en '
                                                        'ander Malpighiaceae. Versamel blomolie van die '
                                                        'blomme om hul larwes te voed. Neste in die grond. '
                                                        'Aanduiders van bewaarde Cerrado.',
                                           'habitat': 'Sanderige grond, rotswande',
                                           'polinizacao': 'Buzzing op oliеblomme — Malpighiaceae'}},
        'back_link': '← Portefeulje',
        'lang_label': 'Taal',
        'cluster_name': 'Voorkomste',
        'footer_copy': '© 2022–2026 · Meliponini-waarnemingsentrum · Brasilië',
        'raw_cols': {'especie': 'Spesie',
                     'cientifico': 'Wetenskaplike Naam',
                     'tamanho': 'Grootte',
                     'raio': 'Voedselsoekradius (m)',
                     'mel': 'Heuningproduksie',
                     'iucn': 'IUCN',
                     'bioma': 'Bioom',
                     'registros': 'GBIF-rekords',
                     'colonia': 'Kolonie (werk.)',
                     'mel_ano': 'Heuning/jaar (kg)',
                     'habitat': 'Habitat',
                     'polinizacao': 'Bestuiwing',
                     'tipo': 'Tipe'},
        'tipo_vals': {'meli': 'Meliponini', 'sol': 'Solitêr'},
        'tok_nd': 'duisende',
        'tok_and': ' en ',
        'tok_sp_top': 'SP konsentreer {n} GBIF-rekords — meer as enige ander deelstaat.',
        'tok_sp_plain': 'SP konsentreer {n} GBIF-rekords.',
        'tok_sp_generic': 'SP is onder die deelstate wat die beste bemonster is.'}}
