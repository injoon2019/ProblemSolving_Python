'''
Problem Solving Baekjoon 14889_2
Author: Injun Son
Date: August 23, 2020
'''


from collections import deque
import sys
from itertools import combinations
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
members = [i for i in range(N)]
possible_team = []

#가능한 팀 조합
for team in list(combinations(members, N//2)):
    possible_team.append(team)

min_stat_gap = sys.maxsize
#123, 456이나 456, 123이나 상관없다. 따라서 combination에서도 반만 조사하면된다
for i in range(len(possible_team)//2):
    #A팀
    team = possible_team[i]
    stat_A = 0
    for j in range(N//2):
        member = team[j]
        for k in team:
            stat_A += S[member][k]

    #A를 제외한 나머지팀
    #combination을 출력해보면 알겠지만 양끝이 서로 대칭이단
    team = possible_team[-i-1]
    stat_B = 0
    for j in range(N//2):
        member = team[j]
        for k in team:
            stat_B += S[member][k]

    min_stat_gap = min(min_stat_gap, abs(stat_A - stat_B))

print(min_stat_gap)