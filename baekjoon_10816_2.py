'''
Problem Solving Baekjoon 10816_2
Author: Injun Son
Date: August 10, 2020
'''
import sys
import math
M = int(input())
arr = list(map(int, input().split()))
N = int(input())
arr2 = list(map(int, input().split()))

hashmap = {}

for i in arr:
    if i in hashmap:
        hashmap[i] +=1
    else:
        hashmap[i] = 1

for i in arr2:
    if i in hashmap:
        print(hashmap[i], end= " ")
    else:
        print("0", end= " ")