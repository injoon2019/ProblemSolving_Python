'''
Problem Solving Baekjoon 1918_2
Author: Injun Son
Date: September 3, 2020
'''
from collections import deque
import sys
str = sys.stdin.readline().strip()
stack = []
prior = {"*":2, "/":2, "+":1, "-":1, "(":0}
post_list = []
for ch in '('+str+')':
    #알파벳이면
    if ch.isupper():
        post_list.append(ch)
    elif ch=='(':
        stack.append(ch)
    elif ch==')':
        while True:
            x = stack.pop()
            if x=='(':
                break
            post_list.append(x)
    #연산자면
    else:
        while stack[-1] !='(' and prior[ch] <= prior[stack[-1]]:
            post_list.append(stack.pop())
        stack.append(ch)

print(''.join(post_list))

'''
연산자 우선순위 지정
후위 표현식으로 만들어져 반환될 리스트 생성
중위 표현식을 왼쪽부터 한 글짜씩 읽음
피연산자면 리스트에 append
'('이면 스택에 PUSH, ')'이면 '('가 나올때까지 스택에서 POP, 리스트에 append
연산자면 스택에서 이보다 높은 우선순위들 POP, 리스트에 append
그리고 이 연산자를 스택에 PUSH
스택에 남아있는 연산자는 모두 POP, 리스트에 append
'''