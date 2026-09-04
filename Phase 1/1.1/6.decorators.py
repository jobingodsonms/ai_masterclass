#A decorator allows you to add extra functionality to an existing function without changing the function's original code.

#def greet():
#    print("Hello")

#def decorator(function):

#    def wrapper():
#        print("Starting function")

#        function()

#       print("Function finished")

#    return wrapper
#new_greet = decorator(greet)
#new_greet()
#________________________________________________________

#*args handles positional arguments.
#Example:
#add(10, 20)
#args receives:(10, 20)

#**kwargs handles keyword arguments.
#Example:
#add(a=10, b=20)
#kwargs receives:{"a": 10, "b": 20}

#_______________________________________________

#import time

#def timer(func):

   # def wrapper(*args, **kwargs):

     #   start = time.time()

    #    result = func(*args, **kwargs)

   #     end = time.time()

  #      print(f"{func.__name__} took {end - start:.4f} seconds")

 #       return result

 #   return wrapper

#@timer
#def calculate():
 #   time.sleep(2)
 #   print("Calculation complete")

#calculate()

#_________________________________________________________
#EXECRICE 

def decorator(func):
    def wrapper(*args, **kwargs):
        print(func.__name__ + " this is the name of the function ")
        func(*args, **kwargs)
        print("After the function is called.")
    return wrapper

@decorator
def function( a,b,c):
    print(a+b+c)

function(3,4,5)

