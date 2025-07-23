from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 메모를 저장할 오브젝트 (리스트)
notes = []

# 메모장 홈 페이지
@app.route('/')
def index():
    return render_template('index.html', notes=notes)

# 메모 추가
@app.route('/add', methods=['POST'])
def add():
    note = request.form['note']
    notes.append(note)  # 메모 리스트에 추가
    print(notes)
    return redirect(url_for('index'))

# 메모 삭제
@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(notes):
        del notes[index]  # 지정된 인덱스의 메모 삭제
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
