# 오르막수 = 수의 자리가 오름차순 (같은 수도 인정)
# ex 1114 
# 오르막수가 아닌것
# ex  1221

# 수의 길이 N
N = int(input())
arr = [[0] * 10 for _ in range(N)]
for i in range(10):
    arr[0][i] = 1

if N >= 2:
    for i in range(1, N):
        for j in range(10):
            arr[i][j] = sum(arr[i-1][j:]) % 10007

print(sum(arr[N-1]) % 10007)

