# a = [3,5,6]
# b = [9,4,2]
# c = a + b
# print(c)
# a = [6,4,55]
# c = a + b
# print(c)

# 求长度
# a_list = ['a',"asddd",1,66,3.55]
# print(len(a_list))

# 查找
# seek = [522,2,55,'a',"sss"]
# print(seek.index("sss"))

# 一个值在列表出现的次数
# sum = [12,55,21,12,12]
# print(sum.count(12))

# 列表乘法
# a = [12,22]
# b = a * 3
# print(b)
# c = [a] * 3
# print(c)
# print([a * 3])
# a.append(3)
# print(a * 3)
# print(b)
# print(c)

# 元素排序sort
# one = [5, 9, 2, 4]
# one.sort()
# print(one)
#
# two = [4, 1, 6, 2]
# two.sort(reverse=True)
# print(two)
#
# three = ['s', 'c', 'x']
# three.sort(key=len)
# print(three)

# sorted 改变生成新序列，不会改变原序列
# li_one = [8, 2, 4, 66]
# li_two = sorted(li_one)
# print(li_two)
# print(li_one)

# # reverse() 逆置列表 从右至左
# one = ['l', 'f', 'w', 's']
# one.reverse()
# print(one)

# li_one = ['p', 'y', 't', 'h', 'o', 'n']
# print(li_one[1:4:2])
# print(li_one[2:])
# print(li_one[:3])
# print(li_one[:])
# one = ["abc", "def"]
# print(one[:1])

# 复制
# a = [0, 5, 4, 8, 6]
# b = a.copy()
# print("b=" + str(b) + '\n')

# del 删除
# name = ['aaa', 'ss', 'lll']
# del name[1]
# print(name)
# del name

# remove() 移除匹配到的第一个
# arr = ['a', 'd', 'd']
# arr.remove('d')
# print(arr)

# pop() 移除某个元素
# num = [1, 2, 3, 4, 5]
# num.pop()
# print(num)
# num.pop(0)
# print(num)
# 会改变列表元素

# clear()   清空列表
# n_d = [1, 2, 3, 4]
# n_d.clear()
# print(n_d)

# 列表推导式 [exp for x in list]
# ls = [1, 2, 3, 4, 5, 6, 7]
# i = 1
# ls = [i*i for i in ls]
# print(ls)

# if判断语句和for语句
# lss = [1, 3, 4, 5, 7, 9]
# d = 1
# lss = [d for d in lss if d < 10]
# print(lss)
# # for循环嵌套
# ldd = [2, 4, 5, 8, 9]
# x = y = 0
# lsd = [x+y for x in lss for y in ldd]
# print(lsd)

# 复习
a = [12, 51, 15, 4, 5]
# a.insert(0,5)
# print(a)
# a.insert(4,5.2)
# print(a)
# a[2] = 15
# print(a[2])
# print(a.index(15))
# print(21 in a)
# a[0] = 21
# print(21 in a)
# a.count(4)
# print(a.count(4))
# a = a[::-1]
# print(a)
# a = a[::-2]
# print(a)
# a.remove(12)
# print(a)
# del a[0:5]
# print(a)
# del a
# print()

# 元组
# 元组不可修改 改变的是列表
# tuple_1 = [1, 2, 3, [4, 5]]
# tuple_1[3][0] = "a"
# tuple_1[3][1] = "b"
# print(tuple_1)

# 元组删除
# tuple_1 = (1, 2, 3)
# del tuple_1
# print(tuple_1)
# 使用切片删除元组元素
# tuple_1 = (1, 2, 3, 4)
# tuple_1 = tuple_1[1:3:1]
# print(tuple_1)

# 课内实践
# tu_num1 = ('p', 'y', 't', 'h', ['o', 'n'])
# tu_num1[4][1] = 'x'
# print(tu_num1)
# tu_num1[len(tu_num1)-1].append('h')
# print(tu_num1)

# index()查找 count()出现次数 max()元组最大数
# min()元组最小数 list()转换列表 tuple()转换元组
# tuple_2 = (1, 23, 43, 20, 49, 23, 23)
# print(tuple_2.index(23))
# print(tuple_2.count(23))
# print(max(tuple_2))
# print(min(tuple_2))
# list(tuple_2)
# print(tuple_2)
# tuple(tuple_2)
# print(tuple_2)

# 课内实践
# b = (1, 52, 7, 4, 7)
# b += tuple("Jack")
# print(b)
# i = 0
# for i in b:
#     print(i)
# print(b[1:4])
# print(b.index(4))
# print(b.count(7))
# b = list(b)

