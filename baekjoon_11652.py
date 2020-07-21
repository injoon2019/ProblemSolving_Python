'''
Problem Solving Baekjoon 11652
Author: Injun Son
Date: July 21, 2020
'''
import sys
N = int(sys.stdin.readline())
card = {}
for _ in range(N):
    n = int(sys.stdin.readline())
    if n not in card:
        card[n] = 0
    card[n]+=1

#key:value = 숫자, 횟수
card_list = [(n, card[n]) for n in card]
card_list.sort(key=lambda x: (-x[1], x[0]))
print(card_list[0][0])