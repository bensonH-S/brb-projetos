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
import logging

# Configurar logging para depuração
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Definir o tamanho da página como A4 em paisagem (297 mm x 210 mm)
PAGE_SIZE = (A4[1], A4[0])  # Inverte largura e altura para paisagem: 297 mm x 210 mm

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

    # Buscar os dados completos do banco de dados, incluindo os campos adicionais
    cnp_list = [row["cnp"] for row in table_data]
    # logger.info(f"CNPs para consulta: {cnp_list}")

    # Construir a cláusula IN manualmente para evitar problemas com SQLAlchemy
    if not cnp_list:
        return None  # Evitar query vazia

    cnp_list_str = ",".join(str(cnp) for cnp in cnp_list)
    query_str = f"""
        SELECT 
            d.cnp,
            d.razao_social,
            d.cnpj,  # Substituído s.inicio_vigencia_seguro por d.cnpj
            s.vencimento,
            d.cc,
            d.telefone,
            d.endereco,
            d.cidade,
            d.uf,
            d.cep,
            s.valor_proposto
        FROM cnp_data d
        LEFT JOIN seguradora s ON d.cnp = s.cnp
        WHERE d.cnp IN ({cnp_list_str})
    """
    # logger.info(f"Query gerada: {query_str}")

    with engine.connect() as conn:
        df_pdf = pd.read_sql(query_str, conn)

        # Formatar o vencimento
        df_pdf["vencimento"] = df_pdf["vencimento"].apply(
            lambda x: x.strftime("%d/%m/%y") if pd.notnull(x) else ""
        )
        # Formatar o valor proposto
        df_pdf["valor_proposto"] = df_pdf["valor_proposto"].apply(
            lambda x: f"R$ {float(x):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") if pd.notnull(x) else ""
        )
        # Formatar o CNPJ (opcional, se necessário)
        df_pdf["cnpj"] = df_pdf["cnpj"].apply(
            lambda x: f"{str(x)[:2]}.{str(x)[2:5]}.{str(x)[5:8]}/{str(x)[8:12]}-{str(x)[12:14]}" if pd.notnull(x) and len(str(x)) == 14 else str(x)
        )

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=PAGE_SIZE, leftMargin=0.5*cm, rightMargin=0.5*cm, topMargin=1*cm, bottomMargin=1*cm)
    elements = []

    styles = getSampleStyleSheet()
    # Estilo personalizado para o título
    title_style = styles['Heading1']
    title_style.alignment = 1  # Centralizado
    title_style.fontSize = 14
    title_style.spaceAfter = 8

    # Estilo para subtítulo (data de geração)
    subtitle_style = styles['Normal']
    subtitle_style.alignment = 1
    subtitle_style.fontSize = 8
    subtitle_style.textColor = colors.grey
    subtitle_style.spaceAfter = 10

    # Estilo para o rodapé
    footer_style = styles['Normal']
    footer_style.alignment = 1
    footer_style.fontSize = 7
    footer_style.textColor = colors.grey

    # Estilo para as células da tabela
    cell_style = styles['Normal']
    cell_style.fontSize = 8
    cell_style.leading = 9  # Espaçamento entre linhas
    cell_style.textColor = colors.black  # Cor preta para o texto

    # Cabeçalho
    title = Paragraph("Relatório de Seguros", title_style)
    current_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    subtitle = Paragraph(f"Gerado em: {current_date}", subtitle_style)
    elements.append(title)
    elements.append(subtitle)
    elements.append(Spacer(1, 10))

    # Dados da tabela
    data = [["CNP", "Razão Social", "CNPJ", "Vencimento", "CC", "Telefone", "Endereço", "Cidade", "UF", "CEP", "Valor Proposto"]]  # Substituído "Início Vig." por "CNPJ"
    for _, row in df_pdf.iterrows():
        data.append([
            Paragraph(str(row["cnp"]), cell_style),
            Paragraph(row["razao_social"], cell_style),
            Paragraph(row["cnpj"], cell_style),  # Substituído inicio_vigencia_seguro por cnpj
            Paragraph(row["vencimento"], cell_style),
            Paragraph(str(row["cc"]), cell_style),
            Paragraph(str(row["telefone"]), cell_style),
            Paragraph(row["endereco"], cell_style),
            Paragraph(row["cidade"], cell_style),
            Paragraph(row["uf"], cell_style),
            Paragraph(str(row["cep"]), cell_style),
            Paragraph(row["valor_proposto"], cell_style)
        ])

    # Definir larguras das colunas (em pontos) para ocupar o espaço disponível
    # Largura total disponível em paisagem: 297 mm - 1 cm (margens) = 287 mm = 814 pontos
    col_widths = [38, 160, 78, 60, 60, 55, 162, 63, 30, 50, 70]  # Total: 814 pontos

    table = Table(data, colWidths=col_widths)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#023e7c")),  # Cabeçalho azul escuro
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('ALIGN', (0, 1), (0, -1), 'CENTER'),  # CNP
        ('ALIGN', (1, 1), (1, -1), 'LEFT'),    # Razão Social
        ('ALIGN', (2, 1), (-1, -1), 'CENTER'), # Demais colunas
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 2),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
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