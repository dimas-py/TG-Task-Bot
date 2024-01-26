import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
import time
from bd_config import User,Task, Session
from keyboard import create_main_keyboard

BOT_TOKEN = "6481132072:AAEcFRg5bH9eEgzUXHMdyzOkdTHClDAqrfw"
FLASK_URL = 'https://f6dd-94-231-133-134.ngrok-free.app'
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    main_kb = create_main_keyboard(user_id, FLASK_URL)

    # Проверяем, существует ли пользователь в базе данных
    if not user_exists(user_id):
        # Если пользователя нет, сохраняем его в базе данных
        save_user(user_id, first_name)
        await message.reply("Поздравляем! Теперь вы базе данных!🤡")
    else:
        await message.reply("Вы уже наш чел!👌")

    await message.answer(f'Привет, {first_name}!😘', reply_markup=main_kb)
    # asyncio.create_task(test(message))


@dp.message()
async def answer(message: Message):
    await message.answer(f"Задача <b>«{message.web_app_data.data}»</b> создана!")


# Новая функция для отправки уведомлений
async def send_notification(user_id, message):
    await bot.send_message(user_id, message)


# Новая функция для получения задач, которые нужно уведомить
def get_tasks_to_notify(current_datetime):
    session = Session()
    tasks_to_notify = (
        session.query(Task)
        .filter(Task.notification == 1)
        .filter(Task.notify_time <= current_datetime)
        .filter(Task.date_term <= current_datetime)
        .all()
    )
    session.close()
    return tasks_to_notify


# Отправка уведомлений по расписанию - работает
async def schedule_notifications():
    while True:
        await asyncio.sleep(10)  # Проверяем каждые 10 секунд

        # Получаем текущую дату и время
        current_datetime = time.strftime('%Y-%m-%d %H:%M:%S')

        # Получаем задачи, у которых дата и время совпадают с текущим моментом
        tasks_to_notify = get_tasks_to_notify(current_datetime)

        # Отправляем уведомления
        for task in tasks_to_notify:
            user_id = task.task_user_id
            task_name = task.task_name
            notification_message = (f'Напоминание🚨️\n'
                                    f'Вам нужно выполнить задачу <b>«{task_name}»</b>❗')

            await send_notification(user_id, notification_message)
            # Помечаем задачу как уведомленную, чтобы не отправлять ее снова
            mark_task_as_notified(task)


# Функция для пометки задачи как уведомленной
def mark_task_as_notified(task):
    session = Session()
    task.notification = 0
    session.add(task)
    session.commit()
    session.close()


# Функция для проверки существования пользователя в базе данных
def user_exists(user_id):
    session = Session()
    user = session.query(User).filter_by(user_id=user_id).first()
    session.close()
    return user is not None


# Функция для сохранения пользователя в базе данных
def save_user(user_id, first_name):
    session = Session()
    new_user = User(user_id=user_id, user_name=first_name)
    session.add(new_user)
    session.commit()
    session.close()


async def main():
    asyncio.create_task(schedule_notifications())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())


