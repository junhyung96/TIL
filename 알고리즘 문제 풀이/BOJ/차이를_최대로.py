from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
visited = [0] * N
result = 0

def bfs(pre, d, total):
    global result
    # print(pre, d, total)
    if d == N:
        result = max(result, total)
        return
    
    for i in range(N):
        if visited[i]:
            continue
        if d == 0:
            visited[i] = 1
            bfs(arr[i], d+1, total)
            visited[i] = 0
        else:
            visited[i] = 1
            bfs(arr[i], d+1, total+abs(pre-arr[i]))
            visited[i] = 0

bfs(0, 0, 0)
print(result)


# 밑의 풀이는
# 3 1 3 혹은 3 1 3 1 3
# 에 대한 예외를 처리할 수 없다

# N = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
# q = deque()
# for item in arr:
#     q.append(item)
# result = deque()

# result.append(q.popleft())

# flag = True
# i = 0

# while q:
#     if flag:
#         result.append(q.pop())
#         if q:
#             result.appendleft(q.pop())  
#     else:
#         result.append(q.popleft())
#         if q:
#             result.appendleft(q.popleft())
#     flag = not flag

# total = 0
# for i in range(N-1):
#     total += abs(result[i] - result[i+1])

# print(total)
    