'''
Problem Solving Baekjoon 10809_2
Author: Injun Son
Date: July 23, 2020
'''
import sys

str = sys.stdin.readline().rstrip()
for i in range(26):
    print(str.find(chr(97+i)), end = " ")