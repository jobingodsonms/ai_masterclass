"""
Handling Missing Data - Assignment Solution (pandas_missing_data.py)

Mental Model:
  Operation      Purpose
  --------------------------------------------------
  isna()         Find missing values (True/False)
  notna()        Find existing values
  isna().sum()   Count missing values per column
  dropna()       Remove missing rows
  fillna()       Replace missing values
  ffill()        Fill using previous value (Forward Fill)
  bfill()        Fill using next value (Backward Fill)
  mean()         Average imputation (Symmetric numerical data)
  median()       Middle value imputation (Robust to outliers)
  mode()         Most frequent value imputation (Categorical text)
"""

import pandas as pd
import numpy as np

# ==============================================================================
# Exercise 1 — Detecting & Counting Missing Data
# ==============================================================================
# Create:
# data = {
#     "Name": ["Arun", "Rahul", "Priya", "Karthik"],
#     "Age": [21, None, 20, None],
#     "Marks": [85, 90, None, 75]
# }
# Tasks:
# 1. Find all missing values.
# 2. Count missing values in each column.
# 3. Display rows where Age is missing.

print("--- Exercise 1: Detecting & Counting Missing Data ---")
data1 = {
    "Name": ["Arun", "Rahul", "Priya", "Karthik"],
    "Age": [21, None, 20, None],
    "Marks": [85, 90, None, 75]
}
df1 = pd.DataFrame(data1)

print("Original DataFrame:\n", df1)
print("\n1. All Missing Values (df.isna()):\n", df1.isna())
print("\n2. Count of Missing Values (df.isna().sum()):\n", df1.isna().sum())

missing_age_df = df1[df1["Age"].isna()]
print("\n3. Rows where Age is missing:\n", missing_age_df)
print()


# ==============================================================================
# Exercise 2 — Dropping vs Imputing
# ==============================================================================
# Using the same DataFrame:
# 1. Remove rows containing missing values.
# 2. Create the original DataFrame again.
# 3. Fill missing Age using median.
# 4. Fill missing Marks using mean.

print("--- Exercise 2: Dropping vs Imputing ---")
clean_df = df1.dropna()
print("1. DataFrame after dropna():\n", clean_df)

# Re-create DataFrame for Imputation
df2 = pd.DataFrame(data1)
median_age = df2["Age"].median()
mean_marks = df2["Marks"].mean()

df2["Age"] = df2["Age"].fillna(median_age)
df2["Marks"] = df2["Marks"].fillna(mean_marks)

print("\nImputation Stats -> Median Age:", median_age, "| Mean Marks:", round(mean_marks, 2))
print("2-4. Filled DataFrame:\n", df2)
print()


# ==============================================================================
# Exercise 3 — Mode Imputation
# ==============================================================================
# Create: City = ["Chennai", "Salem", NaN, "Chennai", NaN]
# Fill missing cities using mode.

print("--- Exercise 3: Mode Imputation ---")
cities = pd.Series(["Chennai", "Salem", None, "Chennai", None])
print("Original City Series:\n", cities)

mode_city = cities.mode()[0]
filled_cities = cities.fillna(mode_city)

print("\nCalculated Mode:", mode_city)
print("Filled City Series:\n", filled_cities)
print()


# ==============================================================================
# Exercise 4 — ffill / bfill
# ==============================================================================
# Create:
# Day       Sales
# Mon       100
# Tue       NaN
# Wed       NaN
# Thu       150
# Fri       NaN
# Try ffill() and bfill(), compare results.

print("--- Exercise 4: ffill vs bfill ---")
sales_data = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Sales": [100, None, None, 150, None]
})

print("Original Sales Data:\n", sales_data)

ffill_df = sales_data.copy()
ffill_df["Sales"] = ffill_df["Sales"].ffill()

bfill_df = sales_data.copy()
bfill_df["Sales"] = bfill_df["Sales"].bfill()

print("\nForward Fill (ffill):\n", ffill_df)
print("\nBackward Fill (bfill):\n", bfill_df)

print("\nComparison Insights:")
print("- ffill() carries Mon's 100 to Tue/Wed and Thu's 150 to Fri.")
print("- bfill() pulls Thu's 150 backward to Tue/Wed, leaving Fri as NaN (no next value exists).")
print()


# ==============================================================================
# Exercise 5 — Messy Data Coercion
# ==============================================================================
# Create DataFrame with numeric column containing [10, 20, "N/A", 30, "?", 40].
# Convert using pd.to_numeric(..., errors="coerce").
# Count how many missing values were created.

print("--- Exercise 5: Messy Data Coercion ---")
messy_df = pd.DataFrame({
    "Raw_Values": [10, 20, "N/A", 30, "?", 40]
})

print("Raw Messy DataFrame:\n", messy_df)

messy_df["Clean_Values"] = pd.to_numeric(messy_df["Raw_Values"], errors="coerce")
missing_count = messy_df["Clean_Values"].isna().sum()

print("\nCleaned DataFrame:\n", messy_df)
print("Missing values (NaN) created from string placeholders:", missing_count)
print()


# ==============================================================================
# 🤖 AI/Data Challenge — E-commerce Reasoning Strategy
# ==============================================================================
# For each column in an e-commerce dataset (customer_id, price, quantity, discount, city),
# decide what strategy you would use if values are missing.

print("--- 🤖 AI/Data Challenge: E-commerce Reasoning Strategy ---")
ecommerce_strategy = """
E-Commerce Missing Value Strategy Breakdown:

1. customer_id:
   - Strategy: dropna(subset=["customer_id"])
   - Reason  : A transaction without a valid customer ID cannot be attributed to a user session or user profile.
               Filling it with dummy IDs would corrupt user analytics and recommendations.

2. price:
   - Strategy: Median Imputation grouped by Product Category.
   - Reason  : Price is a continuous numerical variable prone to high-value outliers (e.g., luxury electronics).
               Using median prices within the same product category avoids distorting item value.

3. quantity:
   - Strategy: fillna(1)
   - Reason  : In e-commerce transaction logs, if a purchase row exists, at least 1 unit was bought.
               Defaulting missing quantity to 1 is domain-logical.

4. discount:
   - Strategy: fillna(0.0)
   - Reason  : Missing discount values indicate no discount coupon was applied.
               Filling with 0.0 reflects full retail price payment.

5. city:
   - Strategy: fillna("Unknown") or Mode by Zip/State
   - Reason  : City is a categorical text variable. Filling with "Unknown" keeps row counts intact without
               falsifying demographic reports.
"""
print(ecommerce_strategy)
