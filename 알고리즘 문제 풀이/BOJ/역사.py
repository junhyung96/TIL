# 역사, 그 중에서도 한국사에 해박한 세준이는 많은 역사적 사건들의 전후 관계를 잘 알고 있다. 
# 즉, 임진왜란이 병자호란보다 먼저 일어났으며, 무오사화가 기묘사화보다 먼저 일어났다는 등의 지식을 알고 있는 것이다.

# 세준이가 알고 있는 일부 사건들의 전후 관계들이 주어질 때, 주어진 사건들의 전후 관계도 알 수 있을까? 
# 이를 해결하는 프로그램을 작성해 보도록 하자.

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
parent = [[] for _ in range(n+1)]
for _ in range(k):
    pre, post = map(int, input().split())
    parent[pre].append(post)

def find_history(s, e):
    global history_valid
    if history_valid:
        return 
    if visited[s] == 1:
        return
    visited[s] = 1
    for next in parent[s]:
        if next == e:
            history_valid = True
            return
        if visited[next] == 0:
            find_history(next, e)


s = int(input())
for _ in range(s):
    p1, p2 = map(int, input().split())
    history_valid = False

    visited = [0] * (n+1)
    find_history(p1, p2)
    if history_valid:
        print(-1)
        continue
    visited = [0] * (n+1)
    find_history(p2, p1)
    if history_valid:
        print(1)

    if not history_valid:
        print(0)