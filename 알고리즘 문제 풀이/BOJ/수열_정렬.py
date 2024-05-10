# 수열 정렬

# 수열 P : 0 부터 N-1 까지의 수를 한번 씩 포함하고 있는 수열
# B[P[i]] = A[i] 

# N <= 50
# 배열의 원소 <= 1000

# 수열 P를 길이가 N인 배열 A에 적용하면 길이가 N인 배열 B가 된다.
# 배열 B가 비내림차순인 경우의 수열을 출력
# 여러개라면 사전순으로 앞서는 것을 출력

# 해야할 것

# 수열 P 를 배멸 A에 적용할 수 있어야 함
# 비내림차순임을 알 수 있어야 함 = 오름차순 만들기 수열인 것

# 풀이 1

# 길이가 N 인 수열 P 를 사전순으로 배열 A 에 적용
# 비내림차순인 경우 수열을 출력 후 종료

# 풀이 2

# 배열 A 를 탐색하며 가장 작은 수 부터 인덱스 부여
# == 배열 A 를 정렬하고 인덱스 순으로 부여 (중복제거 필수)

import sys
input = sys.stdin.readline

N = int(input())
arr_A = list(map(int, input().split()))

# set_A = sorted(set(arr_A))
# result = [-1] * N

# index = 0
# for i in range(len(set_A)):
#     for j in range(N):
#         if set_A[i] == arr_A[j]:
#             result[j] = index
#             index += 1

# for k in range(N):
    # print(result[k], end=" ")

sorted_A = sorted(arr_A)
result = []
for i in range(N):
    result.append(sorted_A.index(arr_A[i]))
    sorted_A[result[-1]] = 0 # 중복일 수 있으므로 0으로 초기화

print(*result)