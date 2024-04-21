def solution(arr):
  stack = []
  for i in arr:
      if stack and stack[-1] == i:
         continue
      stack.append(i)
  return stack

print(solution([1, 1, 3, 3, 0, 1, 1])) # [1, 3, 0, 1]
print(solution([4, 4, 4, 3, 3])) # [4, 3]