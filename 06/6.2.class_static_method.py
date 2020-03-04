class Bird:
    # 使用@classmethod修饰的方法是类方法
    @classmethod
    def fly(cls):
        print('类方法fly: ', cls)
    # 使用@staticmethod修饰的方法是静态方法
    @staticmethod
    def info(p):
        print('静态方法info: ', p)

# 调用类方法,Bird类会自动绑定到第一个参数
Bird.fly()
# 调用静态方法,不会自动绑定,因此必须手动绑定第一个参数
Bird.info('crazyit')
# 创建Bird对象
b = Bird()
# 使用对象调用fly()类方法,其实依然还是使用类调用的
# 因此第一个参数依然会自动绑定到Bird类
b.fly()
# 使用对象调用info()静态方法,其实依然还是使用类调用的
# 因此程序必须为第一个参数执行绑定
b.info('fkit')