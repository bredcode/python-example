## 📘 5. To-Do 리스트 서버(API)로 전환하기

### 🎯 실습 목표

이 실습에서는 기존에 SQLite 데이터베이스를 사용하여 로컬에서 동작하던 To-Do 리스트 프로그램을  
**Flask 웹 서버로 전환**하여, 외부에서 **HTTP 요청을 통해 데이터를 관리할 수 있는 API 형태로 확장**합니다.

즉, 기존에 터미널로 조작하던 할 일 목록 기능을 **웹 API 형태로 외부에서 사용 가능하게 만드는 것**이 목표입니다.

---

### 📂 사전 준비

이 실습은 4단계에서 구현한 `todo.py` 모듈을 **그대로 재사용**하되,  
Flask를 이용해 서버(`server.py`)를 별도의 파일로 만들어  
해당 모듈을 **임포트하여 API 형태로 연결**하는 방식으로 구성됩니다.

디렉토리 구조 예:

```bash
project/
├── todo.py
└── server.py
```

---

### 🧩 기능 요구 사항

1.  **Flask 서버 구현**

    - `Flask`를 사용해 RESTful API 서버를 구현합니다.
    - `server.py` 파일에서 실행되며, `todo.py` 모듈의 함수들을 직접 호출합니다.

2.  **REST API 엔드포인트**

    | 기능      | HTTP 메서드 | 경로           | 설명                          |
    | --------- | ----------- | -------------- | ----------------------------- |
    | 전체 조회 | GET         | /todos         | 전체 할 일 목록 반환          |
    | 추가      | POST        | /todos         | 새 할 일 추가                 |
    | 상태 변경 | PUT         | /todos/{index} | 특정 인덱스의 할 일 상태 토글 |
    | 삭제      | DELETE      | /todos/{index} | 특정 인덱스의 할 일 삭제      |

3.  **요청/응답 형식**

    - `POST /todos` 요청 시 JSON 형식으로 전달:

      ```json
      { "task": "할 일 내용" }
      ```

    - 응답은 JSON 형식 메시지 또는 전체 목록입니다.

4.  **에러 처리**

    - 유효하지 않은 인덱스 접근, 빈 입력값 등에 대한 처리 포함
    - HTTP 상태 코드 사용 (`200`, `400`, `404` 등)

5.  **서버 실행 후 동작 예시**

    ```bash
    python server.py
    Running on http://127.0.0.1:5000/
    ```

    - 브라우저 또는 Postman, curl을 통해 API 테스트 가능

---

### 💡 힌트

1.  Flask 설치 필요 시:

    ```shell
    pip install flask
    ```

2.  `todo.py`는 그대로 사용하고 `create_todo(task)`, `toggle_todo(index)` 등의 함수가 외부에서 import 되어 사용됩니다.
3.  서버가 사용하는 Flask 코드 예(단순 예시):

    ```python
    from flask import Flask, request, jsonify import todo

    app = Flask(__name__)
    @app.route("/todos", methods=["GET"])
    def get_all():
        return jsonify(todo.get_all_todos())
    ```

4.  POST 요청은 JSON 본문(body)에서 `request.get_json()`을 통해 데이터를 추출합니다.
