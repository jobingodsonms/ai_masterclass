#ITER & NEXT
#An iterable is an object that you can loop through.
#An iterator is an object that remembers where it currently is in a sequence and gives you the next item when you ask for it.
#Python provides two important functions: iter() & next()

#1. Create an iterator from numpy import character

#from it and use next() to print the first three values.
numbers = [10, 20, 30, 40, 50]
it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))

#2. Use next() to print each character individually.
word = "PYTHON"
it = iter(word)
for char in word:
    print(next(it))

numbers = [5, 10, 15]
it= iter(numbers)
print(next(it))
print(next(it))
print(next(it))
print(next(it))  # This will raise StopIteration since there are no more items in the iterator.