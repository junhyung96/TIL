# 1번부터 N번까지의 사람이 있고 ( 4 <= N <= 20)
# 두 팀으로 나누어야 함
# 두 사람이 만나면 팀에 능력치가 부과됨
# 두 팀의 능력치 차 최솟값을 출력


import sys
input = sys.stdin.readline

N = int(input())
status = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N
result = 1e9
comb = []

def combination(cur):
    global result 
    
    for item in range(cur+1, N):
        comb.append(item)
        # result = min(result, diff_status(comb))
        diff = diff_status(comb)
        if result > diff:
            result = diff
        else:
            return
        combination(item)
        comb.pop()
        
def diff_status(team):
    team1 = team
    team2 = [i for i in range(N) if i not in team1]
    
    sum1 = 0
    sum2 = 0
    
    for i in team1:
        for j in team1:
            sum1 += status[i][j]        
   
    for i in team2:
        for j in team2:
            sum2 += status[i][j]        
    
    return(abs(sum1-sum2))
         
combination(-1)
print(result)