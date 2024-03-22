import sys
input = sys.stdin.readline

T = int(input())

def get_max_sum(n, graph):
    dp = [list([0, 0] for _ in range(n)) for _ in range(2)]    # 해당 좌표 스티커를 안뗐으면 인덱스0  뗐으면1
    dp[0][0][1] = graph[0][0]
    dp[1][0][1] = graph[1][0]

    for i in range(1, n):
        # 해당 좌표 스티커를 안뗐을 경우
        dp[0][i][0] = max(dp[0][i-1][0], dp[0][i-1][1], 
                          dp[1][i-1][0], dp[1][i-1][1])
        dp[1][i][0] = max(dp[0][i-1][0], dp[0][i-1][1], 
                          dp[0][i][0], dp[0][i][1], dp[1][i-1][0], dp[1][i-1][1], dp[1][i-2][0], dp[1][i-2][1])
        # 해당 좌표 스티커를 뗐을 경우
        dp[0][i][1] = max(dp[0][i-1][0] + graph[0][i], 
                          dp[1][i-1][0] + graph[0][i], dp[1][i-1][1] + graph[0][i])
        dp[1][i][1] = max(dp[0][i-1][0] + graph[1][i], dp[0][i-1][1] + graph[1][i])

    return(max(dp[1][n-1][0], dp[1][n-1][1], dp[0][n-1][0], dp[0][n-1][1]))

for test_case in range(T):
    N = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    print(get_max_sum(N, stickers))
    


