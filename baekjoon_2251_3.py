'''
Problem Solving Baekjoon 2251_3
Author: Injun Son
Date: September 19, 2020
'''
from collections import deque
import sys, copy
from itertools import permutations

a, b, c = map(int, input().split())
q, check, limit = deque(), dict(), [a, b, c]
ans = [0 for _ in range(c+1)]
#가능한 인덱스 순열
index_permutation = list(permutations([0,1,2], 2))

def bfs(x, y, z):
    q.append([x, y, z])
    check[(x, y, z)] =1
    while q:
        waters = q.popleft()
        if waters[0]==0:
            ans[waters[2]] = 1

        for i in range(len(index_permutation)):
            nfrom = index_permutation[i][0]
            nto = index_permutation[i][1]
            new_waters = copy.deepcopy(waters)

            #만약 from에서 to로 물을 더했을 때 넘치는 상황이라면
            if waters[nfrom] + waters[nto] > limit[nto]:
                new_waters[nfrom] = waters[nfrom]+waters[nto] - limit[nto]
                new_waters[nto] = limit[nto]
            else:
                new_waters[nfrom] = 0
                new_waters[nto] = waters[nfrom]+waters[nto]

            if tuple(new_waters) not in check:
                check[tuple(new_waters)]=1
                q.append(new_waters)

bfs(0, 0, c)

for i in range(c+1):
    if ans[i]==1:
        print(i, end=" ")