'''
Problem Solving Baekjoon 1476
Author: Injun Son
Date: August 13, 2020
'''
e, s, m = map(int, input().split())
count =1
dict = {}
E, S, M = 1, 1, 1
while count <= 7980:
    dict[(E, S, M)] = count
    E = (E+1)%16
    if E==0:
        E=1
    S = (S+1)%29
    if S==0:
        S=1
    M = (M+1)%20
    if M==0:
        M=1
    count +=1

print(dict[(e,s,m)])
