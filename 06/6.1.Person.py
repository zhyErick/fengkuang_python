class Person:
    '这是学习Python定义的一个Person类'
    # 下面定义了一个类变量
    hair = 'black'
    def __init__(self, name = 'Charlie', age = 8):
        # 下面为Person对象增加两个实例变量
        self.name = name
        self.age = age
    # 下面定义了一个say方法
    def say(self, content):
        print(content)


# 调用Person类的构造方法,返回一个Person对象
# 将该Person对象赋值给p变量
p = Person()
# 输出p的name,age实例变量
print(p.name, p.age)    # Charlie 8
# 输出p的name实例变量,直接为该实例变量赋值
p.name = '李刚'
# 访问p的say()方法,在声明say()方法时定义了两个形参
# 但第一个形参(self)是自动绑定的,因此调用该方法只需为第二个形参指定一个值
p.say('Python语言很简单,学习很容易!')
# 再次输出p的name,age实例变量
print(p.name, p.age)    # 李刚 8

# 为p对象增加一个skills实例变量
p.skills = ['programing', 'swimming']
print(p.skills)
# 删除p对象的name实例变量
del p.name
# 再次访问p的name实例变量
#print(p.name)   # AttributeError

# 先定义一个函数
def info(self):
    print("---info函数---", self)

# 试用info对p的foo方法赋值(动态增加方法)
p.foo = info
# python不会自动将调用者绑定到第一个参数
# 因此程序需要手动将调用者绑定到第一个参数
p.foo(p)

# 试用lambda表达式对p对象的bar方法赋值(动态增加方法)
p.bar = lambda self: print('---lambda表达式---', self)
p.bar(p)

def intro_func(self, content):
    print("我是一个人%s,信息为:%s" % (self,content))

# 导入MethodType
from types import MethodType
# 试用MethodType对info_func进行包装,将该函数第一个参数绑定p
p.intro = MethodType(intro_func, p)
# 第一个参数已经绑定,无需传入
p.intro("生活在别处")