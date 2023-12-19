from flask import Flask, render_template, request, session

from bd_config import Task, Session

app = Flask(__name__)
app.secret_key = 'secret_key'  # не забыть поменять на более сложный


# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "GET":
#         user_id = request.args.get('user_id')
#         session['user_id'] = user_id  # Сохраняем user_id в сессии Flask
#         return render_template("form.html", user_id=user_id)
#     # Теперь у нас есть user_id, который был передан из телеграм-бота
#     if request.method == "POST":
#         try:
#             task_name = request.json.get('taskName')
#             task_description = request.json.get('taskDescription')
#
#             # Получаем user_id из сессии
#             user_id = session.get('user_id')
#             sessions = Session()
#             new_task = Task(task_name=task_name, task_description=task_description, task_user_id=user_id)
#             sessions.add(new_task)
#             sessions.commit()
#         except Exception as e:
#             sessions.rollback()
#             print(f"Error {e}")
#             print("Ошибка добавления записей в БД")
#
#     return render_template("form.html")

print('это ветка бэка')
# и какой-то код
# новый коммент


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
