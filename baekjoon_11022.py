'''
Problem Solving Baekjoon 11022
Author: Injun Son
Date: July 14, 2020
'''
import sys
T = int(input())
for i in range(0,T):
    A,B = map(int, sys.stdin.readline().split())
    print("Case #{}: {} + {} = {}".format(i+1, A, B, A+B))

'''
sys를 이용해서 라인 통쨰로 입력받기
format을 이용해서 출력하기 
'''