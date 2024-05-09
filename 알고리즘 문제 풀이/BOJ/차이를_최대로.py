from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
q = deque()
for item in arr:
    q.append(item)
result = deque()

result.append(q.popleft())

flag = True
i = 0

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
while q:
    if flag:
        result.appendleft(q.pop())  
        if q:
            result.append(q.pop())
    else:
        result.appendleft(q.popleft())
        if q:
            result.append(q.popleft())
    flag = not flag   

total = 0
for i in range(N-1):
    total += abs(result[i] - result[i+1])
# print(result)
print(total)

# -100 -11 -5 0 5 7
# 0 -11 7 -100 5 -5
# 11 18 107 105 10
# 251
