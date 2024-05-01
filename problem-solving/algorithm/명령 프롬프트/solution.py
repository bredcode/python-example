def solution(n, arr):
  max_len = 0
  for i in arr:
    max_len = max(max_len, len(i))

  ret = ""
  for j in range(0, max_len):
    is_same = True
    ch = arr[0][j]
    for i in range(0, len(arr)):
      if ch != arr[i][j]:
        is_same = False
        break
    if not is_same:
      ret += "?"
    else:
      ret += ch

  return ret

print(solution(3, ["config.sys","config.inf","configures"]))
print(solution(2, ["contest.txt","context.txt"]))