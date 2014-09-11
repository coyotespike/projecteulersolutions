"""
Find the largest palindrome made from the product of two 3-digit numbers.

    palin = "able was i ere i saw elba"
    if palin == palin[::-1]:
        print 'yay!'

"""

def palindrome(factora, factorb):

    listofresults = []

    for num in range(100, factora+1):
        for othernum in range(100, factorb+1):
            result = num*othernum
            if str(result)[::-1] == str(result):
                listofresults.append(result)

    return max(listofresults)

factora=factorb=999

#print palindrome(factora, factorb)



def palindromeb(start, stop):

    listofresults = []

    for num in xrange(start, stop, -1):
        for othernum in xrange(start,stop, -1):
            result = num*othernum
            if str(result)[::-1] == str(result):
                listofresults.append(result)

    return max(listofresults)

start = 999
stop = 900

#print palindromeb(factora, factorb)


import timeit
def wrapped1():
    return palindrome(factora, factorb)
def wrapped2():
    return palindromeb(start, stop)


trial1 = timeit.timeit(wrapped1, number=10)
trial2 = timeit.timeit(wrapped2, number=10)

print trial1
print trial2

print "New algorithm is " + str(100-((float(trial2)/trial1)*100)) + "% faster than old algorithm"