'''
Problem Solving Baekjoon 2251_4
Author: Injun Son
Date: September 19, 2020
'''
from collections import deque
import sys, copy
from itertools import permutations

a, b, c = map(int, input().split())
poss_permutation = list(permutations([0,1,2], 2))
water_limit = [a,b,c]
ans = [0]*(c+1)

def bfs(x, y, z):
    q = deque()
    check = dict()
    check[(x,y,z)] = 1
    q.append([x,y,z])
    while q:
        waters = q.popleft()

        if waters[0]==0:
            ans[waters[2]] = 1

        for i in range(len(poss_permutation)):
            from_n = poss_permutation[i][0]
            to_n = poss_permutation[i][1]
            waters_copy = copy.deepcopy(waters)

            #물을 받는 곳이 넘치는 경우
            if waters[from_n]+waters[to_n]> water_limit[to_n]:
                waters_copy[from_n] = waters_copy[from_n] - (water_limit[to_n] - waters_copy[to_n])
                waters_copy[to_n] = water_limit[to_n]

            else:
                waters_copy[to_n] += waters_copy[from_n]
                waters_copy[from_n] = 0

            if tuple(waters_copy) not in check:
                check[tuple(waters_copy)]=1
                q.append(waters_copy)

bfs(0, 0, c)

for i in range(c+1):
    if ans[i]==1:
        print(i, end=" ")