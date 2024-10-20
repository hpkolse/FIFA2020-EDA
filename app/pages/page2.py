from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load your data
df = pd.read_csv('../players_20.csv')

# Create your plotly visualization for team stats
fig = px.bar(df, x='club', y='overall', color='potential')

# Define the layout for the team stats page
layout = html.Div([
    html.H2('Team Stats'),
    dcc.Graph(
        id='team-graph',
        figure=fig
    )
])
