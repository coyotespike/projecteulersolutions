"""
The prime factors of 13195 are 5, 7, 13 and 29 (13195*7*13*29

What is the largest prime factor of the number 600851475143 ?

Uses the sieve of Eratosthenes: if not divisible by 2, 3, 5, 7, 11, or 17, then the number is likely prime.

An inelegant solution. It begins with a list of primes instead of generating them from 2 and 3.
Further, in order to avoid leaving in primes artificially listed, it tests the list and removes elements after having made it.
So it visits the list twice.

Two fundamental theorems might have been helpful. One. Any nonzero integer may be represented as a product of distinct primes.
Two. If an integer has a prime factor greater than its square root, there must be a prime less than the square root.
Three. Therefore, if all the primes less than the square root of a number are not factors of the number, then there is no prime
greater than the square root of that number, which is also a factor of the number.

"We can stop here, because we know there can be no prime factor of N that is greater than
the square root of N. Why? Because, if there were, then there would also be a prime factor less than the square root of N, and we have
already found out that there is none."
"""

def Eratosthenes_products (number):

    listofprimes = [2,3,5,7,11,13]
    count = 14


    while count<number:

        if all(count%num !=0 for num in listofprimes):
            listofprimes.append(count)
        # add another prime to the list

        # increment the counter
        count +=1

        for num in listofprimes:
            if number%num !=0:
                listofprimes.remove(num)

        # test if all the primes multiplied together exceed the target number
        if reduce(lambda x, y: x * y, listofprimes) >= number:
            break

    #return the last prime


    return listofprimes

print Eratosthenes_products(600851475143)

# This rather elegant solution is limited: it only works for odd target numbers
number=600851475143
value=number
i=2
max_prime=i
while(value>1):
    if(value%i==0):
        value=value/i
        max_prime=i
    else:
        i=i+1

print('Max prime of %d is %d\n'%(number,max_prime))

# I do not understand this solution
num = 600851475143
for i in xrange(2, int(num**0.5)):
    if num%i == 0 and all(i%j != 0 for j in xrange(2, int(i**0.5)+1)) == True:
        temp = i
print "Answer:", temp


"""
These previous attempts crashed my computer, since I attempted to compute more primes than necessary.

    # divide every new number by the known primes so far
    # if none equal 0, add that number to the list of primes

    # alternatively, generate the list of all numbers, and if divisible by any known prime,
    # delete from the list
    for num in listofall[::-1]:
        for othernum in listofall[::]:
            if num%othernum == 0 and num!=othernum:
                listofall.remove(num)
                break

    for num in listofall:
        if number % num == 0:
            listofprimes.append(num)

            First i tried making all prime numbers in the target number, then testing them to see if they were factors.
            Second, I am trying testing all factors, then seeing if they are prime. That also crashes the computer
            Third, I will try generating from the bottom up.
                listofprimes = [2]
    listofall = [num for num in range(2, number/2)]

    print "initialized problem"

    for num in listofall:
        if number%num == 0:
            listofprimes.append(num)
    print "made list of primes"

    for num in listofprimes[::-1]:
        for othernum in listofprimes[::]:
            if num%othernum == 0 and num!=othernum:
                listofprimes.remove(num)
                break

    return listofprimes[-1]

        if count%(all(listofprimes))!=0:
            listofprimes.append(count)
"""