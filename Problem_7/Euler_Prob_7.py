__author__ = 'nicholasstellitano'

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
# To calculate this prime number we can use the Sieve of Eratosthenes


def sieve_erato(list, p):
    n = int(len(list)**.5)
    if list[p]:
        x = p+p
        while x < len(list):
            list[x] = False
            x += p
    if p < n:
        return sieve_erato(list, p+1)
    return list

y = [True] * 130000
y[0] = False
y[1] = False

print sieve_erato(y, 2)

i = 0
count = 0
while i < len(y):
    if y[i]:
        count += 1
        if count == 10001:
            print i
    i += 1