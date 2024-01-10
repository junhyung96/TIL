# ACM크래프트는 다이나믹한 게임 진행을 위해 건물을 짓는 순서가 정해져 있지 않다. 
# 즉, 첫 번째 게임과 두 번째 게임이 건물을 짓는 순서가 다를 수도 있다.
# 매 게임시작 시 건물을 짓는 순서가 주어진다. 
# 또한 모든 건물은 각각 건설을 시작하여 완성이 될 때까지 Delay가 존재한다.

# 1번 건물의 건설이 완료된다면 2번과 3번의 건설을 시작할수 있다. 
# (동시에 진행이 가능하다) 그리고 4번 건물을 짓기 위해서는 
# 2번과 3번 건물이 모두 건설 완료되어야지만 4번건물의 건설을 시작할수 있다.
import sys
from collections import deque
input = sys.stdin.readline

def Kahn():
    pass

T = int(input()) # 테스트케이스 수
for test in range(T):
    N, K = map(int, input().split()) # N 건물의 수, 규칙의 수
    time_to_build = list(map(int, input().split()))

    # 진입차수 체크
    nodes = [0] * N
    # 해당 노드까지 걸리는 시간 dp
    dp = [0] * N
    # 위상정렬 Kahn 을 위한 큐
    q = deque()
    # 위상정렬된 노드
    sorted_nodes = []
    # 인접리스트
    adj_ls = [[] for _ in range(N)]

    for _ in range(K):
        a, b = map(int ,input().split())
        nodes[b-1] += 1
        adj_ls[a-1].append(b-1)

    goal = int(input())

    while sum(nodes) != -N:
        for i in range(N):
            if nodes[i] == 0:
                nodes[i] -= 1
                q.append((i, time_to_build[i]))
                dp[i] = max(time_to_build[i], dp[i])
        while q:
            node, time = q.popleft()
            sorted_nodes.append(node)
            for next_node in adj_ls[node]:
                nodes[next_node] -= 1
                dp[next_node] = max(dp[next_node], time_to_build[next_node]+dp[node])
    
    # print(time_to_build)
    # print(dp)
    print(dp[goal-1])

                


    
