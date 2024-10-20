from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

# Load your data
df = pd.read_csv('../players_20.csv')
positions = df['player_positions'].unique()

# Create your plotly visualization for player stats
fig = px.scatter(df, x='age', y='overall', color='potential')

# Define the layout with a dropdown
layout = html.Div([
    html.H2('Player Stats'),
    dcc.Dropdown(
        id='position-dropdown',
        options=[{'label': pos, 'value': pos} for pos in positions],
        value=positions[0],  # default value
        clearable=False
    ),
    dcc.Graph(
        id='player-graph',
        figure=fig
    )
])


