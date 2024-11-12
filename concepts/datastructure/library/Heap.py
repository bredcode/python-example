import heapq

# 힙 생성 (기본적으로 최소 힙)
min_heap = []

# 힙에 원소 추가 (push)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 4)
heapq.heappush(min_heap, 2)

print("최소 힙 상태:", min_heap)  # 출력: 최소 힙 상태: [1, 2, 4, 3]

# 힙에서 원소 제거 (pop)
print("pop:", heapq.heappop(min_heap))  # 출력: pop: 1
print("최소 힙 상태:", min_heap)        # 출력: 최소 힙 상태: [2, 3, 4]

# 최대 힙을 만들기 위해서는 부호를 반전
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -4)
heapq.heappush(max_heap, -2)

print("최대 힙 상태:", [-x for x in max_heap])  # 출력: 최대 힙 상태: [4, 2, 3, 1]

# 힙에서 원소 제거 (pop)
print("pop:", -heapq.heappop(max_heap))  # 출력: pop: 4
print("최대 힙 상태:", [-x for x in max_heap]) # 출력: 최대 힙 상태: [3, 2, 1]
