from collections import OrderedDict
# 创建普通的dict对象
my_data = {'Python': 20, 'Swift':32, 'Kotlin': 43, 'Go': 25}
# 创建基于key排序的OrdedDict
d1 = OrderedDict(sorted(my_data.items(), key=lambda t: t[0]))
# 创建基于value排序的OrderedDict
d2 = OrderedDict(sorted(my_data.items(), key=lambda t: t[1]))
print(d1)
print(my_data.items())
print(d1 == d2)