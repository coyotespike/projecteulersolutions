"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

There is, of course, a far more elegant solution which uses powers, given that the lowest common multiple of any set of numbers
must be composed of primes raised to a power, and the power of each primes must equal the highest power of the primes
composing each member in the set of numbers.
In other word 20 = 2^2 * 5^1, and 120 = 20 * 6 = (2^2 * 5^1) * (2^1 * 3^1)

For each prime less than or equal to our highest number, we want the highest power of the prime that won't make it larger
than our highest number. So for range(1, 21), for the prime number 2, we want 4, because 2^5 is larger than 20.

To understand the code below, I need to understand finding exponents with logarithms better. Later, perhaps.

from common import primeSieve (this code does not work and must be replaced by my own function)
from math import sqrt, log

def PE(N):
    primes=primeSieve(N+1) #returns list of all primes <=N
    sqrtN=sqrt(N)
    ans=1
    for p in primes:
        if p <= sqrtN:
            ans*=p**(int(log(N)/log(p)))
        else:
            ans*=p
    return ans

print PE(20)

    guess = 1
    for num in xrange(1, number+1):
        if num %2 != 0 and num%3 !=0:
            guess *= num
    guess *= 6
    print guess

Since my brute force solution looked like it would exhaust my computer's memory before completing, I devised this algorithm instead.
    # take each integer in the range and find its prime factors
    # for each prime factor, add as many to your list as in the integer with the greatest number of that factor
    # multiply each number in the resulting list together. This should be our target number

"""

# these two functions return the smallest even divisor of all the numbers multiplied together. Semantically incorrect!
def factorial(number):
    if number == 1:
        return 1

    else:
        return number * (factorial(number-1))

def smallest_even_divisor(number):
    number = factorial(number)
    # furthermore, the smallest even divisor would just be the number itself - so don't double the guess!
    guess = 2*number

    print "finished prep"

    while guess % number != 0:
        guess +=1

    return guess

def testfunction(testnum):
    # dividing by each number successively returns an incorrect result
    # therefore, the problem does not want the smallest divisor of all the numbers added together.
    for num in xrange(1, 11):
        testnum = testnum/num

    return testnum

testnum = float(2520)

def sqr_root (y):
    # This code finds the square root of a polynomial.
    epsilon = 0.01
    y = 24.0
    guess = y/2.0

    while abs(guess*guess - y) >= epsilon: #as long as it's not close enough: #this is also the test
        guess = guess - (((guess**2) - y)/(2*guess)) #here is the generation

    if (int(guess) - guess) < 0:
        guess +=1
    return int(guess)


def make_primes(number):
    """
    Returns a list of all primes below a given number
    """
    listofprimes = [2]
    starter = 3
    while starter <= number:
        if all (starter%num for num in listofprimes) != 0:
            listofprimes.append(starter)
        starter += 1

    return listofprimes

def even_divisor(number):
    counter = 0
    guess = number

    for num in make_primes(number):
        guess *= num
    print guess
    while any(guess % num for num in xrange(1, number+1)) !=0:
        guess += 1
        counter +=1
        if counter % 1000000 == 0:
            print counter

    return guess

#print even_divisor(10)


def find_prime_factors(number):
    """
    Takes: each integer in the range
    Returns: the number's prime factors
    """
    primefactors = []

    # take all the prime numbers up to the number's square root
    primes = make_primes(number)

    # as long as the number is not a prime
    while number not in primes and number != 1:
        # divide it by the prime numbers
        for num in primes:
            # it divides evenly, add the prime number to our list of factors
            if number%num == 0:
                # divide the number by a prime
                number = number/num
                # add the prime to a list
                primefactors.append(num)
        # the number has itself now been reduced to a prime, and must be added as well
    if number != 1:
        primefactors.append(number)
    return primefactors

def number_of_each_factor(rangenumber):

    prime_of_each = [find_prime_factors(num) for num in xrange(2, rangenumber+1)]
    primes = make_primes(rangenumber)
    tempholder = []
    # for each prime in the range,
    for num in primes:
        # count how many are in each list in prime_of_each
        range_of_each = (max([list.count(num) for list in prime_of_each]))
        # put as many primes into a list as are in the list with the greatest number
        tempholder.append ([num]*range_of_each)
    return tempholder

def factors_multiplied(number):
    """
    Takes: a number
    Returns: the smallest positive divisor of each number in the range of the original number
    """
    # get the list of the greatest number of prime factors for each number in range(targetnumber)
    greatest_number = number_of_each_factor(number)

    # flatten this list of lists into a single list
    factors_together = [item for sublist in greatest_number for item in sublist]

    # now multiply each prime together
    answer = reduce(lambda x, y: x*y, factors_together)

    # since any number is reducible to its primes, and the divisor must be evenly divisible by each dividend,
    # the target number is made up of as many primes as each dividend holds.
    return answer

#print factors_multiplied(1000)

from math import sqrt, log

def PE(N):
    primes= make_primes(N)
    sqrtN=sqrt(N)
    ans=1
    for p in primes:
        if p <= sqrtN:
            ans*=p**(int(log(N)/log(p)))
        else:
            ans*=p
    return ans

print PE(100000)