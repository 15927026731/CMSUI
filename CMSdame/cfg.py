CMS_web = "http://127.0.0.1:8080"

CMS_system = str(CMS_web)+"/admin"


name_data = "wudehao"
password_data = "ZJqr@2022"

mysqldata = {
    "host":'127.0.0.1',# 本机就写：localhost
    "port":3306,# 要连接到的数据库端口号，MySQL是3306
    "user":"root",# 数据库的用户名
    "password":'root',# 数据库的密码
    "database":'empirecms',# 要操作的数据库
    "charset":'utf8'# 码表
}