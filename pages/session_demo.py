from dash import Dash, html, dcc,callback,Output,Input,State,register_page
import dash




register_page(
    __name__,
    path='/session_demo',
    title='Session Demo',
    name='Session Demo'

)

layout = html.Div([
    html.Link(
        rel='stylesheet',
        href='/static/MyStylesheet1.css'
    ),
    html.Div(children=[

    html.Div(children='''
        Enter Any value to save in session : 
    '''),
    dcc.Input(id="input_name", type="text", placeholder="Name", style={'marginRight':'10px'}),
    html.Button('Submit', id='submit-val', n_clicks=0)

])
])

@callback(
    Output('local', 'data'),
    Input('submit-val', 'n_clicks'),
    State('input_name', 'value'),
    State('local', 'data')
)
def update_session_and_navigate(n_clicks, value,data):
        data = data or {}
        if value:
            data['session_demo'] = data.get('session_demo','') + value + ' '
        return data



