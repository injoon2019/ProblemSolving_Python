'''
Problem Solving Baekjoon 5525
Author: Injun Son
Date: August 27, 2020
'''
import sys

N = int(input())
M = int(input())
S = input()

answer = 0
pattern = 0
i= 1
while i< M-1:
    if S[i-1]=='I' and S[i]=='O' and S[i+1]=='I':
        pattern +=1
        if pattern ==N:
            answer +=1
            pattern -=1
        i+=1
    else:
        pattern = 0
    i+=1

print(answer)