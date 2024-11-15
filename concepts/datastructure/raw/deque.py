class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.sz = 0

    def push_front(self, data):
        node = Node(data)
        self.sz += 1
        if self.front is None:  # 덱이 비어 있는 경우
            self.front = self.rear = node
        else:
            node.next = self.front
            self.front.prev = node
            self.front = node

    def push_back(self, data):
        node = Node(data)
        self.sz += 1
        if self.rear is None:  # 덱이 비어 있는 경우
            self.front = self.rear = node
        else:
            node.prev = self.rear
            self.rear.next = node
            self.rear = node

    def pop_front(self):
        if self.front is None:  # 덱이 비어 있는 경우
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:  # 덱이 비어 있게 된 경우
            self.rear = None
        else:
            self.front.prev = None
        self.sz -= 1
        return data

    def pop_back(self):
        if self.rear is None:  # 덱이 비어 있는 경우
            return None
        data = self.rear.data
        self.rear = self.rear.prev
        if self.rear is None:  # 덱이 비어 있게 된 경우
            self.front = None
        else:
            self.rear.next = None
        self.sz -= 1
        return data

    def size(self):
        return self.sz

    def is_empty(self):
        return self.sz == 0

# 테스트 코드
deque = Deque()

# push_front와 push_back 테스트
deque.push_front(1)
deque.push_back(2)
deque.push_front(0)
deque.push_back(3)

print(deque.pop_front())  # 0
print(deque.pop_back())   # 3
print(deque.pop_front())  # 1
print(deque.size())       # 1
print(deque.pop_back())   # 2
print(deque.is_empty())   # True
