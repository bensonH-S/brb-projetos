# Importação das bibliotecas necessárias
import dash  # Framework para criar aplicações web interativas
from dash import dcc, html, callback_context  # Componentes do Dash: controle de componentes, HTML e contexto de callback
from dash.dependencies import Input, Output, State  # Dependências para gerenciar entradas, saídas e estados nos callbacks
import dash_bootstrap_components as dbc  # Componentes estilizados do Bootstrap para Dash
import dash_table  # Tabela interativa do Dash
import pandas as pd  # Biblioteca para manipulação de dados em formato tabular
from sqlalchemy import text  # Para executar consultas SQL de forma segura
from database.connection import engine  # Conexão com o banco de dados configurada em outro módulo
import datetime  # Para manipulação de datas
import base64  # Para decodificar arquivos enviados em base64
import io  # Para manipulação de streams de entrada/saída
from etl.importa_seguradora import importar_seguradora  # Função externa para importar dados de seguradora de planilhas

# Definição do layout da página
layout = html.Div([
    # Título da página centralizado
    html.H3("Informações de Seguros", className="text-center mb-4",
            style={"fontSize": "28px", "fontWeight": "bold", "color": "#023e7c", "marginTop": "30px"}),  # Estilo personalizado com cor azul escura
    
    # Linha com campo de busca e botões
    dbc.Row([
        # Coluna para o campo de busca
        dbc.Col(
            dbc.Input(id="search-seguro", type="text",
                      placeholder="Buscar Seguro por CNP ou Razão Social...",
                      className="mb-3"), width=4),  # Campo de texto para filtrar seguros
        
        # Coluna para botões de ação (Adicionar e Importar)
        dbc.Col([
            dbc.Button("+ Adicionar Novo Seguro", id="open-seguro-modal", color="primary",
                       className="mb-3 me-2"),  # Botão para abrir modal de criação de novo seguro
            dcc.Upload(
                id='upload-seguro-data',
                children=dbc.Button("Importar Planilha", color="secondary", className="mb-3"),
                multiple=False,  # Permite apenas um arquivo por vez
                accept=".xlsx"  # Aceita apenas arquivos Excel
            )
        ], width=8, className="d-flex justify-content-end"),  # Alinhamento à direita
    ], justify="between"),  # Espaçamento entre os elementos da linha

    # Tabela para exibir os dados dos seguros
    dash_table.DataTable(
        id='seguro-table',
        columns=[  # Definição das colunas da tabela
            {"name": "CNP", "id": "cnp", "type": "numeric"},
            {"name": "CNPJ", "id": "cnpj", "type": "text"},
            {"name": "Razão Social", "id": "razao_social", "type": "text"},
            {"name": "Início Vigência", "id": "inicio_vigencia_seguro", "type": "text"},
            {"name": "Vencimento", "id": "vencimento", "type": "text"},
            {"name": "Valor Cobertura", "id": "valor_cobertura", "type": "text"},
            {"name": "Valor Parcela", "id": "valor_parcela", "type": "text"},
            {"name": "Detalhes", "id": "editar", "type": "text"},  # Coluna para ação de visualizar/editar
            {"name": "Excluir", "id": "excluir", "type": "text"}  # Coluna para ação de exclusão
        ],
        data=[],  # Dados inicialmente vazios, serão preenchidos via callback
        style_table={'overflowX': 'auto', 'border': '1px solid #ddd'},  # Estilo da tabela com rolagem horizontal
        style_header={'backgroundColor': '#023e7c', 'color': 'white',  # Cabeçalho azul escuro com texto branco
                      'fontWeight': 'bold', 'textAlign': 'center'},
        style_data={'textAlign': 'center', 'border': '1px solid #ddd', 'fontSize': '14px'},  # Estilo dos dados
        style_cell={'padding': '8px'},  # Padding das células
        style_cell_conditional=[  # Estilos condicionais para colunas específicas
            {'if': {'column_id': 'editar'}, 'width': '80px'},
            {'if': {'column_id': 'excluir'}, 'width': '80px'}
        ],
        page_size=15,  # Número de linhas por página
    ),
    
    # Armazenamento temporário para controle de ações
    dcc.Store(id="seguro-edit-action", data=0),  # Contador de ações de edição
    dcc.Store(id="seguro-edit-mode", data=False),  # Estado do modo de edição (ativo/inativo)
    
    # Notificações (toasts) para feedback ao usuário
    dbc.Toast(
        "Alteração realizada com sucesso!",
        id="seguro-save-success-toast",
        header="Sucesso",
        icon="success",
        duration=2000,  # Duração em milissegundos
        is_open=False,  # Inicialmente fechado
        style={'position': 'fixed', 'top': '10px', 'right': '10px', 'width': '300px', 'zIndex': 1000}  # Posição fixa no canto superior direito
    ),
    dbc.Toast(
        "Seguro excluído com sucesso!",
        id="seguro-delete-success-toast",
        header="Sucesso",
        icon="success",
        duration=2000,
        is_open=False,
        style={'position': 'fixed', 'top': '10px', 'right': '10px', 'width': '300px', 'zIndex': 1000}
    ),
    dbc.Toast(
        id="seguro-import-success-toast",
        header="Sucesso",
        icon="success",
        duration=3000,
        is_open=False,
        style={'position': 'fixed', 'top': '10px', 'right': '10px', 'width': '300px', 'zIndex': 1000}
    ),
    dbc.Toast(
        id="seguro-import-error-toast",
        header="Erro",
        icon="danger",
        duration=3000,
        is_open=False,
        style={'position': 'fixed', 'top': '10px', 'right': '10px', 'width': '300px', 'zIndex': 1000}
    ),
    
    # Modal para visualização/edição de seguro
    dbc.Modal([
        dbc.ModalHeader("Visualizar Seguro"),  # Título do modal
        dbc.ModalBody(id="seguro-modal-body"),  # Conteúdo dinâmico do modal
        dbc.ModalFooter([
            dbc.Button("Editar", id="seguro-enable-edit-btn", color="primary", style={'display': 'block'}),  # Botão para ativar modo de edição
            dbc.Button("Salvar", id="seguro-save-btn", color="success", style={'display': 'none'}),  # Botão para salvar alterações (inicialmente oculto)
            dbc.Button("Cancelar", id="seguro-close-modal-btn", color="danger", className="ms-2")  # Botão para fechar o modal
        ])
    ], id="modal-seguro", is_open=False),  # Modal inicialmente fechado
    
    # Modal para confirmação de exclusão
    dbc.Modal([
        dbc.ModalHeader("Confirmação de Exclusão"),
        dbc.ModalBody("Tem certeza que deseja excluir este seguro? Esta ação não pode ser desfeita."),
        dbc.ModalFooter([
            dbc.Button("Excluir", id="seguro-confirm-delete-btn", color="danger"),  # Botão para confirmar exclusão
            dbc.Button("Cancelar", id="seguro-cancel-delete-btn", color="secondary")  # Botão para cancelar exclusão
        ])
    ], id="modal-seguro-delete", is_open=False)  # Modal inicialmente fechado
])

