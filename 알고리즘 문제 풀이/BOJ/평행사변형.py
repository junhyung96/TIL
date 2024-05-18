# 평행사변형의 세 점이 주어지고 
# 적절한 점을 찾아 평행사변형을 만들어라 여러개 나올 수 있다
# 만들어진 모든 사각형 중 가장 큰 둘레의 길이와
# 가장 작은 둘레의 길이의 차이를 출력
# 만들 수 없다면 -1

# 평행사변형을 만들 수 있는지
# == 삼각형이 가능한가

# 평행사변형을 만들 수 있다면 점을 찾기
# 필요없음

# 둘레 구하기
# 삼각형 변의 길이 중 2개를 선택해 x 2

# 차이 구하기


import sys
from itertools import islice
input = sys.stdin.readline

points = []
tokens = iter(input().rstrip().split())
for _ in range(3):
    points.append(list(map(int, islice(tokens, 2))))

def isTriangle(point1, point2, point3):
    a, b = point1
    c, d = point2
    e, f = point3
    if a == c and c == e:
        return False
    if a != c and c != e and (b-d)/(a-c) == (d-f)/(c-e):
        return False
    return True

def getLength(point1, point2):
    a, b = point1
    c, d = point2
    dist = ((a-c)**2 + (b-d)**2) ** 0.5
    return dist

if not isTriangle(*points):
    print(-1.0)
    exit()

distance_of_points = []

for i in range(3):
    if i != 2:
        distance_of_points.append(getLength(points[i], points[i+1]))
    else:
        distance_of_points.append(getLength(points[i], points[0]))

round_of_parallelograms =[]

for i in range(3):
    if i != 2:
        round_of_parallelograms.append(distance_of_points[i]*2+distance_of_points[i+1]*2)
    else:
        round_of_parallelograms.append(distance_of_points[i]*2+distance_of_points[0]*2)

round_of_parallelograms.sort()

print(round_of_parallelograms[2] - round_of_parallelograms[0])