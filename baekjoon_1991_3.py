'''
Problem Solving Baekjoon 1991_3
Author: Injun Son
Date: August 20, 2020
'''
import sys
class Node:
    def __init__(self, data, lchild, rchild):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

def preorder(Node):
    print(Node.data, end="")
    if Node.lchild != '.':
        preorder(tree[Node.lchild])
    if Node.rchild != '.':
        preorder(tree[Node.rchild])

def inorder(Node):
    if Node.lchild != '.':
        inorder(tree[Node.lchild])
    print(Node.data, end="")
    if Node.rchild != '.':
        inorder(tree[Node.rchild])

def postorder(Node):
    if Node.lchild != '.':
        postorder(tree[Node.lchild])
    if Node.rchild != '.':
        postorder(tree[Node.rchild])
    print(Node.data, end="")

N = int(input())
tree = {}
for _ in range(N):
    arr = list(input().split())
    tree[arr[0]] = Node(arr[0], arr[1], arr[2])

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])