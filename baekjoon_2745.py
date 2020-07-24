'''
Problem Solving Baekjoon 2745
Author: Injun Son
Date: July 24, 2020
'''
import sys
N, B = input().split()
B = int(B)
dic = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10,
       'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':18, 'J':19, 'K':20,
       'L':21, 'M':22, 'N':23, 'O':24, 'P':25, 'Q':26, 'R':27, 'S':28, 'T':29, 'U':30,
       'V':31, 'W':32, 'X':33, 'Y':34, 'Z':35}

sum = 0
for i in range(0, len(N)):
    sum += (B**(len(N)-i-1)) *dic[N[i]]

print(sum)

'''
n, base = input().split()
print(int(n, base=int(base)))
'''