# 기타줄 N 개가 끊어졌다
# 기타줄을 6개 패키지 혹은 낱개로 살 수 있다
# 기타줄 브랜드 M 개 ( 각각의 브랜드에서 파는 기타줄 가격이 주어진다. )
# 적어도 N개를 사기 위해 필요한 돈의 수를 최소로 하라

# N <= 100, M <= 50
# 0 <= 가격 <= 1000

# 해야할 것
# 적어도 N개의 기타줄을 사는데 필요한 돈 구하기
# 낱개 기타줄의 가격의 최솟값을 곱하다보면 세트보다 비싸지는 역치 계산
# 사실 모든 기타줄 브랜드의 가격을 알 필요가 없다 최솟값만 저장

# 1개부터 시작해서 DP로 모든 기타줄 수마다 최솟값 구하기


import sys
input = sys.stdin.readline

min_set = 1000
min_each = 1000

N, M = map(int, input().split())
# prices_of_each_brand = [list(map(int, input().split())) for _ in range(M)]
for _ in range(M):
    price_set, price_each = map(int, input().split())
    min_set = min(min_set, price_set)
    min_each = min(min_each, price_each)


dp = [0] * 101

for i in range(1, 7):
    dp[i] = min(min_set, min_each*i)

for j in range(7, 101):
    if j % 6 == 0:
        dp[j] = dp[j-6] + dp[6]
    else:
        dp[j] = dp[j//6*6] + dp[j%6]

print(dp[N])
# print(dp[:13])