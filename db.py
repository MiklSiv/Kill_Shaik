import  sqlite3 as sq



with sq.connect('primer.db') as con:
   cur = con.cursor()

   w = cur.execute(""" SELECT * FROM data
   """)

   q = cur.fetchall()
   print (q)

