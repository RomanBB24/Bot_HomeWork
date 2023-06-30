from aiogram import executor
import logging
from config import dp
from handlers import commands, calback, extra, admin, fsm_mentor

commands.register_handlers_commands(dp)
calback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsm_mentor.register_handlers_fsm_mentor(dp)
extra.register_handlers_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)