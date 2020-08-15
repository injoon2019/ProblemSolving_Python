'''
Problem Solving Baekjoon 10971_2
Author: Injun Son
Date: August 15, 2020
'''
import sys
from itertools import permutations
from itertools import permutations

n = int(input())
d= []
for i in range(n):
    d.append([int(a) for a in input().split()])

perm = [i for i in range(n)]
answer = 9123491234
def sum_routes(r):
    global d, n
    tmp = 0
    for i in range(len(r)-1):
        if d[r[i]][r[i+1]] !=0:
            tmp +=d[r[i]][r[i+1]]
        else:
            return -1

    if d[r[-1]][r[0]] ==0:
        return -1
    else:
        tmp += d[r[-1]][r[0]]

    return tmp

for c in permutations(perm):
    tmpans = sum_routes(c)
    if tmpans != -1:
        answer = min(answer, tmpans)

print(answer)