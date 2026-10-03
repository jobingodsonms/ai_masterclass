"""
Time Series in Pandas - Assignment Solution (pandas_time_series.py)

Mental Model:
  Time Series Analysis in Pandas revolves around DatetimeIndex and Resampling.

  Frequency Codes:
  - D  : Daily
  - W  : Weekly
  - ME : Month End
  - QE : Quarter End
  - YE : Year End

  Resampling Formula:
    df.resample("frequency").operation()
"""

import pandas as pd
import numpy as np

# ==============================================================================
# Step 1 — Create 30 Dates
# ==============================================================================
# Generate 30 daily dates starting from 2026-01-01.

print("--- Step 1: Create 30 Dates ---")
dates = pd.date_range(start="2026-01-01", periods=30, freq="D")
print("Generated Date Range (First 5):", dates[:5])
print("Total dates generated:", len(dates))
print()


# ==============================================================================
# Step 2 — Create Sales Data
# ==============================================================================
# Generate 30 sales values starting from 100 with step of 10: 100, 110, 120, ..., 390.

print("--- Step 2: Create Sales Data ---")
sales = list(range(100, 400, 10))
print("Generated Sales Data (First 5):", sales[:5])
print("Total sales entries:", len(sales))
print()


# ==============================================================================
# Step 3 — Create Time Series DataFrame
# ==============================================================================
# Create DataFrame with Sales indexed by dates.

print("--- Step 3: Create Time Series DataFrame ---")
df = pd.DataFrame({"Sales": sales}, index=dates)
print("Time Series DataFrame (Head 5):\n", df.head())
print("Index Type:", type(df.index))
print()


# ==============================================================================
# Step 4 — Resampling Calculations
# ==============================================================================
# A. Weekly total: df.resample("W").sum()
# B. Monthly total: df.resample("ME").sum()
# C. Weekly average: df.resample("W").mean()

print("--- Step 4: Resampling Calculations ---")

weekly_total = df.resample("W").sum()
monthly_total = df.resample("ME").sum()
weekly_avg = df.resample("W").mean()

print("A. Weekly Total Sales (df.resample('W').sum()):\n", weekly_total)
print("\nB. Monthly Total Sales (df.resample('ME').sum()):\n", monthly_total)
print("\nC. Weekly Average Sales (df.resample('W').mean()):\n", weekly_avg)
print()


# ==============================================================================
# Step 5 — Final Challenge
# ==============================================================================
# Find:
# 1. Highest-selling day
# 2. Lowest-selling day
# 3. Total sales for January
# 4. Average weekly sales

print("--- Step 5: Final Challenge ---")

highest_date = df["Sales"].idxmax()
highest_amount = df["Sales"].max()

lowest_date = df["Sales"].idxmin()
lowest_amount = df["Sales"].min()

january_total_sales = df.loc["2026-01"]["Sales"].sum()
avg_weekly_sales_total = df.resample("W")["Sales"].sum().mean()

print(f"1. Highest-selling day : {highest_date.strftime('%Y-%m-%d')} with {highest_amount} sales")
print(f"2. Lowest-selling day  : {lowest_date.strftime('%Y-%m-%d')} with {lowest_amount} sales")
print(f"3. Total sales for Jan : {january_total_sales}")
print(f"4. Average weekly sales: {round(avg_weekly_sales_total, 2)}")
