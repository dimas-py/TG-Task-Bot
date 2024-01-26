function submitForm(event) {
            event.preventDefault();

            // Получаем значения полей формы
            let taskName = document.getElementById("name-task-id").value;
            let taskDescription = document.getElementById("taskDescription").value;
            let taskDate = document.getElementById("date-task").value;
            let userId = document.getElementById("user_id").value;

            // Получаем приоритет задачи
            let ordinary = document.getElementById("ordinary").checked;
            let average = document.getElementById("average").checked;
            let urgent = document.getElementById("urgent").checked;

            // Получаем информацию об уведомлениях
            let notification = document.getElementById("checkbox").checked;
            let once_time = document.getElementById('once-time').value

            // Создаем объект JSON
            let jsonData = {
                taskName: taskName,
                taskDescription: taskDescription,
                user_id: userId,
                taskDate: taskDate,
                ordinary: ordinary,
                average: average,
                urgent: urgent,
                notification: notification,
                once_time: once_time
            };

            // отладка
            console.log("JSON Data:", jsonData);

            // Отправляем данные на сервер
            fetch('/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(jsonData)
            })
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.error('Error:', error));

            // Закрытие окна приложения, после нажатия "Создать задачу"
            setTimeout(() => {
                let tg = window.Telegram.WebApp;
                tg.sendData(taskName);
            }, 300); // где 1000, ждать 1 секунду
        }