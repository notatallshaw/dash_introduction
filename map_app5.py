# Standard Libraries
import random


# Third Party Libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd


three11_df = pd.read_msgpack('311_2017.msgpack')
mid_lat = (three11_df['Latitude'].max() + three11_df['Latitude'].min()) / 2
mid_lon = (three11_df['Longitude'].max() + three11_df['Longitude'].min()) / 2
mapbox_api_token = 'pk.eyJ1IjoicXVhbnR6dXIiLCJhIjoiY2pybm8zMzBjMDE4eDRjdGRxMTliYXB5byJ9.YGMtlRHc6S7HsFrl4dp_rw'
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

sample_data = three11_df.head(100)
app.layout = html.Div(children=[
    html.H1(children='311 Report Data 2017', id='first'),
    html.Div(id='dummy'),
    dcc.Graph(
            id='three11-graph',
            style={'height': '900px'},
            figure={
                'data': [
                    {'lat': sample_data['Latitude'],
                     'lon': sample_data['Longitude'],
                     'mode': 'markers',
                     'type': 'scattermapbox',
                     'hoverinfo': 'text',
                     'hovertext': [
                         f'Agency: {a}<br>Type: {t}'
                         for a, t in
                         zip(sample_data['Agency Name'], sample_data['Complaint Type'])
                     ]},
                ],
                'layout': {
                    'title': 'NYC 311 Report Locations - 2017',
                    'autosize': True,
                    'mapbox': {
                        'accesstoken': mapbox_api_token,
                        'center': {'lat': mid_lat, 'lon': mid_lon},
                        'zoom': 10,
                    }
                }
            }
        )
])



if __name__ == '__main__':
    app.run_server(debug=True)
