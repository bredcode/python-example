def solution(data1, data2):
  ans = "TRUE" if sorted(data1) == sorted(data2) else "FALSE"
  return ans


print(solution("blather", "reblath"))
print(solution("maryland", "landam"))
print(solution("bizarre", "brazier"))