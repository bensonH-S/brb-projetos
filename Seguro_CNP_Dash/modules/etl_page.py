import base64
import io
from dash import html, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc
from etl.etl import rodar_etl

# Layout principal da aba "ETL"
layout = html.Div([
    # Título da página
    html.H3("Executar ETL", className="mb-4",
            style={"fontSize": "28px", "fontWeight": "bold", "color": "#023e7c"}),  # Adicionada a cor #023e7c para consistência
    
    # Componente de upload para selecionar o arquivo Excel
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Arraste ou ',
            html.A('selecione um arquivo Excel', style={'color': '#023e7c'})  # Ajustada a cor do link para #023e7c
        ]),
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
        accept='.xlsx, .xls',  # Aceita apenas arquivos Excel
        multiple=False  # Permite apenas um arquivo por vez
    ),
    
    # Div para exibir o nome do arquivo carregado ou mensagens de erro
    html.Div(id='output-filename', style={'margin': '10px 0'}),
    
    # Div com os botões "Executar ETL" e "Limpar"
    html.Div([
        # Botão para executar o processo de ETL
        dbc.Button("Executar ETL", id="btn-run-etl", n_clicks=0, color="primary",
                   className="me-2", style={'backgroundColor': '#023e7c', 'borderColor': '#023e7c'}),  # Ajustada a cor para #023e7c
        # Botão para limpar o upload
        dbc.Button("Limpar", id="btn-clear", n_clicks=0, color="secondary"),
    ], style={'margin': '10px 0'}),
    
    # Componente de loading para indicar que o ETL está em execução
    dcc.Loading(
        id="loading-etl",
        type="default",  # Tipo de spinner (padrão)
        children=html.Div(id="output-etl", style={'margin': '10px 0'})  # Div para exibir mensagens de saída do ETL
    ),
    
    # Toast de sucesso para notificar que o ETL foi executado
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

# Callback para gerenciar o upload, execução do ETL e limpeza
@callback(
    Output("output-filename", "children"),  # Exibe o nome do arquivo ou mensagens de erro
    Output("output-etl", "children"),  # Exibe mensagens de saída do ETL
    Output("upload-data", "contents"),  # Limpa o conteúdo do upload
    Output("upload-data", "filename"),  # Limpa o nome do arquivo
    Output("etl-success-toast", "is_open"),  # Controla a exibição do toast de sucesso
    Input("upload-data", "filename"),  # Trigger para quando um arquivo é selecionado
    Input("btn-run-etl", "n_clicks"),  # Trigger para o botão "Executar ETL"
    Input("btn-clear", "n_clicks"),  # Trigger para o botão "Limpar"
    State("upload-data", "contents"),  # Conteúdo do arquivo enviado
    State("upload-data", "filename"),  # Nome do arquivo enviado
    prevent_initial_call=True
)
def update_etl(filename_trigger, n_clicks_run, n_clicks_clear, contents, filename):
    from dash import callback_context
    ctx = callback_context

    # Verifica se o callback foi acionado
    if not ctx.triggered:
        return None, None, None, None, False

    # Identifica qual componente disparou o callback
    trigger = ctx.triggered[0]['prop_id'].split('.')[0]

    # Ação do botão "Limpar": reseta o upload e mensagens
    if trigger == "btn-clear":
        return None, None, None, None, False

    # Ação do botão "Executar ETL": processa o arquivo Excel
    if trigger == "btn-run-etl" and contents and filename:
        # Valida a extensão do arquivo
        if not filename.endswith(('.xlsx', '.xls')):
            return None, html.P("Erro: Por favor, selecione um arquivo Excel (.xlsx ou .xls).", style={"color": "#dc3545"}), None, None, False
        
        # Decodifica o conteúdo do arquivo
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        excel_file = io.BytesIO(decoded)
        
        try:
            # Executa o processo de ETL
            rodar_etl(excel_file)
            return None, None, None, None, True  # Exibe o toast de sucesso
        except Exception as e:
            # Exibe mensagem de erro se o ETL falhar
            return None, html.P(f"Erro ao executar ETL: {str(e)}", style={"color": "#dc3545"}), None, None, False

    # Ação ao selecionar um arquivo: exibe o nome do arquivo
    if trigger == "upload-data" and filename_trigger:
        if filename_trigger.endswith(('.xlsx', '.xls')):
            # Retorna os dados do upload sem limpar, mantendo-os para o ETL
            return html.P(f"Arquivo carregado: {filename_trigger}", style={"color": "#495057"}), None, contents, filename_trigger, False
        return html.P("Erro: Por favor, selecione um arquivo Excel (.xlsx ou .xls).", style={"color": "#dc3545"}), None, contents, filename_trigger, False

    return None, None, None, None, False