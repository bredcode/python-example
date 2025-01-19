from collections import deque

def bfs():
    # 방향 벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0)])  # 시작점 (0, 0)
    maze[0][0] = 1  # 시작 위치는 이미 방문했으므로 1로 초기화

    while queue:
        x, y = queue.popleft()
        
        # 도착 지점에 도달하면 최소 칸 수 반환
        if x == n - 1 and y == m - 1:
            return maze[x][y]

        # 4가지 방향 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 유효한 범위 내에 있고 이동할 수 있는 칸인 경우
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1  # 이동한 칸 수 저장

# 입력 받기
n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

# BFS 실행 및 결과 출력
print(bfs())
