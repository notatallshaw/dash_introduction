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
all_zips = set(three11_df['Incident Zip'])
mid_lat = (three11_df['Latitude'].max() + three11_df['Latitude'].min()) / 2
mid_lon = (three11_df['Longitude'].max() + three11_df['Longitude'].min()) / 2

mapbox_api_token = 'pk.eyJ1IjoicXVhbnR6dXIiLCJhIjoiY2pybm8zMzBjMDE4eDRjdGRxMTliYXB5byJ9.YGMtlRHc6S7HsFrl4dp_rw'
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

sample_data = three11_df.head(100)
app.layout = html.Div(children=[
    html.H1(children='311 Report Data 2017', id='first'),
    html.Div('Choose a Zip Code:'),
    dcc.Dropdown(
        id='all-zips',
        options=[{'label': z, 'value': z} for z in all_zips],
        value=None
    ),
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


@app.callback(output=Output('three11-graph', 'figure'),
              inputs=[Input('all-zips', 'value')])
def filter_map_to_zip(incident_zip):
    if not incident_zip:
        raise PreventUpdate
    zip_df = three11_df.loc[three11_df['Incident Zip'] == incident_zip]
    mid_lat = (zip_df['Latitude'].max() + zip_df['Latitude'].min()) / 2
    mid_lon = (zip_df['Longitude'].max() + zip_df['Longitude'].min()) / 2
    return {
        'data': [
            {'lat': zip_df['Latitude'],
             'lon': zip_df['Longitude'],
             'mode': 'markers',
             'type': 'scattermapbox',
             'hoverinfo': 'text',
             'hovertext': [
                 f'Agency: {a}<br>Type: {t}'
                 for a, t in
                 zip(zip_df['Agency Name'], zip_df['Complaint Type'])
             ]},
        ],
        'layout': {
            'title': 'NYC 311 Report Locations - 2017',
            'autosize': True,
            'mapbox': {
                'accesstoken': mapbox_api_token,
                'center': {'lat': mid_lat, 'lon': mid_lon},
                'zoom': 15,
            }
        }
    }



if __name__ == '__main__':
    app.run_server(debug=True)
