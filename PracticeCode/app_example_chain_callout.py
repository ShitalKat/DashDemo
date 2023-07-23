from dash import Dash, dcc, html, Input, Output, callback

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

all_options = {
    'Python': ['Dash', 'Django', 'Flask'],
    'Sql': ['Snowflakes', 'MongoDB', 'MySql']
}
selected_lang = 'Sql'
app.layout = html.Div([
    dcc.RadioItems(
        list(all_options.keys()),selected_lang,
        id='lang-radio',
    ),

    html.Hr(),

    dcc.RadioItems(id='framework-radio'),

    html.Hr(),

    html.Div(id='display-selected-values')
])


@callback(
    Output('framework-radio', 'options'),
    Input('lang-radio', 'value'))
def set_cities_options(selected_lang):
    return [{'label': i, 'value': i} for i in all_options[selected_lang]]


@callback(
    Output('framework-radio', 'value'),
    Input('framework-radio', 'options'))
def set_cities_value(available_options):
    return available_options[0]['value']


@callback(
    Output('display-selected-values', 'children'),
    Input('lang-radio', 'value'),
    Input('framework-radio', 'value'))
def set_display_children(selected_lang, selected_famework):
    return f'{selected_famework} is a framework in {selected_lang}'


if __name__ == '__main__':
    app.run(debug=True)
