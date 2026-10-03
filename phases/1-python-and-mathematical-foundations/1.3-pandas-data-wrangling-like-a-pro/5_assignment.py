"""
MultiIndex in Pandas - Assignment Solution (pandas_multiindex.py)

Mental Model:
  MultiIndex (Hierarchical Indexing) provides multiple levels of organization:

  India/
      ├── Chennai     (Sales = 500)
      ├── Salem       (Sales = 300)
      └── Coimbatore  (Sales = 400)
  USA/
      ├── New York    (Sales = 700)
      └── Texas       (Sales = 600)

Key Operations:
  1. Create from columns : df.set_index(["Country", "City"])
  2. Select Level 1      : df.loc["India"]
  3. Select Specific Cell: df.loc[("India", "Salem")]
  4. Convert to Columns  : df.reset_index()
"""

import pandas as pd
import numpy as np

# ==============================================================================
# Task 1 — Create DataFrame Normally
# ==============================================================================
# Create:
#   Country       City          Sales
#   India         Chennai       500
#   India         Salem         300
#   India         Coimbatore    400
#   USA           New York      700
#   USA           Texas         600

print("--- Task 1: Create DataFrame Normally ---")
sales_data = {
    "Country": ["India", "India", "India", "USA", "USA"],
    "City": ["Chennai", "Salem", "Coimbatore", "New York", "Texas"],
    "Sales": [500, 300, 400, 700, 600]
}
df = pd.DataFrame(sales_data)
print("Normal DataFrame:\n", df)
print("Index:", df.index)
print()


# ==============================================================================
# Task 2 — set_index() to create MultiIndex
# ==============================================================================
# Make Country and City a MultiIndex using set_index().

print("--- Task 2: set_index(['Country', 'City']) ---")
multi_df = df.set_index(["Country", "City"])
print("MultiIndex DataFrame:\n", multi_df)
print("Index Type:", type(multi_df.index))
print()


# ==============================================================================
# Task 3 — Display India's Data
# ==============================================================================
# Select and display only India's data using .loc['India'].

print("--- Task 3: Display India's Data (df.loc['India']) ---")
india_df = multi_df.loc["India"]
print(india_df)
print()


# ==============================================================================
# Task 4 — Display Salem's Data
# ==============================================================================
# Select and display only Salem's data using tuple lookup .loc[('India', 'Salem')].

print("--- Task 4: Display Salem's Data (df.loc[('India', 'Salem')]) ---")
salem_data = multi_df.loc[("India", "Salem")]
print(salem_data)
print()


# ==============================================================================
# Task 5 — reset_index()
# ==============================================================================
# Convert the MultiIndex back to normal columns using reset_index().

print("--- Task 5: reset_index() ---")
reset_df = multi_df.reset_index()
print("Converted Back to Normal Columns:\n", reset_df)
print("Index:", reset_df.index)
