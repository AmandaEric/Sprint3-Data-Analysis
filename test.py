import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Load Dataset
# ---------------------------

df = pd.read_csv("womens_wrestling_2024.csv")

print("Full Dataset:\n")
print(df)

# ---------------------------
# QUESTION 1
# Which country won the most medals?
# ---------------------------

medal_count = df.groupby("Country")["Medal"].count()

print("\nMedal Count by Country:")
print(medal_count.sort_values(ascending=False))

# ---------------------------
# QUESTION 2
# How many gold medals did Japan win?
# ---------------------------

japan_gold = df[(df["Country"] == "Japan") & (df["Medal"] == "Gold")]

print("\nJapan Gold Medals:")
print(japan_gold)

# ---------------------------
# FILTER Example
# Show only USA wrestlers
# ---------------------------

usa_wrestlers = df[df["Country"] == "USA"]

print("\nUSA Wrestlers:")
print(usa_wrestlers)

# ---------------------------
# SORT Example
# Sort by Weight Class
# ---------------------------

sorted_df = df.sort_values(by="WeightClass")

print("\nSorted by Weight Class:")
print(sorted_df)

# ---------------------------
# AGGREGATION Example
# Count medals by type
# ---------------------------

medal_type_count = df["Medal"].value_counts()

print("\nMedals by Type:")
print(medal_type_count)

# ---------------------------
# STRETCH: Graph
# ---------------------------

medal_count.plot(kind="bar")
plt.title("Medals by Country - Women's Wrestling Paris 2024")
plt.xlabel("Country")
plt.ylabel("Number of Medals")
plt.show()
