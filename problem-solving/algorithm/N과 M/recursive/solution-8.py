# https://www.acmicpc.net/problem/15657

N, M = None, None
numbers = []
result = []

def solve(start, depth):
    if depth == M:
        print(*result)
        return

    for i in range(start, N):
        result.append(numbers[i])
        solve(i, depth + 1)  # `i`를 그대로 전달해 비내림차순을 유지
        result.pop()

# 입력 받기
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()  # 입력된 숫자들을 오름차순으로 정렬
solve(0, 0)
