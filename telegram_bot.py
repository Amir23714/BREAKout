from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token='6234279060:AAFx1KgWvVNg1prHpQfvlS203nZaOt4IH5U')
dp = Dispatcher(bot)

## Keyboard
button_authorization = KeyboardButton('Log in 🤳')
button_client_work = KeyboardButton('Add an account to work 🚜')
button_statistics = KeyboardButton('Statistics 💻')

first_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_client_work).add(button_statistics)
first_kb_no_admins = ReplyKeyboardMarkup(resize_keyboard=True).add(button_authorization)

## Admins
admins = [682751445, 1992272849]


@dp.message_handler(commands=['start'])
async def alarm(message: types.Message):
    if (message.from_user.id in admins):
        await message.answer(f"Greetings, {message.from_user.username}", reply_markup=first_kb)
    else:
        await message.answer(f"Greetings, {message.from_user.username}, log in!", reply_markup=first_kb_no_admins)


@dp.message_handler(text=['Add an account to work 🚜'])
async def process_client_work_command(message: types.Message):
    await message.reply(f"Add account section.\n"
                        f"\n"
                        f"Enter API_KEY and SECRET_KEY with a space, which is tied to the work account:")


@dp.message_handler()
async def get_phone(message: types.Message):
    phone = message.text
    await message.reply(f"Your API_KEY: {message.text.split()[0]}\nSECRET_KEY: {message.text.split()[1]}\n")


if __name__ == '__main__':
    executor.start_polling(dp)
