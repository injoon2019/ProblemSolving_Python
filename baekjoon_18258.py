'''
Problem Solving Baekjoon 18258
Author: Injun Son
Date: August 4, 2020
'''
import sys
queue = [0]*2000001
front=0
rear=-1
size=0
N = int(sys.stdin.readline())
for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        rear +=1
        size +=1
        queue[rear] = int(command[1])
    if command[0] == 'front':
        if size==0:
            print(-1)
        else:
            print(queue[front])
    if command[0] == 'back':
        if size==0:
            print(-1)
        else:
            print(queue[rear])
    if command[0] == 'size':
        print(size)
    if command[0] == 'empty':
        if size==0:
            print(1)
        else:
            print(0)
    if command[0] == 'pop':
        if size==0:
            print(-1)
        else:
            print(queue[front])
            front+=1
            size -=1