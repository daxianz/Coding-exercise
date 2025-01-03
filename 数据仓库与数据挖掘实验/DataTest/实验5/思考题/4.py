# -*- coding: utf-8 -*-

lst1 = input("请输入第一个列表(空格分隔):")
lst2 = input("请输入第二个列表：(空格分隔):")

lst1 = [int(i) for i in lst1.split()]
lst2 = [int(i) for i in lst2.split()]

sum = 0
num_list = [i * j for i in lst1 for j in lst2]
for i in num_list:
    sum += i
print("两个列表内积为：" + str(sum))
