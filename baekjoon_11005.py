'''
Problem Solving Baekjoon 11005
Author: Injun Son
Date: July 24, 2020
'''
import sys
import math

arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A',
       'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
       'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
       'V', 'W', 'X', 'Y', 'Z']
N, B = map(int, input().split())
string = []
while N !=0:
    string.append(arr[N%B])
    N //=B

string.reverse()
print("".join(string))