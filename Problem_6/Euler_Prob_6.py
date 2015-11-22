__author__ = 'nicholasstellitano'

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

from math import *

### Square of the Sum ###

x = list(range(0,101))
print x
square_sum = sum(x)**2

### sum of squares ###

def sum_of_sqrs(count):
    if count == 100:
        print x[0]
        print x[count]
        return x[count]**2
    else:
        return x[count]**2 + sum_of_sqrs(count+1)

count = 0

sum_sqrs = sum_of_sqrs(count)

print square_sum - sum_sqrs