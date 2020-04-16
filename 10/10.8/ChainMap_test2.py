from collections import ChainMap
import builtins
my_name = '孙悟空'

def test1():
    my_name = 'yeeku'
    # 将locals,globals,builtins的变量变成ChainMap
    pylookup = ChainMap(locals(), globals(), vars(builtins))
    # 访问my_name对应的value,优先使用局部范围的定义
    print(pylookup['my_name']) # 'yeeku'
    # 访问len对应的value, 由于在局部范围,全局范围中都找不到,因此访问内置的len函数
    print(pylookup['len'])

test1()