import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
baby_shark = 2
exp = 0
distance = 0
sx, sy = 0, 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            sx, sy = i, j
            arr[i][j] = 0

def bfs(x, y):
    global baby_shark
    q = deque()
    visited = [[0]*N for _ in range(N)]
    visited[x][y] = 1
    q.append((x, y, 0))
    # fishes = []

    while q:
        x, y, d = q.popleft()
        for dx, dy in [[-1,0],[0,-1],[1,0],[0,1]]:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                if arr[nx][ny] > baby_shark:
                    continue
                visited[nx][ny] = 1
                q.append((nx, ny, d+1))
                if arr[nx][ny] == 0:
                    continue
                if arr[nx][ny] < baby_shark:
                    return (nx, ny, d+1)
    # print(visited)
    # print(fishes)
    # if fishes:
    #     fishes.sort(key = lambda x: (x[2], x[0], x[1]))
    #     return fishes[0]
    # else:
    return 0, 0, 0

while 1:
    sx, sy, dist = bfs(sx, sy)
    if dist == 0:
        break
    exp += 1
    if exp == baby_shark:
        baby_shark += 1
        exp = 0
    arr[sx][sy] = 0
    distance += dist

print(distance)