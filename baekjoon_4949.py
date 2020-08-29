'''
Problem Solving Baekjoon 4949
Author: Injun Son
Date: August 29, 2020
'''
import sys
from collections import deque
string = input()
while string != '.':
    stack = []
    is_True = True
    for i in string:
        if i=="(" or i=="[":
             stack.append(i)
        elif i==")" or i=="]":
            if i==")":
                if len(stack) > 0:
                    c = stack.pop()
                    if c != "(":
                        is_True = False
                        break
                else:
                    is_True = False
                    break
            elif i=="]":
                if len(stack)>0:
                    c = stack.pop()
                    if c!="[":
                        is_True = False
                        break
                else:
                    is_True = False
                    break
    if is_True and len(stack)==0:
        print("yes")
    else:
        print("no")
    string = input()

