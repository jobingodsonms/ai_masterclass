"""
NumPy Shape Manipulation and Broadcasting - Topic File

Structure:
1. Concept (What it is)
2. Why AI engineers use it
3. Syntax
4. Example (runnable)
5. Mini Practice (all mini practice with solutions)
6. Assignments (solutions included + Challenge)
"""

import numpy as np

# ==============================================================================
# 1. Concept (What it is)
# ==============================================================================
# Raw data often comes in shapes that don't directly match what ML models expect.
# Shape manipulation (reshaping, flattening, transposing) and broadcasting allow
# you to reformat data efficiently without changing its contents or writing explicit loops.
#
# Data Pipeline Flow:
#   Raw data -> NumPy array -> reshape / transpose / flatten -> correct format -> ML model
#
# Key Concepts:
# 1. reshape(rows, cols):
#    Changes array structure without changing data. Total element count MUST stay equal.
# 2. Using `-1` in reshape:
#    NumPy automatically calculates the missing dimension based on total size.
# 3. flatten() & ravel():
#    Flattens multi-dimensional arrays into 1D vectors.
#    - flatten(): returns a copy of the array.
#    - ravel(): returns a flattened view (or copy if necessary).
# 4. Transpose (.T):
#    Swaps rows and columns (orientation shift from shape (M, N) to (N, M)).
# 5. Broadcasting:
#    Automatically expands smaller or compatible arrays across larger arrays without copying data.


# ==============================================================================
# 2. Why AI engineers use it
# ==============================================================================
# - Model Inputs: Reshaping image tensors (e.g., 28x28 image matrix -> 784 1D vector for MLPs).
# - Matrix Operations: Transposing weight matrices and feature batches for matrix multiplication `X @ W.T`.
# - Data Augmentation & Normalization: Subtracting mean vector (shape (D,)) from feature matrix (shape (N, D)) via broadcasting.
# - Machine Learning Pipeline: Formatting batched data `(batch_size, sequence_length, features)`.


# ==============================================================================
# 3. Syntax
# ==============================================================================
# Reshaping:
#   arr.reshape(rows, cols)
#   arr.reshape(3, -1)           -> Inferred column count
#   arr.reshape(-1, 2)           -> Inferred row count
#
# Flattening:
#   arr.flatten()                -> Returns a new 1D copy
#   arr.ravel()                  -> Returns a 1D view/copy
#
# Transpose:
#   matrix.T                     -> Swaps axes (rows <-> cols)
#   np.transpose(matrix)         -> Functional equivalent
#
# Broadcasting Rules:
#   1. Scalar to Array: a + 5  (5 is broadcast across all elements)
#   2. 1D to 2D Array: (N, M) + (M,) -> (M,) is broadcast across all N rows
#   3. Compatibility Check: Trailing dimensions must match or one of them must be 1.


# ==============================================================================
# 4. Example (Runnable)
# ==============================================================================
print("=" * 60)
print("SECTION 4: RUNNABLE EXAMPLES")
print("=" * 60)

# --- 1. Reshape & -1 Inference ---
numbers = np.array([1, 2, 3, 4, 5, 6])
print("Original 1D array:", numbers, "| Shape:", numbers.shape)

reshaped_2x3 = numbers.reshape(2, 3)
print("\nreshaped(2, 3):\n", reshaped_2x3, "| Shape:", reshaped_2x3.shape)

reshaped_auto = numbers.reshape(3, -1)
print("\nreshaped(3, -1):\n", reshaped_auto, "| Shape:", reshaped_auto.shape)

# --- 2. Flatten & Transpose ---
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("\nOriginal Matrix (2x3):\n", matrix)

flat = matrix.flatten()
print("flatten():", flat, "| Shape:", flat.shape)

transposed = matrix.T
print("\nTransposed Matrix (.T) (3x2):\n", transposed, "| Shape:", transposed.shape)

# --- 3. Broadcasting ---
a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
b = np.array([1, 2, 3])

print("\nMatrix A (2x3):\n", a)
print("Vector B (3,):", b)
print("A + B (Broadcasting B across rows):\n", a + b)


# ==============================================================================
# 5. Mini Practice (all mini practice for this topic) + Solutions
# ==============================================================================
print("\n" + "=" * 60)
print("SECTION 5: MINI PRACTICE")
print("=" * 60)

