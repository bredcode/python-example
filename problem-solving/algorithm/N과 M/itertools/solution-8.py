# https://www.acmicpc.net/problem/15657

import itertools

def solve(N, M, numbers):
    # 주어진 수열을 오름차순으로 정렬
    numbers.sort()
    
    # M개를 중복 허용하여 비내림차순으로 고르는 조합 생성
    for sequence in itertools.combinations_with_replacement(numbers, M):
        print(*sequence)

# 입력 받기
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

solve(N, M, numbers)