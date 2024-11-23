import numpy as np
import pandas as pd
import plotly.express as px
from matplotlib.pyplot import legend


def create_interactive_plotly(df):
    """
    Creates an interactive scatter plot using Plotly.

    Parameters:
    df (DataFrame): A DataFrame containing 'x' and 'y' columns.
    """
    # Creating an interactive scatter plot
    df['category'] = np.random.choice(['Group A', 'Group B', 'Group C'], size=len(df))
    fig = px.scatter(df, x='x', y='y', title='Interactive Scatter Plot of x vs y', color="category",
                     labels={'x': 'x', 'y': 'y)'}, )
    fig.show()
    return fig


# Example data
df = pd.DataFrame({'x': np.random.rand(50), 'y': np.random.rand(50)})
create_interactive_plotly(df)
