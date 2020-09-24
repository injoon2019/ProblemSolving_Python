'''
Problem Solving Baekjoon 15661_2
Author: Injun Son
Date: September 24, 2020
'''
from itertools import combinations
import sys
'''
다른 사람 풀이 참고해서 itertools 안쓰고 풀어보기  
'''
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = sys.maxsize
alist = [k for k in range(n)]
check = [False]*n
cnt = n//2

def calc(alist):
    ret = 0

    bset = set([elem for elem in range(n)])
    blist = list(bset - set(alist))

    a_score = 0
    alen = len(alist)
    for i in range(alen-1):
        for j in range(i+1, alen):
            if i==j:
                continue
            x, y = alist[i], alist[j]
            a_score += arr[x][y]
            a_score += arr[y][x]

    b_score = 0
    blen = len(blist)
    for i in range(blen-1):
        for j in range(i+1, blen):
            if i==j:
                continue
            x, y = blist[i], blist[j]
            b_score += arr[x][y]
            b_score += arr[y][x]

    return abs(a_score - b_score)



def go(alist, tmp, idx):
    global ans
    if tmp==cnt:
        ans = min(ans, calc(alist))
        return

    for i in range(idx, n):
        if check[i]:
            continue
        check[i] = True
        go(alist+[i], tmp+1, i)
        check[i] = False

go([], 0, 0)
print(ans)