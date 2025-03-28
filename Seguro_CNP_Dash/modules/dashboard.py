# Página do dashboard
# Este módulo exibe um dashboard com informações resumidas sobre CNPs e seus seguros.

# Importações necessárias
import dash
from dash import dcc, html, callback_context
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
from sqlalchemy import text
from database.connection import engine  # Conexão com o banco de dados
import datetime  # Para manipulação de datas
from calendar import monthrange  # Para calcular o último dia do mês
import plotly.express as px  # Para gráficos interativos
import plotly.graph_objects as go  # Para gráficos mais personalizados

# Definição do layout do dashboard
layout = html.Div([
    # Cabeçalho com título e versão
    html.Div([
        html.H3("Dashboard - Gestão de Seguros", className="text-center mb-2",
                style={"fontSize": "32px", "fontWeight": "bold", "color": "#023e7c", "marginTop": "20px", "textShadow": "2px 2px 4px rgba(0,0,0,0.1)"}),
        html.Div("Versão: v100.01", className="text-center mb-4",
                 style={"fontSize": "14px", "color": "#666", "fontStyle": "italic"})
    ]),

    # Linha com o campo de busca
    dbc.Row([
        # Coluna para o campo de busca (4 colunas de largura)
        dbc.Col(
            dbc.Input(id="search-dashboard", type="text",
                      placeholder="Buscar por CNP ou Razão Social...",
                      className="mb-3",
                      style={"borderRadius": "5px", "border": "2px solid #023e7c", "boxShadow": "0 2px 5px rgba(0,0,0,0.1)", "padding": "10px"}),
            width=4, style={"margin": "0 auto"}
        ),
    ], justify="center", className="mb-4"),

    # Linha com cards de resumo geral
    html.Hr(className="my-4", style={"borderColor": "#023e7c", "borderWidth": "2px"}),  # Linha divisória
    html.H4("Resumo Geral", className="text-center mb-4",
            style={"fontSize": "26px", "fontWeight": "bold", "color": "#023e7c", "textShadow": "1px 1px 3px rgba(0,0,0,0.1)"}),
    dbc.Row([
        # Card 1: Número total de CNPs
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Total de CNPs", className="card-title text-center", style={"fontSize": "16px", "color": "#023e7c"}),
                    html.H3(id="total-cnps", className="card-text text-center", style={"color": "#023e7c", "fontSize": "24px", "fontWeight": "bold"}),
                ])
            ], style={"border": "2px solid #023e7c", "borderRadius": "10px", "boxShadow": "0 4px 8px rgba(0,0,0,0.2)", "background": "linear-gradient(135deg, #f5f7fa, #c3cfe2)"})
        ], width=3, className="mb-4"),
        # Card 2: Número de seguros ativos
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Seguros Ativos", className="card-title text-center", style={"fontSize": "16px", "color": "#023e7c"}),
                    html.H3(id="seguros-ativos", className="card-text text-center", style={"color": "#023e7c", "fontSize": "24px", "fontWeight": "bold"}),
                ])
            ], style={"border": "2px solid #023e7c", "borderRadius": "10px", "boxShadow": "0 4px 8px rgba(0,0,0,0.2)", "background": "linear-gradient(135deg, #f5f7fa, #c3cfe2)"})
        ], width=3, className="mb-4"),
        # Card 3: Valor total de cobertura
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Valor Total de Cobertura", className="card-title text-center", style={"fontSize": "16px", "color": "#023e7c"}),
                    html.H3(id="valor-total-cobertura", className="card-text text-center", style={"color": "#023e7c", "fontSize": "24px", "fontWeight": "bold"}),
                ])
            ], style={"border": "2px solid #023e7c", "borderRadius": "10px", "boxShadow": "0 4px 8px rgba(0,0,0,0.2)", "background": "linear-gradient(135deg, #f5f7fa, #c3cfe2)"})
        ], width=3, className="mb-4"),
        # Card 4: Seguros que vencem no mês subsequente
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Próximos Vencimentos", className="card-title text-center", style={"fontSize": "16px", "color": "#023e7c"}),
                    html.H3(id="seguros-proximos-vencer", className="card-text text-center", style={"color": "#023e7c", "fontSize": "24px", "fontWeight": "bold"}),
                ])
            ], style={"border": "2px solid #023e7c", "borderRadius": "10px", "boxShadow": "0 4px 8px rgba(0,0,0,0.2)", "background": "linear-gradient(135deg, #f5f7fa, #c3cfe2)"})
        ], width=3, className="mb-4"),
    ], justify="center", className="mb-5"),

    # Seção de Gráficos
    html.Hr(className="my-5", style={"borderColor": "#023e7c", "borderWidth": "2px"}),  # Linha divisória
    html.H4("Análise Visual", className="text-center mb-5",
            style={"fontSize": "26px", "fontWeight": "bold", "color": "#023e7c", "textShadow": "1px 1px 3px rgba(0,0,0,0.1)"}),

    # Linha 1: Top 5 CNPs e Status de Pagamento
    dbc.Row([
        # Gráfico 1: Top 5 CNPs que Mais Produziram nos Últimos 12 Meses
        dbc.Col([
            html.Div([
                html.H5("Top 5 CNPs que Mais Produziram nos Últimos 12 Meses", className="text-center mb-3", style={"fontSize": "18px", "color": "#023e7c", "fontWeight": "bold"}),
                dcc.Graph(id="grafico-top-valor-cobertura")
            ], style={"backgroundColor": "#f9f9f9", "borderRadius": "10px", "padding": "20px", "boxShadow": "0 4px 8px rgba(0,0,0,0.1)"})
        ], width=6, className="mb-5"),
        # Gráfico 2: Distribuição do Status de Pagamento
        dbc.Col([
            html.Div([
                html.H5("Distribuição do Status de Pagamento", className="text-center mb-3", style={"fontSize": "18px", "color": "#023e7c", "fontWeight": "bold"}),
                dcc.Graph(id="grafico-status-pagamento")
            ], style={"backgroundColor": "#f9f9f9", "borderRadius": "10px", "padding": "20px", "boxShadow": "0 4px 8px rgba(0,0,0,0.1)"})
        ], width=6, className="mb-5"),
    ], justify="center", className="mb-5"),

    # Linha 2: Vencimentos ao Longo do Tempo e Evolução da Média dos Top 5 CNPs
    dbc.Row([
        # Gráfico 3: Vencimentos ao Longo do Tempo
        dbc.Col([
            html.Div([
                html.H5("Vencimentos ao Longo do Tempo", className="text-center mb-3", style={"fontSize": "18px", "color": "#023e7c", "fontWeight": "bold"}),
                dcc.Graph(id="grafico-vencimentos-tempo")
            ], style={"backgroundColor": "#f9f9f9", "borderRadius": "10px", "padding": "20px", "boxShadow": "0 4px 8px rgba(0,0,0,0.1)"})
        ], width=6, className="mb-5"),
        # Gráfico 4: Evolução da Média Mensal dos Top 5 CNPs
        dbc.Col([
            html.Div([
                html.H5("Evolução da Média Mensal dos Top 5 CNPs", className="text-center mb-3", style={"fontSize": "18px", "color": "#023e7c", "fontWeight": "bold"}),
                dcc.Graph(id="grafico-evolucao-top5")
            ], style={"backgroundColor": "#f9f9f9", "borderRadius": "10px", "padding": "20px", "boxShadow": "0 4px 8px rgba(0,0,0,0.1)"})
        ], width=6, className="mb-5"),
    ], justify="center", className="mb-5"),

    # Tabela interativa para exibir os dados dos CNPs e seguros
    html.Hr(className="my-5", style={"borderColor": "#023e7c", "borderWidth": "2px"}),  # Linha divisória
    html.H4("Detalhes dos Seguros", className="text-center mb-5",
            style={"fontSize": "26px", "fontWeight": "bold", "color": "#023e7c", "textShadow": "1px 1px 3px rgba(0,0,0,0.1)"}),
    dash_table.DataTable(
        id='dashboard-table',
        # Definição das colunas da tabela
        columns=[
            {"name": "CNP", "id": "cnp", "type": "numeric"},
            {"name": "Razão Social", "id": "razao_social", "type": "text"},
            {"name": "Início Vigência", "id": "inicio_vigencia_seguro", "type": "text"},
            {"name": "Vencimento", "id": "vencimento", "type": "text"},
            {"name": "Valor Cobertura", "id": "valor_cobertura", "type": "text"},
            {"name": "Valor Proposto", "id": "valor_proposto", "type": "text"},
            {"name": "Status Pagamento", "id": "status_pagamento", "type": "text"},
            {"name": "Parcelas Pagas", "id": "parcelas_pagas", "type": "text"},
        ],
        data=[],  # Dados inicialmente vazios (serão preenchidos via callback)
        # Estilo da tabela
        style_table={'overflowX': 'auto', 'border': '2px solid #023e7c', 'borderRadius': '10px', 'boxShadow': '0 4px 8px rgba(0,0,0,0.2)', 'marginBottom': '50px'},
        style_header={'backgroundColor': '#023e7c', 'color': 'white',
                      'fontWeight': 'bold', 'textAlign': 'center', 'border': '1px solid #023e7c', 'fontSize': '16px'},
        style_data={'textAlign': 'center', 'border': '1px solid #023e7c', 'fontSize': '14px', 'backgroundColor': '#f9f9f9'},
        style_cell={'padding': '12px'},
        # Estilo condicional para o status de pagamento
        style_data_conditional=[
            {
                'if': {
                    'column_id': 'status_pagamento',
                    'filter_query': '{status_pagamento} = "Pendente"'
                },
                'backgroundColor': '#FF9999',  # Vermelho claro
                'color': 'black'
            },
            {
                'if': {
                    'column_id': 'status_pagamento',
                    'filter_query': '{status_pagamento} = "Parcialmente Pago"'
                },
                'backgroundColor': '#FFFF99',  # Amarelo claro
                'color': 'black'
            },
            {
                'if': {
                    'column_id': 'status_pagamento',
                    'filter_query': '{status_pagamento} = "Pago"'
                },
                'backgroundColor': '#90EE90',  # Verde claro
                'color': 'black'
            },
        ],
        page_size=15,  # Número de linhas por página
    ),
])