# 十大歌手
# singer = input("歌手的姓名：")
# count = 0
# score_10 = []
# for i in score_10:
#     # 输入每位评委分数，比较大小，
#     put_score = int(input("输入评委分数："))
#     score_10 += [put_score]
#     if i == 0:
#         continue
#     elif i > 0:
#         if score_10[i] < score_10[i-1]:
#             min(score_10[i])
#         elif score_10[i] > score_10[i-1]:
#             max(score_10[i])
#     count += score_10[i]
# #     去掉最高数和最小数
# sum = count - max(score_10) - min(score_10)
# print(sum)

# list_singer = []
# i = 0
# while i < 10:
#     score = int(input("单个输入分数："))
#     print(i, end='')
#     sum += score
#     list_singer += [score]
# count = sum - max(list_singer) - min(list_singer)
# print(count)

# 十大歌手
# 一位歌手的平均分
# li_singer = [50, 40, 66, 57, 20, 99, 72, 64, 69, 71]
# sum_1 = 0
# for i in li_singer:
#     sum_1 += i
# # 计算平均分公式 平均分 = 总数 - 最大数 - 最小数
# average = sum_1 - max(li_singer) - min(li_singer)
# print(average)

# adj_1 = int(input("第一位评委分数："))
# adj_2 = int(input("第二位评委分数："))
# adj_3 = int(input("第三位评委分数："))
# adj_4 = int(input("第四位评委分数："))
# adj_5 = int(input("第五位评委分数："))
# adj_6 = int(input("第六位评委分数："))
# adj_7 = int(input("第七位评委分数："))
# adj_8 = int(input("第八位评委分数："))
# adj_9 = int(input("第九位评委分数："))
# adj_10 = int(input("第十位评委分数："))
# count = 0
# list_10 = []
# for i in range(10):
#     put_score = int(input("输入评委分数"))
#     if list_10 == max(list_10)
#     count += list_10

# 正确答案
# 评分列表
# score_li = []
# # 总分
# total_score = 0
# for i in range(1,11):
#     score = float(input(f"请第{i}位评委输入评分：\n"))
#     score_li.append(score)
# score_li.sort()
# print(f"去掉最低分：{score_li[0]}")
# print(f"去掉最高分：{score_li[len(score_li)-1]}")
# # 去掉最低分
# score_li.remove(score_li[0])
# # 去掉最高分
# score_li.pop()
# for j in score_li:
#     total_score += j
# print(f'选手最终得分为：{total_score/(len(score_li))}')

# 神奇魔方阵
# n = 5
# # 5 * 5 二维列表
# magic_square = [[0 for x in range(n)] for y in range(n)]
# i = n / 2
# j = n - 1
# num = 1
# while num <= (n * n):
#     if i == -1 and j == n:
#         j = n - 2
#         i = 0
#     else:
#         if j == n:
#             j = 0
#         if i < 0:
#             i = n - 1
#     if magic_square[int(i)][int(j)]:
#         j = j - 2
#         i = i + 1
#         continue
#     else:
#         magic_square[int(i)][int(j)] = num
#         num = num + 1
#     j = j + 1
#     i = i - 1
# for i in range(0, n):
#     for j in range(0, n):
#         print('%2d ' % (magic_square[i][j]), end='')
#         if j == n - 1:
#             print()

# 集合
# s1 = {1}
# s2 = {1,'b', (2, 6)}
# s = set()
# s3 = set('python')
# s4 = set(range(5))
# # 不能空{} 可以空set（）
# set_demo1 = {}
# set_demo2 = set()
# print(type(set_demo1))
# print(type(set_demo2))
# 集合是可变的

# S = {2, 'S', 5.2, (4, 3)}
# S.add('v')
# S.remove(2)
# S.discard(5.2)
# S.pop()
# S.clear()
# T = S.copy()
# S.isdisjoint(T)
# print(S)

# 集合推导式
# ls = [1, 2, 3, 4, 5, 6, 7, 8]
# s = {i for i in ls if i % 2 == 0}
# print(s)

# set.update(s)添加多个元素
# set_1 = {1, 2}
# list_2 = [3, 4]
# tuple_3 = (5, 6)
# dict_4 = {'key1': 7, 'key2': 8}
# set_1.update(list_2)
# print(set_1)
# set_1.update(tuple_3)
# print(set_1)
# set_1.update(dict_4)
# print(set_1)

# 课内实践
# def remove_duplicates(s):
#     return join(set(s))
# input_string = "assvewnvnwui"
# result = remove_duplicates(input_string)
# print(result)

num_one = 12
def sum(num_two):
    global num_one
    num_one = 90
    return num_one + num_two
print(sum(10))