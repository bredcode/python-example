def isHanNumber(n):
    n = str(n)
    digits = []

    for ch in n:
        digits.append(int(ch))

    if len(digits) <= 2:
        return True

    diff = digits[1] - digits[0]
    for i in range(1, len(digits) - 1):
        if digits[i + 1] - digits[i] != diff:
            return False

    return True

def solution(N):
    count = 0
    for i in range(1, N + 1):
        if isHanNumber(i):
            count += 1

    return count

print(solution(110)) # 99