import requests
import sys
sys.path.append('C:/Users/24202/PycharmProjects/CMSUI/CMSdame')
from .cfg import *
sys.path.append('C:/Users/24202/PycharmProjects/CMSUI/CMSdame')
sys.path.append('C:\\Users\\24202\\PycharmProjects\\CMSUI\\CMSdame\\lib')
sys.path.append('C:\\Users\\24202\\PycharmProjects\\CMSUI')
sys.path.append('C:\\Program Files\\Python311\\python311.zip')
sys.path.append('C:\\Program Files\\Python311\\Lib')
sys.path.append('C:\\Program Files\\Python311\\DLLs')
sys.path.append('C:\\Users\\24202\\AppData\\Roaming\\Python\\Python311\\site-packages')
sys.path.append('C:\\Program Files\\Python311')
sys.path.append('C:\\Program Files\\Python311\\Lib\\site-packages')
sys.path.append('D:\\')


class REQUEST:

    def login(self):#登录结果
        try:
            url = "http://127.0.0.1:8080/e/member/doaction.php"
            data = {"enews": "login",
                    "ecmsfrom": "9",
                    "username": name_data,
                    "password": password_data,
                    "Submit": "登录"}
            params = {}
            login = requests.post(url, data=data, params=params)
            return login
        except Exception as e:
            print("登录异常")

    def logincookie(self,):#登录后获取cookie
        cookie = str((REQUEST().login()).cookies)
        cookie1 = str(cookie[43:50])
        cookie2 = str(cookie[90:91])
        cookie3 = str(cookie[132:133])
        cookie4 = str(cookie[170:190])
        cookie5 = str(cookie[228:260])
        name = str(cookie[27:34])
        cookie = {
            "cookie": str(name) + "username=" + str(cookie1) + "; " + str(name) + "userid=" + str(cookie2) + "; " + str(
                name) + "groupid="
                      + str(cookie3) + "; " + str(name) + "rnd=" + str(cookie4) + "; " + str(name) + "auth=" + str(
                cookie5)}
        return cookie

    def add(self,phone,title):#添加新闻接口
        url = "http://127.0.0.1:8080/e/DoInfo/ecms.php"
        data = {"enews": "MAddInfo", "classid": "12", "id": "0", "filepass": "1701246164", "mid": "80", "title": str(title),
                "smalltext": "测试内容测试内容"
            , "myarea": "东城区", "email": "524979780@qq.com", "mycontact": int(phone), "address": "杭州西湖",
                "addnews": "提交"}

        headers = REQUEST().logincookie()
        add = requests.post(url, data, headers)
        return add

    def find(self,findname):#查询新闻接口
        url = "http://127.0.0.1:8080/e/DoInfo/ListInfo.php"
        parame = {"keyboard": str(findname), "show": "0", "Submit2": "搜索", "sear": "1", "mid": "1", "ecmscheck": "0"}
        headers = REQUEST().logincookie()
        find = requests.get(url=url, params=parame, headers=headers)
        return find


if __name__ == "__main__":
    print(REQUEST().login().cookies)
