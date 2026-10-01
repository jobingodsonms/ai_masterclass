"""
NumPy Matrix Operations & Linear Algebra - Assignment Solution (numpy_linear_algebra.py)

Mental Model:
  Dot Product (Vectors):
    a @ b = a1*b1 + a2*b2 + ... + an*bn -> single scalar number.
  * vs @:
    *  -> Element-wise multiplication (Hadamard product, shapes must match).
    @  -> Matrix multiplication (dot product of rows and columns).
  Shape Rules:
    (M x N) @ (N x P) -> (M x P).
    The inner dimensions (N) must match; the output takes outer dimensions (M x P).
  Identity Matrix:
    A @ I = A (Identity matrix acts like multiplying by 1).
  Neural Network Layer:
    Input x (shape (F,)) @ Weights W (shape (F, O)) -> Output (shape (O,)).
"""

import numpy as np

# ==============================================================================
# Task 1 — Dot Product
# ==============================================================================
# Create:
# a = np.array([2, 4, 6])
# b = np.array([1, 3, 5])
# Calculate dot product using np.dot() and @ operator. Verify both match.

a = np.array([2, 4, 6])
b = np.array([1, 3, 5])

print("--- Task 1: Dot Product ---")
dot_np = np.dot(a, b)
dot_matmul = a @ b

print("a:", a)
print("b:", b)
print("np.dot(a, b):", dot_np)
print("a @ b       :", dot_matmul)
print("Results match?:", dot_np == dot_matmul)
print()


# ==============================================================================
# Task 2 — Matrix Multiplication (* vs @)
# ==============================================================================
# Create:
# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])
# Calculate A * B and A @ B. Observe the difference.

A = np.array([
    [1, 2],
    [3, 4]
])
B = np.array([
    [5, 6],
    [7, 8]
])

print("--- Task 2: * vs @ Matrix Multiplication ---")
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("\nElement-wise Multiplication (A * B):\n", A * B)
# Explanation: [1*5, 2*6] -> [5, 12]; [3*7, 4*8] -> [21, 32]

print("\nMatrix Multiplication (A @ B):\n", A @ B)
# Explanation: Row 1 dot Col 1 = 1*5 + 2*7 = 19; Row 1 dot Col 2 = 1*6 + 2*8 = 22
#               Row 2 dot Col 1 = 3*5 + 4*7 = 43; Row 2 dot Col 2 = 3*6 + 4*8 = 50
print()


# ==============================================================================
# Task 3 — Shape Rules
# ==============================================================================
# Create A of shape (3, 4) and B of shape (4, 2).
# Calculate C = A @ B. Print shapes.

print("--- Task 3: Shape Rules ---")
np.random.seed(42)
A_shape = np.random.randint(1, 10, size=(3, 4))
B_shape = np.random.randint(1, 10, size=(4, 2))

# Prediction: (3, 4) @ (4, 2) -> inner 4 matches, output shape is (3, 2)
C = A_shape @ B_shape

print("A shape :", A_shape.shape)
print("B shape :", B_shape.shape)
print("C shape :", C.shape)
print("Matrix C:\n", C)
print()


# ==============================================================================
# Task 4 — Transpose
# ==============================================================================
# Create matrix = np.array([[1, 2, 3], [4, 5, 6]])
# Print original matrix, original shape, transposed matrix, transposed shape.

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("--- Task 4: Transpose ---")
print("Original matrix:\n", matrix)
print("Original shape :", matrix.shape)

transposed_matrix = matrix.T
print("\nTransposed matrix:\n", transposed_matrix)
print("Transposed shape :", transposed_matrix.shape)
print()


# ==============================================================================
# Task 5 — Identity Matrix
# ==============================================================================
# Create a 3 x 3 identity matrix I.
# Create A = np.array([[2, 4, 6], [1, 3, 5], [7, 8, 9]])
# Calculate A @ I and check if result equals A.

I = np.eye(3)
A_square = np.array([
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
])

print("--- Task 5: Identity Matrix ---")
print("Matrix A:\n", A_square)
print("Identity Matrix I:\n", I)

A_times_I = A_square @ I
print("\nA @ I:\n", A_times_I)
print("Does A @ I equal A?:", np.array_equal(A_times_I, A_square))
print()


# ==============================================================================
#  Final AI Challenge — Neural Network Forward Pass
# ==============================================================================
# Input vector x (3 features: study_hours=5, attendance=80, previous_score=70)
# Output neurons = 2, Weights matrix shape = (3, 2)
# Calculate output = x @ weights.

x = np.array([5, 80, 70])
weights = np.array([
    [0.2, 0.1],
    [0.3, 0.4],
    [0.5, 0.2]
])

print("--- Final AI Challenge: Neural Network Forward Pass ---")
output = x @ weights

print("Input x shape       :", x.shape)        # (3,)
print("Weights matrix shape:", weights.shape)  # (3, 2)
print("Output vector shape :", output.shape)   # (2,)
print("Output values       :", output)

# Detailed Explanation:
# Output neuron 1 = (5 * 0.2) + (80 * 0.3) + (70 * 0.5) = 1.0 + 24.0 + 35.0 = 60.0
# Output neuron 2 = (5 * 0.1) + (80 * 0.4) + (70 * 0.2) = 0.5 + 32.0 + 14.0 = 46.5
#
# Shape Transformation Logic:
# (3,) @ (3, 2) -> The 1D vector of 3 features aligns with the 3 rows of weights.
# NumPy computes the dot product of the input vector with each of the 2 columns of the weight matrix.
# The inner dimension 3 contracts, resulting in an output vector of shape (2,), representing 2 neuron outputs.
