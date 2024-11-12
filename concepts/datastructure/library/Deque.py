from collections import deque

# 덱 생성
d = deque()

# 덱의 양쪽에 원소 추가
d.append(1) # 오른쪽에 추가
d.appendleft(2) # 왼쪽에 추가
d.append(3) # 오른쪽에 추가
d.appendleft(4) # 왼쪽에 추가

print("덱 상태:", list(d)) # 출력: 덱 상태: [4, 2, 1, 3]

# 덱의 양쪽에서 원소 제거
print("오른쪽 제거:", d.pop()) # 출력: 오른쪽 제거: 3
print("왼쪽 제거:", d.popleft()) # 출력: 왼쪽 제거: 4
print("덱 상태:", list(d)) # 출력: 덱 상태: [2, 1]