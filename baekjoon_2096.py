'''
Problem Solving Baekjoon 2096
Author: Injun Son
Date: October 10, 2020
'''
import sys
#https://blog.naver.com/PostView.nhn?blogId=jqkt15&logNo=222088128498

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
left_max, center_max, right_max = s[0][0], s[0][1], s[0][2]
left_min, center_min, right_min = s[0][0], s[0][1], s[0][2]

for i in range(1, n):
    left_max, center_max, right_max = max(left_max, center_max)+s[i][0], max(left_max, center_max, right_max)+s[i][1], max(center_max, right_max)+ s[i][2]
    left_min, center_min, right_min = min(left_min, center_min)+s[i][0], min(left_min, center_min, right_min)+s[i][1], min(center_min, right_min)+ s[i][2]

print(max(left_max, center_max, right_max), min(left_min, center_min, right_min))