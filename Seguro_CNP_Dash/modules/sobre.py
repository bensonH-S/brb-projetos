# modules/sobre.py
import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc

# Layout da página "Sobre"
layout = html.Div([
    # Título principal com a versão
    html.H3("Sobre a Aplicação", className="text-center mb-2",
            style={"fontSize": "32px", "fontWeight": "bold", "color": "#023e7c", "marginTop": "20px"}),
    html.P("Versão: v100.01", className="text-center mb-3",
           style={"color": "#023e7c", "fontWeight": "bold", "fontSize": "18px"}),
    html.P("Desenvolvido por Benson Henrique (Matrícula: u512228), com assistência da IA Grok, criada por xAI.",
           className="text-center mb-4", style={"color": "#666", "fontStyle": "italic"}),

    # Dropdown para selecionar o tipo de documentação
    html.P("Selecione o tipo de documentação que deseja visualizar:", style={"color": "#666", "marginBottom": "10px"}),
    dcc.Dropdown(
        id="doc-type-dropdown",
        options=[
            {"label": "Diagrama e Estrutura do Banco de Dados", "value": "banco_dados"},
            {"label": "Informação Técnica", "value": "info_tecnica"},
            {"label": "Manual de Uso", "value": "manual_uso"},
        ],
        value="banco_dados",  # Valor padrão
        style={"width": "50%", "marginBottom": "20px"}
    ),
    html.Div(id="doc-content", className="mb-4", style={"border": "2px solid #023e7c", "borderRadius": "10px", "padding": "15px"}),
])

