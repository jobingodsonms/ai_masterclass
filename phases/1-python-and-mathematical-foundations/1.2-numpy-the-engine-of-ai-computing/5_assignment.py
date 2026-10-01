"""
NumPy Array Creation - Assignment Solution (numpy_creation.py)

Mental Model:
  np.zeros(shape):
    Create array filled with 0.0 (or ints with dtype=int).
  np.ones(shape):
    Create array filled with 1.0 (or ints with dtype=int).
  np.arange(start, stop, step):
    Generate numbers with a specified step (stop is excluded).
  np.linspace(start, stop, num):
    Generate exactly `num` evenly spaced values (stop is included).
  np.random.randint(low, high, size):
    Generate random integers in [low, high).
  np.random.seed(seed):
    Ensure 100% reproducible random generation for ML experiments.
  np.eye(N):
    Create N x N identity matrix (1s on main diagonal).
"""

import numpy as np

# ==============================================================================
# Task 1 — Zeros
# ==============================================================================
# Create a 3 x 5 array containing only zeros.

print("--- Task 1: Zeros ---")
zeros_matrix = np.zeros((3, 5))
print("3 x 5 Zeros Matrix:\n", zeros_matrix)
print("Shape:", zeros_matrix.shape)
print()


# ==============================================================================
# Task 2 — Ones
# ==============================================================================
# Create a 4 x 4 array containing only ones with integer data type.

print("--- Task 2: Ones (Integer) ---")
ones_matrix = np.ones((4, 4), dtype=int)
print("4 x 4 Ones Matrix:\n", ones_matrix)
print("dtype:", ones_matrix.dtype)
print()


# ==============================================================================
# Task 3 — arange()
# ==============================================================================
# Generate 10, 20, 30, 40, ... 100 using one NumPy command.

print("--- Task 3: arange() ---")
tens_array = np.arange(10, 101, 10)
print("Generated Array:", tens_array)
print()


# ==============================================================================
# Task 4 — linspace()
# ==============================================================================
# Generate exactly 11 values evenly spaced between 0 and 100.

print("--- Task 4: linspace() ---")
linspace_array = np.linspace(0, 100, 11)
print("11 Evenly Spaced Values (0 to 100):\n", linspace_array)
print()


# ==============================================================================
# Task 5 — Random Integers
# ==============================================================================
# Generate a 5 x 5 array containing random integers between 1 and 100.

print("--- Task 5: Random Integers ---")
# High value is exclusive, so 101 includes up to 100
random_matrix = np.random.randint(1, 101, size=(5, 5))
print("5 x 5 Random Matrix (1 to 100):\n", random_matrix)
print()


# ==============================================================================
# Task 6 — Reproducibility
# ==============================================================================
# Set random seed to 42 and generate 10 random integers between 1 and 50.

print("--- Task 6: Reproducibility ---")
np.random.seed(42)
first_run = np.random.randint(1, 51, size=10)
print("First Run  (seed=42):", first_run)

np.random.seed(42)
second_run = np.random.randint(1, 51, size=10)
print("Second Run (seed=42):", second_run)
print("Are both runs identical?:", np.array_equal(first_run, second_run))
print()


# ==============================================================================
# Task 7 — Identity Matrix
# ==============================================================================
# Create a 5 x 5 identity matrix.

print("--- Task 7: Identity Matrix ---")
identity_5x5 = np.eye(5)
print("5 x 5 Identity Matrix:\n", identity_5x5)
print()


# ==============================================================================
# Mini AI Challenge — Fake Student Dataset
# ==============================================================================
# Generate dataset for 100 students:
# - ages: random integers from 18 to 25
# - study_hours: random float values from 0 to 10
# - scores: random integers from 0 to 100
# Vectorized solution (no for loops).

print("--- Mini AI Challenge: Fake Student Dataset ---")
np.random.seed(42)

ages = np.random.randint(18, 26, size=100)
study_hours = np.round(np.random.rand(100) * 10, 2)
scores = np.random.randint(0, 101, size=100)

print("Ages        - Shape:", ages.shape, "| Range:", np.min(ages), "-", np.max(ages))
print("  Sample (first 10):", ages[:10])

print("\nStudy Hours - Shape:", study_hours.shape, "| Range:", np.min(study_hours), "-", np.max(study_hours))
print("  Sample (first 10):", study_hours[:10])

print("\nExam Scores - Shape:", scores.shape, "| Range:", np.min(scores), "-", np.max(scores))
print("  Sample (first 10):", scores[:10])
