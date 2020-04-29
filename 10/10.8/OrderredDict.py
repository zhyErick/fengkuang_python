from collections import OrderedDict
# 创建OrderedDict对象
dx = OrderedDict(b=5, c=2, a=7)
print(dx)
d = OrderedDict()
# 向OrderedDict中添加key-value对
d['Python'] = 89
d['Swift'] = 92
d['Kotlin'] =97
d['Go'] = 87
#  遍历OrdereDict的key-value对
for k,v in d.items():
    print(k,v)


