import sqlite3 as sql

conn = sql.connect('data_base_KillSheik.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE arduino (time real, date text)''')
#cursor.execute('''CREATE TABLE from_com (date text)''')

#cursor.execute(f"INSERT INTO to_com VALUES('888')")
conn.commit()
conn.close()