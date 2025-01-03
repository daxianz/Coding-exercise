# -*- coding: utf-8 -*-

numbers = input("请输入一个包含若干整数的列表（用逗号分隔）：")
numbers_list = [int(num) for num in numbers.split(',')]

odd_numbers = [num for num in numbers_list if num % 2 != 0]


print(odd_numbers)
