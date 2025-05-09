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
        html.P("Esta seção descreve a estrutura do banco de dados MySQL usado na aplicação CentralSeg.", style={"color": "#666"}),
        html.Hr(),

        # Estrutura das Tabelas
        html.H5("Estrutura das Tabelas", style={"color": "#023e7c"}),
        html.P("Detalhes das tabelas do banco de dados e seus relacionamentos:", style={"color": "#666"}),
        html.Ul([
            html.Li("cnp_data: Armazena informações básicas dos CNPs (cnp, cnpj, razao_social, etc.)."),
            html.Li("seguradora: Contém detalhes dos seguros (cnp, inicio_vigencia_seguro, vencimento, valor_cobertura, etc.)."),
            html.Li("pag_seguradora: Registra os pagamentos dos seguros (cnp, numero_parcela, status)."),
            html.Li("cnp_historico: Armazena o histórico mensal de produção dos CNPs (cnp, jan_23, fev_23, ..., dez_25)."),
            html.Li("Relacionamentos: A chave primária 'cnp' da tabela cnp_data é usada como chave estrangeira nas tabelas seguradora, pag_seguradora e cnp_historico."),
        ], style={"color": "#666"}),
        html.P("Abaixo a query DDL das tabelas presentes no CentralSeg:", style={"color": "#666"}),
        html.H6("gecaf.cnp_data", style={"color": "#023e7c"}),
        html.Pre("""
CREATE TABLE `cnp_data` (
  `cnp` int(11) NOT NULL,
  `situacao` tinyint(4) NOT NULL DEFAULT 1,
  `cnpj` varchar(30) DEFAULT NULL,
  `razao_social` varchar(255) DEFAULT NULL,
  `cc` varchar(50) DEFAULT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `telefone_proprietario` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `endereco` varchar(255) DEFAULT NULL,
  `bairro` varchar(100) DEFAULT NULL,
  `cidade` varchar(100) DEFAULT NULL,
  `uf` char(2) DEFAULT NULL,
  `cep` varchar(20) DEFAULT NULL,
  `latitude` decimal(10,6) DEFAULT NULL,
  `longitude` decimal(10,6) DEFAULT NULL,
  `observacao` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`cnp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
        """, style={"color": "#666", "backgroundColor": "#f8f9fa", "padding": "10px", "borderRadius": "5px"}),
        html.H6("gecaf.cnp_historico", style={"color": "#023e7c"}),
        html.Pre("""
CREATE TABLE `cnp_historico` (
  `cnp` int(11) NOT NULL,
  `dez_23` decimal(15,2) DEFAULT NULL,
  `jan_24` decimal(15,2) DEFAULT NULL,
  `fev_24` decimal(15,2) DEFAULT NULL,
  `mar_24` decimal(15,2) DEFAULT NULL,
  `abr_24` decimal(15,2) DEFAULT NULL,
  `mai_24` decimal(15,2) DEFAULT NULL,
  `jun_24` decimal(15,2) DEFAULT NULL,
  `jul_24` decimal(15,2) DEFAULT NULL,
  `ago_24` decimal(15,2) DEFAULT NULL,
  `set_24` decimal(15,2) DEFAULT NULL,
  `out_24` decimal(15,2) DEFAULT NULL,
  `nov_24` decimal(15,2) DEFAULT NULL,
  `dez_24` decimal(15,2) DEFAULT NULL,
  `jan_25` decimal(15,2) DEFAULT NULL,
  `fev_25` decimal(15,2) DEFAULT NULL,
  `mar_25` decimal(15,2) DEFAULT NULL,
  `abr_25` decimal(15,2) DEFAULT NULL,
  `mai_25` decimal(15,2) DEFAULT NULL,
  `jun_25` decimal(15,2) DEFAULT NULL,
  `jul_25` decimal(15,2) DEFAULT NULL,
  `ago_25` decimal(15,2) DEFAULT NULL,
  `set_25` decimal(15,2) DEFAULT NULL,
  `out_25` decimal(15,2) DEFAULT NULL,
  `nov_25` decimal(15,2) DEFAULT NULL,
  `dez_25` decimal(15,2) DEFAULT NULL,
  PRIMARY KEY (`cnp`),
  CONSTRAINT `fk_cnp_historico` FOREIGN KEY (`cnp`) REFERENCES `cnp_data` (`cnp`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
        """, style={"color": "#666", "backgroundColor": "#f8f9fa", "padding": "10px", "borderRadius": "5px"}),
        html.H6("gecaf.pag_seguradora", style={"color": "#023e7c"}),
        html.Pre("""
CREATE TABLE `pag_seguradora` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cnp` int(11) NOT NULL,
  `numero_parcela` int(11) NOT NULL CHECK (`numero_parcela` > 0),
  `data_vencimento` date DEFAULT NULL,
  `status` enum('PAGO','PENDENTE','EMITIR') DEFAULT NULL,
  `data_pagamento` datetime DEFAULT NULL,
  `usuario_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_cnp_numero_parcela` (`cnp`,`numero_parcela`),
  CONSTRAINT `fk_pag_seguradora_cnp` FOREIGN KEY (`cnp`) REFERENCES `seguradora` (`cnp`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=361 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
        """, style={"color": "#666", "backgroundColor": "#f8f9fa", "padding": "10px", "borderRadius": "5px"}),
        html.H6("gecaf.seguradora", style={"color": "#023e7c"}),
        html.Pre("""
CREATE TABLE `seguradora` (
  `cnp` int(11) NOT NULL,
  `inicio_vigencia_seguro` date DEFAULT NULL,
  `vencimento` date DEFAULT NULL,
  `valor_cobertura` decimal(15,2) DEFAULT NULL,
  `valor_proposto` decimal(15,2) DEFAULT NULL,
  `valor_parcela` decimal(15,2) DEFAULT NULL,
  `forma_de_pgt` varchar(20) DEFAULT NULL,
  `situacao_proposta` varchar(50) DEFAULT NULL,
  `obs` text DEFAULT NULL,
  `apolice` varchar(50) DEFAULT NULL,
  `multiseguros` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`cnp`),
  CONSTRAINT `fk_seguradora_cnp` FOREIGN KEY (`cnp`) REFERENCES `cnp_data` (`cnp`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
        """, style={"color": "#666", "backgroundColor": "#f8f9fa", "padding": "10px", "borderRadius": "5px"}),

        # Como o Banco de Dados Funciona
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
        html.P("Esta seção contém informações técnicas detalhadas sobre a aplicação CentralSeg.", style={"color": "#666"}),
        html.Hr(),

        # Tecnologias Utilizadas
        html.H5("Tecnologias Utilizadas", style={"color": "#023e7c"}),
        html.Ul([
            html.Li("Python 3.13+: Linguagem principal para lógica da aplicação e ETL."),
            html.Li("Dash 2.18.2: Framework para criação do dashboard interativo."),
            html.Li("Plotly 6.0.1: Para gráficos interativos (barras, donut, linhas)."),
            html.Li("Pandas 2.2.3: Para manipulação de dados no ETL e dashboard."),
            html.Li("MySQL 8.0+: Banco de dados relacional."),
            html.Li("SQLAlchemy 2.0.39: Para conexão entre Python e MySQL."),
            html.Li("Dash Bootstrap Components 1.7.1: Para estilização e layout responsivo."),
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

        # Boas Práticas no ETL
        html.H5("Boas Práticas no ETL", style={"color": "#023e7c"}),
        html.Ul([
            html.Li("Validação de dados: Verifica se as tabelas estão vazias antes de processar."),
            html.Li("Logging: Usa a biblioteca logging para registrar erros e progresso do ETL."),
            html.Li("Tratamento de erros: Inclui try/except para lidar com falhas na conexão ou nos dados."),
        ], style={"color": "#666"}),

        # Trechos de Código Importantes
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

        # Configurações do Ambiente
        html.H5("Configurações do Ambiente", style={"color": "#023e7c"}),
        html.P("Download Python | Python.org", style={"color": "#666"}),
        html.P("Baixe e instale um editor de código da sua preferência, mas recomendo o VSCode.", style={"color": "#666"}),
        html.P("Faça a instalação do Python através do site oficial.", style={"color": "#666"}),
        html.P("Siga os passos abaixo para configurar o ambiente de desenvolvimento:", style={"color": "#666"}),
        html.Ol([
            html.Li("Clone o repositório: git clone <URL_DO_REPOSITORIO>."),
            html.Li("Crie um ambiente virtual: python -m venv venv."),
            html.Li("Instale as dependências: pip install -r requirements.txt."),
            html.Li("Baixar e instalar o XAMPP (essa aplicação serve como servidor para rodar a instância do MySQL/MariaDB)."),
            html.Li("Fazer a importação do banco de dados; a cópia do backup encontra-se em Seguro_CNP_Dash\\database, o arquivo de backup chama-se DB_Gecaf.sql."),
            html.Li("Configure o banco de dados MySQL e atualize as credenciais no arquivo connection.py."),
            html.Li("Execute a aplicação: python app.py."),
        ], style={"color": "#666"}),
        html.P("Obs.: A aplicação vai rodar localmente (127.0.0.1) utilizando a porta 8050. O endereço é: 127.0.0.1:8050.", style={"color": "#666"}),
    ]
    elif doc_type == "manual_uso":
        return [
        html.H4("Introdução", className="mb-3",
                style={"fontSize": "26px", "fontWeight": "bold", "color": "#023e7c"}),
        html.P("Esse Manual explica como usar a aplicação CentralSeg de forma eficiente.", style={"color": "#666"}),
        html.Hr(),

        # Navegação
        html.H5("Navegação", style={"color": "#023e7c"}),
        html.P("Use o menu lateral para acessar as diferentes seções da aplicação:", style={"color": "#666"}),
        html.Ul([
            html.Li("Dashboard: visualize métricas e gráficos gerais, como os top 5 CNPs, vencimento ao longo do tempo, "
                    "distribuição do status de pagamento, evolução de produção e detalhes dos seguros através de uma tabela. "),
                    ("É possível filtrar por CNP também."),
            html.Li("CNPs: gerencie informações dos CNPs, como razão social, endereço e contato, pode incluir, editar e deletar também."),
            html.Li("Seguro: consulte detalhes dos seguros, incluindo datas de vigência e valores. É possível importar os dados do seguro "
                    "através da planilha que a seguradora encaminhar para o BRB para realizar a importação bastar clicar em importar seguro."),
            html.Li("Relatórios: gere relatórios personalizados com base nos dados disponíveis. Conseguimos identificar quais conveniência "
                    "estão preste a vence filtrando essa informação no campo da data logo ao lado do botão ‘Exportar como PDF’."),
            html.Li("Exportar como PDF: essa é uma opção foi implementada para gerar um relatório em pdf com algumas informações do CNP, "
                    "do seguro e do valor proposto do seguro, com base na movimentação dos últimos 12 meses."),
            html.Li("Executar ETL: Esse modulo serve para extrair os dados de (Recolhimento 005) e (Malote AG 107) gerado pelo EIS e armazenar "
                    "a informação da média de movimentação no banco de dados."),
            html.Li("Sobre: Acessa informações sobre manual de uso, documentação técnica e diagrama e estrutura do banco de dados."),
        ], style={"color": "#666"}),

        # Para que Serve o ETL e Como Executar?
        html.H5("Para que Serve o ETL e Como Executar?", style={"color": "#023e7c"}),
        html.P("Executar ETL: Esse modulo serve para extrair os dados de (Recolhimento 005) e (Malote AG 107) gerado pelo EIS, com base nesses "
               "dados extraídos identificar qual é a média de movimentação de cada CNP e aplicar o valor proposto do seguro.", style={"color": "#666"}),
        html.P("Regras do valor proposto:", style={"color": "#666"}),
        html.Table([
            html.Thead(
                html.Tr([
                    html.Th("Média Mensal", style={"color": "#023e7c", "border": "1px solid #ddd", "padding": "8px"}),
                    html.Th("Valor Proposto da Cobertura", style={"color": "#023e7c", "border": "1px solid #ddd", "padding": "8px"}),
                ])
            ),
            html.Tbody([
                html.Tr([
                    html.Td("<= R$ 70.000,00", style={"color": "#666", "border": "1px solid #ddd", "padding": "8px"}),
                    html.Td("R$ 70.000,00", style={"color": "#666", "border": "1px solid #ddd", "padding": "8px"}),
                ]),
                html.Tr([
                    html.Td("<= R$ 90.000,00", style={"color": "#666", "border": "1px solid #ddd", "padding": "8px"}),
                    html.Td("R$ 90.000,00", style={"color": "#666", "border": "1px solid #ddd", "padding": "8px"}),
                ]),
                html.Tr([
                    html.Td("<= R$ 100.000,00", style={"color": "#666", "border": "1px solid #ddd", "padding": "8px"}),
                    html.Td("R$ 100.000,00", style={"color": "#666", "border": "1px solid #ddd", "padding": "8px"}),
                ]),
                html.Tr([
                    html.Td("<= R$ 120.000,00", style={"color": "#666", "border": "1px solid #ddd", "padding": "8px"}),
                    html.Td("R$ 120.000,00", style={"color": "#666", "border": "1px solid #ddd", "padding": "8px"}),
                ]),
                html.Tr([
                    html.Td("<= R$ 150.000,00", style={"color": "#666", "border": "1px solid #ddd", "padding": "8px"}),
                    html.Td("R$ 150.000,00", style={"color": "#666", "border": "1px solid #ddd", "padding": "8px"}),
                ]),
                html.Tr([
                    html.Td("<= R$ 180.000,00", style={"color": "#666", "border": "1px solid #ddd", "padding": "8px"}),
                    html.Td("R$ 180.000,00", style={"color": "#666", "border": "1px solid #ddd", "padding": "8px"}),
                ]),
                html.Tr([
                    html.Td("> R$ 180.000,00", style={"color": "#666", "border": "1px solid #ddd", "padding": "8px"}),
                    html.Td("R$ 200.000,00", style={"color": "#666", "border": "1px solid #ddd", "padding": "8px"}),
                ]),
            ])
        ], style={"width": "100%", "borderCollapse": "collapse", "marginBottom": "20px"}),
        html.P("Para executar o ETL, siga os passos abaixo:", style={"color": "#666"}),
        html.Ol([
            html.Li("Clique na aba 'Executar ETL' no menu lateral."),
            html.Li("Clique no botão 'Executar ETL' para iniciar o processo."),
            html.Li("Aguarde a mensagem de confirmação (ex.: 'ETL executado com sucesso!')."),
            html.Li("Volte ao Dashboard para visualizar os dados atualizados."),
        ], style={"color": "#666"}),

        # Regras para Contratação e Gerenciamento do Seguro
        html.H5("Regras para Contratação e Gerenciamento do Seguro", style={"color": "#023e7c"}),
        html.P("Esta seção detalha as regras e procedimentos para a contratação e gerenciamento do seguro dos CNPs.", style={"color": "#666"}),
        html.Ul([
            html.Li("O valor de cobertura é definido pelo Banco, levando-se em conta sua média de movimentação financeira diária, "
                    "referente aos últimos 12 (doze) meses."),
            html.Li("O valor de cobertura é calculado pela GECOR e comunicado à Corretora de Seguros. Para definição do valor de cobertura "
                    "de cada Correspondente, leva-se em conta sua média de movimentação financeira diária, referente aos últimos 12 (doze) "
                    "meses. O cálculo considera a seguinte fórmula: RECOLHIMENTO (005) - MALOTE AG (107) / 22 = movimentação financeira do CNP."),
            html.Li("Para novos contratos referentes a correspondentes existentes e que possuem movimentação registrada, o valor da cobertura "
                    "do seguro não poderá ser iniciado em R$ 100.000,00 (cem mil reais). Nesse caso, considera-se a média de movimentação "
                    "do correspondente."),
            html.Li("Compete ainda, à Conveniência BRB, realizar anualmente por ocasião do vencimento, a renovação do seguro contratado assim "
                    "como efetuar os endossos necessários, comunicando à Seguradora a ocorrência de quaisquer eventos ou alterações ocorridas "
                    "na respectiva apólice."),
            html.Li("Nos casos de perdas não cobertas pelo seguro, indenização paga pela seguradora não suficiente para cobrir o valor sinistrado, "
                    "diferenças de caixa e valores oriundos de sinistros não regularizados no prazo contratual, o BRB promoverá cobrança da quantia "
                    "devida, por meio de glosa dos valores a serem pagos mensalmente à Conveniência BRB e mediante débito direto em sua conta de "
                    "depósito à vista. Se não houver saldo que suporte o débito respectivo, o Banco poderá, ainda, promover a cobrança por meio "
                    "judicial sem prejuízo da aplicação de outras penalidades cabíveis."),
        ], style={"color": "#666"}),

        # Acessar Dados no EIS
        html.H5("Acessar Dados no EIS", style={"color": "#023e7c"}),
        html.H6("Recolhimento e Suprimento", style={"color": "#023e7c"}),
        html.Ol([
            html.Li("Acesse EIS > Auditoria."),
            html.Li("Selecione Recolhimento e Suprimento."),
            html.Li("Configuração > Desmarcar Todas > Marcar 005 > OK."),
            html.Li("Inserir período desejado."),
            html.Li("Dependência: 0600 a 0899."),
            html.Li("Transação: 025300 a 025400."),
            html.Li("Marcar: Resultado p/ Excel."),
            html.Li("Clicar em Pesquisar."),
        ], style={"color": "#666"}),
        html.H6("Cheque de Malote", style={"color": "#023e7c"}),
        html.Ol([
            html.Li("Acesse EIS > Auditoria."),
            html.Li("Selecione Cheque de Malote."),
            html.Li("Configuração > Desmarcar Todas > Marcar 89 > OK."),
            html.Li("Inserir período desejado."),
            html.Li("Dependência: 0600 a 0899."),
            html.Li("Transação: 036602 a 036602."),
            html.Li("Marcar: Resultado p/ Excel."),
            html.Li("Clicar em Pesquisar."),
        ], style={"color": "#666"}),
        html.H6("Créditos de Agência", style={"color": "#023e7c"}),
        html.Ol([
            html.Li("Acesse EIS > Auditoria."),
            html.Li("Selecione Créditos de Agência."),
            html.Li("Configuração > Desmarcar Todas > Marcar 107 > OK."),
            html.Li("Inserir período desejado."),
            html.Li("Dependência: 0011 a 0599."),
            html.Li("Transação: 316000 a 316999."),
            html.Li("Marcar: Resultado p/ Excel."),
            html.Li("Clicar em Pesquisar."),
        ], style={"color": "#666"}),

        # Dicas de Uso
        html.H5("Dicas de Uso", style={"color": "#023e7c"}),
        html.P("Algumas dicas para aproveitar ao máximo a aplicação:", style={"color": "#666"}),
        html.Ul([
            html.Li("Use os filtros na aba Dashboard para personalizar a visualização dos dados (ex.: filtrar por CNP ou período)."),
            html.Li("Certifique-se de que o banco de dados MySQL está acessível antes de executar o ETL."),
            html.Li("Na aba Relatórios, exporte os dados para PDF para análises externas."),
        ], style={"color": "#666"}),
    ]

    else:
        return html.P("Selecione uma opção no menu acima.", style={"color": "#666"})