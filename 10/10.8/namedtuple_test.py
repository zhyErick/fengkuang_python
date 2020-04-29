from collections import namedtuple
# 定义命名元组: Point
Point = namedtuple('Point', ['x', 'y'])
# 初始化Point对象,即可用位置参数,也可用命名参数
p = Point(11, y=22)
# 像普通元素一样根据索引访问元素
print(p[0] + p[1])
# 执行元素解包,按元素位置解包
a, b = p
print(a, b)
# 根据字段名访问各元素
print(p.x + p.y)
print(p)
my_data = ['East', 'North']
# 创建命名元组
p2 = Point._make(my_data)
print(p2)
# 将命名元组对象转换成OrderDict
print(p2._asdict())
# 替换命名元组对象的字段值
p2._replace(y='South')
print(p2)
# 输出p2包含所有字段
print(p2._fields)
# 定义一个命名元组类
Color = namedtuple('Color', 'red green blue')
# 再定义一个命名元素类,其字段由Point的字段加上Color的字段组成
Pixel = namedtuple('Pixel', Point._fields + Color._fields)
# 创建Pixel对象,分别x,y,red,green,blue字段值
pix = Pixel(11, 22, 128, 255, 0)
print(pix)