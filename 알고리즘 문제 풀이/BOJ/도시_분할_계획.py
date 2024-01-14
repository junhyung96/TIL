# 최소 신장 트리
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = sorted([list(map(int, input().split())) for _ in range(M)], key = lambda x : x[2])
parent = [i for i in range(N+1)]

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]
    
def union(a, b):
    parent[max(a, b)] = min(a, b)

result = 0
cnt = 0
for a, b, c in graph:
    find_a = find(a)
    find_b = find(b)
    if find_a != find_b:
        union(find_a, find_b)
        result += c
        cnt += 1
        if cnt == N-1:
            break
print(result-c)