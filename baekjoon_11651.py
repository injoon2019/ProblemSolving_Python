'''
Problem Solving Baekjoon 11651
Author: Injun Son
Date: July 20, 2020
'''

N = int(input())
arr = [tuple(map(int, input().split(" "))) for _ in range(N)]
ans = sorted(arr, key=lambda x: (x[1], x[0]))
for i in ans:
    print(i[0], i[1])