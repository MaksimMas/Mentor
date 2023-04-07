from aiogram import types, Dispatcher
from create_bot import dp, bot

#@dp.message_handler(commands=['start','help'])
async def comands_start(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет!Это бот для поиска менторов")

def register_handlers_client(dp : Dispatcher) :
    dp.register_message_handler(comands_start, commands=['start','help'])