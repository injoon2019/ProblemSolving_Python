'''
Problem Solving Baekjoon 17136_2
Author: Injun Son
Date: October 13, 2020
'''

import sys

def dfs(depth):
    global n, answer, total_one

    #이미 최소값보다 뎁스가 커지면 더이상 탐색 안하고 리턴
    if answer > 0 and answer <= depth:
        return

    #남은 1이 없을 때 뎁스가 최소값보다 작다면
    if total_one ==0:
        if answer == -1 or answer > depth:
            answer = depth
        return

    # 시작점 찾기
    for y in range(n):
        for x in range(n):
            if MAP[y][x]:
                break
        if MAP[y][x]:
            break

    if MAP[y][x]:
        # 해당 점에 1~5 사이즈를 대본다
        for size in range(1, 5+1):
            if paper[size]:
                one2zero = [] #1에서 0으로 바뀐 자표 저장해서 나중에 돌려놓는다

                if is_coverable(y, x, size): #해당 사이즈로 덮을 수 있다면
                    for i in range(y, y+size):
                        for j in range(x, x+size):
                            MAP[i][j] =0 #1에서 0으로 바꾼다
                            one2zero.append((i, j)) #바꾼 좌표 저장

                    total_one -= size**(2)
                    paper[size] -=1
                    dfs(depth+1)
                    paper[size] +=1
                    total_one += size**(2)

                    # 바뀐 좌표들을 다시 0에서 1로 바꿔줌
                    for pos in one2zero:
                        MAP[pos[0]][pos[1]] = 1

#색종이로 채울 수 있는지 검사하는 함수
def is_coverable(y, x, size):
    global n
    for i in range(y, y+size):
        for j in range(x, x+size):
            if 0<=i<10 and 0<=j<10:
                if MAP[i][j]==0:
                    return False
            else:
                return False
    return True

n = 10
MAP = [list(map(int, input().split())) for _ in range(n)]
paper = [0]+ [5]*5
answer = -1
total_one = sum(sum(m) for m in MAP)
dfs(0)
print(answer)
