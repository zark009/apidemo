# -*-coding:utf-8 -*-
import xlrd
from xlutils.copy import copy

from common.api import *

oldwb = xlrd.open_workbook('url.xls')
oldsh = oldwb.sheet_by_index(0)
nrows = oldsh.nrows
newwb = copy(oldwb)
newsh = newwb.get_sheet(0)

def resultExcel():
    for i in range(1, nrows):
     url = oldsh.cell_value(i, 1)
     print(url)
     requests_data = oldsh.cell_value(i, 0)
     print(requests_data)
     r = GetHttp(url, requests_data)
     status = r.status_code
     if status==200:
       content = r.text
     reqtime = float(r.elapsed.microseconds) / 1000
     AC_result = content
     newsh.write(i, 3, content)
     newsh.write(i, 5, Time())
     newsh.write(i, 6, reqtime)
     EX_result = oldsh.cell(i, 2).value
     #print("实际返回:" + AC_result)
     #print("预期返回:" + EX_result)
     if re.search(EX_result,str(content)):
        newsh.write(i, 4, "PASS")
     else:
        newsh.write(i, 4, "FAIL")

     if reqtime < 20.0:
        newsh.write(i, 7, 'Normal')
     else:
        newsh.write(i, 7, 'Timeout')
def saveExcel():
  newwb.save('url.xls')
if __name__ == '__main__':
  resultExcel()
  saveExcel()