import os
import mysql.connector
import time

print("Start Script")
try:
  time.sleep(80)   

  password = os.environ['DB_PASSWORD']

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="user"
  )

  mycursor = mydb.cursor()

  mycursor.execute("DROP TABLE utente;")

  mycursor.execute("CREATE TABLE utente (id bigint NOT NULL, is_admin bit NOT NULL, mail varchar(255) NOT NULL, password varchar(255) NOT NULL, PRIMARY KEY (id), UNIQUE (mail));")

  mycursor.execute('INSERT INTO utente VALUES (1, 1, "admin", "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918");')

  mydb.commit()

except Exception as e: print(e)

print("RIP")

while True:
    time.sleep(4000000)