# Callback para atualizar o conteúdo com base na escolha do dropdown
@dash.callback(
    Output("doc-content", "children"),
    [Input("doc-type-dropdown", "value")]
)
def update_doc_content(doc_type):
    if doc_type == "banco_dados":
        return [
            html.H4("Diagrama, Modelagem e Estrutura do Banco de Dados", className="mb-3",
                    style={"fontSize": "26px", "fontWeight": "bold", "color": "#023e7c"}),
            html.P("Esta seção descreve a estrutura do banco de dados MySQL usado na aplicação Seguro CNP Dash.", style={"color": "#666"}),
            html.Hr(),

            # Diagrama do Banco de Dados
            html.H5("Diagrama de Relacionamento", style={"color": "#023e7c"}),
            html.P("O diagrama abaixo mostra as tabelas do banco de dados e seus relacionamentos:", style={"color": "#666"}),
            # Placeholder para a imagem do diagrama (salve a imagem como 'diagrama_banco.png' na pasta assets)
            html.Img(src="/assets/imagens/diagrama.png", style={"width": "80%", "margin": "0 auto", "display": "block"}),
            html.P("Descrição do diagrama:", style={"color": "#666"}),
            html.Ul([
                html.Li("cnp_data: Armazena informações básicas dos CNPs (cnp, cnpj, razao_social, etc.)."),
                html.Li("seguradora: Contém detalhes dos seguros (cnp, inicio_vigencia_seguro, vencimento, valor_cobertura, etc.)."),
                html.Li("pag_seguradora: Registra os pagamentos dos seguros (cnp, numero_parcela, status)."),
                html.Li("cnp_historico: Armazena o histórico mensal de produção dos CNPs (cnp, jan_23, fev_23, ..., dez_25)."),
                html.Li("Relacionamentos: A chave primária 'cnp' da tabela cnp_data é usada como chave estrangeira nas tabelas seguradora, pag_seguradora e cnp_historico."),
            ], style={"color": "#666"}),

            # Estrutura das Tabelas
            html.H5("Estrutura das Tabelas", style={"color": "#023e7c"}),
            html.P("Detalhes das colunas de cada tabela:", style={"color": "#666"}),
            html.Ul([
                html.Li("cnp_data: cnp (int, PK), cnpj (varchar), razao_social (varchar), situacao (varchar), telefone (varchar), email (varchar), endereco (varchar), bairro (varchar), cidade (varchar), uf (char), cep (varchar), latitude (float), longitude (float), observacao (text)."),
                html.Li("seguradora: cnp (int, FK), inicio_vigencia_seguro (date), vencimento (date), valor_cobertura (decimal), valor_proposto (decimal), valor_parcela (decimal), forma_de_pgt (varchar), situacao_proposta (varchar), obs (text), apolice (varchar), multisseguros (varchar)."),
                html.Li("pag_seguradora: id (int, PK), cnp (int, FK), numero_parcela (int), data_vencimento (date), data_pagamento (date), status (varchar), usuario_ied (varchar)."),
                html.Li("cnp_historico: cnp (int, FK), jan_23 (decimal), fev_23 (decimal), ..., dez_25 (decimal)."),
            ], style={"color": "#666"}),

            # Como o Banco Funciona
            html.H5("Como o Banco de Dados Funciona", style={"color": "#023e7c"}),
            html.P("O banco de dados MySQL é usado para armazenar e gerenciar os dados da aplicação. Algumas características:", style={"color": "#666"}),
            html.Ul([
                html.Li("Conexão: A aplicação se conecta ao MySQL usando SQLAlchemy com o driver mysql-connector-python."),
                html.Li("Acesso Remoto: O MySQL pode ser configurado para aceitar conexões remotas, ajustando o bind-address e criando um usuário remoto."),
                html.Li("Segurança: Recomenda-se usar senhas fortes, configurar SSL para criptografar conexões, e restringir o acesso por IP."),
                html.Li("Manutenção: Índices são usados na coluna 'cnp' para melhorar a performance das consultas. Backups regulares devem ser realizados."),
            ], style={"color": "#666"}),
        ]

    elif doc_type == "info_tecnica":
        return [
            html.H4("Informação Técnica", className="mb-3",
                    style={"fontSize": "26px", "fontWeight": "bold", "color": "#023e7c"}),
            html.P("Esta seção contém informações técnicas detalhadas sobre a aplicação Seguro CNP Dash.", style={"color": "#666"}),
            html.Hr(),

            # Tecnologias Utilizadas
            html.H5("Tecnologias Utilizadas", style={"color": "#023e7c"}),
            html.Ul([
                html.Li("Python 3.9+: Linguagem principal para lógica da aplicação e ETL."),
                html.Li("Dash 2.17.1: Framework para criação do dashboard interativo."),
                html.Li("Plotly 5.22.0: Para gráficos interativos (barras, donut, linhas)."),
                html.Li("Pandas 2.2.2: Para manipulação de dados no ETL e dashboard."),
                html.Li("MySQL 8.0+: Banco de dados relacional."),
                html.Li("SQLAlchemy 2.0.31: Para conexão entre Python e MySQL."),
                html.Li("Dash Bootstrap Components 1.6.0: Para estilização e layout responsivo."),
                html.Li("mysql-connector-python 8.4.0: Driver para conexão com MySQL."),
            ], style={"color": "#666"}),
            html.P("Recomenda-se usar as versões listadas para evitar problemas de compatibilidade.", style={"color": "#666"}),

            # Estrutura do Projeto
            html.H5("Estrutura do Projeto", style={"color": "#023e7c"}),
            html.P("A estrutura de pastas do projeto é a seguinte:", style={"color": "#666"}),
            html.Pre("""
Seguro_CNP/
│── app.py                   # Arquivo principal da aplicação Dash
│── requirements.txt         # Lista de dependências
│── config.py                # Configurações globais
│── run.py                   # Script para iniciar a aplicação
│
├── assets/                  # Arquivos estáticos (CSS, imagens, etc.)
│
├── data/                    
│   ├── input/               # Arquivos de entrada (Excel, CSV)
│   ├── output/              # Arquivos gerados (logs, exportações)
│
├── etl/                     # Processamento de dados
│   ├── etl.py               # Script ETL principal
│
├── database/                
│   ├── db_init.py           # Script para inicializar o banco de dados
│   ├── connection.py        # Script para conexão com o banco
│
├── modules/                 # Componentes modulares da aplicação
│   ├── dashboard.py         # Página do dashboard
│   ├── cnps.py              # Página de cadastro e edição de CNPs
│   ├── seguro.py            # Página de seguros
│   ├── relatorios.py        # Página de relatórios
│   ├── etl_page.py          # Interface para executar o pipeline de ETL
│   ├── sobre.py             # Documentação e manual de uso (esta página)
│   └── __init__.py
│
├── logs/                    # Armazena logs da aplicação
│
└── venv/                    # Ambiente virtual (não incluso no controle de versão)
            """, style={"color": "#666", "backgroundColor": "#f8f9fa", "padding": "10px", "borderRadius": "5px"}),
            html.P("Descrição dos arquivos:", style={"color": "#666"}),
            html.Ul([
                html.Li("app.py: Ponto de entrada da aplicação, gerencia as rotas e o menu lateral."),
                html.Li("requirements.txt: Lista de dependências do projeto, usada para instalar as bibliotecas necessárias."),
                html.Li("config.py: Contém configurações globais, como portas, URLs de conexão, e outras variáveis de ambiente."),
                html.Li("run.py: Script para iniciar a aplicação, geralmente usado em produção."),
                html.Li("etl/etl.py: Script do pipeline de ETL (extração, transformação, carregamento)."),
                html.Li("database/db_init.py: Script para inicializar o banco de dados, criando tabelas e inserindo dados iniciais, se necessário."),
                html.Li("database/connection.py: Configuração da conexão com o MySQL, usando SQLAlchemy."),
                html.Li("modules/dashboard.py: Contém o dashboard principal com gráficos e tabelas interativas."),
                html.Li("modules/cnps.py: Gerenciamento de informações dos CNPs, como cadastro e edição."),
                html.Li("modules/seguro.py: Detalhes dos seguros, incluindo vigência e valores."),
                html.Li("modules/relatorios.py: Geração de relatórios personalizados."),
                html.Li("modules/etl_page.py: Interface para executar o pipeline de ETL."),
                html.Li("modules/sobre.py: Documentação e manual de uso (esta página)."),
                html.Li("assets/: Contém arquivos estáticos, como imagens (ex.: logo do BRB, diagrama do banco)."),
                html.Li("data/input/: Armazena arquivos de entrada, como Excel ou CSV, usados no ETL (se aplicável)."),
                html.Li("data/output/: Armazena arquivos gerados, como logs ou exportações do dashboard."),
                html.Li("logs/: Diretório para armazenar logs da aplicação, úteis para depuração."),
                html.Li("venv/: Ambiente virtual do Python, não incluído no controle de versão."),
            ], style={"color": "#666"}),

            # Pipeline do Projeto
            html.H5("Pipeline do Projeto", style={"color": "#023e7c"}),
            html.P("O pipeline de ETL (Extração, Transformação, Carregamento) é implementado no arquivo etl.py:", style={"color": "#666"}),
            html.Ul([
                html.Li("Extração: Os dados são extraídos do MySQL (tabelas cnp_data, seguradora, pag_seguradora, cnp_historico) usando SQLAlchemy."),
                html.Li("Transformação: Os dados são processados com Pandas, incluindo formatação de datas (ex.: de 'YYYY-MM-DD' para 'DD/MM/YYYY'), "
                        "conversão de valores monetários (ex.: formatar como R$ 1.234,56) e cálculo de métricas (ex.: média dos últimos 12 meses)."),
                html.Li("Carregamento: Os dados transformados são salvos em arquivos CSV (ex.: dados_transformados.csv, historico_transformado.csv) "
                        "e usados pelo dashboard."),
            ], style={"color": "#666"}),
            html.P("Boas práticas no ETL:", style={"color": "#666"}),
            html.Ul([
                html.Li("Validação de dados: Verifica se as tabelas estão vazias antes de processar."),
                html.Li("Logging: Usa a biblioteca logging para registrar erros e progresso do ETL."),
                html.Li("Tratamento de erros: Inclui try/except para lidar com falhas na conexão ou nos dados."),
            ], style={"color": "#666"}),

            # Trechos de Código
            html.H5("Trechos de Código Importantes", style={"color": "#023e7c"}),
            html.P("Abaixo estão alguns trechos de código importantes da aplicação:", style={"color": "#666"}),
            html.H6("Conexão com o MySQL (database/connection.py)", style={"color": "#023e7c"}),
            html.Pre("""
from sqlalchemy import create_engine

DATABASE_URL = "mysql+mysqlconnector://usuario:senha@localhost:3306/seguro_cnp"
engine = create_engine(DATABASE_URL)
            """, style={"color": "#666", "backgroundColor": "#f8f9fa", "padding": "10px", "borderRadius": "5px"}),
            html.H6("Imports no app.py", style={"color": "#023e7c"}),
            html.Pre("""
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from modules import dashboard, cnps, seguro, relatorios, etl_page, sobre
import logging
            """, style={"color": "#666", "backgroundColor": "#f8f9fa", "padding": "10px", "borderRadius": "5px"}),
            html.H6("Callback no dashboard.py (exemplo)", style={"color": "#023e7c"}),
            html.Pre("""
@dash.callback(
    Output("graph-top-cnps", "figure"),
    [Input("filtro-busca", "value")]
)
def update_graph_top_cnps(search_value):
    # Lógica para atualizar o gráfico
    return figure
            """, style={"color": "#666", "backgroundColor": "#f8f9fa", "padding": "10px", "borderRadius": "5px"}),
        ]

    elif doc_type == "manual_uso":
        return [
            html.H4("Manual de Uso", className="mb-3",
                    style={"fontSize": "26px", "fontWeight": "bold", "color": "#023e7c"}),
            html.P("Este manual explica como usar a aplicação Seguro CNP Dash de forma eficiente.", style={"color": "#666"}),
            html.Hr(),

            # Introdução
            html.H5("Introdução", style={"color": "#023e7c"}),
            html.P("A aplicação Seguro CNP Dash foi desenvolvida para gerenciar informações de seguros de CNPs, "
                   "oferecendo um dashboard interativo, relatórios e um pipeline de ETL para atualização de dados.", style={"color": "#666"}),

            # Navegação
            html.H5("Navegação", style={"color": "#023e7c"}),
            html.P("Use o menu lateral para acessar as diferentes seções da aplicação:", style={"color": "#666"}),
            html.Ul([
                html.Li("Dashboard: visualize métricas e gráficos gerais, como os top 5 CNPs e a evolução de produção."),
                html.Li("CNPs: gerencie informações dos CNPs, como razão social, endereço e contato."),
                html.Li("Seguro: consulte detalhes dos seguros, incluindo datas de vigência e valores."),
                html.Li("Relatórios: gere relatórios personalizados com base nos dados disponíveis."),
                html.Li("Executar ETL: atualize os dados do dashboard com informações recentes do banco de dados."),
                html.Li("Sobre: acesse informações sobre a aplicação (você está aqui)."),
            ], style={"color": "#666"}),
            # Placeholder para imagem (ex.: captura de tela do menu lateral)
            html.P("Imagem: Menu lateral da aplicação", style={"color": "#666"}),
            html.Img(src="/assets/menu_lateral.png", style={"width": "50%", "margin": "0 auto", "display": "block"}),

            # Como Executar o ETL
            html.H5("Como Executar o ETL", style={"color": "#023e7c"}),
            html.P("Na aba 'Executar ETL', siga os passos abaixo:", style={"color": "#666"}),
            html.Ol([
                html.Li("Clique na aba 'Executar ETL' no menu lateral."),
                html.Li("Clique no botão 'Executar ETL' para iniciar o processo."),
                html.Li("Aguarde a mensagem de confirmação (ex.: 'ETL executado com sucesso!')."),
                html.Li("Volte ao Dashboard para visualizar os dados atualizados."),
            ], style={"color": "#666"}),
            # Placeholder para imagem (ex.: captura de tela da aba ETL)
            html.P("Imagem: Aba Executar ETL", style={"color": "#666"}),
            html.Img(src="/assets/aba_etl.png", style={"width": "50%", "margin": "0 auto", "display": "block"}),

            # Regras para Contratação e Gerenciamento do Seguro
            html.H5("Regras para Contratação e Gerenciamento do Seguro", style={"color": "#023e7c"}),
            html.P("Esta seção detalha as regras e procedimentos para a contratação e gerenciamento do seguro dos CNPs.", style={"color": "#666"}),
            html.Ul([
                html.Li("O valor de cobertura é definido pelo Banco, levando-se em conta sua média de movimentação financeira diária, referente aos últimos 12 (doze) meses."),
                html.Li("Algumas regras devem ser observadas para a contratação do seguro:"),
                html.Ul([
                    html.Li("Capital segurado: R$ 100.000,00 (Cem mil reais):"),
                    html.Ul([
                        html.Li("Valor de cobertura destinada a novos CNPs, uma vez que ainda não há registros de transações para que possa ser realizado o cálculo da média de movimentação financeira. Entende-se por Correspondentes Novos aqueles que nunca operaram como Conveniência BRB ou ainda aquelas áreas no qual nunca houve Correspondentes."),
                        html.Li("Para os CNPs que encontram-se em atividade, este valor de cobertura somente será permitida se a média de movimentação de numerário for entre R$ 70.000,00 e R$ 100.000,00 (cem mil reais)."),
                    ]),
                    html.Li("Capital segurado: R$ 70.000,00 (Setenta mil reais):"),
                    html.Ul([
                        html.Li("Para este tipo de cobertura de seguro, a média de movimentação do CNP deve estar inferior ao valor de R$ 70.000,00 (Setenta mil reais)."),
                    ]),
                    html.Li("Capital segurado: R$ 150.000,00 (Cento e cinquenta mil reais):"),
                    html.Ul([
                        html.Li("Para este tipo de cobertura de seguro, a média de movimentação do CNP deve estar entre os valores de R$ 100.000,00 (Cem mil reais) a R$ 150.000,00 (Cento e cinquenta mil reais)."),
                    ]),
                    html.Li("Capital segurado: R$ 200.000,00 (Duzentos mil reais):"),
                    html.Ul([
                        html.Li("Para este tipo de cobertura, a média de movimentação do CNP deve ser superior ao valor de R$ 150.000,00 (Cento e cinquenta mil reais)."),
                    ]),
                ]),
                html.Li("O valor de cobertura é calculado pela GECOR e comunicado à Corretora de Seguros. Para definição do valor de cobertura de cada Correspondente, leva-se em conta sua média de movimentação financeira diária, referente aos últimos 12 (doze) meses. O cálculo considera a seguinte fórmula: {Recolhimentos - [36602 (Cheques de malotes) - 3160 (Créditos de agências)] / 22 = movimentação financeira do CNP}."),
                html.Li("Para novos contratos referentes a correspondentes existentes e que possuem movimentação registrada, o valor da cobertura do seguro não poderá ser iniciado em R$ 100.000,00 (cem mil reais). Nesse caso, considera-se a média de movimentação do correspondente."),
                html.Li("Caso o valor do seguro não seja suficiente para cobrir o valor sinistrado, a empresa deve recolher ao Banco a diferença devida, observadas as condições ajustadas contratualmente e previstas neste Manual."),
                html.Li("Compete ainda, à Conveniência BRB, realizar anualmente por ocasião do vencimento, a renovação do seguro contratado assim como efetuar os endossos necessários, comunicando à Seguradora a ocorrência de quaisquer eventos ou alterações ocorridas na respectiva apólice."),
                html.Li("Nos casos de perdas não cobertas pelo seguro, indenização paga pela seguradora não suficiente para cobrir o valor sinistrado, diferenças de caixa e valores oriundos de sinistros não regularizados no prazo contratual, o BRB promoverá cobrança da quantia devida, por meio de glosa dos valores a serem pagos mensalmente à Conveniência BRB e mediante débito direto em sua conta de depósito à vista. Se não houver saldo que suporte o débito respectivo, o Banco poderá, ainda, promover a cobrança por meio judicial sem prejuízo da aplicação de outras penalidades cabíveis."),
            ], style={"color": "#666"}),

            # Dicas de Uso
            html.H5("Dicas de Uso", style={"color": "#023e7c"}),
            html.P("Algumas dicas para aproveitar ao máximo a aplicação:", style={"color": "#666"}),
            html.Ul([
                html.Li("Use os filtros na aba Dashboard para personalizar a visualização dos dados (ex.: filtrar por CNP ou período)."),
                html.Li("Certifique-se de que o banco de dados MySQL está acessível antes de executar o ETL."),
                html.Li("Na aba Relatórios, exporte os dados para CSV para análises externas."),
            ], style={"color": "#666"}),
            # Placeholder para imagem (ex.: captura de tela do Dashboard com filtros)
            html.P("Imagem: Dashboard com filtros aplicados", style={"color": "#666"}),
            html.Img(src="/assets/dashboard_filtros.png", style={"width": "50%", "margin": "0 auto", "display": "block"}),
        ]

    else:
        return html.P("Selecione uma opção no menu acima.", style={"color": "#666"})