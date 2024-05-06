class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_first(self, data):
        new_node = Node(data, self.head)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert_at(self, idx, data):
        if idx == 1:
            self.insert_first(data)
            return
        if idx > self.size:
            raise IndexError("out of index")
        
        new_node = Node(data)
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        if new_node.next is None:
            self.tail = new_node
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            return
        if self.size == 1:
            self.head = self.tail = None
            self.size -= 1
            return

        self.head = self.head.next
        self.size -= 1

    def remove_last(self):
        if self.is_empty():
            return
        if self.size == 1:
            self.head = self.tail = None
            self.size -= 1
            return

        current = self.head
        while current.next != self.tail:
            current = current.next
        
        current.next = None
        self.tail = current
        self.size -= 1

    def remove(self, data):
        if self.is_empty():
            return
        current = self.head

        if current.data == data:
            self.head = current.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return

        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                self.size -= 1
                return
            current = current.next

    def search(self, data):
        idx = 1
        current = self.head
        while current:
            if current.data == data:
                print(f"{idx}번째에 '{data}'가 있습니다.")
                return
            current = current.next
            idx += 1
        print(f"'{data}'가 존재하지 않습니다.")

    def print(self):
        current = self.head
        print(f"=== 크기 : {self.size} ===")
        while current:
            print(current.data)
            current = current.next

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

# 예제 사용
linked_list = LinkedList()

linked_list.insert_first("화")
linked_list.print()
linked_list.insert_first("월")
linked_list.print()
linked_list.insert_last("금")
linked_list.print()
linked_list.insert_at(3, "목")
linked_list.print()
linked_list.insert_at(3, "수")
linked_list.print()

linked_list.search("월")
linked_list.search("화")
linked_list.search("수")
linked_list.search("목")
linked_list.search("금")
linked_list.search("토")
linked_list.search("일")

linked_list.remove("일")
linked_list.print()
linked_list.remove("화")
linked_list.print()
linked_list.remove("목")
linked_list.print()
linked_list.remove("수")
linked_list.print()
linked_list.remove("월")
linked_list.print()
linked_list.remove("금")
linked_list.print()
linked_list.remove("토")
linked_list.print()
