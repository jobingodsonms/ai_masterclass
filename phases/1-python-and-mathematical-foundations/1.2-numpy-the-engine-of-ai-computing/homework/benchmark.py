"""
Benchmarking Engine (benchmark.py)

Performance Benchmarking & Scalability Comparison:
Compares custom matrix multiplication algorithms against NumPy's C-optimized np.matmul()
across progressive matrix sizes up to 10,000 x 10,000.
"""

import time
import numpy as np
from matrix_engine import (
    matrix_multiply,
    matrix_multiply_vectorized_3d,
    matrix_multiply_vectorized_row,
    matrix_multiply_tiled,
    validate_matrix_dimensions
)


def benchmark_matrix_multiplication(sizes: list[int] = None) -> list[dict]:
    """
    Part 5 & 6: Progressive benchmarking across matrix sizes up to 10,000 x 10,000.
    
    Args:
        sizes: List of square matrix sizes to benchmark (e.g. [10, 50, 100, 250, 500, 1000, 2000, 5000, 10000]).
        
    Returns:
        List of dictionaries containing timing & correctness benchmark data per size.
    """
    if sizes is None:
        sizes = [10, 50, 100, 250, 500, 1000, 2000, 5000, 10000]

    benchmark_results = []

    print("=" * 105)
    print(f"{'MATRIX MULTIPLICATION ENGINE - BENCHMARK REPORT':^105}")
    print("=" * 105)
    header = (
        f"{'Size (NxN)':<12} | "
        f"{'Naive (Loop)':<14} | "
        f"{'3D Vector':<12} | "
        f"{'Row Vector':<12} | "
        f"{'Tiled':<12} | "
        f"{'NumPy (BLAS)':<14} | "
        f"{'Speedup (x)':<11} | "
        f"{'Correct':<7}"
    )
    print(header)
    print("-" * 105)

    for size in sizes:
        # Generate reproducible random float matrices for benchmarking
        np.random.seed(42)
        A = np.random.rand(size, size).astype(np.float64)
        B = np.random.rand(size, size).astype(np.float64)

        # 1. Always run NumPy's built-in np.matmul as baseline ground truth
        t0 = time.perf_counter()
        expected = np.matmul(A, B)
        numpy_time = time.perf_counter() - t0

        # Timing placeholders
        naive_time = None
        vec_3d_time = None
        vec_row_time = None
        tiled_time = None
        is_correct = True

        # --- Method 1: Naive Triple Loop (Only run for size <= 250 to avoid hours of execution) ---
        if size <= 250:
            t0 = time.perf_counter()
            res_naive = matrix_multiply(A, B)
            naive_time = time.perf_counter() - t0
            is_correct = is_correct and np.allclose(res_naive, expected)
        else:
            naive_time = float('nan')  # Skipped due to O(N^3) Python loop time

        # --- Method 2: 3D Broadcasting Vectorized (Only run for size <= 500 due to memory limits) ---
        if size <= 500:
            try:
                t0 = time.perf_counter()
                res_3d = matrix_multiply_vectorized_3d(A, B)
                vec_3d_time = time.perf_counter() - t0
                is_correct = is_correct and np.allclose(res_3d, expected)
            except MemoryError:
                vec_3d_time = float('nan')
        else:
            vec_3d_time = float('nan')  # Skipped due to multi-GB 3D array memory allocation

        # --- Method 3: Row Vectorized (Run for size <= 1000) ---
        if size <= 1000:
            t0 = time.perf_counter()
            res_row = matrix_multiply_vectorized_row(A, B)
            vec_row_time = time.perf_counter() - t0
            is_correct = is_correct and np.allclose(res_row, expected)
        else:
            vec_row_time = float('nan')  # Skipped for large matrices

        # --- Method 4: Tiled/Blocked Vectorized (Run for size <= 1000) ---
        if size <= 1000:
            t0 = time.perf_counter()
            res_tiled = matrix_multiply_tiled(A, B, block_size=64)
            tiled_time = time.perf_counter() - t0
            is_correct = is_correct and np.allclose(res_tiled, expected)
        else:
            tiled_time = float('nan')

        # Calculate best custom algorithm time for speedup comparison
        custom_times = [t for t in [vec_row_time, tiled_time, vec_3d_time, naive_time] if not np.isnan(t)]
        best_custom_time = min(custom_times) if custom_times else float('nan')
        speedup = (best_custom_time / numpy_time) if not np.isnan(best_custom_time) and numpy_time > 0 else float('nan')

        # Format helper
        def fmt_time(t):
            if np.isnan(t):
                return "N/A (Skipped)"
            elif t < 0.001:
                return f"{t * 1e6:.1f} us"
            elif t < 1.0:
                return f"{t * 1e3:.2f} ms"
            else:
                return f"{t:.3f} s"

        row_str = (
            f"{f'{size}x{size}':<12} | "
            f"{fmt_time(naive_time):<14} | "
            f"{fmt_time(vec_3d_time):<12} | "
            f"{fmt_time(vec_row_time):<12} | "
            f"{fmt_time(tiled_time):<12} | "
            f"{fmt_time(numpy_time):<14} | "
            f"{f'{speedup:.1f}x':<11} | "
            f"{'PASS' if is_correct else 'FAIL':<7}"
        )
        print(row_str)

        benchmark_results.append({
            "size": size,
            "naive_time": naive_time,
            "vec_3d_time": vec_3d_time,
            "vec_row_time": vec_row_time,
            "tiled_time": tiled_time,
            "numpy_time": numpy_time,
            "speedup": speedup,
            "correct": is_correct
        })

    print("-" * 105)
    return benchmark_results


if __name__ == "__main__":
    benchmark_matrix_multiplication()
