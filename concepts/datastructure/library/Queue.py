from collections import deque

# 큐 생성
queue = deque()

# 큐에 원소 추가 (enqueue)
queue.append(1)
queue.append(2)
queue.append(3)

print("큐 상태:", list(queue)) # 출력: 큐 상태: [1, 2, 3]

# 큐에서 원소 제거 (dequeue)
print("dequeue:", queue.popleft()) # 출력: dequeue: 1
print("큐 상태:", list(queue)) # 출력: 큐 상태: [2, 3]