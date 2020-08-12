'''
Problem Solving Baekjoon 1783
Author: Injun Son
Date: August 12, 2020
'''
#세로 길이 N와 가로 길이 M
'''
case1: 세로 3이상, 가로 7이상
case2: 세로 3이상, 가로 7미만
case3: 세로 3미만, 가로 7이상
case4: 세로 3미만, 가로 7미만 
'''
r, c = map(int, input().split())
count =1
if r==1 or c==1:
    print(1)
    exit()

if r>=3 and c>=7:
    count +=4
    count += (c-7)
    print(count)
elif r>=3 and c<7:
    print(min(4, c))
elif r<3 and c>=7:
    tmp = c - 1
    count += (tmp // 2)
    print(min(count, 4))
elif r<3 and c<7:
    tmp = c-1
    count += (tmp//2)
    print(count)