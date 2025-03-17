import dash
from dash import dcc, html, dash_table, callback_context
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
from database.connection import engine
from sqlalchemy import text

# Layout da página de CNPs
layout = html.Div([
    html.H3("Cadastro das Conveniência BRB", className="text-center mb-4", style={"fontSize": "28px", "fontWeight": "bold", "color": "#007bff"}),
    
    # Botão para adicionar novo CNP
    dbc.Row([
        dbc.Col(dbc.Button("+ Adicionar Novo CNP", id="open-modal", color="primary", className="mb-3"), width=3),
    ], justify="start"),
    
    # Tabela para exibir os CNPs cadastrados
    dash_table.DataTable(
        id='cnp-table',
        columns=[
            {"name": "CNP", "id": "cnp", "type": "numeric"},
            {"name": "Situação", "id": "situacao", "type": "text"},
            {"name": "CNPJ", "id": "cnpj", "type": "text"},
            {"name": "Razão Social", "id": "razao_social", "type": "text"},
            {"name": "Editar", "id": "editar", "type": "text"},
            {"name": "Excluir", "id": "excluir", "type": "text"}
        ],
        data=[],
        style_table={'overflowX': 'auto', 'border': '1px solid #ddd'},
        style_header={'backgroundColor': '#007bff', 'color': 'white', 'fontWeight': 'bold', 'textAlign': 'center'},
        style_data={'textAlign': 'center', 'border': '1px solid #ddd', 'fontSize': '14px'},
        style_cell={'padding': '8px'},
        style_cell_conditional=[
            {'if': {'column_id': 'editar'}, 'width': '80px'},
            {'if': {'column_id': 'excluir'}, 'width': '80px'}
        ],
        page_size=10
    ),
    
    # Modal para adicionar/editar CNP
    dbc.Modal([
        dbc.ModalHeader("Adicionar/Editar CNP"),
        dbc.ModalBody([
            html.Div(id="modal-content"),
            # Mensagem de sucesso
            dbc.Alert(
                "Alteração realizada com sucesso!",
                id="save-success-alert",
                color="success",
                dismissable=False,
                is_open=False,
                duration=3000  # Aparece por 3 segundos
            )
        ]),
        dbc.ModalFooter([
            dbc.Button("Salvar", id="save-cnp", color="success"),
            dbc.Button("Cancelar", id="close-modal", color="danger"),
        ]),
    ], id="modal-cnp", is_open=False),
    
    # Modal de confirmação para exclusão
    dbc.Modal([
        dbc.ModalHeader("Confirmação de Exclusão"),
        dbc.ModalBody("Tem certeza que deseja excluir este CNP? Esta ação não pode ser desfeita."),
        dbc.ModalFooter([
            dbc.Button("Excluir", id="confirm-delete", color="danger"),
            dbc.Button("Cancelar", id="cancel-delete", color="secondary"),
        ]),
    ], id="modal-delete", is_open=False)
])

# Callback para carregar e atualizar os dados da tabela
@dash.callback(
    Output("cnp-table", "data"),
    Input("cnp-table", "id")
)
def load_cnp_data(_):
    try:
        with engine.connect() as conn:
            query = text("SELECT cnp, situacao, cnpj, razao_social FROM cnp_data")
            df = pd.read_sql(query, conn)
            df["situacao"] = df["situacao"].apply(lambda x: "ATIVA" if x == 1 else "INATIVA")
            df["editar"] = "✏️ Editar"
            df["excluir"] = "🗑️ Excluir"
        return df.to_dict("records")
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return []

# Callback para abrir o modal de edição
@dash.callback(
    [Output("modal-cnp", "is_open", allow_duplicate=True), Output("modal-content", "children")],
    [Input("cnp-table", "active_cell"), Input("open-modal", "n_clicks")],
    State("cnp-table", "data"),
    prevent_initial_call=True
)
def open_edit_modal(active_cell, n_clicks, table_data):
    ctx = callback_context.triggered[0]["prop_id"]
    
    if ctx == "open-modal.n_clicks" and n_clicks:
        modal_content = html.Div([
            dbc.Row([
                dbc.Col(dbc.Label("CNP:"), width=4),
                dbc.Col(dbc.Input(id="input-cnp", type="text", placeholder="Digite o CNP"), width=8),
            ], className="mb-2"),
            dbc.Row([
                dbc.Col(dbc.Label("Situação:"), width=4),
                dbc.Col(dcc.Dropdown(id="input-situacao", options=[
                    {"label": "ATIVA", "value": 1},
                    {"label": "INATIVA", "value": 0}
                ], value=1, clearable=False), width=8),
            ], className="mb-2"),
            dbc.Row([
                dbc.Col(dbc.Label("CNPJ:"), width=4),
                dbc.Col(dbc.Input(id="input-cnpj", type="text", placeholder="Digite o CNPJ"), width=8),
            ], className="mb-2"),
            dbc.Row([
                dbc.Col(dbc.Label("Razão Social:"), width=4),
                dbc.Col(dbc.Input(id="input-razao", type="text", placeholder="Digite a Razão Social"), width=8),
            ], className="mb-2"),
        ])
        return True, modal_content
    
    if ctx == "cnp-table.active_cell" and active_cell and active_cell["column_id"] == "editar":
        row = active_cell["row"]
        selected_cnp = table_data[row]
        modal_content = html.Div([
            dbc.Row([
                dbc.Col(dbc.Label("CNP:"), width=4),
                dbc.Col(dbc.Input(id="input-cnp", type="text", value=selected_cnp["cnp"], disabled=True), width=8),
            ], className="mb-2"),
            dbc.Row([
                dbc.Col(dbc.Label("Situação:"), width=4),
                dbc.Col(dcc.Dropdown(id="input-situacao", options=[
                    {"label": "ATIVA", "value": 1},
                    {"label": "INATIVA", "value": 0}
                ], value=1 if selected_cnp["situacao"] == "ATIVA" else 0, clearable=False), width=8),
            ], className="mb-2"),
            dbc.Row([
                dbc.Col(dbc.Label("CNPJ:"), width=4),
                dbc.Col(dbc.Input(id="input-cnpj", type="text", value=selected_cnp["cnpj"]), width=8),
            ], className="mb-2"),
            dbc.Row([
                dbc.Col(dbc.Label("Razão Social:"), width=4),
                dbc.Col(dbc.Input(id="input-razao", type="text", value=selected_cnp["razao_social"]), width=8),
            ], className="mb-2"),
        ])
        return True, modal_content
    
    return False, None

