A list comprehension is a shorter and more Pythonic way to create lists.
Instead of writing multiple lines of code, you can write everything in one line.

  
NORMAL WAY:

numbers = []
for i in range(5):
    numbers.append(i)
print(numbers)

LIST COMPREHENSION:
syntax: new_list = [expression for item in iterable]


Mini Practice:
1. Create a list of numbers from 1 to 50
#list=[i for i in range(1,51)]
#print(list) 

2.Create a list of cubes from 1 to 10.
#list=[i*i*i for i in range(10)]
#print(list)

3.Create a list of only odd numbers from 1 to 30.
#list=[i for i in range(30) if i%2==1]
#print(list)

4. Uppercase every word.
#list=["apple","banana","cherry"]
#res=[lis.upper() for lis in list]
#print(res)

5. if...else inside List Comprehension
#list=[12,25,8,31,40]
#pas=[ "pass" if lis>=20 else "fail" for lis in list]
#print(pas)


Assignment:

1.Create a list of the first 50 squares.
2.Remove all odd numbers using a list comprehension.
3.Convert all remaining numbers into strings.
4.Print the final list.

list=[i*i for i in range(1,51)]

l2 = [i for i in list if i % 2 == 1]

l3 = [str(i) for i in l2]
print(l3)
