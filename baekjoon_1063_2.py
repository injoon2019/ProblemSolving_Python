'''
Problem Solving Baekjoon 1063_2
Author: Injun Son
Date: October 17, 2020
'''

from collections import deque
import sys

m = {'R': (0,1), 'L':(0,-1), 'B':(-1,0), 'T':(1,0), 'RT':(1,1), 'LT':(1,-1), 'RB':(-1,1), 'LB': (-1, -1)}

def to_cord2(s):
    return (int(s[1])-1, ord(s[0]) -ord('A'))

def to_cord1(n):
    return (chr(ord('A')+n[1]) + str(n[0]+1))

class Chess:
    def __init__(self, king, stone):
        self.king = king
        self.stone = stone

    def move(self, command):
        king2 = (self.king[0] + m[command][0], self.king[1] + m[command][1])
        if king2[0] < 0 or king2[0] >= 8 or king2[1] < 0 or king2[1] >= 8:
            return

        if self.stone == king2:
            stone2 = (self.stone[0]+ m[command][0], self.stone[1]+m[command][1])

            if stone2[0]< 0 or stone2[0]>=8 or stone2[1] < 0 or stone2[1]>=8:
                return

            self.king = king2
            self.stone = stone2

        else:
            self.king = king2


king, stone, N = input().split()
king = to_cord2(king)
stone = to_cord2(stone)
N = int(N)

chess = Chess(king, stone)
for _ in range(N):
    chess.move(input())
print(to_cord1(chess.king))
print(to_cord1(chess.stone))