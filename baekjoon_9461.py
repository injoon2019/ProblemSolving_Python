'''
Problem Solving Baekjoon 9461
Author: Injun Son
Date: July 17, 2020
'''
import math

T = int(input())
for t in range(T):
    N = int(input())

    arr = [0]*101

    arr[1]=arr[2]=arr[3]=1
    arr[4]=arr[5]=2
    arr[6]=3 #arr[1]+arr[5]
    arr[7]=4 #arr[2]+arr[6]
    arr[8]=5 #arr[3]+arr[7]
    arr[9]=7
    arr[10]=9

    for i in range(11, 101):
        arr[i] = arr[i-5]+arr[i-1]

    print(arr[N])