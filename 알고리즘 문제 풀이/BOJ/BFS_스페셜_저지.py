import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
adj_ls = [[] for _ in range(N+1)]
# adj_ls = {n: [] for n in range(1, N+1)}
for _ in range(N-1):
    node1, node2 = map(int, input().split())
    adj_ls[node1].append(node2)
    adj_ls[node2].append(node1)

answer = list(map(int, input().split()))
# print(adj_ls)

visited = [False] * (N + 1)
q = [1]
idx = 1
isVaild = True

while isVaild:
    prev_idx = idx
    
    for cur in q:
        partial_q = []
        visited[cur] = True
        
        for nxt in adj_ls[cur]:
            if not visited[nxt]:
                partial_q.append(nxt)
        
        if partial_q:
            if sorted(partial_q) != sorted(answer[idx:idx + len(partial_q)]):
                isVaild = False
                break
            idx += len(partial_q)
    
    if not partial_q:
        break
    
    q = answer[prev_idx:idx]
    
print(1 if isVaild else 0)

# def bfs():
#     visited = [False] * (N + 1)
#     q = deque()
#     i = 0
#     q.append(1)
#     i += 1
#     visited[1] = True
    
#     while q:
#         if i == N:
#             break
#         cur = q.popleft()
#         nxt = answer[i]
#         if nxt in adj_ls[cur] and not visited[nxt]:
#             q.appendleft(cur)
#             q.append(nxt)
#             # print(nxt)
#             i += 1
#             visited[nxt] = True
    
#     if i == N:
#         print(1)
#     else:
#         print(0)
    
# bfs()
