import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from modules import dashboard, cnps, seguro, relatorios

# Inicializar a aplicação Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
server = app.server

# Layout da aplicação com um menu lateral
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.Row([
        dbc.Col([
            html.H2("Sistema Seguro CNP", className="text-center"),
            dbc.Nav([
                dbc.NavLink("Dashboard", href="/", active="exact"),
                dbc.NavLink("CNPs", href="/cnps", active="exact"),
                dbc.NavLink("Seguro", href="/seguro", active="exact"),
                dbc.NavLink("Relatórios", href="/relatorios", active="exact"),
                dbc.NavLink("Executar ETL", href="/etl", active="exact"),
            ], vertical=True, pills=True),
        ], width=2, className="bg-light"),
        
        dbc.Col(id="page-content", width=10)
    ])
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
        return html.Div([html.H3("Executar ETL"), html.P("Aqui será implementada a funcionalidade de upload de planilha.")])
    else:
        return html.H3("404 - Página não encontrada")

app.callback(Output("page-content", "children"), [Input("url", "pathname")])(render_page_content)

if __name__ == "__main__":
    app.run_server(debug=True) # True ativa o elemento Dev Tools para debug
