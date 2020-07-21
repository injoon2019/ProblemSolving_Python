'''
Problem Solving Baekjoon 11652_2
Author: Injun Son
Date: July 21, 2020
'''
import sys
N = int(sys.stdin.readline())
dict = {}
for _ in range(N):
    n = int(sys.stdin.readline())
    if n not in dict:
        dict[n] = 1

    dict[n] +=1

card_list = [(n, dict[n]) for n in dict]
sorted(card_list, key = lambda x: (-x[1], x[0]))
print(card_list[0][0])