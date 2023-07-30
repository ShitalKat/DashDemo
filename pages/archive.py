import dash
from dash import html, dcc


dash.register_page(
    __name__,
    path='/archive',
    title='Archive',
    name='Archive',
    redirect_from=["/archive2021", "/archive2020"] # If user goes to this page, he will redirect to /archive page
)

layout = html.Div(children=[
    html.H1(children='This is our Archive page'),

    html.Div(children='''
        This is our Archive page content.
    '''),

])