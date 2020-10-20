'''
Problem Solving Programmers 12977
Author: Injun Son
Date: October 20, 2020
'''
import math
from itertools import combinations

def sumPrime(num_list):
    erathos = [True]*5000
    erathos[0] = erathos[1] = False
    count = 0

    def Erathos():
        for i in range(2, int(math.sqrt(5000))+1):
            for j in range(i*2, 5000, i):
                erathos[j] = False

    Erathos()
    possible_combs = list(combinations(num_list, 3))

    for comb in possible_combs:
        tmp_sum = sum(comb)
        if erathos[tmp_sum] ==True:
            count +=1

    return count

print(sumPrime([1,2,3,4]))
print(sumPrime([1,2,7,6,4]))