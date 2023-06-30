from aiogram import types, Dispatcher
from config import bot


async def echo_text(message: types.Message) -> None:
    bad_words = ['xeon', 'radeon', 'Кодер']
    for word in bad_words:
        if word in message.text.lower().replace(" ", ""):
            await message.delete()
            await message.answer(
                f"плохие слова запрещены @{message.from_user.username}\n"
                f"сама такая {word}"
            )

    if message.text.startswith('.'):
        await message.pin()
    if message.text == "dice":  # 🎲🎯🎰🎳🏀⚽️
        a = await message.answer_dice()


async def echo_sticker(message: types.Message) -> None:
    await bot.send_sticker(message.chat.id, message.sticker.file_id)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo_text, content_types=['text'])
    dp.register_message_handler(echo_sticker, content_types=['sticker'])
