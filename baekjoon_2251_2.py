'''
Problem Solving Baekjoon 2251_2
Author: Injun Son
Date: August 19, 2020
'''
from collections import deque
import sys, copy
from itertools import permutations

def bfs(x, y, z):
    q.append([x, y, z])
    check.append([x,y, z])
    while q:
        waters = q.popleft()
        #이게 문제 조건이다
        if waters[0]==0:
            ans[waters[2]]=1

        for i in range(len(index_permutation)):
            nfrom = index_permutation[i][0]
            nto = index_permutation[i][1]
            new_waters = copy.deepcopy(waters)

            if waters[nfrom] + waters[nto]> limit[nto]:
                new_waters[nfrom] = waters[nfrom] + waters[nto]- limit[nto]
                new_waters[nto] = limit[nto]
            else:
                new_waters[nfrom] = 0
                new_waters[nto]= waters[nfrom]+waters[nto]

            if new_waters not in check:
                check.append(new_waters)
                q.append(new_waters)


a, b, c = map(int, input().split())
q, check, limit = deque(), [], [a, b, c]
ans = [0 for i in range(c+1)]
#가능한 인덱스 순열
index_permutation = list(permutations([0,1,2], 2))

bfs(0, 0, c)

for i in range(c+1):
    if ans[i]==1:
        print(i, end= " ")