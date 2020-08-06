'''
Problem Solving Baekjoon 1931
Author: Injun Son
Date: August 6, 2020
'''
N = int(input())
times = []
for _ in range(N):
    start, finish = map(int, input().split())
    times.append((start, finish))

times.sort(key=lambda x: (x[1], x[0]))
count = 0
cur_finish=0
for start, finish in times:
    if start >= cur_finish:
        cur_finish = finish
        count +=1

print(count)

'''
현재 t1 시간까지 도달했다고 하고, 현재 가능한 회의가 a1, a2, a3, a4, ... 가 있으며 a1이 가장 일찍 끝나는 회의라고 해봅시다.
a1이 아닌 a_i를 사용해서 스케쥴을 만들어놓은 상황을 생각해보면, a_i 대신 a1을 사용해도 그 스케쥴은 여전히 조건을 만족하며 회의의 수는 동일합니다.
즉 끝나는 시간이 가장 이르지 않은 회의를 포함한 최대 스케쥴을 만들었을 경우, 회의를 바꿔치기해서 끝나는 시간이 가장 이른 회의만으로도
 최대 스케쥴을 만들 수 있으므로 해당 그리디가 성립합니다.
'''