class HeapSort:
    def __init__(self, size):
        # 힙 배열과 원소 개수를 초기화
        self.heap = [0] * (size + 1)
        self.cnt = 0

    def print(self):
        print("=== heap ===")
        print(self.heap[1:self.cnt + 1])

    def push(self, data):
        # 1번 인덱스부터 넣는게 힙의 원칙
        self.cnt += 1
        self.heap[self.cnt] = data

        # 자식과 부모 관계를 설정
        cur = self.cnt
        par = cur // 2

        # 현재 위치보다 부모가 더 크면 -> 최소힙 정의 따라 스왑
        while cur > 1 and self.heap[cur] < self.heap[par]:
            self.heap[cur], self.heap[par] = self.heap[par], self.heap[cur]
            cur = par
            par = cur // 2

    def pop(self):
        if self.cnt == 0:
            return None

        # 루트 데이터 pop
        data = self.heap[1]

        # 힙의 가장 마지막 데이터를 루트로 가져옴
        self.heap[1] = self.heap[self.cnt]
        self.cnt -= 1

        cur = 1
        while True:
            child = cur * 2
            # 최소 힙 정의에 따라 현재 자식 중 더 작은 값으로 이동
            if child < self.cnt and self.heap[child] > self.heap[child + 1]:
                child += 1

            # 더이상 swap하지 않아도 되는 경우
            if child > self.cnt or self.heap[cur] < self.heap[child]:
                break

            self.heap[cur], self.heap[child] = self.heap[child], self.heap[cur]
            cur = child

        return data


# 힙 정렬 객체 생성 및 테스트
min_heap_sort = HeapSort(10)

arr = [29, 10, 14, 37, 8, 27]
for elem in arr:
    min_heap_sort.push(elem)
min_heap_sort.print()

for _ in arr:
    print(min_heap_sort.pop())
