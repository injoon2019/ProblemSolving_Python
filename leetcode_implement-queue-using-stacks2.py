'''
Problem Solving leetcode mplement-queue-using-stacks
Author: Injun Son
Date: October 18, 2020
'''
import sys
from collections import deque
from typing import List

sys.setrecursionlimit(100000)
import re


class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        return self.stack1.pop()

    def peek(self) -> int:
        return self.stack1[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0
