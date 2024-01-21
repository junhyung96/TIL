import sys
from collections import deque
input = sys.stdin.readline
                

# 백조가 만나는 조건..
# 처음 백조의 위치로 부터 bfs로 백조1 백조2를 그래프에 기록한다
# 빙판을 녹이면서 백조1, 백조2가 서로 만나는지 체크
R, C = map(int, input().split())
graph1 = [[''] * C for _ in range(R)]
graph2 = [[''] * C for _ in range(R)]
disconnected = True
# print(graph1)
for i in range(R):
    j = 0
    for block in list(input().rstrip()):
        # print(i, j, graph1[i][j])
        graph1[i][j] = [block, 0]
        graph2[i][j] = [block, 0]
        j += 1
# print(graph1[1][1])

def bfs(x, y, s):
    q = deque()
    q.append((x, y))
    visited = [[0] * C for _ in range(R)]
    visited[x][y] = 1
    graph1[x][y][1] = s
    while q:
        x, y = q.popleft()
        for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < R and 0 <= ny < C:
                if graph1[nx][ny][0] == 'L' and visited[nx][ny] == 0:
                    print(0)
                    exit()
                if graph1[nx][ny][0] == '.' and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    graph1[nx][ny][1] = s
                    q.append((nx, ny))

swan = 0
for i in range(R):
    for j in range(C):
        if graph1[i][j][0] == 'L':
            swan += 1
            bfs(i, j, swan)

for x in range(R):
    for y in range(C):
        graph2[x][y][0], graph2[x][y][1] = graph1[x][y][0], graph1[x][y][1]

day = 0

while disconnected:
    day += 1
    print(day)
    for x in range(R):
        for y in range(C):
            # print(graph1[x][y][0])
            if graph1[x][y][0] != 'X':
                continue
            for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < R and 0 <= ny < C and graph1[nx][ny][0] != 'X':
                    print(nx, ny)
                    if graph1[nx][ny][1] != 0 and graph2[x][y][1] != 0 and (graph1[nx][ny][1] != graph2[x][y][1]):
                        disconnected = False
                        break
                    
                    graph2[x][y][0] = '.'
                    graph2[x][y][1] = graph1[nx][ny][1]
    print(graph1)
    print(graph2)
    for x in range(R):
        for y in range(C):
            graph1[x][y] = graph2[x][y]


print(day)
                        
