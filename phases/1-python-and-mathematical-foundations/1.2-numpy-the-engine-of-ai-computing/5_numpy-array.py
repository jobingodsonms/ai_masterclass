"""
NumPy Array Creation - Topic File

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
# In AI and machine learning, you rarely type datasets by hand.
# Instead, you programmatically generate arrays for model initializations,
# synthetic benchmarks, data splits, and mathematical transformations.
#
# Key Array Creation Functions:
# 1. np.zeros(shape): Fills array with 0.0 (or ints with dtype=int).
# 2. np.ones(shape): Fills array with 1.0 (or ints with dtype=int).
# 3. np.arange(start, stop, step): Half-open range [start, stop) with step.
# 4. np.linspace(start, stop, num): Closed interval [start, stop] with `num` points.
# 5. np.random.rand(shape): Uniform random floats in [0, 1).
# 6. np.random.randint(low, high, size): Random integers in [low, high).
# 7. np.random.seed(seed): Sets pseudo-random generator state for reproducibility.
# 8. np.eye(N): Creates N x N Identity Matrix (1s on main diagonal, 0s elsewhere).


# ==============================================================================
# 2. Why AI engineers use it
# ==============================================================================
# - Neural Network Weights: Initializing weights with small random floats or zeros/ones.
# - Synthetic Datasets: Generating test inputs, synthetic features, or mock labels for ML pipelines.
# - Time Series & Signal Processing: Creating time steps using `linspace()` (e.g., sampling audio signals).
# - Linear Algebra: Using identity matrix `np.eye()` for matrix inverses, regularization, and coordinate transforms.
# - Reproducibility: Setting `np.random.seed()` ensures model training & data splits are 100% reproducible.


# ==============================================================================
# 3. Syntax
# ==============================================================================
# Zeros & Ones:
#   np.zeros(5)                         -> 1D float array of 5 zeros
#   np.zeros((3, 4))                    -> 2D float array (3 rows, 4 cols)
#   np.ones((2, 3), dtype=int)          -> 2D int array of ones
#
# Ranges & Intervals:
#   np.arange(stop)                     -> [0, 1, ..., stop-1]
#   np.arange(start, stop, step)        -> Half-open interval [start, stop)
#   np.linspace(start, stop, num)       -> Closed interval [start, stop] with `num` values
#
# Random Generation:
#   np.random.rand(rows, cols)          -> Floats in [0.0, 1.0)
#   np.random.randint(low, high, size)  -> Integers in [low, high)
#   np.random.seed(42)                  -> Sets seed for deterministic outputs
#
# Identity Matrix:
#   np.eye(N)                           -> N x N identity matrix


# ==============================================================================
# 4. Example (Runnable)
# ==============================================================================
print("=" * 60)
print("SECTION 4: RUNNABLE EXAMPLES")
print("=" * 60)

# --- 1. Zeros, Ones & Data Types ---
z_2d = np.zeros((2, 3))
o_int = np.ones(4, dtype=int)
print("Zeros (2x3):\n", z_2d)
print("Ones (1D int):", o_int, "| dtype:", o_int.dtype)

# --- 2. arange vs linspace ---
a_range = np.arange(0, 10, 2)
l_space = np.linspace(0, 10, 5)
print("\nnp.arange(0, 10, 2)   :", a_range)   # [0 2 4 6 8] (stop excluded)
print("np.linspace(0, 10, 5) :", l_space)   # [0.  2.5 5.  7.5 10. ] (stop included)

# --- 3. Random Generation & Seed ---
np.random.seed(42)
rand_floats = np.random.rand(2, 3)
rand_ints = np.random.randint(1, 10, size=(2, 3))
print("\nRandom Floats (2x3):\n", np.round(rand_floats, 2))
print("Random Integers (2x3):\n", rand_ints)

# --- 4. Identity Matrix ---
eye_matrix = np.eye(3)
print("\nIdentity Matrix (3x3):\n", eye_matrix)


# ==============================================================================
# 5. Mini Practice (all mini practice for this topic) + Solutions
# ==============================================================================
print("\n" + "=" * 60)
print("SECTION 5: MINI PRACTICE")
print("=" * 60)

# Practice 1: Create a 3x3 mask of ones with integer type
ones_mask = np.ones((3, 3), dtype=int)
print("Mini Practice 1 (Ones Mask):\n", ones_mask)

# Practice 2: Generate 20 time points from 0 to 1 second
time_steps = np.linspace(0, 1, 20)
print("\nMini Practice 2 (Time Steps 0 to 1 sec):")
print(np.round(time_steps, 3))

# Practice 3: Reproducible random noise vector of 5 elements
np.random.seed(100)
noise = np.random.rand(5)
print("\nMini Practice 3 (Reproducible Random Noise):", np.round(noise, 4))


# ==============================================================================
# 6. Assignments (Solutions Included)
# ==============================================================================
# Rule: No Google/AI. Use only Python docs, notes, and experiments.
print("\n" + "=" * 60)
print("SECTION 6: ASSIGNMENT - NUMPY ARRAY CREATION")
print("=" * 60)

# ------------------------------------------------------------------------------
# Task 1 - Zeros
# ------------------------------------------------------------------------------
zeros_3x5 = np.zeros((3, 5))
print("\n[Task 1 - Zeros (3x5)]\n", zeros_3x5)

# ------------------------------------------------------------------------------
# Task 2 - Ones
# ------------------------------------------------------------------------------
ones_4x4_int = np.ones((4, 4), dtype=int)
print("\n[Task 2 - Ones (4x4 int)]\n", ones_4x4_int)

# ------------------------------------------------------------------------------
# Task 3 - arange()
# ------------------------------------------------------------------------------
range_tens = np.arange(10, 101, 10)
print("\n[Task 3 - arange() (10 to 100)]:", range_tens)

# ------------------------------------------------------------------------------
# Task 4 - linspace()
# ------------------------------------------------------------------------------
linespace_11 = np.linspace(0, 100, 11)
print("\n[Task 4 - linspace() (11 points 0 to 100)]:", linespace_11)

# ------------------------------------------------------------------------------
# Task 5 - Random integers
# ------------------------------------------------------------------------------
rand_5x5 = np.random.randint(1, 101, size=(5, 5))
print("\n[Task 5 - Random Integers (5x5)]\n", rand_5x5)

# ------------------------------------------------------------------------------
# Task 6 - Reproducibility
# ------------------------------------------------------------------------------
np.random.seed(42)
seeded_ints = np.random.randint(1, 51, size=10)
print("\n[Task 6 - Reproducibility (seed=42)]:", seeded_ints)

# ------------------------------------------------------------------------------
# Task 7 - Identity Matrix
# ------------------------------------------------------------------------------
eye_5x5 = np.eye(5)
print("\n[Task 7 - Identity Matrix (5x5)]\n", eye_5x5)

# ------------------------------------------------------------------------------
# Mini AI Challenge - Fake Student Dataset
# ------------------------------------------------------------------------------
print("\n[Mini AI Challenge - Synthetic Student Dataset]")
np.random.seed(42)
ages = np.random.randint(18, 26, size=100)
study_hours = np.round(np.random.rand(100) * 10, 2)
scores = np.random.randint(0, 101, size=100)

print("Ages shape       :", ages.shape, "| First 5:", ages[:5])
print("Study Hours shape:", study_hours.shape, "| First 5:", study_hours[:5])
print("Scores shape     :", scores.shape, "| First 5:", scores[:5])
