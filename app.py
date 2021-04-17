import numpy as np
import dash
import dash_table
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, MATCH, ALL
import fn

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

result_view = html.Div([
    html.Div([
    ]),
    html.Div([
    ])
])

app.layout = html.Div([
    html.Div([
        dcc.Input(
            id = "input-item-name",
            type = "text",
            placeholder="Item Name",
        ),
        html.Button('Submit', id='submit-val', n_clicks=0),
        html.Div(id='textarea-example-output', style={'whiteSpace': 'pre-line'})
    ])
])

@app.callback(
    Output('textarea-example-output', 'children'),
    Input('submit-val', 'n_clicks')
)
def update_output(value):
    result = fn.example()
    return result


if __name__ == '__main__':
    app.run_server(debug=True)
