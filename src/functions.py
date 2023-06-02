# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
    plt.figure(figsize=(15,8))
    plt.barh(y, x)
    plt.title(title, fontsize=27)
    plt.xlabel(xlabel, fontsize=19)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.tick_params(left=False)
    sns.despine(left=True)
    plt.show()