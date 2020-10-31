'''
Problem Solving Programmers winter_coding_1
Author: Injun Son
Date: October 31, 2020
'''
import math
from itertools import combinations

def solution(n, delivery):
    answer = ''
    answer_list = ['?']*n
    delivery_copy = delivery

    #확실히 있는 것 제거
    for item in delivery_copy[:]:
        if item[2]==1:
            answer_list[item[0]-1]='O'
            answer_list[item[1]-1]='O'

    #하나는 있는 경우, 다른 하나는 확실히 없는 것이다
    for item in delivery_copy[:]:
        if item[2]==1:
            continue
        if answer_list[item[0]-1] =='O':
            answer_list[item[1]-1]='X'

        if answer_list[item[1]-1] =='O':
            answer_list[item[0]-1]='X'

    return ''.join(answer_list)

# print(solution(6, [[1,3,1],[3,5,0],[5,4,0],[2,5,0]]))
# print(solution(7, [[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]]))
print(solution(4, [[1,2,1]]))