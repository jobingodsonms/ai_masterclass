"""
NumPy Fundamentals - Topic File

Structure:
1. Concept (What it is)
2. Why AI engineers use it
3. Syntax
4. Example
5. Mini Practice (all mini practice with solutions)
6. Assignments (solutions included)

"""

import numpy as np

# ==============================================================================
# 1. Concept (What it is)
# ==============================================================================
# NumPy stands for "Numerical Python".
# It provides a powerful, high-performance data structure called an ndarray
# (N-dimensional array) along with tools for fast mathematical operations.
#
# Intuition:
#   Python List  --> General-purpose container (can hold mixed types, slow loops)
#        ↓
#   NumPy Array  --> Contiguous memory block, fixed data type, optimized in C
#        ↓
#   AI / ML / Data Science Engine (vectorized operations without manual loops)


# ==============================================================================
# 2. Why AI engineers use it
# ==============================================================================
# - Almost all AI data is represented as numbers:
#     * Image  --> Grayscale / RGB pixel grid (2D or 3D NumPy array)
#     * Text   --> Token IDs & dense embeddings (vectors / 2D matrices)
#     * Audio  --> Waveform amplitude samples over time
# - Speed & Vectorization: Operations run orders of magnitude faster than Python loops.
# - The foundation of the modern AI stack:
#     NumPy → Pandas → Scikit-Learn → PyTorch / TensorFlow → Modern LLMs & Vision Models


# ==============================================================================
# 3. Syntax
# ==============================================================================
# Installation:
#   pip install numpy
#
# Importing:
#   import numpy as np
#
# Creating an array:
#   arr = np.array([element1, element2, element3])
#
# Key Array Inspection Attributes:
#   arr.shape  -> Tuple giving the size of each dimension (e.g., (rows, cols))
#   arr.ndim   -> Number of dimensions / axes (e.g., 1 for vector, 2 for matrix)
#   arr.size   -> Total count of elements across all dimensions
#   arr.dtype  -> Data type of elements (e.g., int32, int64, float32, float64)


# ==============================================================================
# 4. Example (Runnable)
# ==============================================================================
print("=" * 60)
print("SECTION 4: RUNNABLE EXAMPLES")
print("=" * 60)

# --- 1D Array (Vector) ---
vector = np.array([10, 20, 30, 40, 50])
print("1D Array:", vector)
print("  .shape :", vector.shape)  # (5,) -> 1 dimension with 5 items
print("  .ndim  :", vector.ndim)   # 1
print("  .size  :", vector.size)   # 5
print("  .dtype :", vector.dtype)  # e.g., int32 or int64

# --- 2D Array (Matrix / Grayscale Image slice) ---
# A 3x3 pixel patch of an image
image_patch = np.array([
    [120, 130, 140],
    [80,  90,  100],
    [200, 210, 220]
])
print("\n2D Array (Image Patch):\n", image_patch)
print("  .shape :", image_patch.shape)  # (3, 3) -> 3 rows, 3 columns
print("  .ndim  :", image_patch.ndim)   # 2
print("  .size  :", image_patch.size)   # 9 elements total
print("  .dtype :", image_patch.dtype)

# --- Vectorization vs Python Loop ---
# Multiplying all elements by 2:
doubled = vector * 2
print("\nVectorized multiplication (vector * 2):", doubled)


# ==============================================================================
# 5. Mini Practice (all mini practice for this topic) + Solutions
# ==============================================================================
print("\n" + "=" * 60)
print("SECTION 5: MINI PRACTICE")
print("=" * 60)

# 1. Create a 1D array of floats and observe its dtype
mp1 = np.array([1.5, 2.5, 3.5, 4.5])
print("Mini Practice 1 (Float Array):", mp1)
print("  dtype:", mp1.dtype)  # float64

# 2. Convert an existing Python list of mixed integers into a specific dtype (e.g., float32 for neural nets)
mp2 = np.array([1, 2, 3, 4], dtype=np.float32)
print("Mini Practice 2 (Explicit float32):", mp2)
print("  dtype:", mp2.dtype)

# 3. Create a 3D array (like a batch of small images or RGB channels) and inspect ndim, shape, and size
mp3 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print("Mini Practice 3 (3D Array):\n", mp3)
print("  .ndim :", mp3.ndim)   # 3
print("  .shape:", mp3.shape)  # (2, 2, 2)
print("  .size :", mp3.size)   # 8


# ==============================================================================
# 6. Assignments (Solutions Included)
# ==============================================================================
# Rule: No Google/AI. Use only Python docs, notes, and experiments.
#
# Assignment Goal:
#                  NumPy Array
#                      │
#           ┌──────────┼──────────┐
#           ↓          ↓          ↓
#         shape       ndim       size
#           │          │          │
#        structure  dimensions  elements

print("\n" + "=" * 60)
print("SECTION 6: ASSIGNMENT - NUMPY BASICS")
print("=" * 60)

# --- Task 1: Create and print array [10, 20, 30, 40, 50] ---
# Explanation: np.array() wraps a standard Python list into an optimized NumPy ndarray.
task1_arr = np.array([10, 20, 30, 40, 50])
print("\n[Task 1] Created Array:")
print(task1_arr)

# --- Task 2: Print 10, 30, 50 using indexing ---
# Explanation: NumPy arrays are 0-indexed just like Python lists.
# Index 0 -> 10, Index 2 -> 30, Index 4 -> 50.
print("\n[Task 2] Accessing Elements (10, 30, 50):")
print("Index 0:", task1_arr[0])
print("Index 2:", task1_arr[2])
print("Index 4:", task1_arr[4])
# Bonus one-liner using slice with step of 2:
print("Or using slice with step 2 (task1_arr[::2]):", task1_arr[::2])

# --- Task 3: Multiply the entire array by 3 ---
# Explanation: NumPy applies scalar arithmetic element-by-element (broadcasting/vectorization).
task3_result = task1_arr * 3
print("\n[Task 3] Array multiplied by 3:")
print("Result  :", task3_result)
print("Expected: [30 60 90 120 150]")

# --- Task 4: Calculate sum, mean, minimum, maximum ---
# Explanation: NumPy provides fast built-in aggregation methods directly on the array object
# or via top-level np functions (np.sum, np.mean, np.min, np.max).
arr_sum = task1_arr.sum()
arr_mean = task1_arr.mean()
arr_min = task1_arr.min()
arr_max = task1_arr.max()

print("\n[Task 4] Aggregation Statistics:")
print(f"  Sum     : {arr_sum}")
print(f"  Mean    : {arr_mean}")
print(f"  Minimum : {arr_min}")
print(f"  Maximum : {arr_max}")

# --- Task 5: Create 2D array and find shape, ndim, size ---
# Explanation:
# - shape tells us the dimensions as (rows, columns) -> (3, 3)
# - ndim tells us the number of axes/dimensions -> 2
# - size tells us the total number of items in the array (rows * cols) -> 9
task5_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\n[Task 5] 2D Array:")
print(task5_2d)
print("\nArray Inspection:")
print("  shape (structure)   :", task5_2d.shape)
print("  ndim (dimensions)   :", task5_2d.ndim)
print("  size (total elements):", task5_2d.size)
print("  dtype (data type)   :", task5_2d.dtype)