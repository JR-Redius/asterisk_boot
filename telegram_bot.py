from aiogram import Bot, Dispatcher, types, executor
#from main import getSearch
from botMainFunctions import getSearchNumber
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

bot = Bot(token="1966342656:AAEikQMfVsuHureW2I8fJhPJtx4zG64rVvc")
dp = Dispatcher(bot)


# mes_error_4 = 'Длинна корпоративного номера составляет 4 цифры'


def get_keyboard_user():
    # Генерация клавиатуры.
    buttons = [
        types.InlineKeyboardButton(text="Изменить пароль", callback_data="num_decr"),
        types.InlineKeyboardButton(text="Изменить имя", callback_data="num_incr"),
        types.InlineKeyboardButton(text="Изменить группу", callback_data="num_finish"),
        types.InlineKeyboardButton(text="Показать историю звонков", callback_data="num_cdr")
    ]
    # Благодаря row_width=2, в первом ряду будет две кнопки, а оставшаяся одна
    # уйдёт на следующую строку
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


@dp.message_handler()
async def echo_message(msg: types.Message):
    dict_user = getSearchNumber(str(msg.text))
    await msg.answer(
        "номер телефона = " + dict_user['name'] + "\nИмя пользователя = " + dict_user['fullname'] + "\nIp адресс = " +
        dict_user['ipaddr']+"\nгруппа дозвона = "+dict_user['context'], reply_markup=get_keyboard_user())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
