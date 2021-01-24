'''
Problem Solving leetcode combinations
Author: Injun Son
Date: October 23, 2020
'''
import sys
import collections
import heapq
import functools
import itertools
import re
import math
import bisect
from typing import *

import itertools

class tmp:
    def __init__(self, val= 0):
        self.val = val

class_example1 = tmp(10)
class_example2 = tmp(20)
#
# print(class_example1.val)
# print(class_example2.val)

print(id(class_example1), id(class_example2))
def swap(a, b):
    # print(id(a), id(b))
    tmp = a
    a = b
    b = tmp
    # print(id(a), id(b))

swap(class_example1,class_example2)
print(id(class_example1), id(class_example2))
# print(a, b)