'''
Problem Solving Programmers woowa 2
Author: Injun Son
Date: November 7, 2020
'''
import math
from itertools import combinations
from itertools import combinations

def solution(s, op):
    answer = []
    for i in range(1, len(s)):
        num1 = int(s[:i])
        num2 = int(s[i:])
        temp = 0
        if op == "+":
            temp = num1 + num2
        elif op == "-":
            temp = num1 - num2
        elif op == '*':
            temp = num1 * num2

        answer.append(temp)
    return answer

print(solution("1234", "+"))
print(solution("987987", "-"))
print(solution("31402", "*"))

# Custom Test Case
print(solution("12", "*"))