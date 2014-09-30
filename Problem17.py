"""
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

Here is a very succinct solution from Project Euler, using a Python package. I also like the easy use of time.clock().
from num2words import num2words
import time

timeBefore = time.clock()

cnt = 0
for i in range (1,1001):
    num_word = num2words(i)
    num_word = num_word.replace(" ","")
    num_word = num_word.replace("-","")
    cnt += len(num_word)
print cnt

timeAfter = time.clock()
elapsed_time = timeAfter - timeBefore
print elapsed_time
"""
def count_words(number):
    counter = 0
    # definitions
    numdict = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
#    num = number
    for num in range(1, number+1):
#    if num == number:

        num = str(num)

        if len(num)==4:
            counter+=len("onethousand")

        if len(num)==3:
            counter += len(numdict[int(num[0])])
            counter += len("hundred")
            if num[-1] != "0" or num[-2] != "0":
                counter+=len("and")

            num = num[1:]
#            counter += count_words(number)

        if len(num) == 2:
            if num[-2] == "0":
                counter+=len(numdict[int(num[-1])])
            if num[-2] == "1":
                if num[-1] == "0":
                    counter+=len("ten")

                if num[-1] == "1":
                    counter+=len("eleven")

                if num[-1] == "2":
                    counter+=len("twelve")

                if num[-1] == "3":
                    counter+=len("thirteen")

                if num[-1] == "4":
                    counter+=len("fourteen")

                if num[-1] == "5":
                    counter+=len("fifteen")

                if num[-1] == "6":
                    counter+=len("sixteen")

                if num[-1] == "7":
                    counter+=len("seventeen")

                if num[-1] == "8":
                    counter+=len("eighteen")

                if num[-1] == "9":
                    counter+=len("nineteen")


            if num[-2] == "2":
                counter+=len("twenty")
                counter+=len(numdict[int(num[-1])])
            if num[-2] == "3":
                counter+=len("thirty")
                counter+=len(numdict[int(num[-1])])
            if num[-2] == "4":
                counter+=len("forty")
                counter+=len(numdict[int(num[-1])])
            if num[-2] == "5":
                counter+=len("fifty")
                counter+=len(numdict[int(num[-1])])
            if num[-2] == "6":
                counter+=len("sixty")
                counter+=len(numdict[int(num[-1])])
            if num[-2] == "7":
                counter+=len("seventy")
                counter+=len(numdict[int(num[-1])])
            if num[-2] == "8":
                counter+=len("eighty")
                counter+=len(numdict[int(num[-1])])
            if num[-2] == "9":
                counter+=len("ninety")
                counter+=len(numdict[int(num[-1])])
        if len(num) == 1:
            counter += len(numdict[int(num)])
    return counter

print count_words(1000)
