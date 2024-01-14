# 하노이탑 이동순서
# N 개의 원판을 이동
# 1번 2번 3번 기둥이 있다
# 시작위치 1번기둥
# 목표 3번기둥으로 모두 옮기기
# 1번 기둥의 제일 밑 원판을 3번 기둥으로 옮기려면
# 1. N-1개의 원판들은 2번기둥으로 모두 이동시킨다
# 2. 제일 밑 원판을 3번 기둥으로 이동시킨다
# 3. 2번 기둥의 원판들을 3번 기둥으로 이동시킨다
# 4개 이동 시켜보자
# 1234 0 0
# 4 123 0
# 0 123 4
# 0 0 1234

def hanoi(start, end, n):
    global cnt
    cnt += 1
    if n == 1:
        arr.append((start, end))
        return
    hanoi(start, 6-start-end, n-1)
    arr.append((start, end))
    hanoi(6-start-end, end, n-1)

N = int(input())
cnt = 0
arr = []
hanoi(1, 3, N)
print(cnt)
for item in arr:
    print(item[0], item[1]) 