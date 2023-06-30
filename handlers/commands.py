from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
from .keyboards import start_markup



async def start_command(message: types.Message) -> None:
    await bot.send_message(message.chat.id,
                           f"Здравствуй отец! {message.from_user.full_name}",
                           reply_markup=start_markup)

async def mem_handler(message: types.Message) -> None:
    await message.answer_photo(
        photo="https://fuzeservers.ru/wp-content/uploads/d/c/4/dc4383acd028957f884d444b41bec874.jpeg"
    )

    photo = open("media/images/mem.jpg", "rb")
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo
    )


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(mem_handler, Text(equals="мем", ignore_case=True))