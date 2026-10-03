"""
Merge & Join in Pandas - Assignment Solution (pandas_merge_join.py)

Mental Model:
  Operation   Main Idea
  --------------------------------------------------
  merge()     Combine based on matching keys/columns
  join()      Combine based on index labels
  concat()    Stack/attach DataFrames (vertically/horizontally)

  Join Types (how):
  - inner : Intersection of keys (only matching rows in BOTH tables)
  - left  : Everything from left table + matching right rows (NaN if no match)
  - right : Everything from right table + matching left rows (NaN if no match)
  - outer : Full union of keys (all rows from BOTH tables)
"""

import pandas as pd
import numpy as np

# ==============================================================================
# Exercise 1 — Inner Join
# ==============================================================================
# Create:
# Customers: Customer_ID (101, 102, 103), Name (Arun, Rahul, Priya)
# Orders: Order_ID (1, 2, 3), Customer_ID (101, 102, 104), Amount (500, 800, 900)
# Perform an inner merge. Observe which customers remain.

print("--- Exercise 1: Inner Join ---")
customers_ex1 = pd.DataFrame({
    "Customer_ID": [101, 102, 103],
    "Name": ["Arun", "Rahul", "Priya"]
})
orders_ex1 = pd.DataFrame({
    "Order_ID": [1, 2, 3],
    "Customer_ID": [101, 102, 104],
    "Amount": [500, 800, 900]
})

print("Customers Table:\n", customers_ex1)
print("\nOrders Table:\n", orders_ex1)

inner_result = pd.merge(customers_ex1, orders_ex1, on="Customer_ID", how="inner")
print("\nInner Merge Result (only Customer_IDs 101 & 102 remain):\n", inner_result)
print()


# ==============================================================================
# Exercise 2 — Compare Joins
# ==============================================================================
# Perform how="inner", how="left", how="right", how="outer" on the same DataFrames.

print("--- Exercise 2: Compare Joins ---")
left_result = pd.merge(customers_ex1, orders_ex1, on="Customer_ID", how="left")
right_result = pd.merge(customers_ex1, orders_ex1, on="Customer_ID", how="right")
outer_result = pd.merge(customers_ex1, orders_ex1, on="Customer_ID", how="outer")

print("1. Inner Join (Intersection):\n", inner_result)
print("\n2. Left Join (All Customers, Priya gets NaN Amount):\n", left_result)
print("\n3. Right Join (All Orders, Order 3 gets NaN Name):\n", right_result)
print("\n4. Outer Join (Full Union of both tables):\n", outer_result)
print()


# ==============================================================================
# Exercise 3 — Different Column Names
# ==============================================================================
# Create:
# customers: Customer_ID, Name
# orders: Buyer_ID, Amount
# Merge using left_on and right_on.

print("--- Exercise 3: Different Column Names ---" )
cust_diff = pd.DataFrame({"Customer_ID": [101, 102, 103], "Name": ["Arun", "Rahul", "Priya"]})
ord_diff = pd.DataFrame({"Buyer_ID": [101, 102, 104], "Amount": [500, 800, 900]})

diff_merged = pd.merge(cust_diff, ord_diff, left_on="Customer_ID", right_on="Buyer_ID", how="inner")
print(diff_merged)
print()


# ==============================================================================
# Exercise 4 — concat()
# ==============================================================================
# Create:
# January: Name (Arun, Rahul), Sales (500, 700)
# February: Name (Priya, Karthik), Sales (600, 800)
# Use concat() to combine them vertically.

print("--- Exercise 4: Vertical Concatenation (concat) ---")
january = pd.DataFrame({"Name": ["Arun", "Rahul"], "Sales": [500, 700]})
february = pd.DataFrame({"Name": ["Priya", "Karthik"], "Sales": [600, 800]})

stacked_sales = pd.concat([january, february], axis=0, ignore_index=True)
print("Vertically Stacked Sales (Jan + Feb):\n", stacked_sales)
print()


# ==============================================================================
# Exercise 5 — Three-Table Merge
# ==============================================================================
# Create:
# customers: Customer_ID, Name, City
# orders: Order_ID, Customer_ID, Product_ID, Quantity
# products: Product_ID, Product, Category, Price
# Merge all three into one master DataFrame.

print("--- Exercise 5: Three-Table Merge ---")
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

# First merge orders with customers
orders_customers = pd.merge(orders_3t, customers_3t, on="Customer_ID", how="inner")

# Second merge with products
master_df = pd.merge(orders_customers, products_3t, on="Product_ID", how="inner")
print("Master Merged DataFrame (3 Tables):\n", master_df)
print()


# ==============================================================================
# Mini Challenge
# ==============================================================================
# Using the merged master DataFrame:
# 1. Create: Revenue = Quantity * Price
# 2. Use groupby() to calculate Total revenue by Category.

print("--- Mini Challenge ---")
master_df["Revenue"] = master_df["Quantity"] * master_df["Price"]

print("Master DataFrame with Revenue Feature:\n", master_df[["Order_ID", "Name", "City", "Product", "Category", "Quantity", "Price", "Revenue"]])

category_revenue = master_df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)
print("\nTotal Revenue by Category:\n", category_revenue)
