# import pymysql
# # mysql的连接 和创建spider数据库
# db=pymysql.connect(host='localhost',user='root',password='',port=3306)
# cursor=db.cursor()
# cursor.execute('SELECT VERSION()')
# data=cursor.fetchone()
# print('Database version:',data)
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET  utf8")
# db.close()
#
#
# # 创建表
# import pymysql
#
# db=pymysql.connect(host='localhost',user='root',password='',port=3306,db='spiders')
# cursor=db.cursor()
# sql='CREATE TABLE IF NOT EXISTS students(id VARCHAR(255) NOT NULL,name VARCHAR(255)NOT NULL ,age INT NOT NULL,PRIMARY KEY(id))'
# cursor.execute(sql)
# db.close()

# 插入数据
import pymysql
id='20120001'
user='Bob'
age=20
db=pymysql.connect(host='localhost',user='root',password='',port=3306,db='spiders')
cursor=db.cursor()
sql='INSERT INTO students(id,name,age)VALUES (%s,%s,%s)'
try:
    cursor.execute(sql,(id,user,age))
    db.commit()
except:
    db.rollback()
db.close()





