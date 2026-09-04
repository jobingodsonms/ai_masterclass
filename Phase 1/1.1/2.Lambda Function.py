A lambda function is an anonymous (unnamed) function that is written in a single line.

NORMAL WAY:
def square(x):
  return x * x

LAMBDA FUCNTION:
square = lambda x: x * x

syntax: lambda parameters: expression


Mini Practice:

1. if number greater (return True or false)
#pos = lambda a: a > 0
#print(pos(5))  

2. greates of two numbers
#maxi = lambda a,b: a if a > b else b
#print(maxi(5,10))

3. pass or fail 
#res = lambda a: "pass" if a > 50 else "fail"
#print(res(60))

4. Checking whether a year is a leap year (return True or False)
#year = lambda a: "leap year" if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0) else "not leap year"
#print(year(2020))

5. Returning the longest of three strings.
#longest = lambda first, second, third: first if len(first) > len(second) and len(first) > len(third) else second if len(second) > len(third) else third#
#print(longest("apple", "banana", "kiwi"))

ASSIGNMENT:

1. Returning the grade:
"A" if marks ≥ 90
"B" if marks ≥ 75
"C" if marks ≥ 50
"F" otherwise

#grade= lambda marks: "A" if marks >= 90 else "B" if marks >= 80 else "C" if marks >= 70 else "D" if marks >= 60 else "F"
#print(grade(85))
