"""
Lambda Functions - Topic File

Structure:
1. Concept (What it is)
2. Why AI engineers use it
3. Syntax
4. Example
5. Mini Practice (with solutions)
6. Assignments (solutions included)

This file follows the learning template and provides runnable examples.
"""

# 1. Concept (What it is)
# Small anonymous functions written in a single expression with `lambda`.

# 2. Why AI engineers use it
# - Inline short callbacks (sorting, mapping)
# - Quick one-off small functions in pipelines

# 3. Syntax
# lambda arguments: expression

# 4. Example
add = lambda a, b: a + b
print('Example add(3,5) ->', add(3,5))

# 5. Mini Practice (with solutions)
# 1. lambda that returns x + 10
mp1 = (lambda x: x + 10)(5)
print('\nMini Practice 1 ->', mp1)  # 15

# 2. lambda for maximum of two numbers
max_two = lambda a, b: a if a > b else b
print('Mini Practice 2 ->', max_two(7,3))  # 7

# 3. lambda that checks if a number is even
is_even = lambda x: x % 2 == 0
print('Mini Practice 3 ->', is_even(4), is_even(5))  # True False

# 4. lambda in sorted() to sort by second value
pairs = [(1,'b'), (2,'a'), (3,'c')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print('Mini Practice 4 ->', sorted_pairs)

# 5. lambda that returns last character of a word (robust)
last_char = lambda s: s[-1] if s else ''
print('Mini Practice 5 ->', last_char('python'), last_char('ai'), last_char(''))

# 6. Additional: map with lambda
print('Mini Practice 6 ->', list(map(lambda x: x*2, [1,2,3])))

# 6. Assignments (solutions)
# Rule: No Google/AI. Use only Python docs, notes, and experiments.

# Assignment 1: grading lambda
grade = lambda m: 'A' if m >= 90 else ('B' if m >= 75 else ('C' if m >= 50 else 'F'))
print('\nAssignment 1 ->', grade(95), grade(82), grade(67), grade(40))

# Assignment 2: sort by age
people = [('alice', 29), ('bob', 23), ('carol', 31)]
sorted_by_age = sorted(people, key=lambda x: x[1])
print('Assignment 2 ->', sorted_by_age)

# Assignment 3: last character lambda
last = lambda s: s[-1] if s else None
print('Assignment 3 ->', last('python'), last('ai'), last(''))
