# https://www.acmicpc.net/problem/15656

import itertools

def solve(N, M, numbers):
    # 주어진 수열을 오름차순으로 정렬
    numbers.sort()
    
    # 정렬된 숫자 리스트에서 M개를 중복을 허용하며 고르는 경우의 수 생성
    for sequence in itertools.product(numbers, repeat=M):
        print(*sequence)

# 입력 받기
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

solve(N, M, numbers)
