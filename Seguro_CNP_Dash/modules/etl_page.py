import base64
import io
from dash import html, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc
from etl.etl import rodar_etl

layout = html.Div([
    html.H3("Executar ETL", className="mb-4"),
    dcc.Upload(
        id='upload-data',
        children=html.Div(['Arraste ou ', html.A('selecione um arquivo Excel', style={'color': '#007bff'})]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px 0',
            'backgroundColor': '#f8f9fa'
        },
        accept='.xlsx, .xls',
        multiple=False
    ),
    html.Div(id='output-filename', style={'margin': '10px 0'}),
    html.Div([
        dbc.Button("Executar ETL", id="btn-run-etl", n_clicks=0, color="primary", className="me-2"),
        dbc.Button("Limpar", id="btn-clear", n_clicks=0, color="secondary"),
    ], style={'margin': '10px 0'}),
    dcc.Loading(
        id="loading-etl",
        type="default",
        children=html.Div(id="output-etl", style={'margin': '10px 0'})
    ),
    dbc.Toast(
        "ETL executado com sucesso!",
        id="etl-success-toast",
        header="Sucesso",
        icon="success",
        duration=2000,
        is_open=False,
        style={
            'position': 'fixed',
            'top': '10px',
            'right': '10px',
            'width': '300px',
            'zIndex': 1000
        }
    )
])

@callback(
    Output("output-filename", "children"),
    Output("output-etl", "children"),
    Output("upload-data", "contents"),
    Output("upload-data", "filename"),
    Output("etl-success-toast", "is_open"),
    Input("upload-data", "filename"),
    Input("btn-run-etl", "n_clicks"),
    Input("btn-clear", "n_clicks"),
    State("upload-data", "contents"),
    State("upload-data", "filename"),
    prevent_initial_call=True
)
def update_etl(filename_trigger, n_clicks_run, n_clicks_clear, contents, filename):
    from dash import callback_context
    ctx = callback_context

    if not ctx.triggered:
        return None, None, None, None, False

    trigger = ctx.triggered[0]['prop_id'].split('.')[0]

    if trigger == "btn-clear":
        return None, None, None, None, False

    if trigger == "btn-run-etl" and contents and filename:
        if not filename.endswith(('.xlsx', '.xls')):
            return None, html.P("Erro: Por favor, selecione um arquivo Excel (.xlsx ou .xls).", style={"color": "#dc3545"}), None, None, False
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        excel_file = io.BytesIO(decoded)
        try:
            rodar_etl(excel_file)
            return None, None, None, None, True
        except Exception as e:
            return None, html.P(f"Erro ao executar ETL: {str(e)}", style={"color": "#dc3545"}), None, None, False

    if trigger == "upload-data" and filename_trigger:
        if filename_trigger.endswith(('.xlsx', '.xls')):
            # Retorna os dados do upload sem limpar, mantendo-os para o ETL
            return html.P(f"Arquivo carregado: {filename_trigger}", style={"color": "#495057"}), None, contents, filename_trigger, False
        return html.P("Erro: Por favor, selecione um arquivo Excel (.xlsx ou .xls).", style={"color": "#dc3545"}), None, contents, filename_trigger, False

    return None, None, None, None, False
