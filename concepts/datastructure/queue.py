class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def push(self, data):
        new_node = Node(data, None)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            self.size += 1
            return

        self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return

        cur = self.front
        self.front = self.front.next
        print(cur.data)
        self.size -= 1

    def print(self):
        cur = self.front
        print(f'크기 : {self.get_size()}')
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

queue = Queue()

queue.push("월")
queue.push("화")
queue.push("수")
queue.push("목")
queue.push("금")
queue.print() # 월 화 수 목 금
print("-------")

queue.pop() # 월
queue.pop() # 화
queue.pop() # 수
queue.pop() # 목
queue.pop() # 금
queue.pop() # None
