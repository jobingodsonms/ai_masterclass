"""
Pandas Merge, Join & Concat - Topic File

Structure:
1. Concept (What it is)
2. Why AI engineers use it
3. Syntax
4. Example (runnable)
5. Mini Practice (all mini practice for this topic with solutions)
6. Assignments (solutions included + Mini Challenge)
"""

import pandas as pd
import numpy as np

# ==============================================================================
# 1. Concept (What it is)
# ==============================================================================
# Real-world data is rarely stored in a single table. It is spread across normalized relational tables.
# Pandas provides powerful functions to combine, join, and stack DataFrames:
#
# Key Operations:
# 1. pd.merge(left, right, on="key", how="type"):
#    Combines DataFrames based on matching values in common key columns.
#    - Inner Join (how="inner"): Default. Retains ONLY keys present in BOTH tables (intersection).
#    - Left Join (how="left"): Retains ALL rows from left table; fills missing right values with NaN.
#    - Right Join (how="right"): Retains ALL rows from right table; fills missing left values with NaN.
#    - Outer Join (how="outer"): Retains ALL rows from BOTH tables (full union).
# 2. Merging on Different Column Names:
#    pd.merge(df1, df2, left_on="Customer_ID", right_on="Buyer_ID")
# 3. Merging on Multiple Keys:
#    pd.merge(df1, df2, on=["Store", "Product"])
# 4. Handling Duplicate Column Names:
#    suffixes=("_cust", "_ord") renames overlapping non-key columns.
# 5. df.join():
#    Joins DataFrames based on index labels.
# 6. pd.concat([df1, df2]):
#    Stacks DataFrames vertically (axis=0, adding rows) or horizontally (axis=1, adding columns).
#
# Difference Matrix:
#   Operation | Main Idea
#   ----------------------------------------------------
#   merge()   | Combine based on matching keys/columns
#   join()    | Combine based on index labels
#   concat()  | Stack/attach DataFrames (vertically/horizontally)
#
# The E-Commerce Data Pipeline:
#   Raw Tables (Customers, Orders, Products)
#      ↓ pd.merge()
#   Master Joined DataFrame
#      ↓ Feature Engineering (Revenue = Price * Quantity)
#   df.groupby("Category")["Revenue"].sum()
#      ↓
#   Executive Summary Reports


# ==============================================================================
# 2. Why AI engineers use it
# ==============================================================================
# - Relational Data Integration: Joining SQL database extracts (users, transactions, products) into ML training tables.
# - Feature Augmentation: Enrichment of transaction datasets with user demographic or geographic metadata.
# - Batch Concatenation: Stacking monthly CSV logs or distributed sensor output files into one master dataset.
# - Preprocessing & Pipeline Construction: Constructing flat 2D feature matrices required for model training.


# ==============================================================================
# 3. Syntax
# ==============================================================================
# Basic Merge (Inner Join):
#   merged = pd.merge(df_left, df_right, on="KeyColumn")
#
# Specifying Join Type:
#   merged = pd.merge(df1, df2, on="Key", how="inner")   # Intersection
#   merged = pd.merge(df1, df2, on="Key", how="left")    # All Left
#   merged = pd.merge(df1, df2, on="Key", how="right")   # All Right
#   merged = pd.merge(df1, df2, on="Key", how="outer")   # Full Union
#
# Mismatched Column Names:
#   merged = pd.merge(df1, df2, left_on="Cust_ID", right_on="User_ID")
#
# Multiple Keys & Custom Suffixes:
#   merged = pd.merge(df1, df2, on=["Store", "Item"], suffixes=("_df1", "_df2"))
#
# Concatenation:
#   stacked_rows = pd.concat([df1, df2], axis=0, ignore_index=True)  # Vertical
#   side_cols    = pd.concat([df1, df2], axis=1)                    # Horizontal


# ==============================================================================
# 4. Example (Runnable)
# ==============================================================================
print("=" * 60)
print("SECTION 4: RUNNABLE EXAMPLES")
print("=" * 60)

# --- 1. Creating Sample Tables ---
customers = pd.DataFrame({
    "Customer_ID": [101, 102, 103],
    "Name": ["Arun", "Rahul", "Priya"]
})

orders = pd.DataFrame({
    "Order_ID": [1, 2, 3],
    "Customer_ID": [101, 102, 101],
    "Amount": [500, 800, 300]
})

print("Customers:\n", customers)
print("\nOrders:\n", orders)

# --- 2. Inner Merge ---
inner_merged = pd.merge(customers, orders, on="Customer_ID", how="inner")
print("\nInner Merge (customers & orders):\n", inner_merged)

# --- 3. Left vs Outer Merge with Missing Matches ---
orders_extra = pd.DataFrame({
    "Order_ID": [1, 2, 4],
    "Customer_ID": [101, 102, 104],
    "Amount": [500, 800, 900]
})

left_merged = pd.merge(customers, orders_extra, on="Customer_ID", how="left")
outer_merged = pd.merge(customers, orders_extra, on="Customer_ID", how="outer")
print("\nLeft Merge (keep all customers):\n", left_merged)
print("\nOuter Merge (keep all customers & orders):\n", outer_merged)

# --- 4. Vertical Concatenation (concat) ---
jan_sales = pd.DataFrame({"Name": ["Arun", "Rahul"], "Sales": [500, 700]})
feb_sales = pd.DataFrame({"Name": ["Priya", "Karthik"], "Sales": [600, 800]})
all_sales = pd.concat([jan_sales, feb_sales], axis=0, ignore_index=True)
print("\nVertical Concat (Jan + Feb):\n", all_sales)


