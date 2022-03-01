from botMainFunctions import getSearchNumber, getListUser, getCreateNewUser, getDeleteUser


#query = input('1 - search, 2-create, 3-delete: ')

# Создание нового пользователя


def getCreate():
    user_dict = {}
    context = ['from_out_kdk',
               'from_out_buh',
               'from_out_feo',
               'from_out_exp',
               'from_out_ok',
               'from_out_jur',
               'from_out_go',
               'from_out_pto',
               'from_out_energetik',
               'from_out_meh',
               'from_out_dis',
               'from_out_snab',
               'from_out_lab']

    user_number = input('Введите номер телефона: ')
    user_fullname = input('Введите ФИО: ')
    user_secret = input('Введите пароль пользователя: ')
    user_context = input('Ввыберите контекст: ')

    if len(user_number) == 4:
        user_dict['bot_new_name'] = user_number
    user_dict['bot_new_fullname'] = user_fullname
    user_dict['bot_new_secret'] = user_secret
    if user_context in context:
        user_dict['bot_new_context'] = user_context
    else:
        print('неверное значение')

    print(getCreateNewUser(user_dict))


#getCreate()
# Проверка выходных данных
def getSearch(numberX):
    result = getSearchNumber(numberX)
    if type(result) == list:
        for i in result:
            print('Номер = ', i['name'])
            print('Имя = ', i['fullname'])
            print('Пароль = ', i['secret'])
            print('Контекст = ', i['context'])
            print('IP адрес = ', i['ipaddr'])
    elif type(result) == dict:
        print('Номер = ', result['name'])
        print('Имя = ', result['fullname'])
        print('Пароль = ', result['secret'])
        print('Контекст = ', result['context'])
        print('IP адрес = ', result['ipaddr'])
    else:
        print(result)
    return result

# Удаление пользователя
def getDelete():
    number = input('Введите номер который необходимо удалить: ')
    if len(number) == 4:
        getDeleteUser(number)

# if query == '1':
#     getSearch()
# elif query == '2':
#     getCreate()
# elif query == '3':
#     getDelete()
# else:
#     print('Неверный выбор')