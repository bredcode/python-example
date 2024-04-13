def solution(expression):
  expression = expression.replace('-', ' -').replace('+', ' +')
  expression = expression.split()
  
  ans = 0
  for i in expression:
    if i.startswith("-"):
        ans -= int(i[1:])
    elif i.startswith("+"):
        ans += int(i[1:])
    else:
        ans += int(i)

  return ans
