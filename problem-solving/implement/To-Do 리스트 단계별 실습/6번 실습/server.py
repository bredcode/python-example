from flask import Flask, request, jsonify, render_template, redirect
import todo

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", todos=todo.load_todos())

@app.route("/todos", methods=["POST"])
def create_todo():
    task = request.form.get("task")
    if not task:
        return redirect("/")
    todo.create_todo(task)
    return redirect("/")

@app.route("/todos/<int:index>", methods=["PUT"])
def toggle(index):
    toggled = todo.toggle_todo(index)
    if toggled:
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
