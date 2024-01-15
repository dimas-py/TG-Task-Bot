import asyncio
import requests
import time
from datetime import time
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
from aiogram.types import Message

from bd_config import User, Session, Task
from keyboard import create_main_keyboard

BOT_TOKEN = "6481132072:AAEcFRg5bH9eEgzUXHMdyzOkdTHClDAqrfw"
FLASK_URL = 'https://16ba-94-231-133-134.ngrok-free.app'
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
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
