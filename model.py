import mysql.connector as mysql
from mysql.connector import Error

try:
    conn = mysql.connect(host='localhost', user='root', password='root')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE bescom")
        print("Connection Successfull !!")
except Error as e:
    if e.errno == 1007:
        cursor.execute("DROP DATABASE bescom")
        print("Database Successfully dropped :(")