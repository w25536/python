from math import gcd

def solution(a, b):


    b //= gcd(a, b)

    num = []
    i = 2

    while i <= b:
        if b % i == 0:
            b //= i
            num.append(i)
        else:
            i += 1

    if all( i in [2,5] for i in num):
        return 1


    return 2 
