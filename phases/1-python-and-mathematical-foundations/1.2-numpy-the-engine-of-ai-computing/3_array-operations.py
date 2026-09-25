"""
NumPy Array Operations - Topic File

Structure:
1. Concept (What it is)
2. Why AI engineers use it
3. Syntax
4. Example (runnable)
5. Mini Practice (all mini practice with solutions)
6. Assignments (solutions included + Challenge)

This file follows the learning template and provides runnable examples.
"""

import numpy as np

# ==============================================================================
# 1. Concept (What it is)
# ==============================================================================
# NumPy array operations perform mathematical, logical, and statistical calculations
# across entire arrays element-by-element (vectorization) without explicit Python loops.
#
# Key Concepts:
# 1. Element-wise Arithmetic:
#    Operations between arrays of the same shape apply to corresponding elements.
# 2. Scalar Operations (Broadcasting Intro):
#    Operating with a single number distributes that scalar to every element.
# 3. Boolean Filtering (Masking):
#    Comparison operations return arrays of Booleans, which can index into the array
#    to select only elements that satisfy the condition.
# 4. Aggregations & Axes:
#    Statistical reductions can run across the entire array or along specific dimensions:
#      - axis=0 -> collapse rows, work DOWN columns (column-wise)
#      - axis=1 -> collapse columns, work ACROSS rows (row-wise)


# ==============================================================================
# 2. Why AI engineers use it
# ==============================================================================
# - Normalization / Standardization: Scaling feature values `(X - mean) / std`.
# - Loss Calculations: Mean Squared Error (MSE) `np.mean((y_pred - y_true)**2)`.
# - Outlier Removal: Filtering samples `data[data < threshold]`.
# - Feature-wise Statistics: Calculating mean and std across training batches (`axis=0`).
# - Performance: Vectorized C-implementations run 10x-100x faster than standard Python loops.


# ==============================================================================
# 3. Syntax
# ==============================================================================
# Element-wise Arithmetic:
#   a + b, a - b, a * b, a / b, a ** 2
#
# Scalar Operations:
#   a + 10, a * 2, a / 5
#
# Comparisons & Boolean Masking:
#   mask = a > 25              -> Boolean array of True/False
#   filtered = a[a > 25]       -> Extracts elements where condition is True
#   combined = a[(a >= 15) & (a <= 40)]  -> Multiple conditions using `&` (and), `|` (or)
#
# Aggregations:
#   np.sum(arr),    arr.sum()
#   np.mean(arr),   arr.mean()
#   np.min(arr),    arr.min()
#   np.max(arr),    arr.max()
#   np.std(arr),    arr.std()
#   np.median(arr)             -> (Note: arr.median() does not exist; use np.median(arr))
#
# Axis Parameter (2D Arrays):
#   np.sum(matrix, axis=0)     -> Sum down columns (result shape: [num_cols])
#   np.sum(matrix, axis=1)     -> Sum across rows (result shape: [num_rows])


# ==============================================================================
# 4. Example (Runnable)
# ==============================================================================
print("=" * 60)
print("SECTION 4: RUNNABLE EXAMPLES")
print("=" * 60)

# --- Element-wise Arithmetic ---
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])
print("Array a:", a)
print("Array b:", b)
print("a + b  :", a + b)  # [11, 22, 33, 44]
print("a * b  :", a * b)  # [10, 40, 90, 160]

# --- Scalar Operations ---
print("\na * 2  :", a * 2)  # [20, 40, 60, 80]
print("a + 5  :", a + 5)    # [15, 25, 35, 45]

# --- Comparisons & Filtering ---
data = np.array([10, 20, 30, 40, 50])
print("\ndata > 25       :", data > 25)        # [False, False, True, True, True]
print("data[data > 25] :", data[data > 25])  # [30, 40, 50]

# --- 2D Aggregations & Axes ---
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print("\nMatrix:\n", matrix)
print("Total sum           :", np.sum(matrix))           # 450
print("Column sums (axis=0):", np.sum(matrix, axis=0))   # [120, 150, 180]
print("Row sums    (axis=1):", np.sum(matrix, axis=1))   # [60, 150, 240]


# ==============================================================================
# 5. Mini Practice (all mini practice for this topic) + Solutions
# ==============================================================================
print("\n" + "=" * 60)
print("SECTION 5: MINI PRACTICE")
print("=" * 60)

# Practice 1: Feature Standardization (Z-score normalization)
# Formula: (x - mean) / std
features = np.array([10.0, 20.0, 30.0, 40.0, 50.0])
mean_val = np.mean(features)
std_val = np.std(features)
standardized = (features - mean_val) / std_val
print("Mini Practice 1 (Standardized Features):")
print("  Original    :", features)
print("  Mean        :", round(mean_val, 2))
print("  Std Dev     :", round(std_val, 2))
print("  Standardized:", np.round(standardized, 2))

