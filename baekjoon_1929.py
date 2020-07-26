'''
Problem Solving Baekjoon 1929
Author: Injun Son
Date: July 25, 2020
'''
import sys
import math
erathos = [True]*1000001
erathos[0] = erathos[1] = False
def erathos_func():
    for i in range(2, int(math.sqrt(1000001))+1):
        for j in range(i+i, 1000001, i):
            erathos[j] = False

erathos_func()
M, N = map(int, input().split())
for i in range(M, N+1):
    if erathos[i]==True:
        print(i)