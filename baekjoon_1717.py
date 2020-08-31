'''
Problem Solving Baekjoon 1717
Author: Injun Son
Date: August 31, 2020
'''
import sys, copy
from collections import deque
input=  sys.stdin.readline
print = sys.stdout.write

#부모 찾기
def getParent(zip, c):
    if c==zip[c]:
        return c
    zip[c] = getParent(zip, zip[c])
    return zip[c]

#합집합
def unionParent(zip, a, b):
    a = getParent(zip, a)
    b = getParent(zip, b)
    if a< b:
        zip[b] = a
    else:
        zip[a] = b

#같은 부모인지 확인하기
def findParent(zip, a, b):
    a = getParent(zip, a)
    b = getParent(zip, b)
    if a==b:
        print("YES\n")
    else:
        print("NO\n")
    
n, m= map(int, input().split())

#n개의 집합
zip = [i for i in range(n+1)]

for i in range(m):
    t, a, b = map(int, input().split())
    #합집합 만들기
    if t ==0:
        unionParent(zip, a, b)
    #부모 동일 확인
    else:
        findParent(zip, a, b)