from collections import Counter
# 创建空的Counter对象
cl = Counter()
# 以可迭代的对象创建Counter对象
c2 = Counter('hannah')
print(c2)
# 以可迭代对象创建Counter对象
c3 = Counter(['Python', 'Swift', 'Swift', 'Python', 'Kotlin', 'python'])
print(c3)

# 以dict来创建cournter对象
c4 = Counter({'red': 4, 'blue': 3})
print(c4)

# 使用关键字参数创建Counter
c5 = Counter(Python=4, Swift=8)
print(c5)