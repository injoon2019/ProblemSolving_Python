'''
Problem Solving Baekjoon 10828
Author: Injun Son
Date: July 21, 2020
'''
import sys
stack = []

def process_stack(command):

    if command[0] == 'push':
        stack.append(command[1])

    elif command[0] == 'top':
        size = len(stack)
        if size==0:
            print(-1)
        else:
            print(stack[-1])

    elif command[0] == 'size':
        size = len(stack)
        print(size)

    elif command[0] == 'empty':
        size = len(stack)
        if size == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'pop':
        size = len(stack)
        if size==0:
            print(-1)
        else:
            print(stack.pop())


n = int(input())

for _ in range(n):
    command = sys.stdin.readline().split()
    process_stack(command)
