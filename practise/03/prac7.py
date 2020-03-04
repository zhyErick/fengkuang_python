# 用户随机输入N个大写字母,程序使用dict统计用户输入的每个字母的次数
my_str = input("请输入N个大写字母:")
my_list = list(my_str)
my_dict ={}
for i in {}.fromkeys(my_list).keys():
    my_dict[i] = my_str.count(i)

print(my_dict)