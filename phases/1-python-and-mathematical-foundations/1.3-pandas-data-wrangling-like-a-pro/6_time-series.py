"""
Pandas Time Series Analysis - Topic File

Structure:
1. Concept (What it is)
2. Why AI engineers use it
3. Syntax
4. Example (runnable)
5. Mini Practice (all mini practice for this topic with solutions)
6. Assignments (solutions included + Step 1 to 5 Final Challenge)
"""

import pandas as pd
import numpy as np

# ==============================================================================
# 1. Concept (What it is)
# ==============================================================================
# Time Series data consists of observations recorded sequentially over time.
# Pandas excels at time-series analysis through specialized `DatetimeIndex` structures,
# date parsing, slicing, and frequency resampling.
#
# Key Concepts:
# 1. Generating Dates (pd.date_range):
#    - pd.date_range(start="2026-01-01", end="2026-01-10")
#    - pd.date_range(start="2026-01-01", periods=10, freq="D")
# 2. Parsing Date Strings (pd.to_datetime):
#    Converts plain text strings into `datetime64[ns]` objects.
# 3. DatetimeIndex & Date Slicing:
#    Setting Date as the index enables label slicing like `df.loc["2026-01-03":"2026-01-06"]`.
# 4. Frequency Resampling (df.resample):
#    Changes time frequency (e.g. Daily -> Weekly, Monthly, Yearly).
#    Structure: df.resample("frequency").operation()
#
# Frequency Codes Table:
#   Code | Frequency Meaning
#   -------------------------------------
#   D    | Daily
#   W    | Weekly
#   ME   | Month End
#   QE   | Quarter End
#   YE   | Year End
#
# Common Resample Aggregations:
#   - df.resample("W").sum()    -> Weekly Total
#   - df.resample("ME").mean()  -> Monthly Average
#   - df.resample("W").max()    -> Weekly Maximum


# ==============================================================================
# 2. Why AI engineers use it
# ==============================================================================
# - Financial & Stock Forecasting: Resampling high-frequency tick data to daily/weekly OHLC candles.
# - Demand & Sales Forecasting: Aggregating daily transaction logs to weekly/monthly demand metrics for ARIMA / LSTM models.
# - IoT & Sensor Pipelines: Downsampling millisecond telemetry data to 1-minute anomaly detection windows.
# - Feature Engineering: Creating lag features, rolling window averages, and day-of-week / month indicators.


# ==============================================================================
# 3. Syntax
# ==============================================================================
# Date Generation & Conversion:
#   dates = pd.date_range(start="2026-01-01", periods=30, freq="D")
#   df["Date"] = pd.to_datetime(df["Date"])
#   df = df.set_index("Date")
#
# Date Slicing:
#   df.loc["2026-01-15"]                            -> Specific Date
#   df.loc["2026-01-01":"2026-01-10"]               -> Date Range
#   df.loc["2026-01"]                               -> Entire Month
#
# Resampling:
#   weekly_sum  = df.resample("W").sum()
#   monthly_avg = df.resample("ME").mean()
#   yearly_total = df.resample("YE").sum()
#
# Extreme Day Lookups:
#   highest_day = df["Sales"].idxmax()
#   lowest_day  = df["Sales"].idxmin()


# ==============================================================================
# 4. Example (Runnable)
# ==============================================================================
print("=" * 60)
print("SECTION 4: RUNNABLE EXAMPLES")
print("=" * 60)

# --- 1. Creating Time Series DataFrame ---
dates = pd.date_range(start="2026-01-01", periods=10, freq="D")
sales = [100, 120, 150, 130, 180, 200, 170, 220, 250, 300]
df = pd.DataFrame({"Sales": sales}, index=dates)

print("Daily Sales DataFrame:\n", df)

# --- 2. Date Slicing ---
print("\nSlicing Date Range (2026-01-03 to 2026-01-06):\n", df.loc["2026-01-03":"2026-01-06"])

