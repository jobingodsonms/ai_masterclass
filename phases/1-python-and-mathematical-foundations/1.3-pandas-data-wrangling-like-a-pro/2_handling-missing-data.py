"""
Handling Missing Data in Pandas - Topic File

Structure:
1. Concept (What it is)
2. Why AI engineers use it
3. Syntax
4. Example (runnable)
5. Mini Practice (all mini practice for this topic with solutions)
6. Assignments (solutions included + AI/Data Challenge)
"""

import pandas as pd
import numpy as np

# ==============================================================================
# 1. Concept (What it is)
# ==============================================================================
# Real-world datasets are rarely clean. They often contain missing or corrupt values.
# Pandas represents missing numerical/categorical data using `NaN` (Not a Number) or `None`.
#
# Key Concepts:
# 1. Detecting Missing Data:
#    - df.isna(): Returns Boolean DataFrame (True where data is missing).
#    - df.notna(): Opposite of isna() (True where data exists).
#    - df.isna().sum(): Counts total missing values per column.
# 2. Filtering Rows with Missing Data:
#    - df[df["Col"].isna()]: Extracts rows where "Col" is missing.
#    - df[df["Col"].notna()]: Extracts rows where "Col" has valid data.
# 3. Dropping Missing Data:
#    - df.dropna(): Removes all rows with at least one missing value.
#    - df.dropna(subset=["col1", "col2"]): Removes rows missing values ONLY in specified columns.
# 4. Imputation / Filling Strategies:
#    - Mean Imputation: df["Col"].fillna(df["Col"].mean()) -> For symmetric numerical data.
#    - Median Imputation: df["Col"].fillna(df["Col"].median()) -> For skewed numerical data (robust to outliers).
#    - Mode Imputation: df["Col"].fillna(df["Col"].mode()[0]) -> For categorical text data.
#    - Forward Fill: df["Col"].ffill() -> Propagates previous valid value forward (great for time-series).
#    - Backward Fill: df["Col"].bfill() -> Propagates next valid value backward.
# 5. Cleaning Messy String Placeholders:
#    - pd.to_numeric(df["Col"], errors="coerce"): Converts "N/A", "?", "" into proper NaN values.
#
# Missing Data Workflow:
#   Inspect dataset -> Find & Count missing values -> Choose per-column strategy -> Impute/Drop -> Re-verify (isna().sum())


# ==============================================================================
# 2. Why AI engineers use it
# ==============================================================================
# - Model Requirements: Machine Learning algorithms (Scikit-Learn, PyTorch, XGBoost) fail or crash when fed NaNs.
# - Preserving Data Integrity: Avoids biased model predictions caused by improper zero-filling (e.g. 0 age vs mean age).
# - Outlier Protection: Using median instead of mean prevents high salary outliers from skewing missing values.
# - Time-Series Continuity: Using `ffill()`/`bfill()` maintains signal continuity in stock prices or sensor readings.


# ==============================================================================
# 3. Syntax
# ==============================================================================
# Detection:
#   df.isna()                             -> Boolean mask of missing values
#   df.notna()                            -> Boolean mask of valid values
#   df.isna().sum()                       -> Count of NaNs per column
#
# Dropping:
#   df_clean = df.dropna()                -> Drops rows with ANY missing value
#   df_clean = df.dropna(subset=["ID"])   -> Drops rows missing critical column 'ID'
#
# Filling (Imputation):
#   df["Age"] = df["Age"].fillna(df["Age"].mean())
#   df["Salary"] = df["Salary"].fillna(df["Salary"].median())
#   df["City"] = df["City"].fillna(df["City"].mode()[0])
#   df["Price"] = df["Price"].ffill()     -> Forward fill
#   df["Price"] = df["Price"].bfill()     -> Backward fill
#
# Coercing Messy Strings to Numeric:
#   df["Col"] = pd.to_numeric(df["Col"], errors="coerce")


# ==============================================================================
# 4. Example (Runnable)
# ==============================================================================
print("=" * 60)
print("SECTION 4: RUNNABLE EXAMPLES")
print("=" * 60)

# --- 1. Creating Messy DataFrame ---
data = {
    "Name": ["Arun", "Rahul", "Priya", "Karthik"],
    "Age": [21, None, 20, 23],
    "Salary": [35000, 42000, None, 38000],
    "City": ["Chennai", "Salem", None, "Chennai"]
}
df = pd.DataFrame(data)
print("Original Messy DataFrame:\n", df)

# --- 2. Counting Missing Data ---
print("\nMissing Values Count (df.isna().sum()):\n", df.isna().sum())

# --- 3. Filtering Missing Rows ---
missing_age_rows = df[df["Age"].isna()]
print("\nRows where Age is missing:\n", missing_age_rows)

# --- 4. Mean & Median & Mode Imputation ---
df_filled = df.copy()
df_filled["Age"] = df_filled["Age"].fillna(df_filled["Age"].median())
df_filled["Salary"] = df_filled["Salary"].fillna(df_filled["Salary"].mean())
df_filled["City"] = df_filled["City"].fillna(df_filled["City"].mode()[0])
print("\nFilled DataFrame (Median Age, Mean Salary, Mode City):\n", df_filled)

