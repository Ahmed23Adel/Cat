# Cat
For any categorical columns in dataframe, you may want to create new column for each unique value in that column.

suppose for column "LandContour", it's object ("string"), it has values {"Lvl","HLS","Bnk","Low"}, so we create columns {"LandContour_Lvl","LandContour_HLS","LandContour_Bnk","LandContour_Low"}


<img width="365" alt="Screen Shot 2021-08-28 at 2 57 08 PM" src="https://user-images.githubusercontent.com/69484554/131218662-4becab8d-1b0f-4cf4-bb5b-f3c61151eddd.png">

and taking these columns take values:


![Uploading Screen Shot 2021-08-28 at 2.59.52 PM.png…]()

if cell ith row for column LandContour_Low equal one; then that mean that LandContour in 4th row is equal to "Low", otherwise it equal to zero.




code example:

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

