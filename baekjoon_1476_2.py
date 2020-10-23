'''
Problem Solving Baekjoon 1476_2
Author: Injun Son
Date: October 21, 2020
'''

e, s, m = map(int, input().split())
E, S, M = 1, 1, 1
year = 1
for i in range(1, 15*28*19 +1 ):
    if E==e and S==s and M==m:
        print(year)
        break

    if 1<=E<=14:
        E+=1
    elif E==15:
        E = 1

    if 1<=S<=27:
        S+=1
    elif S==28:
        S = 1

    if 1<=M<=18:
        M +=1
    elif M==19:
        M=1

    year +=1
