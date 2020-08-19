'''
Problem Solving Baekjoon 1987
Author: Injun Son
Date: August 18, 2020
'''
from collections import deque
import sys

n, m = map(int, input().split())
a = [list(input().strip()) for _ in range(n)]
check, ans = [False]*26, 0

def dfs(x, y, z):
    global ans
    ans = max(ans, z)
    for dx, dy in (-1,0), (1,0), (0, -1), (0,1):
        nx, ny = x+dx, y+dy
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        c = ord(a[nx][ny])-ord('A')
        if not check[c]:
            check[c] = True
            dfs(nx, ny, z+1)
            check[c]= False

check[ord(a[0][0])- ord('A')] = True
dfs(0, 0, 1)
print(ans)