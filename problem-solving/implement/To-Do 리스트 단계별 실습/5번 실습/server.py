from flask import Flask, request, jsonify
import todo

app = Flask(__name__)

@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todo.load_todos()), 200

@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()
    task = data.get("task")
    if not task:
        return jsonify({"error": "할 일을 입력해주세요."}), 400
    todo.create_todo(task)
    return jsonify({"message": "할 일이 추가되었습니다."}), 200

@app.route("/todos/<int:index>", methods=["PUT"])
def toggle(index):
    if todo.toggle_todo(index):
        return jsonify({"message": "할 일 상태가 변경되었습니다."}), 200
    return jsonify({"error": "존재하지 않는 번호입니다."}), 404

@app.route("/todos/<int:index>", methods=["DELETE"])
def delete(index):
    deleted = todo.delete_todo(index)
    if deleted:
        return jsonify({"message": f"'{deleted}' 할 일이 삭제되었습니다."}), 200
    return jsonify({"error": "존재하지 않는 번호입니다."}), 404

if __name__ == "__main__":
    app.run(debug=True)
