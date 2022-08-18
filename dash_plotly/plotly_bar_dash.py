from dash import Dash, dcc, html, Input, Output
import plotly.express as px 

app = Dash(__name__)

app.layout = html.Div([html.H3("Restaurant tips by day of week "), 
                       dcc.Dropdown(id= "dropdown",
                                    options=["fri" , "Sat", "Sun"],
                                    value = "Friday",
                                    clearable = True),
                       dcc.Graph(id = "graph")])

@app.callback(
    Output("graph", "figure"),
    Input("dropdown", "value"))
def update_bar_chart(day):
    "day parameter is from slide bar"
    df = px.data.tips() #! Replace with your data 
    mask = df["day"] == day
    fig = px.bar(df[mask], x = "sex", y = "total_bill",
                 color = "smoker", barmode = "group")
    return fig

app.run_server(debug = True)
