column = 'ABCDEFGH'
row = '87654321'

# 킹의 위치 1, 돌의 위치 2

import sys
input = sys.stdin.readline

KING, STONE, N = input().rstrip().split()

move_dict = { 
    'R' : [0, 1], 'L' : [0, -1], 'B' : [1, 0], 'T' : [-1, 0],
    'RT' : [-1, 1], 'LT' : [-1, -1], 'RB' : [1, 1], 'LB' : [1, -1],
}

x, y = row.index(KING[1]), column.index(KING[0])
a, b = row.index(STONE[1]), column.index(STONE[0])
chess_board = [[0] * 8 for _ in range(8)]
chess_board[x][y] = 1
chess_board[a][b] = 2

for move in range(int(N)):
    # print("king ", x, y, "stone ", a, b)
    order = input().rstrip()
    dx, dy = move_dict[order]
    nx, ny = x+dx, y+dy
    if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
        continue
    if nx == a and ny == b:
        na, nb = a+dx, b+dy
        if na < 0 or na >= 8 or nb < 0 or nb >= 8:
            continue
        a, b = na, nb
    x, y = nx, ny
# print("king ", x, y, "stone ", a, b)
print(column[y]+row[x])
print(column[b]+row[a])