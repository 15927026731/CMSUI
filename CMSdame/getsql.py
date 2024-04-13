import pymysql
from cfg import *

class SQL :

    def find(self,findsql):#输入输入sql语句进行查询

        #连接数据库，通过cfg的数据量字典填入
        # cmd = pymysql.connect(
        #     host=str(mysqldata["host"]),
        #     port=int(mysqldata["port"]),
        #     user=str(mysqldata["user"]),
        #     password=str(mysqldata["password"]),
        #     database=str(mysqldata["database"]),
        #     charset="utf-8"
        #     )


        cmd = pymysql.connect(
            host='127.0.0.1',  # 本机就写：localhost
            port=3306,  # 要连接到的数据库端口号，MySQL是3306
            user='root',  # 数据库的用户名
            password='root',  # 数据库的密码
            database='empirecms',  # 要操作的数据库
            charset='utf8'  # 码表
        )
        con = cmd.cursor() #建立光标
        con.execute(str(findsql),)#执行sql语句
        findend = con.fetchall()#返回所有列数据

        con.close()#关闭数据库
        return findend

if __name__ == "__main__":
    sqldata = (SQL().find("select username from phome_enewsmember order by userid;"))
    for data in sqldata:
        print(data[0])


