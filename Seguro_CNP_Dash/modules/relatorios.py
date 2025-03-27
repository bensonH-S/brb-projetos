import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
from database.connection import engine
from sqlalchemy import text
import datetime
from datetime import timedelta
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, cm
import io
import base64

# Definir o tamanho personalizado para metade do A4 (210 mm x 148.5 mm)
HALF_A4 = (210*mm, 148.5*mm)  # Largura do A4 (210 mm), altura é metade do A4 (297 mm / 2)

# Layout da página ajustado para espaçamento consistente com seguro.py
layout = html.Div([
    # Título com margem inferior de 24px (mb-4), igual ao seguro.py
    html.H3("Relatórios de Seguros", className="text-center mb-4", 
            style={"fontSize": "28px", "fontWeight": "bold", "color": "#023e7c", "marginTop": "30px"}),
    
    # Filtros em uma linha com espaçamento uniforme
    dbc.Row([
        # Campo de busca por CNP
        dbc.Col(
            dbc.Input(id="filter-cnp", type="text", 
                      placeholder="Digite o CNP...", 
                      className="mb-3",  # Margem inferior de 16px, como em seguro.py
                      style={'border': '1px solid #ced4da', 'borderRadius': '4px', 'padding': '6px', 'fontSize': '14px'}),
            width=4
        ),
        # Filtros de data e botão de exportar
        dbc.Col([
            dbc.Row([
                # Data inicial
                dbc.Col(
                    dbc.Input(id="start-date-filter", type="date", 
                              className="mb-3",  # Margem inferior de 16px
                              style={'border': '1px solid #ced4da', 'borderRadius': '4px', 'padding': '6px', 'fontSize': '14px', 'width': '150px'}),
                    width=4
                ),
                # Data final
                dbc.Col(
                    dbc.Input(id="end-date-filter", type="date", 
                              className="mb-3",  # Margem inferior de 16px
                              style={'border': '1px solid #ced4da', 'borderRadius': '4px', 'padding': '6px', 'fontSize': '14px', 'width': '150px'}),
                    width=4
                ),
                # Botão de exportar
                dbc.Col(
                    dbc.Button("Exportar como PDF", id="export-pdf-btn", color="primary", 
                               className="mb-3",  # Margem inferior de 16px
                               style={'width': '150px', 'fontSize': '14px', 'padding': '6px', 'backgroundColor': '#023e7c', 'borderColor': '#023e7c'}),
                    width=4
                ),
            ], justify="end")  # Alinha os elementos à direita
        ], width=8, className="d-flex justify-content-end"),
    ], justify="between"),  # Espaçamento uniforme entre as colunas
    
    # Tabela
    dash_table.DataTable(
        id='report-table',
        columns=[
            {"name": "CNP", "id": "cnp", "type": "numeric"},
            {"name": "Razão Social", "id": "razao_social", "type": "text"},
            {"name": "Início Vigência", "id": "inicio_vigencia_seguro", "type": "text"},
            {"name": "Vencimento", "id": "vencimento", "type": "text"},
            {"name": "Média Últ. 12 Meses", "id": "media_ultimos_12_meses", "type": "text"},
            {"name": "Valor Cobertura", "id": "valor_cobertura", "type": "text"},
            {"name": "Valor Proposta Cobertura", "id": "valor_proposto", "type": "text"},
        ],
        data=[],
        style_table={'overflowX': 'auto', 'border': '1px solid #ddd'},
        style_header={'backgroundColor': '#023e7c', 'color': 'white', 'fontWeight': 'bold', 'textAlign': 'center'},
        style_data={'border': '1px solid #ddd', 'fontSize': '14px'},
        style_data_conditional=[
            {'if': {'column_id': 'razao_social'}, 'textAlign': 'left'},
            {'if': {'column_id': 'cnp'}, 'textAlign': 'center'},
            {'if': {'column_id': 'inicio_vigencia_seguro'}, 'textAlign': 'center'},
            {'if': {'column_id': 'vencimento'}, 'textAlign': 'center'},
            {'if': {'column_id': 'media_ultimos_12_meses'}, 'textAlign': 'center'},
            {'if': {'column_id': 'valor_cobertura'}, 'textAlign': 'center'},
            {'if': {'column_id': 'valor_proposto'}, 'textAlign': 'center'},
        ],
        style_cell={'padding': '8px'},
        page_size=15,
    ),
    dcc.Download(id="download-pdf")
])

