__author__ = 'nicholasstellitano'

# Euler Problem 3: The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Prime numbers are odd (except for the number 2) and a prime factor should be equal or less than half of 600851475143
# If we utilize a list of odd numbers and eliminate all numbers that are not prime, we can then identify the largest
# prime factor.  The index of a list can determine what the value is 2i + 1 : for example [2,3,5,7,9] 2(3)+1 = 7
# The is_prime function was copied from: https://www.daniweb.com/programming/software-development/code/216880/check-if-a-number-is-a-prime-number-python

def is_prime(n):
    #'''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

num = 600851475143

i = int(600851475143**.5) -1
while i > 2:
    if num % i == 0:
        if is_prime(i):
            print(i)
            i = 2
    i -= 2

