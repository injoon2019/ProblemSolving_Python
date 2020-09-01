'''
Problem Solving Baekjoon 3190
Author: Injun Son
Date: October 1, 2020
'''
import math, sys

N = int(input())
K = int(input())
apples = []
for _ in range(K):
    y, x = map(int, input().split())
    apples.append([y, x])
L = int(input())
moves = []
for _ in range(L):
    command = input().split()
    moves.append([int(moves[0]), moves[1]])
