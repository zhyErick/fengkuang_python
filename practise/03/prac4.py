# 用户输入一个整数n,生成长度为n的列表，将n个随机的奇数放入列表中
import random
length = int(input('请输入一个整数：'))
my_list = []
for i in range(length):
    while True:
        num = random.randint(1, 1000)
        if num % 2 == 1:
            my_list.append(num)
            break

print(my_list)