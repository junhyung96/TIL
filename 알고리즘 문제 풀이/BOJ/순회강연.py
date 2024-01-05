# 한 저명한 학자에게 n(0 ≤ n ≤ 10,000)개의 대학에서 강연 요청을 해 왔다. 
# 각 대학에서는 d(1 ≤ d ≤ 10,000)일 안에 와서 강연을 해 주면 
# p(1 ≤ p ≤ 10,000)만큼의 강연료를 지불하겠다고 알려왔다. 
# 각 대학에서 제시하는 d와 p값은 서로 다를 수도 있다. 
# 이 학자는 이를 바탕으로, 가장 많은 돈을 벌 수 있도록 순회강연을 하려 한다. 
# 강연의 특성상, 이 학자는 하루에 최대 한 곳에서만 강연을 할 수 있다.

# 예를 들어 네 대학에서 제시한 p값이 각각 50, 10, 20, 30이고, 
# d값이 차례로 2, 1, 2, 1 이라고 하자. 
# 이럴 때에는 첫째 날에 4번 대학에서 강연을 하고, 
# 둘째 날에 1번 대학에서 강연을 하면 80만큼의 돈을 벌 수 있다.

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = []
univ = [False] * 10001
for _ in range(N):
    p, d = map(int, input().split())
    q.append((p, d))

q.sort(key=lambda x: x[0], reverse=True)
q.sort(key=lambda x: x[1])


result = [0] * 10001 
# print(q)
result[0] = int(1e9)
cur_day = 0
while q:
    p, d = q.pop(0)
    # print(p,d)
    if d > cur_day:
        cur_day += 1
        result[cur_day] = p
    else:
        min_p = min(result[:d])
        idx = result.index(min_p)
        if min_p < p:
            result[idx] = p
        
# print(result[:30])
print(sum(result[1:]))