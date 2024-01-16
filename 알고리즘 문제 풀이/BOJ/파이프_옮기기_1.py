import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
# print(dp)
# dp[x][y][0:가로, 1:세로, 2:대각선]
dp[0][1][0] = 1
for i in range(2, N):
    if graph[0][i] == 1:
        break
    dp[0][i][0] = 1

for i in range(1, N):
    for j in range(1, N):
        if graph[i][j] == 0 and graph[i-1][j] == 0 and graph[i][j-1] == 0:
            dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

        if graph[i][j] == 0:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]

print(sum(dp[N-1][N-1]))
# from collections import deque
# N = int(input())
# graph = [list(map(int, input().split())) for _ in range(N)]
# graph[0][1] = 1
# visited = [[0] * N for _ in range(N)]
# result = 0

# if graph[N-1][N-1] == 1:
#     print(0)
#     exit()
    
# def bfs(x1, y1, x2, y2):
#     global result

#     q = deque()
#     q.append([(x1, y1), (x2, y2)])
    
#     while q:
#         (x1, y1), (x2, y2) = q.popleft()
#         # print(x1, y1, x2, y2)
#         if x2 == N-1 and y2 == N-1:
#             result += 1
#             continue

#         # 가로로 놓여있을 때
#         if x2 - x1 == 0 and y2 - y1 == 1:
#             # 가로로 그대로 진행
#             if (x2 == N-1 or (x2 != N-1 and y2+1 < N-1)) and graph[x2][y2+1] == 0:
#                 q.append([(x2, y2), (x2, y2+1)])

        
#         # 세로로 놓여있을 때
#         elif x2 - x1 == 1 and y2 - y1 == 0:
#             # 세로로 그대로 진행
#             if (y2 == N-1 or (y2 != N-1 and x2+1 < N-1)) and graph[x2+1][y2] == 0:
#                 q.append([(x2, y2), (x2+1, y2)])
            

#         # 대각선으로 놓여있을 때
#         elif x2 - x1 == 1 and y2 - y1 == 1:
#             # 가로로 진행
#             if (x2 == N-1 or (x2 != N-1 and y2+1 < N-1)) and graph[x2][y2+1] == 0:
#                 q.append([(x2, y2), (x2, y2+1)])
#             # 세로로 진행
#             if (y2 == N-1 or (y2 != N-1 and x2+1 < N-1)) and graph[x2+1][y2] == 0:
#                 q.append([(x2, y2), (x2+1, y2)])

#         # 오른쪽 대각선 아래로 진행
#         if x2+1 < N and y2+1 < N and graph[x2+1][y2+1] == 0 and graph[x2][y2+1] == 0 and graph[x2+1][y2] == 0:
#             q.append([(x2, y2), (x2+1, y2+1)])

# bfs(0, 0, 0, 1)

# print(result)
