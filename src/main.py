# Third party imports


# Local import
from src.functions import price_history


def main():

    data = price_history.get_price_history(ticker_list=['AAPL', 'MSFT'], save_csv=True)

if __name__ == "__main__":
    main()