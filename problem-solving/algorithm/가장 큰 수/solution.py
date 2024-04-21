def solution(N, K):
  stack = []

  for i in N:
    if not stack:
      stack.append(i)
    else:
      while stack and i > stack[-1] and K > 0:
        ret = stack.pop()
        K -= 1
      stack.append(i)
  
  while K > 0:
    stack.pop()
    K -= 1
  
  return "".join(stack)

print(solution("5477292842", 4))