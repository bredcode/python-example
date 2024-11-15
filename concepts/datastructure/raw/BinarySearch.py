def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # 중간 인덱스 계산
        if arr[mid] == target:     # 목표 값을 찾은 경우
            return mid
        elif arr[mid] < target:    # 목표 값이 중간 값보다 큰 경우
            left = mid + 1
        else:                      # 목표 값이 중간 값보다 작은 경우
            right = mid - 1

    return -1  # 목표 값을 찾지 못한 경우

# 테스트 코드
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_value = 7

result = binary_search(sorted_array, target_value)
if result != -1:
    print(f"타겟: {target_value} 발견된 인덱스: {result}")
else:
    print(f"타겟 {target_value} 이 리스트에 없습니다")


# def lower_bound(arr, target):
#     left, right = 0, len(arr)
#     while left < right:
#         mid = (left + right) // 2
#         if arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid
#     return left

# def upper_bound(arr, target):
#     left, right = 0, len(arr)
#     while left < right:
#         mid = (left + right) // 2
#         if arr[mid] <= target:
#             left = mid + 1
#         else:
#             right = mid
#     return left

# # 테스트
# sorted_array = [1, 3, 3, 3, 5, 7, 9, 9, 11]
# target_value = 3
# lb = lower_bound(sorted_array, target_value)
# ub = upper_bound(sorted_array, target_value)

# print(f"Lower bound of {target_value} is at index: {lb}")  # 출력: 1
# print(f"Upper bound of {target_value} is at index: {ub}")  # 출력: 4

