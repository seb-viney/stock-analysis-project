# Third party imports
from dash import Dash ,html, dcc
from dash.dependencies import Input, Output
# Local import
from . import ids

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
                    dropdown_button(app, dropdown_title, dropdown_item_list),
                ],
            ),
            #bar_chart.render(app),
        ],
    )