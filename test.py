import pandas as pd
# import matplotlib.pyplot as plt

# ---------------------------
# Load Dataset
# ---------------------------

df = pd.read_csv("2025_D1_Womens_Wrestling_Top3_by_Weight.csv")

print("Full Dataset:\n")
print(df)

# ---------------------------
# QUESTION 1
# Which college won the most matches?
# ---------------------------

total_wins = df.groupby("School")["Wins"].sum()

print("\nTotal Wins by School:")
print(total_wins.sort_values(ascending=False))

# ---------------------------
# QUESTION 2
# Which school scored the most total points?
# ---------------------------

total_points = df.groupby("School")["Total_Points_Scored"].sum()

print("\nTotal Points by School:")
print(total_points.sort_values(ascending=False))

# ---------------------------
# FILTER Example
# Show only Iowa wrestlers
# ---------------------------

iowa_wrestlers = df[df["School"] == "Iowa"]

print("\nIowa Wrestlers:")
print(iowa_wrestlers)

# ---------------------------
# SORT Example
# Sort by Weight Class
# ---------------------------

sorted_df = df.sort_values(by="Weight_Class_lbs")

print("\nSorted by Weight Class:")
print(sorted_df)

# ---------------------------
# AGGREGATION Example
# Total Takedowns by School
# ---------------------------

takedowns_total = df.groupby("School")["Takedowns"].sum()

print("\nTotal Takedowns by School:")
print(takedowns_total)

# ---------------------------
# STRETCH: Graph
# Bar chart of total wins by school
# ---------------------------

# total_wins.plot(kind="bar")
# plt.title("Total Wins by School")
# plt.xlabel("School")
# plt.ylabel("Number of Wins")
# plt.show()
tech_falls_per_school = df.groupby("School")["Tech_Falls"].sum()
print("\nEach schools total amount of Tech-Falls:")
print(tech_falls_per_school)