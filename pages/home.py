import dash
from dash import html, dcc

dash.register_page(
    __name__,
    path='/',
    title='Home',
    name='Home',
    order=1
)

layout = html.Div(children=[
    html.H1(children='Home'),

    html.Div(children='''
        Welcome to home page.
    '''),
    html.A("Link to external site (open in new tab)", href='https://plot.ly', target="_blank"), html.Br(),
    html.A("Link to internal sample site (open in new tab)", href='/sample', target="_blank"), html.Br(),
    html.A("Link to internal sample site (open in same tab)", href='/sample'),

])