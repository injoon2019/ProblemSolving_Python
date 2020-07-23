'''
Problem Solving Baekjoon 11655
Author: Injun Son
Date: July 23, 2020
'''
import sys

str = sys.stdin.readline().rstrip()
alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha_upper = alpha.upper()
for i in range(len(str)):
    if (ord(str[i])>=ord('a') and ord(str[i])<=ord('z')) or ord(str[i])>=ord('A') and ord(str[i])<=ord('Z'):
        if ord(str[i])>=ord('a') and ord(str[i])<=ord('z'):
            print(alpha[ (ord(str[i])-ord('a')+13) %26  ], end="")
        if ord(str[i])>=ord('A') and ord(str[i])<=ord('Z'):
            print(alpha_upper[ (ord(str[i])-ord('A')+13) %26  ], end="")
    else:
        print(str[i], end="")