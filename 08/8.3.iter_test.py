# 定义一个代表斐波那契数列的迭代器
class Fibs:
    def __init__(self,len):
        self.first = 0
        self.sec = 1
        self.__len = len
    # 定义迭代器所需的__next__方法
    def __next__(self):
        # 如果__len__属性为0，结束迭代
        if self.__len == 0:
            raise StopIteration
        # 完成数列计算
        self.first, self.sec = self.sec, self.first + self.sec
        self.__len -= 1
        return self.first
    # 定义__iter__方法，该方法返回迭代器
    def __iter__(self):
        return self


# 创建Fibs对象
fibs = Fibs(10)
# 获取迭代器的下一个元素
print(next(fibs))
# 使用for 循环遍历迭代器
for el in fibs:
    print(el, end=' ')
#将列表转换为迭代器
my_iter = iter([2, 'fkit', 4])
print(my_iter.__next__())
print(my_iter.__next__())

