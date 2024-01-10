# 세현이네 집에서 학교까지 가는 길은 N x N 크기의 바둑판과 같다. 
# 그리고 각 블록은 1x1 정사각형으로 구분 지을 수 있다. 
# 세현이는 그 블록마다 숫자와 연산자가 존재한다고 생각해서 
# 임의의 숫자와 연산자를 각 블록에 넣어 바둑판을 만들었다.

# 세현이는 학교에서 집으로 가는 경로에서 만나는 숫자와 
# 연산자의 연산 결과의 최댓값과 최솟값을 구하려고 한다. 
# 세현이는 항상 자신의 집 (1, 1)에서 학교 (N, N)까지 최단거리로 이동한다. 
# 최단거리로 이동하기 위해서는 오른쪽과 아래쪽으로만 이동해야 한다.

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(input().rstrip().split()) for _ in range(N)]
min_res = int(1e9)
max_res = -int(1e9)
visited = [[False] * N for _ in range(N)]

def dfs(x, y, equ, d):
    global min_res
    global max_res
    
    # print(x, y, 'depth',d, equ)
    equ.append(arr[x][y])
    # print(x, y, 'depth',d, equ)
    if d > 0 and d & 1 == 0:
        if equ[1] == '+':
            equ = [str(int(equ[0]) + int(equ[2]))]
        elif equ[1] == '-':
            equ = [str(int(equ[0]) - int(equ[2]))]
        elif equ[1] == '*':
            equ = [str(int(equ[0]) * int(equ[2]))]

    
    if x == N-1 and y == N-1:
        calculated_num = int(equ[0])
        min_res = min(min_res, calculated_num)
        max_res = max(max_res, calculated_num)
        return
    
    for dx, dy in [(1, 0), (0, 1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < N:
            dfs(nx, ny, equ, d+1)
            equ.pop()

dfs(0, 0, [], 0)

print(max_res, min_res)