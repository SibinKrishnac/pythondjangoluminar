import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Shibin@123',
    auth_plugin='mysql_native_password',
    database='pythondecember'
)
cursor=db.cursor()
sql='create table movie(id int,name varchar(50),year int,rating int)'
cursor.execute(sql)
print("table created")
db.close()