# Callback para carregar e atualizar os dados da tabela
@dash.callback(
    Output("seguro-table", "data"),  # Atualiza os dados da tabela
    [Input("seguro-table", "id"), Input("search-seguro", "value"), Input("upload-seguro-data", "contents")]  # Entradas que disparam o callback
)
def load_seguro_data(_, search_value, _upload):
    # Função para carregar os dados do banco e formatá-los para a tabela
    try:
        with engine.connect() as conn:  # Conexão com o banco de dados
            # Consulta SQL para unir dados de seguradoras e informações básicas
            query = text("""
                SELECT 
                  d.cnp,
                  d.cnpj,
                  d.razao_social,
                  s.inicio_vigencia_seguro,
                  s.vencimento,
                  s.valor_cobertura,
                  s.valor_parcela,
                  s.obs
                FROM cnp_data d
                LEFT JOIN seguradora s ON d.cnp = s.cnp
            """)
            df = pd.read_sql(query, conn)  # Carrega os dados em um DataFrame
            
            # Formatação das colunas de data e valores monetários
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
            
            # Adiciona botões de ação (editar e excluir) como texto
            df["editar"] = "🔍 Detalhes"
            df["excluir"] = "🗑️ Excluir"
            
            # Filtra os dados com base no valor de busca, se fornecido
            if search_value:
                df = df[df["cnp"].astype(str).str.contains(search_value, case=False, na=False) |
                        df["razao_social"].str.contains(search_value, case=False, na=False)]
        
        return df.to_dict("records")  # Retorna os dados no formato esperado pela tabela
    except Exception as e:
        print(f"Erro ao carregar dados de seguro: {e}")  # Log de erro
        return []  # Retorna lista vazia em caso de erro

# Callback para importar dados de uma planilha Excel
@dash.callback(
    [Output("seguro-import-success-toast", "is_open"),  # Abre toast de sucesso
     Output("seguro-import-success-toast", "children"),  # Mensagem do toast de sucesso
     Output("seguro-import-error-toast", "is_open"),  # Abre toast de erro
     Output("seguro-import-error-toast", "children")],  # Mensagem do toast de erro
    Input("upload-seguro-data", "contents"),  # Conteúdo do arquivo enviado
    State("upload-seguro-data", "filename")  # Nome do arquivo enviado
)
def import_seguro_data(contents, filename):
    # Verifica se há arquivo para processar
    if contents is None:
        return False, "", False, ""  # Nada a fazer se não houver upload
    
    try:
        # Decodifica o arquivo enviado (base64) para bytes
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        
        # Verifica se o arquivo é um Excel (.xlsx) e lê os dados
        if 'xlsx' in filename.lower():
            df = pd.read_excel(io.BytesIO(decoded), sheet_name="FOLLOW UP")
        else:
            return False, "", True, "Formato de arquivo não suportado. Use .xlsx"  # Erro se o formato for inválido
        
        # Chama função externa para processar a importação
        success, message = importar_seguradora(df)
        if success:
            return True, message, False, ""  # Sucesso na importação
        else:
            return False, "", True, message  # Erro na importação
    
    except Exception as e:
        error_msg = f"Erro ao processar o upload: {str(e)}"
        return False, "", True, error_msg  # Erro genérico no processamento

