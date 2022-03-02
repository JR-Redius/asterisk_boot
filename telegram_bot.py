from aiogram import Bot, Dispatcher, types, executor

# from main import getSearch
from botMainFunctions import getSearchNumber

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
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(*buttons)
    return keyboard


def getNewString(dict_user):
    if dict_user['ipaddr'] is None:
        dict_user['ipaddr'] = ''
    return ("Номер телефона = " + dict_user['name'] + "\nФИО = " + dict_user['fullname'] + "\nПароль = " + dict_user[
        'secret'] + "\nIP Адресс = " + dict_user['ipaddr'] + "\n контекст = " + dict_user['context'])


@dp.message_handler()
async def echo_message(msg: types.Message):
    dict_user = getSearchNumber(str(msg.text))
    if type(dict_user) == list:
        for id_user in dict_user:
            if type(id_user) == dict:
                await msg.answer(getNewString(id_user), reply_markup=get_keyboard_user())
            else:
                print(type(id_user))
    elif type(dict_user) == dict:
        await msg.answer(getNewString(dict_user), reply_markup=get_keyboard_user())
    else:
        await msg.answer('Нет такого пользователя')
    # await msg.answer(getDictAnswer(dict_user),reply_markup=get_keyboard_user())
    # await msg.answer("номер телефона = " + dict_user['name'] + "\nИмя пользователя = " + dict_user['fullname'] +
    # "\nIp адресс = " +dict_user['ipaddr'] + "\nгруппа дозвона = " + dict_user['context'],
    # reply_markup=get_keyboard_user())


@dp.message_handler(commands="test")
async def getTest(msg: types.message):
    await msg.answer("test </br>", )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
