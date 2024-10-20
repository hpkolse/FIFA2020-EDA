import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
from pages import page1, page2

# Initialize the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

app.layout = dbc.Container([
    dcc.Location(id='url', refresh=False),
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dcc.Link("Player Stats", href='/page1', className='nav-link')),
            dbc.NavItem(dcc.Link("Team Stats", href='/page2', className='nav-link')),
        ],
        brand="FIFA 2020 EDA",
        color="primary",
        dark=True
    ),
    html.Div(id='page-content')
])

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/page1':
        return page1.layout
    elif pathname == '/page2':
        return page2.layout
    else:
        return '404 - Page not found'
    
# Callback for updating the graph
@app.callback(
    Output('player-graph', 'figure'),
    [Input('position-dropdown', 'value')]
)
def update_graph(selected_position):
    filtered_df = df[df['player_positions'] == selected_position]
    fig = px.scatter(filtered_df, x='Age', y='Overall', color='Potential')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
