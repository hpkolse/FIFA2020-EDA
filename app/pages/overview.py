import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px
from data_loader import df

dash.register_page(__name__, path='/', name='Overview')

layout = html.Div([
    html.H1('FIFA 2020 Overview'),
    dcc.Dropdown(
        id='overview-dropdown',
        options=[{'label': col, 'value': col} for col in df.columns if df[col].dtype in ['int64', 'float64']],
        value='overall'
    ),
    dcc.Graph(id='overview-graph')
])

@callback(
    Output('overview-graph', 'figure'),
    Input('overview-dropdown', 'value')
)
def update_overview_graph(attribute):
    fig = px.histogram(df, x=attribute, title=f'Distribution of {attribute}')
    return fig