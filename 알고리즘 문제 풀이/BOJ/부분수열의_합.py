import sys
input = sys.stdin.readline


def backtrack(size, target_number, tmp_sum, cnt, pre):
    global result
    if cnt !=0 and tmp_sum == target_number:
        result += 1
    for i in range(pre, size):
        backtrack(size, target_number, tmp_sum+arr[i], cnt+1, i+1)


N, S = map(int, input().split())
arr = list(map(int, input().split()))
total = sum(arr)
result = 0
backtrack(N, S, 0, 0, 0)
print(result)
