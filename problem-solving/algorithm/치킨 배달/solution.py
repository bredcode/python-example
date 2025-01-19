n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []

# 치킨 거리 계산 함수
def calculate_chicken_distance(selected_chickens):
    total_distance = 0
    for hy, hx in house:
        min_distance = float('inf')
        for cy, cx in selected_chickens:
            distance = abs(hy - cy) + abs(hx - cx)
            min_distance = min(min_distance, distance)
        total_distance += min_distance
    return total_distance

def dfs(selected_chicken, pos):
    # 치킨집 조합이 m개 선택되었으면 거리 계산
    if len(selected_chicken) == m: 
        return calculate_chicken_distance(selected_chicken)
    ret = float('inf')
    for i in range(pos, len(chicken)):  # 현재 위치 pos부터 탐색
        selected_chicken.append(chicken[i])  # 현재 치킨집 추가
        ret = min(ret, dfs(selected_chicken, i + 1)) # 다음 치킨집 탐색
        selected_chicken.pop()  # 탐색이 끝나면 치킨집 제거 (백트래킹)
    return ret

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

result = dfs([], 0)
print(result)
