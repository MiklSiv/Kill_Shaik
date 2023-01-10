import sqlite3 as sql

conn = sql.connect('example.db')
cursor = conn.cursor()
#cursor.execute('''CREATE TABLE to_com (date text)''')
#cursor.execute('''CREATE TABLE from_com (date text)''')

cursor.execute(f"INSERT INTO to_com VALUES('888')")
conn.commit()
conn.close()