'''
Problem Solving Baekjoon 17404
Author: Injun Son
Date: September 25, 2020
'''
from collections import deque
import sys
from itertools import combinations
blocks = [[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]
max_depth = 0
def print_board(N, twod_block):
    for i in range(N):
        for j in range(N):
            print(twod_block[i][j], end=" ")
        print()
    print()

def solution(blocks):
    max_depth = blocks[-1][0] +1
    twod_block = [ [-111]*max_depth for _ in range(max_depth)]
    idx = 0

    for i in range(max_depth):
        for j in range(max_depth):
            if idx >= len(blocks):
                break

            if blocks[idx][0]==j:
                twod_block[i][j] = blocks[idx][1]
                idx +=1
                break

    print_board(max_depth, twod_block)
    answer = []
    return answer

solution(blocks)
