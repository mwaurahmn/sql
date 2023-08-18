# Import Libraries
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# Visualization display
sns.set(rc={'figure.figsize':(15,8)}, font_scale = 2)
sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 16
matplotlib.rcParams['figure.figsize'] = (15, 8)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

def run_query(query, connection):
    '''
    Takes a SQL query as an argument.
    Returns the results in a dataframe.
    '''
    df = pd.read_sql(query, con = connection)
    return df

def show_tables(query, connection):
    '''
    Calls run_query() function to return a list of all tables and views in the database.
    '''
    df = run_query(query, connection)
    ls = df[df.columns[0]].values.tolist()
    return ls

def horizontal_barplot(y, x, title, xlabel):
    '''
    Takes the x and y variables and plots a horizontal barplot.
    Also takes the title of the plot and the label of the x-axis.
    '''
    plt.barh(y, x)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.tick_params(left=False)
    sns.despine(left=True)
    plt.show()

def lineplot(x, y, category, title):
    '''
    Takes the variables needed to plot a line graph.
    '''
    sns.lineplot(x = x, y = y, hue = category)
    plt.title(title)
    plt.show()