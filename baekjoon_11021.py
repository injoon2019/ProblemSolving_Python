'''
Problem Solving Baekjoon 11021
Author: Injun Son
Date: July 14, 2020
'''
import sys
T = int(input())
for i in range(1,T+1):
    A,B = map(int, sys.stdin.readline().split())
    print("Case #{}: {}".format(i, A+B))


'''
stdin 을 이용해서 입력을 받는 방법
format을 이용해서 출력하는 방법
'''