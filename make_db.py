import sqlite3 as sql

conn = sql.connect('example.db')
cursor = conn.cursor()
#cursor.execute('''CREATE TABLE to_com
             #(date text)''')
#cursor.execute('''CREATE TABLE from_com
             #(date text)''')



cursor.execute("UPDATE to_com SET date='retw'")

cursor.execute('SELECT * FROM to_com')
Q = cursor.fetchone()
print(Q[0])
conn.commit()
conn.close()