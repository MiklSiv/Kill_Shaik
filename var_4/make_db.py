import sqlite3
import time

conn = sqlite3.connect('data_base.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE arduino (time real, in_com text, out_com text)''')
#for i in range(10):
    #cursor.execute(f'''INSERT INTO arduino(id, time, date) VALUES ({i}, {time.time()}, 'text');''')

#cursor.execute(f'''UPDATE arduino SET time = {time.time()}, date = "NEW" WHERE id = 0''')

conn.commit()
conn.close()



# код из интернета
def update_sqlite_table():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_update_query = """Update sqlitedb_developers set salary = 10000 where id = 4"""
        cursor.execute(sql_update_query)
        sqlite_connection.commit()
        print("Запись успешно обновлена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
