'''
Problem Solving Programmers 42577
Author: Injun Son
Date: Dec 22, 2020
'''
import math
from itertools import combinations
from itertools import combinations
from collections import defaultdict


def solution(prices):
    # 각 칸이 끝날 때까지 작은 칸을 만나지 않는다고 가정하고 초기화 한다
    answer = [i for i in range(len(prices) - 1, -1, -1)]
    stack = []  # 스택에는 값이 아닌 인덱스를 저장한다

    for i in range(len(prices)):
        # 만약 가격이 스택 맨위의 가격보다 낮다면 스택에서 그 가격보다 낮은 것들을 빼고, 그 answer의 인덱스에는 얼마나 지났는지 계산해서 넣어준다.
        while stack and prices[i] < prices[stack[-1]]:
            answer[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)

    return answer


print(solution([1, 2, 3, 2, 3]))
print(solution([5, 6, 3, 4, 2]))
