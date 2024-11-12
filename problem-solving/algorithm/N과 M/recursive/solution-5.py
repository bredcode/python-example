# https://www.acmicpc.net/problem/15654

N, M = None, None
numbers = []
result = []
visited = []

def solve(depth):
    if depth == M:
        print(*result)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result.append(numbers[i])
            solve(depth + 1)
            result.pop()
            visited[i] = False

# 입력 받기
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()  # 입력된 숫자들을 오름차순으로 정렬
visited = [False] * N
solve(0)
