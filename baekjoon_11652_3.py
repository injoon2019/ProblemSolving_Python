'''
Problem Solving Baekjoon 11652_2
Author: Injun Son
Date: August 24, 2020
'''
import sys
from collections import Counter
N = int(input())
arr = [int(input()) for _ in range(N)]
dic = {}
for i in arr:
    if dic.get(i):
        dic[i]+=1
    else:
        dic[i]=1

card_list = [(n, dic[n]) for n in dic]
card_list.sort(key = lambda x: (-x[1], x[0]))
print(card_list[0][0])