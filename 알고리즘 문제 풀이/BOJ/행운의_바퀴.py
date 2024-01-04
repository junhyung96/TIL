import sys

N, K = map(int, input().split())
roulette = ['?'] * (N)

current_index = 0
dup = ''
for _ in range(K):
    count, al = input().rstrip().split()
    count = int(count)
    count %= N
    while count:
        current_index += 1
        count -= 1
        if current_index >= N:
            current_index = 0
    if roulette[current_index] == al:
        continue
    if (roulette[current_index] != '?' and roulette[current_index] != al)\
        or al in dup:
        print('!')
        exit()
    
    dup += al
    roulette[current_index] = al


for _ in range(N):
    print(roulette[current_index], end='')
    current_index -= 1
    if current_index == -1:
        current_index = N-1

