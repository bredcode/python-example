def solution(email_address):
    # 도메인을 찾기 위해 '@'의 위치를 찾습니다.
    at_index = email_address.index('@')

    # '@' 앞의 문자들을 '*'로 대체하고 도메인은 그대로 유지합니다.
    hidden_part = '*' * at_index
    domain = email_address[at_index:]

    # 결과 문자열을 반환합니다.
    return hidden_part + domain

test_cases = [
    "example@gmail.com",
    "my.email@domain.co.kr"
]

for test in test_cases:
  result = solution(test)
  print(result)