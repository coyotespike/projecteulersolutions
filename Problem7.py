"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

Again, if all the prime numbers less than the square root of a number are not factors of the number, then we can be sure
that there is no prime number greater than the square root of the number which is also a factor of the number.
"""
from math import sqrt
def make_primes(number):
    """
    Returns a list of all primes below a given number
    """
    listofprimes = [2]
    starter = 3
    while len(listofprimes) < number:
        if all (starter%num for num in listofprimes if num <= sqrt(starter)) != 0:
            listofprimes.append(starter)
        starter += 2

    return "The length of the list of primes is " + str(len(listofprimes)) + ", and" \
                                                                             " the " + str(number) + "st prime number is " + str(listofprimes[-1]) + "."

print make_primes(10001)