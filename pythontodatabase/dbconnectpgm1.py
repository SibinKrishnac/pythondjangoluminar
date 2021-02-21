import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Shibin@123',
    auth_plugin='mysql_native_password'

)
cursor=db.cursor()
sql='select version()'
cursor.execute(sql)
data=cursor.fetchone()
print(data)
db.close()