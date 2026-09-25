"""
NumPy Array Operations - Assignment Solution (numpy_operations.py)

Mental Model:
  Arithmetic:
    Element-by-element (vectorization).
  Broadcasting:
    Scalar operations apply to every element.
  Boolean Masking:
    condition -> array of True/False -> array[mask] selects matching items.
  Axis:
    axis=0 -> work DOWN columns (collapse rows)
    axis=1 -> work ACROSS rows (collapse columns)
"""

import numpy as np

# ==============================================================================
# Task 1 - Arithmetic
# ==============================================================================
# Create:
# a = np.array([10, 20, 30, 40, 50])
# b = np.array([1, 2, 3, 4, 5])
# Calculate: a + b, a - b, a * b, a / b

a = np.array([10, 20, 30, 40, 50])
b = np.array([1, 2, 3, 4, 5])

print("--- Task 1: Arithmetic ---")
print("a + b:", a + b)  # [11, 22, 33, 44, 55]
print("a - b:", a - b)  # [9, 18, 27, 36, 45]
print("a * b:", a * b)  # [10, 40, 90, 160, 250]
print("a / b:", a / b)  # [10., 10., 10., 10., 10.]
print()


# ==============================================================================
# Task 2 - Scalar Operations
# ==============================================================================
# Using a, calculate: a + 10, a * 2, a / 5, a ** 2

print("--- Task 2: Scalar Operations ---")
print("a + 10 :", a + 10)  # [20, 30, 40, 50, 60]
print("a * 2  :", a * 2)   # [20, 40, 60, 80, 100]
print("a / 5  :", a / 5)   # [2., 4., 6., 8., 10.]
print("a ** 2 :", a ** 2)  # [100, 400, 900, 1600, 2500]
print()


# ==============================================================================
# Task 3 - Filtering
# ==============================================================================
# Using: numbers = np.array([5, 12, 18, 25, 31, 40, 50])
# Find:
# - Numbers greater than 20
# - Numbers less than 20
# - Numbers equal to 25
# - Numbers between 15 and 40 (combined condition)

numbers = np.array([5, 12, 18, 25, 31, 40, 50])

print("--- Task 3: Filtering ---")
print("Original numbers               :", numbers)
print("Numbers > 20                   :", numbers[numbers > 20])
print("Numbers < 20                   :", numbers[numbers < 20])
print("Numbers == 25                  :", numbers[numbers == 25])
print("Numbers between 15 and 40 (15 <= n <= 40):", numbers[(numbers >= 15) & (numbers <= 40)])
print()


# ==============================================================================
# Task 4 - Statistics
# ==============================================================================
# For: scores = np.array([65, 72, 88, 91, 76, 95, 60, 84])
# Calculate: Sum, Mean, Minimum, Maximum, Median, Standard deviation

scores = np.array([65, 72, 88, 91, 76, 95, 60, 84])

print("--- Task 4: Statistics ---")
print("Scores   :", scores)
print("Sum      :", np.sum(scores))
print("Mean     :", round(float(np.mean(scores)), 2))
print("Minimum  :", np.min(scores))
print("Maximum  :", np.max(scores))
print("Median   :", np.median(scores))
print("Std Dev  :", round(float(np.std(scores)), 2))
print()


# ==============================================================================
# Task 5 - axis
# ==============================================================================
# Given:
# marks = np.array([
#     [80, 70, 90],
#     [60, 85, 75],
#     [95, 88, 92]
# ])
# Find:
# - Total of the entire array
# - Sum of each column
# - Sum of each row
# - Average of each column
# - Average of each row

marks = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [95, 88, 92]
])

print("--- Task 5: axis Operations ---")
print("Marks:\n", marks)
print("Total of entire array        :", np.sum(marks))
print("Sum of each column (axis=0)  :", np.sum(marks, axis=0))
print("Sum of each row    (axis=1)  :", np.sum(marks, axis=1))
print("Average of each col (axis=0) :", np.round(np.mean(marks, axis=0), 2))
print("Average of each row (axis=1) :", np.round(np.mean(marks, axis=1), 2))
print()


# ==============================================================================
# Challenge - Temperature Analysis
# ==============================================================================
# Given:
# temperatures = np.array([
#     [30, 32, 31, 29, 33],
#     [28, 30, 29, 31, 32],
#     [35, 34, 33, 36, 37]
# ])
# Find:
# - Overall average temperature
# - Hottest temperature
# - Coldest temperature
# - Average temperature for each day/row
# - Which temperatures are above 32

temperatures = np.array([
    [30, 32, 31, 29, 33],
    [28, 30, 29, 31, 32],
    [35, 34, 33, 36, 37]
])

print("--- Challenge: Temperature Analysis ---")
print("Temperatures:\n", temperatures)
print("1. Overall average temperature :", round(float(np.mean(temperatures)), 2))
print("2. Hottest temperature         :", np.max(temperatures))
print("3. Coldest temperature         :", np.min(temperatures))
print("4. Average temp per day (axis=1):", np.round(np.mean(temperatures, axis=1), 2))
print("5. Temperatures above 32       :", temperatures[temperatures > 32])
