from flask import Flask, render_template, request, session, jsonify
from bd_config import Task, Session, DoneTask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key = 'secret_key'  # не забыть поменять на более сложный


# Создание задач
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

            # Сохраняем выбранные параметры уведомлений в БД
            if notification:
                notify_time = request.json.get('once_time')
                new_task.notify_time = notify_time

            sessions_bd.add(new_task)
            sessions_bd.commit()
        except Exception as e:
            print(f"Error {e}")
            print("Ошибка добавления записей в БД")

    return render_template("index.html")


# Получение списка задач
@app.route('/get_tasks', methods=["GET", "POST"])
def get_tasks():
    user_id = request.args.get('user_id')
    session['user_id'] = user_id
    print(user_id)

    sessions = Session()
    tasks = (sessions.query(Task.id,
                            Task.task_name,
                            Task.task_description,
                            Task.date_term,
                            Task.task_priority,
                            Task.notification,
                            Task.notify_time)
             .filter_by(task_user_id=user_id).all())

    tasks_result = [{'task_id': task_id,
                     'task_name': task_name,
                     'task_description': task_description,
                     'date_term': f'{date_term.year}, {date_term.month}, {date_term.day}',
                     'task_priority': task_priority,
                     'notification': notification,
                     'notify_time': f'{notify_time.strftime("%H:%M") if notify_time else None}'}

                    for task_id, task_name, task_description,
                    date_term, task_priority,
                    notification,
                    notify_time in tasks]

    return render_template("tasks.html", tasks_json=tasks_result)


# Выполненные задачи
@app.route('/done_task', methods=['POST', 'GET'])
def done_task():
    if request.method == 'POST':
        get_task = request.json.get('deletedTask')['task_id']
        sessions = Session()
        del_task = sessions.query(Task).get(get_task)
        done_tasks = DoneTask(
            task_user_id=del_task.task_user_id,
            task_name=del_task.task_name,
            task_description=del_task.task_description,
            date_term=del_task.date_term,
            task_priority=del_task.task_priority,
            notification=del_task.notification,
            notify_time=del_task.notify_time
        )

        sessions.add(done_tasks)
        sessions.delete(del_task)
        sessions.commit()
        return jsonify({'status': 'success'})

    if request.method == 'GET':
        user_id = request.args.get('user_id')
        session['user_id'] = user_id

        sessions = Session()
        tasks = (sessions.query(DoneTask.id,
                                DoneTask.task_name,
                                DoneTask.task_description,
                                DoneTask.date_term,
                                DoneTask.task_priority,
                                DoneTask.notification,
                                DoneTask.notify_time)
                 .filter_by(task_user_id=user_id).all())

        tasks_result = [{'task_id': task_id,
                         'task_name': task_name,
                         'task_description': task_description,
                         'date_term': f'{date_term.year}, {date_term.month}, {date_term.day}',
                         'task_priority': task_priority,
                         'notification': notification,
                         'notify_time': f'{notify_time.strftime("%H:%M") if notify_time else None}'}

                        for task_id, task_name, task_description,
                        date_term, task_priority, notification,
                        notify_time in tasks]

        return render_template("done_tasks.html", tasks_json=tasks_result)


@app.route('/clear_done_task', methods=['POST'])
def clear_done_task():
    data = request.get_json()

    if data and data.get('cleared'):
        # Получаем массив удаленных задач из JSON
        deleted_tasks = data.get('deletedTasks', [])

        sessions = Session()
        for task_data in deleted_tasks:
            task_id = task_data.get('task_id')
            task = sessions.query(DoneTask).filter(DoneTask.id == task_id).first()
            sessions.delete(task)

        sessions.commit()

        return jsonify({'status': 'success', 'deletedTasks': deleted_tasks})
    else:
        return jsonify({'status': 'error', 'error': 'Invalid request'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
