'''
Problem Solving Baekjoon 1717_2
Author: Injun Son
Date: August 31, 2020
'''
import sys, copy
from collections import deque
input = sys.stdin.readline
output = sys.stdout.write
def getParent(zip, c):
    if c==zip[c]:
        return c
    zip[c] = getParent(zip, zip[c])
    return zip[c]

def unionParent(zip, a, b):
    a = getParent(zip, a)
    b = getParent(zip, b)
    if a< b:
        zip[b] = a
    else:
        zip[a] = b

def findParent(zip, a, b):
    if getParent(zip, a) == getParent(zip, b):
        print("YES")
    else:
        print("NO")

n, m = map(int, input().split())
zip = [i for i in range(n+1)]
for _ in range(m):
    c, a, b = map(int, input().split())
    #union
    if c==0:
        unionParent(zip, a, b)
    #check
    if c==1:
        findParent(zip, a, b)