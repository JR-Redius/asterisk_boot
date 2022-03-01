from botConnectSQL import getConnectionSQL
from pymysql import cursors
import pymysql


def getListUser(querySQL):
    list_user = []
    sql_query = querySQL
    bot_connection = getConnectionSQL()
    user = bot_connection.cursor()
    user.execute(sql_query)
    for id in user:
        list_user.append(id)
    return list_user


def getSearchNumber(bot_search_number_user):
    temp_true_list_user = []
    if bot_search_number_user.isdigit():
        if len(bot_search_number_user) == 4:
            sql = 'SELECT name, fullname, secret, context, ipaddr FROM sippeers WHERE name = ' + str(
                bot_search_number_user) + ';'
            list_user = getListUser(sql)
            for id in list_user:
                if id['name'] == bot_search_number_user:
                    temp_true_list_user = id
            return temp_true_list_user
        else:
            return 'Неверный формат номера, номер состоит из 4 цифр. Попробуйте еще раз'
    else:
        temp_str = str(bot_search_number_user.replace(' ', ''))
        if temp_str.isalpha():
            sql = 'SELECT name, fullname, secret, context, ipaddr FROM sippeers WHERE fullname LIKE "%' + str(bot_search_number_user) + '%";'
            list_user = getListUser(sql)
            if not list_user:
                return 'Такого пользователя не зарегистрированно'
            else:
                return list_user
        else:
            return 'Такого пользователя не зарегистрированно'


def getEditUserInfo(bot_dict_edit_info):
    print('Редактирование информации')
    # sql = 'UPDATE sippeers TO '+str(botArgument)+'='+str(botValue)+' WHERE name='+str(phoneNumber)+';'
    if 'bot_edit_fullname' in bot_dict_edit_info:
        print('изменить имя пользователя')
    elif 'bot_edit_secret' in bot_dict_edit_info:
        print('Изменить пароль пользователя')
    elif 'bot_edit_context' in bot_dict_edit_info:
        print('Изменить контекст')
    else:
        print('Неверный параметр')


def getCreateNewUser(bot_dict_create_user):
    sql = "INSERT INTO sippeers (name, fullname, host, type, context, secret, nat, disallow, allow, `call-limit`) " \
          "VALUES ('" + str(bot_dict_create_user['bot_new_name']) + "', '" + str(
        bot_dict_create_user['bot_new_fullname']) + "', 'dynamic', 'friend', '" + str(
        bot_dict_create_user['bot_new_context']) + "', '" + str(
        bot_dict_create_user['bot_new_secret']) + "', 'no', 'all', 'alaw,ulaw', '1'); "
    bot_connection = getConnectionSQL()
    user_create = bot_connection.cursor()
    user_create.execute(sql)
    bot_connection.commit()
    return 'Пользователь создан'


def getDeleteUser(bot_numder_delete_user):
    sql = 'DELETE FROM sippeers WHERE name=' + str(bot_numder_delete_user) + ';'

    bot_connection = getConnectionSQL()
    user_delete = bot_connection.cursor()
    user_delete.execute(sql)
    bot_connection.commit()
    return 'Пользователь удален'
