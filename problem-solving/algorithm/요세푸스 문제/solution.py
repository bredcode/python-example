def solution(N, K):
  queue = []

  for i in range(1, N + 1):
    queue.append(i)
 
  ret = []

  while queue:
    for i in range(1, K):
      val = queue.pop(0)
      queue.append(val)
      print(queue)

    ret.append(queue.pop(0))
  
  return ret

print(solution(7, 3)) # [3, 6, 2, 7, 5, 1, 4]
