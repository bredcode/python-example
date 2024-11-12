# https://www.acmicpc.net/problem/15651

N, M = None, None
result = []

def solve(depth):
    if depth == M:
        print(*result)
        return

    for i in range(1, N + 1):
        result.append(i)
        solve(depth + 1)
        result.pop()

# 입력 받기
N, M = map(int, input().split())
solve(0)
