# Part 1.1 — Assignments: Python for AI (Foundations)

**Rule:** No Google / AI tools. Use only the official Python docs, your notes, and your own coding experiments.

---

## 1. List Comprehensions — Assignments

1. Create a list of the first 50 squares, remove all odd squares using a list comprehension, convert the remaining numbers to strings, and print the final list. (End result: a list of stringified even squares.)

2. Convert `temps_c = [0, 20, 37, 100]` to Fahrenheit using a single list comprehension. Show the resulting list.

3. From `sentences = [" AI is fun ", "","Python  ", "  data"]`, produce a cleaned list of lowercase words (trim whitespace and remove empties) using list comprehension(s) only.

4. Build a list of prime numbers from 1..100 using list comprehension(s). You may write helper functions, but the final list should be constructed with a list comprehension.

---

## 2. Lambda Functions — Assignments

1. Implement a lambda-based grading function that returns:
   - "A" if marks ≥ 90
   - "B" if marks ≥ 75
   - "C" if marks ≥ 50
   - "F" otherwise

   Show example outputs for marks: 95, 82, 67, 40.

2. Using `lambda` and `sorted()`, sort the list `[("alice", 29), ("bob", 23), ("carol", 31)]` by age (second element). Show the sorted list.

3. Create a lambda that, given a string, returns its last character. Demonstrate on `"python"`, `"ai"`, and an empty string (handle empty robustly).

---

## 3. map(), filter(), reduce() — Assignments

1. Given `numbers = list(range(1, 11))`, use `map()` to produce a list of their squares.

2. Use `filter()` to keep only numbers divisible by 3 from the squared list.

3. Use `functools.reduce()` to compute the sum of the filtered numbers.

4. Chain the operations: square every number, keep only even squares, then compute the sum of the remaining numbers. Provide the intermediate lists and final result.

---

## 4. Iterators — Assignments

1. Create an iterator from the list `[10, 20, 30, 40, 50]` and print the first three values using `next()`.

2. From the string `"PYTHON"`, create an iterator and print each character one-by-one using `next()` in a loop that handles `StopIteration` gracefully.

3. Implement a custom iterator class `CountDown(n)` that yields `n, n-1, ..., 1`. Demonstrate it with `n=5` and show usage with both `next()` and a `for` loop.

---

## 5. Generators — Assignments

1. Write a generator `evens(n)` that yields the first `n` even numbers. Demonstrate for `n=5`.

2. Implement a generator `read_lines(path)` that yields lines from a text file one at a time. Create a small sample text file and show reading three lines.

3. Write a generator expression (not a full `def`) that produces cubes for `0..9` and convert it to a list. Explain briefly (in comments) the type/behavior difference between the generator expression and a list.

---

## 6. Decorators — Assignments

1. Create a decorator `@log_call` that prints `Calling <func_name>` before the call and `Finished <func_name>` after. Apply it to a sample function and show output.

2. Build a `@timer` decorator that measures execution time (use `time.time()`), prints the elapsed time, and returns the original function's result. Demonstrate on a function that sleeps for ~0.5s.

3. Create a decorator `@count_calls` that tracks how many times a function was called. Use it on two functions and show independent counts.

---

## 7. Context Managers - Assignments

1. File Handling
Create a text file called data.txt using a with statement and:
Write 3 lines of text into it.
Then open it again using with and read the contents.
Print the contents.

2. Create a context manager called FileProcessor that:

Opening file...
Processing file...
Closing file...

automatically.

Use it like:

with FileProcessor("data.txt") as file:
    data = file.read()



## Submission notes

- For each assignment, include a small example script or a short code cell demonstrating your solution and the output. Keep solutions in the same folder and name files clearly (e.g., `list_comprehensions_solution.py`).
- Add brief comments documenting your approach and any edge cases handled.
- Respect the rule: no external AI/Google — the goal is to practice and learn through your own coding and the Python docs.

Good luck — paste here if you want quick review or unit tests for any solution.
