'''
Problem Solving Baekjoon 9663_2
Author: Injun Son
Date: August 25, 2020
'''
import sys, copy
from collections import deque
from itertools import combinations

n = int(input())
count = 0
# 수직, 왼쪽 대각선, 오른쪽 대각선
row, left, right = [0 for _ in range(n)], [0 for _ in range(2*n -1)], [0 for _ in range(2*n -1)]
# https://rebas.kr/761
def quuenlocation(index):
    global count
    if index == n:
        count +=1
        return

    #어짜피 각 열에는 한개의 퀸밖에 존재 못함을 이용
    for col in range(n): #열을 이동하며
        if row[]

queenlocation(0)
print(count)