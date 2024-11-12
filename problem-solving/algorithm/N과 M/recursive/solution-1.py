# https://www.acmicpc.net/problem/15649

N, M = None, None
result = []
visited = []

def solve(depth):
    if depth == M:  # depth가 M과 같으면 출력
        print(*result)
        return
    
    for i in range(1, N + 1):
        if not visited[i]:  # 숫자 i가 방문되지 않았을 때
            visited[i] = True
            result.append(i)
            solve(depth + 1)  # depth 증가
            result.pop()
            visited[i] = False

# 입력 받기
N, M = map(int, input().split())
visited = [False] * (N + 1)
solve(0)

