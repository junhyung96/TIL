import sys
input = sys.stdin.readline
# 수열의 합

# N 과 L 이 주어진다.
# 합이 N이면서 길이가 적어도 L인 가장 짧은 연속된 음이아닌 정수 리스트를 구하라
N, L = map(int, input().split())

# 길이가 2보다 크거나 같고 100보다 작거나 같으므로 0부터 99까지 누적합 리스트 구하기

sequence = [i for i in range(100)]
prefix_sum = [0] * 100
for i in range(1, 100):
    prefix_sum[i] = prefix_sum[i-1] + sequence[i]     

# 합이 주어지면 N에서 0부터 L-1까지의 합을 뺀 나머지가 L으로 나누어지는지 판단
# 나누어지면 몫만큼 0~L-1 의 각 원소에 더해주고 출력
# 나누어지지않으면 L += 1 해서 판단
# N보다 0~L-1의 합이 커지면 부적합 -1 출력
length = L
for seq_sum in prefix_sum[L-1:]:
    if seq_sum > N:
        print(-1)
        break
    if (N - seq_sum) % length == 0:
        quotient = (N - seq_sum) // length
        for i in range(length):
            print(i+quotient, end=' ')
        break
    length += 1
else:
    print(-1)

'''시간 최소 
n,l=map(int,input().split())

for i in range(l,101):
    ix=n-(i*(i+1)//2)
    if ix%i==0:
        x=ix//i
        if x+1>=0:
            print(*(i for i in range(x+1,x+i+1)))
            break
else:
    print(-1)
'''