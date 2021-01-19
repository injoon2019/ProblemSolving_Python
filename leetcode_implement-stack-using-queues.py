'''
Problem Solving leetcode implement-stack-using-queues
Author: Injun Son
Date: January 19, 2021
'''
import sys
from collections import deque
from typing import List

sys.setrecursionlimit(100000)
import re
from collections import deque

class MyStack:

    def __init__(self):
        q1 = deque()
        q2 = deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1.append(x)
        while self.q2:
            self.q1.append(self.q2.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q1.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q1[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1)==0

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(x)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()