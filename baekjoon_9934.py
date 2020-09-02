'''
Problem Solving Baekjoon 9934
Author: Injun Son
Date: September 1, 2020
'''
import sys
import heapq

class Node:
    def __init__(self, num, lchild=None, rchild=None, building_num=None):
        self.num = num
        self.lchild = lchild
        self.rchild = rchild
        self.building_num = building_num

count = 0
def inorder(num):
    global count
    if tree[num].lchild!=None:
        inorder(tree[num].lchild.num)

    tree[num].building_num = nums[count]
    count +=1

    if tree[num].rchild!=None:
        inorder(tree[num].rchild.num)

tree = {}
K = int(input())
nums = list(map(int, input().split()))
for i in range(2**K -1):
    tree[i] = Node(i)

for i in range(2**K -1):
    if i*2 +2 < 2**K -1:
        tree[i].lchild = tree[i*2 +1]
        tree[i].rchild = tree[i*2+2]

inorder(0)
space_list= []
i=1
while i <=2*11:
    space_list.append(i)
    i = i*2 +1

count = 0
for i in range(2**K -1):
    print(tree[i].building_num, end=" ")
    count +=1
    if count in space_list:
        print("")
