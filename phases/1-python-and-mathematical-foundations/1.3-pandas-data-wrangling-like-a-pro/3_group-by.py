"""
Pandas GroupBy & Aggregations - Topic File

Structure:
1. Concept (What it is)
2. Why AI engineers use it
3. Syntax
4. Example (runnable)
5. Mini Practice (all mini practice for this topic with solutions)
6. Assignments (solutions included + Mini E-Commerce Challenge)
"""

import pandas as pd
import numpy as np

# ==============================================================================
# 1. Concept (What it is)
# ==============================================================================
# `groupby()` is one of Pandas' most powerful features for data analysis and reporting.
# It implements the classic Split-Apply-Combine paradigm:
#   1. Split: Group rows based on matching values in one or more key columns.
#   2. Apply: Compute an aggregation function (mean, sum, count, min, max, std) on each group.
#   3. Combine: Merge the group summary results into a clean Series or DataFrame.
#
# Key Concepts:
# 1. GroupBy Object:
#    df.groupby("Department") returns a Lazy GroupBy object waiting for an aggregation method.
# 2. Aggregations (sum, mean, count, min, max):
#    - df.groupby("Dept")["Salary"].mean()
#    - df.groupby("Dept")["Salary"].sum()
# 3. Multiple Aggregations (.agg()):
#    df.groupby("Dept")["Salary"].agg(["mean", "min", "max", "count"])
# 4. Multi-Column Grouping:
#    df.groupby(["City", "Category"])["Sales"].sum()
# 5. size() vs count():
#    - count(): Counts non-missing (non-NaN) values per group.
#    - size(): Counts total row count per group (including NaNs).
# 6. Flattening Index with reset_index():
#    Resets group index labels back into standard DataFrame columns.
# 7. Feature Engineering with transform():
#    Broadcasts group-level statistics back to EVERY original row (retaining original shape).
#
# Mental Map:
#              DATASET
#                 ↓
#              GROUP BY (Split)
#                 ↓
#        ┌────────┴────────┐
#        ↓                 ↓
#       CSE                ECE
#        ↓                 ↓
#    40k,45k,50k       35k,38k (Apply)
#        ↓                 ↓
#     average            average
#        ↓                 ↓
#     45,000             36,500 (Combine)
#
# The GroupBy Formula:
#   Calculate X for every Y  -->  df.groupby("Y")["X"].aggregation()


# ==============================================================================
# 2. Why AI engineers use it
# ==============================================================================
# - Executive Reporting & Dashboards: Creating high-level summary tables for business metrics.
# - Feature Engineering for ML Models: Generating group-level features (e.g. mean user spending, category average price).
# - Data Exploration (EDA): Analyzing feature distribution across different target classes or demographics.
# - Cohort Analysis: Grouping users by signup date/month to track retention and lifetime value.


# ==============================================================================
# 3. Syntax
# ==============================================================================
# Basic Aggregations:
#   df.groupby("Category")["Sales"].mean()
#   df.groupby("Category")["Sales"].sum()
#   df.groupby("Category")["Sales"].count()
#   df.groupby("Category")["Sales"].min()
#   df.groupby("Category")["Sales"].max()
#
# Multiple Aggregations (.agg()):
#   df.groupby("Category")["Sales"].agg(["mean", "min", "max", "count"])
#
# Per-Column Aggregations:
#   df.groupby("Category").agg({"Sales": "sum", "Discount": "mean"})
#
# Multi-Column Grouping:
#   df.groupby(["City", "Category"])["Sales"].sum()
#
# Resetting Index:
#   summary_df = df.groupby("Category")["Sales"].mean().reset_index()
#
# Feature Engineering (transform):
#   df["Cat_Avg_Sales"] = df.groupby("Category")["Sales"].transform("mean")


# ==============================================================================
# 4. Example (Runnable)
# ==============================================================================
print("=" * 60)
print("SECTION 4: RUNNABLE EXAMPLES")
print("=" * 60)

# --- 1. Basic GroupBy ---
emp_data = {
    "Name": ["Arun", "Rahul", "Priya", "Karthik", "Vijay"],
    "Department": ["CSE", "CSE", "ECE", "ECE", "CSE"],
    "Salary": [40000, 45000, 35000, 38000, 50000]
}
df = pd.DataFrame(emp_data)
print("Original Employee DataFrame:\n", df)

avg_salary = df.groupby("Department")["Salary"].mean()
print("\nAverage Salary per Department:\n", avg_salary)

# --- 2. Multiple Aggregations ---
multi_agg = df.groupby("Department")["Salary"].agg(["mean", "min", "max", "count"])
print("\nDepartment Salary Summary (.agg):\n", multi_agg)

# --- 3. GroupBy with reset_index() ---
summary_reset = df.groupby("Department")["Salary"].mean().reset_index()
print("\nSummary with reset_index():\n", summary_reset)

