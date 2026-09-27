import pandas as pd
df = pd.read_csv("data/raw/customers.csv")
print("========== DATASET OVERVIEW ==========")
print("Dataset shape:", df.shape)  #for see row and column
print("Column names:", df.columns.tolist())  # to see column names
print("Data types:")
print(df.dtypes)   #to see data types of each column
print("Null values per column:")
print(df.isnull().sum())  # to see null values in each column
print("Duplicate rows:", df.duplicated().sum())  # to see duplicate rows
print("Unique customer IDs:", df['customer_id'].nunique())  # to see unique customer IDs
print("Age statistics:")
print(df['age'].describe())  # to see summary statistics of age
print("Gender distribution:")
print(df['gender'].value_counts())  # to see count of each gender
print("City distribution:")
print(df['city'].value_counts())  # to see count of each city
print("State distribution:")
print(df['state'].value_counts())  # to see count of each state
print("Signup date range:")
print("Min:", df['signup_date'].min(), "Max:", df['signup_date'].max())  # to see the date range of signups
