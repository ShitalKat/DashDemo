from dash import Dash, html, dcc, register_page, callback,Output,Input
import dash

app = Dash(__name__, use_pages=True)


@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)

app.layout = html.Div([

    # The memory store reverts to the default on every page refresh
    dcc.Store(id='memory'),
    # The local store will take the initial data
    # only the first time the page is loaded
    # and keep it until it is cleared.
    dcc.Store(id='local', storage_type='local'),
    # Same as the local store but will lose the data
    # when the browser/tab closes.
    dcc.Store(id='session', storage_type='session'),
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
    html.Div(style= {'display': 'inline-block'},children = [html.H3(id='user_label')]),
	dash.page_container,
    html.Footer(className = 'topnav',children=[html.H5('This is footer')])
])



@callback(Output('user_label', 'children'), Input('session', 'data'))
def update_label(data):
    return f"This is Session Variable -  {data.get('username')}"





if __name__ == '__main__':
	app.run(debug=True)