## 문제

이메일 주소의 개인 정보를 보호하기 위해, 이메일 주소의 도메인을 제외한 모든 문자를 `*`로 가리는 프로그램을 작성하십시오. 이메일 주소가 문자열 `email_address`로 주어졌을 때, 도메인을 제외한 나머지 부분을 모두 `*`로 가린 문자열을 반환하는 함수, `solution`을 완성해주세요.

### 제한 조건

`email_address`는 길이 5 이상, 50이하인 문자열입니다. - 이메일 주소는 항상 "@"를 포함하고, "@"은 한 번만 나타납니다.

### 입출력 예

| email_address           | return                      |
| ----------------------- | --------------------------- |
| "example@gmail.com"     | "**\*\*\***@gmail.com"      |
| "my.email@domain.co.kr" | "**\*\*\*\***@domain.co.kr" |

### 샘플 코드

```python
def solution(email_address):
  # 코드 작성

test_cases = [
    "example@gmail.com",
    "my.email@domain.co.kr"
]

for test in test_cases:
  result = solution(test)
  print(result)
```
