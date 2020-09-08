'''
Problem Solving Programmers 67257_2
Author: Injun Son
Date: September 8, 2020
'''

expression = "100-200*300-500+20"
import re
from itertools import permutations

priorities = permutations(['*','+','-']) # 연산자 순열

def solution(expression):
    answer = 0
    for priority in priorities:
        num = re.split('[*+-]',expression) # 숫자 배열
        opr = re.split('[0-9]+',expression)[1:-1] # 연산자 배열, 숫자로 시작하고 끝나기 때문에 [1:-1]을 안하면 처음과 끝에 빈 elem이 list에 들어간다
        # stack을 이용해 우선 연산자 계산
        for x in priority[:2]:
            while x in opr:
                idx = opr.index(x)
                tmp = num[idx]+opr[idx]+num[idx+1]
                num[idx] = str(eval(tmp))
                num.pop(idx+1)
                opr.pop(idx)
        # 마지막 계산
        tmp = ''
        for i in range(len(opr)):
            tmp += num[i] + opr[i]
        tmp = abs(eval(tmp + num[-1]))
        # 최종 값(절댓값)이 가장 큰 것을 찾음
        if tmp > answer:
            answer = tmp
    return answer

print(solution(expression))