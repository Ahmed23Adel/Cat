import pandas as pd
# intialise data of lists.
""" This module Cat, is designed for categorical data which has specific count of values in columns
for for every non numeric column, say X; we look for all values in column X say Y Z, we create new 
columns called X_Y, X_Z, and insert values eithre 1, or 0 coreponding if ith row was equal to Y or Z.


"""

def get_non_num_cols(df):
    """ return non numeric column in dataframe

    Parameters:
    -----------
    df: dataframe for which we want to extract all non numeric columns

    Returne:
    ----------
    list of column names of non numeric columns in data frame 
    """
    numerics = ['number']
    newdf = df.select_dtypes(exclude=numerics).columns
    return newdf 

def expand_cat_cols_rmv_all(df,exclude=None):
    """ for each non numeric colum say X, take all value of that column, Y, and Z; we create 
    column X_Y, and X_Z  and remove column X. and insert values 0, or 1 saying ith row is equal to
    Y, or Z.

    this funcoitn removes all previous columsn X

    Parameters:
    ----------
    df: data frame we want to remove non numeric columsn
    exclude: (optional) if there is a specific column that we dont' want to expand, put it in exclude list

    return:
    --------
    None. 
    it edit the input data frame
    
    """
    cols=get_non_num_cols(df)
    for col in cols:
        if exclude==None or( not exclude == None and  not col in exclude):
            vals = df[col].unique()
            for val in vals:
                new_col_name=col + "_" +val
                df[new_col_name]=int(df.loc[:,col].to_list()==val)
            print(col)
            del df[col]


def expand_cat_cols_rmv_cols(df,rmv=None,exclude=None):
    """ for each non numeric colum say X, take all value of that column, Y, and Z; we create 
    column X_Y, and X_Z  and remove column X. and insert values 0, or 1 saying ith row is equal to
    Y, or Z.

    this doesn't delete all column, only in rmv list
    Parameters:
    ----------
    df: data frame we want to remove non numeric columsn
    exclude: (optional) if there is a specific column that we dont' want to expand, put it in exclude list
    rmv: list of columns you need to remove after expansion.
    
    return:
    --------
    None. 
    it edit the input data frame
    """

    cols=get_non_num_cols(df)
    for col in cols:
        if exclude==None or( not exclude == None and  not col in exclude):
            vals = df[col].unique()
            for val in vals:
                new_col_name=col + "_" +val
                df[new_col_name]=[int(i ==val) for i in  df.loc[:,col].to_list()]
            print(col)
            if not rmv ==None and col in rmv:
                del df[col]

        








