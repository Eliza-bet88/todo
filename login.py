import psycopg
def get_connection():
    return psycopg.connect("dbname=postgres user=postgres password=151731 host=localhost")

import hashlib

email = input("email: ")
password = input("password:")

conn = get_connection()
cur = conn.cursor()

sql = "SELECT * FROM log WHERE email = %s AND password = %s;"
cur.execute(sql, (email,password))
login = cur.fetchall()

if login:
    print ("Logged in")
else:
    print ("Login failed")

cur.close()
conn.close()




# email = input("email: ")
# password = input("password:")

# conn = get_connection()
# cur = conn.cursor()

# sql = "SELECT * FROM log WHERE email = '" + email + "' AND password = '" + password + "';"
# cur.execute(sql)
# login = cur.fetchall()
# print(login)
# if login:
#     print ("Logged in")
# else:
#     print ("Login failed")

# cur.close()
# conn.close()