@dash.callback(
    Output("report-table", "data"),
    [Input("filter-cnp", "value"),
     Input("start-date-filter", "value"),
     Input("end-date-filter", "value")]
)
def load_report_data(filter_cnp, start_date, end_date):
    # Mapa de meses para construir as colunas dos últimos 12 meses
    mes_map = {
        "01": "jan", "02": "fev", "03": "mar", "04": "abr",
        "05": "mai", "06": "jun", "07": "jul", "08": "ago",
        "09": "set", "10": "out", "11": "nov", "12": "dez"
    }

    # Obter os últimos 12 meses a partir da data atual
    ultimos_12_meses = []
    data_atual = datetime.datetime.now()
    for i in range(12):
        data_retroativa = data_atual - timedelta(days=i * 30)
        mes_retroativo = data_retroativa.strftime("%m")
        ano_retroativo = data_retroativa.strftime("%y")
        coluna_mes = f"{mes_map[mes_retroativo]}_{ano_retroativo}"
        ultimos_12_meses.append(coluna_mes)

    # Construir a expressão para somar os valores dos últimos 12 meses
    expressao_soma = "+".join(f"COALESCE(`{coluna}`, 0)" for coluna in ultimos_12_meses)

    with engine.connect() as conn:
        query = text(f"""
            SELECT 
                d.cnp,
                d.razao_social,
                s.inicio_vigencia_seguro,
                s.vencimento,
                COALESCE(ROUND(({expressao_soma}) / 12, 2), 0) AS media_ultimos_12_meses,
                s.valor_cobertura,
                s.valor_proposto
            FROM cnp_data d
            LEFT JOIN seguradora s ON d.cnp = s.cnp
            LEFT JOIN cnp_historico h ON d.cnp = h.cnp
        """)
        df = pd.read_sql(query, conn)

        df["inicio_vigencia_seguro"] = df["inicio_vigencia_seguro"].apply(
            lambda x: x.strftime("%d/%m/%y") if pd.notnull(x) else ""
        )
        df["vencimento"] = df["vencimento"].apply(
            lambda x: x.strftime("%d/%m/%y") if pd.notnull(x) else ""
        )
        df["media_ultimos_12_meses"] = df["media_ultimos_12_meses"].apply(
            lambda x: f"R$ {float(x):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") if pd.notnull(x) else ""
        )
        df["valor_cobertura"] = df["valor_cobertura"].apply(
            lambda x: f"R$ {float(x):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") if pd.notnull(x) else ""
        )
        df["valor_proposto"] = df["valor_proposto"].apply(
            lambda x: f"R$ {float(x):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") if pd.notnull(x) else ""
        )

        if filter_cnp:
            df = df[df["cnp"].astype(str).str.contains(filter_cnp, case=False, na=False)]
        
        if start_date and end_date:
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
            df["vencimento_dt"] = pd.to_datetime(df["vencimento"], format="%d/%m/%y", errors='coerce')
            df = df[
                (df["vencimento_dt"] >= start_date) &
                (df["vencimento_dt"] <= end_date)
            ]
            df = df.drop(columns=["vencimento_dt"])

    return df.to_dict("records")

@dash.callback(
    Output("download-pdf", "data"),
    Input("export-pdf-btn", "n_clicks"),
    State("report-table", "data"),
    prevent_initial_call=True
)
def export_to_pdf(n_clicks, table_data):
    if not n_clicks or not table_data:
        return None

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=HALF_A4, leftMargin=1*cm, rightMargin=1*cm, topMargin=1*cm, bottomMargin=1*cm)
    elements = []

    styles = getSampleStyleSheet()
    # Estilo personalizado para o título
    title_style = styles['Heading1']
    title_style.alignment = 1  # Centralizado
    title_style.fontSize = 14  # Ajustado para caber melhor
    title_style.spaceAfter = 8

    # Estilo para subtítulo (data de geração)
    subtitle_style = styles['Normal']
    subtitle_style.alignment = 1
    subtitle_style.fontSize = 8  # Ajustado para caber melhor
    subtitle_style.textColor = colors.grey
    subtitle_style.spaceAfter = 10

    # Estilo para o rodapé
    footer_style = styles['Normal']
    footer_style.alignment = 1
    footer_style.fontSize = 7  # Ajustado para caber melhor
    footer_style.textColor = colors.grey

    # Cabeçalho
    title = Paragraph("Relatório de Seguros", title_style)
    current_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    subtitle = Paragraph(f"Gerado em: {current_date}", subtitle_style)
    elements.append(title)
    elements.append(subtitle)
    elements.append(Spacer(1, 10))

    # Dados da tabela
    data = [["CNP", "Razão Social", "Início\nVigência", "Vencimento", "Média Últ.\n12 Meses", "Valor\nCobertura", "Valor Proposta\nCobertura"]]
    for row in table_data:
        data.append([
            str(row["cnp"]),
            row["razao_social"],
            row["inicio_vigencia_seguro"],
            row["vencimento"],
            row["media_ultimos_12_meses"],
            row["valor_cobertura"],
            row["valor_proposto"]
        ])

    # Definir larguras das colunas (em pontos)
    col_widths = [35, 240, 55, 55, 65, 65, 65]  # Total: 580 pontos

    table = Table(data, colWidths=col_widths)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#023e7c")),  # Alterado para #023e7c
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('ALIGN', (0, 1), (0, -1), 'CENTER'),
        ('ALIGN', (1, 1), (1, -1), 'LEFT'),
        ('ALIGN', (2, 1), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 2),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 7),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)

    # Rodapé
    elements.append(Spacer(1, 10))
    footer = Paragraph("Relatório gerado pelo CentralSeg GECAF - Gerência de Operações e Logística de Canais Físicos", footer_style)
    elements.append(footer)

    doc.build(elements)
    buffer.seek(0)

    return dcc.send_bytes(buffer.getvalue(), "relatorio_seguros.pdf")