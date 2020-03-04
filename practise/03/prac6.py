# 用户输入n格字符串,将这些字符串收集到列表中,然后去除其中重复的字符串后输出列表

length = int(input("请输入字符串个数:"))
old_list = []
for i in range(length):
     old_list.append(input('请输入字符串:'))
print(old_list)
new_list = []
for i in old_list:
    if i not in new_list:
        new_list.append(i)

print(new_list)