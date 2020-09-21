'''
Problem Solving Baekjoon 14867
Author: Injun Son
Date: September 19, 2020
'''
from collections import deque
import sys, copy
from itertools import permutations

'''
가능한 옵션
1. A 채우기
2. B 채우기
3. A에 있는 것 그냥 버리기
4. B에 있는 것 그냥 버리기 
5. A를 B에 붓기
    1-1. A에 남아 있는 양과 B에 남아 있는 물이 B의 용량보다 많은 경우
    1-2. 용량보다 많지 않은 경우
6. B를 A에 붇기
    2-1. B에 남아 있는 양과 A에 남아 있는 물이 A의 용량보다 많은 경우
    2-2. 용량보다 많지 않은 경우
'''


def bfs(x, y, z, k):
    q = deque()
    check = dict()
    check[(x, y)] = 1
    cnt = 0
    q.append([x, y, cnt])
    while q:
        x, y, cnt = q.popleft()
        waters = [x, y]
        if waters[0]==z and waters[1]==k:
            print(cnt)
            return

        for i in range(6):
            waters_copy = copy.deepcopy(waters)
            if i==0: #A 채우기
                waters_copy[0] = water_limit[0]
                if tuple(waters_copy) not in check:
                    check[tuple(waters_copy)] = 1
                    waters_copy.append(cnt+1)
                    q.append(waters_copy)

            elif i==1: #B 채우기
                waters_copy[1] = water_limit[1]
                if tuple(waters_copy) not in check:
                    check[tuple(waters_copy)] = 1
                    waters_copy.append(cnt + 1)
                    q.append(waters_copy)

            elif i==2: #A에 있는 것 그냥 버리기
                waters_copy[0] = 0
                if tuple(waters_copy) not in check:
                    check[tuple(waters_copy)] = 1
                    waters_copy.append(cnt + 1)
                    q.append(waters_copy)

            elif i==3: #B에 있는 것 그냥 버리기
                waters_copy[1] = 0
                if tuple(waters_copy) not in check:
                    check[tuple(waters_copy)] = 1
                    waters_copy.append(cnt + 1)
                    q.append(waters_copy)

            elif i==4: # A를 B에 붓기
                #A와 B에 현재 있는 용량이 B의 맥시멈보다 많을 경우
                if waters[0]+waters[1] > water_limit[1]:
                    waters_copy[0] = waters_copy[0] - (water_limit[1]-waters_copy[1]) #B의 빈공간만큼만 A에서 뺀다
                    waters_copy[1] = water_limit[1]
                else:
                    waters_copy[1] = waters_copy[1] + waters_copy[0]
                    waters_copy[0] = 0

                if tuple(waters_copy) not in check:
                    check[tuple(waters_copy)] = 1
                    waters_copy.append(cnt + 1)
                    q.append(waters_copy)

            elif i==5: # B를 A에 붓기
                #A와 B에 현재 있는 용량이 A의 맥시멈보다 많을 경우
                if waters[0]+waters[1] > water_limit[0]:
                    waters_copy[1] = waters_copy[1] - (water_limit[0]-waters_copy[0]) #A의 빈공간만큼만 B에서 뺀다
                    waters_copy[0] = water_limit[0]
                else:
                    waters_copy[0] = waters_copy[0] + waters_copy[1]
                    waters_copy[1] = 0

                if tuple(waters_copy) not in check:
                    check[tuple(waters_copy)] = 1
                    waters_copy.append(cnt + 1)
                    q.append(waters_copy)

    print(-1)

a, b, c, d = map(int, input().split())
water_limit = [a, b]
bfs(0, 0, c, d)