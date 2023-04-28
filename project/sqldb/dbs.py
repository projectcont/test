import sqlite3
import sys
import paths_ as loc
print(sys.path)
import os
from typing import List, Dict, Union, Optional


def user_get(email: str):
    '''
    функция извлекает параметры user (с данным email), из базу данных database.sqlite
    :param user:
    :return:
    '''
    root=loc.path()
    filepath=os.path.join(root, 'sqldb', 'database.sqlite')
    con = sqlite3.connect(filepath, timeout=5.0, detect_types=0, isolation_level='DEFERRED', check_same_thread=True,
                          factory=sqlite3.Connection, cached_statements=128, uri=False)
    cursor = con.cursor()
    query = f"SELECT * FROM user WHERE email='{email}' "
    cursor.execute(query)
    userlist =cursor.fetchall()
    con.close()
    return len(userlist), userlist


def user_add(user):
    '''
    функция добавляет  user, его параметры в  базу данных database.sqlite
    user - экземпляр класса  User
    :param user:
    :return:
    '''

    getted_lendth, getted_users = user_get(user.email)
    # если email уже есть в БД то возникает исключение
    if getted_lendth>0:
        raise Exception('ПОЛЬЗОВАТЕЛЬ УЖЕ ЕСТЬ В БАЗЕ ДАННЫХ')
        return 0


    else:
        root = loc.path()
        filepath = os.path.join(root, 'sqldb', 'database.sqlite')
        con = sqlite3.connect(filepath, timeout=5.0, detect_types=0, isolation_level='DEFERRED', check_same_thread=True,
                              factory=sqlite3.Connection, cached_statements=128, uri=False)
        cursor = con.cursor()
        query=f"INSERT INTO user (name, email,score) VALUES ('{user.name}', '{user.email}', '{user.score}')"
        cursor.execute(query)
        con.commit()
        con.close()
        return 1

