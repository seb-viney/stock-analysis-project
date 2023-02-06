# Third party imports
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

# Local import
from . import ids

def line_chart(app: Dash, dataframe, colour:str="Stock Code",
                x_axis:str="Date", y_axis:str="Open Change") -> html.Div:
    
    '''
    example call: data_visualization.line_chart(app, dataframe=data[["Open","Stock Code"]])
    dataframe: The data
    colour: Which column in the data to compare
    '''

    @app.callback(
        Output(ids.BAR_CHART, "children"),
        [
            Input(ids.DROPDOWN, "value"),
        ],
    )
    def update_line_chart(dataframe: list[str]) -> html.Div:
        filtered_data = dataframe #.query("nation in @nations")

        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.", id=ids.LINE_CHART)

        fig = px.line(filtered_data, x=x_axis, y=y_axis, color=colour, text=colour)

        return html.Div(dcc.Graph(figure=fig), id=ids.LINE_CHART)

    return html.Div(id=ids.LINE_CHART)

    