# Third party imports
from dash import Dash ,html, dcc

# Local import

def dropdown_button(app: Dash, title:str='', item_list:list=[]) -> html.Div:  

    #IDs
    DROPDOWN = 'dropdown-id'
    SELECT_ALL_BUTTON = 'select-all-button'

    return html.Div(
        children=[
            html.H6(title),
            dcc.Dropdown(
                id=DROPDOWN,
                options=[{"label": item, "value": item} for item in item_list],
                value=item_list,
                multi=True,
            ),
            html.Button(
                id=SELECT_ALL_BUTTON,
                className="dropdown-button",
                children=["Select All"],
                multi=True,
            )
        ]
    )

def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    dropdown_button(app, 'test', ['one', 'two', 'three']),
                ],
            ),
            bar_chart.render(app),
        ],
    )