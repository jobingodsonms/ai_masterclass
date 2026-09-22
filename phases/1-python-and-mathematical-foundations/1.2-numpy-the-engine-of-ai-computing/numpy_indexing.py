"""
NumPy Accessing Data - Assignment Solution (numpy_indexing.py)

Mental Model:
  1D: array[index]
  2D: array[row, column]
  2D slicing: array[row_start:row_end, column_start:column_end]
  Remember: ":" means "everything", and start is included, stop is excluded.
"""

import numpy as np

# ==============================================================================
# Task 1 — 1D Indexing
# ==============================================================================
# Problem:
# Create: numbers = np.array([10, 20, 30, 40, 50, 60, 70])
# Print:
# - First element
# - Fourth element
# - Last element
# - Second-last element

numbers = np.array([10, 20, 30, 40, 50, 60, 70])

print("--- Task 1: 1D Indexing ---")
print("Array              :", numbers)
print("First element  [0] :", numbers[0])   # 10
print("Fourth element [3] :", numbers[3])   # 40 (0-indexed: index 3 is 4th element)
print("Last element   [-1]:", numbers[-1])  # 70
print("Second-last    [-2]:", numbers[-2])  # 60
print()


# ==============================================================================
# Task 2 — Slicing
# ==============================================================================
# Problem: Using the same array, print:
# - First 3 elements
# - Last 3 elements
# - Elements from index 2 to 5
# - Every second element
# - The array in reverse

print("--- Task 2: 1D Slicing ---")
print("First 3 elements    [:3] :", numbers[:3])   # [10, 20, 30]
print("Last 3 elements     [-3:]:", numbers[-3:])  # [50, 60, 70]
print("Index 2 to 5        [2:6]:", numbers[2:6])  # [30, 40, 50, 60] (stop 6 excluded)
print("Every second item   [::2]:", numbers[::2])  # [10, 30, 50, 70]
print("Array in reverse    [::-1]:", numbers[::-1]) # [70, 60, 50, 40, 30, 20, 10]
print()


# ==============================================================================
# Task 3 — 2D Indexing
# ==============================================================================
# Problem:
# Create:
# matrix = np.array([
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ])
# Find: 50, 90, 20, 70 using indexing: matrix[row, column]

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("--- Task 3: 2D Indexing ---")
print("Matrix:\n", matrix)
print("Value 50 (row 1, col 1):", matrix[1, 1])
print("Value 90 (row 2, col 2):", matrix[2, 2])
print("Value 20 (row 0, col 1):", matrix[0, 1])
print("Value 70 (row 2, col 0):", matrix[2, 0])
print()


# ==============================================================================
# Task 4 — Rows & Columns
# ==============================================================================
# Problem: Print:
# - First row
# - Second row
# - Third column
# - First column

print("--- Task 4: Rows & Columns ---")
print("First row    (matrix[0, :]):", matrix[0, :])  # or matrix[0]
print("Second row   (matrix[1, :]):", matrix[1, :])  # or matrix[1]
print("Third column (matrix[:, 2]):", matrix[:, 2])
print("First column (matrix[:, 0]):", matrix[:, 0])
print()


# ==============================================================================
# Task 5 — 2D Slicing
# ==============================================================================
# Problem:
# Extract:
# [[20 30]
#  [50 60]]
# from matrix.
# Explanation:
# - Rows needed: row 0 and row 1 -> rows 0:2
# - Columns needed: column 1 and column 2 -> columns 1:3

sub_matrix = matrix[0:2, 1:3]

print("--- Task 5: 2D Slicing ---")
print("Extracted [0:2, 1:3]:\n", sub_matrix)
print()


# ==============================================================================
# ⭐ Challenge — Strided 2D Slicing (The 4 Corners)
# ==============================================================================
# Problem:
# Without manually writing the values, extract:
# [[10 30]
#  [70 90]]
# Explanation:
# - Rows needed: row 0 and row 2 (skipping row 1) -> slice is `::2` (or `0:3:2`)
# - Cols needed: col 0 and col 2 (skipping col 1) -> slice is `::2` (or `0:3:2`)

corners = matrix[::2, ::2]

print("--- ⭐ Challenge: 4 Corners ---")
print("Corners (matrix[::2, ::2]):\n", corners)
