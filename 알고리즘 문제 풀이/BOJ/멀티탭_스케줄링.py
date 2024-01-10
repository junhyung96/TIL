# 기숙사에서 살고 있는 준규는 한 개의 멀티탭을 이용하고 있다. 
# 준규는 키보드, 헤어드라이기, 핸드폰 충전기, 디지털 카메라 충전기 등 
# 여러 개의 전기용품을 사용하면서 어쩔 수 없이 각종 전기용품의 플러그를 뺐다 꽂았다 하는 불편함을 겪고 있다. 
# 그래서 준규는 자신의 생활 패턴을 분석하여, 자기가 사용하고 있는 전기용품의 사용순서를 알아내었고, 
# 이를 기반으로 플러그를 빼는 횟수를 최소화하는 방법을 고안하여 보다 쾌적한 생활환경을 만들려고 한다.

# 예를 들어 3 구(구멍이 세 개 달린) 멀티탭을 쓸 때, 전기용품의 사용 순서가 아래와 같이 주어진다면,

# 키보드
# 헤어드라이기
# 핸드폰 충전기
# 디지털 카메라 충전기
# 키보드
# 헤어드라이기
# 키보드, 헤어드라이기, 핸드폰 충전기의 플러그를 순서대로 멀티탭에 꽂은 다음
# 디지털 카메라 충전기 플러그를 꽂기 전에 핸드폰충전기 플러그를 빼는 것이 최적일 것이므로 플러그는 한 번만 빼면 된다.

import sys
input = sys.stdin.readline 
INF = int(1e9)

N, K = map(int, input().split()) # 멀티탭 플러그 수, 전기 용품 사용 수
schedule = list(map(int, input().split()))

number_of_plugs = len(schedule)
current_plugs = [0] * N
# 현재 사용중인 콘센트 구멍마다 플러그번호를 저장해두고 
change_count = 0
# 반복되는지 반복되면 몇번째에 사용될건지 저장해두고
# 제일 나중에 사용되거나 재사용되지않는 플러그를 뽑고 거기에 다음 거 사용하기
used = 0

for idx in range(number_of_plugs):
    item = schedule[idx]

    if item in current_plugs:
        continue
    
    if used < N:
        current_plugs[current_plugs.index(0)] = item
        used += 1
        continue
    
    repeated_item_idx = [INF] * N
    for j in range(N):
        for i in range(idx+1, len(schedule)):
            if schedule[i] == current_plugs[j]:
                repeated_item_idx[j] = i
                break
    next_item = max(repeated_item_idx)
    change_plug_index = repeated_item_idx.index(next_item)
    current_plugs[change_plug_index] = item
    change_count += 1

print(change_count)
     