'''
Problem Solving Baekjoon 2635
Author: Injun Son
Date: August 29, 2020
'''
start = int(input())

max_length = 2
answer = []
for i in range(1, start+1):
    x = start
    y = i
    ans = [x, y]
    length = 2
    while x >=0 and y>=0:
        x = ans[-2] - ans[-1]
        if x < 0:
            break
        else:
            length +=1
            ans.append(x)
            if length > max_length:
                max_length = length
                answer = ans
        y = ans[-2] - ans[-1]
        if y < 0:
            break
        else:
            length +=1
            ans.append(y)
            if length > max_length:
                max_length = length
                answer = ans
print(len(answer))
print(' '.join(map(str, answer)))