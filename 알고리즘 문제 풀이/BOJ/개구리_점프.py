import sys
input = sys.stdin.readline
# 통나무 N개가 가로 (수평) 방향으로 연못에 떠 있다. 
# 개구리는 한 통나무 A에서 다른 통나무 B로 정확히 수직 방향으로 점프할 수 있다. 
# 단, 점프할 때 다른 통나무 위를 (끝 점 포함) 지나면 안된다.

# 예를 들어 <그림 1>에서 1번 통나무에서 2번 통나무로 점선을 따라 개구리가 점프하는 것이 가능하다. 
# 1번 통나무에서 2번 통나무로 점프한 후 다시 3번 통나무로 점프하면 1번 통나무에서 3번 통나무로 이동하는 것이 가능하다. 
# (통나무 위에서 걸어서 움직이는 것은 언제든 가능하다.)

# 통나무들의 위치를 입력받아 질문으로 주어진 통나무들의 쌍에 대해서 
# 개구리가 한 통나무에서 다른 통나무로 한번 이상의 점프로 이동이 가능한지 판단하는 프로그램을 작성하라.

N, Q = map(int, input().split())

points = []
tag = 1
for _ in range(N):
    x1, x2, y = map(int, input().split())
    points.append((x1, x2, y, tag))
    tag += 1

groups = [-1] * (N+1)
points.sort()
groups[points[0][3]] = 0
min_x = points[0][0]
max_x = points[0][1]

# print(points)
current_group_index = 0

for i in range(1, N):
    x1, x2, y, tag = points[i]
    if x1 <= max_x:
        groups[tag] = current_group_index
        if x2 > max_x:
            max_x = x2
    else:
        min_x = x1
        max_x = x2
        current_group_index += 1
        groups[tag] = current_group_index
# print(groups)

for _ in range(Q):
    s, e = map(int, input().split())
    if groups[s] == groups[e]:
        print(1)
    else:
        print(0)

# x 좌표가 겹치면 무조건 뛸 수 있다 = 다른 통나무 위를 지나면 안되지만 점프 2번하면 되는 것 아닌가?
# 겹치는 통나무를 집합으로 묶어둔다.. 새로운 집합생성....
# 연결리스트? 겹치면 앞의 통나무를 가리키게 하면?

[[1,2,3],[4]]