from flask import Flask, render_template, request, session, jsonify
from bd_config import Task, Notifications, Session

app = Flask(__name__)
app.secret_key = 'secret_key'  # не забыть поменять на более сложный


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        user_id = request.args.get('user_id')
        session['user_id'] = user_id  # Сохраняем user_id в сессии Flask
        return render_template("index.html", user_id=user_id)
    if request.method == "POST":
        try:
            user_id = session.get('user_id')  # Получаем user_id из сессии
            task_name = request.json.get('taskName')
            task_description = request.json.get('taskDescription')
            date_term = request.json.get('taskDate')

            # Получаем приоритет задачи
            priority_ordinary = 'ordinary' if request.json.get('ordinary') else False
            priority_average = 'average' if request.json.get('average') else False
            priority_urgent = 'urgent' if request.json.get('urgent') else False
            priority_task = next((i for i in [priority_ordinary, priority_average, priority_urgent] if i), None)

            notification = request.json.get('notification')  # Получаем состояние уведомления

            sessions_bd = Session()
            new_task = Task(task_user_id=user_id,
                            task_name=task_name,
                            task_description=task_description,
                            date_term=date_term,
                            task_priority=priority_task,
                            notification=notification)
            sessions_bd.add(new_task)
            sessions_bd.flush()

            # Сохраняем выбранные параметры уведомлений в БД
            if notification:
                notify_daily = request.json.get('notify_daily')
                notify_once = request.json.get('notify_once')
                daily_time = request.json.get('daily_time')
                once_time = request.json.get('once_time')

                if notify_daily:
                    new_notify = Notifications(task_id=new_task.id, notify_type='daily', notify_time=daily_time)
                    sessions_bd.add(new_notify)
                elif notify_once:
                    new_notify = Notifications(task_id=new_task.id, notify_type='once', notify_time=once_time)
                    sessions_bd.add(new_notify)

            sessions_bd.commit()
        except Exception as e:
            print(f"Error {e}")
            print("Ошибка добавления записей в БД")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
