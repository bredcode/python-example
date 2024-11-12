# https://www.acmicpc.net/problem/15652

N, M = None, None
result = []

def solve(start, depth):
    if depth == M:
        print(*result)
        return

    for i in range(start, N + 1):
        result.append(i)
        solve(i, depth + 1)  # `i`를 다시 전달해 비내림차순 유지
        result.pop()

# 입력 받기
N, M = map(int, input().split())
solve(1, 0)
