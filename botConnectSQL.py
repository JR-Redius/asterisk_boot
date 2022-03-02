import pymysql.cursors


def getConnectionSQL():
    connection = pymysql.connect(
        host='127.0.0.1',
        user='jred',
        # user='root',
        password='wudiw01e',
        # password='{eq Euflftim @',
        db='asterisk',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
