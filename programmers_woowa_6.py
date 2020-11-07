'''
Problem Solving Programmers woowa 6
Author: Injun Son
Date: November 7, 2020
'''
import math
from itertools import combinations
from itertools import combinations
import collections
from itertools import chain

def solution(logs):
    answer = []
    user_dict = collections.defaultdict(list)
    for log in logs:
        user_num, question_num, score = log.split(" ")
        # 앞에 푼 문제였다면 없애고 새로운 값을 넣는다
        #사용자번호 : [ [ 문제번호, 점수], ... ]
        for user_history in user_dict[user_num]:
            if user_history[0] == question_num:
                user_dict[user_num].remove(user_history)

        user_dict[user_num].append([question_num, score])
        user_dict[user_num].sort()

    user_list = list(user_dict.keys())
    solved_list = list(user_dict.values())

    for i in range(len(user_list)):
        for j in range(i+1, len(user_list)):
            if solved_list[i]==solved_list[j] and len(solved_list[i]) >= 5:
                answer.append(user_list[i])
                answer.append(user_list[j])

    answer = set(answer)
    answer = sorted(list(answer))
    if len(answer)==0:
        return ["None"]
    else:
        return answer

print(solution(["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]))
print(solution(["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "2001 1 100", "2001 2 100", "2001 4 100", "2001 7 95", "2001 9 100", "2002 1 95", "2002 2 100", "2002 4 100", "2002 7 100", "2002 9 100"]))
print(solution(["1901 10 50", "1909 10 50"]))
