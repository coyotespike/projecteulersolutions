# my simple for-loop
power = 2**1000
result = 0
for i in str(power):
    result += int(i)

print result

# one-liner from Project Euler
print sum(int(digit) for digit in str(2**1000))