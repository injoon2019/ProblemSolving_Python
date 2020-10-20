'''
Problem Solving Programmers 49993
Author: Injun Son
Date: October 20, 2020
'''
import math
from itertools import combinations

def prerequsiteSkills(skill, skill_trees):
    answer = 0
    for word in skill_trees:
        learn = []
        index = 0
        for char in word:
            if char in skill:
                if char == skill[index]:
                    index +=1
                    learn.append(char)
                else:
                    if char in learn:
                        continue
                    else:
                        break
            else:
                continue
        else:
            answer +=1

    return answer

print(prerequsiteSkills("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))