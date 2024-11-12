# https://www.acmicpc.net/problem/15650

N, M = None, None
result = []

def solve(start, depth):
    if depth == M:
        print(*result)
        return

    for i in range(start, N + 1):
        result.append(i)
        solve(i + 1, depth + 1)
        result.pop()

# 입력 받기
N, M = map(int, input().split())
solve(1, 0)