# Callback para abrir o modal de visualização/edição de seguro
@dash.callback(
    [Output("modal-seguro", "is_open"),  # Controla a visibilidade do modal
     Output("seguro-modal-body", "children"),  # Conteúdo do corpo do modal
     Output("seguro-edit-action", "data"),  # Contador de ações de edição
     Output("seguro-edit-mode", "data"),  # Estado do modo de edição
     Output("seguro-enable-edit-btn", "style"),  # Estilo do botão "Editar"
     Output("seguro-save-btn", "style")],  # Estilo do botão "Salvar"
    [Input("seguro-table", "active_cell"),  # Célula ativa na tabela
     Input("open-seguro-modal", "n_clicks"),  # Cliques no botão "Adicionar Novo Seguro"
     Input("seguro-edit-action", "data"),  # Contador de ações
     Input("seguro-enable-edit-btn", "n_clicks")],  # Cliques no botão "Editar"
    [State("seguro-table", "data"),  # Dados da tabela
     State("seguro-edit-mode", "data")],  # Estado atual do modo de edição
    prevent_initial_call=True  # Evita execução inicial
)
def open_seguro_modal(active_cell, n_clicks, edit_action, enable_edit_clicks, table_data, edit_mode):
    # Identifica qual evento disparou o callback
    ctx = callback_context.triggered[0]["prop_id"]
    
    # Caso o botão "Adicionar Novo Seguro" seja clicado
    if ctx == "open-seguro-modal.n_clicks" and n_clicks:
        # Cria o conteúdo do modal para adicionar um novo seguro
        modal_content = html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.Label("CNP:"),
                    dbc.Input(id="seguro-input-cnp", type="number", placeholder="Digite o CNP")
                ], width=6),
                dbc.Col([
                    dbc.Label("CNPJ:"),
                    dbc.Input(id="seguro-input-cnpj", type="text", placeholder="Digite o CNPJ")
                ], width=6)
            ], className="mb-2"),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Razão Social:"),
                    dbc.Input(id="seguro-input-razao-social", type="text", placeholder="Digite a Razão Social", disabled=True)
                ], width=12)
            ], className="mb-2"),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Início Vigência Seguro:"),
                    dbc.Input(id="seguro-input-inicio", type="text", placeholder="DD/MM/YYYY", value="", className="date-input")
                ], width=6),
                dbc.Col([
                    dbc.Label("Vencimento:"),
                    dbc.Input(id="seguro-input-vencimento", type="text", placeholder="DD/MM/YYYY", value="", className="date-input", disabled=True)
                ], width=6)
            ], className="mb-2"),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Valor Cobertura:"),
                    dbc.Input(id="seguro-input-valor-cobertura", type="text", placeholder="Digite o valor da cobertura", value="", disabled=True)
                ], width=6),
                dbc.Col([
                    dbc.Label("Valor Parcela:"),
                    dbc.Input(id="seguro-input-valor-parcela", type="text", placeholder="Digite o valor da parcela", value="")
                ], width=6)
            ], className="mb-2"),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Observação:"),
                    dbc.Textarea(id="seguro-input-obs", placeholder="Digite uma observação")
                ], width=12)
            ], className="mb-2"),
            html.Div(id="debito-fields", style={'display': 'none'})  # Campos de débitos ocultos inicialmente
        ])
        return True, dbc.ModalBody(modal_content), edit_action + 1, False, {'display': 'block'}, {'display': 'none'}
    
    # Caso o botão "Detalhes" seja clicado na tabela
    if ctx == "seguro-table.active_cell" and active_cell and active_cell["column_id"] == "editar":
        row = table_data[active_cell["row"]]  # Dados da linha selecionada
        
        # Busca informações adicionais no banco (débito e observações)
        with engine.connect() as conn:
            query = text("""
                SELECT numero_parcela, data_vencimento, status
                FROM pag_seguradora
                WHERE cnp = :cnp
                ORDER BY numero_parcela
            """)
            result = conn.execute(query, {"cnp": row["cnp"]}).fetchall()
            debitos = {f"debito{i}": {"data_vencimento": "", "status": ""} for i in range(1, 6)}  # Inicializa 5 débitos
            for debito in result:
                num_parcela = debito[0]
                data_vencimento = debito[1].strftime("%d/%m/%Y") if debito[1] else ""
                status = debito[2]
                debitos[f"debito{num_parcela}"] = {"data_vencimento": data_vencimento, "status": status}
            query_obs = text("SELECT obs FROM seguradora WHERE cnp = :cnp")
            obs_result = conn.execute(query_obs, {"cnp": row["cnp"]}).fetchone()
            obs = obs_result[0] if obs_result and obs_result[0] is not None else ""

        # Formata os valores monetários para exibição
        try:
            if isinstance(row["valor_parcela"], str) and row["valor_parcela"].startswith("R$"):
                temp = row["valor_parcela"].replace("R$", "").strip().replace(".", "").replace(",", ".")
                valor_parcela_num = float(temp)
            elif isinstance(row["valor_parcela"], (int, float)):
                valor_parcela_num = row["valor_parcela"]
            else:
                valor_parcela_num = None
            display_valor_parcela = f"{valor_parcela_num:.2f}" if valor_parcela_num is not None else ""
        except Exception:
            display_valor_parcela = row["valor_parcela"] if row["valor_parcela"] is not None else ""
        
        try:
            if isinstance(row["valor_cobertura"], str) and row["valor_cobertura"].startswith("R$"):
                temp = row["valor_cobertura"].replace("R$", "").strip().replace(".", "").replace(",", ".")
                valor_cobertura_num = float(temp)
            elif isinstance(row["valor_cobertura"], (int, float)):
                valor_cobertura_num = row["valor_cobertura"]
            else:
                valor_cobertura_num = None
            display_valor_cobertura = f"{valor_cobertura_num:.2f}" if valor_cobertura_num is not None else ""
        except Exception:
            display_valor_cobertura = row["valor_cobertura"] if row["valor_cobertura"] is not None else ""

        # Cria o conteúdo do modal com os dados do seguro
        modal_content = html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.Label("CNP:"),
                    dbc.Input(id="seguro-input-cnp", type="number", value=row["cnp"], disabled=True)
                ], width=6),
                dbc.Col([
                    dbc.Label("CNPJ:"),
                    dbc.Input(id="seguro-input-cnpj", type="text", value=row["cnpj"], disabled=True)
                ], width=6)
            ], className="mb-2"),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Razão Social:"),
                    dbc.Input(id="seguro-input-razao-social", type="text", value=row["razao_social"], disabled=True)
                ], width=12)
            ], className="mb-2"),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Início Vigência Seguro:"),
                    dbc.Input(id="seguro-input-inicio", type="text", placeholder="DD/MM/YYYY", value=row["inicio_vigencia_seguro"], className="date-input", disabled=not edit_mode)
                ], width=6),
                dbc.Col([
                    dbc.Label("Vencimento:"),
                    dbc.Input(id="seguro-input-vencimento", type="text", placeholder="DD/MM/YYYY", value=row["vencimento"], className="date-input", disabled=True)
                ], width=6)
            ], className="mb-2"),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Valor Cobertura:"),
                    dbc.Input(id="seguro-input-valor-cobertura", type="text", value=display_valor_cobertura, disabled=True)
                ], width=6),
                dbc.Col([
                    dbc.Label("Valor Parcela:"),
                    dbc.Input(id="seguro-input-valor-parcela", type="text", value=display_valor_parcela, disabled=not edit_mode)
                ], width=6)
            ], className="mb-2"),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Observação:"),
                    dbc.Textarea(id="seguro-input-obs", value=obs, disabled=not edit_mode)
                ], width=12)
            ], className="mb-2"),
            html.Div([
                html.Hr(),
                html.H5("Pagamentos de Parcelas", className="mb-3"),
                dbc.Row([
                    dbc.Col([
                        dbc.Label("Débito 1:"),
                        dbc.Input(id="seguro-debito1", type="text", value=debitos["debito1"]["data_vencimento"], disabled=True),
                        dcc.Checklist(id="seguro-debito1-check", options=[{"label": " Pago", "value": "pago"}], value=["pago"] if debitos["debito1"]["status"] == "PAGO" else [], style={'marginTop': '5px'})
                    ], width=4),
                    dbc.Col([
                        dbc.Label("Débito 2:"),
                        dbc.Input(id="seguro-debito2", type="text", value=debitos["debito2"]["data_vencimento"], disabled=True),
                        dcc.Checklist(id="seguro-debito2-check", options=[{"label": " Pago", "value": "pago"}], value=["pago"] if debitos["debito2"]["status"] == "PAGO" else [], style={'marginTop': '5px'})
                    ], width=4),
                    dbc.Col([
                        dbc.Label("Débito 3:"),
                        dbc.Input(id="seguro-debito3", type="text", value=debitos["debito3"]["data_vencimento"], disabled=True),
                        dcc.Checklist(id="seguro-debito3-check", options=[{"label": " Pago", "value": "pago"}], value=["pago"] if debitos["debito3"]["status"] == "PAGO" else [], style={'marginTop': '5px'})
                    ], width=4)
                ], className="mb-2"),
                dbc.Row([
                    dbc.Col([
                        dbc.Label("Débito 4:"),
                        dbc.Input(id="seguro-debito4", type="text", value=debitos["debito4"]["data_vencimento"], disabled=True),
                        dcc.Checklist(id="seguro-debito4-check", options=[{"label": " Pago", "value": "pago"}], value=["pago"] if debitos["debito4"]["status"] == "PAGO" else [], style={'marginTop': '5px'})
                    ], width=4),
                    dbc.Col([
                        dbc.Label("Débito 5:"),
                        dbc.Input(id="seguro-debito5", type="text", value=debitos["debito5"]["data_vencimento"], disabled=True),
                        dcc.Checklist(id="seguro-debito5-check", options=[{"label": " Pago", "value": "pago"}], value=["pago"] if debitos["debito5"]["status"] == "PAGO" else [], style={'marginTop': '5px'})
                    ], width=4)
                ], className="mb-2")
            ], id="debito-fields")
        ])
        return True, dbc.ModalBody(modal_content), edit_action + 1, edit_mode, {'display': 'block' if not edit_mode else 'none'}, {'display': 'none' if not edit_mode else 'block'}

    # Caso o botão "Editar" seja clicado no modal
    if ctx == "seguro-enable-edit-btn.n_clicks" and enable_edit_clicks:
        row = table_data[active_cell["row"]]
        with engine.connect() as conn:
            query = text("""
                SELECT numero_parcela, data_vencimento, status
                FROM pag_seguradora
                WHERE cnp = :cnp
                ORDER BY numero_parcela
            """)
            result = conn.execute(query, {"cnp": row["cnp"]}).fetchall()
            debitos = {f"debito{i}": {"data_vencimento": "", "status": ""} for i in range(1, 6)}
            for debito in result:
                num_parcela = debito[0]
                data_vencimento = debito[1].strftime("%d/%m/%Y") if debito[1] else ""
                status = debito[2]
                debitos[f"debito{num_parcela}"] = {"data_vencimento": data_vencimento, "status": status}
            query_obs = text("SELECT obs FROM seguradora WHERE cnp = :cnp")
            obs_result = conn.execute(query_obs, {"cnp": row["cnp"]}).fetchone()
            obs = obs_result[0] if obs_result and obs_result[0] is not None else ""

        try:
            if isinstance(row["valor_parcela"], str) and row["valor_parcela"].startswith("R$"):
                temp = row["valor_parcela"].replace("R$", "").strip().replace(".", "").replace(",", ".")
                valor_parcela_num = float(temp)
            elif isinstance(row["valor_parcela"], (int, float)):
                valor_parcela_num = row["valor_parcela"]
            else:
                valor_parcela_num = None
            display_valor_parcela = f"{valor_parcela_num:.2f}" if valor_parcela_num is not None else ""
        except Exception:
            display_valor_parcela = row["valor_parcela"] if row["valor_parcela"] is not None else ""
        
        try:
            if isinstance(row["valor_cobertura"], str) and row["valor_cobertura"].startswith("R$"):
                temp = row["valor_cobertura"].replace("R$", "").strip().replace(".", "").replace(",", ".")
                valor_cobertura_num = float(temp)
            elif isinstance(row["valor_cobertura"], (int, float)):
                valor_cobertura_num = row["valor_cobertura"]
            else:
                valor_cobertura_num = None
            display_valor_cobertura = f"{valor_cobertura_num:.2f}" if valor_cobertura_num is not None else ""
        except Exception:
            display_valor_cobertura = row["valor_cobertura"] if row["valor_cobertura"] is not None else ""

        # Cria o modal com campos editáveis
        modal_content = html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.Label("CNP:"),
                    dbc.Input(id="seguro-input-cnp", type="number", value=row["cnp"], disabled=True)
                ], width=6),
                dbc.Col([
                    dbc.Label("CNPJ:"),
                    dbc.Input(id="seguro-input-cnpj", type="text", value=row["cnpj"], disabled=True)
                ], width=6)
            ], className="mb-2"),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Razão Social:"),
                    dbc.Input(id="seguro-input-razao-social", type="text", value=row["razao_social"], disabled=True)
                ], width=12)
            ], className="mb-2"),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Início Vigência Seguro:"),
                    dbc.Input(id="seguro-input-inicio", type="text", placeholder="DD/MM/YYYY", value=row["inicio_vigencia_seguro"], className="date-input", disabled=False)
                ], width=6),
                dbc.Col([
                    dbc.Label("Vencimento:"),
                    dbc.Input(id="seguro-input-vencimento", type="text", placeholder="DD/MM/YYYY", value=row["vencimento"], className="date-input", disabled=True)
                ], width=6)
            ], className="mb-2"),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Valor Cobertura:"),
                    dbc.Input(id="seguro-input-valor-cobertura", type="text", value=display_valor_cobertura, disabled=True)
                ], width=6),
                dbc.Col([
                    dbc.Label("Valor Parcela:"),
                    dbc.Input(id="seguro-input-valor-parcela", type="text", value=display_valor_parcela, disabled=False)
                ], width=6)
            ], className="mb-2"),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Observação:"),
                    dbc.Textarea(id="seguro-input-obs", value=obs, disabled=False)
                ], width=12)
            ], className="mb-2"),
            html.Div([
                html.Hr(),
                html.H5("Pagamentos de Parcelas", className="mb-3"),
                dbc.Row([
                    dbc.Col([
                        dbc.Label("Débito 1:"),
                        dbc.Input(id="seguro-debito1", type="text", value=debitos["debito1"]["data_vencimento"], disabled=True),
                        dcc.Checklist(id="seguro-debito1-check", options=[{"label": " Pago", "value": "pago"}], value=["pago"] if debitos["debito1"]["status"] == "PAGO" else [], style={'marginTop': '5px'})
                    ], width=4),
                    dbc.Col([
                        dbc.Label("Débito 2:"),
                        dbc.Input(id="seguro-debito2", type="text", value=debitos["debito2"]["data_vencimento"], disabled=True),
                        dcc.Checklist(id="seguro-debito2-check", options=[{"label": " Pago", "value": "pago"}], value=["pago"] if debitos["debito2"]["status"] == "PAGO" else [], style={'marginTop': '5px'})
                    ], width=4),
                    dbc.Col([
                        dbc.Label("Débito 3:"),
                        dbc.Input(id="seguro-debito3", type="text", value=debitos["debito3"]["data_vencimento"], disabled=True),
                        dcc.Checklist(id="seguro-debito3-check", options=[{"label": " Pago", "value": "pago"}], value=["pago"] if debitos["debito3"]["status"] == "PAGO" else [], style={'marginTop': '5px'})
                    ], width=4)
                ], className="mb-2"),
                dbc.Row([
                    dbc.Col([
                        dbc.Label("Débito 4:"),
                        dbc.Input(id="seguro-debito4", type="text", value=debitos["debito4"]["data_vencimento"], disabled=True),
                        dcc.Checklist(id="seguro-debito4-check", options=[{"label": " Pago", "value": "pago"}], value=["pago"] if debitos["debito4"]["status"] == "PAGO" else [], style={'marginTop': '5px'})
                    ], width=4),
                    dbc.Col([
                        dbc.Label("Débito 5:"),
                        dbc.Input(id="seguro-debito5", type="text", value=debitos["debito5"]["data_vencimento"], disabled=True),
                        dcc.Checklist(id="seguro-debito5-check", options=[{"label": " Pago", "value": "pago"}], value=["pago"] if debitos["debito5"]["status"] == "PAGO" else [], style={'marginTop': '5px'})
                    ], width=4)
                ], className="mb-2")
            ], id="debito-fields")
        ])
        return True, dbc.ModalBody(modal_content), edit_action + 1, True, {'display': 'none'}, {'display': 'block'}

    return False, dash.no_update, edit_action, edit_mode, dash.no_update, dash.no_update

