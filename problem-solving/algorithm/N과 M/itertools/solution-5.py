# https://www.acmicpc.net/problem/15654

import itertools

def solve(N, M, numbers):
    # 주어진 수열을 오름차순으로 정렬
    numbers.sort()
    
    # 정렬된 숫자 리스트에서 M개를 고르는 모든 순열 생성
    for sequence in itertools.permutations(numbers, M):
        print(*sequence)

# 입력 받기
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

solve(N, M, numbers)