# --- 4. Feature Engineering with transform() ---
df["Dept_Avg_Salary"] = df.groupby("Department")["Salary"].transform("mean")
print("\nDataFrame with Dept_Avg_Salary Column:\n", df)


# ==============================================================================
# 5. Mini Practice (all mini practice for this topic) + Solutions
# ==============================================================================
print("\n" + "=" * 60)
print("SECTION 5: MINI PRACTICE")
print("=" * 60)

# Practice 1: Total salary per department
total_sal = df.groupby("Department")["Salary"].sum()
print("Mini Practice 1 (Total Salary per Dept):\n", total_sal)

# Practice 2: Multi-column GroupBy (City + Category)
sales_data = pd.DataFrame({
    "City": ["Chennai", "Chennai", "Salem", "Salem", "Chennai"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics"],
    "Sales": [50000, 20000, 30000, 15000, 25000]
})
city_cat_sales = sales_data.groupby(["City", "Category"])["Sales"].sum()
print("\nMini Practice 2 (Sales by City & Category):\n", city_cat_sales)

# Practice 3: Sorted average salary per department
sorted_avg = df.groupby("Department")["Salary"].mean().sort_values(ascending=False)
print("\nMini Practice 3 (Sorted Avg Salary Descending):\n", sorted_avg)


# ==============================================================================
# 6. Assignments (Solutions Included)
# ==============================================================================
# Rule: No Google/AI. Use only Python docs, notes, and experiments.
print("\n" + "=" * 60)
print("SECTION 6: ASSIGNMENTS & EXERCISES")
print("=" * 60)

# ------------------------------------------------------------------------------
# Exercise 1 — Basic GroupBy
# ------------------------------------------------------------------------------
print("\n[Exercise 1 — Basic GroupBy]")
print("Average Salary :\n", df.groupby("Department")["Salary"].mean())
print("Total Salary   :\n", df.groupby("Department")["Salary"].sum())
print("Minimum Salary :\n", df.groupby("Department")["Salary"].min())
print("Maximum Salary :\n", df.groupby("Department")["Salary"].max())
print("Employee Count :\n", df.groupby("Department")["Salary"].count())

# ------------------------------------------------------------------------------
# Exercise 2 — Multiple Aggregations
# ------------------------------------------------------------------------------
print("\n[Exercise 2 — Multiple Aggregations]")
print(df.groupby("Department")["Salary"].agg(["mean", "min", "max", "count"]))

# ------------------------------------------------------------------------------
# Exercise 3 — Multiple Grouping
# ------------------------------------------------------------------------------
print("\n[Exercise 3 — Multiple Grouping]")
print(sales_data.groupby(["City", "Category"])["Sales"].sum())

# ------------------------------------------------------------------------------
# Exercise 4 — Sorting GroupBy Results
# ------------------------------------------------------------------------------
print("\n[Exercise 4 — Sorting GroupBy Results]")
sorted_dept = df.groupby("Department")["Salary"].mean().sort_values(ascending=False)
print(sorted_dept)

# ------------------------------------------------------------------------------
# Exercise 5 — reset_index()
# ------------------------------------------------------------------------------
print("\n[Exercise 5 — reset_index()]")
reset_df = df.groupby("Department")["Salary"].mean().reset_index()
print(reset_df)

# ------------------------------------------------------------------------------
# Exercise 6 — transform()
# ------------------------------------------------------------------------------
print("\n[Exercise 6 — transform()]")
ex6_df = df.copy()
ex6_df["Dept_Avg_Salary"] = ex6_df.groupby("Department")["Salary"].transform("mean")
print(ex6_df)

# ------------------------------------------------------------------------------
# Mini E-Commerce Challenge
# ------------------------------------------------------------------------------
print("\n[Mini E-Commerce Challenge]")
ecom_df = pd.DataFrame({
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Furniture"],
    "Price": [1000, 500, 2000, 800, 5000],
    "Quantity": [2, 4, 1, 3, 2]
})

# Feature engineering: Revenue
ecom_df["Revenue"] = ecom_df["Price"] * ecom_df["Quantity"]

print("Processed E-Commerce DataFrame:\n", ecom_df)

total_rev = ecom_df.groupby("Category")["Revenue"].sum()
avg_rev = ecom_df.groupby("Category")["Revenue"].mean()
total_qty = ecom_df.groupby("Category")["Quantity"].sum()
sorted_rev = ecom_df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)

print("\n1. Total Revenue by Category:\n", total_rev)
print("\n2. Average Revenue by Category:\n", avg_rev)
print("\n3. Total Quantity Sold by Category:\n", total_qty)
print("\n4. Categories Sorted by Total Revenue (Highest to Lowest):\n", sorted_rev)
