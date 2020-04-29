import itertools as it
# 使用count(10, 3)生成10, 13, 16, ... 的迭代器
for e in it.count(10, 3):
    print(e)
    # 用于跳出无限循环
    if e > 20:
        break
print('-----------')
my_conter = 0
# cycle 用于对序列生成无限循环的迭代器
for e in it.cycle((['Python', 'Kotlin', 'Swift'])):
    print(e)
    # 用于跳出无限循环
    my_conter += 1
    if my_conter > 7:
        break
print('-----------')

# repeat用于生成n个元素重复的迭代器
for e in it.repeat('Python', 3):
    print(e)