# Standard Libraries
import random


# Third Party Libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(children=[
    html.H1(children='Hello World!', id='first'),
    html.Div(id='dummy'),
    dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montréal'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization',
                    'yaxis': {'range': [0, 10]},
                }
            }
        )
])


@app.callback(output=Output('example-graph', 'figure'),
              inputs=[Input('first', 'n_clicks')])
def count_clicks(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    return {
                'data': [
                    {'x': [1, 2, 3],
                     'y': [random.randint(1, 10) for _ in range(3)],
                     'type': 'bar',
                     'name': 'SF'},
                    {'x': [1, 2, 3],
                     'y': [random.randint(1, 10) for _ in range(3)],
                     'type': 'bar',
                     'name': 'Montréal'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization',
                    'yaxis': {'range': [0, 10]},
                }
            }


if __name__ == '__main__':
    app.run_server(debug=True)
