"""
The difference between the sum of the squares of the first ten natural numbers and the square of the sum
is 3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

the sum up to any number n is : n(n+1)/2
the sum of squares up to any number is: (n/6)(2n+1)(n+1)

You can find this sum of squares formula by a simple and beautiful method called finite differences.
For any series of numbers, make a list of the differences between them. Then make a list of the differences between
the differences. When these differences equal each other, that depth of the list is equal to the highest degree of
the polynomial equation which produced the series.
For, instance, the differences between [-3, 2, 13, 30, 53] are [5, 11, 17, 23], and the differences between those are
[6, 6, 6]:

     -3    2    13    30    53
         5   11    17    23
           6     6     6
Therefore the equation must be of the form an^2 + bn + c. Next, if we know that when n=1 the formula works out
to the first number in the series, -3, we can just substitute different values of to get a system of equations.
If n =1, a + b + c = -3
If n=2 4a + 2b + c = 2
If n=3, 9a + 3b + c = 13

These are easy to solve, and tell us what a, b, and c are. Here, the finite differences method easily finds the sum
of squares formula.


"""

def square_difference (number):

    return abs(sum([num**2 for num in range(number+1)]) - (sum(range(number+1))**2))

print square_difference(100)

def math_diff (number):
    return (((number*(number+1))/2)**2 - ((number*((2*number + 1)*(number+1)))/6))

print math_diff(100)