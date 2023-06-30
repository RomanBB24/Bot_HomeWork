from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMMentor(StatesGroup):
    mentor_name = State()
    mentor_age = State()
    mentor_direction = State()
    mentor_group = State()
    mentor_submit = State()

async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMMentor.mentor_name.set()
        await message.answer('Напишите ваше Имя')
    else:
        await message.reply('Не писать в группе а писать в личку')

async def load_name(message: types.Message, state: FSMContext):
     async with state.proxy() as data:
         data['name'] = message.text
     await FSMMentor.next()
     await message.answer('Сколько лет?')

async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числа!")

    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await FSMMentor.next()
    await message.answer('Какое направление?')

async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMMentor.next()
    await message.answer('Какая группа?')


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
    await FSMMentor.next()
    await message.answer(f'Информация о менторе\n'
                         f'имя ментора - {data["name"]}\n'
                         f'Возраст ментора - {data["age"]}\n'
                         f'Направление ментора - {data["direction"]}\n'
                         f'Группа ментора - {data["group"]}\n')
    await message.answer('Всё правильно? да/нет')
async def load_submit(message: types.Message, state: FSMContext):
    if message.text == 'да':
        await message.answer('Записал в базу')
        await state.finish()

    elif message.text == 'нет':
        await message.answer('ok')
        await state.finish()


def register_handlers_fsm_mentor(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMMentor.mentor_name)
    dp.register_message_handler(load_age, state=FSMMentor.mentor_age)
    dp.register_message_handler(load_direction, state=FSMMentor.mentor_direction)
    dp.register_message_handler(load_group, state=FSMMentor.mentor_group)
    dp.register_message_handler(load_submit, state=FSMMentor.mentor_submit)

