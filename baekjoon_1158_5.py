'''
Problem Solving Baekjoon 1158_5
Author: Injun Son
Date: August 19, 2020
'''
from collections import deque
import sys

N, K = map(int, input().split())
visited = [False]*N
ans_nums = []

class LinkedList:
    class Node:
        def __init__(self, data, link=None):
            self.data = data
            self.next_node = link

    def __init__(self):
        self.head_node = None
        self.tail_node = None
        self.size= 0

    def append(self, data, before_node = None):
        new_node = self.Node(data)

        if self.empty():
            self.head_node = new_node
            new_node.next_node = new_node
        else:
            if before_node is None:
                before_node = self.tail_node

            new_node.next_node = before_node.next_node
            before_node.next_node = new_node

        self.tail_node = new_node
        self.size +=1