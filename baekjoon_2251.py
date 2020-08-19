'''
Problem Solving Baekjoon 2251
Author: Injun Son
Date: August 19, 2020
'''
from collections import deque
import sys, copy
from itertools import permutations

def bfs(x, y, z):
    q.append([x,y,z])
    check.append([x,y,z])
    while q:
        k = q.popleft()
        #이 부분 이해 못함
        #문제의조건: 첫 번째 물통(용량이 A인)이 비어 있을 때, 세 번째 물통(용량이 C인)에 담겨있을 수 있는 물의 양
        if k[0] == 0:
            ans[k[2]]=1

        for i in range(len(t)):
            nfrom = t[i][0]
            nto = t[i][1]
            nk = copy.deepcopy(k)
            if k[nfrom] + k[nto] > limit[nto]:
                nk[nfrom] = k[nfrom]+k[nto] - limit[nto]
                nk[nto] = limit[nto]
            else:
                nk[nfrom]=0
                nk[nto] = k[nfrom]+k[nto]

            if nk not in check:
                check.append(nk)
                q.append(nk)

a,b,c = map(int, input().split())
q, check, limit = deque(), [], [a,b,c]
ans = [0 for _ in range(c+1)]
#가능한 인덱스 순열
t = list(permutations([0,1,2], 2))

bfs(0, 0, c)

for i in range(c+1):
    if ans[i]==1:
        print(i, end=' ')