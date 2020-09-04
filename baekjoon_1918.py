'''
Problem Solving Baekjoon 1918
Author: Injun Son
Date: September 3, 2020
'''
from collections import deque
import sys
str = sys.stdin.readline().strip()
stack = []
prior = {'*':2, '/':2, '+':1, '-':1, '(':0}

for ch in '('+str+')':
    if ch.isupper():
        print(ch, end='')
    elif ch=='(':
        stack.append(ch)
    elif ch==')':
        while True:
            x = stack.pop()
            if x=='(':
                break
            print(x, end='')
    else:
        while stack[-1] !='(' and prior[ch] <= prior[stack[-1]]:
            print(stack.pop(), end='')
        stack.append(ch)
