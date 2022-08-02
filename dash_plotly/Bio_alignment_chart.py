import dash
import dash_bio as dashbio
from dash import html
import urllib.request as urlreq
from dash.dependencies import Input, Output


app = dash.Dash(__name__)


data = urlreq.urlopen(
    'https://git.io/alignment_viewer_p53.fasta'
).read().decode('utf-8')

app.layout = html.Div([
    dashbio.AlignmentChart(
        id='my-default-alignment-viewer',
        data=data,
        height=900,
        tilewidth=30,
    ),
    html.Div(id='default-alignment-viewer-output')
])

@app.callback(
    Output('default-alignment-viewer-output', 'children'),
    Input('my-default-alignment-viewer', 'eventDatum')
)
def update_output(value):
    if value is None:
        return 'No data.'
    return str(value)

if __name__ == '__main__':
    app.run_server(debug=True)