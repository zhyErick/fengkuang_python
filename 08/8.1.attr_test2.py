class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 重写__setattr()方法对设置的属性进行检查
    def __setattr__(self, name, value):
        if name == 'name':
            if 2 < len(value) <= 8 or len(value) > 8:
                self.__dict__['name'] = value
            else:
                raise ValueError('name的长度必须在2-8之间')
        elif name == 'age':
            if 10 < value < 60:
                self.__dict__['age'] = value
            else:
                raise ValueError('age值必须在10-60之间')


u = User('fkit', 24)
print(u.name)
print(u.age)
u.name = 'fk'
# u.age = 2