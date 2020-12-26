'''
Problem Solving Programmers 64061
Author: Injun Son
Date: December 26, 2020
'''
import math
from itertools import combinations


def pick(j, board):
    for i in range(0, len(board)):
        if board[i][j] != 0:
            item = board[i][j]
            board[i][j] = 0
            return item


def move(stack, item):
    if stack and stack[-1] == item and item is not None:
        stack.pop()
        return 2
    stack.append(item)
    return 0


def solution(board, moves):
    answer = 0
    stack = []
    for j in moves:
        j = j - 1
        item = pick(j, board)
        if item == 0 or item is None:
            continue
        answer += move(stack, item)

    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]), 4)
print(solution([[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 2, 1, 0, 0], [0, 2, 1, 0, 0], [0, 2, 1, 0, 0]],
               [1, 2, 3, 3, 2, 3, 1]), 4)
print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 5, 1, 4, 3]), 8)
