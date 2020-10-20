# coding:utf-8
import unittest
import os
#import HTMLTestRunner
# import HTMLTestRunner_jpg
# import HTMLTestRunner_PY3V1 #饼图
# import HTMLTestRunner_PY3_New #通过率等表头优化
import HTMLTestRunner_PY3V2 #通过率等表头优化+饼图
import HTMLTestRunner_CN_pie #汉化+饼图
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup
from selenium import webdriver

import sys

# reload(sys)
# sys.setdefaultencoding('utf8')
    
# 用例路径
#case_path = os.path.join(os.getcwd(), "case")
#case_path = "E:\\test\\case"
case_path = "F:/SAASInterfaceAuto/case"
#case_path = r"E:\test\case"
# 报告存放路径
#report_path = os.path.join(os.getcwd(), "report")
#report_path = "E:\\test\\report"
report_path = "F:/SAASInterfaceAuto/report"
#report_path = r"E:\test\report"
# html报告文件
now = time.strftime("%Y%m%d_%H%M%S")
# filename = 'Auto_test_report_'+now+'.html'
filename = 'AutoTestReport_'+now+'.html'
#report_path = ".\\report"+filename
report_abspath = os.path.join(report_path, filename)

discover = unittest.defaultTestLoader.discover(case_path,
                                                pattern="test*.py")#,
                                                #top_level_dir=None)
#生成的报告报错：
# <!--    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">-->
# <!--首先，js代码没有错误，在里面使用了el表达式，但是编辑器总是提示this inspection checks that the script tag content is valid XML，-->
#     <!DOCTYPE html>


fp = open(report_abspath, "wb")
# runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
# runner = HTMLTestRunner_jpg.HTMLTestRunner(stream=fp,
runner = HTMLTestRunner_PY3V2.HTMLTestRunner(stream=fp,
# runner = HTMLTestRunner_PY3_New.HTMLTestRunner(stream=fp,
# runner = HTMLTestRunner_CN_pie.HTMLTestRunner(stream=fp,
                                       # title=u'SAAS-DDS接口自动化测试报告,测试结果如下：',
                                       title=u'SAAS-DDS接口自动化测试报告：',
                                       description=u'用例执行情况：',
                                       tester = '陈诚')   # HTMLTestRunner_PY3_New带测试人员

# 调用add_case函数返回值
runner.run(discover)
fp.close()
#发送邮件
# ----------1.跟发件相关的参数------
smtpserver = "smtp.163.com"  # 发件服务器
port = 0  # 端口
sender = "13662219826@163.com"  # 账号
psw = "13662219826Cc"  # 密码（因为开启了IMAP服务现在换授权码登录了）

# smtpserver = "smtp.139.com"  # 发件服务器
# port = 25  # 端口
# sender = "13662219826@139.com"  # 账号
# psw = "15927691825Gyy"  # 密码（因为开启了IMAP服务现在换授权码登录了）
# receiver = ["xxxx@qq.com"]      # 单个接收人也可以是list
# receiver = ["80003718@sfmail.sf-express.com"]      # 单个接收人也可以是list
receiver = ["943003526@qq.com", "718078871@qq.com", 'david0929@139.com', '596827921@qq.com']  # 多个收件人list对象

'''
顺丰内网：
mail_server = smtplib.SMTP()
mail_server.connect(self.smtp_host, self.smtp_port)

mail.smtp.host = lsmtp.sf-express.com
mail.smtp.port = 25
'''
# ----------2.编辑邮件的内容------
file_path = report_abspath
with open(report_abspath, "rb") as fp:
    mail_body = fp.read()

msg = MIMEMultipart()
msg["from"] = sender  # 发件人
msg["to"] = ";".join(receiver)  # 多个收件人list转str
msg["subject"] = "自动化测试报告，请各位领导查收"  # 主题

# 正文
body = MIMEText(mail_body, "html", "utf-8")
msg.attach(body)

# # 附件
# att = MIMEText(mail_body, "base64", "utf-8")
# att["Content-Type"] = "application/octet-stream"
# # # #att["Content-Disposition"] = 'attachment; filename="test_report.html"'
# # # #att["Content-Disposition"] = 'attachment; filename=report_abspath'
# att["Content-Disposition"] = 'attachment; filename=filename'
# # # att["Content-Disposition"] = ("attachment"; filename=report_abspath)
# msg.attach(att)

# 附件
att = MIMEText(mail_body, "base64", "utf-8")
att["Content-Type"] = "application/octet-stream"
att.add_header("Content-Disposition",'attachment', filename=filename)#问题：发送的附件一直是以report_abspath为名字，没有去取这个变量作为文件名、
msg.attach(att)

    # #邮件内容
    # text = MIMEText(body_main,'html','utf-8')
    # msg.attach(text)

    # #发送附件
    # att = MIMEApplication(open(new_report_fail, 'rb').read())
    # # att = MIMEText(sendfile, 'base64', 'utf-8')
    # att['Content-Type'] = 'application/octet-stream'
    # att.add_header('Content-Disposition', 'attachment', filename=('utf-8', '',now + "_report.html"))
    # msg.attach(att)

print("已生成测试报告文件，见：%r" % report_abspath)
# f = open(report_path)
# Auto_test_report = f.read()
# print Auto_test_report
# driver = webdriver.Firefox()
# driver = webdriver.Ie()
# driver = webdriver.Chrome()
# url = "file:///C:/Users/Administrator/Desktop/" + filename
# print(url)
# driver.get(url)
# time.sleep(5)
# driver.quit()
# for i in range(10,-1,-1):
#     print("准备退出！！！")
#     time.sleep(1)
#     print(i)
	
# ----------3.发送邮件------
send_or_not = 0 # 0-不发送 1-发送
if send_or_not == 1:
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)  # 连服务器
        smtp.login(sender, psw)  # 登录
        smtp.sendmail(sender, receiver, msg.as_string())  # 发送
        smtp.quit()
        print("邮件发送成功，测试情况见附件测试报告。")
    except smtplib.SMTPException:
        print("Error：无法发送邮件")
else:
    print("不发送邮件...")
# #删除多余的测试报告文件
# my_file = report_abspath
# if os.path.exists(my_file):
    # ChenchengSay = raw_input("请决定是否删除测试报告？")
    # if ChenchengSay == "YES":
        # #删除文件，可使用以下两种方法。
        # os.remove(my_file)#彻底删除，回收站也找不到了
        # #os.unlink(my_file)
    # else:
        # print u"先不删除吧！！！"
# else:
    # print 'no such file:%s'%my_file
