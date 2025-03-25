import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
from database.connection import engine
from sqlalchemy import text
import datetime
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, cm
import io
import base64

# Definir o tamanho personalizado para metade do A4 (210 mm x 148.5 mm)
HALF_A4 = (210*mm, 148.5*mm)  # Largura do A4 (210 mm), altura é metade do A4 (297 mm / 2)

layout = html.Div([
    html.H3("Relatórios de Seguros", className="text-center mb-4", 
            style={"fontSize": "28px", "fontWeight": "bold", "color": "#007bff", "marginTop": "30px"}),
    # Filtros
    dbc.Row([
        dbc.Col([
            html.Div([
                dbc.Label("Buscar por CNP:", className="mb-1"),
                dbc.Input(id="filter-cnp", type="text", placeholder="Digite o CNP...", 
                          style={'border': '1px solid #ced4da', 'borderRadius': '4px', 'padding': '6px', 'fontSize': '14px'})
            ])
        ], width=4),
        dbc.Col([
            html.Div([
                html.Div([
                    dbc.Label("Data de Vencimento:", className="mb-1", style={'width': '150px'}),
                    html.Div([
                        dbc.Input(id="start-date-filter", type="date", 
                                  style={'border': '1px solid #ced4da', 'borderRadius': '4px', 'padding': '6px', 'fontSize': '14px', 'width': '150px', 'marginRight': '10px'}),
                        dbc.Input(id="end-date-filter", type="date", 
                                  style={'border': '1px solid #ced4da', 'borderRadius': '4px', 'padding': '6px', 'fontSize': '14px', 'width': '150px'}),
                        dbc.Button("Exportar como PDF", id="export-pdf-btn", color="primary", className="ms-2", 
                                   style={'width': '150px', 'fontSize': '14px', 'padding': '6px'})
                    ], style={'display': 'flex', 'gap': '10px'})
                ], style={'display': 'flex', 'flexDirection': 'column'}),
            ])
        ], width=8, className="d-flex justify-content-end align-items-end")
    ], justify="between"),
    # Tabela
    dash_table.DataTable(
        id='report-table',
        columns=[
            {"name": "CNP", "id": "cnp", "type": "numeric"},
            {"name": "Razão Social", "id": "razao_social", "type": "text"},
            {"name": "Início Vigência", "id": "inicio_vigencia_seguro", "type": "text"},
            {"name": "Vencimento", "id": "vencimento", "type": "text"},
            {"name": "Valor Cobertura", "id": "valor_cobertura", "type": "text"},
            {"name": "Valor Parcela", "id": "valor_parcela", "type": "text"},
        ],
        data=[],
        style_table={'overflowX': 'auto', 'border': '1px solid #ddd'},
        style_header={'backgroundColor': '#007bff', 'color': 'white', 'fontWeight': 'bold', 'textAlign': 'center'},
        style_data={'textAlign': 'center', 'border': '1px solid #ddd', 'fontSize': '14px'},
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
    with engine.connect() as conn:
        query = text("""
            SELECT 
                d.cnp,
                d.razao_social,
                s.inicio_vigencia_seguro,
                s.vencimento,
                s.valor_cobertura,
                s.valor_parcela
            FROM cnp_data d
            LEFT JOIN seguradora s ON d.cnp = s.cnp
        """)
        df = pd.read_sql(query, conn)

        df["inicio_vigencia_seguro"] = df["inicio_vigencia_seguro"].apply(
            lambda x: x.strftime("%d/%m/%y") if pd.notnull(x) else ""
        )
        df["vencimento"] = df["vencimento"].apply(
            lambda x: x.strftime("%d/%m/%y") if pd.notnull(x) else ""
        )
        df["valor_cobertura"] = df["valor_cobertura"].apply(
            lambda x: f"R$ {float(x):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") if pd.notnull(x) else ""
        )
        df["valor_parcela"] = df["valor_parcela"].apply(
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
    data = [["CNP", "Razão Social", "Início Vigência", "Vencimento", "Valor Cobertura", "Valor Parcela"]]
    for row in table_data:
        data.append([
            str(row["cnp"]),
            row["razao_social"],
            row["inicio_vigencia_seguro"],
            row["vencimento"],
            row["valor_cobertura"],
            row["valor_parcela"]
        ])

    # Definir larguras das colunas
    col_widths = [40, 230, 80, 80, 80, 80]

    table = Table(data, colWidths=col_widths)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#007bff")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),  # Ajustado para caber melhor
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 7),  # Ajustado para caber melhor
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)

    # Rodapé
    elements.append(Spacer(1, 10))
    footer = Paragraph("Relatório gerado pelo CentralSeg GECAF - Central de Seguros para Gestão, Controle e Apoio Financeiro", footer_style)
    elements.append(footer)

    doc.build(elements)
    buffer.seek(0)

    return dcc.send_bytes(buffer.getvalue(), "relatorio_seguros.pdf")