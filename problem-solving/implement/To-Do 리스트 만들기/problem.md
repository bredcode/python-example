## To-Do 리스트 만들기

### 문제

사용자가 할 일을 추가하고, 조회하고, 삭제할 수 있는 간단한 To-Do 리스트 API를 작성하세요.

각 할 일(To-Do)은 다음과 같은 정보를 포함합니다

```
id: 할 일의 고유 식별자 (id는 0부터 시작)
title: 할 일의 제목
description: 할 일의 설명
completed: 할 일의 완료 여부 (기본값: False)
```

### 요구 기능

- 할 일 추가(create_todo): 새로운 할 일을 추가합니다.
- 할 일 목록 조회(get_todos): 모든 할 일을 조회합니다.
- 특정 할 일 조회(get_todo): id를 이용해 특정 할 일을 조회합니다.
- 할 일 삭제(delete_todo): id를 이용해 특정 할 일을 삭제합니다.
- 할 일 완료 상태 업데이트(update_todo): id를 이용해 특정 할 일의 완료 상태를 업데이트합니다.

### 예제

```
class Todo:
    ... 작성

    # __repr__ : 클래스를 출력할 때 하나하나 출력할 필요없이 그냥 print(todo)를 하면 아래 포멧에 맞게 출력됨
    def __repr__(self):
        return f"Todo(id={self.id}, title={self.title}, description={self.description}, completed={self.completed})\n"

class TodoManager:
    create_todo, get_todos, get_todo, update_todo, delete_todo
        ... 작성

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
```

### 정답

```python
모든 할 일: [Todo(id=0, title=할 일 0, description=할 일 0 설명, completed=False)
, Todo(id=1, title=할 일 1, description=할 일 1 설명, completed=False)
, Todo(id=2, title=할 일 2, description=할 일 2 설명, completed=False)
, Todo(id=3, title=할 일 3, description=할 일 3 설명, completed=False)
, Todo(id=4, title=할 일 4, description=할 일 4 설명, completed=False)
]
특정 할 일 (ID: 0): Todo(id=0, title=할 일 0, description=할 일 0 설명, completed=False)

특정 할 일 (ID: 1): Todo(id=1, title=할 일 1, description=할 일 1 설명, completed=False)

특정 할 일 (ID: 2): Todo(id=2, title=할 일 2, description=할 일 2 설명, completed=False)

특정 할 일 (ID: 3): Todo(id=3, title=할 일 3, description=할 일 3 설명, completed=False)

특정 할 일 (ID: 4): Todo(id=4, title=할 일 4, description=할 일 4 설명, completed=False)

업데이트된 할 일 (ID: 1): Todo(id=1, title=할 일 1, description=할 일 1 설명, completed=True)

할 일 삭제 후 모든 할 일: [Todo(id=0, title=할 일 0, description=할 일 0 설명, completed=False)
, Todo(id=1, title=할 일 1, description=할 일 1 설명, completed=True)
, Todo(id=3, title=할 일 3, description=할 일 3 설명, completed=False)
, Todo(id=4, title=할 일 4, description=할 일 4 설명, completed=False)
]
```
