# 크기가 N 인 수열이 있을 때
# 각 항에 대하여 1을 더하거나 1을 뺄 수 있다
# 등차수열로 만들 수 있으면 필요한 덧셈 혹은 뺄셈의 총 횟수
# 만들 수 없으면 -1을 출력하라

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
seq = []
for item in arr:
    seq.append(item)
# arr = sorted(arr)

if N == 1:
    print(0)
    exit()

for i in range(1, N):
    seq[i] = round((seq[i] - seq[0]) / i)
seq[0] = 0
# print(seq)    
candi = set(seq[1:])
# print(candi)

def get_seq_item(first, diff, index):
    return first + diff * index

result = int(10**9)
for avg in range(min(candi), min(candi)+4):
    # print("avg = ", avg)
    for first_item in range(arr[0]-1, arr[0]+2):
        cnt = 0
        for i in range(N):
            # print("i :", arr[i], "num :", get_seq_item(first_item, avg, i))
            if abs(arr[i] - get_seq_item(first_item, avg, i)) > 1:
                # print("It is not seq")
                cnt = int(10**9)
                # print(cnt)
                break
            cnt += abs(arr[i] - get_seq_item(first_item, avg, i))
            # print("when i is ", i, " cnt is ", cnt)
        else:
            # print("completed")
            result = min(cnt, result)
        # print("cnt = ",cnt)
        # print("result = ", result)
print(result if result != 10**9 else -1)

# a = int(10**9)
# print(a)
# 0 2 5 8 11
#   2 2.5 8/3 11/4
#   a + n * d