# -*- coding: utf-8 -*-
import datetime

from common.exceltest import *
from report.htmlreport import HtmlReport


def test_api():
    resultExcel()
    saveExcel()


if __name__ == '__main__':

 start_time = datetime.datetime.now()

 test_api()

 end_time = datetime.datetime.now()
 html_report = HtmlReport('test report', '接口测试报告')
 html_report.set_time_took(str(end_time - start_time))
 html_report.generate_html('testreport.html')



