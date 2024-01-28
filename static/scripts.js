let tg = window.Telegram.WebApp; //получаем объект webapp телеграма
tg.expand(); //расширяем на все окно


document.getElementById('once-time').value = new Date().toTimeString().slice(0, 5);
document.addEventListener('DOMContentLoaded', function () {
    let now = new Date();
    let month = now.getMonth() + 1;
    let day = now.getDate();
    let currentDate = now.getFullYear() + '-' + (month < 10 ? '0' : '') + month + '-' + (day < 10 ? '0' : '') + day;
    document.getElementById('date-task').value = currentDate;
    document.getElementById('date-task').min = currentDate;
});


const textarea = document.querySelector('textarea');
const input_text = document.querySelector('.name-task');
const counter = document.querySelector('.current');
const counter_name = document.querySelector('.current-name');
const div_counter_name = document.querySelector('.counter-name')
const div_counter_task_box = document.querySelector('.counter-task-box')


textarea.addEventListener('input', onInput)
function onInput(event) {
const counter_task_box_length = event.target.value.length;
counter.textContent = counter_task_box_length;
if (counter_task_box_length == 250) {
    div_counter_task_box.style.color = '#bd4242'
}else{
    div_counter_task_box.style.color = '#C8C8D2'
}
}


input_text.addEventListener('input', onInput_name)
function onInput_name(event) {
const counter_task_name_length = event.target.value.length;
counter_name.textContent = counter_task_name_length;
if (counter_task_name_length == 30) {
    div_counter_name.style.color = '#bd4242'
}else{
    div_counter_name.style.color = '#C8C8D2'
}
}



document.addEventListener('DOMContentLoaded', function () {
let radioButtons = document.querySelectorAll('.radio-priority input[type="radio"]');
let priorityTaskBlock = document.querySelector('.priority-task');


radioButtons.forEach(function (radioButton) {
radioButton.addEventListener('change', function () {
    let anyChecked = Array.from(radioButtons).some(function (rb) {
        return rb.checked;
    });

    if (anyChecked) {
        priorityTaskBlock.style.backgroundImage = 'none';
    } else {
        priorityTaskBlock.style.backgroundImage = 'url("star.svg")';
    }
});
});
});



document.addEventListener('input', function(event) {
    if (event.target.tagName.toLowerCase() === 'textarea') {
        adjustTextareaHeight(event.target);
    }
});

function adjustTextareaHeight(textarea) {
    textarea.style.height = 'auto';
    textarea.style.height = (textarea.scrollHeight) + 'px';
}



document.addEventListener('DOMContentLoaded', function () {
  var checkbox = document.getElementById('checkbox');
  var notificationsDiv = document.querySelector('.notifications-div');

  checkbox.addEventListener('change', function () {
    if (checkbox.checked) {
      notificationsDiv.style.maxHeight = '60px';
    } else {
      notificationsDiv.style.maxHeight = '0';
    }
  });
});