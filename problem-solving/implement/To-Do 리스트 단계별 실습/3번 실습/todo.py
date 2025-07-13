import json
import os

FILENAME = "todos.json"

# 파일에서 할 일 목록 불러오기
def load_todos():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []

# 파일에 할 일 목록 저장하기
def save_todos():
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

# 전역 변수 todos를 파일에서 불러오기
todos = load_todos()

def show_menu():
    print("\n====== To-Do 리스트 ======")
    print("1. 할 일 생성")
    print("2. 할 일 조회")
    print("3. 할 일 상태 변경")
    print("4. 할 일 삭제")
    print("5. 종료")

def create_todo():
    task = input("할 일을 입력하세요: ")
    if task:
        todos.append({'task': task, 'done': False})
        save_todos()
        print("할 일이 추가되었습니다.")
    else:
        print("빈 값은 추가할 수 없습니다.")

def read_todos():
    if not todos:
        print("등록된 할 일이 없습니다.")
    else:
        print("현재 할 일 목록:")
        idx = 0
        for todo in todos:
            status = "진행 중"
            if todo['done'] == True:
                status = "완료"
            print(f"{idx}. [{status}] {todo['task']}")
            idx += 1

def toggle_todo():
    read_todos()
    if not todos:
        return
    try:
        index = int(input("할 일 상태를 변경할 번호를 입력하세요: "))
        if 0 <= index < len(todos):
            todos[index]['done'] = not todos[index]['done']
            save_todos()
            print("할 일 상태가 변경되었습니다.")
        else:
            print("존재하지 않는 번호입니다.")
    except ValueError:
        print("숫자로 입력해주세요.")

def delete_todo():
    read_todos()
    if not todos:
        return
    try:
        index = int(input("삭제할 번호를 입력하세요: "))
        if 0 <= index < len(todos):
            deleted = todos.pop(index)
            save_todos()
            print(f"'{deleted['task']}' 할 일이 삭제되었습니다.")
        else:
            print("존재하지 않는 번호입니다.")
    except ValueError:
        print("숫자로 입력해주세요.")

# 메인 루프
while True:
    show_menu()
    choice = input("번호를 선택하세요: ")

    if choice == "1":
        create_todo()
    elif choice == "2":
        read_todos()
    elif choice == "3":
        toggle_todo()
    elif choice == "4":
        delete_todo()
    elif choice == "5":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못 입력하였습니다. 다시 입력해주세요.")
