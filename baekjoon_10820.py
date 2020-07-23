'''
Problem Solving Baekjoon 10820
Author: Injun Son
Date: July 23, 2020
'''
import sys

for line in sys.stdin:
    line = line.rstrip("\n")
    small = 0
    big = 0
    num = 0
    space = 0
    for i in range(len(line)):
        ascii = ord(line[i])
        if ascii >= ord('0') and ascii <= ord('9'):
            num +=1
        elif ascii >= ord('a') and ascii <= ord('z'):
            small +=1
        elif ascii >= ord('A') and ascii <= ord('Z'):
            big +=1
        else:
            space +=1
    print(small, big, num, space)