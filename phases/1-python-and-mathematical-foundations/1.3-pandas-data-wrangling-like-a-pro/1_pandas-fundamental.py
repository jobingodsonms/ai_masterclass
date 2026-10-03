"""
Pandas Fundamentals - Topic File

Structure:
1. Concept (What it is)
2. Why AI engineers use it
3. Syntax
4. Example (runnable)
5. Mini Practice (all mini practice for this topic with solutions)
6. Assignments (solutions included + Mini Challenge)
"""

import pandas as pd
import os

# ==============================================================================
# 1. Concept (What it is)
# ==============================================================================
# Pandas is Python's premier library for tabular data manipulation and analysis.
#
# Key Concepts:
# 1. Series:
#    A 1-dimensional labeled collection of data (think: a single column of a table).
#    Contains both Index labels and Values.
# 2. DataFrame:
#    A 2-dimensional labeled data structure (think: a spreadsheet or SQL table).
#    Composed of multiple Series sharing a common index.
# 3. Index & Structure:
#    - df.index: Row labels.
#    - df.columns: Column headers.
#    - df.shape: Tuple of (rows, columns).
# 4. Indexing (loc vs iloc):
#    - loc: Label-based lookup (where is the label?).
#    - iloc: Position-based lookup (where is the integer position 0, 1, 2...?).
# 5. Filtering (Boolean Masking):
#    Selecting rows where conditions evaluate to True.
#    Must use bitwise `&` (AND) and `|` (OR) with parentheses `(cond1) & (cond2)`.
# 6. Sorting:
#    Ordering rows by one or more column values using `sort_values()`.
# 7. CSV I/O:
#    Reading (`pd.read_csv`) and writing (`df.to_csv(..., index=False)`) dataset files.
#
# Mental Map:
#                    PANDAS
#                       │
#          ┌────────────┴────────────┐
#          ↓                         ↓
#       Series                   DataFrame
#     one column                   table
#                                     │
#                ┌────────────────────┼─────────────────┐
#                ↓                    ↓                 ↓
#            Indexing              Filtering          Sorting
#                │
#          ┌─────┴─────┐
#          ↓           ↓
#        loc          iloc
#       labels      positions
#
#                     ↓
#                  CSV files
#                ↙           ↘
#             read_csv     to_csv


# ==============================================================================
# 2. Why AI engineers use it
# ==============================================================================
# - Data Ingestion: Loading structured datasets from CSV, Excel, Parquet, or SQL databases.
# - Exploratory Data Analysis (EDA): Quick inspection of dataset shape, data types, and summaries.
# - Data Cleaning: Handling missing values, filtering outliers, dropping redundant columns.
# - Feature Engineering: Creating new feature columns, encoding categorical labels, transforming text/dates.
# - ML Pipeline Prep: Extracting feature matrices X (DataFrames) and target vectors y (Series) for Scikit-Learn/PyTorch.


# ==============================================================================
# 3. Syntax
# ==============================================================================
# Series Creation:
#   s = pd.Series([85, 90, 78])
#   s = pd.Series([85, 90, 78], index=["Arun", "Rahul", "Priya"])
#   s = pd.Series({"Arun": 85, "Rahul": 90, "Priya": 78})
#
# DataFrame Creation:
#   df = pd.DataFrame({"Name": ["Arun", "Rahul"], "Age": [21, 22]})
#
# Inspection Attributes:
#   df.shape, df.columns, df.index, df.head()
#
# Indexing (loc vs iloc):
#   df.iloc[row_pos]                  -> Select row by 0-based integer position
#   df.iloc[row_pos, col_pos]         -> Select specific cell by position
#   df.loc[row_label]                 -> Select row by index label
#   df.loc[row_label, "ColumnName"]   -> Select cell by row label and column name
#
# Selecting Columns:
#   df["ColumnName"]                  -> Returns 1D Series
#   df[["Col1", "Col2"]]              -> Returns 2D DataFrame
#
# Filtering:
#   df[df["Marks"] > 80]
#   df[(df["Age"] > 20) & (df["Marks"] > 80)]
#   df[(df["City"] == "Chennai") | (df["Marks"] >= 90)]
#
# Sorting:
#   df.sort_values("Marks")                              -> Ascending
#   df.sort_values("Marks", ascending=False)             -> Descending
#   df.sort_values(["Age", "Marks"], ascending=[True, False])
#
# CSV Storage:
#   df = pd.read_csv("filename.csv")
#   df.to_csv("filename.csv", index=False)


# ==============================================================================
# 4. Example (Runnable)
# ==============================================================================
print("=" * 60)
print("SECTION 4: RUNNABLE EXAMPLES")
print("=" * 60)

# --- 1. Series & Custom Index ---
marks_series = pd.Series([85, 90, 78], index=["Arun", "Rahul", "Priya"])
print("Series with Custom Index:\n", marks_series)
print("Rahul's Score (label lookup):", marks_series["Rahul"])

# --- 2. DataFrame Creation ---
data = {
    "Name": ["Arun", "Rahul", "Priya"],
    "Age": [21, 22, 20],
    "Marks": [85, 90, 78]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)
print("Shape  :", df.shape)
print("Columns:", list(df.columns))

