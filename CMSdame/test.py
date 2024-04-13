from CMSdame.lib.readxlex import *
import sys
sys.path.append('C:/Users/24202/PycharmProjects/CMSUI/CMSdame/lib')


# print(ExcelData(".lib.data3.xls","Sheet1").readExcel())
data_path = "lib/data3.xls"
sheetname = 'Sheet1'
get_data = ExcelData(data_path, sheetname)
datas = get_data.readExcel()
print(datas)