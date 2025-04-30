from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.filters import Command

import asyncio
from itertools import islice

TOKEN = "7801302292:AAHuoFG3Uy1MT9HJ8k3eP17pO39Fo_KvMgI"

bot = Bot(TOKEN)

dp = Dispatcher()

email = "example@gmail.ru"
number_phone = "+79065099999"

start_line = 3

user_states = {}

@dp.message(Command("start"))
async def start_handler(message: Message):
    user_id = message.from_user.id
    user_states[user_id] = False
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
        InlineKeyboardButton(text = "Наш сайт", url="https://милкагросервис.рф/"),
        InlineKeyboardButton(text="Github Разраба", url="https://github.com/GL1KK")
        ]
        ])
    await message.answer(f"Здравствуйте! Что Вас интересует?", reply_markup=keyboard)



@dp.message(Command("contacts"))
async def contacts_handler(message: Message):
    await message.answer(f"Вот наши контакты:\nemail: {email}\n номер телефона: {number_phone}")

@dp.message(Command("catalog"))
async def catalog_handler(message: Message):
        user_id = message.from_user.id
        user_states[user_id] = False
        buttons = [
             [KeyboardButton(text="Остановить")]
        ]
        keyboard = ReplyKeyboardMarkup(
             keyboard=buttons,
             resize_keyboard=True,
             one_time_keyboard=True,
             input_field_placeholder="Нажмите чтобы остановить"
        )
        with open("info.txt") as file:
            for title in file:
                link = next(file, ' ')
                await message.answer(f"Имя: {title}\nСсылка: {link}", reply_markup=keyboard)
                if user_states[user_id] == True:
                    await message.answer("Останавливаю....", reply_markup=ReplyKeyboardRemove())
                    break
                await asyncio.sleep(2)
        await message.answer("Работа завершена", reply_markup=ReplyKeyboardRemove())

@dp.message(lambda message: message.text == "Остановить")
async def stop_handler(message: Message):
    user_id = message.from_user.id
    if user_id in user_states:
        user_states[user_id] = True
        await message.answer("Останавливаю....", reply_markup=ReplyKeyboardRemove())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())