'''
Problem Solving Programmers 42577
Author: Injun Son
Date: Dec 21, 2020
'''
import math
from itertools import combinations
from itertools import combinations
from collections import defaultdict


def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in phone_book[i + 1:]:
            if phone_book[i] in j:
                return False
    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
