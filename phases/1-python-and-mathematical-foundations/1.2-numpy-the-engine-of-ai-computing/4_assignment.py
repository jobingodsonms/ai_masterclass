"""
NumPy Shape Manipulation & Broadcasting - Assignment Solution (numpy_shapes.py)

Mental Model:
  reshape():
    Change shape without changing data (total elements must match).
  -1 in reshape:
    NumPy infers the missing dimension automatically.
  flatten() / ravel():
    Convert multi-dimensional array into 1D vector.
  .T (Transpose):
    Swap rows and columns (switch orientation).
  Broadcasting:
    Automatically expand compatible dimensions for element-wise operations.
"""

import numpy as np

# ==============================================================================
# Task 1 - Reshape
# ==============================================================================
# Create: numbers = np.arange(1, 13) -> [1 2 3 4 5 6 7 8 9 10 11 12]
# Reshape into 3 x 4, then into 4 x 3.

numbers = np.arange(1, 13)

print("--- Task 1: Reshape ---")
print("Original numbers:", numbers)

reshaped_3x4 = numbers.reshape(3, 4)
print("\nReshaped into 3 x 4:\n", reshaped_3x4)

reshaped_4x3 = numbers.reshape(4, 3)
print("\nReshaped into 4 x 3:\n", reshaped_4x3)
print()


# ==============================================================================
# Task 2 - -1
# ==============================================================================
# Using the same `numbers` array:
# Try: numbers.reshape(3, -1) and numbers.reshape(-1, 4)

print("--- Task 2: -1 Inference ---")
# Prediction for (3, -1): Total 12 elements / 3 rows = 4 columns -> shape (3, 4)
reshaped_auto1 = numbers.reshape(3, -1)
print("numbers.reshape(3, -1) -> Shape:", reshaped_auto1.shape)
print(reshaped_auto1)

# Prediction for (-1, 4): Total 12 elements / 4 columns = 3 rows -> shape (3, 4)
reshaped_auto2 = numbers.reshape(-1, 4)
print("\nnumbers.reshape(-1, 4) -> Shape:", reshaped_auto2.shape)
print(reshaped_auto2)
print()


# ==============================================================================
# Task 3 - Flatten
# ==============================================================================
# Create 3x3 matrix and flatten it into 1D array using flatten()

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("--- Task 3: Flatten ---")
print("Original Matrix:\n", matrix)
flattened_arr = matrix.flatten()
print("Flattened array:", flattened_arr)
print("Flattened shape:", flattened_arr.shape)
print()


# ==============================================================================
# Task 4 - Transpose
# ==============================================================================
# Transpose the 3x3 matrix using .T

print("--- Task 4: Transpose ---")
transposed_arr = matrix.T
print("Transposed Matrix (.T):\n", transposed_arr)
print()


# ==============================================================================
# Task 5 - Broadcasting
# ==============================================================================
# prices = np.array([100, 200, 300, 400])
# Add a 10% increase by multiplying by 1.10

prices = np.array([100, 200, 300, 400])

print("--- Task 5: Broadcasting (1D / Scalar) ---")
increased_prices = prices * 1.10
print("Original prices :", prices)
print("10% Increase    :", increased_prices)
print()


# ==============================================================================
# Task 6 - 2D Broadcasting
# ==============================================================================
# marks = np.array([
#     [70, 80, 90],
#     [60, 75, 85],
#     [90, 95, 88]
# ])
# Add [5, 10, 2] to every row.

marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [90, 95, 88]
])
bonus = np.array([5, 10, 2])

print("--- Task 6: 2D Broadcasting ---")
print("Original Marks:\n", marks)
print("Bonus to add   :", bonus)
updated_marks = marks + bonus
print("Updated Marks :\n", updated_marks)
print()


# ==============================================================================
# Challenge - Student Marks Bonus & Analysis
# ==============================================================================
# 3 students x 3 subjects: Give everyone 5-mark bonus with 1 NumPy operation.
# Calculate new mean, max, min.

print("--- Challenge: Marks Bonus & Analysis ---")
marks_bonus = marks + 5
print("Marks with 5-mark bonus:\n", marks_bonus)
print("New Mean mark :", round(float(np.mean(marks_bonus)), 2))
print("New Max mark  :", np.max(marks_bonus))
print("New Min mark  :", np.min(marks_bonus))
