'''
Problem Solving Baekjoon 11399
Author: Injun Son
Date: August 12, 2020
'''
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
sum =0
for i in range(len(arr)):
    for j in range(0, i+1):
        sum += arr[j]

print(sum)