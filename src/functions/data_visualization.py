# Third party imports
import pandas as pd
import matplotlib.pyplot as matplt
import seaborn as sns

def line_chart(dataframe, hue="Stock Code", x_axis="Date", y_axis="Open"):
    
    '''
    example call: data_visualization.line_chart(dataframe=data[["Open","Stock Code"]])
    dataframe: The data
    hue: Which column in the data to compare
    '''
    
    sns.set_theme(style="darkgrid", palette="pastel")
    sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
    sns.lineplot(data=dataframe, x=x_axis, y=y_axis, hue=hue)
    matplt.show()

    