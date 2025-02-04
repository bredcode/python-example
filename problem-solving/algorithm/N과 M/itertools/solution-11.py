# https://www.acmicpc.net/problem/15665

import itertools

def solve(N, M, numbers):
    # 주어진 수열을 오름차순으로 정렬
    numbers.sort()
    
    # 중복된 수열을 저장할 set
    unique_sequences = set()
    
    # M개를 고르는 모든 중복 순열 생성
    for sequence in itertools.product(numbers, repeat=M):
        unique_sequences.add(sequence)
    
    # 중복 제거 후 사전 순으로 정렬하여 출력
    for sequence in sorted(unique_sequences):
        print(*sequence)

# 입력 받기
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

solve(N, M, numbers)
