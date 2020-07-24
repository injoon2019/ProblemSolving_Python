'''
Problem Solving Baekjoon 9613
Author: Injun Son
Date: July 24, 2020
'''
import sys
import math
T = int(input())
for _ in range(T):
    sum = 0
    lst = list(map(int, input().split()))
    for i in range(1, lst[0]):
        for j in range(i+1, lst[0]+1):
            sum += math.gcd(lst[i], lst[j])

    print(sum)

