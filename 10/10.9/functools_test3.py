from functools import *
# 设初始值(默认为0)为x, 当前序列元素为y, 将x+y作为下一次计算的初始值
print(reduce(lambda x, y: x+y, range(5)))
print(reduce(lambda x, y: x+y, range(6)))
# 设置初始值10
print(reduce(lambda x, y: x+y, range(6), 10))
print('\n---------')
class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'User[name=%s]' % self.name
# 定义一个老式大小比较函数,User的name越长,该User越大
def old_cmp(u1, u2):
    return len(u1.name) - len(u2.name)
my_data = [User('Kotlin'), User('Swift'), User('Go'), User('Java')]
# 对my_data排序,需要关键函数(调用cmp_to_key将old_cmp)转换为关键字函数
my_data.sort(key=cmp_to_key(old_cmp))
print(my_data)
print('------------------')