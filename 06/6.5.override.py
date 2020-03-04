class Bird:
    # Bird 类的fly()方法
    def fly(self):
        print("我在天空里自由自在的飞翔。。。")

class Ostrich(Bird):
    # 重写Bird类的fly()方法
    def fly(self):
        print("我只能再地上奔跑")

# 创建Ostrich对象
os = Ostrich()
# 执行Ostrich对象的fly()方法
os.fly()