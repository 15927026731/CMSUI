import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
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


class WebUI:

    def __init__(self):
        self.wd = webdriver.Edge(service=Service(r"d:\msedgedriver.exe"))
        self.wd.implicitly_wait(10)
        self.wd.get("http://127.0.0.1:8080")

    def login(self, username, password):#用户密码输入
        if username is not None:
            self.wd.find_element(By.NAME, """username""").send_keys(str(username))
        if password is not None:
            self.wd.find_element(By.XPATH,
                                 """/html/body/table[1]/tbody/tr/td/table/tbody/tr/td[1]/form/input[4]""").send_keys(
                str(password))
        self.wd.find_element(By.XPATH, """/html/body/table[1]/tbody/tr/td/table/tbody/tr/td[1]/form/input[5]""").click()

    def register(self, ):#注册窗口切换
        self.wd.find_element(By.XPATH, "/html/body/table[1]/tbody/tr/td/table/tbody/tr/td[1]/form/input[6]").click()
        for hands in self.wd.window_handles:
            self.wd.switch_to.window(hands)
            if "注册会员" in self.wd.title:
                break

    def registerclick(self):#注册点击
        self.wd.find_element(By.XPATH, "/html/body/table[4]/tbody/tr/td[2]/table/tbody/tr[3]/td/input").click()

    def registerdata(self, name, password, repassword, email):#注册内容输入
        if name is not None:
            self.wd.find_element(By.XPATH, """//*[@id="username"]""").send_keys(name)
        if password is not None:
            self.wd.find_element(By.XPATH, """//*[@id="password"]""").send_keys(password)
        if repassword is not None:
            self.wd.find_element(By.XPATH, """//*[@id="repassword"]""").send_keys(repassword)
        if email is not None:
            self.wd.find_element(By.XPATH, """//*[@id="email"]""").send_keys(email)
        time.sleep(3)
        self.wd.find_element(By.XPATH, "/html/body/table[4]/tbody/tr/td[2]/table/tbody/tr[9]/td[2]/input[1]").click()

    def findhand(self, handname):#查询窗口句柄
        for hand in self.wd.window_handles:
            self.wd.switch_to.window(hand)
            if webUI.wd.title in handname:
                break


webUI = WebUI()

# if __name__ == "__main__":
#     webUI.login("test1", "ZJqr@@022")
