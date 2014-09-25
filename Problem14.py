"""
The Collatz sequence:

n --> n/2 (n is even)
n --> 3n + 1 (n is odd)

Which starting number, under one million, produces the longest chain?

Attempting brute force test. Try every number in the range.

Common way to optimize: store number, counter pairs in a dictionary. If the number changes into one already in the
dictionary, stop testing - just add the value to the counter as it stands. In other words, memoize the solution.
"""

def collatz(number):
    num = number
    counter = 1
    while num != 1:
        if num%2 == 0:
            num = num/2
            counter +=1
        elif num%2 != 0:
            num = (3*num+1)
            counter+=1

    if counter >= 525:
        print counter, number

    return counter

#print max([collatz(number) for number in reversed(range(10**4, 10**6))])

def collatz2(number):
    num = number
    counter = 1
    while num != 1:
        if num%2 == 0:
            num = num/2
            counter +=1
        elif num%2 != 0:
            num = (3*num+1)
            counter+=1

    if counter >= 525:
        print counter, number

    return counter

#print max([collatz(number) for number in reversed(range(10**4, 10**6))])