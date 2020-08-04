'''
Problem Solving Baekjoon 2745_2
Author: Injun Son
Date: July 30, 2020
'''
import sys
target_str, cipher_num = input().split()
cipher_num = int(cipher_num)

decimal_result = 0

for i in range(0, len(target_str)):
    cipher_char = target_str[len(target_str)-1-i]

    if cipher_char.isnumeric():
        decimal_result += int(cipher_char)*(cipher_num**i)
    else:
        decimal_result += (ord(cipher_char)-ord('A')+10)*(cipher_num**i)
print(decimal_result)
