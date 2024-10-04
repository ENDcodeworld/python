# l = []
# for i in range(3):
#     x = int (input('请输入一个整数：'))
#     l.append(x)
#
# l.sort()
# print(1)
#
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d x %d=")

# import turtle as t
# def draw_fiveStars(leng):
#     count = 1
#     while count <= 5:
#         t.forward(leng)
#         t.right(144)
#         count += 1
#     leng += 10
#     if leng <= 100:
#        draw_fiveStars(leng)
# def main():
#     t.penup()
#     t.backward(100)
#     t.pendown(2)
#     t.pencolor('red')
#     segment = 50
#     draw_fiveStars(segment)
#     t.exitonclick()
# if __name__ == '_main_':
#  main()

# string = ("python是一种面向对象的丶解释型0的计算机程序设计语言")
# print(string)

# dict_demo = {"name":"zhangsan","age" : 18}
# print(type(dict_demo))
# name = input("请输入你的名字：")
# print(name)

# zh_name = "通用名称：阿莫西林胶囊"
# en_name = "Amoxicillin Casules"
# character = "性状：本品内容物为白色至黄色粉末或颗粒"
# print(zh_name,en_name,character,sep = "\n")

# 打印购物小票
# JSD = 40
# SC = 50
# DKQ = 8
# WX = 5
# sum = JSD+SC+DKQ+WX
# print(sum)

# 失败品
# C = -273.15
# K = 5
# count = C * K
# print(count)

#T(K) = t(°C）+273.15
# celsius = float(input("请输入摄氏温度："))
# kelvin = celsius + 273.15
# print(celsius,"°C对应的开尔文为：",kelvin)

#身体质量指数（BMI)=体重（单位为kg）÷身高²（单位为m）
# weight = float(input("请输入体重："))
# height = float(input("请输入身高："))
# BMI = weight / (height * height)
# print("你的BMI指数是：",BMI)

# 圆的面积公式：S=Πr²
# radius = float(input("输入你的半径："))
# diamater = radius * 2
# S =float( 3.14 * (radius * radius))
# print("圆的直径是：",diamater,"面积是：",S)

# all_coal =float(29.5)
# t4 = 4
# t2 =float(2.5)
# re_coal = float(all_coal - t4 * 3)
# sum = re_coal // t2
# print("最终需要多少次运完",sum)

# print(bool(0))
# print(bool(''))
# print(bool(' '))
# print(bool(1))
# print(bool(-3))
# print(bool(''))

# print(False+True)
# print(True+True)
# print(False*True)
# print(True*True)
# print(False-True)
# print(True-True)

# print(int(5.9))
# print(round(5.9))

# x = 10
# y = 20
# print(x and y)
# print(x or y)
# print(not x)

# a = 1
# b = 1
# print(a is b)
# print(a is not b)
# print(id(a))
# print(id(b))

i = 0
for i in range(10):
    j = 0
    print()
    for j in range(10):
        print("_",end=" ")
    print()
