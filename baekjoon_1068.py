'''
Problem Solving Baekjoon 1068
Author: Injun Son
Date: August 31, 2020
'''
import sys, copy
from collections import deque

class Node:
    def __init__(self):
        self.child = []
    def setChild(self, node):
        self.child.append(node)
    def removeChild(self, node):
        self.child.remove(node)

def preorder(node):
    global cnt
    if node.child ==[]:
        cnt +=1
    for child in node.child:
        preorder(tree[child])

N = int(input())
tree = [Node() for _ in range(N)]
cnt = 0
parents = list(map(int, input().split()))

for i in range(N):
    if parents[i] != -1:
        tree[parents[i]].setChild(i)

if N!= 1:
    i = int(input())
    if parents[i] == -1:
        cnt = 0
    else:
        tree[parents[i]].removeChild(i)
        preorder(tree[parents.index(-1)])
print(cnt)