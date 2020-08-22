'''
Problem Solving Baekjoon 9093
Author: Injun Son
Date: August 22, 2020
'''
import sys
from heapq import heappush, heappop
T = int(input())
for _ in range(T):
    sentence = input()
    sentence_split = sentence.split()
    for word in sentence_split:
        for i in range(len(word)-1, -1, -1):
            print(word[i], end= "")
        print(" ", end="")