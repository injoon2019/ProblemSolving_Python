'''
Problem Solving Baekjoon 1339
Author: Injun Son
Date: September 5, 2020
'''
from collections import deque
import sys
from itertools import combinations
#https://mygumi.tistory.com/156
N = int(input())
words = [ input() for _ in range(N)]
alpha = [0]*26
for i in range(N):
    j=0
    for w in words[i][::-1]:
        alpha[ord(w)-ord('A')] += 10**j
        j+=1

alpha.sort(reverse=True)
ans, t = 0, 9
for i in range(26):
    if alpha[i]==0:
        break
    ans += (t* alpha[i])
    t -=1

print(ans)