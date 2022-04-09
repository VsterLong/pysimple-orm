import pymysql
import orm
from typing import List
import orm.sql_config as config

from utils.convert import dict_arr_2_class


def do_select_all(sql, class_name, param=None):
    with pymysql.connect(host=config._host, port=config._port, user=config._user, password=config._passwd, database=config._database, cursorclass=pymysql.cursors.DictCursor) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, param)
            data = cursor.fetchall()
    data = dict_arr_2_class(data, class_name)
    return data


def do_select_many(sql, class_name, offset, size):
    with pymysql.connect(host=config._host, port=config._port, user=config._user, password=config._passwd, database=config._database, cursorclass=pymysql.cursors.DictCursor) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql+" limit {}, {}".format(offset, size))
            data = cursor.fetchmany(size)

    data = dict_arr_2_class(data, class_name)
    return data


def do_execute(sql, param=None) -> int:
    with pymysql.connect(host=config._host, port=config._port, user=config._user, password=config._passwd, database=config._database, cursorclass=pymysql.cursors.DictCursor) as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(sql, param)
                conn.commit()
                return conn.affected_rows()
            except Exception as e:
                conn.rollback()
                print(e)
                return -1
