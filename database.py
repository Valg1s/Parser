from os import close
import sqlite3
from sqlite3.dbapi2 import connect

def connect_db():
    conn = sqlite3.connect('parse.db')
    cur = conn.cursor()
    return conn, cur


def close_db(conn, cur):
    conn.commit()
    cur.close()


def add_parse_files(title, cost_dollar, cost_UAH, region):
    conn, cur = connect_db()
    create_table_query = '''CREATE TABLE IF NOT EXISTS cars(
        car_id INT PRIMARY KEY,
        title TEXT,
        cost_dollar TEXT,
        cost_UAH TEXT,
        region TEXT);'''
    cur.execute(create_table_query)
    conn.commit()
    check_id_query = '''SELECT car_id FROM cars;'''
    cur.execute(check_id_query)
    all_car_id_in_table = cur.fetchall()
    print(all_car_id_in_table)
    if len(all_car_id_in_table) == 0:
        new_id = 0
    else:
        new_id = all_car_id_in_table[-1][-1] + 1
    add_data_query = f'''INSERT INTO cars (car_id, title, cost_dollar, cost_UAH, region) VALUES({new_id}, '{title}', '{cost_dollar}', '{cost_UAH}', '{region}');'''
    cur.execute(add_data_query)
    print('end')
    close_db(conn, cur)

add_parse_files()