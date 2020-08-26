'''
Problem Solving Baekjoon 1991_4
Author: Injun Son
Date: August 25, 2020
'''
import sys
class Node:
    def __init__(self, data, lchild, rchild):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

N = int(input())
tree = {}

for _ in range(N):
    node_num, lchild_num, rchild_num = input().split()
    node = Node(node_num, lchild_num, rchild_num)
    tree[node_num] = node

def pre_order(start_node_num):
    Node = tree[start_node_num]
    print(Node.data, end="")
    if Node.lchild != '.':
        pre_order(Node.lchild)
    if Node.rchild != '.':
        pre_order(Node.rchild)

def in_order(start_node_num):
    Node = tree[start_node_num]
    if Node.lchild != '.':
        in_order(Node.lchild)
    print(Node.data, end="")
    if Node.rchild != '.':
        in_order(Node.rchild)

def post_order(start_node_num):
    Node = tree[start_node_num]
    if Node.lchild != '.':
        post_order(Node.lchild)
    if Node.rchild != '.':
        post_order(Node.rchild)
    print(Node.data, end="")

pre_order('A')
print()
in_order('A')
print()
post_order('A')
