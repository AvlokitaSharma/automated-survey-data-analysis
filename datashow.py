import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Load analysis results
df = pd.read_csv('word_frequencies.csv')

# Plot
fig = px.bar(df, x='Word', y='Frequency', title='Most Common Words in Survey Responses')

# Dash app
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1('Survey Data Analysis Dashboard'),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
