'''
Problem Solving Baekjoon 6588
Author: Injun Son
Date: July 26, 2020
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

N = int(input())
while N != 0:
    for i in range(3, N):
        if erathos[i]==True and erathos[N-i]==True:
            print("{} = {} + {}".format(N, i, N-i))
            break

    N = int(input())