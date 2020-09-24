'''
Problem Solving Baekjoon 1062
Author: Injun Son
Date: September 24, 2020
'''
from itertools import combinations
import sys

answer = -sys.maxsize
n, k = map(int, input().split())

def dfs(idx, cnt):
    global answer

    if cnt ==k-5:
        read_cnt = 0
        for word in words:
            for w in word:
                if not learn[ord(w)- ord('a')]:
                    break
            else:
                read_cnt +=1
        answer = max(answer, read_cnt) if answer else read_cnt
        return

    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt+1)
            learn[i] = False


if k<5 or k==26:
    print(0 if k<5 else n)
    exit()

words = [set(input()[4:-4]) for _ in range(n)]
learn = [False]*26

for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = True

dfs(0,0)
print(answer)