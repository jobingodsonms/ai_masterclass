"""
NumPy Matrix Operations & Linear Algebra - Topic File

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
# Linear algebra is the mathematical backbone of modern Artificial Intelligence and Machine Learning.
# Vectors represent features, data points, or embeddings.
# Matrices represent dataset batches, linear transformations, and neural network weights.
#
# Key Concepts:
# 1. Vectors (1D Array): Represents features of a single data sample.
# 2. Dot Product (np.dot(a, b) or a @ b): Sum of element-wise products -> scalar result.
# 3. Matrix Multiplication (A @ B or np.matmul(A, B)): Linear transformation of feature spaces.
# 4. * vs @ Operator:
#    - `*` performs element-wise multiplication (Hadamard product).
#    - `@` performs true matrix multiplication (dot product of rows and columns).
# 5. Matrix Shape Rule:
#    (M x N) @ (N x P) -> (M x P). Inner dimensions MUST match!
# 6. Transpose (.T): Swaps rows and columns (switches orientation).
# 7. Identity Matrix (np.eye()): Matrix multiplier identity (A @ I = A).
# 8. Inverse (np.linalg.inv(A)): Matrix inverse such that A @ inv(A) = I.


# ==============================================================================
# 2. Why AI engineers use it
# ==============================================================================
# - Linear Regression & Perceptrons: Output = dot_product(features, weights) + bias.
# - Neural Network Layers: Dense / Fully-Connected Layer forward pass: `Output = X @ W + B`.
# - Attention Mechanisms (Transformers / LLMs): Query-Key attention calculation `Q @ K.T`.
# - Dimensionality Reduction & PCA: Eigenvalue decomposition and covariance matrices.
# - Speed & Vectorization: Matrix multiplication running on BLAS / LAPACK libraries is 100x faster than loops.


# ==============================================================================
# 3. Syntax
# ==============================================================================
# Dot Product (Vectors):
#   result = np.dot(v1, v2)
#   result = v1 @ v2
#
# Element-wise vs Matrix Multiplication:
#   A * B                        -> Element-wise multiplication (same shape required)
#   A @ B                        -> Matrix multiplication (inner dimensions must match)
#   np.matmul(A, B)              -> Functional matrix multiplication
#
# Transpose & Inverse:
#   matrix.T                     -> Transpose matrix (rows <-> cols)
#   np.linalg.inv(matrix)        -> Inverse matrix (must be square & non-singular)
#
# Identity Matrix Property:
#   A @ np.eye(N)                -> Returns matrix A unchanged


# ==============================================================================
# 4. Example (Runnable)
# ==============================================================================
print("=" * 60)
print("SECTION 4: RUNNABLE EXAMPLES")
print("=" * 60)

# --- 1. Vector Dot Product ---
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
dot_val = v1 @ v2  # 1*4 + 2*5 + 3*6 = 32
print("Vector 1:", v1)
print("Vector 2:", v2)
print("Dot Product (v1 @ v2):", dot_val)

# --- 2. Element-wise (*) vs Matrix Multiplication (@) ---
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("\nMatrix A:\n", A)
print("Matrix B:\n", B)
print("Element-wise Multiplication (A * B):\n", A * B)
print("Matrix Multiplication       (A @ B):\n", A @ B)

# --- 3. Shape Rules & Transpose ---
X = np.random.randint(1, 10, size=(2, 3))
W = np.random.randint(1, 10, size=(3, 4))
out = X @ W
print("\nShape Rule: (2, 3) @ (3, 4) -> Output Shape:", out.shape)

# --- 4. Identity Matrix & Inverse ---
I = np.eye(2)
print("\nA @ Identity Matrix:\n", A @ I)

A_inv = np.linalg.inv(A)
print("\nA @ Inverse(A):\n", np.round(A @ A_inv, 2))


# ==============================================================================
# 5. Mini Practice (all mini practice for this topic) + Solutions
# ==============================================================================
print("\n" + "=" * 60)
print("SECTION 5: MINI PRACTICE")
print("=" * 60)

# Practice 1: Feature Weighted Prediction (Single Sample)
features = np.array([5.0, 80.0, 7.0])     # [Study hours, Attendance, Assignments]
weights  = np.array([0.5, 0.2, 1.5])     # Feature weights
prediction = np.dot(features, weights)
print("Mini Practice 1 (Weighted Score Prediction):")
print("  Prediction Score:", prediction)  # 5*0.5 + 80*0.2 + 7*1.5 = 2.5 + 16.0 + 10.5 = 29.0

# Practice 2: Batch Feature Transformation (5 samples x 3 features @ 3 x 2 weights)
X_batch = np.ones((5, 3))
W_layer = np.array([
    [0.1, 0.2],
    [0.3, 0.4],
    [0.5, 0.6]
])
layer_output = X_batch @ W_layer
print("\nMini Practice 2 (Batch Dense Layer Forward Pass):")
print("  Batch Input Shape :", X_batch.shape)
print("  Weights Shape     :", W_layer.shape)
print("  Layer Output Shape:", layer_output.shape)
print("  First sample output:", layer_output[0])

# Practice 3: Identity property check
square_mat = np.array([[4, 7], [2, 6]])
identity_2d = np.eye(2)
print("\nMini Practice 3 (Identity Match):", np.array_equal(square_mat @ identity_2d, square_mat))


# ==============================================================================
# 6. Assignments (Solutions Included)
# ==============================================================================
# Rule: No Google/AI. Use only Python docs, notes, and experiments.
print("\n" + "=" * 60)
print("SECTION 6: ASSIGNMENT - NUMPY MATRIX & LINEAR ALGEBRA")
print("=" * 60)

# ------------------------------------------------------------------------------
# Task 1 — Dot Product
# ------------------------------------------------------------------------------
a = np.array([2, 4, 6])
b = np.array([1, 3, 5])
dot_func = np.dot(a, b)
dot_oper = a @ b

print("\n[Task 1 — Dot Product]")
print("a:", a, "| b:", b)
print("np.dot(a, b):", dot_func)
print("a @ b       :", dot_oper)
print("Match?      :", dot_func == dot_oper)

# ------------------------------------------------------------------------------
# Task 2 — Matrix Multiplication vs Element-wise
# ------------------------------------------------------------------------------
A_task2 = np.array([[1, 2], [3, 4]])
B_task2 = np.array([[5, 6], [7, 8]])

print("\n[Task 2 — * vs @ Multiplication]")
print("Element-wise (A * B):\n", A_task2 * B_task2)
print("Matrix Mult  (A @ B):\n", A_task2 @ B_task2)

# ------------------------------------------------------------------------------
# Task 3 — Shape Rules
# ------------------------------------------------------------------------------
np.random.seed(42)
A_shape = np.random.randint(1, 10, size=(3, 4))
B_shape = np.random.randint(1, 10, size=(4, 2))
C_shape = A_shape @ B_shape

print("\n[Task 3 — Shape Rules]")
print("A shape:", A_shape.shape)
print("B shape:", B_shape.shape)
print("C shape:", C_shape.shape)

# ------------------------------------------------------------------------------
# Task 4 — Transpose
# ------------------------------------------------------------------------------
mat_t = np.array([[1, 2, 3], [4, 5, 6]])

print("\n[Task 4 — Transpose]")
print("Original Matrix:\n", mat_t, "| Shape:", mat_t.shape)
print("Transposed (.T):\n", mat_t.T, "| Shape:", mat_t.T.shape)

# ------------------------------------------------------------------------------
# Task 5 — Identity Matrix
# ------------------------------------------------------------------------------
I_3d = np.eye(3)
A_3d = np.array([[2, 4, 6], [1, 3, 5], [7, 8, 9]])
result_I = A_3d @ I_3d

print("\n[Task 5 — Identity Matrix Verification]")
print("A @ I equals A?:", np.array_equal(result_I, A_3d))

# ------------------------------------------------------------------------------
# Final AI Challenge — Neural Network Layer Forward Pass
# ------------------------------------------------------------------------------
print("\n[Final AI Challenge — Neural Network Forward Pass]")
x_in = np.array([5, 80, 70])
weights_layer = np.array([
    [0.2, 0.1],
    [0.3, 0.4],
    [0.5, 0.2]
])
output_layer = x_in @ weights_layer

print("x shape      :", x_in.shape)
print("weights shape:", weights_layer.shape)
print("output shape :", output_layer.shape)
print("output values:", output_layer)
print("Shape Transformation Intuition: (3,) @ (3, 2) -> Inner dimension 3 contracts via dot product, leaving (2,) output features.")