# Callback para carregar os dados da tabela, cards e gráficos
@dash.callback(
    [
        Output("dashboard-table", "data"),
        Output("total-cnps", "children"),
        Output("seguros-ativos", "children"),
        Output("valor-total-cobertura", "children"),
        Output("seguros-proximos-vencer", "children"),
        Output("grafico-top-valor-cobertura", "figure"),
        Output("grafico-status-pagamento", "figure"),
        Output("grafico-vencimentos-tempo", "figure"),
        Output("grafico-evolucao-top5", "figure"),
    ],
    [Input("dashboard-table", "id"), Input("search-dashboard", "value")]
)
def load_dashboard_data(_, search_value):
    """
    Carrega os dados do banco de dados para a tabela, cards e gráficos.
    - Consulta as tabelas cnp_data, seguradora, pag_seguradora e cnp_historico para obter informações completas.
    - Formata os dados para exibição (datas, valores monetários, status de pagamento).
    - Filtra os dados com base no valor de busca (CNP ou Razão Social).
    - Calcula métricas para os cards de resumo e gráficos.
    """
    try:
        with engine.connect() as conn:
            # Consulta SQL para buscar dados das tabelas cnp_data e seguradora
            query = text("""
                SELECT 
                  d.cnp,
                  d.cnpj,
                  d.razao_social,
                  s.inicio_vigencia_seguro,
                  s.vencimento,
                  s.valor_cobertura,
                  s.valor_proposto
                FROM cnp_data d
                LEFT JOIN seguradora s ON d.cnp = s.cnp
            """)
            df = pd.read_sql(query, conn)  # Executa a consulta e carrega os dados em um DataFrame

            # Formata as datas para o padrão DD/MM/YYYY
            df["inicio_vigencia_seguro"] = df["inicio_vigencia_seguro"].apply(
                lambda x: x.strftime("%d/%m/%Y") if pd.notnull(x) else ""
            )
            df["vencimento"] = df["vencimento"].apply(
                lambda x: x.strftime("%d/%m/%Y") if pd.notnull(x) else ""
            )

            # Calcula as datas do mês subsequente
            current_date = datetime.datetime.now()
            next_month = current_date.replace(day=1) + datetime.timedelta(days=32)
            next_month_start = next_month.replace(day=1)
            _, last_day = monthrange(next_month.year, next_month.month)
            next_month_end = next_month.replace(day=last_day)

            # Converte a coluna de vencimento para datetime para cálculos
            df["vencimento_date"] = pd.to_datetime(df["vencimento"], format="%d/%m/%Y", errors="coerce")

            # Formata os valores monetários para o padrão brasileiro (R$ 1.234,56)
            df["valor_cobertura"] = df["valor_cobertura"].apply(
                lambda x: f"R$ {float(x):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") if pd.notnull(x) else ""
            )
            df["valor_proposto"] = df["valor_proposto"].apply(
                lambda x: f"R$ {float(x):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") if pd.notnull(x) else ""
            )

            # Consulta os dados de pagamento para cada CNP
            query_pag = text("""
                SELECT cnp, numero_parcela, status
                FROM pag_seguradora
            """)
            df_pag = pd.read_sql(query_pag, conn)

            # Calcula o status de pagamento e o número de parcelas pagas
            def get_payment_status(cnp):
                if pd.isna(cnp):
                    return "Sem Seguro", "0/0"
                parcelas = df_pag[df_pag["cnp"] == cnp]
                if parcelas.empty:
                    return "Sem Seguro", "0/0"
                # Conta o número total de parcelas (todos os registros para o CNP)
                total_parcelas = len(parcelas)
                # Conta o número de parcelas pagas (status = "PAGO")
                pagas = len(parcelas[parcelas["status"] == "PAGO"])
                if total_parcelas == 0:
                    return "Sem Parcelas", "0/0"
                if pagas == total_parcelas:
                    return "Pago", f"{pagas}/{total_parcelas}"
                elif pagas == 0:
                    return "Pendente", f"{pagas}/{total_parcelas}"
                else:
                    return "Parcialmente Pago", f"{pagas}/{total_parcelas}"

            # Aplica a função para cada CNP
            df[["status_pagamento", "parcelas_pagas"]] = df["cnp"].apply(
                lambda x: pd.Series(get_payment_status(x))
            )

            # Filtra os dados com base no valor de busca
            if search_value:
                df = df[df["cnp"].astype(str).str.contains(search_value, case=False, na=False) |
                        df["razao_social"].str.contains(search_value, case=False, na=False)]

            # Calcula métricas para os cards de resumo
            total_cnps = len(df["cnp"].unique())  # Número total de CNPs
            seguros_ativos = len(df[df["vencimento"] != ""])  # Número de seguros ativos (com vencimento)
            
            # Calcula o valor total de cobertura
            df["valor_cobertura_num"] = df["valor_cobertura"].apply(
                lambda x: float(x.replace("R$", "").replace(".", "").replace(",", ".").strip()) if isinstance(x, str) and x else 0
            )
            df["valor_proposto_num"] = df["valor_proposto"].apply(
                lambda x: float(x.replace("R$", "").replace(".", "").replace(",", ".").strip()) if isinstance(x, str) and x else 0
            )
            valor_total_cobertura = df["valor_cobertura_num"].sum()
            valor_total_cobertura = f"R$ {valor_total_cobertura:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

            # Calcula o número de seguros que vencem no mês subsequente
            seguros_proximos_vencer = len(df[(df["vencimento_date"] >= next_month_start) & (df["vencimento_date"] <= next_month_end)])

            # Consulta os dados históricos para calcular a média dos últimos 12 meses
            query_historico = text("SELECT * FROM cnp_historico")
            df_historico = pd.read_sql(query_historico, conn)

            # Define os últimos 12 meses a partir de março de 2025
            meses_12 = [
                "mar_25", "fev_25", "jan_25", "dez_24", "nov_24", "out_24",
                "set_24", "ago_24", "jul_24", "jun_24", "mai_24", "abr_24"
            ]

            # Calcula a média dos últimos 12 meses para cada CNP
            df_historico["media_12_meses"] = df_historico[meses_12].mean(axis=1, skipna=True)
            # Converte explicitamente para float para evitar o FutureWarning
            df_historico["media_12_meses"] = df_historico["media_12_meses"].astype(float).fillna(0)

            # Gráfico 1: Top 5 CNPs que Mais Produziram nos Últimos 12 Meses
            df_top_valor = df_historico[["cnp", "media_12_meses"]].copy()
            df_top_valor = df_top_valor.sort_values(by="media_12_meses", ascending=False).head(5)  # Top 5
            df_top_valor["label"] = df_top_valor["cnp"].astype(str)  # Usar apenas o número do CNP como rótulo
            fig_top_valor = go.Figure(data=[
                go.Bar(
                    x=df_top_valor["label"],
                    y=df_top_valor["media_12_meses"],
                    marker=dict(
                        color=["#1f77b4", "#4e9bd4", "#7bbde3", "#a8d5f0", "#d1e9f9"],
                        line=dict(color="#ffffff", width=2)
                    ),
                    text=df_top_valor["media_12_meses"].apply(lambda x: f"R$ {x:,.2f}"),
                    textposition="outside",
                    textfont=dict(size=12, color="#023e7c"),
                    hoverinfo="x+y"
                )
            ])
            fig_top_valor.update_layout(
                title="",
                xaxis_title="CNP",
                yaxis_title="Média Mensal (R$)",
                xaxis=dict(tickangle=0, title_font=dict(size=14, color="#023e7c"), tickfont=dict(size=12, color="#023e7c")),
                yaxis=dict(title_font=dict(size=14, color="#023e7c"), tickfont=dict(size=12, color="#023e7c")),
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                font=dict(color="#023e7c"),
                margin=dict(l=50, r=50, t=30, b=50),
                showlegend=False,
                height=400
            )

            # Gráfico 2: Distribuição do Status de Pagamento (Donut)
            df_status = df["status_pagamento"].value_counts().reset_index()
            df_status.columns = ["status_pagamento", "contagem"]
            fig_status_pagamento = go.Figure(
                data=[
                    go.Pie(
                        labels=df_status["status_pagamento"],
                        values=df_status["contagem"],
                        hole=0.5,
                        marker=dict(
                            colors=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"],
                            line=dict(color="#ffffff", width=2)
                        ),
                        textinfo="percent+label",
                        textposition="inside",
                        textfont=dict(size=14, color="#ffffff"),
                        hoverinfo="label+percent",
                        pull=[0.05, 0, 0, 0, 0]  # Destaca a primeira fatia
                    )
                ]
            )
            fig_status_pagamento.update_layout(
                title="",
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                font=dict(color="#023e7c"),
                margin=dict(l=50, r=50, t=30, b=50),
                height=400
            )

            # Gráfico 3: Vencimentos ao Longo do Tempo (Linha)
            df["mes_vencimento"] = df["vencimento_date"].dt.to_period("M").astype(str)
            df_vencimentos = df[df["mes_vencimento"] != "NaT"].groupby("mes_vencimento").size().reset_index(name="contagem")
            df_vencimentos = df_vencimentos.sort_values("mes_vencimento")
            fig_vencimentos = go.Figure(data=[
                go.Scatter(
                    x=df_vencimentos["mes_vencimento"],
                    y=df_vencimentos["contagem"],
                    mode="lines+markers",
                    line=dict(color="#1f77b4", width=3),
                    marker=dict(size=10, color="#ff7f0e", line=dict(width=2, color="#ffffff")),
                    hoverinfo="x+y",
                    text=df_vencimentos["contagem"],
                    textposition="top center",
                    textfont=dict(size=12, color="#023e7c")
                )
            ])
            fig_vencimentos.update_layout(
                title="",
                xaxis_title="Mês de Vencimento",
                yaxis_title="Número de Seguros",
                xaxis=dict(tickangle=45, title_font=dict(size=14, color="#023e7c"), tickfont=dict(size=12, color="#023e7c")),
                yaxis=dict(title_font=dict(size=14, color="#023e7c"), tickfont=dict(size=12, color="#023e7c")),
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                font=dict(color="#023e7c"),
                margin=dict(l=50, r=50, t=30, b=50),
                showlegend=False,
                height=400
            )

            # Gráfico 4: Evolução da Média Mensal dos Top 5 CNPs (Linhas)
            top_5_cnps = df_top_valor["cnp"].tolist()  # Lista dos Top 5 CNPs
            df_evolucao = df_historico[df_historico["cnp"].isin(top_5_cnps)][["cnp"] + meses_12]
            df_evolucao_melted = df_evolucao.melt(id_vars=["cnp"], value_vars=meses_12, var_name="mes", value_name="valor")
            df_evolucao_melted["cnp"] = df_evolucao_melted["cnp"].astype(str)
            # Mapeia os nomes dos meses para um formato mais legível
            mes_map = {
                "abr_24": "Abr/24", "mai_24": "Mai/24", "jun_24": "Jun/24", "jul_24": "Jul/24",
                "ago_24": "Ago/24", "set_24": "Set/24", "out_24": "Out/24", "nov_24": "Nov/24",
                "dez_24": "Dez/24", "jan_25": "Jan/25", "fev_25": "Fev/25", "mar_25": "Mar/25"
            }
            df_evolucao_melted["mes"] = df_evolucao_melted["mes"].map(mes_map)
            fig_evolucao = go.Figure()
            colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
            for i, cnp in enumerate(top_5_cnps):
                df_cnp = df_evolucao_melted[df_evolucao_melted["cnp"] == str(cnp)]
                fig_evolucao.add_trace(
                    go.Scatter(
                        x=df_cnp["mes"],
                        y=df_cnp["valor"],
                        mode="lines+markers",
                        name=f"CNP {cnp}",
                        line=dict(color=colors[i % len(colors)], width=3),
                        marker=dict(size=10, line=dict(width=2, color="#ffffff")),
                        hoverinfo="x+y",
                        text=df_cnp["valor"].apply(lambda x: f"R$ {x:,.2f}" if pd.notnull(x) else "N/A"),
                        textposition="top center",
                        textfont=dict(size=12, color="#023e7c")
                    )
                )
            fig_evolucao.update_layout(
                title="",
                xaxis_title="Mês",
                yaxis_title="Valor (R$)",
                xaxis=dict(tickangle=45, title_font=dict(size=14, color="#023e7c"), tickfont=dict(size=12, color="#023e7c")),
                yaxis=dict(title_font=dict(size=14, color="#023e7c"), tickfont=dict(size=12, color="#023e7c")),
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                font=dict(color="#023e7c"),
                margin=dict(l=50, r=50, t=30, b=50),
                legend=dict(orientation="h", yanchor="bottom", y=-0.4, xanchor="center", x=0.5),
                height=400
            )

        # Remove colunas auxiliares antes de retornar os dados para a tabela
        df = df.drop(columns=["cnpj", "vencimento_date", "valor_cobertura_num", "valor_proposto_num", "mes_vencimento"], errors="ignore")

        return (
            df.to_dict("records"),
            str(total_cnps),
            str(seguros_ativos),
            valor_total_cobertura,
            str(seguros_proximos_vencer),
            fig_top_valor,
            fig_status_pagamento,
            fig_vencimentos,
            fig_evolucao
        )

    except Exception as e:
        print(f"Erro ao carregar dados do dashboard: {e}")
        # Retorna valores padrão para evitar falhas no callback
        empty_fig = go.Figure()
        empty_fig.update_layout(title="Erro ao carregar gráfico", title_x=0.5)
        return [], "0", "0", "R$ 0,00", "0", empty_fig, empty_fig, empty_fig, empty_fig