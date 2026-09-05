"""
Map, Filter, Reduce - Topic File

Structure: Concept, Why, Syntax, Example, Mini Practice (solutions), Assignments (solutions)
"""

from functools import reduce

# 1. Concept
# map: transform each item; filter: keep items matching condition; reduce: aggregate to single value

# 2. Why AI engineers use it
# functional pipelines for preprocessing and aggregation

# 3. Syntax examples and 4. Example
numbers = list(range(1, 11))
print('\nExample numbers ->', numbers)

# Map: squares
squares = list(map(lambda x: x**2, numbers))
print('Example squares ->', squares)

# Filter: divisible by 3
div_by_3 = list(filter(lambda x: x % 3 == 0, squares))
print('Example divisible by 3 (from squares) ->', div_by_3)

# Reduce: sum of numbers
total = reduce(lambda a, b: a + b, numbers)
print('Example total ->', total)

# Mini Practice solutions
mp1 = list(map(lambda x: x**2, numbers))
mp2 = list(map(int, ['10','20','30']))
mp3 = list(filter(lambda x: x > 5, [2,6,1,8,4]))
mp4 = list(filter(lambda w: w.startswith('a'), ['ai','bot','agent','ml']))
mp5 = reduce(lambda a,b: a+b, [1,2,3,4,5])
mp6 = reduce(lambda a,b: a if a > b else b, [3,7,2,9,5])
print('\nMini Practice map/filter/reduce ->', mp1, mp2, mp3, mp4, mp5, mp6)

# Assignment solutions
# 1. squares (map)
squares_map = list(map(lambda x: x**2, numbers))
print('\nAssignment 1 -> squares_map sample', squares_map[:5])

# 2. keep numbers divisible by 3 from squared list
filtered = list(filter(lambda x: x % 3 == 0, squares_map))
print('Assignment 2 -> filtered sample', filtered[:5])

# 3. reduce to compute sum
sum_filtered = reduce(lambda a,b: a + b, filtered) if filtered else 0
print('Assignment 3 -> sum_filtered', sum_filtered)

# 4. Chain: square -> keep even squares -> sum
even_squares = list(filter(lambda x: x % 2 == 0, map(lambda x: x**2, numbers)))
sum_even_squares = reduce(lambda a,b: a + b, even_squares) if even_squares else 0
print('Assignment 4 -> even_squares', even_squares)
print('Assignment 4 -> sum_even_squares', sum_even_squares)
