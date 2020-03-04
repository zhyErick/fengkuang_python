def swap(dw):
    # 下面代码实现dw的a,b两个元素的值交换
    dw['a'], dw['b'] = dw['b'], dw['a']
    print("在swap()函数里,a元素的值是", dw['a'], ";b元素的值是", dw['b'])

dw = {'a': 6, 'b': 9}
swap(dw)
print("交换结束后, a元素的是", dw['a'], ";b元素的值是", dw['b'])