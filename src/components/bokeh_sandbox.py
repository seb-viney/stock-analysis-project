# Import Python modules
import math
import datetime as dt

# Third party imports
import numpy as np
import yfinance as yf

from bokeh.io import curdoc
from bokeh.plotting import figure, show
from bokeh.layouts import row, column
from bokeh.models import TextInput, Button, DatePicker, MultiChoice

# Local import

import price_history
search_list=['GOOG', 'GOOGL', 'MSFT', 'AMZN']


def load_data(ticker1, ticker2, start, end):
    ticker1_df = yf.download(ticker1, start, end)
    ticker2_df = yf.download(ticker2, start, end)
    return ticker1_df, ticker2_df

def plot_candle_stick(data, indicators, sync_axis=None):
    dataframe = data
    gain = dataframe.Close > dataframe.Open
    loss = dataframe.Open > dataframe.Close
    candle_width = 12*60*60*1000
    if sync_axis is not None:
        plot = figure(x_axis_type="datetime", tools="pan, wheel_zoom, reset, save", width=1000,
                      x_range=sync_axis)
    else:
        plot = figure(x_axis_type="datetime", tools="pan, wheel_zoom, reset, save", width=1000)

    plot.xaxis.major_label_orientation = math.pi / 4
    plot.grid.grid_line_alpha = 0.25

    plot.segment(dataframe.index, dataframe.High,
                 dataframe.index, dataframe.Low, 
                 color="black")
    plot.vbar(dataframe.index[gain], 
                candle_width,
                dataframe.Open[gain], 
                dataframe.Close[gain], 
                fill_color="#00ff00",
                line_color="#00ff00")
    plot.vbar(dataframe.index[loss],
                candle_width,
                dataframe.Open[loss],
                dataframe.Close[loss],
                fill_color="#ff0000",
                line_color="#ff0000")
    
    for indicator in indicators:
        if indicator == "100 Day SMA":
            dataframe['SMA100'] = dataframe['Close'].rolling(100).mean()
            plot.line(dataframe.index, dataframe.SMA100, color="purple", legend_label=indicator)
        elif indicator == "30 Day SMA":
            dataframe['SMA30'] = dataframe['Close'].rolling(30).mean()
            plot.line(dataframe.index, dataframe.SMA30, color="blue", legend_label=indicator)
        elif indicator == "Linear Regression Line":
            par = np.polyfit(range(len(dataframe.index)), dataframe.Close.values, 1, full=True)
            slope = par[0][0]
            intercept = par[0][1]
            y_pred = [slope * i + intercept for i in range(len(dataframe.index.values))]
            dataframe['LRL'] = dataframe['Close'].rolling(30).mean()
            plot.segment(dataframe.index[0], y_pred[0],
                         dataframe.index[-1], y_pred[-1],
                         color="red",
                         legend_label=indicator)
    plot.legend.location = "top_left"
    plot.legend.click_policy = "hide"
    return plot
    

def on_button_click(ticker1, ticker2, start, end, indicators):
    ticker1_df, ticker2_df = load_data(ticker1, ticker2, start, end)
    plot_1 = plot_candle_stick(ticker1_df, indicators)
    plot_2 = plot_candle_stick(ticker2_df, indicators, sync_axis=plot_1.x_range)
    curdoc().clear()
    curdoc().add_root(layout)
    curdoc().add_root(row(plot_1, plot_2))


## ---------LAYOUT---------
stock1_text = TextInput(title="Stock 1")
stock2_text = TextInput(title="Stock 2")

todays_date = dt.datetime.now().strftime("%Y-%m-%d")
date_picker_from = DatePicker(title="Start Date", value="2020-01-01", max_date=todays_date)
date_picker_to = DatePicker(title="End Date", value=todays_date, max_date=todays_date)

indicator_choice = MultiChoice(options=["100 Day SMA",
                                        "30 Day SMA",
                                        "Linear Regression Line"])

load_button = Button(label="Load Data", button_type="success")
load_button.on_click(lambda: on_button_click(stock1_text.value, stock2_text.value, 
                                             date_picker_from.value, date_picker_to.value,
                                             indicator_choice.value
                                            ))

layout = column(stock1_text, 
                stock2_text, 
                date_picker_from, 
                date_picker_to, 
                indicator_choice, 
                load_button)
curdoc().clear()
curdoc().add_root(layout)
on_button_click("GOOG", "MSFT", 
                    "2020-01-01", todays_date,
                    ["100 Day SMA", "30 Day SMA", "Linear Regression Line"]
                )

if __name__ == "__main__":
    ticker1_df, ticker2_df = load_data('goog', 'msft', "2020-01-01", dt.datetime.now().strftime("%Y-%m-%d"))
    indicators=["100 Day SMA", "30 Day SMA", "Linear Regression Line"]
    plot_1 = plot_candle_stick(data=ticker1_df, indicators=indicators)
    plot_2 = plot_candle_stick(ticker2_df, indicators, sync_axis=plot_1.x_range)
    show(row(plot_1, plot_2))
