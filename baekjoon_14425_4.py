'''
Problem Solving Baekjoon 14425_4
Author: Injun Son
Date: September 9, 2020
'''
import sys
import math
import sys
#트라이 알고리즘으로 풀기
#https://developmentdiary.tistory.com/459

input = sys.stdin.readline

class Node:
    def __init__(self, chr):
        self.chr = chr
        self.child = {}
        self.check = False

#해당 문자열이 있는지 확인
def triedfs(node, s, n):
    if len(s)==n:
        if node.check:
            result.append(s)
            return
        else:
            return

    if s[n] in node.child:
        triedfs(node.child[s[n]], s, n+1)
    return

trie = Node('')
N, M = map(int, input().split())
for _ in range(N):
    tmp = trie
    word = input().rstrip()
    for i in range(len(word)): #문자열 추가
        if word[i] in tmp.child: #해당 문자가 있으면
            tmp = tmp.child[word[i]] #해당 문자의 노드로 이동
            if i==len(word)-1:
                tmp.check = True

        else:
            a = Node(word[i])
            tmp.child[word[i]] = a
            tmp = a
            if i==len(word)-1:
                tmp.check = True

result = []
for _ in range(M):
    p = input().rstrip()
    triedfs(trie, p, 0)

print(len(result))
