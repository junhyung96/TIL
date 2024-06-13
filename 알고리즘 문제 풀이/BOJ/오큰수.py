# 오큰수란?
# 수열의 각 원소에 대해서 자신보다 오른쪽에 있으면서 큰 수 중 가장 왼쪽에 있는 수

# 각 원소의 오큰수를 출력하되 없다면 -1을 출력

# 수열의 크기 N 이 1 ~ 1,000,000 이므로 이중 순회 불가능

# 뒤에서 부터 시작해서 나보다 크면 오큰수가 되어주겠지 하고 바톤 넘기기



import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
NGE = [0] * N
NGE[N-1] = -1
cur_max = seq[N-1]
end_idx = N-1
for i in range(N-2, -1, -1):
    if seq[i] >= cur_max:
        NGE[i] = -1
        end_idx = i
        cur_max = seq[i]
    for j in range(i+1, end_idx+1):
        if seq[i] < seq[j]:
            NGE[i] = seq[j]
            break
        if seq[i] < NGE[j]:
            NGE[i] = NGE[j]
            break

print(*NGE)




