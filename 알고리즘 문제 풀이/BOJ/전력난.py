import sys
input = sys.stdin.readline


def find(x):
    if parents[x] == x:
        return x
    
    parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    parents[max(a, b)] = min(a, b)


booli = True

m, n = map(int, input().split())
while booli:
    M, N = m, n
    nodes = [] 
    parents = [i for i in range(m)]
    total = 0
    while True:
        arr = list(map(int ,input().split()))
        if len(arr) == 2:
            m, n = arr
            if arr[0] == 0 and arr[1] == 0:
                booli = False
            break
        total += arr[2]
        nodes.append(arr)
    nodes.sort(key= lambda x : x[2])



    result = 0
    cnt = 0
    for a, b, c in nodes:
        find_a = find(a)
        find_b = find(b)
        if find_a != find_b:
            union(find_a, find_b)
            result += c
            cnt += 1
            if cnt == M-1:
                break
    print(total-result)