# ==============================================================================
# 5. Mini Practice (all mini practice for this topic) + Solutions
# ==============================================================================
print("\n" + "=" * 60)
print("SECTION 5: MINI PRACTICE")
print("=" * 60)

# Practice 1: Merge on different column names
df_cust = pd.DataFrame({"Customer_ID": [101, 102], "Name": ["Arun", "Rahul"]})
df_ord = pd.DataFrame({"Buyer_ID": [101, 102], "Amount": [500, 800]})
merged_diff = pd.merge(df_cust, df_ord, left_on="Customer_ID", right_on="Buyer_ID")
print("Mini Practice 1 (left_on & right_on):\n", merged_diff)

# Practice 2: Horizontal concatenation (axis=1)
df_features = pd.DataFrame({"Age": [21, 22], "City": ["Chennai", "Salem"]})
df_scores = pd.DataFrame({"Score": [85, 92]})
horiz_concat = pd.concat([df_features, df_scores], axis=1)
print("\nMini Practice 2 (Horizontal Concat axis=1):\n", horiz_concat)

# Practice 3: Suffixes for overlapping columns
df1_meta = pd.DataFrame({"ID": [1, 2], "Name": ["ItemA", "ItemB"]})
df2_meta = pd.DataFrame({"ID": [1, 2], "Name": ["CatA", "CatB"]})
merged_suff = pd.merge(df1_meta, df2_meta, on="ID", suffixes=("_product", "_category"))
print("\nMini Practice 3 (Custom Suffixes):\n", merged_suff)


# ==============================================================================
# 6. Assignments (Solutions Included)
# ==============================================================================
# Rule: No Google/AI. Use only Python docs, notes, and experiments.
print("\n" + "=" * 60)
print("SECTION 6: ASSIGNMENTS & EXERCISES")
print("=" * 60)

# ------------------------------------------------------------------------------
# Exercise 1 — Inner Join
# ------------------------------------------------------------------------------
c_df = pd.DataFrame({"Customer_ID": [101, 102, 103], "Name": ["Arun", "Rahul", "Priya"]})
o_df = pd.DataFrame({"Order_ID": [1, 2, 3], "Customer_ID": [101, 102, 104], "Amount": [500, 800, 900]})

print("\n[Exercise 1 — Inner Join]")
print(pd.merge(c_df, o_df, on="Customer_ID", how="inner"))

# ------------------------------------------------------------------------------
# Exercise 2 — Compare Joins
# ------------------------------------------------------------------------------
print("\n[Exercise 2 — Compare Joins]")
print("Inner:\n", pd.merge(c_df, o_df, on="Customer_ID", how="inner"))
print("Left:\n", pd.merge(c_df, o_df, on="Customer_ID", how="left"))
print("Right:\n", pd.merge(c_df, o_df, on="Customer_ID", how="right"))
print("Outer:\n", pd.merge(c_df, o_df, on="Customer_ID", how="outer"))

# ------------------------------------------------------------------------------
# Exercise 3 — Different Column Names
# ------------------------------------------------------------------------------
c_diff = pd.DataFrame({"Customer_ID": [101, 102, 103], "Name": ["Arun", "Rahul", "Priya"]})
o_diff = pd.DataFrame({"Buyer_ID": [101, 102, 104], "Amount": [500, 800, 900]})

print("\n[Exercise 3 — Different Column Names]")
print(pd.merge(c_diff, o_diff, left_on="Customer_ID", right_on="Buyer_ID"))

# ------------------------------------------------------------------------------
# Exercise 4 — concat()
# ------------------------------------------------------------------------------
jan = pd.DataFrame({"Name": ["Arun", "Rahul"], "Sales": [500, 700]})
feb = pd.DataFrame({"Name": ["Priya", "Karthik"], "Sales": [600, 800]})

print("\n[Exercise 4 — Vertical Concat]")
print(pd.concat([jan, feb], axis=0, ignore_index=True))

# ------------------------------------------------------------------------------
# Exercise 5 — Three-Table Merge
# ------------------------------------------------------------------------------
customers_3t = pd.DataFrame({
    "Customer_ID": [101, 102, 103],
    "Name": ["Arun", "Rahul", "Priya"],
    "City": ["Chennai", "Salem", "Madurai"]
})
orders_3t = pd.DataFrame({
    "Order_ID": [1, 2, 3],
    "Customer_ID": [101, 102, 101],
    "Product_ID": ["P01", "P02", "P03"],
    "Quantity": [2, 1, 4]
})
products_3t = pd.DataFrame({
    "Product_ID": ["P01", "P02", "P03"],
    "Product": ["Laptop", "Shirt", "Mouse"],
    "Category": ["Electronics", "Clothing", "Electronics"],
    "Price": [1000, 500, 800]
})

merged_3t = pd.merge(orders_3t, customers_3t, on="Customer_ID")
final_3t = pd.merge(merged_3t, products_3t, on="Product_ID")

print("\n[Exercise 5 — Three-Table Merge]\n", final_3t)

# ------------------------------------------------------------------------------
# Mini Challenge
# ------------------------------------------------------------------------------
print("\n[Mini Challenge]")
final_3t["Revenue"] = final_3t["Quantity"] * final_3t["Price"]
category_revenue = final_3t.groupby("Category")["Revenue"].sum().sort_values(ascending=False)

print("Merged Master Data with Revenue:\n", final_3t[["Order_ID", "Name", "Category", "Quantity", "Price", "Revenue"]])
print("\nTotal Revenue by Category:\n", category_revenue)
