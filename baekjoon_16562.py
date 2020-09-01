'''
Problem Solving Baekjoon 16562
Author: Injun Son
Date: August 31, 2020
'''
import sys
import math

def getParent(v):
    if zip[v]==v:
        return v
    else:
        y = getParent(zip[v])
        zip[v] = y
    return zip[v]

def unionParent(a, b):
    a = getParent(a)
    b = getParent(b)
    if a < b:
        zip[b] = a
    else:
        zip[a] = b

def findParent(a, b):
    if getParent(a)==getParent(b):
        return True
    else:
        return False

N, M, K = map(int, input().split())
zip = [i for i in range(N+1)]
price = [0]+list(map(int, input().split()))

for _ in range(M):
    v, w = map(int, input().split())
    unionParent(v, w)

for i in range(1, N+1):
    getParent(i)

prices_per_groups = [sys.maxsize for i in range(N+1)]

for i in range(1, N+1):
    prices_per_groups[zip[i]] = min(prices_per_groups[zip[i]], price[i])

ans= 0
for i in range(1, N+1):
    if prices_per_groups[i] != sys.maxsize:
        ans += prices_per_groups[i]

if ans <=K:
    print(ans)
else:
    print("Oh no")