from aiogram import Bot, Dispatcher, types, executor
from main import getSearch
from botMainFunctions import getSearchNumber
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

bot = Bot(token="1966342656:AAEikQMfVsuHureW2I8fJhPJtx4zG64rVvc")
dp = Dispatcher(bot)

mes_error_4 = 'Длинна корпоративного номера составляет 4 цифры'


@dp.message_handler()
async def echo_message(msg: types.Message):
    print('echo')



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
