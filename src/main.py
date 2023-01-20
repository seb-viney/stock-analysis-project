# Third party imports


# Local import
from functions import price_history, data_visualization


def main():

    data = price_history.get_price_history(ticker_list=['AAPL', 'MSFT'], save_csv=True)
    data_visualization.line_chart(dataframe=data[["Open","Stock Code"]])

if __name__ == "__main__":
    main()

    print("test")