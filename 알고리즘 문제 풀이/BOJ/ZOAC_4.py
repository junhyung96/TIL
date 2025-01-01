import sys
input_ = sys.stdin.readline

H, W, N, M = map(int, input_().split())

print(((H-1)//(N+1) + 1) * ((W-1)//(M+1) + 1))