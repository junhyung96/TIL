# 과제 최대값..

# N 개의 줄에 두 정수 1 <= d <= 1000, 1 <= w <= 100 이 주어짐
# d : 과제 마감일까지 남은 일 수, w : 과제의 점수

# 하루에 하나의 과제를 끝낼 수 있음

import sys
input = sys.stdin.readline

result = 0
N = int(input())
assignments = []
for i in range(N):
    d, w = map(int, input().split())
    assignments.append([d, w, 0])
assignments.append([0, 0, 0])

# 마지막날부터 현재날로부터 마감일이 이후인 것들 중 제일 큰 점수를 배치
for day in range(N, 0, -1):
    max_index = -1
    max_score = 0
    for j in range(N):
    # for d, w, isSubmitted in assignments:
        d, w, isSubmitted = assignments[j]
        if isSubmitted:
            continue
        if d < day:
            continue
        if w >= max_score:
            max_score = w
            max_index = j
    result += max_score
    assignments[max_index][2] = 1

print(result)
# 위 코드의 경우 N이 커지면 해결 불가..
