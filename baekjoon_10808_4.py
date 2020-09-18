'''
Problem Solving Baekjoon 10808_3
Author: Injun Son
Date: August 24, 2020
'''
import sys

string = input()

for i in range(ord('a'), ord('z')+1):
    print(string.count(chr(i)), end=" ")