# Practice 1: Flatten a 2D image pixel grid into a 1D feature vector
image_grid = np.array([
    [100, 150, 200],
    [50,   75, 125]
])
feature_vector = image_grid.flatten()
print("Mini Practice 1 (Image Flattening):")
print("  Grid shape:", image_grid.shape)
print("  Vector    :", feature_vector, "| Shape:", feature_vector.shape)

# Practice 2: Transpose student-feature matrix to feature-student layout
# Dataset: 3 Students x 2 Features (Height, Weight) -> Transpose to 2 x 3
student_features = np.array([
    [170, 60],
    [175, 70],
    [165, 55]
])
transposed_features = student_features.T
print("\nMini Practice 2 (Feature Transpose):")
print("  Original (3x2):\n", student_features)
print("  Transposed (2x3):\n", transposed_features)

# Practice 3: Row-wise mean subtraction (Broadcasting)
data_matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
offset = np.array([5, 10, 15])
centered_data = data_matrix - offset
print("\nMini Practice 3 (Broadcasting Subtraction):")
print("  Centered Matrix:\n", centered_data)


# ==============================================================================
# 6. Assignments (Solutions Included)
# ==============================================================================
# Rule: No Google/AI. Use only Python docs, notes, and experiments.
print("\n" + "=" * 60)
print("SECTION 6: ASSIGNMENT - NUMPY SHAPES & BROADCASTING")
print("=" * 60)

# ------------------------------------------------------------------------------
# Task 1 - Reshape
# ------------------------------------------------------------------------------
numbers = np.arange(1, 13)

print("\n[Task 1 - Reshape]")
print("Original numbers:", numbers)
r_3x4 = numbers.reshape(3, 4)
print("3 x 4:\n", r_3x4)
r_4x3 = numbers.reshape(4, 3)
print("4 x 3:\n", r_4x3)

# ------------------------------------------------------------------------------
# Task 2 - -1
# ------------------------------------------------------------------------------
print("\n[Task 2 - -1 Dimension Inference]")
auto_3_neg1 = numbers.reshape(3, -1)
print("numbers.reshape(3, -1) shape:", auto_3_neg1.shape)
print(auto_3_neg1)

auto_neg1_4 = numbers.reshape(-1, 4)
print("numbers.reshape(-1, 4) shape:", auto_neg1_4.shape)
print(auto_neg1_4)

# ------------------------------------------------------------------------------
# Task 3 - Flatten
# ------------------------------------------------------------------------------
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\n[Task 3 - Flatten]")
print("Original 3x3 Matrix:\n", matrix)
flattened_matrix = matrix.flatten()
print("Flattened array:", flattened_matrix)

# ------------------------------------------------------------------------------
# Task 4 - Transpose
# ------------------------------------------------------------------------------
print("\n[Task 4 - Transpose]")
transposed_matrix = matrix.T
print("Transposed Matrix (.T):\n", transposed_matrix)

# ------------------------------------------------------------------------------
# Task 5 - Broadcasting
# ------------------------------------------------------------------------------
prices = np.array([100, 200, 300, 400])

print("\n[Task 5 - Broadcasting Scalar]")
prices_increased = prices * 1.10
print("Original prices :", prices)
print("10% Increased   :", prices_increased)

# ------------------------------------------------------------------------------
# Task 6 - 2D Broadcasting
# ------------------------------------------------------------------------------
marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [90, 95, 88]
])
bonus_vector = np.array([5, 10, 2])

print("\n[Task 6 - 2D Broadcasting]")
updated_marks = marks + bonus_vector
print("Original Marks:\n", marks)
print("Bonus Vector   :", bonus_vector)
print("Updated Marks :\n", updated_marks)

# ------------------------------------------------------------------------------
# Challenge - Student Marks Bonus & Analysis
# ------------------------------------------------------------------------------
print("\n[Challenge - Student Marks Bonus & Analysis]")
marks_bonus = marks + 5
print("Marks with 5-mark bonus:\n", marks_bonus)
print("New Mean mark :", round(float(np.mean(marks_bonus)), 2))
print("New Max mark  :", np.max(marks_bonus))
print("New Min mark  :", np.min(marks_bonus))
