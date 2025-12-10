# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv("data/combined_sales_data.csv")

fig = px.bar(df, x="date", y="sales", color="sales", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Sales Dashboard'),

    html.Div(children='''
        Dashboard generated from CSV data
    '''),

    dcc.Graph(
        id='sales-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
