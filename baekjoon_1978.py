'''
Problem Solving Baekjoon 1978
Author: Injun Son
Date: July 25, 2020
'''
import sys
import math
erathos = [True]*1001
erathos[0] = erathos[1] = False
def erathos_func():
    for i in range(2, int(math.sqrt(1001))+1):
        for j in range(i+i, 1001, i):
            erathos[j] = False

erathos_func()
N = int(input())
arr = list(map(int, input().split()))
count = 0
for i in range(N):
    if erathos[arr[i]]==True:
        count +=1

print(count)