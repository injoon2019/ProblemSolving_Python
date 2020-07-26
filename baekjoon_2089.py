'''
Problem Solving Baekjoon 2089
Author: Injun Son
Date: July 25, 2020
'''
import sys
N = int(input())
arr = []
while N!=0:
    if (N%-2) !=0:
        arr.append(abs(N%-2))
        N = N//(-2)
        N +=1
    else:
        arr.append(N%-2)
        N = N//-2

if len(arr)==0:
    print(0)
else:
    for i in range(len(arr)-1, -1, -1):
        print(arr[i], end="")