'''
Problem Solving Baekjoon 9466_4
Author: Injun Son
Date: August 31, 2020
'''
import sys
sys.setrecursionlimit(100000)
from collections import deque

T = int(input())

def dfs(x):
    global result
    visit[x] = True
    cycle.append(x)
    num = numbers[x]

    if visit[num]==True:
        if num in cycle:
            result+=(cycle[cycle.index(num):])
        return
    else:
        dfs(num)

for _ in range(T):
    N = int(input())
    numbers = [0]+list(map(int, input().split()))
    visit = [True]+[False]*N
    result = []
    for i in range(1, N+1):
        if not visit[i]:
            cycle = []
            dfs(i)

    print(N - len(result))