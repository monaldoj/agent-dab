import os
import dash
import dash_bootstrap_components as dbc
from dash import html, Input, Output, State, dcc
from DatabricksChatbot import DatabricksChatbot
# Ensure environment variable is set correctly

# Initialize the Dash app with a clean theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

# Create the chatbot component
chatbot = DatabricksChatbot(app=app)

# Define the app layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(chatbot.layout, width={'size': 8, 'offset': 2}, id="chatbot-row")
    ])
], fluid=True)

if __name__ == '__main__':
    app.run(debug=True)
