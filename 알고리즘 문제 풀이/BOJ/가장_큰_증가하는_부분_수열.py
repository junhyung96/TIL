import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

length_dp = [0] * N
sum_dp = [0] * N

length_dp[0] = 1
sum_dp[0] = arr[0]

for i in range(1, N):

    available_j = []
    for j in range(0, i):
        if arr[i] > arr[j] and length_dp[j] + 1 > length_dp[i]:
            available_j.append((j, length_dp[j]+1, sum_dp[j]))

    if not available_j: 
        length_dp[i] = 1
        sum_dp[i] = arr[i]
        continue

    available_j.sort(key=lambda x: (x[1], x[2]), reverse=True)
    length_dp[i] = available_j[0][1]
    sum_dp[i] = sum_dp[available_j[0][0]] + arr[i]

print(max(sum_dp))