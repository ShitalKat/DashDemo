# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input #DCC stands for Dash Core Components
import pandas as pd
import plotly.express as px


# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app - incorporate css

app = Dash(__name__)
@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)

# App layout
app.layout = html.Div([
    html.Link(
        rel='stylesheet',
        href='/static/mycuststyle.css'
    ),
    html.Div(className='row', children = [
        html.H1('This is my H1 Tag'),
        html.H2('This is my H2 Tag'),
        html.H3('This is my H3 Tag'),
        html.H4('This is my H4 Tag'),
        html.H5('This is my H5 Tag'),

    ]),
    html.Div(className='row', children='My First App with Data, Graph, and Controls',
             style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),

    html.Div(className='row', children=[
        dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'],
                       value='lifeExp',
                       inline=True,
                       id='my-radio-buttons-final')
    ]),

    html.Div(className='row', children=[
        html.Div(className='six columns', children=[
            dash_table.DataTable(data=df.to_dict('records'), page_size=11, style_table={'overflowX': 'auto'})
        ]),
        html.Div(className='six columns', children=[
            dcc.Graph(figure={}, id='histo-chart-final')
        ])
    ])
])

# Add controls to build the interaction
@callback(
    Output(component_id='histo-chart-final', component_property='figure'),
    Input(component_id='my-radio-buttons-final', component_property='value')
)
def update_graph(col_chosen): 
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig




# Run the app
if __name__ == '__main__':
    app.run(debug=True)
