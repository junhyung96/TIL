import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
# 완전히 감염된 상태인지 어떻게 구분할 것인지
# 해당 위치로 전염된 시점 저장하기
# graph[n][m] = [바이러스명, 침투된시간]
graph = [[[] for _ in range(M)] for _ in range(N)]

start_cities = []

for i in range(N):
    cities = list(map(int, input().split()))
    for j in range(M):
        graph[i][j] = [cities[j], 0]
        # 전염병 시작지점 저장
        if cities[j] == 1 or cities[j] == 2:
            start_cities.append([i, j, cities[j], 0])
        
# BFS로 전염시키기
q = deque()
for start_city in start_cities:
    q.append(start_city)

while q:
    
    x, y, virus, time = q.popleft()
    if graph[x][y][0] == 3:
        continue
    for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        nx, ny = x+dx, y+dy
        # 그래프 범위 밖이라면 넘어가기
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        # 백신을 가지고 있거나 3번 바이러스라면 넘어가기
        if graph[nx][ny][0] == -1 or graph[nx][ny][0] == 3:
            continue
        # 아직 전염 되지 않았다면 전염시키고 넘어가기
        if graph[nx][ny][0] == 0:
            graph[nx][ny] = [virus, time+1]
            q.append([nx, ny, virus, time+1])
            continue
        # 이미 같은 바이러스로 전염시킨 장소라면 넘어가기
        if graph[nx][ny][0] == virus:
            continue
        # 전염 되었는데 시간이 같다면 3번으로 만들기
        if graph[nx][ny][0] == 1 or graph[nx][ny][0] == 2:
            if graph[nx][ny][1] == time+1:
                graph[nx][ny][0] = 3
                
    # for i in range(N):
    #     for j in range(M):
    #         print(graph[i][j][0], end=" ")
    #     print()
    # print()

number_of_viruses = [0] * 3
for i in range(N):
    for j in range(M):
        # print(graph[i][j][0], end=" ")
        if graph[i][j][0] == -1 or graph[i][j][0] == 0:
            continue
        number_of_viruses[graph[i][j][0]-1] += 1
    # print()
# print(graph)
print(*number_of_viruses)


            
            
        
