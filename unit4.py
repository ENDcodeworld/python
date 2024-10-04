# print('ddddd')
# print("ddddd")
# print('''ss\rsssxxx''')
# print("let's \rlearn \rpython")
# print('\v')
# print(r'nkkkk:\njhjnjji\r:kkojj\b')
# value = 10
# format = '我今年%d岁'
# print(format % value)

# name = '张矝'
# age = 19
# address = '北京市昌平区'
# print('-----------------')
# print("姓名：%s" % name)
# print("年龄：%d" % age)
# print("地址：%s" % address)
# print('-----------------')

# name = '张处长'
# age = '50'
# string = "姓名：{}\n年龄：{}"
# print(string.format(name,age))

# name = '张总'
# age = 50
# string = "姓名：{1}\n年龄：{0}"
# print(string.format(age,name))
#
# name = '张强'
# age = 20
# weight = 65
# string = "姓名：{name}\n年龄：{age}\n重量：{weight}"
# print(string.format(name=name,age=age,weight=weight))

# points = 50
# total = 100
# print('所占百分比：{:.2%}'.format(points/total))

# age = 20
# gender = '男'
# print(f'年龄：{age}\n性别：{gender}')

# 例题
# 进制转换
# ten = int(input("请输入数据：\n"))
# change = input("选择要改变的进制：二，八，十六\n")
# if change == '2':
#     print(f"进制转换后的数据为：{bin(ten)}")
# elif change == '8':
#     print(f"进制转换后的数据为：{oct(ten)}")
# elif change == '16':
#     print(f"进制转换后的数据为：{hex(ten)}")

# print("======================开始下载=====================")
# points = 64
# total = 100
#
# print('{:.2%}'.format(points/total))
# print("")

# 文本进度条
# import time
# incomplete_sign = 50
# print('='*23+'开始下载'+'='*25)
# for i in range(incomplete_sign + 1):
#     completed = "*" * i
#     incomplete = "." * (incomplete_sign - i)
#     percentage = (i / incomplete_sign) * 100
#     print("\r{:.0f}%[{}{}]".format(percentage,completed,incomplete), end="")
#     time.sleep(0.6)
# print("\n" + '='*23+'下载完成'+'='*25)

# 字符串的查找
# word = 't'
# string = 'Python'
# result = string.find(word)
# print(result)

# # 字符串的替换
# string = "ALL"

# 字符串的分割与拼接
# string_example = " The more efforts you make, the more fortune you get."
# print(string_example.split())
# print(string_example.split('m'))
# print(string_example.split('e',2))
#
# symbol = '*'
# world = 'python'
# print(symbol.join(world))
#
# start = '黑神话'
# end = '悟空'
# print(start + end)

# # 删除字符串的指定字符
# old_string = '  life is short, Use Python '
# strip_str = old_string.strip()
# lstrip_str = old_string.lstrip()
# rstrip_str = old_string.rstrip()
# print(f'strip 方法:{strip_str}')
# print(f'lstrip 方法:{lstrip_str}')
# print(f'rstrip 方法:{rstrip_str}')
# # 打印输出时需要用英文符号':'

# # 字符串的大小写转换
# old_string = 'hello woRld'
# upper_str = old_string.upper()
# lower_str = old_string.lower()
# cap_str = old_string.capitalize()
# title_str = old_string.title()
# print(f'upper的方法:{upper_str}')
# print(f'lower的方法:{lower_str}')
# print(f'capitalize的方法:{cap_str}')
# print(f'title的方法:{title_str}')

# 字符串对齐
# sentence = 'hello world'
# center_str = sentence.center(30,'-')
# print(f"居中对齐:{center_str}")
# ljust_str = sentence.ljust(30,'-')
# print(f"居左对齐:{ljust_str}")
# rjust_str = sentence.rjust(30,'-')
# print(f"居右对齐:{rjust_str}")

# 敏感词替换
# mgc_string = "政治敏感，暴力倾向，不健康色彩"
# if mgc_string == '政治敏感':
#     zzmg_string = mgc_string.replace("政治敏感","000")
#     print(zzmg_string)
# elif mgc_string == "暴力倾向":
#     blqx_string = mgc_string.replace("暴力倾向", "+++")
#     print(blqx_string)
# elif mgc_string == "不健康色彩":
#     bjksc_string = mgc_string.replace("cnm","***")
#     print(bjksc_string)

# sensitive_character = '你好'
# test_sentence = input('请输入一段话:')
# # 遍历输入的字符是存在敏感词库中
# for line  in sensitive_character:
#     if line in sensitive_character:
#         test_sentence = test_sentence.replace(line,'*')
# print(test_sentence)

# 文字排版工具
# string = input("请输入文字进行排版：")
# selcet_rule = input("选择排版的功能：1.删除空格，2.英文标点替换，3.英文单词大写功能\n")
# if selcet_rule == '1':
# 注意if的==1要加‘’
#     strip_str = string.strip()
#     print(f'删除空格：{strip_str}')


# string = "他问，你知道cba是什么单词的缩写么,..3      ？    "
# print(string)
# print("1.删除空格")
# print("1.英文标点替换")
# print("3.首字母大写")
# print("4.退出")
#
# while True:
#     option = input("请输入功能选项：\n")
#     if option == '1':
#         string = string.replace(' ','')
#         print(string)
#     #替换英文标点
#     elif option == '2':
#         for i in string:
#             if i == ',':
#                 string = string.replace(',','，')
#             elif i == '.':
#                 string = string.replace('.','。')
#             elif i == '?':
#                 string = string.replace('?','？')
#             elif i == "'":
#                 string = string.replace("'","‘")
#         string = string
#         print(string)
#     # 字母大写功能
#     elif option == '3':
#         string = string.upper()
#         print(string)
#     elif option == '4':
#         break

# name = '张青'
# age = 25
# string = "姓名：{1}\n年龄：{0}"
# print(string.format(age,name))

# age = 20
# gender = '男'
# print(f'年龄：{age}\n性别：{gender}')
#
#
# symbol = '*'
# world = 'Python'
# print(symbol.join(world))

old = ' Ldldsdssss'
lst_str = old.lstrip(' L')
print(f'{lst_str}')