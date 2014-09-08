"""
Finds the sum of all the multiples of 3 or 5 below 1000.

"""

def multiple_3_or_5 (number):
    """
    this implementation initalizes a counter variable and uses a simple for-loop
    """
    result = 0
    for n in range(number):
        if (n % 3==0) or (n % 5==0):
            result += n
    return result

def second_multiple_3_or_5 (number):
    """
    this implementation uses a list comprehension and the built-in function sum()
    """
    listrange = [num for num in range(number) if num%3==0 or num%5==0]
    return sum(listrange)

print multiple_3_or_5(1000)
print second_multiple_3_or_5(1000)