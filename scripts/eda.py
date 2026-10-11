import pandas as pd 
import numpy as np
df = pd.read_csv("data/processed/customers_cleaned.csv")

# Count customers by state
state_counts = df["state"].value_counts()



import matplotlib.pyplot as plt
plt.figure( figsize = (10,7))
plt.bar(state_counts.index, state_counts.values)
plt.title("Customers by State")
plt.xlabel("State")
plt.ylabel("Number of Customers")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visuals/customers_by_state.png", dpi=300, bbox_inches="tight")
plt.show()


# age distribution visualization
plt.figure( figsize= (10,6))
plt.hist(df["age"].dropna(), bins = 8)

plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.savefig("visuals/customer_age_distribution.png", dpi=300, bbox_inches="tight")
plt.show()


 

# Gender distribution pie chart
import matplotlib.pyplot as plt
gender_counts = df["gender"].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    gender_counts.values,
    labels=gender_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Customer Gender Distribution")

plt.tight_layout()
plt.savefig(
    "visuals/customer_gender_distribution.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()


# signup_distribution

# Signup date analysis

df["signup_date"] = pd.to_datetime(df["signup_date"])

monthly_signups = df["signup_date"].dt.to_period("M").value_counts().sort_index()

print("Monthly Signups:")
print(monthly_signups)


plt.figure(figsize=(10, 6))

plt.bar(monthly_signups.index.astype(str), monthly_signups.values)

plt.title("Customer Signups by Month")
plt.xlabel("Month")
plt.ylabel("Number of Signups")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "visuals/customer_signups_by_month.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()



city_counts = df["city"].value_counts()

plt.figure(figsize=(10, 7))

plt.bar(city_counts.index, city_counts.values)

plt.title("Customers by City")
plt.xlabel("Number of Customers")
plt.ylabel("City")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "visuals/customers_by_city.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()