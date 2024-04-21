def solution(ps):
  stack = []
  for i in ps:
      if i == '(':
          stack.append(i)
      elif i == ')':
          if stack:
              stack.pop()
          # 스택에 '('가 더이상 없는 경우
          else:
              print("NO")
              return
  # 괄호 쌍이 모두 맞지 않아 스택에 남은 경우
  if stack:
      print('NO')
  else:
      print('YES')
  return

n = int(input())
for i in range(n):
    ps = input()
    solution(ps)