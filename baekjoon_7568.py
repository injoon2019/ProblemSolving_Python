'''
Problem Solving Baekjoon 7568
Author: Injun Son
Date: August 24, 2020
'''
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(100000)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
bigger_than_me = [0]*N

# for i in range(N):
#     for j in range(N):
#         if i!=j:
#             if arr[i][0] < arr[j][0] and arr[i][1]<arr[j][1]:
#                 bigger_than_me[i]+=1
# print(bigger_than_me)
# 나보다 큰 사람이 없어야 이기는 것!
#만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다.
for i in range(len(bigger_than_me)):
    count = 0
    for j in range(len(bigger_than_me)):
        if i!=j and arr[i][0] < arr[j][0] and arr[i][1]<arr[j][1]:
            count +=1

    print(count+1, end=" ")