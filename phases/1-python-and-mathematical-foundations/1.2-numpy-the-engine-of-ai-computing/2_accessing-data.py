"""
NumPy Accessing Data: Indexing, Slicing, 2D & 3D Arrays - Topic File

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
# Accessing data in NumPy is how we retrieve specific values, sub-matrices,
# channels, or batches from N-dimensional arrays.
#
# Mental Model:
#   1D: array[index]                              -> Single axis (vector)
#   2D: array[row, column]                        -> Two axes (matrix / grayscale image)
#   3D: array[depth/channel, row, column]         -> Three axes (RGB image / batch of matrices)
#
# Key Rule:
#   Slicing uses [start:stop:step].
#   - start is INCLUDED
#   - stop is EXCLUDED
#   - ":" means "select everything along this axis"


# ==============================================================================
# 2. Why AI engineers use it
# ==============================================================================
# - Image Cropping: Selecting a bounding box region `image[y1:y2, x1:x2]`.
# - Channel Separation: Extracting the Red channel of an RGB image `image[:, :, 0]`.
# - Batch Slicing: Extracting a mini-batch of training data `dataset[0:32]`.
# - Feature Extraction: Selecting specific tabular columns/features `X[:, [0, 2, 5]]`.
# - Time Series Subsetting: Taking the last N timesteps `sequence[-N:]`.


# ==============================================================================
# 3. Syntax
# ==============================================================================
# 1D Indexing & Slicing:
#   arr[0]              -> First item
#   arr[-1]             -> Last item
#   arr[start:stop]     -> Range from start up to stop-1
#   arr[:n]             -> First n elements
#   arr[n:]             -> From index n to end
#   arr[::step]         -> Every `step` elements (arr[::-1] reverses)
#
# 2D Indexing & Slicing:
#   matrix[row, col]               -> Single scalar at (row, col)
#   matrix[row, :] or matrix[row]  -> Entire row
#   matrix[:, col]                 -> Entire column
#   matrix[r_start:r_stop, c_start:c_stop] -> Sub-grid / Patch
#
# 3D Indexing & Slicing:
#   arr3d[batch, row, col]         -> Single element in 3D volume
#   arr3d[:, :, channel]           -> Specific channel across whole 2D grid


# ==============================================================================
# 4. Example (Runnable)
# ==============================================================================
print("=" * 60)
print("SECTION 4: RUNNABLE EXAMPLES")
print("=" * 60)

# --- 1D Indexing & Slicing ---
arr1d = np.array([10, 20, 30, 40, 50])
print("1D Array         :", arr1d)
print("  First (arr1d[0]):", arr1d[0])
print("  Last (arr1d[-1]):", arr1d[-1])
print("  Slice (1 to 4)  :", arr1d[1:4])   # [20, 30, 40]
print("  Reversed (::-1) :", arr1d[::-1])  # [50, 40, 30, 20, 10]

# --- 2D Indexing & Slicing ---
# Matrix layout:
#         col 0  col 1  col 2
# row 0 [   1      2      3   ]
# row 1 [   4      5      6   ]
# row 2 [   7      8      9   ]
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("\n2D Matrix:\n", matrix)
print("  Element at row 1, col 2 (matrix[1, 2]):", matrix[1, 2])  # 6
print("  Entire Row 1 (matrix[1, :])           :", matrix[1, :])  # [4, 5, 6]
print("  Entire Col 2 (matrix[:, 2])           :", matrix[:, 2])  # [3, 6, 9]
print("  Sub-matrix [0:2, 1:3]:\n", matrix[0:2, 1:3])           # [[2, 3], [5, 6]]

# --- 3D Array Example (e.g. 2 samples, each 2x2 pixels) ---
cube = np.array([
    [[10, 20], [30, 40]],  # Sample 0
    [[50, 60], [70, 80]]   # Sample 1
])
print("\n3D Array (shape 2x2x2):\n", cube)
print("  Sample 0 (cube[0]):\n", cube[0])
print("  Value at sample 1, row 0, col 1 (cube[1, 0, 1]):", cube[1, 0, 1])  # 60


# ==============================================================================
# 5. Mini Practice (all mini practice for this topic) + Solutions
# ==============================================================================
print("\n" + "=" * 60)
print("SECTION 5: MINI PRACTICE")
print("=" * 60)

# Practice 1: Extract the middle element of [100, 200, 300, 400, 500]
p1_arr = np.array([100, 200, 300, 400, 500])
mid_element = p1_arr[len(p1_arr) // 2]
print("Mini Practice 1 (Middle element):", mid_element)  # 300

# Practice 2: Select all columns except the last one (Feature matrix X vs Target y)
data_table = np.array([
    [1.2, 3.4, 0],
    [5.6, 7.8, 1],
    [9.0, 2.1, 0]
])
X = data_table[:, :-1]  # all rows, all columns except last
y = data_table[:, -1]   # all rows, only last column
print("Mini Practice 2 (Features X):\n", X)
print("Mini Practice 2 (Labels y)   :", y)

# Practice 3: Extract the diagonal from a 3x3 matrix using indexing
p3_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
diagonal = np.array([p3_matrix[i, i] for i in range(3)])
print("Mini Practice 3 (Diagonal)   :", diagonal)  # [1, 5, 9]


# ==============================================================================
# 6. Assignments (Solutions Included)
# ==============================================================================
# Rule: No Google/AI. Use only Python docs, notes, and experiments.
print("\n" + "=" * 60)
print("SECTION 6: ASSIGNMENT - NUMPY INDEXING & SLICING")
print("=" * 60)

# ------------------------------------------------------------------------------
# Task 1 - 1D Indexing
# ------------------------------------------------------------------------------
numbers = np.array([10, 20, 30, 40, 50, 60, 70])
print("\n[Task 1 - 1D Indexing]")
print("Array               :", numbers)
print("First element  ([0]):", numbers[0])   # 10
print("Fourth element ([3]):", numbers[3])   # 40 (0-indexed: index 3 is 4th)
print("Last element   ([-1]):", numbers[-1]) # 70
print("Second-last    ([-2]):", numbers[-2]) # 60

# ------------------------------------------------------------------------------
# Task 2 - Slicing
# ------------------------------------------------------------------------------
print("\n[Task 2 - Slicing]")
print("First 3 elements   ([:3]) :", numbers[:3])   # [10, 20, 30]
print("Last 3 elements    ([-3:]):", numbers[-3:])  # [50, 60, 70]
print("Index 2 to 5       ([2:6]):", numbers[2:6])  # [30, 40, 50, 60] (stop=6 is excluded)
print("Every second item  ([::2]):", numbers[::2])  # [10, 30, 50, 70]
print("Array in reverse   ([::-1]):", numbers[::-1]) # [70, 60, 50, 40, 30, 20, 10]

# ------------------------------------------------------------------------------
# Task 3 - 2D Indexing
# ------------------------------------------------------------------------------
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print("\n[Task 3 - 2D Indexing]")
print("Matrix:\n", matrix)
print("Value 50 (row 1, col 1):", matrix[1, 1])
print("Value 90 (row 2, col 2):", matrix[2, 2])
print("Value 20 (row 0, col 1):", matrix[0, 1])
print("Value 70 (row 2, col 0):", matrix[2, 0])

# ------------------------------------------------------------------------------
# Task 4 - Rows & Columns
# ------------------------------------------------------------------------------
print("\n[Task 4 - Rows & Columns]")
print("First row    (matrix[0, :]):", matrix[0, :])
print("Second row   (matrix[1, :]):", matrix[1, :])
print("Third column (matrix[:, 2]):", matrix[:, 2])
print("First column (matrix[:, 0]):", matrix[:, 0])

# ------------------------------------------------------------------------------
# Task 5 - 2D Slicing
# ------------------------------------------------------------------------------
# Goal: Extract [[20, 30], [50, 60]]
# Explanation:
# - Rows needed: row 0 and row 1 -> rows slice is 0:2
# - Cols needed: col 1 and col 2 -> cols slice is 1:3
sub_block = matrix[0:2, 1:3]
print("\n[Task 5 - 2D Slicing]")
print("Extracted Sub-matrix [0:2, 1:3]:\n", sub_block)

# ------------------------------------------------------------------------------
# Challenge - Strided 2D Slicing (The 4 Corners)
# ------------------------------------------------------------------------------
# Goal: Extract the 4 corners:
#   [[10, 30],
#    [70, 90]]
# Intuition:
# - Rows needed: row 0 and row 2 (skip row 1) -> row slice `::2`
# - Cols needed: col 0 and col 2 (skip col 1) -> col slice `::2`
corners = matrix[::2, ::2]
print("\n[Challenge - 4 Corners using Strided Slicing (matrix[::2, ::2])]")
print(corners)
