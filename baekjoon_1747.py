'''
Problem Solving Baekjoon 1747
Author: Injun Son
Date: September 5, 2020
'''
from collections import deque
import sys
from itertools import combinations
import math

N = int(input())
primes = [True]*1004000
primes[0] = primes[1] = False
def Erathos():
    for i in range(2, int(math.sqrt(1004000)+1)):
        for j in range(i*2, 1004000, i):
            primes[j]=False


def is_Palindrome(num):
    str_num = str(num)
    str_num_reverse = str_num[::-1]
    return str_num == str_num_reverse

Erathos()

for i in range(N, 1004000):
    if primes[i]==True and is_Palindrome(i):
        print(i)
        break