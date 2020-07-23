'''
Problem Solving Baekjoon 10808
Author: Injun Son
Date: July 23, 2020
'''
import sys

str = sys.stdin.readline().rstrip()
arr = [0]*26
for i in range(len(str)):
    arr[ord(str[i])-ord('a')] +=1

for i in range(len(arr)):
    print(arr[i], end=" ")