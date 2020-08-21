'''
Problem Solving Baekjoon 1644
Author: Injun Son
Date: August 21, 2020
'''
import sys
import math
N = int(input())
is_Prime = [True]*4000000
prime_list = []

def Erathos():
    for i in range(2, int(math.sqrt(4000000))+1):
        for j in range(i*2, 4000000, i):
            is_Prime[j]=False

def select_primes():
    for i in range(2, 4000000):
        if is_Prime[i]:
            prime_list.append(i)

Erathos()
select_primes()

left, right = 0, 0
tmp, count = 0, 0
while True:
    if tmp == N:
        count +=1
        tmp -= prime_list[left]
        left +=1

    elif right==len(prime_list):
        break

    else:
        if tmp > N:
            tmp -= prime_list[left]
            left+=1
        else: #tmp <N
            tmp += prime_list[right]
            right +=1

print(count)
