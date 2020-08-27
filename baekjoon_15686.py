'''
Problem Solving Baekjoon 15686
Author: Injun Son
Date: August 26, 2020
'''
import math, sys
from itertools import combinations

r, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
possible_chicken_num = [i for i in range(1, m+1)]
chicken_coordinates = []
#(y, x)좌표와 최소 치킨 거리를 저장
house_coordinates = {}
def get_chicken_coordinates():
    for i in range(r):
        for j in range(r):
            if graph[i][j]==2:
                chicken_coordinates.append((i, j))
            elif graph[i][j]==1:
                house_coordinates[(i, j)] = sys.maxsize

get_chicken_coordinates()
min_ans = sys.maxsize
possible_combs = list(combinations(chicken_coordinates, m))

def get_chicken_distance(house_coordinates, chicken_coordinates):
    return abs(house_coordinates[0]-chicken_coordinates[0])+abs(house_coordinates[1]-chicken_coordinates[1])

#치킨집이 이렇게 남은 상황일 때
for comb in possible_combs:
    #key는 house의 y, x 좌표이다
    for _, key in enumerate(house_coordinates):
        for chicken in comb:
            house_coordinates[key] = min(house_coordinates[key], get_chicken_distance(key, chicken))
    min_ans = min(min_ans, sum(house_coordinates.values()))

    #딕셔너리 재초기화
    for _, key in enumerate(house_coordinates):
        house_coordinates[key] = sys.maxsize
print(min_ans)