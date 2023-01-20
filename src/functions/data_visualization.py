# Third party imports
import pandas as pd
import matplotlib.pyplot as matplt
import seaborn as sns

def line_chart(dataframe, hue="Stock Code", x_axis="Date", y_axis="Open"):
    
    '''
    example call: 
    
    '''
    sns.set_theme(style="darkgrid", palette="pastel")
    sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})
    sns.lineplot(data=dataframe, x=x_axis, y=y_axis, hue=hue)
    matplt.show()

    