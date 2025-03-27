import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from modules import dashboard, cnps, seguro, relatorios, etl_page  # Importando o módulo de ETL
import logging

# Desativar logs do servidor Flask/Werkzeug
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Inicializar a aplicação Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
server = app.server

# Layout da aplicação com um menu lateral fixo
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.Row([
        dbc.Col([
            # Logo do BRB
            html.Img(src="/assets/imagens/brb-banco.png", style={"width": "100%", "padding": "10px"}),
            dbc.Nav([
                dbc.NavLink("Dashboard", href="/", active="exact"),
                dbc.NavLink("CNPs", href="/cnps", active="exact"),
                dbc.NavLink("Seguro", href="/seguro", active="exact"),
                dbc.NavLink("Relatórios", href="/relatorios", active="exact"),
                dbc.NavLink("Executar ETL", href="/etl", active="exact"),
            ], vertical=True, pills=True, className="mt-3"),
        ], width=2, style={"position": "fixed", "height": "100vh", "overflow-y": "auto", "background-color": "#EDEDED", "color": "white"}),
        
        # Ajustar o conteúdo principal para não sobrepor o menu
        dbc.Col(id="page-content", width=10, style={"margin-left": "16.67%"}),
    ], style={"margin": "0"})
])

# Callback para trocar de página
def render_page_content(pathname):
    if pathname == "/" or pathname == "/dashboard":
        return dashboard.layout
    elif pathname == "/cnps":
        return cnps.layout
    elif pathname == "/seguro":
        return seguro.layout
    elif pathname == "/relatorios":
        return relatorios.layout
    elif pathname == "/etl":
        return etl_page.layout
    else:
        return html.H3("404 - Página não encontrada")

app.callback(Output("page-content", "children"), [Input("url", "pathname")])(render_page_content)

if __name__ == "__main__":
    app.run_server(debug=False, host='0.0.0.0', port=8050)