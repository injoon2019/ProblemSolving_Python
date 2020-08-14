'''
Problem Solving Baekjoon 1107
Author: Injun Son
Date: August 14, 2020
'''
target = int(input())
M = int(input())
answer = abs(100-target)
if M!=0:
    broken_buttons = list(map(int, input().split()))
if M==0:
    print(min(len(str(target)), answer))
    exit()
not_broken_buttons = [True]*10

for i in range(10):
    if i in broken_buttons:
        not_broken_buttons[i]=False

def canMove(channel):
    length = 0
    if channel == 0:
        if not_broken_buttons[channel]== False:
            return 0
        else:
            return 1

    while channel>0:
        if not_broken_buttons[channel%10] == False:
            return 0
        length+=1
        channel //=10
    return length


for i in range(0, 1000001):
    c = i
    length = canMove(c)
    if length >0 :
        press = abs(c - target)
        answer = min(answer, press+length)

print(answer)