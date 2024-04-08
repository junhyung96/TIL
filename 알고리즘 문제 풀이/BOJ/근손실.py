import sys
input = sys.stdin.readline

N, K = map(int, input().split())
exercies_kits = list(map(int, input().split()))
result = 0
visited = [0] * N

def dfs(day, weight):
    global result    
    for i in range(N):
        if visited[i]: continue
        if weight + exercies_kits[i] - K >= 0:
            if day+1 == N:
                result += 1
            visited[i] = 1
            dfs(day+1, weight + exercies_kits[i] - K)
            visited[i] = 0

dfs(0, 0)
print(result)