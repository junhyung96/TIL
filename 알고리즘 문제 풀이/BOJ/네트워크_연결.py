import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
edges = []
parents = [i for i in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a-1, b-1, c))

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

print(cost)