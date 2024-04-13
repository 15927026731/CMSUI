import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from .lib.weblogin import webUI
from selenium.webdriver.common.action_chains import ActionChains
import sys
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
# from .lib.cfg import *

# wd = webdriver.Edge(service=Service(r"d:\msedgedriver.exe"))


def setup_module():
    print("\n 初始化")


# 执行总用例前的初始化

def steardowm_module():
    print("\n 清除")


# 执行总用例结束后的清除


class Test_001:

    @classmethod
    def setup_class(cls):
        print("class类执行的初始化开始")

    @classmethod
    def teardown_class(cls):
        print("class类执行结束的清除")

    def setup_method(self):
        print("\n方法的初始化开始")

    def teardown_method(self):
        print("\n方法的执行结束")


    @pytest.fixture  # 自定义创建用户初始化
    def creattest1(self):
        webUI.wd.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td/table/tbody/tr/td[1]/form/input[6]").click()
        for heand in webUI.wd.window_handles:
            webUI.wd.switch_to.window(heand)
            if "注册会员" in webUI.wd.title:
                break
        webUI.wd.find_element(By.NAME, "button").click()
        webUI.wd.find_element(By.XPATH, """//*[@id="password"]""").send_keys("ZJqr@@022")
        webUI.wd.find_element(By.XPATH, """//*[@id="repassword"]""").send_keys("ZJqr@@022")
        webUI.wd.find_element(By.XPATH, """//*[@id="email"]""").clear()
        webUI.wd.find_element(By.XPATH, """//*[@id="email"]""").send_keys("2420288461@qq.com")
        webUI.wd.find_element(By.XPATH, """//*[@id="username"]""").clear()
        webUI.wd.find_element(By.XPATH, """//*[@id="username"]""").send_keys("test1")
        webUI.wd.find_element(By.XPATH, "/html/body/table[4]/tbody/tr/td[2]/table/tbody/tr[9]/td[2]/input[1]").click()
        print("\n创建用户成功")
        for hand in webUI.wd.window_handles:
            webUI.wd.switch_to.window(hand)
            if "帝国网站管理系统 - Powered by EmpireCMS" in webUI.wd.title:
                break

    @pytest.fixture()
    def loginclean(self):#清除账号密码输入框内容
        try:
            webUI.wd.find_element(By.XPATH,"/html/body/table[1]/tbody/tr/td/table/tbody/tr/td[1]/form/input[3]").clear()
            webUI.wd.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td/table/tbody/tr/td[1]/form/input[4]").clear()
        except Exception as e:
            print("未知异常"+str(e))
        yield
        try:
            webUI.wd.find_element(By.XPATH,"/html/body/table[1]/tbody/tr/td/table/tbody/tr/td[1]/form/input[3]").clear()
            webUI.wd.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td/table/tbody/tr/td[1]/form/input[4]").clear()
        except Exception as e:
            print("未知异常"+str(e))

    @pytest.fixture()
    def singout(self):#退出清除操作

        yield
        try:
            webUI.wd.find_element(By.XPATH,"/html/body/table[1]/tbody/tr/td/table/tbody/tr/td[1]/a[6]").click()
            webUI.wd.switch_to.alert.accept()
            webUI.wd.find_element(By.XPATH,"/html/body/table/tbody/tr[2]/td/div/a").click()
        except Exception as e:
            print(e)

    def test_001(self,singout):  # 正确登录，调用自定义初始化fixture，自动执行初始化和结束清除
        webUI.login("test1", "ZJqr@@022")
        text = webUI.wd.find_element(By.XPATH, """/html/body/table/tbody/tr[2]/td/div/b""").text
        assert text == "登录成功!"

    @pytest.mark.parametrize("username,password,expectedalert",#数据驱动，
                             [("test1", "1234", "您的用户名或密码有误!"),
                              (None, None, "用户名和密码不能为空"),
                              ("test1", None, "用户名和密码不能为空"),
                              (None,"tZJqr@@022","用户名和密码不能为空")])


    def test_002(self,username,password,expectedalert,loginclean):  # 正确登录，调用自定义初始化fixture，自动执行初始化和结束清除，调用数据驱动
        webUI.login(username,password)
        text = webUI.wd.find_element(By.XPATH, """/html/body/table/tbody/tr[2]/td/div/b""").text
        assert text == expectedalert


    def test_003(self,singout):  # 登录成功按钮点击
        webUI.login("test1","ZJqr@@022")
        webUI.wd.find_element(By.XPATH,"/html/body/table/tbody/tr[2]/td/div/a").click()
        assert webUI.wd.title == "帝国网站管理系统 - Powered by EmpireCMS"


    @pytest.fixture()
    def backweb(self):
        yield
        webUI.findhand("帝国网站管理系统 - Powered by EmpireCMS")


    def test_004(self,backweb):  # 注册按钮点击
        webUI.register()
        for heand in webUI.wd.window_handles:
            webUI.wd.switch_to.window(heand)
            if "注册会员" in webUI.wd.title:
                break
        assert webUI.wd.title == "注册会员"


    @pytest.fixture()
    def registerclear(self):
        webUI.findhand("注册会员")
        try:
            webUI.wd.find_element(By.XPATH,"""//*[@id="username"]""").clear()
            webUI.wd.find_element(By.XPATH,"""//*[@id="password"]""").clear()
            webUI.wd.find_element(By.XPATH,"""//*[@id="repassword"]""").clear()
            webUI.wd.find_element(By.XPATH,"""//*[@id="email"]""").clear()
        except Exception as e:
            print(e)

    @pytest.mark.parametrize("name,password,repassword,email",
                             [("wdh", None, "ZJqr@2022", "wdh@qq.com"),
                              (None, "ZJqr@2022", "ZJqr@2022", "wdh@qq.com")])


    def test_005(self,name,password,repassword,email,backweb):  # 注册空输入用户
        webUI.register()
        webUI.registerclick()
        webUI.registerdata(name,password,repassword,email)
        assert "用户名，密码与邮箱不能为空" == webUI.wd.find_element(By.XPATH,"/html/body/table/tbody/tr[2]/td/div/b").text

    def test_006(self):  # 注册用户
        webUI.registerdata("wdh2","ZJqr@2022","ZJqr@2022","wdh@qq.com")
        test = webUI.wd.find_element(By.XPATH,"/html/body/table/tbody/tr[2]/td/div/b").text
        assert "注册成功" == test

    def test_002_001(self):  # 鼠标停留
        webUI.wd.get("http://127.0.0.1:8080")
        webUI.wd.find_element(By.XPATH, "/html/body/table[4]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/a[2]")
        ac = ActionChains(webUI.wd)  # 鼠标移动
        ac.move_to_element(
            webUI.wd.find_element(By.XPATH, "/html/body/table[4]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/a[2]")).perform()
        webUI.wd.get_screenshot_as_file("test_009.png")  # 截图保存
        assert 1 == 1

    def test_010(self):  # 弹窗确认
        wd = webdriver.Edge(service=Service(r"d:\msedgedriver.exe"))
        wd.get("https://cdn2.byhy.net/files/selenium/test4.html")
        wd.find_element(By.XPATH, """//*[@id="b1"]""").click()
        tips = str((wd.switch_to.alert.text))
        print(tips)
        assert tips == "现在开始和白月黑羽一起学Python!"

    def test_011(self):  # 点击弹窗
        wd = webdriver.Edge(service=Service(r"d:\msedgedriver.exe"))
        wd.get("https://cdn2.byhy.net/files/selenium/test4.html")
        wd.find_element(By.XPATH, """//*[@id="b1"]""").click()
        time.sleep(3)
        wd.switch_to.alert.accept()
        hand = str(wd.title)
        assert hand == "白月黑羽：web自动化 - 弹出对话框"

    def test_012(self):  # 确认弹窗
        wd = webdriver.Edge(service=Service(r"d:\msedgedriver.exe"))
        wd.get("https://cdn2.byhy.net/files/selenium/test4.html")
        wd.find_element(By.XPATH, """//*[@id="b2"]""").click()
        time.sleep(2)
        hand = str(wd.switch_to.alert.text)
        assert hand == "你确定要和白月黑羽一起学Python吗？"

    def test_013(self):  # 包含某个内容
        wd = webdriver.Edge(service=Service(r"d:\msedgedriver.exe"))
        wd.get("https://cdn2.byhy.net/files/selenium/test4.html")
        wd.find_element(By.XPATH, """//*[@id="b2"]""").click()
        time.sleep(2)
        hand = str(wd.switch_to.alert.text)
        print(hand)
        assert hand in "测试你确定要和白月黑羽一起学Python吗？"

    def test_014(self):  # 不包含在某个内容
        wd = webdriver.Edge(service=Service(r"d:\msedgedriver.exe"))
        wd.get("https://cdn2.byhy.net/files/selenium/test4.html")
        wd.find_element(By.XPATH, """//*[@id="b2"]""").click()
        time.sleep(2)
        hand = str(wd.switch_to.alert.text)
        print(hand)
        assert hand not in "测试"

    def test_015(self):  # 弹窗确认
        wd = webdriver.Edge(service=Service(r"d:\msedgedriver.exe"))
        wd.get("https://cdn2.byhy.net/files/selenium/test4.html")
        wd.find_element(By.XPATH, """//*[@id="b2"]""").click()
        wd.switch_to.alert.accept()
        hand = str((wd.find_element(By.XPATH, "/html/body/div/li[1]")).text)
        print(hand)
        assert hand == "确定"

    def test_016(self):  # 弹窗确认
        wd = webdriver.Edge(service=Service(r"d:\msedgedriver.exe"))
        wd.get("https://cdn2.byhy.net/files/selenium/test4.html")
        wd.find_element(By.XPATH, """//*[@id="b2"]""").click()
        wd.switch_to.alert.accept()#弹窗确认
        tips = str(wd.find_element(By.XPATH, "/html/body/div/li").text)
        assert tips == "确定"

    def test_017(self):  # 弹窗取消
        wd = webdriver.Edge(service=Service(r"d:\msedgedriver.exe"))
        wd.get("https://cdn2.byhy.net/files/selenium/test4.html")
        wd.find_element(By.XPATH, """//*[@id="b2"]""").click()
        wd.switch_to.alert.dismiss()#弹窗取消
        tips = str(wd.find_element(By.XPATH, "/html/body/div/li").text)
        assert tips == "取消操作"

    def test_018(self):  # 弹窗输入
        wd = webdriver.Edge(service=Service(r"d:\msedgedriver.exe"))
        wd.get("https://cdn2.byhy.net/files/selenium/test4.html")
        time.sleep(2)
        wd.find_element(By.XPATH,"""//*[@id="b3"]""").click()
        wd.switch_to.alert.send_keys("测试内容")#弹窗输入
        wd.switch_to.alert.accept()#弹窗确认
        tips = str(wd.find_element(By.XPATH, "/html/body/div/li").text)
        assert tips in "你想学习:测试内容"

