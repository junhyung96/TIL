import sys

src = sys.stdin.readline

v, e = map(int, src().split())
parents = [i for i in range(v + 1)]
graph = sorted([tuple(map(int, src().split())) for line in range(e)], key=lambda x: x[2])


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
for a, b, c in graph:
    if find(a) != find(b):
        union(a, b)
        cost += c
        cnt += 1
        if cnt == v - 1:
            break
print(cost)