todos = []  # [{'task': '할 일', 'done': False}, ...]

def show_menu():
    print("\n====== To-Do 리스트 ======")
    print("1. 할 일 생성")
    print("2. 할 일 조회")
    print("3. 할 일 상태 변경" )
    print("4. 할 일 삭제")
    print("5. 종료")

def create_todo():
    print("할 일을 생성합니다.")

def read_todos():
    print("할 일 목록을 조회합니다.")

def toggle_todo():
    print("할 일을 업데이트합니다.")

def delete_todo():
    print("할 일을 삭제합니다.")

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
