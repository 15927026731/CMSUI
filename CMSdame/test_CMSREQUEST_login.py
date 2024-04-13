import pytest
# import sys
# sys.path.append('C:/Users/24202/PycharmProjects/CMSUI/CMSdame/lib')
from .lib.requestlogin import *
from .lib.readxlex import *


class Test_001:

    def test_001(self):
        test = str(REQUEST().login().text)
        assert "登录成功" in test



    @pytest.mark.parametrize("phone,title",  #数据驱动，调用读取xls表格方法，调用data3.xls的Sheet1表数据，作用于驱动
                             ExcelData("data3.xls", "Sheet1").readExcel())

    def test_002(self,phone,title):
        print(ExcelData("data3.xls", "Sheet1").readExcel())
        test = str(REQUEST().add(phone,title).text)
        assert "提交信息成功" in test



    @pytest.mark.parametrize("findname",
                             ExcelData("data3.xls", "Sheet2").readExcel())
    def test_003(self,findname):
        test = str(REQUEST().find(findname).text)
        assert "findname" not in test



