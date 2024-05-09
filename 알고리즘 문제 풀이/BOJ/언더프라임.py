# 언더프라임
# 
# 언더프라임 : 소인수분해해서 소수의 목록의 길이가 소수인 수
#
# 입력 
# 정수 A, B 범위 2 <= A <= B <= 100,000
#
# 출력
# A 보다 크거가 같고 B 보다 작거나 같은 정수 중 언더프라임인 것의 개수
#
# 해야하는 것 = 소인수분해, 소수판정
# 10만까지의 수를 소수판정
# 최대 10만개의 수를 소인수분해
# 소인수분해 과정이 100,000개의 수를 소수로 나눠봐야함
# 소수는 9592개 있음 10,000 * 100,000 이미 시간초과
#----------------------------------------------------------
# import sys
# input = sys.stdin.readline

# # 소수판정 => 메모이제이션
# # 소수가 아니다 => 1 소수다 => 0
# memo = [0] * 100_001
# memo[0] = 1
# memo[1] = 1
# prime_nums = []

# for i in range(2, 100_001):
#     if memo[i] == 1:
#         continue
#     prime_nums.append(i)
#     for j in range(2*i, 100_001, i):
#         memo[j] = 1

# # 소인수 분해 - 반환값 : 소인수분해 목록 길이
# def prime_factorization(n):
#     target = n
#     count = 0
#     index = 0
#     while target != 1:
#         cur = prime_nums[index]
#         if target % cur == 0:
#             target /= cur
#             count += 1
#         else:
#             index += 1
#     return count

# # 실행
# A, B = map(int, input().split())

# num_of_underprime = 0

# for num in range(A, B+1):
#     if memo[num] == 0:
#         continue
#     if memo[prime_factorization(num)]:
#         continue
#     num_of_underprime += 1

# print(num_of_underprime)

#----------------------------------------------------------

import sys
input = sys.stdin.readline

# 소수판정 => 메모이제이션
# 소수가 아니다 => 1 소수다 => 0
memo = [0] * 100_001
factor_count = [0] * 100_001
memo[0] = 1
memo[1] = 1
prime_nums = []

for i in range(2, 100_001):
    if memo[i] == 1:
        continue
    factor_count[i] = 1
    prime_nums.append(i)
    for j in range(2*i, 100_001, i):
        memo[j] = 1
        factor_count[j] += 1
    sqr = i*i
    while sqr <= 100_001:
        for k in range(sqr, 100_001, sqr):
            factor_count[k] += 1
        sqr *= i

# 소인수 분해 - 반환값 : 소인수분해 목록 길이
def prime_factorization(n):
    target = n
    count = 0
    index = 0
    while target != 1:
        cur = prime_nums[index]
        if target % cur == 0:
            target /= cur
            count += 1
        else:
            index += 1
    return count

# 실행
A, B = map(int, input().split())

num_of_underprime = 0

for num in range(A, B+1):
    if memo[factor_count[num]]:
        continue
    num_of_underprime += 1

print(num_of_underprime)
