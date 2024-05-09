# 단어 N개로 이루어진 집합의 부분집합 중
# 접두사X 집합인 부분집합의 최대크기는?

# 접두사X 집합 어느 하나라도 다른 단어의 접두어가 되지 않는 것

# N <= 50

# 해야할 것
# 부분집합을 구할 수 있어야함.
# 길이가 N 인 집합은 부분집합이 몇개 있을까?
# 문자열의 길이도 50미만
# 공집합을 포함해서 2^n개
# 따라서 모든 부분집합을 구할 수는 없음

# 부분집합이 접두사X 집합임을 알 수 있어야 함.

import sys
input = sys.stdin.readline

N = int(input())
arr = []
# 다른 문자열에 포함되면 0으로 변경
arr_valid = [1] * N 
for _ in range(N):
    arr.append(input().rstrip())
arr.sort()
for i in range(N):
    for j in range(i+1, N):
        li = len(arr[i])
        if arr[i] == arr[j][0:li]:
            arr_valid[i] = 0
            break

print(sum(arr_valid))