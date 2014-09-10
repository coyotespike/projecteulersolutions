"""
Returns the sum of the even-valued Fibonacci sequence terms <= 4,000,000
The first 10 terms of the Fibonacci sequence are: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89.

Of course, the list comprehension need not be constructed as a separate step, but may be constructed inside the sum().
"""

def fib_seq (number):

    fib_list = [1, 2]

    while fib_list[-1] < number:
        fib_list.append (fib_list[-1] + fib_list[-2])

    even_terms = [num for num in fib_list if num%2==0 and num <= number]
    even_terms_added = sum(even_terms)

    return even_terms_added

print fib_seq(4000000)

def calcE(number):
    """
    Someone else's solution, which mathematically I do not understand. Dollars to donuts it's faster than mine.
    """
    x = y = 1
    sum = 0
    while sum < number:
        sum += (x + y)
        x, y = x + 2 * y, 2 * x + 3 * y
    return sum

print calcE(4000000)

def fib(n):
    """
    I like this one. A little Python magic.
    """
#returns first # in Fib. sequence to have n digits

    a, b, = 1, 1
    g=[]

    while b < n:
        a, b = b, a+b
        if b % 2 == 0:
            g.append(b)
    print(sum(g))

fib(4000000)