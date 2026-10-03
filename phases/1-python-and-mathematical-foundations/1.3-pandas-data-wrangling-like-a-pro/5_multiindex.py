"""
Pandas MultiIndex (Hierarchical Indexing) - Topic File

Structure:
1. Concept (What it is)
2. Why AI engineers use it
3. Syntax
4. Example (runnable)
5. Mini Practice (all mini practice for this topic with solutions)
6. Assignments (solutions included + 5 Part E Tasks)
"""

import pandas as pd
import numpy as np

# ==============================================================================
# 1. Concept (What it is)
# ==============================================================================
# MultiIndex (Hierarchical Indexing) allows a DataFrame to have multiple levels of indexing
# along a single axis (rows or columns).
# It provides a structured, multi-dimensional way of representing complex data in a 2D format.
#
# Key Concepts:
# 1. Hierarchical Levels:
#    Level 1 -> Country (e.g. India, USA)
#    Level 2 -> City (e.g. Chennai, Salem, New York)
# 2. Folder Mental Model:
#    India/
#       ├── Chennai  (Sales: 100)
#       └── Salem    (Sales: 150)
#    USA/
#       └── Texas    (Sales: 250)
# 3. Creating MultiIndex:
#    - pd.MultiIndex.from_tuples([("India", "Chennai"), ...], names=["Country", "City"])
#    - df.set_index(["Country", "City"]): Converts standard columns into a MultiIndex.
# 4. Selecting Data:
#    - df.loc["India"]: Selects all rows under Level 1 key "India".
#    - df.loc[("India", "Salem")]: Selects exact row using a tuple key.
#    - df.loc[[("India", "Chennai"), ("USA", "Texas")]]: Selects multiple tuple pairs.
# 5. Resetting Index:
#    df.reset_index(): Converts MultiIndex levels back into standard DataFrame columns.
#
# Summary Table:
#   Concept                      | Code Syntax
#   -------------------------------------------------------------------------
#   Create MultiIndex from tuple | pd.MultiIndex.from_tuples(...)
#   Create from columns          | df.set_index(["Col1", "Col2"])
#   Select first level           | df.loc["Level1_Key"]
#   Select specific combination  | df.loc[("Level1_Key", "Level2_Key")]
#   Remove MultiIndex            | df.reset_index()


# ==============================================================================
# 2. Why AI engineers use it
# ==============================================================================
# - Multi-Level Aggregations: Output of complex groupbys and pivot tables naturally generate MultiIndex structures.
# - Hierarchical Time-Series Data: Indexing multi-region or multi-store sensor/sales data (e.g., [Year, Month, Store_ID]).
# - Slice & Dice High-Dimensional Features: Quick slicing of multi-factor features without dropping indexing context.


# ==============================================================================
# 3. Syntax
# ==============================================================================
# From Tuples:
#   idx = pd.MultiIndex.from_tuples([("India", "Chennai"), ("USA", "Texas")], names=["Country", "City"])
#   df = pd.DataFrame({"Sales": [100, 250]}, index=idx)
#
# From DataFrame Columns:
#   df_multi = df.set_index(["Country", "City"])
#
# Selection:
#   df_multi.loc["India"]                          -> Selects all rows for India
#   df_multi.loc[("India", "Salem")]               -> Selects exact cell/row for India, Salem
#   df_multi.loc[[("India", "Chennai"), ("USA", "Texas")]]
#
# Resetting Index:
#   df_flat = df_multi.reset_index()


# ==============================================================================
# 4. Example (Runnable)
# ==============================================================================
print("=" * 60)
print("SECTION 4: RUNNABLE EXAMPLES")
print("=" * 60)

# --- 1. Creating MultiIndex via set_index() ---
data = {
    "Country": ["India", "India", "India", "USA", "USA"],
    "City": ["Chennai", "Salem", "Coimbatore", "New York", "Texas"],
    "Sales": [100, 150, 200, 300, 250]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

df_multi = df.set_index(["Country", "City"])
print("\nMultiIndex DataFrame (set_index):\n", df_multi)

# --- 2. Selecting Data ---
print("\nSelecting Level 1 ('India'):\n", df_multi.loc["India"])
print("\nSelecting Specific Tuple ('India', 'Salem'):\n", df_multi.loc[("India", "Salem")])

# --- 3. Resetting Index ---
df_reset = df_multi.reset_index()
print("\nResetting MultiIndex back to normal columns:\n", df_reset)


# ==============================================================================
# 5. Mini Practice (all mini practice for this topic) + Solutions
# ==============================================================================
print("\n" + "=" * 60)
print("SECTION 5: MINI PRACTICE")
print("=" * 60)

# Practice 1: MultiIndex from tuples
idx_tuples = pd.MultiIndex.from_tuples([("DeptA", "E01"), ("DeptA", "E02"), ("DeptB", "E03")], names=["Dept", "EmpID"])
df_tuples = pd.DataFrame({"Score": [90, 85, 95]}, index=idx_tuples)
print("Mini Practice 1 (from_tuples):\n", df_tuples)

# Practice 2: Select Level 1 DeptA
print("\nMini Practice 2 (Select DeptA):\n", df_tuples.loc["DeptA"])

# Practice 3: Select tuple ("DeptB", "E03")
print("\nMini Practice 3 (Select DeptB, E03):\n", df_tuples.loc[("DeptB", "E03")])


# ==============================================================================
# 6. Assignments (Solutions Included)
# ==============================================================================
# Rule: No Google/AI. Use only Python docs, notes, and experiments.
print("\n" + "=" * 60)
print("SECTION 6: ASSIGNMENTS & EXERCISES")
print("=" * 60)

# ------------------------------------------------------------------------------
# Task 1 — Create DataFrame normally
# ------------------------------------------------------------------------------
assign_data = {
    "Country": ["India", "India", "India", "USA", "USA"],
    "City": ["Chennai", "Salem", "Coimbatore", "New York", "Texas"],
    "Sales": [500, 300, 400, 700, 600]
}
task1_df = pd.DataFrame(assign_data)
print("\n[Task 1 — Normal DataFrame]\n", task1_df)

# ------------------------------------------------------------------------------
# Task 2 — set_index() for MultiIndex
# ------------------------------------------------------------------------------
task2_df = task1_df.set_index(["Country", "City"])
print("\n[Task 2 — MultiIndex DataFrame]\n", task2_df)

# ------------------------------------------------------------------------------
# Task 3 — Display India's Data
# ------------------------------------------------------------------------------
print("\n[Task 3 — India Data (loc['India'])]\n", task2_df.loc["India"])

# ------------------------------------------------------------------------------
# Task 4 — Display Salem's Data
# ------------------------------------------------------------------------------
print("\n[Task 4 — Salem Data (loc[('India', 'Salem')])]\n", task2_df.loc[("India", "Salem")])

# ------------------------------------------------------------------------------
# Task 5 — reset_index()
# ------------------------------------------------------------------------------
task5_df = task2_df.reset_index()
print("\n[Task 5 — Converted back to Normal Columns (reset_index())]\n", task5_df)
