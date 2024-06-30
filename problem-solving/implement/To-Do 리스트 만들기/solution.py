class Todo:
    def __init__(self, id, title, description=None, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def __repr__(self):
        return f"Todo(id={self.id}, title={self.title}, description={self.description}, completed={self.completed})\n"

class TodoManager:
    def __init__(self):
        self.todos = []

    def create_todo(self, todo):
        self.todos.append(todo)
        return todo

    def get_todos(self):
        return self.todos

    def get_todo(self, id):
        for todo in self.todos:
            if todo.id == id:
                return todo
        return None

    def update_todo(self, todo_id, title = None, description = None, completed = None):
        todo = self.get_todo(todo_id)
        if todo is None:
            return None
        if title is not None:
            todo.title = title
        if description is not None:
            todo.description = description
        if completed is not None:
            todo.completed = completed
        return todo

    def delete_todo(self, todo_id):
        todo = self.get_todo(todo_id)
        if todo is not None:
            self.todos.remove(todo)
            return True
        return False

if __name__ == "__main__":
    manager = TodoManager()
    
    ids = []
    for id in range(5):
      ids.append(id)
      todo = Todo(id, f"할 일 {id}", f"할 일 {id} 설명")
      manager.create_todo(todo)
    
    print("모든 할 일:", manager.get_todos())
    for id in ids:
      print(f"특정 할 일 (ID: {id}):", manager.get_todo(id))
    
    manager.update_todo(1, completed=True)
    print("업데이트된 할 일 (ID: 1):", manager.get_todo(1))
    
    manager.delete_todo(2)
    print("할 일 삭제 후 모든 할 일:", manager.get_todos())
