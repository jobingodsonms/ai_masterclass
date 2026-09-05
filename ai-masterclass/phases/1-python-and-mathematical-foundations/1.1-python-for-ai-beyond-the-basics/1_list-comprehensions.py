"""
List Comprehensions - Topic File

Structure:
1. Concept (What it is)
2. Why AI engineers use it
3. Syntax
4. Example
5. Mini Practice (all mini practice with solutions)
6. Assignments (solutions included)

This file follows the learning template and provides runnable examples.
"""

# 1. Concept (What it is)
# A list comprehension provides a concise way to build lists from iterables.
# It combines a for-loop and optional condition into a single expression.

# 2. Why AI engineers use it
# - Quick feature transforms
# - Compact filtering and mapping
# - Readable, expressive preprocessing steps

# 3. Syntax
# [expression for item in iterable if condition]

# 4. Example (runnable)
numbers = [1, 2, 3, 4, 5, 6]
squares = [n**2 for n in numbers]
even_squares = [n**2 for n in numbers if n % 2 == 0]
labels = [f"{n}-even" if n % 2 == 0 else f"{n}-odd" for n in numbers]

print('Example -> squares:', squares)
print('Example -> even_squares:', even_squares)
print('Example -> labels:', labels)

# 5. Mini Practice (all mini practice for this topic) + Solutions
# 1. From [1,2,3,4,5,6], create a list of squares.
mp1 = [i*i for i in [1,2,3,4,5,6]]
print('\nMini Practice 1 ->', mp1)  # [1,4,9,16,25,36]

# 2. From [1,2,3,4,5,6], create squares of only odd numbers.
mp2 = [i*i for i in [1,2,3,4,5,6] if i % 2 == 1]
print('Mini Practice 2 ->', mp2)  # [1,9,25]

# 3. Convert ["ai","ml","python"] to uppercase in one line.
mp3 = [w.upper() for w in ["ai","ml","python"]]
print('Mini Practice 3 ->', mp3)  # ['AI','ML','PYTHON']

# 4. From ["apple","","banana"," ","grape"], keep only non-empty trimmed strings.
raw = ["apple","","banana"," ","grape"]
mp4 = [s.strip() for s in raw if s.strip()]
print('Mini Practice 4 ->', mp4)  # ['apple','banana','grape']

# 5. Create (x, x**2) pairs for x in range(5).
mp5 = [(x, x**2) for x in range(5)]
print('Mini Practice 5 ->', mp5)  # [(0,0),(1,1),(2,4),(3,9),(4,16)]

# 6. Additional small practice: map numbers to parity strings.
mp6 = ["even" if n % 2 == 0 else "odd" for n in range(1,11)]
print('Mini Practice 6 ->', mp6)

# 6. Assignments (solutions included)
# Rule: No Google/AI. Use only Python docs, notes, and experiments.

# Assignment 1:
# Create a list of the first 50 squares, remove all odd squares, convert remaining numbers to strings, print final list.
squares50 = [i*i for i in range(1,51)]
# remove odd squares -> keep even squares
even_squares50 = [s for s in squares50 if s % 2 == 0]
# convert to strings
even_str = [str(s) for s in even_squares50]
print('\nAssignment 1 -> count:', len(even_str), 'sample:', even_str[:10])

# Assignment 2:
# Convert temps_c to Fahrenheit using one comprehension.
temps_c = [0, 20, 37, 100]
temps_f = [round((c * 9/5) + 32, 2) for c in temps_c]
print('Assignment 2 ->', temps_f)

# Assignment 3:
# Clean sentences list to trimmed lowercase words, remove empties.
sentences = [" AI is fun ", "","Python  ", "  data"]
clean_words = [s.strip().lower() for s in sentences if s.strip()]
print('Assignment 3 ->', clean_words)

# Assignment 4:
# Build list of prime numbers from 1..100 using list comprehension (helper allowed).
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

primes_1_100 = [n for n in range(1, 101) if is_prime(n)]
print('Assignment 4 -> primes count:', len(primes_1_100), 'primes sample:', primes_1_100[:10])
