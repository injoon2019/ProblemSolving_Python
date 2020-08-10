'''
Problem Solving Baekjoon 11729
Author: Injun Son
Date: August 10, 2020
'''
import sys
from collections import deque

stackList = []
stackList.append([])
stack1 = []
stack2 = []
stack3 = []
N = int(input())
stack1 = [i for i in range(N, 0, -1)]
stackList.append(stack1)
stackList.append(stack2)
stackList.append(stack3)
count = 0
answer_list = []
def move(origin, dest):
    global count
    answer_list.append([origin, dest])
    count +=1
    stackList[dest].append(stackList[origin].pop())

def hanoi(n, origin, by, dest):
    if n==1:
        move(origin, dest)
    else:
        hanoi(n-1, origin, dest, by)
        move(origin, dest)
        hanoi(n-1, by, origin, dest)

hanoi(N, 1, 2, 3)
print(count)
for a, b in answer_list:
    print(a,b)

