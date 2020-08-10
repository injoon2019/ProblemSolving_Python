'''
Problem Solving Baekjoon 10816
Author: Injun Son
Date: August 10, 2020
'''
import sys
import math
M = int(input())
arr = list(map(int, input().split()))
N = int(input())
arr2 = list(map(int, input().split()))
count_arr = [0 for i in range(-10000000, 10000001)]
for i in arr:
    count_arr[i+10000000]+=1
for i in arr2:
    print(count_arr[i+10000000], end=" ")
