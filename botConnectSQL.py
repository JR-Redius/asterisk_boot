import pymysql.cursors


def getConnectionSQL():
    connection = pymysql.connect(
        host='127.0.0.1',
        user='jred',
        password='wudiw01e',
        db='asterisk',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
