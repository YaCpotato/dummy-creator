import numpy as np
import dash
import dash_table as dt
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
    ]),
    html.Div(id="table1")
])

@app.callback(
    Output('table1', 'children'),
    Input('submit-val', 'n_clicks')
)
def update_output(value):
    df = fn.DummyFrame()
    df.create_numeric('test', 30)
    df.create_numeric('test-2', 30)
    result = df.publish()
    data = result.to_dict('rows')
    columns =  [{"name": i, "id": i,} for i in (result.columns)]
    return dt.DataTable(data=data, columns=columns)


if __name__ == '__main__':
    app.run_server(debug=True)
