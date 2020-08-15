'''
Problem Solving Baekjoon 10971_2
Author: Injun Son
Date: August 15, 2020
'''
import sys
from itertools import permutations
sys.setrecursionlimit(100000)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
order = [i for i in range(0, N)]
permutation_list = list(permutations(order, N))
answer = sys.maxsize

for list in permutation_list:
    temp_sum = 0
    broken = False
    for i in range(len(list)-1):
        if graph[list[i]][list[i+1]] == 0 or graph[list[len(list)-1]][list[0]] ==0:
            broken = True
            break
        else:
            temp_sum += graph[list[i]][list[i+1]]
    if not broken:
        temp_sum += graph[list[len(list)-1]][list[0]]
        answer = min(temp_sum, answer)
print(answer)