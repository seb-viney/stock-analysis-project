# Import Python modules
import os

# Third party imports
import pandas as pd
import yfinance as yf

def get_price_history(ticker_list:str=[], period:str='5d', interval:str='1d', save_csv:bool=False):
    
    '''
    example call: get_price_history(ticker_list=['AAPL', 'MSFT'], save_csv=True)
    ticker_list: list of stock codes
    valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
    valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
    '''

    df_list = list()
    for ticker in ticker_list:
        data = yf.download(tickers=ticker, group_by="Ticker", period=period, interval=interval)
        data['Stock Code'] = ticker
        df_list.append(data)
    
    price_history_df = pd.concat(df_list)

    if save_csv == True:
        price_history_df.to_csv('data\price_history.csv')

    return price_history_df
    