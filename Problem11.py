"""
OMG, I have just realized the below code searches vertically, and diagonally in both directions, but not horizontally!

A very nice piece of code, after my hackity solution, which decomposes the string into lists of integers, thereby
allowing the author to navigate using matrix-like commands.

A function is more appropriate than a lambda here, since it can handle IndexErrors, thereby generalizing the solution.

I have a notion I'll meet more grids in the future.
"""

import re

filename = "/Users/timothyroy/Documents/project_euler/grid.txt"
   # open the file with the data
data = open(filename, "r")

    # extract the info inside as a string. I had to do this because Python won't let me put the grid down in the
    # interpreter
dataset = data.read()

# this gets rid of the spaces, turning the data into one long string
blockset = dataset.replace(" ", "")

# the regex '.' is a metacharacter which matches any character except line breaks
# this code turns the long string into a list of two characters each.
grid = re.findall('..',blockset)
print dataset


# this makes a list of the products of the "vertical four" elements. len-60 to prevent IndexErrors
block = map(lambda num: (int(grid[num]) * int(grid[num+20]) * int(grid[num+40]) * int(grid[num+60])), range(len(grid)-60))

def diagonal_right():
    diagonallist = []
    try:
        for num in range(len(grid)):
            diagonallist.append (int(grid[num]) * int(grid[num+21]) * int(grid[num+42]) * int(grid[num+63]))
    except IndexError:
        pass
    return diagonallist

dr = diagonal_right()

def diagonal_left():
    diag_left = []
    try:
        for num in range(len(grid)):
            diag_left.append (int(grid[num]) * int(grid[num-19]) * int(grid[num-38]) * int(grid[num-57]))
    except IndexError:
        pass

    return diag_left
dl = diagonal_left()

masterlist = []
masterlist.extend(block+dr+dl)
print max(masterlist)

# multiply it by the three numbers above it, below it, diagonal up and down and left and right
# return the largest of these


from operator import mul

def euler_11(file="/Users/timothyroy/Documents/project_euler/grid.txt"):
    table = map(lambda x:map(int, x), map(lambda x:x.split(), open(file,"r").read().split("\n")))
    results = []
    for x in xrange(20):
        for y in xrange(20):
            if x+3 < 20:
                results.append(reduce(mul, [table[y][x+i] for i in xrange(4)]))
            if y+3 < 20:
                results.append(reduce(mul, [table[y+i][x] for i in xrange(4)]))
            if y+3 < 20 and x+3 <20:
                results.append(reduce(mul, [table[y+i][x+i] for i in xrange(4)]))
            if x > 2 and y+3 < 20:
                results.append(reduce(mul, [table[y+i][x-i] for i in xrange(4)]))
    return max(results)

print euler_11(file="/Users/timothyroy/Documents/project_euler/grid.txt")