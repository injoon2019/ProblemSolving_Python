'''
Problem Solving Baekjoon 15661
Author: Injun Son
Date: September 24, 2020
'''
from itertools import combinations
import sys

'''
스타트와 링크(14889와 다른 점:
14889는 항상 팀을 절반으로 나누었다.
이 문제에서는 절반으로 나누지 않으니 그 안에서 한번 더 comb를 구해야한다 
'''

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
min_ans = sys.maxsize

members = [i for i in range(N)]
start_combs = []
for i in range(1, N//2 +1):
    start_combs.append(list(combinations(members, i)))

for comb in start_combs:
    #left_team의 절반만해도 되긴한다
    for left_team in comb:
        right_team = list(set(members) - set(left_team))

        #양 팀 각각 합을 구하자
        left_sum, right_sum = 0, 0
        if len(left_team) >1:
            left_team_combs = list(combinations(left_team, 2))
            for left_pairs in left_team_combs:
                left_sum += graph[left_pairs[0]][left_pairs[1]]
                left_sum += graph[left_pairs[1]][left_pairs[0]]

        if len(right_team) >1:
            right_team_combs = list(combinations(right_team, 2))
            for right_pairs in right_team_combs:
                right_sum += graph[right_pairs[0]][right_pairs[1]]
                right_sum += graph[right_pairs[1]][right_pairs[0]]

        min_ans = min(min_ans, abs(left_sum - right_sum))

print(min_ans)