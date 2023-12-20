function submitForm(event) {
            event.preventDefault();

            // Получаем значения полей формы
            let taskName = document.getElementById("name-task-id").value;
            let taskDescription = document.getElementById("taskDescription").value;
            let userId = document.getElementById("user_id").value;

            // Создаем объект JSON
            let jsonData = {
                taskName: taskName,
                taskDescription: taskDescription,
                user_id: userId
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
        }