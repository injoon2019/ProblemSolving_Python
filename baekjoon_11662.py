'''
Problem Solving Baekjoon 11662
Author: Injun Son
Date: August 10, 2020
'''
import sys
import math
import math
arr = list(map(int, input().split()))
Ax , Ay = arr[0], arr[1]
Bx , By = arr[2], arr[3]
Cx , Cy = arr[4], arr[5]
Dx , Dy = arr[6], arr[7]

min_dist = sys.maxsize
def calc_dist(x1, y1, x2, y2):
    dist = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
    return dist

interval = 1000000
M_xa, M_ya = (Bx - Ax) / interval, (By - Ay) / interval
K_xa, K_ya = (Dx - Cx) / interval, (Dy - Cy) / interval
for i in range(1000001):
    dist = calc_dist(Ax+ M_xa*i, Ay+ M_ya*i, Cx+ K_xa*i,  Cy+ K_ya*i)
    min_dist = min(dist, min_dist)

print(min_dist)
#print('{:0.10f}'.format(min_dist))