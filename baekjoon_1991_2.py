'''
Problem Solving Baekjoon 1991_2
Author: Injun Son
Date: August 3, 2020
'''
import sys
class Node:
    def __init__(self, item, lchild, rchild):
        self.item = item
        self.lchild = lchild
        self.rchild = rchild

def preorder(Node):
    print(Node.item, end="")
    if Node.lchild != '.':
        preorder(tree[Node.lchild])
    if Node.rchild != '.':
        preorder(tree[Node.rchild])

def inorder(Node):
    if Node.lchild != '.':
        inorder(tree[Node.lchild])
    print(Node.item, end="")
    if Node.rchild != '.':
        inorder(tree[Node.rchild])

def postorder(Node):
    if Node.lchild != '.':
        postorder(tree[Node.lchild])
    if Node.rchild != '.':
        postorder(tree[Node.rchild])
    print(Node.item, end="")


N = int(input())
tree = {}
for _ in range(N):
    data = input().split()
    tree[data[0]] = Node(item = data[0], lchild = data[1], rchild=data[2])

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
