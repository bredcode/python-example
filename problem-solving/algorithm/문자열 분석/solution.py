def solution(string):

  # 각 문자열에 대해 소문자, 대문자, 숫자, 공백의 개수를 계산하여 출력
  answer = [0, 0, 0, 0]
  for ch in string:
    if ch.islower():
        answer[0] += 1
    elif ch.isupper():
        answer[1] += 1
    elif ch.isdigit():
        answer[2] += 1
    elif ch.isspace():
        answer[3] += 1

  return answer

tests = [
  "This is String",
  "SPACE    1    SPACE",
  " S a M p L e I n P u T     ",
  "0L1A2S3T4L5I6N7E8"
]

for test in tests:
  print(solution(test))