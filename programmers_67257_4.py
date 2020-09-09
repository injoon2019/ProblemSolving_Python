'''
Problem Solving Programmers 67257_4
Author: Injun Son
Date: September 8, 2020
'''

expression = "100-200*300-500+20"
import re
from itertools import permutations

priorities = permutations(['+', '-', '*'])

def solution(expression):
    answer = 0
    for priority in priorities:
        num = re.split(r'[+\-*]', expression)
        opr  =re.split(r'[0-9]+', expression)[1:-1]
        for x in priority:
            while x in opr:
                idx = opr.index(x)
                a = num[idx]
                operator = opr[idx]
                b = num[idx+1]
                tmp = str(eval(a+operator+b))
                num.pop(idx+1)
                opr.pop(idx)
                num[idx] = tmp
        answer= max(answer, abs(int(num[0])))
    return answer
print(solution(expression))


solution(expression)