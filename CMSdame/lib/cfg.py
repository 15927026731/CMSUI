CMS_web = "http://127.0.0.1:8080"#访问地址

CMS_system = str(CMS_web)+"/admin"#首页地址

#登录接口缺省值
name_data = "wudehao"
password_data = "ZJqr@2022"



import pymysql

#创建连接对象
conn = pymysql.connect(
    host='127.0.0.1',    # 本机就写：localhost
    port=3306,                 # 要连接到的数据库端口号，MySQL是3306
    user='root',                # 数据库的用户名
    password='root',            # 数据库的密码
    database='empirecms',      # 要操作的数据库
    charset='utf8'             # 码表
)

#创建一个游标
cursor = conn.cursor()
# 4.执行SQL语句，获取结果集---假如需求是：查询order表中所有的订单信息
sql = 'select * from phome_enewsmember order by userid  desc;'  #phome_ecms_news是要操作的数据库中的表名
cursor.execute(sql)#返回数据库表的行数 执行语句后回缓存到内存，后续使用cursor.fet进行操作


number = (cursor.fetchone())
print((number[2]))

# print(cursor.fetchone())#输出一条,每执行一次，则减少一条内存数据
# print(cursor.fetchmany(2))#输出指定条数数据
# print(cursor.fetchall())#全部输出



# for data in cursor.fetchall():
#     print(data)
