class BaseClass:
    def foo(self):
        print('父类中定义的foo方法')

class SubClass(BaseClass):
    def foo(self):
        print('子类重写父类中的foo方法')
    
    def bar(self):
        print('执行bar方法')
        # 直接执行foo方法，将会调用子类重写之后的foo()方法
        self.foo()
        # 使用类名调用实例方法(未绑定)调用父类被重写的方法
        BaseClass.foo(self)

sc = SubClass()
sc.bar()