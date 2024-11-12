# https://www.acmicpc.net/problem/15652

import itertools

def solve(N, M):
    # 1부터 N까지의 숫자를 M개씩 중복을 허용하며 비내림차순으로 고르는 조합 생성
    for sequence in itertools.combinations_with_replacement(range(1, N + 1), M):
        print(*sequence)

# 입력 받기
N, M = map(int, input().split())
solve(N, M)
