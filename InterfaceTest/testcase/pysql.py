import pymysql
#1建立连接：数据库的链接信息 ：  mysql对应的默认端口：3306
host="test.lemonban.com"
user="test"
password="test"
port=3306

mysql=pymysql.connect(host=host,user=user,password=password,port=3306,charset='utf-8')##建立连接，保存
#2新建一个查询页面
cursor=mysql.cursor()##游标对象，记录
#3编写sql
sql=' select max(mobilephone) from future.member '
#sql='select * from future.loan'
#4执行sql
cursor.execute(sql)
#5查看执行结果
result=cursor.fetchone()##获取查询结果集里面最近的一条数据返回
##results=cursor.fetchall()  ##返回N条数据(获取全部结果集)  存放在元组里（（），（），（））
print(type(result),result)

#6关闭查询
cursor.close()
#7关闭数据库链接
mysql.close()