# 用户输入一个整数n，生成长度为n的列表，将n个随机数放入列表
import random
in_int = int(input('请输入一个整数:'))
my_list = []
for i in range(in_int):
    num = random.randint(1,100)
    my_list.append(num)
print(my_list)
