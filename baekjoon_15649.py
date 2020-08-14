'''
Problem Solving Baekjoon 15649
Author: Injun Son
Date: August 13, 2020
'''
from itertools import permutations

n, m = map(int, input().split())
n_list = [i for i in range(1, n+1)]
permute = list(permutations(n_list, m))

for i in permute:
    for j in i:
        print(j, end=" ")
    print("")