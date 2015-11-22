__author__ = 'nicholasstellitano'

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# By increasing a number by 20, the number will then only need to be divisible by 3,7,11,13,16,17,18,19

list = [3,7,11,13,16,17,18,19]

x = 20
while True:
    test = 0
    for y in list:
        test = test + (x % y)
        if test > 0:
            break
    if test == 0:
        break
    x += 20

print x