'''
Problem Solving Baekjoon 10808_2
Author: Injun Son
Date: July 23, 2020
'''
import sys

str = sys.stdin.readline().rstrip()

for i in range(ord('a'), ord('z')):
    print(str.count(chr(i)), end=" ")