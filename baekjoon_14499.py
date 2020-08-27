'''
Problem Solving Baekjoon 14499
Author: Injun Son
Date: August 26, 2020
'''
import math, sys

r, c, y, x, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
dir_arr = list(map(int, input().split()))

#동 서 북 남
#1 2 3 4

for i in dir_arr:
    pass