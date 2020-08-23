'''
Problem Solving Baekjoon 13458
Author: Injun Son
Date: August 23, 2020
'''
from collections import deque
import sys

N = int(input())
students = list(map(int, input().split()))
B, C = map(int, input().split())
sum = 0
for student in students:
    student -= B
    sum +=1
    if student >= 1:
        if student % C ==0:
            sum += (student//C)
        else:
            sum += (student//C)+1

print(sum)