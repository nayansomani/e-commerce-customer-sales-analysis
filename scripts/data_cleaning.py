import pandas as pd
df = pd.read_csv("data/raw/customers.csv")
# data cleaning step
print("missing value:", df.isnull().sum())

print("rows with missing value:  ")
print(df[df.isnull().any(axis = 1)])
# cleaning age
invalid_age = df[(df['age']<12) | (df['age']>100)]  
print("invalid age", invalid_age)
print("replace invalid age to NAN")

df.loc[(df["age"] < 12) | (df["age"] > 100), "age"] = pd.NA 

print(df["age"])

# checking duplicate values
colm = ["customer_name","gender","age","city","state","signup_date" ]
duplicate = df[df.duplicated(subset=colm,keep = False)]


# unique city
df["city"] = df['city'].str.strip().str.title()
print("unique citty" , df["city"].unique())


# duplicate value
df = df.drop_duplicates(subset = ["customer_name","gender","age","city","state","signup_date"], keep="first")
df = df.reset_index(drop=True)
print("dataset after removal duplicate")
print(df)
print(df.shape)

# Save cleaned dataset
df.to_csv("data/processed/customers_cleaned.csv", index=False)

print("Cleaned dataset saved successfully!")