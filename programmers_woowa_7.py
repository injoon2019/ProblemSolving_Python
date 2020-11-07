'''
Problem Solving Programmers woowa 7
Author: Injun Son
Date: November 7, 2020
'''
import math
from itertools import combinations
from itertools import combinations

dir = -1
dy = [0, 1, 1, -1]
dx = [1, -1, 0, 1]

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end= " ")
        print()
    print()

def solution(n, horizontal):
    matrix = [[0]*n for _ in range(n)]
    answer = [[]]
    num = 1
    for i in range(n):
        for j in range(n):
            matrix[i][j] = num
            num +=1

    for i in range(n):
        for j in range(n):
            sum = i+j
            if sum%2 ==0:



print(solution(4, True))
print(solution(5, False))