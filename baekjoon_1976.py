'''
Problem Solving Baekjoon 1976
Author: Injun Son
Date: August 31, 2020
'''
import sys, copy
from collections import deque
# input=  sys.stdin.readline
# print = sys.stdout.write

def getParent(zip, a):
    if a==zip[a]:
        return zip[a]
    zip[a] = getParent(zip, zip[a])
    return zip[a]

def unionParent(zip, a, b):
    a = getParent(zip, a)
    b = getParent(zip, b)
    if a<b:
        zip[b] = a
    else:
        zip[a] = b

def findParent(zip,a , b):
    if getParent(zip, a)== getParent(zip, b):
        return True
    else:
        return False

N = int(input())
zip = [i for i in range(N+1)]
M = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            unionParent(zip, i+1, j+1)

for i in range(0, len(plan)-1):
    if not findParent(zip, plan[i], plan[i+1]):
        print("NO")
        exit()

print("YES")