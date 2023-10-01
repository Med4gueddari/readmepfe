import mysql.connector

from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='sco_db',
                                         user='root',
                                         password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("SELECT Code_CARINE FROM magasin")
        records = cursor.fetchall()
        for row in records:
            print(row)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
