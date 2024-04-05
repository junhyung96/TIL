import sys
input = sys.stdin.readline

# 주사위의 각 면 마다 상하좌우 인덱스를 매핑해서 찾아가도록 하기
dice = [0] * 6
# 생각해야 하는것 바닥면과 윗면 
# 바닥면은 값을 갱신
# 윗면은 출력
# 맨 처음 주사위 인덱스
#   1
# 2 0 3
#   4
#   5
# 바닥면 인덱스 기준
# 동 : 0 > 2, 1 > 1, 2 > 5, 3 > 0, 4 > 4, 5 > 3
# 서 : 0 > 3, 1 > 1, 2 > 0, 3 > 5, 4 > 4, 5 > 2
# 북 : 0 > 4, 1 > 0, 2 > 2, 3 > 3, 4 > 5, 5 > 1
# 남 : 0 > 1, 1 > 5, 2 > 2, 3 > 3, 4 > 0, 5 > 4
def switch_dice(cur_arr, direction):
    if direction == 1:
        result = [cur_arr[3], cur_arr[1], cur_arr[0], cur_arr[5], cur_arr[4], cur_arr[2]]
    elif direction == 2:
        result = [cur_arr[2], cur_arr[1], cur_arr[5], cur_arr[0], cur_arr[4], cur_arr[3]]
    elif direction == 3:
        result = [cur_arr[1], cur_arr[5], cur_arr[2], cur_arr[3], cur_arr[0], cur_arr[4]]
    elif direction == 4:
        result = [cur_arr[4], cur_arr[0], cur_arr[2], cur_arr[3], cur_arr[5], cur_arr[1]]
    return result

delta_search = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
# 주사위 각 인덱스가 바라보는 방향

# 지도의 크기 N x M
# 주사위의 좌표 x, y
# 명령의 개수 K
N, M, x, y, K = map(int, input().split())
# 지도
graph = [list(map(int, input().split())) for _ in range(N)]
# 명령
for order in map(int, input().split()):
    # print(order)
    dx, dy = delta_search[order][0], delta_search[order][1]
    nx, ny = x+dx, y+dy
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
    x, y = nx, ny 
    # print("point", x, y)
    dice = switch_dice(dice, order)
    # print(graph[x][y])
    if graph[x][y] == 0:
        graph[x][y] = dice[0]
    else:
        dice[0] = graph[x][y]
        graph[x][y] = 0
    # print(dice)
    print(dice[5])

