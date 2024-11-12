# https://www.acmicpc.net/problem/15651

import itertools

def solve(N, M):
    # 1부터 N까지의 숫자를 M개씩 중복을 허용하여 고르는 경우의 수 생성
    for sequence in itertools.product(range(1, N + 1), repeat=M):
        print(*sequence)

# 입력 받기
N, M = map(int, input().split())
solve(N, M)
