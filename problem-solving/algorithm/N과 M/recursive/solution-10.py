# https://www.acmicpc.net/problem/15664

N, M = None, None
numbers = []
result = []
unique_sequences = set()

def solve(start, depth):
    if depth == M:
        unique_sequences.add(tuple(result))
        return

    for i in range(start, N):
        result.append(numbers[i])
        solve(i + 1, depth + 1)
        result.pop()

# 입력 받기
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()  # 입력된 숫자들을 오름차순으로 정렬
solve(0, 0)

# 결과를 사전 순으로 정렬하여 출력
for sequence in sorted(unique_sequences):
    print(*sequence)
