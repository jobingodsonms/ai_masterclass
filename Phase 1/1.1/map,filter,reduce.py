#Original List
  #    │
 #     ▼
 #map()     → Transform every item
 #filter()  → Keep only selected items
 #reduce()  → Combine all items into one result

#________________________________________________________________

#map() applies the same function to every element in an iterable.
#map(function, iterable)
#numbers = [1, 2, 3, 4, 5]
#squares = list(map(lambda x: x**2, numbers))
#print(squares)

#________________________________________________________________

#filter() removes items that don't satisfy a condition.
#filter(function, iterable)
#numbers = [1, 2, 3, 4, 5]
#even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
#print(even_numbers)

#________________________________________________________________

#reduce() combines all elements into one final value.
#reduce(function, iterable)
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
