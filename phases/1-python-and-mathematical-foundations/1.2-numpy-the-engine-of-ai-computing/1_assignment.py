"""
NumPy Basics - Assignment Solution 

Goal:
Understand and practice NumPy fundamentals:
- Array creation
- Indexing
- Vectorized operations
- Built-in aggregations (sum, mean, min, max)
- Array inspection attributes (.shape, .ndim, .size, .dtype)

Mental Model:
                 NumPy Array
                     │
          ┌──────────┼──────────┐
          ↓          ↓          ↓
        shape       ndim       size
          │          │          │
       structure  dimensions  elements
"""

import numpy as np

# ==============================================================================
# Task 1: Create and Print NumPy Array
# ==============================================================================
# Problem: Create this NumPy array: [10, 20, 30, 40, 50] and print it.
# How it works: np.array() converts standard Python data structures into
# contiguous, homogeneous NumPy ndarrays.

numbers = np.array([10, 20, 30, 40, 50])

print("--- Task 1: Create Array ---")
print("Array:", numbers)
print()


# ==============================================================================
# Task 2: Access Elements Using Indexing
# ==============================================================================
# Problem: Print 10, 30, 50 using indexing.
# How it works: NumPy arrays use zero-based indexing:
#   Index 0 -> first element (10)
#   Index 2 -> third element (30)
#   Index 4 -> fifth element (50)

print("--- Task 2: Indexing ---")
print("Element at index 0:", numbers[0])
print("Element at index 2:", numbers[2])
print("Element at index 4:", numbers[4])

# Alternative elegant way (Slicing with step of 2: [start:stop:step]):
# print("Using slice [::2]:", numbers[::2])
print()


# ==============================================================================
# Task 3: Vectorized Multiplication
# ==============================================================================
# Problem: Multiply the entire array by 3.
# Expected: [30 60 90 120 150]
# How it works: Vectorization allows element-wise arithmetic without explicit loops.

multiplied = numbers * 3

print("--- Task 3: Vectorized Multiplication (* 3) ---")
print("Result  :", multiplied)
print("Expected: [30 60 90 120 150]")
print()


# ==============================================================================
# Task 4: Array Aggregations
# ==============================================================================
# Problem: Calculate sum, mean, minimum, and maximum for the array.
# How it works: NumPy methods perform fast C-level reductions over the array data.

arr_sum = numbers.sum()
arr_mean = numbers.mean()
arr_min = numbers.min()
arr_max = numbers.max()

print("--- Task 4: Aggregations ---")
print("Sum    :", arr_sum)
print("Mean   :", arr_mean)
print("Minimum:", arr_min)
print("Maximum:", arr_max)
print()


# ==============================================================================
# Task 5: 2D Array and Attributes (.shape, .ndim, .size)
# ==============================================================================
# Problem: Create this 2D array:
# [
#  [1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]
# ]
# Then find shape, number of dimensions, and number of elements.

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("--- Task 5: 2D Array & Properties ---")
print("Matrix:\n", matrix)
print()
print("1. .shape (Structure / Rows x Columns):", matrix.shape)  # (3, 3) -> 3 rows, 3 cols
print("2. .ndim  (Number of Dimensions/Axes)  :", matrix.ndim)   # 2 dimensions (2D)
print("3. .size  (Total Elements in Array)    :", matrix.size)   # 9 total elements
print("4. .dtype (Data Type of Elements)      :", matrix.dtype)  # int32 / int64
