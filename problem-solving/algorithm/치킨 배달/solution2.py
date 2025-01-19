from itertools import combinations

# 거리 계산 함수
def calculate_chicken_distance(house, chicken):
    total_distance = 0
    for hy, hx in house:
        min_distance = float('inf')
        for cy, cx in chicken:
            distance = abs(hy - cy) + abs(hx - cx)
            min_distance = min(min_distance, distance)
        total_distance += min_distance
    return total_distance
    
n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

# 집과 치킨집 위치 저장
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

# 치킨집 선택 및 최소 거리 계산
min_distance = float('inf')
for selected_chicken in combinations(chicken, m):
    distance = calculate_chicken_distance(house, selected_chicken)
    min_distance = min(min_distance, distance)

print(min_distance)
