import dash
from dash import html, dcc

dash.register_page(
    __name__,
    path='/',
    title='Our Home Page',
    name='Our Home Page'
)

layout = html.Div(children=[
    html.H1(children='Home'),

    html.Div(children='''
        Welcome to home page.
    ''')
])