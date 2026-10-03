"""
Pandas Fundamentals - Assignment Solution (pandas_fundamentals.py)

Mental Model:
                   PANDAS
                      │
         ┌────────────┴────────────┐
         ↓                         ↓
      Series                   DataFrame
    one column                   table
                                    │
               ┌────────────────────┼─────────────────┐
               ↓                    ↓                 ↓
           Indexing              Filtering          Sorting
               │
         ┌─────┴─────┐
         ↓           ↓
       loc          iloc
      labels      positions

                    ↓
                 CSV files
               ↙           ↘
            read_csv     to_csv
"""

import pandas as pd
import os

# ==============================================================================
# Exercise 1 — Series
# ==============================================================================
# Create a Series containing:
#   Python -> 90
#   Java -> 80
#   C++ -> 75
#   JavaScript -> 85
# Give the languages as the index. Then retrieve the score of Java.

print("--- Exercise 1: Series ---")
scores_series = pd.Series(
    [90, 80, 75, 85],
    index=["Python", "Java", "C++", "JavaScript"]
)
print("Language Scores Series:\n", scores_series)
print("\nJava Score (scores_series['Java']):", scores_series["Java"])
print()


# ==============================================================================
# Exercise 2 — DataFrame
# ==============================================================================
# Create DataFrame with columns: Name, Age, Marks, City
# Data:
#   Arun    21   85   Chennai
#   Rahul   22   92   Salem
#   Priya   20   78   Madurai
#   Karthik 23   65   Chennai

print("--- Exercise 2: DataFrame ---")
students_df = pd.DataFrame({
    "Name": ["Arun", "Rahul", "Priya", "Karthik"],
    "Age": [21, 22, 20, 23],
    "Marks": [85, 92, 78, 65],
    "City": ["Chennai", "Salem", "Madurai", "Chennai"]
})
print(students_df)
print("Shape:", students_df.shape)
print()


# ==============================================================================
# Exercise 3 — Indexing (iloc vs loc)
# ==============================================================================
# Using the DataFrame:
# 1. Select the first row using iloc.
# 2. Select Rahul's row using loc.
# 3. Select the Marks column.
# 4. Select Name and City.
# 5. Get Priya's marks using iloc.

print("--- Exercise 3: Indexing ---")
print("1. First row (df.iloc[0]):\n", students_df.iloc[0])
print("\n2. Rahul's row (df.loc[1]):\n", students_df.loc[1])
print("\n3. Marks column (df['Marks']):\n", students_df["Marks"])
print("\n4. Name and City columns (df[['Name', 'City']]):\n", students_df[["Name", "City"]])
print("\n5. Priya's marks (df.iloc[2, 2]):", students_df.iloc[2, 2])
print()


# ==============================================================================
# Exercise 4 — Filtering
# ==============================================================================
# Find:
# 1. Students with marks greater than 80.
# 2. Students younger than 22.
# 3. Students from Chennai.
# 4. Students with marks >= 80 and age > 20.

print("--- Exercise 4: Filtering ---")
print("1. Marks > 80:\n", students_df[students_df["Marks"] > 80])
print("\n2. Age < 22:\n", students_df[students_df["Age"] < 22])
print("\n3. City == Chennai:\n", students_df[students_df["City"] == "Chennai"])
print("\n4. Marks >= 80 AND Age > 20:\n", students_df[(students_df["Marks"] >= 80) & (students_df["Age"] > 20)])
print()


# ==============================================================================
# Exercise 5 — Sorting
# ==============================================================================
# Sort the DataFrame:
# 1. By marks ascending.
# 2. By marks descending.
# 3. By age ascending.

print("--- Exercise 5: Sorting ---")
print("1. By Marks Ascending:\n", students_df.sort_values("Marks"))
print("\n2. By Marks Descending:\n", students_df.sort_values("Marks", ascending=False))
print("\n3. By Age Ascending:\n", students_df.sort_values("Age"))
print()


# ==============================================================================
# Exercise 6 — CSV Storage
# ==============================================================================
# Save your DataFrame as students.csv, then load that CSV back into a new DataFrame.

print("--- Exercise 6: CSV Storage ---")
csv_path = "students.csv"
students_df.to_csv(csv_path, index=False)
print(f"DataFrame successfully exported to '{csv_path}'.")

loaded_students_df = pd.read_csv(csv_path)
print("Loaded DataFrame from CSV:\n", loaded_students_df)

# Cleanup generated file
if os.path.exists(csv_path):
    os.remove(csv_path)
print()


# ==============================================================================
# 🔥 Mini Challenge
# ==============================================================================
# Find students who:
#   are from Chennai AND have marks above 70
# Then sort those students by marks from highest to lowest.

print("--- Mini Challenge ---")
chennai_top = students_df[
    (students_df["City"] == "Chennai") & (students_df["Marks"] > 70)
].sort_values("Marks", ascending=False)

print("Chennai students with Marks > 70 (Highest to Lowest):\n", chennai_top)
