# Third party imports
from dash import Dash ,html
from dash_bootstrap_components.themes import BOOTSTRAP

# Local import
from components import dashboard_layout, price_history, data_visualization


def main():

    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Insert Dashboard Title Here"
    app.layout = dashboard_layout.create_layout(app)
    app.run()

    data = price_history.get_price_history(ticker_list=['AAPL', 'MSFT'], save_csv=True, period='2y')
    data_visualization.line_chart(dataframe=data[["Date","Open Change","Stock Code"]],
                                    hue="Stock Code",
                                    x_axis="Date",
                                    y_axis="Open Change"
                                )

if __name__ == "__main__":
    main()