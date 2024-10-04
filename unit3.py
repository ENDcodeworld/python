# if语句的应用
# score = 85
# if score >= 90:
#     print("超级棒！")
# elif 80 <= score < 89:
#     print("优秀！")
# elif 70 <= score <= 79:
#     print("良好")
# elif 60 <= score <= 69:
#     print("及格")
# else:
#     print("考试不及格！")

# if的嵌套
# years = 2020
# month = 2
# if month in [1,3,5,7,8,10,12]:
#     print("%d月有31天" %month)
# elif month in[4,6,9,11]:
#     print("%d月有30天" %month)
# elif month == 2:
#     if years % 400 == 0 or years % 4 == 0 and years % 100 == 0:
#         print("%d年%d月有29天" % (years,month))
#     else :
#         print("%d年%d月有28天" % (years,month))

# 四则运算

# one = float (input("请输入加减乘除："):

# 猜数字


# i = 1
# result = 0
# while i <= 10:
#     result += i
#     i += 1
# print(result)

# # while嵌套画三角形
# i = 1
# while i < 6:
#     j = 0
#     while j < i:
#         print("*",end=" ")
#         j += 1
#     print()
#     i += 1
#
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# 100以内的偶数
# i = 0
# while i < 100:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# 判断一个数是正还是负
# i = input("请输入一个数判断是正数还是负数：")
# if i < '0':
#     print("该数是负数。")
# elif i > '0':
#     print("该数是正数。")
# else:
#     print("该数为0。")

# 实现100以内的质数
# i = 2
# num = []
# while i < 100:
#     j = 2
#     while j < 100:
#         if i % j == 0:
#             break
#         print(i)
#         print(j)


# num = []
# i = 2
# for i in range(2,100):
#     j = 2
#     for j in range(2,i):
#         if(i % j == 0):
#             break
#     else:
#         num.append(i)
# print(num)

