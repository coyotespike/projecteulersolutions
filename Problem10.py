"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

reduce (lambda x, y: x+y, listofprimes)
The answer here is: (1999993, 142913828922)

I have found a beautifully simple implementation of the sieve of Eratosthenes, and partly understood an implementation
(apparently very fast) of the Sieve of Sundaram.

"""

from math import sqrt
def make_primes(number):
    """
    Returns a list of all primes below a given number
    """
    listofprimes = [2]
    starter = 3
    result = 2

    while starter < number:
        if all (starter%num for num in listofprimes if num <= sqrt(starter)) != 0:
            listofprimes.append(starter)
            result += starter
        starter += 2

    return listofprimes[-1], result

def Euler_version (number):
    marked = [0] * number
    value = 3
    s = 2
    while value < number:
        if marked[value] == 0:
            s += value
            i = value
            while i < number:
                marked[i] = 1
                i += value
        value += 2
    return s

def primes(n): # Sieve of Eratosthenes
    prime, sieve = [], set()
    for q in xrange(2, n+1):
        if q not in sieve:
            prime.append(q)
            sieve.update(range(q*q, n+1, q))
    return prime

# Apparently this is the fasted stackoverflow has found, based on the sieve of Sundaram
def sundaram3(max_n):
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)