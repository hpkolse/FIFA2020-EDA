import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('players_20.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('FIFA 2020 Player Analysis'),
    
    dcc.Dropdown(
        id='player-attribute',
        options=[{'label': col, 'value': col} for col in df.columns if df[col].dtype in ['int64', 'float64']],
        value='overall',
        style={'width': '50%'}
    ),
    
    dcc.Graph(id='attribute-histogram')
])

@app.callback(
    Output('attribute-histogram', 'figure'),
    Input('player-attribute', 'value')
)
def update_histogram(attribute):
    fig = px.histogram(df, x=attribute, title=f'Distribution of {attribute}')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)