# Callback para formatar campos de data no modal
@dash.callback(
    [Output("seguro-input-inicio", "value"),  # Valor do campo "Início"
     Output("seguro-input-vencimento", "value")],  # Valor do campo "Vencimento"
    [Input("seguro-input-inicio", "value"),  # Entrada do campo "Início"
     Input("seguro-input-vencimento", "value")],  # Entrada do campo "Vencimento"
    prevent_initial_call=True
)
def format_date_fields(inicio, vencimento):
    # Função auxiliar para aplicar máscara de data (DD/MM/YYYY)
    def apply_date_mask(value):
        if not value:
            return ""
        digits = ''.join(filter(str.isdigit, value))  # Extrai apenas números
        if len(digits) > 8:
            digits = digits[:8]  # Limita a 8 dígitos
        if len(digits) >= 2:
            digits = digits[:2] + '/' + digits[2:]
        if len(digits) >= 5:
            digits = digits[:5] + '/' + digits[5:]
        return digits

    formatted_inicio = apply_date_mask(inicio) if inicio else inicio
    formatted_vencimento = vencimento

    # Calcula o vencimento automaticamente (1 ano após o início)
    if formatted_inicio and len(formatted_inicio) == 10:
        try:
            inicio_date = datetime.datetime.strptime(formatted_inicio, "%d/%m/%Y")
            vencimento_date = inicio_date.replace(year=inicio_date.year + 1)
            formatted_vencimento = vencimento_date.strftime("%d/%m/%Y")
        except ValueError:
            formatted_vencimento = ""

    return formatted_inicio, formatted_vencimento

