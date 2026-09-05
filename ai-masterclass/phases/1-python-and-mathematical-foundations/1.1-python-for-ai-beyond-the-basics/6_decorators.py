"""
Decorators - Topic File

Provides decorator examples, mini practice solutions, and assignment solutions.
"""
import time
from functools import wraps

# Example decorator
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print('Before')
        result = func(*args, **kwargs)
        print('After')
        return result
    return wrapper

@simple_decorator
def greet(name):
    print(f'Hello, {name}')

print('\nDecorator example ->')
greet('Jerin')

# Mini Practice solutions
# 1. decorator that prints 'Function started' before execution
def started_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Function started')
        return func(*args, **kwargs)
    return wrapper

@started_decorator
def add(a,b):
    return a+b

print('\nMini Practice 1 ->', add(2,3))

# 2. decorator that prints 'Function ended' after execution
def ended_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('Function ended')
        return result
    return wrapper

@ended_decorator
def mul(a,b):
    return a*b

print('Mini Practice 2 ->', mul(3,4))

# 3. decorator that counts calls
def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"{func.__name__} call #{wrapper.calls}")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_calls
def f1():
    return 'f1'

@count_calls
def f2():
    return 'f2'

f1(); f1(); f2(); f1()

# 4. timer decorator
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f}s")
        return result
    return wrapper

@timer
def sleepy():
    time.sleep(0.5)
    return 'done'

print('\nMini Practice 5 ->', sleepy())

# Assignments (solutions)
# 1. @log_call decorator
def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        res = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return res
    return wrapper

@log_call
def sample(x):
    return x*2

print('\nAssignment 1 ->', sample(5))

# 2. @timer decorator demonstrated above on sleepy()
print('Assignment 2 ->')
sleepy()

# 3. @count_calls demonstrated above with f1 and f2
print('Assignment 3 -> f1 calls:', f1.calls, 'f2 calls:', f2.calls)
