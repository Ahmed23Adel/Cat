# Cat
For any categorical columns in dataframe, you may want to create new column for each unique value in that column.

suppose for column "LandContour", it's object ("string"), it has values {"Lvl","HLS","Bnk","Low"}, so we create columns {"LandContour_Lvl","LandContour_HLS","LandContour_Bnk","LandContour_Low"}


<img width="365" alt="Screen Shot 2021-08-28 at 2 57 08 PM" src="https://user-images.githubusercontent.com/69484554/131218662-4becab8d-1b0f-4cf4-bb5b-f3c61151eddd.png">

and taking these columns take values:


<img width="572" alt="Screen Shot 2021-08-28 at 3 02 23 PM" src="https://user-images.githubusercontent.com/69484554/131218836-a06c1147-26b0-4b86-b185-2d1780622fa0.png">


if cell ith row for column LandContour_Low equal one; then that mean that LandContour in 4th row is equal to "Low", otherwise it equal to zero.




code example:
``` python

data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18],'MSZoning':['RL','RM','RL','FV'],
        'Street':['Pave','Pave','Grvl','Grvl'],
        'Alley':['Pave','Grvl','Pave','Grvl'],
        'LandContour':['Lvl','HLS','Bnk','Low']}
        
# Create DataFrame
df = pd.DataFrame(data)

# Print the output.
print(df.head())
expand_cat_cols_rmv_cols(df,rmv=['Street'],exclude=['Name'])
print(df.head())

```

quick documentation :

def expand_cat_cols_rmv_all(df,exclude=None):
    """ for each non numeric colum say X, take all value of that column, Y, and Z; we create 
    column X_Y, and X_Z  and remove column X. and insert values 0, or 1 saying ith row is equal to
    Y, or Z.
    
    this funcoitn removes all previous columsn X
"""

def expand_cat_cols_rmv_cols(df,rmv=None,exclude=None):
    """ for each non numeric colum say X, take all value of that column, Y, and Z; we create 
    column X_Y, and X_Z  and remove column X. and insert values 0, or 1 saying ith row is equal to
    Y, or Z.

    this doesn't delete all column, only in rmv list
    """

Language used: python</br>


