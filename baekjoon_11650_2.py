'''
Problem Solving Baekjoon 11650_@
Author: Injun Son
Date: July 20, 2020
'''

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

answer= sorted(arr, key = lambda x: (x[0], x[1]))

for i in answer:
    print(i[0], i[1])

'''
1. list of tuple로 입력받기
2. 두 개 이상의 기준으로 정렬하기
'''