'''
Problem Solving Baekjoon 17103
Author: Injun Son
Date: September 3, 2020
'''
from collections import deque
import sys

import sys
import copy
import math
input = sys.stdin.readline
prime_list = [True]*1000001
prime_list[0] = prime_list[1] = False
def Erathos():
    for i in range(2, int(math.sqrt(1000001))+1):
        for j in range(i*2, 1000001, i):
            prime_list[j]= False

Erathos()

T = int(input())
for _ in range(T):
    count = 0
    num = int(input())
    for i in range(2, num//2+1):
        if prime_list[i]==True and prime_list[num-i]==True:
            count +=1
    print(count)

