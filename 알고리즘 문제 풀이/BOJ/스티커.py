# import sys
# input = sys.stdin.readline

# T = int(input())

# def get_max_sum(length, graph):
#     dp = [list([0, 0] for _ in range(length)) for _ in range(2)]    # 해당 좌표 스티커를 안뗐으면 인덱스0  뗐으면1
#     dp[0][0][1] = graph[0][0]
#     dp[0][1][0] = max(graph[0][0], graph[0][1])
#     dp[0][1][1] = graph[0][1]
#     for i in range(2, n):


# for test_case in range(T):
#     n = int(input())
#     stickers = [list(map(int, input().split())) for _ in range(2)]
#     print(get_max_sum(n, stickers))
    


