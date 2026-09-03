#Original List
  #    │
 #     ▼
 #map()     → Transform every item
 #filter()  → Keep only selected items
 #reduce()  → Combine all items into one result

#________________________________________________________________

1. Map: Applies a function to every item in an iterable and returns a new iterable with the results.
#map() applies the same function to every element in an iterable.
Syntax: map(function, iterable)
#numbers = [1, 2, 3, 4, 5]
#squares = list(map(lambda x: x**2, numbers))
#print(squares)

#________________________________________________________________

2. Filter: Filters items from numpy import single

from an iterable based on a condition.
#filter() removes items that don't satisfy a condition.
Syntax: filter(function, iterable)

#numbers = [1, 2, 3, 4, 5]
#even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
#print(even_numbers)

#________________________________________________________________

3. Reduce: Reduces the iterable to a single value.
#reduce() combines all elements into one final value.
Syntax: reduce(function, iterable)

#from functools import reduce
#numbers = [2,3,4]
#product = reduce(lambda a, b: a * b, numbers)
#print(product)

#________________________________________________________________
#________________________________________________________________

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mapped = list(map(lambda x:x**2, numbers))
filtered = list(filter(lambda x:x%3==0, mapped))
total = reduce(lambda a,b:a+b, filtered)
