# -*- coding:utf-8 -*-
import datetime

import xlrd

from report.pyh import *


class HtmlReport:
    def __init__(self, title, head):
        self.title = title                                       # 网页标签名称
        self.head = head                                      # 标题
        self.filename = 'testreport.html'   # 结果文件名
        self.dir = './'         # 结果文件目录
        self.time_took = '00:00:00'         # 测试耗时
        self.success_num = 0                  # 测试通过的用例数
        self.fail_num = 0                     # 测试失败的用例数
        self.error_num = 0                    # 运行出错的用例数
        self.block_num = 0                    # 未运行的测试用例总数
        self.case_total = 0                   # 运行测试用例总数

    # 生成HTML报告
    def generate_html(self, file):

        page = PyH(self.title)
        page.addJS('./report/test.js')
        page.addCSS('./report/test.css')
        page << h1(self.head, align='center',bgcolor='#27ab9b') # 标题居中
        page << p('测试日期：' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        page << p('测试总耗时：' + self.time_took)

        wb = xlrd.open_workbook('url.xls')
        sh = wb.sheet_by_index(0)
        nrows = sh.nrows
        print(nrows)
        case_id = 0
        case_name = 0
        interface_url = 0
        param_data = 0
        ac_result = 0
        ex_result = 0
        run_time = 0
        #logger.info('正在查询测试用例总数')
        self.case_total = nrows-1
        #logger.info('正在查询执行通过的用例数')
        self.success_num = nrows
        #logger.info('正在查询执行失败的用例数')
        self.fail_num = nrows
        #page << p('用例总数：' + str(self.case_total) + '&nbsp'*10 + '成功用例数(Pass)：' + str(self.success_num) +\
         #             '&nbsp'*10 + '失败用例数(Fail)：' + str(self.fail_num) + '&nbsp'*10)

        page << p('用例总数：' + str(self.case_total))
            #  表格标题caption 表格边框border 单元格边缘与其内容之间的空白cellpadding 单元格之间间隔为cellspacing
        tab = table(border='1', cellpadding='1', cellspacing='0')
        tab1 = page << tab
        tab1 = tab1 << tr(id="test")
        tab1 << (td('用例ID')+td('接口名称')+td('用例描述')+ td('接口url')+ td('执行结果') + td('运行时间'))
                          # + td('入参', bgcolor='#ABABAB',  align='center')
                          # + td('实际结果', bgcolor='#ABABAB', align='center')
        for i in range(1, nrows):
           case_id = sh.cell_value(i,11)
           interface_name = sh.cell_value(i,8)
           case_name = sh.cell_value(i,9)
           interface_url = sh.cell_value(i,1)
           param_data = sh.cell_value(i,0)
           ac_result = sh.cell_value(i,3)
           ex_result = sh.cell_value(i,4)
           run_time =  sh.cell_value(i,6)
           tab1 << tr(td(int(case_id), align='center') + td(interface_name) + td(case_name) + td(interface_url)+td(a(ex_result,href="#"),style="cursor:pointer",onclick="func("+str(i)+")") + td(run_time,a("ms")))
           tab1 = tab1 << tr(id=str(i),style="display:none;")
           tab1 = tab1 << (td(a("入参:" + param_data + '<br/>'), a("实际输出:" + ac_result), colspan="6"))
           #(td(a("入参:" + param_data + '<br/>', style="display:block;"), a("实际输出:" + ac_result), colspan="5"))
        page << p('<br/>')

        page.printOut(file)

    # 创建报告保存目录




    # 统计运行耗时
    def set_time_took(self, time):
        self.time_took = time
        return self.time_took
