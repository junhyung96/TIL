# 첫째 줄에 대회의 정보 penalty, start, last, ce, cscore, format이 주어진다.
# 둘째 줄에 대회에 포함된 문제의 수 N (1 ≤ N ≤ 26)이 주어진다.
# 셋째 줄부터 N개의 줄에 대회 문제의 값 id, order, pscore가 한 줄에 하나씩 주어진다.
# 다음 줄에는 대회에 참가한 유저의 수 M (1 ≤ M ≤ 1,000)이 주어지고, 그 다음 줄에 대회에 참가한 유저의 아이디가 주어진다.
# 그 다음 줄에는 이 대회에 제출된 제출의 수 S (1 ≤ S ≤ 1,000,000)가 주어진다.
# 다음 S개의 줄에 제출의 정보 sid, pid, uid, result, presult, score, date가 한 줄에 하나씩 주어진다. 제출은 제출 번호가 증가하는 순이다.
# 대회에 참가한 유저의 아이디에 포함되지 않은 유저의 제출도 주어질 수 있다. 이 경우에는 그 유저의 모든 제출을 무시한다.

# ------------------------------------------------------------------------------------------------------------------------------------- 

# 총 M개의 줄을 출력해야 한다. 우선 순위가 높은 사람부터 낮은 사람까지 다음 정보를 한 줄에 하나씩 ,로 구분해 출력해야 한다.

# 유저의 등수
# 유저의 아이디
# 유저 u의 문제 p에 대한 결과, 문제는 대회 문제의 값 order의 오름차순으로 출력해야 한다.

# 일반 대회
# 맞은 경우: "a/시도한 횟수/획득한 페널티"
# 시도를 한 적은 있으나 맞지 못한 경우: "w/시도한 횟수/--"
# 시도를 한 적이 없는 경우: "0/--"

# 점수 대회
# 맞은 경우: "성공 여부/좋은 제출의 점수/시도한 횟수/획득한 페널티"
# 성공 여부는 좋은 제출의 점수가 문제의 배점이 같으면 a, 아니면 p이다.
# 시도를 한 적은 있으나 좋은 제출이 없는 경우: "w/시도한 횟수/--"
# 시도를 한 적이 없는 경우: "0/--"
# 유저의 최종 정보 "획득한 점수/유저의 페널티"

import sys
input = sys.stdin.readline

penalty, *start, last, ce, cscore, format = input().split()
# print(penalty, start, last, ce, cscore, format)
penalty, last, ce, cscore, format = int(penalty), int(last), int(ce), int(cscore), int(format)

class Problem:
    def __init__(self, id, order, pscore):
        self.id = id
        self.order = order
        self.pscore = pscore





N = int(input()) # 대회에 포함된 문제의 수
for _ in range(N):
    competition = []
    id, order, pscore = map(int, input().split())
    competition.append(Problem(id, order, pscore))
    # for comp in competition:
    #     print(comp.id, comp.order, comp.pscore)

S = int(input()) # 제출된 문제의 수