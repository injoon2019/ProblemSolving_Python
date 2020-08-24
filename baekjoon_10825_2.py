'''
Problem Solving Baekjoon 10825_2
Author: Injun Son
Date: August 24, 2020
'''

N = int(input())
arr = []
for _ in range(N):
    name, kor, eng, math = list(input().split())
    kor, eng, math = map(int, [kor, eng, math])
    arr.append([name, kor, eng, math])

arr.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))
for i in arr:
    print(i[0])