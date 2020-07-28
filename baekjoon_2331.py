'''
Problem Solving Baekjoon 2331
Author: Injun Son
Date: July 27, 2020
'''
import sys
sys.setrecursionlimit(100000)

def digitSum(num):
    sum = 0
    while num:
        sum += (num%10)**P
        num //=10
    return sum

A, P = map(int, sys.stdin.readline().rstrip().split())
arr = []
num = A
while num not in arr:
    arr.append(num)
    num = digitSum(num)

repeat_start = arr.index(num)
print(repeat_start)

