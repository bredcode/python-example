import sqlite3

DB_NAME = "todos.db"

# 데이터베이스 연결 및 테이블 생성
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            done INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

# 파일에서 할 일 목록 불러오기 → DB에서 불러오기
def load_todos():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT task, done FROM todos")
    rows = cur.fetchall()
    conn.close()
    return [{'task': row[0], 'done': bool(row[1])} for row in rows]

# 파일에 할 일 목록 저장하기 → DB 초기화 후 다시 저장
def save_todos():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("DELETE FROM todos")  # 기존 데이터 삭제
    for todo in todos:
        cur.execute("INSERT INTO todos (task, done) VALUES (?, ?)",
                    (todo['task'], int(todo['done'])))
    conn.commit()
    conn.close()

# DB 초기화 및 로드
init_db()
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
