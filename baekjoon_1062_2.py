'''
Problem Solving Baekjoon 1062_2
Author: Injun Son
Date: October 15, 2020
'''
from itertools import combinations
import sys

# antatica -> antic
answer = -sys.maxsize
N, K = map(int, input().split())

def back_tracking(idx, cur_count):
    global answer
    if cur_count == K-5:
        tmp = 0
        for word in words:
            for w in word:
                if not learned_alpha[ord(w)-ord('a')]:
                    break
            else:
                tmp +=1
        answer = max(answer, tmp) if answer else tmp
        return

    for i in range(idx, 26):
        if not learned_alpha[i]:
            learned_alpha[i]=True
            back_tracking(i, cur_count+1)
            learned_alpha[i]=False

if K<5 or K==26:
    print(0 if K<5 else N)
    exit()

words = [set(input()[4:-4]) for _ in range(N)]
learned_alpha = [False]*26

for c in ('a', 'c', 'i', 'n', 't'):
    learned_alpha[ord(c) - ord('a')] = True

back_tracking(0, 0)
print(answer)