'''
Problem Solving Baekjoon 1541
Author: Injun Son
Date: August 15, 2020
'''
import sys
from collections import deque
#1+1+1-1
equation = input().split("-")
for i in range(len(equation)):
    tmp_sum = 0
    if '+' in equation[i]:
        tmp = list(map(int, equation[i].split("+")))
        tmp_sum = sum(tmp)
        equation[i] = tmp_sum
    else:
        equation[i] = int(equation[i])

ans = equation[0]
for i in range(1, len(equation)):
    ans -= equation[i]
print(ans)