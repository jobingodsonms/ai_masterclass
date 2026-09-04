##yield means: "Give this value now, but remember where I stopped so I can continue later."

#def count():
#    for i in range(1, 6):
#        yield i

#for numbers in count():
#    print(numbers)

def test():
    print("Starting")
    yield 10
    print("Middle")
    yield 20
    print("Ending")
    yield 30

x = test()
print(next(x))
print(next(x))
print(next(x))