import pandas as pd

#load the csv files
df1 = pd.read_csv('data/daily_sales_data_0.csv')
df2 = pd.read_csv('data/daily_sales_data_1.csv')
df3 = pd.read_csv('data/daily_sales_data_2.csv')

#Filter rows to only include pink morsel
df1 = df1[df1["product"]=="pink morsel"]
df2 = df2[df2["product"]=="pink morsel"]
df3 = df3[df3["product"]=="pink morsel"]

#turn the price value to numeric
df1["price"] = df1["price"].replace('[\$,]', '', regex=True).astype(float)
df2["price"] = df2["price"].replace('[\$,]', '', regex=True).astype(float)
df3["price"] = df3["price"].replace('[\$,]', '', regex=True).astype(float)
df1["price"] = pd.to_numeric(df1["price"])
df2["price"] = pd.to_numeric(df2["price"])
df3["price"] = pd.to_numeric(df3["price"])

#create a new sales column
df1["sales"] = df1["quantity"] * df1["price"]
df2["sales"] = df2["quantity"] * df2["price"]
df3["sales"] = df3["quantity"] * df3["price"]

#keep only the relevant columns
df1 = df1[["sales","date","region"]]
df2 = df2[["sales","date","region"]]
df3 = df3[["sales","date","region"]]

#combine all csv
combined_df = pd.concat([df1,df2,df3])

#save combined csv
combined_df.to_csv('data/combined_sales_data.csv', index=False)

print("Task 2 completed , combined_sales_data.csv created successfully")
print(combined_df.head())