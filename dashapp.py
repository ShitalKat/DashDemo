from dash import Dash, html, dcc, register_page, callback,Output,Input
import dash

import flask
import os
#dash_app = Dash(__name__, use_pages=True)



def create_dash_app(requests_pathname_prefix: str = None) -> dash.Dash:
    server = flask.Flask(__name__)
    server.secret_key = os.environ.get('secret_key', 'secret')
    dash_app = dash.Dash(__name__,use_pages=True, server=server, requests_pathname_prefix=requests_pathname_prefix)

    
    @callback(Output('session_demo_label', 'children'), Input('local', 'data'))
    def update_label(data):
        if data:
            return f"This is Session Variable -  {data.get('session_demo')}"
        else: return "No value in session"
    
    dash_app.layout = html.Div([

    # The memory store reverts to the default on every page refresh
    dcc.Store(id='memory'),
    # The local store will take the initial data
    # only the first time the page is loaded
    # and keep it until it is cleared.
    dcc.Store(id='local', storage_type='local'), #across multiple tab
    # Same as the local store but will lose the data
    # when the browser/tab closes.
    dcc.Store(id='session', storage_type='session'), #limited for single tab
        html.Link(
        rel='stylesheet',
        href='/static/MyStylesheet1.css'
    ),
    
    html.Div( children = 
        [
            html.Div( className='topnav',children=[
                dcc.Link(
                    f"{page['name']}", href=page["relative_path"]
                )]
            )
            for page in dash.page_registry.values()
            
        ]
    ), 
    #html.Div(style= {'display': 'inline-block'},children = [html.H3(id='session_demo_label')]),
	dash.page_container,
    html.Footer(className = 'footer',children=[html.P(id='session_demo_label')])
    ])
    return dash_app






