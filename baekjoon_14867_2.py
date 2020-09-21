'''
Problem Solving Baekjoon 14867_2
Author: Injun Son
Date: September 19, 2020
'''
from collections import deque
import sys, copy
from itertools import permutations

'''
잘 풀었는데 비슷한 방식으로 푼 다른 사람의 코드와 성능 차이가 너무 난다
확인해보자
'''

def bfs(a, b, c, d):
    visited = dict()
    queue = deque()
    queue.append((0,0))
    visited[(0,0)] = 0

    while queue:
        y, x = queue.popleft()
        if (c,d) in visited and y==c and x==d:
            return print(visited[(c, d)])

        #A 채우기
        if y < a and not(a,x) in visited:
            visited[(a,x)] = visited[(y,x)]+1
            queue.append((a,x))

        #B 채우기
        if x<b and not (y, b) in visited:
            visited[(y, b)] = visited[(y, x)]+1
            queue.append((y, b))

        #A 비우기
        if not (0, x) in visited:
            visited[(0, x)] = visited[(y, x)]+1
            queue.append((0,x))

        #B비우기
        if not (y,0) in visited:
            visited[(y,0)] = visited[(y, x)]+1
            queue.append((y,0))

        #A에서 B로 붓기
        #최대 용량 안넘기는 경우
        if not (0, x+y) in visited and y <= b-x:
            visited[(0, x+y)] = visited[(y, x)]+1
            queue.append((0, x+y))

        #최대용량 넘기는 경우
        if not (y-(b-x), b) in visited and y > b-x:
            visited[(y-(b-x), b)] = visited[(y, x)] +1
            queue.append((y-(b-x), b))

        #B에서 A로 붓기
        if not (y+x, 0) in visited and x <= a-y:
            visited[(y+x, 0)] = visited[(y, x)] +1
            queue.append((y+x, 0))

        if not (a, x-(a-y)) in visited and x> a-y:
            visited[(a, x-(a-y))] = visited[(y, x)]+1
            queue.append((a, x-(a-y)))

    return print(-1)

a, b, c, d = map(int, input().split())
bfs(a, b, c, d)