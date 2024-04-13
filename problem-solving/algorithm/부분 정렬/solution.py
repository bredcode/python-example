def solution(array, i, j, k):
  array = array[i - 1:j]
  array = sorted(array)

  return array[k - 1]

print(solution([1, 5, 2, 6, 3, 7, 4], 2, 5, 3)) # 5
print(solution([1, 5, 2, 6, 3, 7, 4], 4, 4, 1)) # 6
print(solution([1, 5, 2, 6, 3, 7, 4], 1, 7, 3)) # 3