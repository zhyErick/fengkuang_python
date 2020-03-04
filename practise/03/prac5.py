# 用户输入一个整数n,生成长度为n的列表，将n个随机的大写字符放入列表中
import random
length = int(input('请输入一个整数：'))
my_list = []
for i in range(length):
    num = random.randint(65, 65 + 25)
    my_list.append(chr(num))

print(my_list)