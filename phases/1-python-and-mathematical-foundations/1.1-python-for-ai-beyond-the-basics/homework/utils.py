"""Reusable helpers for the text-processing pipeline."""

from functools import wraps
from pathlib import Path
from time import perf_counter

def timer(function):
	"""Report how long a function takes and return its result."""
	@wraps(function)
	def timed_function(*args, **kwargs):
		start_time = perf_counter()
		result = function(*args, **kwargs)
		elapsed = perf_counter() - start_time
		print(f"{function.__name__} completed in {elapsed:.4f} seconds")
		return result

	return timed_function

def save_results(content, filename):
	"""Write result content to a UTF-8 text file."""
	output_path = Path(filename)
	output_path.parent.mkdir(parents=True, exist_ok=True)
	with output_path.open("w", encoding="utf-8") as file:
		file.write(content)
