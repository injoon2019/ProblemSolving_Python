'''
Problem Solving Baekjoon 10808_3
Author: Injun Son
Date: August 24, 2020
'''
import sys

str = sys.stdin.readline().rstrip()

for i in range(ord('a'), ord('z')+1):
    print(str.count(chr(i)), end=" ")