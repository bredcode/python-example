# https://www.acmicpc.net/problem/15650

import itertools

def solve(N, M):
    # 1부터 N까지의 숫자를 M개씩 고르는 조합 생성
    for sequence in itertools.combinations(range(1, N + 1), M):
        print(*sequence)

# 입력 받기
N, M = map(int, input().split())
solve(N, M)
