#Problem 1 : Below 10: 3,5,6,9 (all multiples of 3 and 5) sum to 23.  What is the sum for 1000
#            Below 15: 3,4,6,9,10,12,15 sum to 59
#            Each subsequent block of 15 will increase by 7*15=105

d = 1000/15
d_rem = float(1000 % 15)
s = 60
n = 105

def sums(dd):
    if dd < 1:
        return 0
    sumed = s + n*(dd-1) + sums(dd-1)
    return sumed

def sub_leftover(x):
    above = (x+1)*15
    cutoff = 1000
    total_sub = 0
    while above >= cutoff:
        if (above % 3 == 0):
            total_sub += above
        elif (above % 5 == 0):
            total_sub += above
        above -= 1

    return total_sub

total_sum = sums(d+1) -sub_leftover(d)

print total_sum

