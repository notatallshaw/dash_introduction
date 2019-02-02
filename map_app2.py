import dash
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Hello World!', id='first'),
    html.Div(id='dummy')
])


@app.callback(output=Output('dummy', 'children'),
              inputs=[Input('first', 'n_clicks')])
def count_clicks(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    return f'Clicks: {n_clicks}'


if __name__ == '__main__':
    app.run_server(debug=True)
