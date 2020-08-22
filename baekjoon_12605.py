'''
Problem Solving Baekjoon 12605
Author: Injun Son
Date: August 22, 2020
'''
import sys
T = int(input())
for i in range(T):
    s=''
    words = input().split()
    s += ' '.join(words[::-1])
    print(f"Case #{i+1}: ".format(i)+s)