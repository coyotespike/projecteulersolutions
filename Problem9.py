"""
A pythagorean triplet is a set of three natural numbers, a<b<c, for which a^2+b^2=c^2. There exists exactly one
Pythagorean triplet for which a+b+c = 1000. Find the product of these numbers, abc.

This is more easily solved by using Euclid's formula: a=m^2-n^2, b=2mn, c=m^2+n^2. The triple generated by this formula
is primitive only if m and n are coprime, and if m-n is odd. If both m and n are odd, then a, b, and c will be even and
the triple will not be primitive.

That these formulas are correct is easily seen by squaring the first two; they work out to the third. Here is a simple
proof.

c^2-a^2 = b^2, so (c-a)(c+a) = b^2. Thus, (c+a)/b = b/(c-a). Let's make (c+a)/b = m/n. Next, (c-a)/b is the reciprocal
of b/(c-a), so it must equal the reciprocal of (c+a)/b, so it equal n/m.

Solve the resulting equations, c/b + a/b = m/n and c/b - a/b = n/m, for a/b and c/b. This results in:
a/b = m^2 - n^2 / 2mn, and c/b = m^2 + n^2 / 2mn. We have assumed these are fully reduced, so you can equate the
numerators and denominators.

These Pythagorean triples turn out to have a number of interesting properties: at most one is a square, c is odd and
only one of a and b is odd. Every integer greater than 2, which is not of the form 4n+2 (2 mod 4), is part of a primitive
Pythagorean triple.
"""
from math import sqrt

def triplet_sum (number):
    a=3
    b=4
    c = sqrt(a**2 + b**2)

    while a+b+c < number:
        a=b
        b+=1
        temp = sqrt(a**2 + b**2)
        if temp in range(number):
            c = temp
            print "yeeha!"
            print c

    return a+b+c, a, b, c, temp, a*b*c

def triplet_sum2 (number):
    for a in range(1000):
        for b in range(1000):
            c = sqrt(a**2 + b**2)
            if c in range(number):
                if a<b<c:
                    if a+b+c == number:
                        return a+b+c, a*b*c, a, b, c

print triplet_sum2(1000)