from functools import *
@singledispatch
def test(arg, verbose):
    if verbose:
        print("默认参数:", end=" ")
    print(arg)
# 限制test函数的第一个int类型的函数版本
@test.register(int)
def _(argu, verbose):
    if verbose:
        print("整形参数为: ", end=" ")
    print(argu)
test('python', True)
# 调用第一个参数为int类型的版本
test(20, True)
# 限制test函数的第一个参数为list参数的函数版本
@test.register(list)
def _(argb, verbose=False):
    if verbose:
        print("列表中所有元素为:")
    for i, elem in enumerate(argb):
        print(i, elem, end=" ")
test([20, 10, 16, 30, 14], True)
print("\n-------------")
# 定义一个函数,不使用函数装饰器修饰
def nothing(arg, verbose=False):
    print("~~None参数~~")
# 当test函数第一个参数为None类型时,转向调用nothing函数
test.register(type(None), nothing)
test(None, True)
print("\n-------------")

from decimal import Decimal
# 限制test函数第一个参数为float或Decimal类型的函数版本
@test.register(float)
@test.register(Decimal)
def test_num(arg, verbose=False):
    if verbose:
        print("参数的一半为:", end=" ")
    print(arg / 2)

# 通过test.dispatch(类型)即可获取它转向的函数
print(test_num is test.dispatch(float))
print(test_num is test.dispatch(Decimal))
print(test_num is test)