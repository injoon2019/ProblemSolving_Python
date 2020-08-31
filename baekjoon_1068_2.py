'''
Problem Solving Baekjoon 1068_2
Author: Injun Son
Date: August 31, 2020
'''
import sys, copy
from collections import deque

class Node:
    def __init__(self):
        self.childs = []

    def addChild(self, node):
        self.childs.append(node)

    def removeChild(self, node):
        self.childs.remove(node)

def preorder(node):
    global cnt
    if node.childs == []:
        cnt +=1
    else:
        for child in node.childs:
            preorder(tree[child])

N = int(input())
tree = [Node() for _ in range(N)]
parents = list(map(int, input().split()))
target= int(input())

for i in range(len(parents)):
    if parents[i] != -1:
        tree[parents[i]].addChild(i)

cnt = 0
if N !=1:
    if parents[target] == -1:
        cnt = 0
    else:
        tree[parents[target]].removeChild(target)
        preorder(tree[parents.index(-1)])
print(cnt)