# Callbacks para controlar os checklists de pagamento (débito 1 a 5)
@dash.callback(
    Output("seguro-debito1-check", "value"),
    [Input("seguro-debito1-check", "value")],
    [State("seguro-edit-mode", "data")]
)
def control_debito1_check(value, edit_mode):
    if not edit_mode:
        raise dash.exceptions.PreventUpdate  # Impede atualização se não estiver em modo de edição
    return value

@dash.callback(
    Output("seguro-debito2-check", "value"),
    [Input("seguro-debito2-check", "value")],
    [State("seguro-edit-mode", "data")]
)
def control_debito2_check(value, edit_mode):
    if not edit_mode:
        raise dash.exceptions.PreventUpdate
    return value

@dash.callback(
    Output("seguro-debito3-check", "value"),
    [Input("seguro-debito3-check", "value")],
    [State("seguro-edit-mode", "data")]
)
def control_debito3_check(value, edit_mode):
    if not edit_mode:
        raise dash.exceptions.PreventUpdate
    return value

@dash.callback(
    Output("seguro-debito4-check", "value"),
    [Input("seguro-debito4-check", "value")],
    [State("seguro-edit-mode", "data")]
)
def control_debito4_check(value, edit_mode):
    if not edit_mode:
        raise dash.exceptions.PreventUpdate
    return value

