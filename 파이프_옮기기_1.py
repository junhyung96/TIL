import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
graph[0][1] = 1
visited = [[0] * N for _ in range(N)]
result = 0

def bfs(x1, y1, x2, y2):
    global result

    q = deque()
    q.append([(x1, y1), (x2, y2)])
    
    while q:
        (x1, y1), (x2, y2) = q.popleft()
        print(x1, y1, x2, y2)
        if x2 == N-1 and y2 == N-1:
            result += 1
            continue

        # 가로로 놓여있을 때
        if x2 - x1 == 0 and y2 - y1 == 1:
            # 가로로 그대로 진행
            if y2+1 < N and graph[x2][y2+1] == 0:
                q.append([(x2, y2), (x2, y2+1)])
            
        
        # 세로로 놓여있을 때
        if x2 - x1 == 1 and y2 - y1 == 0:
            # 세로로 그대로 진행
            if x2+1 < N and graph[x2+1][y2] == 0:
                q.append([(x2, y2), (x2+1, y2)])

        # 대각선으로 놓여있을 때
        if x2 - x1 == 1 and y2 - y1 == 1:
            # 가로로 진행
            if y2+1 < N and graph[x2][y2+1] == 0:
                q.append([(x2, y2), (x2+1, y2)])
            # 세로로 진행
            if x2+1 < N and graph[x2+1][y2] == 0:
                q.append([(x2, y2), (x2+1, y2)])

        # 오른쪽 대각선 아래로 진행
        if x2+1 < N and y2+1 < N and graph[x2+1][y2+1] == 0 and graph[x2][y2+1] == 0 and graph[x2+1][y2] == 0:
            q.append([(x2, y2), (x2+1, y2+1)])

bfs(0, 0, 0, 1)

print(result)
