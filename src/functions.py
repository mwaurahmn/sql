# Import Libraries
import pandas as pd

'''
run_query() function.
Takes a SQL query as an argument.
Returns the results in a dataframe.
'''
def run_query(query, connection):
    df = pd.read_sql(query, con = connection)
    return df

'''
show_tables() function.
Calls run_query() function to return a list of all tables and views in the database.
'''
def show_tables(query, connection):
    df = run_query(query, connection)
    ls = df[df.columns[0]].values.tolist()
    return ls
