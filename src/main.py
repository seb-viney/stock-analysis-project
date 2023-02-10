# Third party imports
from dash import Dash ,html
from dash_bootstrap_components.themes import BOOTSTRAP

# Local import
from components import dashboard, price_history, data_visualization


def main():
    search_list=['GOOG', 'GOOGL', 'MSFT', 'AMZN']
    data = price_history.get_price_history(ticker_list=search_list, save_csv=True, period='2y')

    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Insert Dashboard Title Here"
    app.layout = dashboard.create_layout(app,dropdown_title ='Stock Codes', dropdown_item_list=search_list)
    app.run()

    data_visualization.line_chart(dataframe=data[["Date","Open Change","Stock Code"]],
                                    hue="Stock Code",
                                    x_axis="Date",
                                    y_axis="Open Change"
                                )

if __name__ == "__main__":
    main()