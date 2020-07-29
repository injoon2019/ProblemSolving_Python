'''
Problem Solving Baekjoon 7576
Author: Injun Son
Date: July 29, 2020
'''
import sys
sys.setrecursionlimit(100000)

c, r = map(int, sys.stdin.readline().rstrip().split())
arr = [list(input().split()) for _ in range(r)]
coord_list = []

for i in range(r):
    for j in range(c):
        if arr[i][j]=='1':
            spread(i, j)