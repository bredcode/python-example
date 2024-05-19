def solution(decimal, n):
    result = ''
    
    while decimal > 0:
        remainder = decimal % n
        result = str(remainder) + result
        decimal //= n
    
    return result if result else '0'


tests = [
  [8, 2],
  [15, 4],
  [248, 8],
  [349, 10]
]

for number, n in tests:
    print(solution(number, n))
