# import re
#
#
# report_abspath = 'Auto_test_report_20180718_235943.html'
# text = report_abspath#Auto_test_report_20180718_151900.html
# pattern = 'Auto_test_report'
# match = re.findall(pattern, text)
# print match
#
#
# # file.name	返回文件的名称。
#
# # with open(report_abspath, "rb") as fp:
#     # mail_body = fp.read()
#
#
# # #删除多余的测试报告文件
# # my_file = report_path
# # if os.path.exists(my_file):
#     # ChenchengSay = raw_input("请决定是否删除测试报告？")
#     # if ChenchengSay == "YES":
#         # #删除文件，可使用以下两种方法。
#         # os.remove(my_file)#彻底删除，回收站也找不到了
#         # #os.unlink(my_file)
#     # else:
#         # print u"先不删除吧！！！"
# # else:
#     # print 'no such file:%s'%my_file
#
# # while  delfile =! my_file:
# 	# os.remove(my_file)
#
#
# 	# while 1:            # 循环条件为1必定成立
#     # print i         # 输出1~10
#     # i += 1
#     # if i > 10:     # 当i大于10时跳出循环
#         # break
#
#
#
# #python可以通过os包对文件进行操作。以下代码分别实现一文件夹下所有文件名的读取和文件删除操作
#
# import os
# #读取path目录下的文件名，返回文件名list列表
# def readFileName(path):
#     lists = []
#     for root,dirs,files in os.walk(path):
#         for file in files:
#             lists.append(os.path.join(root,file))
#     return lists
#
# #删除路径为filepath的文件
# def delFile(filepath):
#     os.remove(filepath)
#     print "ok"
#
#
# >>> readFileName('E:\\test\\report')
# ['E:\\test\\report\\Auto_test_report_20180718_151900.html', 'E:\\test\\report\\Auto_test_report_20180718_234820.html', 'E:\\test\\report\\Auto_test_report_20180718_235328.html', 'E:\\test\\report\\Auto_test_report_20180718_235425.html', 'E:\\test\\report\\Auto_test_report_20180718_235636.html', 'E:\\test\\report\\Auto_test_report_20180718_235943.html', 'E:\\test\\report\\__init__.py']
# >>> filenames = readFileName('E:\\test\\report')
# >>> type(filenames)
# <type 'list'>
#
# >>> for name in filenames:
# 	if name == 'E:\\test\\report\\__init__.py':
# 		print '不能删除__init__.py文件'
# 		pass
# 	if name == 'E:\\test\\report\\Auto_test_report_20180718_235943.html':
# 		print '不能删除最新的测试报告'
# 		pass
# 	else:
# 		os.remove(name)
#
#
# 不能删除最新的测试报告
# 不能删除__init__.py文件
# # \