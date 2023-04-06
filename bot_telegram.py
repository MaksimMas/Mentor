from aiogram import Bot, types
from aiogram.dispatcher import  Dispatcher
from aiogram.utils import executor

import os

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot)
#Клиентская часть
@dp.message_handler(commands=[ ])

#Админка


#Общая часть
@dp.message_handler()
async def echo_send(message : types.Message):
    await message.answer(message.text)
    #await message.reply(message.text)
    #await bot.send_message()


executor.start_polling(dp,skip_updates=True)