# --- 5. Forward & Backward Fill ---
ts_data = pd.Series([100, None, None, 150, None])
print("\nOriginal Time Series Series:\n", ts_data.values)
print("ffill():", ts_data.ffill().values)
print("bfill():", ts_data.bfill().values)


# ==============================================================================
# 5. Mini Practice (all mini practice for this topic) + Solutions
# ==============================================================================
print("\n" + "=" * 60)
print("SECTION 5: MINI PRACTICE")
print("=" * 60)

# Practice 1: Detect missing values in a sample DataFrame
prac_df = pd.DataFrame({"Score": [88, np.nan, 95], "Grade": ["A", None, "S"]})
print("Mini Practice 1 (isna sum):\n", prac_df.isna().sum())

# Practice 2: Median Imputation on skewed salary data
skewed_salary = pd.Series([30000, 32000, 35000, 1000000, np.nan])
median_val = skewed_salary.median()
filled_salary = skewed_salary.fillna(median_val)
print("\nMini Practice 2 (Median Imputation):")
print("  Median value:", median_val)
print("  Filled Series:\n", filled_salary.values)

# Practice 3: Coerce invalid strings "?" to NaN
messy_series = pd.Series(["10", "20", "N/A", "30", "?", "40"])
clean_numeric = pd.to_numeric(messy_series, errors="coerce")
print("\nMini Practice 3 (Coerce strings to numeric):\n", clean_numeric)
print("  NaN count:", clean_numeric.isna().sum())


# ==============================================================================
# 6. Assignments (Solutions Included)
# ==============================================================================
# Rule: No Google/AI. Use only Python docs, notes, and experiments.
print("\n" + "=" * 60)
print("SECTION 6: ASSIGNMENTS & EXERCISES")
print("=" * 60)

# ------------------------------------------------------------------------------
# Exercise 1 — Detecting & Counting Missing Data
# ------------------------------------------------------------------------------
ex1_data = {
    "Name": ["Arun", "Rahul", "Priya", "Karthik"],
    "Age": [21, None, 20, None],
    "Marks": [85, 90, None, 75]
}
ex1_df = pd.DataFrame(ex1_data)

print("\n[Exercise 1 — Detecting Missing Data]")
print("1. df.isna():\n", ex1_df.isna())
print("2. Missing counts (df.isna().sum()):\n", ex1_df.isna().sum())
print("3. Rows where Age is missing:\n", ex1_df[ex1_df["Age"].isna()])

# ------------------------------------------------------------------------------
# Exercise 2 — Dropping vs Imputing
# ------------------------------------------------------------------------------
print("\n[Exercise 2 — Dropping vs Imputing]")
print("1. Clean DataFrame (dropna):\n", ex1_df.dropna())

ex2_df = pd.DataFrame(ex1_data)
ex2_df["Age"] = ex2_df["Age"].fillna(ex2_df["Age"].median())
ex2_df["Marks"] = ex2_df["Marks"].fillna(ex2_df["Marks"].mean())
print("2. Filled DataFrame (Median Age, Mean Marks):\n", ex2_df)

# ------------------------------------------------------------------------------
# Exercise 3 — Mode Imputation
# ------------------------------------------------------------------------------
city_series = pd.Series(["Chennai", "Salem", None, "Chennai", None])
mode_city = city_series.mode()[0]
filled_city = city_series.fillna(mode_city)

print("\n[Exercise 3 — Mode Imputation]")
print("Original City Series:\n", city_series)
print("Mode value:", mode_city)
print("Filled City Series:\n", filled_city)

# ------------------------------------------------------------------------------
# Exercise 4 — ffill / bfill
# ------------------------------------------------------------------------------
sales_df = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Sales": [100, None, None, 150, None]
})

print("\n[Exercise 4 — ffill vs bfill]")
print("Original Sales:\n", sales_df)
print("ffill():\n", sales_df.assign(Sales=sales_df["Sales"].ffill()))
print("bfill():\n", sales_df.assign(Sales=sales_df["Sales"].bfill()))

# ------------------------------------------------------------------------------
# Exercise 5 — Messy Data Coercion
# ------------------------------------------------------------------------------
messy_df = pd.DataFrame({"Values": [10, 20, "N/A", 30, "?", 40]})
messy_df["Values"] = pd.to_numeric(messy_df["Values"], errors="coerce")

print("\n[Exercise 5 — Messy Data Coercion]")
print("Coerced DataFrame:\n", messy_df)
print("Missing values created:", messy_df["Values"].isna().sum())

# ------------------------------------------------------------------------------
# AI/Data Challenge — E-commerce Reasoning Strategy
# ------------------------------------------------------------------------------
print("\n[AI/Data Challenge — E-commerce Reasoning Strategy]")
strategy_summary = """
Column Strategy Matrix for 1-Million Row E-commerce Dataset:
--------------------------------------------------------------------------------
Column        Missing Strategy & Rationale
--------------------------------------------------------------------------------
customer_id : dropna(subset=["customer_id"]) -> Cannot associate transactions without user ID.
price       : median imputation by product category -> Skewed distribution, median fits category.
quantity    : fillna(1) or median -> Default to 1 minimum purchase if transaction occurred.
discount    : fillna(0.0) -> Missing discount implies full price paid (0% discount).
city        : fillna("Unknown") or Mode by Zip -> Categorical label, unknown retains sample count.
--------------------------------------------------------------------------------
"""
print(strategy_summary)
