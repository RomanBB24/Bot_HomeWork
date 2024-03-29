from aiogram import types, Dispatcher
from config import bot, ADMINs


async def ban(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMINs:
            await message.answer("я на тебя не работаю")
        elif not message.reply_to_message:
            await message.answer("это должно быть ответом на сообщение!")
        else:
            await message.delete()
            await bot.kick_chat_member(
                message.chat.id,
                message.reply_to_message.from_user.id
            )
            await message.answer(
                f"{message.from_user.first_name} забанил "
                f"{message.reply_to_message.from_user.full_name}"
            )
    else:
        await message.answer("Не здесь")


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')