@dash.callback(
    Output("seguro-debito5-check", "value"),
    [Input("seguro-debito5-check", "value")],
    [State("seguro-edit-mode", "data")]
)
def control_debito5_check(value, edit_mode):
    if not edit_mode:
        raise dash.exceptions.PreventUpdate
    return value

# Callbacks para estilizar os checklists de pagamento (verde para "pago", vermelho para "pendente")
@dash.callback(
    Output("seguro-debito1-check", "style"),
    Input("seguro-debito1-check", "value")
)
def style_debito1_check(value):
    return {'marginTop': '5px', 'color': 'green' if "pago" in value else 'red'}

@dash.callback(
    Output("seguro-debito2-check", "style"),
    Input("seguro-debito2-check", "value")
)
def style_debito2_check(value):
    return {'marginTop': '5px', 'color': 'green' if "pago" in value else 'red'}

@dash.callback(
    Output("seguro-debito3-check", "style"),
    Input("seguro-debito3-check", "value")
)
def style_debito3_check(value):
    return {'marginTop': '5px', 'color': 'green' if "pago" in value else 'red'}

@dash.callback(
    Output("seguro-debito4-check", "style"),
    Input("seguro-debito4-check", "value")
)
def style_debito4_check(value):
    return {'marginTop': '5px', 'color': 'green' if "pago" in value else 'red'}

