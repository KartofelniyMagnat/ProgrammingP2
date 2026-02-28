"""
Python Iterators
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol,
which consist of the methods __iter__() and __next__().
"""

def squares_up_to(n):
    for i in range(1, n + 1):
        yield i * i

print("Squares up to N")
n = 5
for val in squares_up_to(n):
    print(val)


def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

print("\nEven numbers up to N ")
n = int(input("Enter N: "))
print(", ".join(str(x) for x in even_numbers(n)))


def divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

print("\nDivisible by 3 and 4 up to N=100")
for val in divisible_by_3_and_4(100):
    print(val)

def squares(a, b):
    for i in range(a, b + 1):
        yield i * i


print("\nSquares from A to B ")
a, b = 2, 6
for val in squares(a, b):
    print(val)

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

print("\nCountdown from N to 0 ")
for val in countdown(5):
    print(val)
