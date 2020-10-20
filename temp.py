# "[requestId=fc25167a2184458bb9381fb6ef2d8420,systemCode=JV-DDS-ISS,containerNo=tempCLCMB01A1589771742507A-A02,containerType=C1,srcDeptCode=CLCMB01A,destDeptCode=CLCMB01AJ1,destUnitAreaCode=CLCMB01AA02,limitTypeCode=<null>,virtualFlag=21,networkType=2,packageNoList=[CL1504567994207],operateDeptCode=CLCMB01A,operateEmpCode=CL10000399,tenantId=CL,operateTm":"1589771742511]"


# str1 ="fc25167a2184458bb9381fb6ef2d8420"
# print(len(str1))

from tkinter import *
import random
# 定义函数， 功能为生成有大写字母、 小写字母、 数字组成的6位随机验证码
def creatAuthCode():
    res1 = ""
    res2 = ""
    res3 = ""
    for i in range(2):
      num = random.randint(0, 9)
      res1 += str(num)
      num = random.randint(65, 91)
      res2 += str(chr(num))
      num = random.randint(97, 123)
      res3 += str(chr(num))
      string = str(res1 + res2 + res3)
      txt.set(string)
# 创建根窗口
root = Tk()
root.title("登录界面")
# root.resizable(False, False)
root.geometry("300x200")

# 设置用户账号输入框
ID = Label(root, text = "账号:")
ID.place(relx = 0.2, rely = 0.2, anchor =CENTER)
text1 = Entry(root)
text1.place(relx = 0.5, rely =0.2, anchor = CENTER, width = 150, height = 25)

# 设置用户密码码输入框
password =Label(root, text = "密码:")
password.place(relx = 0.2, rely = 0.4,anchor = CENTER)
text2 = Entry(root)
text2.place(relx = 0.5,rely = 0.4, anchor = CENTER, width = 150, height = 25)

# 设置验证码输入框
code =Label(root, text = "验证码:")
code.place(relx = 0.22, rely = 0.6,anchor = CENTER)
code = Entry(root)
code.place(relx = 0.4,rely = 0.6, anchor = CENTER, width = 70, height = 25)

# 设置获取验证码的按钮
txt =StringVar()
txt.set("获取验证码")
codestr = Button(root, textvariable =txt, command = creatAuthCode, fg = "red", bg = "blue")
codestr.place(relx = 0.8, rely = 0.6, anchor = CENTER)

# 设置登录按钮
enter = Button(root, text = "登录")
enter.place(relx = 0.5, rely = 0.8,anchor = CENTER)
root.mainloop()