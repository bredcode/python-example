from collections import deque

def solution(str):
    dq = deque()
    
    for ch in str:
        dq.append(ch)

    while len(dq) > 1:
        first = dq.pop()
        last = dq.popleft()
        if first != last:
            return False

    return True

print(solution("helleh")) # True
print(solution("heldleh")) # True
print(solution("heldeleh")) # True