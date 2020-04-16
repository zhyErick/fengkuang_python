from collections import Counter
# 创建Counter对象
c = Counter(Python=4, Swift=2, Kotlin=3, Go=-2)
# 统计Counter中所有元素出现次数之和
print(sum(c.values()))

# 将Counter转换为list,只保留各key
print(list(c))
# 将Cou转换为set,只保留各key
print(set(c))
# 将Counter转换为dict
print(dict(c))
# 将Counter都转换为list,元素都是(元素,次数)组
list_of_pairs=c.items()
print(list_of_pairs)
# 将列表元素为(元素,次数)组的list转换为Counter
c2 = Counter(dict(list_of_pairs))
print(c2)

# 获取Counter中最少出现的三个元素
print(c.most_common()[-4:-1])

# 清空所有key-value对
c.clear()
print(c)

c = Counter(a=3, b=1, c=-1)
d = Counter(a=1, b=-2, d=3)

# 对Counter执行加法
print(c + d)
# 对Counter行减法
print(c - d)
Counter({'a': 2})
# 对Counter执行交运算
print(c & d)
print(c | d)
print(+c)
print(-c)
print(-d)