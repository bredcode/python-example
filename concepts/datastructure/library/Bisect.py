import bisect

def lower_bound(arr, target):
    # target 이상인 첫 번째 위치를 반환
    return bisect.bisect_left(arr, target)

def upper_bound(arr, target):
    # target 초과인 첫 번째 위치를 반환
    return bisect.bisect_right(arr, target)

# 예제 배열 (정렬된 상태여야 함)
sorted_array = [1, 3, 3, 3, 5, 7, 9, 9, 11]

# 테스트
target_value = 3
lb = lower_bound(sorted_array, target_value)
ub = upper_bound(sorted_array, target_value)

print(f"타겟: {target_value} Lower bound index: {lb}")  # 출력: 1
print(f"타겟: {target_value} Upper bound index: {ub}")  # 출력: 4
