'''
Problem Solving Baekjoon 9466_3
Author: Injun Son
Date: August 31, 2020
'''
import sys
sys.setrecursionlimit(10000)
from collections import deque

T = int(input())

def dfs(x):
    global result
    visit_check[x] = True
    cycle.append(x)
    number = numbers[x]

    if visit_check[number]:
        if number in cycle:
            result += cycle[cycle.index(number):]
        return
    else:
        dfs(number)

for _ in range(T):
    n = int(input())
    numbers = [0]+ list(map(int, input().split()))
    visit_check = [True]+[False]*n
    result = []
    for i in range(1, n+1):
        if not visit_check[i]:
            cycle = []
            dfs(i)

    print(n - len(result))