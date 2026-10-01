"""
Matrix Multiplication Engine - Main Test Suite (main.py)

Executes:
1. Small matrix sanity test (Part 2)
2. Incompatible dimension error handling (Part 3)
3. Correctness verification across all 4 custom implementations (Part 4, 7, 8)
4. Progressive benchmark suite up to 10,000 x 10,000 (Part 5 & 6)
5. Final concept checklist verification summary
"""

import sys
import numpy as np

from matrix_engine import (
    matrix_multiply,
    matrix_multiply_vectorized_3d,
    matrix_multiply_vectorized_row,
    matrix_multiply_tiled,
    validate_matrix_dimensions
)
from benchmark import benchmark_matrix_multiplication


def run_unit_tests():
    """Runs all functional unit tests and validation checks."""
    print("=" * 80)
    print("1. RUNNING PART 2 - SMALL MATRIX TEST")
    print("=" * 80)

    A_test = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])
    B_test = np.array([
        [7, 8],
        [9, 10],
        [11, 12]
    ])

    expected_output = np.array([
        [58, 64],
        [139, 154]
    ])

    # Test custom naive triple loop
    res_naive = matrix_multiply(A_test, B_test)
    res_3d = matrix_multiply_vectorized_3d(A_test, B_test)
    res_row = matrix_multiply_vectorized_row(A_test, B_test)
    res_tiled = matrix_multiply_tiled(A_test, B_test)

    expected_matmul = np.matmul(A_test, B_test)

    print("Input A (2x3):\n", A_test)
    print("Input B (3x2):\n", B_test)
    print("\nCustom Output (naive):\n", res_naive)
    print("Expected Output:\n", expected_output)

    assert np.array_equal(res_naive, expected_output), "Part 2 naive implementation output failed!"
    assert np.array_equal(res_3d, expected_output), "Part 2 3D vectorized output failed!"
    assert np.array_equal(res_row, expected_output), "Part 2 row vectorized output failed!"
    assert np.array_equal(res_tiled, expected_output), "Part 2 tiled output failed!"
    assert np.array_equal(res_naive, expected_matmul), "Matches np.matmul ground truth!"

    print("\n[SUCCESS] Part 2 Small Matrix Test Passed across all custom algorithms!")

    print("\n" + "=" * 80)
    print("2. RUNNING PART 3 - INVALID SHAPE ERROR HANDLING TEST")
    print("=" * 80)

    A_invalid = np.array([[1, 2, 3], [4, 5, 6]])  # shape (2, 3)
    B_invalid = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])  # shape (2, 4)

    try:
        matrix_multiply(A_invalid, B_invalid)
        print("[FAIL] Failed to raise ValueError for incompatible shapes (2, 3) and (2, 4)")
        sys.exit(1)
    except ValueError as e:
        print(f"[SUCCESS] Correctly caught ValueError: {e}")

    print("\n" + "=" * 80)
    print("3. ALGORITHM CORRECTNESS CHECK (RANDOM MATRICES)")
    print("=" * 80)

    np.random.seed(123)
    A_rand = np.random.randint(1, 20, size=(50, 40))
    B_rand = np.random.randint(1, 20, size=(40, 30))

    ground_truth = np.matmul(A_rand, B_rand)

    check_naive = matrix_multiply(A_rand, B_rand)
    check_3d = matrix_multiply_vectorized_3d(A_rand, B_rand)
    check_row = matrix_multiply_vectorized_row(A_rand, B_rand)
    check_tiled = matrix_multiply_tiled(A_rand, B_rand, block_size=16)

    assert np.array_equal(check_naive, ground_truth), "Naive algorithm failed on 50x40 @ 40x30!"
    assert np.array_equal(check_3d, ground_truth), "3D vectorized algorithm failed on 50x40 @ 40x30!"
    assert np.array_equal(check_row, ground_truth), "Row vectorized algorithm failed on 50x40 @ 40x30!"
    assert np.array_equal(check_tiled, ground_truth), "Tiled algorithm failed on 50x40 @ 40x30!"

    print("[SUCCESS] All 4 matrix multiplication algorithms produced 100% identical outputs to np.matmul()!")


def print_final_checklist():
    """Prints the checklist summary explaining core NumPy concepts learned."""
    checklist_text = """
================================================================================
FINAL NUMPY CONCEPTS CHECKLIST
================================================================================
1. Arrays & Data Structures:
   - ndarray: High-performance contiguous C memory array with uniform dtypes.
   - shape & ndim: Tuple describing array dimensions (e.g. (2, 3)) and axis count.
   - dtype: Numerical data type (int32, float64) governing byte representation.

2. Manipulation & Indexing:
   - Slicing: Zero-copy views into sub-matrices (e.g., A[i_block:i_end, :]).
   - New Axes: Adding virtual dimensions using np.newaxis or None for broadcasting.

3. Vectorization & Broadcasting:
   - Vectorization: Replacing explicit Python loops with C-level array iterations.
   - Broadcasting: Expanding smaller or 1D/2D arrays across larger dimensions.
   - 3D Broadcasting: A[:, :, None] (m, n, 1) * B[None, :, :] (1, n, p) -> (m, n, p).

4. Memory & Performance Insights:
   - Naive Python Loop Overhead: O(N^3) scalar indexing in Python carries high interpreter latency.
   - 3D Temporary Memory Costs: Creating (M, N, P) tensors requires O(N^3) memory allocation.
     At 10,000 x 10,000, a single 3D tensor requires ~800 GB of RAM!
   - BLAS / LAPACK Optimization: NumPy's np.matmul() utilizes compiled, multi-threaded C/Fortran
     BLAS kernels with CPU L1/L2 cache tiling and SIMD vector instructions.
================================================================================
"""
    print(checklist_text)


def main():
    # 1. Run Functional Tests
    run_unit_tests()

    # 2. Run Benchmarking Suite
    print("\n" + "=" * 80)
    print("4. RUNNING PROGRESSIVE BENCHMARK SUITE UP TO 10,000 x 10,000")
    print("=" * 80)
    benchmark_matrix_multiplication(sizes=[10, 50, 100, 250, 500, 1000, 2000, 5000, 10000])

    # 3. Print Final Checklist Summary
    print_final_checklist()


if __name__ == "__main__":
    main()
