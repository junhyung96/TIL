# 정수 집합 S
# 집합 : 어떤 명확한 조건을 만족시키는 서로 다른 대상들의 모임
# 
# 다음 조건을 만족하는 [A, B] 를 좋은 구간이라고 한다.
# 양의정수 A, B
# A < B
# A <= x <= B 인 x 가 S 에 속하지 않는다

# S 와 n 이 주어졌을 때, n을 포함하는 좋은 구간의 개수
# n 는 S 에서 가장 큰 수와 작거나 같다

# 집합 S 의 크기  1 <= L <= 1000

# 해야할 것

# 특정 숫자 n이 포함되는 구간을 구해야 함
# 구간에는 S 에 포함되는 정수가 없어야 함
# A 를 결정하는 로직
# B 를 결정하는 로직

# n a b c d
# a n b c d
# a b c d n

import sys
input = sys.stdin.readline

L = int(input())
S = list(map(int, input().split()))
n = int(input())
A = 0
B = 0

if n in S:
    print(0)
    exit()

S.append(n)
S.sort()
position_of_n = S.index(n)

# A의 경우의 수 결정
# n 이 제일 작을 때
# n 이 제일 작은 건 아닐 때
if position_of_n == 0:
    A = n
else:
    A = n - S[position_of_n-1]

# B의 경우의 수 결정
B = S[position_of_n+1] - n

print(A * B - 1)