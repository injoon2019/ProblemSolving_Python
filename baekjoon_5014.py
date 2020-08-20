'''
Problem Solving Baekjoon 5014
Author: Injun Son
Date: August 20, 2020
'''
from collections import deque
import sys, copy
from itertools import permutations
def bfs():
    global curret_floor
    q = deque()
    q.append([curret_floor, 0])
    visited[curret_floor] = 0

    while q:
        current_pos, count = q.popleft()
        if current_pos == target:
            return count

        if current_pos+U <= height and visited[current_pos+U]>count+1:
            visited[current_pos + U] = count + 1
            q.append([current_pos+U, count+1])

        if current_pos-D >= 1 and visited[current_pos-D]>count+1:
            visited[current_pos - D] = count + 1
            q.append([current_pos-D, count+1])

    return "use the stairs"

height, curret_floor, target, U, D = map(int, input().split())
visited = [sys.maxsize]*(height+1)
print(bfs())