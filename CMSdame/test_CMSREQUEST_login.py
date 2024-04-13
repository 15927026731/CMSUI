import pytest
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
from lib.requestlogin import *
from CMSdame.lib.readxlex import *


class Test_001:

    def test_001(self):
        test = str(REQUEST().login().text)
        assert "登录成功" in test

    @pytest.mark.parametrize("phone,tittle",
                             ExcelData("lib/data3.xls", "Sheet1").readExcel()
                             )
    def test_002(self, phone, tittle):
        test = str(REQUEST().add(phone, tittle).text)
        assert "提交信息成功" in test

    @pytest.mark.parametrize("findname", ExcelData("lib/data3.xls", "Sheet2").readExcel())
    def test_003(self, findname):
        test = str(REQUEST().find(findname).text)
        # assert  test == None
        # assert not None

        assert "return" in test
