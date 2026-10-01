"""
Matrix Multiplication Engine (matrix_engine.py)

Custom Matrix Multiplication Implementations:
1. matrix_multiply(A, B): Naive triple-loop implementation.
2. matrix_multiply_vectorized_3d(A, B): 3D broadcasting implementation (A[:, :, None] * B[None, :, :]).
3. matrix_multiply_vectorized_row(A, B): 2D row-vectorized implementation.
4. matrix_multiply_tiled(A, B, block_size): Memory-aware block/tiled matrix multiplication.
"""

import numpy as np


def validate_matrix_dimensions(A: np.ndarray, B: np.ndarray) -> tuple[int, int, int]:
    """
    Validates that inputs A and B are 2D arrays with compatible dimensions for matrix multiplication.
    
    Returns:
        tuple (m, n, p) representing shape(A) = (m, n) and shape(B) = (n, p).
        
    Raises:
        ValueError: If A or B are not 2D arrays or if inner dimensions do not match.
    """
    if not isinstance(A, np.ndarray) or not isinstance(B, np.ndarray):
        raise TypeError("Inputs A and B must be NumPy ndarrays.")

    if A.ndim != 2 or B.ndim != 2:
        raise ValueError(f"Matrix multiplication requires 2D arrays. Got A.ndim={A.ndim}, B.ndim={B.ndim}.")

    m, n_a = A.shape
    n_b, p = B.shape

    if n_a != n_b:
        raise ValueError(
            f"Incompatible matrix dimensions for multiplication: "
            f"A shape ({m}, {n_a}) and B shape ({n_b}, {p}). "
            f"Inner dimensions ({n_a} and {n_b}) must match."
        )

    return m, n_a, p


def matrix_multiply(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """
    Part 1 & 3: Naive matrix multiplication using explicit 3-nested Python loops.
    Mathematical Definition: C[i, j] = sum_k (A[i, k] * B[k, j])
    
    Does NOT use @, np.matmul(), or np.dot().
    """
    m, n, p = validate_matrix_dimensions(A, B)

    # Determine result data type based on inputs
    result_dtype = np.result_type(A.dtype, B.dtype)
    C = np.zeros((m, p), dtype=result_dtype)

    # Triple loop implementation
    for i in range(m):
        for j in range(p):
            total_sum = 0
            for k in range(n):
                total_sum += A[i, k] * B[k, j]
            C[i, j] = total_sum

    return C


def matrix_multiply_vectorized_3d(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """
    Part 7: Fully vectorized matrix multiplication using 3D broadcasting.
    Shapes:
      A[:, :, None] -> (m, n, 1)
      B[None, :, :] -> (1, n, p)
      Broadcast Product -> (m, n, p)
      Sum over axis=1 (n dimension) -> (m, p)
      
    Note: Creates temporary array of shape (m, n, p). High memory usage!
    Does NOT use @, np.matmul(), or np.dot().
    """
    m, n, p = validate_matrix_dimensions(A, B)

    # Check for excessive memory usage (> 500MB) before allocating 3D tensor
    element_count = m * n * p
    estimated_bytes = element_count * np.dtype(np.result_type(A.dtype, B.dtype)).itemsize
    if estimated_bytes > 500 * 1024 * 1024:  # 500 MB threshold
        raise MemoryError(
            f"3D broadcasting for shapes ({m}, {n}) and ({n}, {p}) requires "
            f"{estimated_bytes / (1024**2):.1f} MB temporary memory. Exceeds safe threshold."
        )

    # 3D Broadcasting & Summation
    expanded_A = A[:, :, np.newaxis]  # (m, n, 1)
    expanded_B = B[np.newaxis, :, :]  # (1, n, p)
    
    product_3d = expanded_A * expanded_B  # (m, n, p)
    C = np.sum(product_3d, axis=1)        # (m, p)

    return C


def matrix_multiply_vectorized_row(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """
    Part 4: Row-vectorized matrix multiplication (1 Python loop).
    Eliminates 2 Python loops by computing each row using 2D broadcasting & reduction:
      C[i, :] = sum(A[i, :, None] * B, axis=0)
      
    Does NOT use @, np.matmul(), or np.dot().
    """
    m, n, p = validate_matrix_dimensions(A, B)
    result_dtype = np.result_type(A.dtype, B.dtype)
    C = np.zeros((m, p), dtype=result_dtype)

    for i in range(m):
        # A[i, :, np.newaxis] has shape (n, 1)
        # B has shape (n, p)
        # A[i, :, None] * B broadcasts to (n, p)
        # np.sum(..., axis=0) sums across rows of B (n dimension) -> shape (p,)
        C[i, :] = np.sum(A[i, :, np.newaxis] * B, axis=0)

    return C


def matrix_multiply_tiled(A: np.ndarray, B: np.ndarray, block_size: int = 64) -> np.ndarray:
    """
    Part 8: Memory-aware tiled (block) matrix multiplication.
    Partitions matrices into smaller sub-blocks to fit into CPU L1/L2 cache
    and avoid memory overflow for larger matrices.
    
    Does NOT use @, np.matmul(), or np.dot().
    """
    m, n, p = validate_matrix_dimensions(A, B)
    result_dtype = np.result_type(A.dtype, B.dtype)
    C = np.zeros((m, p), dtype=result_dtype)

    # Process block tiles
    for i_block in range(0, m, block_size):
        i_end = min(i_block + block_size, m)
        for k_block in range(0, n, block_size):
            k_end = min(k_block + block_size, n)
            
            # Slice sub-block of A
            A_sub = A[i_block:i_end, k_block:k_end]  # shape (m_sub, n_sub)
            
            for j_block in range(0, p, block_size):
                j_end = min(j_block + block_size, p)
                
                # Slice sub-block of B
                B_sub = B[k_block:k_end, j_block:j_end]  # shape (n_sub, p_sub)
                
                # Compute block product using row vectorization
                # C_sub[i, :] += sum(A_sub[i, :, None] * B_sub, axis=0)
                for row_idx in range(A_sub.shape[0]):
                    row_a = A_sub[row_idx, :, np.newaxis]  # (n_sub, 1)
                    block_prod = np.sum(row_a * B_sub, axis=0)  # (p_sub,)
                    C[i_block + row_idx, j_block:j_end] += block_prod

    return C
