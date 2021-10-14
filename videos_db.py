import mysql.connector

mydb = mysql.connector.connect(
	host='localhost',
	user='root',
	passwd = 'password',
	auth_plugin='mysql_native_password',
	database= 'videos')

my_cursor = mydb.cursor()

#my_cursor.execute('CREATE DATABASE videos')

#my_cursor.execute('SHOW DATABASES')

#my_cursor.execute('SHOW TABLES')

#my_cursor.execute('DESCRIBE videos')

query = "SELECT * FROM videos"

#iserir = 'INSERT INTO videos (titulo, url, tipo, data) VALUES (%s, %s, %s, %(data)s)'

#delete = "TRUNCATE TABLE videos"

#my_cursor.execute(delete)

my_cursor.execute(query)

for db in my_cursor:
	print(db)
