'''
Problem Solving Baekjoon 9935
Author: Injun Son
Date: November 5, 2020
'''
import sys
sys.setrecursionlimit(100000)

string1 = list(input())
string2 = list(input())

stack = []

for char in string1:
    stack.append(char)

    if char == stack[-1]:
        if len(stack) >= len(string2) and stack[-len(string2):] == string2:
            for _ in range(len(string2)):
                stack.pop()

if len(stack)==0:
    print("FRULA")
else:
    print(''.join(stack))