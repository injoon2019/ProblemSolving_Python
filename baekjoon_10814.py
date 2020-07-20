'''
Problem Solving Baekjoon 10814
Author: Injun Son
Date: July 20, 2020
'''

N = int(input())
arr = []
for i in range(N):
    age, name = input().split(" ")
    arr.append((int(age), name, i))

ans = sorted(arr, key = lambda x: (x[0], x[2]))
for i in ans:
    print(i[0], i[1])