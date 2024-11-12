class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
    self.sz = 0
  
  def push(self, data):
    node = Node(data)
    self.sz += 1
    if self.top is None:
      self.top = node
    else:
      node.next = self.top
      self.top = node
  
  def pop(self):
    if self.top is None:
      return None
    
    node = self.top
    self.top = self.top.next
    self.sz -= 1
    
    return node.data

  def peek(self):
    if self.top is None:
      return None
    
    return self.top.data
  
  def size(self):
    return self.sz
  
  def is_empty(self):
    return self.top is None
  
stack = Stack()

for i in range(1, 10):
  stack.push(i)

print(stack.pop()) # 9
print(stack.pop()) # 8
print(stack.pop()) # 7
print(stack.size()) # 6
print(stack.pop()) # 6
print(stack.pop()) # 5
print(stack.peek()) # 4
print(stack.is_empty()) # False