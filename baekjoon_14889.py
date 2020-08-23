'''
Problem Solving Baekjoon 14889
Author: Injun Son
Date: August 23, 2020
'''
from collections import deque
import sys
from itertools import combinations
N = int(input())
entire_members = [i for i in range(0, N)]
graph = [list(map(int, input().split())) for _ in range(N)]
possible_combination = list(combinations([i for i in range(0, N)], N//2))
MIN = sys.maxsize

print(possible_combination)
for combination in possible_combination:
    team_A = combination
    team_B = list(set(entire_members)-set(team_A))
    team_A_sum, team_B_sum = 0,0
    for i in team_A:
        team_A_no_i = set(team_A)-set([i])
        for j in team_A_no_i:
            team_A_sum += graph[i][j]

    for i in team_B:
        team_B_no_i = set(team_B)-set([i])
        for j in team_B_no_i:
            team_B_sum += graph[i][j]
    MIN = min(MIN, abs(team_B_sum - team_A_sum))

print(MIN)