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
import io
import base64

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
            {"name": "Observação", "id": "obs", "type": "text"}
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
                s.valor_parcela,
                s.obs
            FROM cnp_data d
            LEFT JOIN seguradora s ON d.cnp = s.cnp
        """)
        df = pd.read_sql(query, conn)

        df["inicio_vigencia_seguro"] = df["inicio_vigencia_seguro"].apply(
            lambda x: x.strftime("%d/%m/%Y") if pd.notnull(x) else ""
        )
        df["vencimento"] = df["vencimento"].apply(
            lambda x: x.strftime("%d/%m/%Y") if pd.notnull(x) else ""
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
            df["vencimento_dt"] = pd.to_datetime(df["vencimento"], format="%d/%m/%Y", errors='coerce')
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
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    elements = []

    styles = getSampleStyleSheet()
    title = Paragraph("Relatório de Seguros", styles['Heading1'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    data = [["CNP", "Razão Social", "Início Vigência", "Vencimento", "Valor Cobertura", "Valor Parcela", "Observação"]]
    for row in table_data:
        data.append([
            str(row["cnp"]),
            row["razao_social"],
            row["inicio_vigencia_seguro"],
            row["vencimento"],
            row["valor_cobertura"],
            row["valor_parcela"],
            row["obs"] if row["obs"] else ""
        ])

    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#007bff")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)

    doc.build(elements)
    buffer.seek(0)

    return dcc.send_bytes(buffer.getvalue(), "relatorio_seguros.pdf")