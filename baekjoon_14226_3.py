'''
Problem Solving Baekjoon 14226_3
Author: Injun Son
Date: September 9, 2020
'''
import sys
import math
from collections import deque

n = int(input())

q = deque()
q.append((1,0))

visited = dict()
visited[(1,0)] = 0
while q:
    s, c = q.popleft()
    if s==n:
        print(visited[(s,c)])
        sys.exit()
    if (s,s) not in visited.keys() and 1<=s<2001:
        visited[(s,s)] = visited[(s,c)]+1
        q.append((s,s))
    if (s-1,c) not in visited.keys() and 1<=s-1<1001 and 1<=c<2001:
        visited[(s-1,c)] = visited[(s,c)]+1
        q.append((s-1,c))
    if (s+c, c) not in visited.keys() and 1<=s+c<1001 and 1<=c<2001:
        visited[(s+c, c)] = visited[(s,c)]+1
        q.append((s+c, c))


'''
이 방법과 똑같은 방법으로 풀다가 틀리신 분을 봤었는데, 반례가 매우 드물게 있고 손으로 계산 가능한 정도가 아니기 때문에 반례를 알려드리는 것은 크게 의미가 없을 것 같습니다. 
하나 드리자면, 872에 대한 정답은 22이지만 이 코드는 23을 출력합니다.
기본적으로 BFS는 "현재 상태"를 나타내는 모든 변수들이 전부 개별적으로 고려되어야 합니다. 
지금 코드를 보면, 횟수를 나타내는 cnt를 제외하고 num과 clipboard라는 2개의 변수를 큐에 담고 있음에도 불구하고 
방문 체크는 오로지 num에 대해서만 하고 있습니다. 이렇게 하면 최적해가 나오지 않을 수 있습니다.
예를 들어 A라는 수의 이모티콘을 화면에 최대한 빨리 출력하는 순간에 클립보드에는 B개의 이모티콘이 담겨있다고 해봅시다. 
그런데 A개의 이모티콘을 화면에 출력하는 데에는 더 오랜 시간이 걸리지만 이 때 C개의 이모티콘이 클립보드에 담겨있는 경우 D개를 화면에 출력하는 시간을 더 단축하는 경우가 있을 수 있습니다.
 이 코드는 그런 경우를 처리하지 못합니다. A개를 출력하는 순간 C개의 이모티콘이 클립보드에 담긴 상황을 이미 배제해버리기 때문입니다.
그래서 이런 문제에 대해 정확한 BFS를 구현하려면 num과 clipboard 값 둘 다를 모두 고려해야 합니다. 
visited[num][clipboard]와 같이 사용하도록 해야 합니다. 이 문제 뿐만 아니라, 
어떠한 BFS든 서로 종속적이지 않은 변수들을 큐에 넣어야 한다면 방문 체크 역시 각각을 별개의 차원으로 놓고 해야 합니다.
'''
