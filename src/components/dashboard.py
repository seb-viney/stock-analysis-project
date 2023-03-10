# Third party imports
from dash import Dash ,html, dcc
from dash.dependencies import Input, Output, State
# Local import
from . import ids, price_history

def input_items(app: Dash):
    @app.callback(
        Output('output-container-button', 'children'),
        [Input('button-example-1', 'n_clicks')],
        [State('input-box', 'value')])
    def update_output(n_clicks, value):
        data = price_history.get_price_history(ticker_list=[value], save_csv=True, period='2y')
        print(data.head())
        return 'The input value was "{}"'.format(
            value,
            n_clicks,
            data
        )
    return html.Div(
        children=[
            html.Div(dcc.Input(id='input-box', type='text')),
            html.Button('Submit', id='button-example-1'),
            html.Div(id='output-container-button',
            children='Enter a value and press submit')
        ]
    )

def dropdown_button(app: Dash, title:str='', item_list:list=[]) -> html.Div:  

    @app.callback(
        Output(ids.DROPDOWN, "value"),
        Input(ids.SELECT_ALL_BUTTON, "n_clicks"),
    )
    def select_all(_:int) -> list[str]:
        return item_list

    return html.Div(
        children=[
            html.H6(title),
            dcc.Dropdown(
                id=ids.DROPDOWN,
                options=[{"label": item, "value": item} for item in item_list],
                value=item_list,
                multi=True,
            ),
            html.Button(
                id=ids.SELECT_ALL_BUTTON,
                className="dropdown-button",
                children=["Select All"],
                n_clicks=0,
            ),
        ]
    )

def create_layout(app: Dash, dropdown_title:str='', dropdown_item_list:list=[]) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    input_items(app),
                    dropdown_button(app, dropdown_title, dropdown_item_list),                    
                ],
            ),
            #bar_chart.render(app),
        ],
    )