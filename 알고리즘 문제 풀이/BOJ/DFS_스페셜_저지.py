# 정점의 수 100,000

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
adj_ls = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    adj_ls[a].append(b)
    adj_ls[b].append(a)
    
DFS_seq = list(map(int, input().split()))

# dfs 구현해서 따라가면서 맞는지 조사..
# 하나의 노드에서 다음 노드로 넘어갈 때
# 방문 여부 저장
# 고려사항
# 현재 노드에서 갈 수 있는 노드가 있는지?
# 현재 노드에서 갈 수 있는 노드가 있다면 방문했는지?
# 다 방문했다면 이전 노드로 돌아가서 체크하기
# 이전 노드는 어떻게 알건데?

def dfs_valid_check(pre, next):
    # print("# check ", pre, "to next ", next)
    # 다음 노드로 갈 수 있다! ㄱㄱ
    if next in adj_ls[pre]:
        visited[next] = True
        # print('can go')
        return next, True
    
    # 시간복잡도 이슈가 있을 수 있음
    # 갈 수 있는 노드 모두 방문했는지 알려면 visited 다 조사해야됨
    for nod in adj_ls[pre]:
        # 갈 수 있는 노드가 남아있는데 다음 노드가 그 중 없다는 것
        if not visited[nod]:
            # print('not in next but remain')
            return pre, False
    
    # 다음 노드가 없고 현재 노드에서 방문 할 수 있는 곳 다 갔다면
    # 이전 노드로 돌아가서 위의 사항들 다시 체크하기 
    if pre != 1:
        return dfs_valid_check(DFS_seq[DFS_seq.index(pre)-1], next)
    else:
        return pre, True

if DFS_seq[0] != 1:
    print(0)
    exit()

cur = 1
visited[1] = True

for i in range(1, N):
    node = DFS_seq[i]
    cur, isValid = dfs_valid_check(cur, node)
    if not isValid:
        print(0)
        exit()

print(1)
# start = 1
# while True:
#     next, isValid = dfs_valid_check(start)
#     if not isValid:
#         print(0)
#         exit()
#     start = next
