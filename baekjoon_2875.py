'''
Problem Solving Baekjoon 2875
Author: Injun Son
Date: August 11, 2020
'''
import sys
F, M, K = map(int, input().split())
count = 0
while count != K:
    if F >= 2*M:
        F -=1
        count +=1
    else:
        M -=1
        count +=1

print(min(M, F//2))