@dash.callback(
    Output("seguro-debito5-check", "style"),
    Input("seguro-debito5-check", "value")
)
def style_debito5_check(value):
    return {'marginTop': '5px', 'color': 'green' if "pago" in value else 'red'}

# Callback para salvar ou cancelar alterações no modal
@dash.callback(
    [Output("seguro-table", "data", allow_duplicate=True),  # Atualiza a tabela
     Output("modal-seguro", "is_open", allow_duplicate=True),  # Fecha o modal
     Output("seguro-save-success-toast", "is_open", allow_duplicate=True),  # Exibe toast de sucesso
     Output("seguro-table", "active_cell", allow_duplicate=True),  # Limpa célula ativa
     Output("seguro-edit-mode", "data", allow_duplicate=True)],  # Reseta modo de edição
    [Input("seguro-save-btn", "n_clicks"), Input("seguro-close-modal-btn", "n_clicks")],  # Botões "Salvar" e "Cancelar"
    [State("seguro-input-cnp", "value"),  # Valores dos campos do modal
     State("seguro-input-cnpj", "value"),
     State("seguro-input-razao-social", "value"),
     State("seguro-input-inicio", "value"),
     State("seguro-input-vencimento", "value"),
     State("seguro-input-valor-cobertura", "value"),
     State("seguro-input-valor-parcela", "value"),
     State("seguro-input-obs", "value"),
     State("seguro-debito1-check", "value"),
     State("seguro-debito2-check", "value"),
     State("seguro-debito3-check", "value"),
     State("seguro-debito4-check", "value"),
     State("seguro-debito5-check", "value"),
     State("seguro-table", "data")],
    prevent_initial_call=True
)
def save_or_cancel_seguro(save_clicks, cancel_clicks, cnp, cnpj, razao_social,
                          inicio, vencimento, valor_cobertura, valor_parcela, obs,
                          debito1_check, debito2_check, debito3_check, debito4_check, debito5_check,
                          table_data):
    ctx = callback_context.triggered[0]["prop_id"]
    
    # Caso o botão "Cancelar" seja clicado
    if ctx == "seguro-close-modal-btn.n_clicks" and cancel_clicks:
        temp_data = table_data.copy() if table_data else []
        if temp_data and 'editar' in temp_data[0]:
            temp_data[0]['editar'] += " "  # Pequeno hack para forçar atualização
        return temp_data, False, False, None, False
    
    # Caso o botão "Salvar" seja clicado
    if ctx == "seguro-save-btn.n_clicks" and save_clicks:
        # Função para validar e converter datas
        def validate_date(date_str):
            if not date_str:
                return None
            try:
                date_obj = datetime.datetime.strptime(date_str, "%d/%m/%Y")
                return date_obj
            except ValueError:
                raise ValueError(f"Data inválida: {date_str}. Use o formato DD/MM/YYYY.")
        
        try:
            inicio_date = validate_date(inicio)
            vencimento_date = validate_date(vencimento)
            inicio_formatted = inicio_date.strftime("%Y-%m-%d") if inicio_date else None
            vencimento_formatted = vencimento_date.strftime("%Y-%m-%d") if vencimento_date else None
        except ValueError as e:
            print(f"Erro de validação de data: {e}")
            return table_data, True, False, None, False

        # Converte valores monetários para formato numérico
        try:
            valor_cobertura_num = float(valor_cobertura.replace(",", ".")) if valor_cobertura else None
        except (ValueError, TypeError):
            valor_cobertura_num = None
        try:
            valor_parcela_num = float(valor_parcela.replace(",", ".")) if valor_parcela else None
        except (ValueError, TypeError):
            valor_parcela_num = None

        # Salva os dados no banco
        try:
            with engine.connect() as conn:
                with conn.begin():  # Inicia transação
                    query_check = text("SELECT COUNT(*) FROM seguradora WHERE cnp = :cnp")
                    exists = conn.execute(query_check, {"cnp": cnp}).scalar() > 0
                    if exists:
                        query = text("""
                            UPDATE seguradora 
                            SET inicio_vigencia_seguro = :inicio,
                                vencimento = :vencimento,
                                valor_cobertura = :valor_cobertura,
                                valor_parcela = :valor_parcela,
                                obs = :obs
                            WHERE cnp = :cnp
                        """)
                    else:
                        query = text("""
                            INSERT INTO seguradora 
                            (cnp, inicio_vigencia_seguro, vencimento, valor_cobertura, valor_parcela, obs)
                            VALUES 
                            (:cnp, :inicio, :vencimento, :valor_cobertura, :valor_parcela, :obs)
                        """)
                    conn.execute(query, {
                        "cnp": cnp, "inicio": inicio_formatted, "vencimento": vencimento_formatted, 
                        "valor_cobertura": valor_cobertura_num, 
                        "valor_parcela": valor_parcela_num,
                        "obs": obs
                    })

                    # Atualiza status dos débitos
                    debito_status = [
                        ("pago" in debito1_check, 1),
                        ("pago" in debito2_check, 2),
                        ("pago" in debito3_check, 3),
                        ("pago" in debito4_check, 4),
                        ("pago" in debito5_check, 5)
                    ]
                    for is_checked, numero_parcela in debito_status:
                        status = "PAGO" if is_checked else "PENDENTE"
                        query_parcela = text("""
                            UPDATE pag_seguradora
                            SET status = :status
                            WHERE cnp = :cnp AND numero_parcela = :numero_parcela
                        """)
                        conn.execute(query_parcela, {
                            "status": status,
                            "cnp": cnp,
                            "numero_parcela": numero_parcela
                        })

            # Recarrega os dados atualizados da tabela
            with engine.connect() as conn:
                query = text("""
                    SELECT 
                      d.cnp,
                      d.cnpj,
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
                df["editar"] = "🔍 Detalhes"
                df["excluir"] = "🗑️ Excluir"
            return df.to_dict("records"), False, True, None, False
        except Exception as e:
            print(f"Erro ao salvar seguro: {e}")
            return table_data, True, False, None, False
    return table_data, True, False, None, False

# Callback para abrir o modal de exclusão
@dash.callback(
    Output("modal-seguro-delete", "is_open"),
    [Input("seguro-table", "active_cell")],
    [State("modal-seguro-delete", "is_open")],
    prevent_initial_call=True
)
def open_delete_modal(active_cell, is_open):
    if active_cell and active_cell["column_id"] == "excluir":
        return True  # Abre o modal se o botão "Excluir" for clicado
    return is_open

# Callback para confirmar ou cancelar a exclusão
@dash.callback(
    [Output("modal-seguro-delete", "is_open", allow_duplicate=True), 
     Output("seguro-table", "data", allow_duplicate=True), 
     Output("seguro-delete-success-toast", "is_open")],
    [Input("seguro-confirm-delete-btn", "n_clicks"), Input("seguro-cancel-delete-btn", "n_clicks")],
    [State("seguro-table", "data"), State("seguro-table", "active_cell")],
    prevent_initial_call=True
)
def confirm_delete_seguro(confirm_clicks, cancel_clicks, table_data, active_cell):
    ctx = callback_context.triggered[0]["prop_id"]
    if not active_cell:
        return False, table_data, False
    row = table_data[active_cell["row"]]
    cnp_to_delete = row["cnp"]
    
    # Caso o botão "Excluir" seja confirmado
    if ctx == "seguro-confirm-delete-btn.n_clicks" and confirm_clicks:
        try:
            with engine.connect() as conn:
                with conn.begin():
                    query_check = text("SELECT COUNT(*) FROM seguradora WHERE cnp = :cnp")
                    exists = conn.execute(query_check, {"cnp": cnp_to_delete}).scalar() > 0
                    if exists:
                        query = text("DELETE FROM seguradora WHERE cnp = :cnp")
                        result = conn.execute(query, {"cnp": cnp_to_delete})
                        if result.rowcount > 0:
                            print(f"Seguro para CNP {cnp_to_delete} excluído com sucesso do banco de dados.")
                        else:
                            print(f"Nenhum registro excluído para CNP {cnp_to_delete}.")
                    else:
                        print(f"Registro com CNP {cnp_to_delete} não encontrado na tabela seguradora.")
            updated_data = [r for r in table_data if r["cnp"] != cnp_to_delete]  # Remove o registro da tabela
            return False, updated_data, True
        except Exception as e:
            print(f"Erro ao excluir seguro: {e}")
            return False, table_data, False
    
    # Caso o botão "Cancelar" seja clicado
    elif ctx == "seguro-cancel-delete-btn.n_clicks" and cancel_clicks:
        return False, table_data, False
    return True, table_data, False
