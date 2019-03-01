import pymysql
class DoMysql:
    #完成与sql数据库的交互
    def __init__(self):###实例化对象的时候就建立连接
    #def connect(self):
        host="test.lemonban.com"
        user="test"
        password="test"
        port=3306

        self.mysql=pymysql.connect(host=host,user=user,password=password,port=3306)

        #self.cursor = self.mysql.cursor()
        self.cursor=self.mysql.cursor(pymysql.cursors.DictCursor)###设置返回字典游标
    def fetch_one(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchone()
    def fetch_all(self,sql):
        self.cursor.executee(sql)
        return self.cursor.fetchall()
    def close(self):
        self.cursor.close()##关闭游标，查询
        self.mysql.close()#关闭链接
if __name__ == '__main__':
    mysql=DoMysql()###实例化，建立连接
    # mysql.connect()
    result=mysql.fetch_one('select max(mobilephone) from future.member')##输入查询语句
    print(result)
    mysql.close()