# Callback para abrir o modal de exclusão
@dash.callback(
    Output("modal-delete", "is_open"),
    Input("cnp-table", "active_cell"),
    State("cnp-table", "data"),
    prevent_initial_call=True
)
def open_delete_modal(active_cell, table_data):
    if active_cell and active_cell["column_id"] == "excluir":
        return True
    return False

# Callback para confirmar a exclusão
@dash.callback(
    [Output("modal-delete", "is_open", allow_duplicate=True), Output("cnp-table", "data", allow_duplicate=True)],
    [Input("confirm-delete", "n_clicks"), Input("cancel-delete", "n_clicks")],
    State("cnp-table", "data"),
    State("cnp-table", "active_cell"),
    prevent_initial_call=True
)
def confirm_delete(confirm_clicks, cancel_clicks, table_data, active_cell):
    ctx = callback_context.triggered[0]["prop_id"]
    
    if not active_cell:
        return False, table_data
    
    row = active_cell["row"]
    selected_cnp = table_data[row]["cnp"]
    
    if ctx == "confirm-delete.n_clicks" and confirm_clicks:
        try:
            with engine.connect() as conn:
                with conn.begin():
                    query = text("DELETE FROM cnp_data WHERE cnp = :cnp")
                    result = conn.execute(query, {"cnp": selected_cnp})
                    if result.rowcount > 0:
                        print(f"CNP {selected_cnp} excluído com sucesso do banco de dados.")
                    else:
                        print(f"Nenhum registro encontrado para CNP {selected_cnp} no banco.")
            updated_data = [row for row in table_data if row["cnp"] != selected_cnp]
            return False, updated_data
        except Exception as e:
            print(f"Erro ao excluir CNP do banco de dados: {e}")
            return False, table_data
    
    elif ctx == "cancel-delete.n_clicks" and cancel_clicks:
        return False, table_data
    
    return True, table_data

# Callback para salvar alterações e controlar o modal
@dash.callback(
    [Output("cnp-table", "data", allow_duplicate=True), 
     Output("modal-cnp", "is_open", allow_duplicate=True), 
     Output("save-success-alert", "is_open")],
    [Input("save-cnp", "n_clicks"), Input("close-modal", "n_clicks")],
    [State("input-cnp", "value"), State("input-situacao", "value"), 
     State("input-cnpj", "value"), State("input-razao", "value"), 
     State("cnp-table", "data")],
    prevent_initial_call=True
)
def save_or_cancel_cnp(save_clicks, cancel_clicks, cnp, situacao, cnpj, razao_social, table_data):
    ctx = callback_context.triggered[0]["prop_id"]
    
    if ctx == "close-modal.n_clicks" and cancel_clicks:
        return table_data, False, False  # Fecha o modal sem salvar
    
    if ctx == "save-cnp.n_clicks" and save_clicks:
        try:
            with engine.connect() as conn:
                with conn.begin():
                    query_check = text("SELECT COUNT(*) FROM cnp_data WHERE cnp = :cnp")
                    exists = conn.execute(query_check, {"cnp": cnp}).scalar() > 0
                    if exists:
                        query = text("""
                            UPDATE cnp_data 
                            SET situacao = :situacao, cnpj = :cnpj, razao_social = :razao_social 
                            WHERE cnp = :cnp
                        """)
                    else:
                        query = text("""
                            INSERT INTO cnp_data (cnp, situacao, cnpj, razao_social) 
                            VALUES (:cnp, :situacao, :cnpj, :razao_social)
                        """)
                    conn.execute(query, {
                        "cnp": cnp, 
                        "situacao": situacao, 
                        "cnpj": cnpj, 
                        "razao_social": razao_social
                    })
            # Recarrega os dados da tabela após salvar
            with engine.connect() as conn:
                query = text("SELECT cnp, situacao, cnpj, razao_social FROM cnp_data")
                df = pd.read_sql(query, conn)
                df["situacao"] = df["situacao"].apply(lambda x: "ATIVA" if x == 1 else "INATIVA")
                df["editar"] = "✏️ Editar"
                df["excluir"] = "🗑️ Excluir"
            # Retorna os dados atualizados, mantém o modal aberto por 3s para mostrar o alerta, e ativa o alerta
            return df.to_dict("records"), True, True
        except Exception as e:
            print(f"Erro ao salvar CNP: {e}")
            return table_data, False, False
    
    return table_data, True, False

# Callback para fechar o modal após o alerta desaparecer
@dash.callback(
    Output("modal-cnp", "is_open", allow_duplicate=True),
    Input("save-success-alert", "is_open"),
    State("modal-cnp", "is_open"),
    prevent_initial_call=True
)
def close_modal_after_alert(alert_is_open, modal_is_open):
    if not alert_is_open and modal_is_open:
        return False  # Fecha o modal quando o alerta desaparece
    return modal_is_open  # Mantém o estado atual do modal