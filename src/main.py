# Third party imports


# Local import
from functions import price_history, data_visualization


def main():

    data = price_history.get_price_history(ticker_list=['AAPL', 'MSFT'], save_csv=True, period='2y')
    data_visualization.line_chart(dataframe=data[["Date","Open Change","Stock Code"]],
                                    hue="Stock Code",
                                    x_axis="Date",
                                    y_axis="Open Change"
                                )

if __name__ == "__main__":
    main()

    print("test")