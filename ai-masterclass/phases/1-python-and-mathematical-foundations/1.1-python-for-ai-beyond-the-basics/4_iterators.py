"""
Iterators - Topic File

Contains concept, examples, mini practice solutions, and assignments with solutions.
"""

# Example: iter() and next()
nums = [10, 20, 30, 40, 50]
it = iter(nums)
print('\nIterator example next() ->', next(it), next(it), next(it))

# Print characters individually using next()
word = 'PYTHON'
itw = iter(word)
print('Iterator example chars ->', end=' ')
try:
    while True:
        ch = next(itw)
        print(ch, end=' ')
except StopIteration:
    print('\nDone with string iteration')

# Mini Practice solutions
# 1. Create iterator and print first three values
it2 = iter([5,10,15,20])
print('\nMini Practice 1 ->', next(it2), next(it2), next(it2))

# 2. Print all items manually handling StopIteration
it3 = iter([1,2])
while True:
    try:
        print('mp2 next ->', next(it3))
    except StopIteration:
        break

# 3. Custom iterator CountDown
class CountDown:
    def __init__(self, n):
        self.current = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

print('\nMini Practice 3 -> CountDown using next():')
cd = CountDown(5)
print(next(cd), next(cd))
print('CountDown with for loop ->', end=' ')
for x in CountDown(5):
    print(x, end=' ')
print('\n')

# Assignments (solutions)
# 1. iterator first three values
it4 = iter([10,20,30,40,50])
print('Assignment 1 ->', next(it4), next(it4), next(it4))

# 2. iterator over string with StopIteration handling
itstr = iter('PYTHON')
try:
    while True:
        print(next(itstr), end=' ')
except StopIteration:
    print('\nAssignment 2 done')

# 3. CountDown demonstrated above
print('Assignment 3 ->', list(CountDown(5)))
