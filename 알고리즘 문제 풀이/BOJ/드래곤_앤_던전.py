# 용사는 공주를 구하기 위해 무시무시한 용이 있는 던전으로 향하기로 하였습니다. 
# 우선 용사는 용사 자신과 던전을 분석하였습니다.

# 용사에게는 세 종류의 능력치가 있습니다. 

# HMaxHP : 용사의 최대 생명력입니다. 이 값은 1이상이어야 하며 던전에 들어간 이후로 변하지 않습니다.
# HCurHP : 현재 용사의 생명력입니다. 던전에 들어가기 전 이 값은 용사의 최대 생명력 HMaxHP와 같습니다. 이 값은 HMaxHP보다 커질 수 없습니다.
# HATK : 용사의 공격력입니다.
# 던전은 총 N개의 방으로 이루어져 있고 i번째 방을 통해서만 i+1번째 방으로 이동 할 수 있습니다. 방에는 포션이 있거나 몬스터가 있는데 몬스터가 있을 경우 몬스터를 쓰러트려야지 다음방으로 이동 할 수 있습니다. N번째 방에는 공주와 용이 있고, 용을 무찌르면 공주를 구할 수 있습니다.

# 몬스터가 있는 방에 올 경우 다음과 같이 전투가 진행됩니다.

# 용사의 공격력 HATK만큼 몬스터의 생명력을 깎습니다.
# 몬스터의 생명력이 0 이하이면 전투가 종료되고 용사는 다음 방으로 이동합니다.
# 몬스터의 공격력만큼 용사의 생명력 HCurHP를 깎습니다.
# 용사의 생명력이 0 이하이면 전투가 종료되고 용사는 사망합니다.
# 다시 1부터 진행합니다.
# 포션이 있는 방에 올 경우 포션을 마셔서 현재 용사의 생명력 HCurHP가 일정량 회복되고 공격력 HATK도 일정량만큼 증가됩니다. 회복된 생명력이 최대 생명력 HMaxHP보다 큰 경우 용사의 현재 생명력 HCurHP가 최대 생명력 HMaxHP와 같아집니다.

# 용사는 던전으로 향하기 전에 만반의 준비를 하고 있습니다. 용사는 수련을 하면 최대 생명력 HMaxHP를 늘릴 수 있는데 얼마나 수련해야 할지 고민입니다.

# 용사는 N번 방에 있는 용을 쓰러트리기 위한 최소의 HMaxHP를 여러분이 계산해주면 좋겠다고 합니다.
import sys
input = sys.stdin.readline

N, ATK = map(int, input().split())

room_atk = [0] * (N+1)
room_atk[0] = ATK
info_rooms = []

# i+1번째 줄엔 i번째 방의 정보를 나타내는 세개의 정수 ti, ai, hi (ti ∈ {1, 2}, 1 ≤ ai, hi  ≤ 1,000,000) 가 주어집니다. 
# ti가 1인 경우 공격력이 ai이고 생명력이 hi인 몬스터가 있음을 나타내고, ti가 2인 경우 용사의 공격력 HATK를 ai만큼 증가시켜주고 용사의 현재 생명력 HCurHP를 hi만큼 회복시켜주는 포션이 있음을 나타냅니다.
for room_i in range(1, N+1):
    ti, a, h = map(int, input().split())
    info_rooms.append([ti, a, h])
    if ti == 2:
        ATK += a
    room_atk[room_i] = ATK
    # ti 1 공격력 a, 생명력 h 인 몬스터 존재
    # ti 2 용사 공격력 a만큼 증가, 용사 현재 생명력 h 만큼 회복

def game(HP):
    max_HP = HP

    for i in range(N):
        ti, a, h = info_rooms[i]
        if ti == 1:
            if h % room_atk[i+1] == 0:
                battle = h // room_atk[i+1] - 1
            else:
                battle = h // room_atk[i+1]
            HP -= a * battle
            if HP <= 0:
                return False
        
        if ti == 2:
            HP = min(max_HP, HP + h)
            
    return True


s = 1
e = int(1e19)

while True:    

    if s >= e:
        break
    mid = (s + e) // 2
    # print(i, s, mid , e)
    if game(mid):
        e = mid
    else:
        s = mid + 1 

print(e)
# for i in range(40, 60):
#     print(i, game(i))  

