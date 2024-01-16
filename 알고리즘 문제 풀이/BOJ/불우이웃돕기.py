import sys
input = sys.stdin.readline

N = int(input())
LAN = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

edges = []
parents = [i for i in range(N)]
total_length = 0
graph = [list(input().rstrip()) for _ in range(N)]
for i in range(N):
    for j in range(N):
        line_length = LAN.index(graph[i][j])
        total_length += line_length
        if i == j:
            continue
        if line_length == 0:
            continue
        edges.append((i, j, line_length))


edges.sort(key=lambda x: x[2])

def find(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]


def union(a, b):
    a, b = find(a), find(b)
    parents[max(a, b)] = min(a, b)


cost = 0
cnt = 0
for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        cost += c
        cnt += 1
        if cnt == N - 1:
            break

if cnt < N-1:
    print(-1)
else:
    print(total_length - cost)