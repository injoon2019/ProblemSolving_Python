'''
Problem Solving Baekjoon 1697_2
Author: Injun Son
Date: August 15, 2020
'''
import sys
from collections import deque
sys.setrecursionlimit(100000)
MAX = 100001
def solve():
    while q:
        cur = q.popleft()
        if cur == y:
            return visited_nums[cur]
        nextPos(cur-1, cur)
        nextPos(cur+1, cur)
        nextPos(cur*2, cur)

def nextPos(nex, cur):
    #nex가 범위 내에 있고
    #한번도 방문하지 않았거나, 최소 time으로 방문한 경우
    if 0<= nex< MAX and (visited_nums[nex]==0 or visited_nums[cur]+1 < visited_nums[nex]):
        visited_nums[nex] = visited_nums[cur]+1
        q.append(nex)

x, y = map(int, input().split())
visited_nums = [0]*(MAX)
q = deque([x])
print(solve())