
city_counts = df["city"].value_counts()

plt.figure(figsize=(10, 7))

plt.barh(city_counts.index, city_counts.values)

plt.title("Customers by City")
plt.xlabel("Number of Customers")
plt.ylabel("City")

plt.tight_layout()

plt.savefig(
    "visuals/customers_by_city.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()