# --- 3. Weekly & Monthly Resampling ---
weekly_total = df.resample("W").sum()
monthly_avg = df.resample("ME").mean()

print("\nWeekly Total Sales (df.resample('W').sum()):\n", weekly_total)
print("\nMonthly Average Sales (df.resample('ME').mean()):\n", monthly_avg)


# ==============================================================================
# 5. Mini Practice (all mini practice for this topic) + Solutions
# ==============================================================================
print("\n" + "=" * 60)
print("SECTION 5: MINI PRACTICE")
print("=" * 60)

# Practice 1: Convert string dates to datetime64 and set index
raw_df = pd.DataFrame({"DateStr": ["2026-02-01", "2026-02-02"], "Visitors": [500, 650]})
raw_df["Date"] = pd.to_datetime(raw_df["DateStr"])
ts_df = raw_df.set_index("Date").drop(columns=["DateStr"])
print("Mini Practice 1 (to_datetime & set_index):\n", ts_df)

# Practice 2: Resample 90-day daily dataset into weekly totals
np.random.seed(42)
days_90 = pd.date_range("2026-01-01", periods=90, freq="D")
df_90 = pd.DataFrame({"Sales": np.random.randint(100, 200, size=90)}, index=days_90)
weekly_90 = df_90.resample("W").sum()
print("\nMini Practice 2 (90-Day Weekly Totals - First 3 weeks):\n", weekly_90.head(3))

# Practice 3: Highest selling day identification
highest_date = df_90["Sales"].idxmax()
highest_value = df_90["Sales"].max()
print(f"\nMini Practice 3 (Highest Sales Day): {highest_date.strftime('%Y-%m-%d')} with {highest_value} sales.")


# ==============================================================================
# 6. Assignments (Solutions Included)
# ==============================================================================
# Rule: No Google/AI. Use only Python docs, notes, and experiments.
print("\n" + "=" * 60)
print("SECTION 6: ASSIGNMENTS & EXERCISES")
print("=" * 60)

# ------------------------------------------------------------------------------
# Steps 1-3 — Create 30-day Time Series DataFrame
# ------------------------------------------------------------------------------
dates_30 = pd.date_range(start="2026-01-01", periods=30, freq="D")
sales_30 = list(range(100, 400, 10))  # 30 sales values: 100, 110, 120, ..., 390
assign_df = pd.DataFrame({"Sales": sales_30}, index=dates_30)

print("\n[Steps 1-3 — 30-Day Time Series DataFrame]\n", assign_df.head(10))
print("... (showing first 10 of 30 days)")

# ------------------------------------------------------------------------------
# Step 4 — Resampling Calculations
# ------------------------------------------------------------------------------
weekly_total = assign_df.resample("W").sum()
monthly_total = assign_df.resample("ME").sum()
weekly_avg = assign_df.resample("W").mean()

print("\n[Step 4A — Weekly Total (df.resample('W').sum())]\n", weekly_total)
print("\n[Step 4B — Monthly Total (df.resample('ME').sum())]\n", monthly_total)
print("\n[Step 4C — Weekly Average (df.resample('W').mean())]\n", weekly_avg)

# ------------------------------------------------------------------------------
# Step 5 — Final Challenge
# ------------------------------------------------------------------------------
highest_day = assign_df["Sales"].idxmax()
highest_sales = assign_df["Sales"].max()

lowest_day = assign_df["Sales"].idxmin()
lowest_sales = assign_df["Sales"].min()

january_total = assign_df.loc["2026-01"]["Sales"].sum()
avg_weekly_sales = assign_df.resample("W")["Sales"].sum().mean()

print("\n[Step 5 — Final Challenge]")
print(f"1. Highest-selling day : {highest_day.strftime('%Y-%m-%d')} ({highest_sales} sales)")
print(f"2. Lowest-selling day  : {lowest_day.strftime('%Y-%m-%d')} ({lowest_sales} sales)")
print(f"3. Total sales for Jan : {january_total}")
print(f"4. Average weekly sales: {round(avg_weekly_sales, 2)}")
