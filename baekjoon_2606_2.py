'''
Problem Solving Baekjoon 2606
Author: Injun Son
Date: August 26, 2020
'''
import math, sys

def find(v):
    if zip[v]==v:
        return v

    zip[v] = find(zip[v])
    return zip[v]

def merge(v, w):
    x = find(v)
    y = find(w)
    if x==y:
        return
    if x<y:
        zip[y] = x
    else:
        zip[x] = y

N = int(input())
M = int(input())
zip = [i for i in range(0, N+1)]
for _  in range(M):
    a, b = map(int, input().split())
    merge(a, b)

for i in range(1, N+1):
    find(i)

cnt = -1
for i in range(1, N+1):
    if zip[i]==1:
        cnt +=1

if cnt==-1:
    print(0)
else:
    print(cnt)