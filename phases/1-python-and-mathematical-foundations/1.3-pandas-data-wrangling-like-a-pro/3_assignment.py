"""
groupby() in Pandas - Assignment Solution (pandas_groupby.py)

Mental Model:
             DATASET
                ↓
             GROUP BY (Split)
                ↓
       ┌────────┴────────┐
       ↓                 ↓
      CSE                ECE
       ↓                 ↓
   40k,45k,50k       35k,38k (Apply)
       ↓                 ↓
    average            average
       ↓                 ↓
    45,000             36,500 (Combine)

The GroupBy Formula:
  Calculate X for every Y  -->  df.groupby("Y")["X"].aggregation()
"""

import pandas as pd
import numpy as np

# ==============================================================================
# Exercise 1 — Basic GroupBy
# ==============================================================================
# Create:
#   Name      Department    Salary
#   Arun      CSE           40000
#   Rahul     CSE           45000
#   Priya     ECE           35000
#   Karthik   ECE           38000
#   Vijay     CSE           50000
# Find:
# 1. Average salary per department
# 2. Total salary per department
# 3. Minimum salary per department
# 4. Maximum salary per department
# 5. Number of employees per department

print("--- Exercise 1: Basic GroupBy ---")
emp_df = pd.DataFrame({
    "Name": ["Arun", "Rahul", "Priya", "Karthik", "Vijay"],
    "Department": ["CSE", "CSE", "ECE", "ECE", "CSE"],
    "Salary": [40000, 45000, 35000, 38000, 50000]
})

print("Original Employee Dataset:\n", emp_df)
print("\n1. Average Salary per Department:\n", emp_df.groupby("Department")["Salary"].mean())
print("\n2. Total Salary per Department:\n", emp_df.groupby("Department")["Salary"].sum())
print("\n3. Minimum Salary per Department:\n", emp_df.groupby("Department")["Salary"].min())
print("\n4. Maximum Salary per Department:\n", emp_df.groupby("Department")["Salary"].max())
print("\n5. Number of Employees per Department:\n", emp_df.groupby("Department")["Salary"].count())
print()


# ==============================================================================
# Exercise 2 — Multiple Aggregations
# ==============================================================================
# Create a summary containing mean, min, max, count for Salary by Department.

print("--- Exercise 2: Multiple Aggregations ---")
salary_summary = emp_df.groupby("Department")["Salary"].agg(["mean", "min", "max", "count"])
print(salary_summary)
print()


# ==============================================================================
# Exercise 3 — Multiple Grouping
# ==============================================================================
# Create:
#   City       Category       Sales
#   Chennai    Electronics    50000
#   Chennai    Clothing       20000
#   Salem      Electronics    30000
#   Salem      Clothing       15000
#   Chennai    Electronics    25000
# Find total sales for each City + Category.

print("--- Exercise 3: Multiple Grouping ---")
sales_df = pd.DataFrame({
    "City": ["Chennai", "Chennai", "Salem", "Salem", "Chennai"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics"],
    "Sales": [50000, 20000, 30000, 15000, 25000]
})

city_cat_sales = sales_df.groupby(["City", "Category"])["Sales"].sum()
print("Total Sales by City & Category:\n", city_cat_sales)
print()


# ==============================================================================
# Exercise 4 — Sorting GroupBy Results
# ==============================================================================
# Find the average salary per department and sort it from highest to lowest.

print("--- Exercise 4: Sorting GroupBy Results ---")
sorted_avg_salary = emp_df.groupby("Department")["Salary"].mean().sort_values(ascending=False)
print("Average Salary (Highest to Lowest):\n", sorted_avg_salary)
print()


# ==============================================================================
# Exercise 5 — reset_index()
# ==============================================================================
# Convert the group index back into a normal column using reset_index().

print("--- Exercise 5: reset_index() ---")
reset_summary = emp_df.groupby("Department")["Salary"].mean().reset_index()
print(reset_summary)
print()


# ==============================================================================
# Exercise 6 — transform()
# ==============================================================================
# Create Dept_Avg_Salary where every employee's row contains their department's average salary.

print("--- Exercise 6: transform() ---")
transformed_df = emp_df.copy()
transformed_df["Dept_Avg_Salary"] = transformed_df.groupby("Department")["Salary"].transform("mean")
print(transformed_df)
print()


# ==============================================================================
# Mini E-Commerce Challenge
# ==============================================================================
# Dataset:
#   Category       Price    Quantity
#   Electronics    1000     2
#   Clothing       500      4
#   Electronics    2000     1
#   Clothing       800      3
#   Furniture      5000     2
# Create: Revenue = Price * Quantity
# Calculate:
# 1. Total revenue by category
# 2. Average revenue by category
# 3. Total quantity sold by category
# 4. Sort categories by total revenue (highest to lowest)

print("--- Mini E-Commerce Challenge ---")
ecom_df = pd.DataFrame({
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Furniture"],
    "Price": [1000, 500, 2000, 800, 5000],
    "Quantity": [2, 4, 1, 3, 2]
})

# Feature Engineering: Revenue
ecom_df["Revenue"] = ecom_df["Price"] * ecom_df["Quantity"]

print("E-Commerce Dataset with Revenue:\n", ecom_df)

total_rev = ecom_df.groupby("Category")["Revenue"].sum()
avg_rev = ecom_df.groupby("Category")["Revenue"].mean()
total_qty = ecom_df.groupby("Category")["Quantity"].sum()
sorted_categories = ecom_df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)

print("\n1. Total Revenue by Category:\n", total_rev)
print("\n2. Average Revenue by Category:\n", avg_rev)
print("\n3. Total Quantity Sold by Category:\n", total_qty)
print("\n4. Categories Sorted by Total Revenue (Highest to Lowest):\n", sorted_categories)
