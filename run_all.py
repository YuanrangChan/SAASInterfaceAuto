# coding:utf-8
import unittest
import os
import HTMLTestRunner
import time

# 用例路径
# case_path = os.path.join(os.getcwd(), "case")
case_path = "F:/SAASInterfaceAuto/case"
# 报告存放路径
# report_path = os.path.join(os.getcwd(), "report")
report_path = "F:/SAASInterfaceAuto/report"

# html报告文件
now = time.strftime("%Y%m%d_%H%M%S")
filename = 'Auto_test_report_'+now+'.html'
#report_path = ".\\report"+filename 
report_abspath = os.path.join(report_path, filename)

discover = unittest.defaultTestLoader.discover(case_path,
                                                pattern="test*.py")#,
                                                #top_level_dir=None)


fp = open(report_abspath, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                       title=u'自动化测试报告,测试结果如下：',
                                       description=u'用例执行情况：')

# 调用add_case函数返回值
runner.run(discover)
fp.close()
