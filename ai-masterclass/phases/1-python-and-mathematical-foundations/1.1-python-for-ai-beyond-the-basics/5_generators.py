"""
Generators - Topic File

Includes examples, mini practice solutions, and assignment solutions.
"""

# Simple generator yielding numbers 1..5
def numbers_gen(n=5):
    for i in range(1, n+1):
        yield i

print('\nGenerator example ->', list(numbers_gen(5)))

# Mini Practice solutions
# 1. generator evens(n)
def evens(n):
    i = 0
    count = 0
    while count < n:
        yield i
        i += 2
        count += 1

print('Mini Practice 1 ->', list(evens(5)))

# 2. read_lines(path) generator (create sample file first)
sample_path = 'sample_text.txt'
with open(sample_path, 'w', encoding='utf8') as f:
    f.write('Line1\nLine2\nLine3\nLine4\n')

def read_lines(path):
    with open(path, 'r', encoding='utf8') as f:
        for line in f:
            yield line.rstrip('\n')

print('Mini Practice 2 -> first three lines:')
rg = read_lines(sample_path)
print(next(rg))
print(next(rg))
print(next(rg))

# 3. generator expression for cubes 0..9
gen_expr = (i**3 for i in range(10))
print('Mini Practice 3 -> type:', type(gen_expr), 'converted to list length:', len(list(gen_expr)))

# Assignments (solutions)
# 1. evens(n) demonstrated above
print('\nAssignment 1 ->', list(evens(5)))

# 2. read_lines(path) already used to read 3 lines
print('Assignment 2 -> read three lines into list:', [line for _, line in zip(range(3), read_lines(sample_path))])

# 3. generator expression vs list: generator yields items lazily; list comprehension builds full list
gexpr = (i**3 for i in range(10))
lcomp = [i**3 for i in range(10)]
print('Assignment 3 -> generator type:', type(gexpr), 'list type:', type(lcomp))