# Practice 2: Threshold clipping with boolean masking
# Replace all negative values with 0 (ReLU activation function intuition)
activations = np.array([-2.5, 1.2, -0.4, 3.8, -1.0, 4.5])
relu_output = activations.copy()
relu_output[relu_output < 0] = 0
print("\nMini Practice 2 (ReLU Activation):")
print("  Input :", activations)
print("  Output:", relu_output)

# Practice 3: Find column-wise maximum in a 2D matrix
scores = np.array([
    [75, 88, 92],
    [82, 79, 95],
    [90, 84, 89]
])
col_max = np.max(scores, axis=0)
print("\nMini Practice 3 (Max per column):", col_max)  # [90, 88, 95]


# ==============================================================================
# 6. Assignments (Solutions Included)
# ==============================================================================
# Rule: No Google/AI. Use only Python docs, notes, and experiments.
print("\n" + "=" * 60)
print("SECTION 6: ASSIGNMENT - NUMPY OPERATIONS")
print("=" * 60)

# ------------------------------------------------------------------------------
# Task 1 - Arithmetic
# ------------------------------------------------------------------------------
a = np.array([10, 20, 30, 40, 50])
b = np.array([1, 2, 3, 4, 5])

print("\n[Task 1 - Arithmetic]")
print("a + b:", a + b)  # [11, 22, 33, 44, 55]
print("a - b:", a - b)  # [9, 18, 27, 36, 45]
print("a * b:", a * b)  # [10, 40, 90, 160, 250]
print("a / b:", a / b)  # [10., 10., 10., 10., 10.]

# ------------------------------------------------------------------------------
# Task 2 - Scalar Operations
# ------------------------------------------------------------------------------
print("\n[Task 2 - Scalar Operations]")
print("a + 10 :", a + 10)  # [20, 30, 40, 50, 60]
print("a * 2  :", a * 2)   # [20, 40, 60, 80, 100]
print("a / 5  :", a / 5)   # [2., 4., 6., 8., 10.]
print("a ** 2 :", a ** 2)  # [100, 400, 900, 1600, 2500]

# ------------------------------------------------------------------------------
# Task 3 - Filtering
# ------------------------------------------------------------------------------
numbers = np.array([5, 12, 18, 25, 31, 40, 50])

print("\n[Task 3 - Filtering]")
print("Original numbers               :", numbers)
print("Numbers > 20                   :", numbers[numbers > 20])
print("Numbers < 20                   :", numbers[numbers < 20])
print("Numbers == 25                  :", numbers[numbers == 25])
# In NumPy, combine conditions using bitwise `&` with parentheses around each condition
print("Numbers between 15 and 40 (15 <= n <= 40):", numbers[(numbers >= 15) & (numbers <= 40)])

# ------------------------------------------------------------------------------
# Task 4 - Statistics
# ------------------------------------------------------------------------------
scores = np.array([65, 72, 88, 91, 76, 95, 60, 84])

print("\n[Task 4 - Statistics]")
print("Scores   :", scores)
print("Sum      :", np.sum(scores))
print("Mean     :", round(float(np.mean(scores)), 2))
print("Minimum  :", np.min(scores))
print("Maximum  :", np.max(scores))
print("Median   :", np.median(scores))
print("Std Dev  :", round(float(np.std(scores)), 2))

# ------------------------------------------------------------------------------
# Task 5 - axis (Calculations on 2D Arrays)
# ------------------------------------------------------------------------------
marks = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [95, 88, 92]
])

print("\n[Task 5 - axis Operations]")
print("Marks:\n", marks)
print("Total of entire array         :", np.sum(marks))
print("Sum of each column (axis=0)   :", np.sum(marks, axis=0))
print("Sum of each row    (axis=1)   :", np.sum(marks, axis=1))
print("Average of each col (axis=0)  :", np.round(np.mean(marks, axis=0), 2))
print("Average of each row (axis=1)  :", np.round(np.mean(marks, axis=1), 2))

# ------------------------------------------------------------------------------
# Challenge - Temperature Analysis
# ------------------------------------------------------------------------------
temperatures = np.array([
    [30, 32, 31, 29, 33],
    [28, 30, 29, 31, 32],
    [35, 34, 33, 36, 37]
])

print("\n[Challenge - Temperature Analysis]")
print("Temperatures:\n", temperatures)
print("1. Overall average temperature :", round(float(np.mean(temperatures)), 2))
print("2. Hottest temperature         :", np.max(temperatures))
print("3. Coldest temperature         :", np.min(temperatures))
print("4. Average temp per day/row    :", np.round(np.mean(temperatures, axis=1), 2))
print("5. Temperatures above 32       :", temperatures[temperatures > 32])