# --- 3. Indexing: loc vs iloc ---
print("\nFirst row via iloc[0]:\n", df.iloc[0])
print("Cell via iloc[1, 2] (Rahul's Marks):", df.iloc[1, 2])
print("Cell via loc[0, 'Name']:", df.loc[0, "Name"])

# --- 4. Filtering ---
top_students = df[df["Marks"] > 80]
print("\nStudents with Marks > 80:\n", top_students)

# --- 5. Sorting ---
sorted_df = df.sort_values("Marks", ascending=False)
print("\nSorted by Marks Descending:\n", sorted_df)


# ==============================================================================
# 5. Mini Practice (all mini practice for this topic) + Solutions
# ==============================================================================
print("\n" + "=" * 60)
print("SECTION 5: MINI PRACTICE")
print("=" * 60)

# Practice 1: Series lookup by label
languages = pd.Series({"Python": 90, "Java": 80, "C++": 75, "JavaScript": 85})
print("Mini Practice 1 (Java score):", languages["Java"])

# Practice 2: Select multiple columns from a DataFrame
sample_df = pd.DataFrame({
    "Name": ["Arun", "Rahul", "Priya", "Karthik"],
    "Age": [21, 22, 20, 23],
    "Marks": [85, 92, 78, 65],
    "City": ["Chennai", "Salem", "Madurai", "Chennai"]
})
print("\nMini Practice 2 (Select Name & City):\n", sample_df[["Name", "City"]])

# Practice 3: Combined condition filtering
filtered_sample = sample_df[(sample_df["City"] == "Chennai") & (sample_df["Marks"] > 70)]
print("\nMini Practice 3 (Chennai & Marks > 70):\n", filtered_sample)


# ==============================================================================
# 6. Assignments (Solutions Included)
# ==============================================================================
# Rule: No Google/AI. Use only Python docs, notes, and experiments.
print("\n" + "=" * 60)
print("SECTION 6: ASSIGNMENTS & EXERCISES")
print("=" * 60)

# ------------------------------------------------------------------------------
# Exercise 1 — Series
# ------------------------------------------------------------------------------
lang_scores = pd.Series(
    [90, 80, 75, 85],
    index=["Python", "Java", "C++", "JavaScript"]
)
print("\n[Exercise 1 — Series]")
print("Series:\n", lang_scores)
print("Java Score:", lang_scores["Java"])

# ------------------------------------------------------------------------------
# Exercise 2 — DataFrame
# ------------------------------------------------------------------------------
students_df = pd.DataFrame({
    "Name": ["Arun", "Rahul", "Priya", "Karthik"],
    "Age": [21, 22, 20, 23],
    "Marks": [85, 92, 78, 65],
    "City": ["Chennai", "Salem", "Madurai", "Chennai"]
})
print("\n[Exercise 2 — DataFrame]\n", students_df)

# ------------------------------------------------------------------------------
# Exercise 3 — Indexing
# ------------------------------------------------------------------------------
print("\n[Exercise 3 — Indexing]")
print("1. First row (iloc[0]):\n", students_df.iloc[0])
print("2. Rahul's row (loc[1]):\n", students_df.loc[1])
print("3. Marks column:\n", students_df["Marks"])
print("4. Name and City columns:\n", students_df[["Name", "City"]])
print("5. Priya's marks via iloc[2, 2]:", students_df.iloc[2, 2])

# ------------------------------------------------------------------------------
# Exercise 4 — Filtering
# ------------------------------------------------------------------------------
print("\n[Exercise 4 — Filtering]")
print("1. Marks > 80:\n", students_df[students_df["Marks"] > 80])
print("2. Age < 22:\n", students_df[students_df["Age"] < 22])
print("3. City == Chennai:\n", students_df[students_df["City"] == "Chennai"])
print("4. Marks >= 80 AND Age > 20:\n", students_df[(students_df["Marks"] >= 80) & (students_df["Age"] > 20)])

# ------------------------------------------------------------------------------
# Exercise 5 — Sorting
# ------------------------------------------------------------------------------
print("\n[Exercise 5 — Sorting]")
print("1. Marks Ascending:\n", students_df.sort_values("Marks"))
print("2. Marks Descending:\n", students_df.sort_values("Marks", ascending=False))
print("3. Age Ascending:\n", students_df.sort_values("Age"))

# ------------------------------------------------------------------------------
# Exercise 6 — CSV Storage
# ------------------------------------------------------------------------------
csv_filename = "students.csv"
students_df.to_csv(csv_filename, index=False)
loaded_df = pd.read_csv(csv_filename)

print("\n[Exercise 6 — CSV Storage]")
print("Loaded DataFrame from CSV:\n", loaded_df)

# Clean up created file after verification
if os.path.exists(csv_filename):
    os.remove(csv_filename)

# ------------------------------------------------------------------------------
# Mini Challenge
# ------------------------------------------------------------------------------
print("\n[Mini Challenge]")
chennai_top_students = students_df[
    (students_df["City"] == "Chennai") & (students_df["Marks"] > 70)
].sort_values("Marks", ascending=False)

print("Chennai students with Marks > 70 (Sorted Highest to Lowest):\n", chennai_top_students)
