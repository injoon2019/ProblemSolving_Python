'''
Problem Solving Programmers woowa 3
Author: Injun Son
Date: November 7, 2020
'''
import math
from itertools import combinations
from itertools import combinations

def solution(money, expected, actual):
    answer = money
    bet_money = 100
    for i in range(len(expected)):
        # 돈이 하나도 안남은 경우 0을 반환하고 종료한다
        if answer == 0:
            return 0

        # 이전판의 돈의 두배를 걸어야하는데 남은 돈이 그것보다 적다면 남은걸 모두 건다
        if answer < bet_money:
            bet_money = answer

        # 딴 경우, 돈에 베팅한 돈을 추가하고, 베팅 머니는 100으로 만든다
        if expected[i] == actual[i]:
            answer += bet_money
            bet_money = 100

        # 진 경우, 베팅한 돈을 감소시키고, 베팅머니는 두배로 증가시킨다
        elif expected[i] != actual[i]:
            answer -= bet_money
            bet_money *= 2
    return answer

print(solution(1000, ['H', 'T', 'H', 'T', 'H', 'T', 'H'], ['T', 'T', 'H', 'H', 'T', 'T', 'H']))
print(solution(1200, ['T', 'T', 'H', 'H', 'H'], ['H', 'H', 'T', 'H', 'T']))
print(solution(1500, ['H', 'H', 'H', 'T', 'H'], ['T', 'T', 'T', 'H', 'T']))