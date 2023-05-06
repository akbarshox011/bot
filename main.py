from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message


token = '6087227140:AAEcCa70bwtKyCpCzXZHC96s27Nruykaapo'

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: Message):
    chat_id = message.chat.id
    fullname = message.from_user.full_name
    await bot.send_message(chat_id, f'salom {fullname} openbudgetuzga xush kelibsiz openbudget')

@dp.message_handler(commands='openbudget')
async def telefon(message: Message):
    await message.reply('https://openbudget.uz/')




@dp.message_handler()
async def echo(message: Message):
    text = message.text
    await message.reply(text)

executor.start_polling(dp, skip_updates=True)
