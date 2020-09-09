'''
Problem Solving Baekjoon 14425
Author: Injun Son
Date: September 9, 2020
'''
import sys
import math
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
word_set  = set()
for _ in range(N):
    word_set.add(input())

count = 0

for _ in range(M):
    if input() in word_set:
        count +=1

print(count)