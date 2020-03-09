class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info():
        pass


#创建一个item对象,将之赋值给im变量
im = Item('鼠标', 29.8)
print(im.__dir__())
print(dir(im))
print(im.__dict__['name'])
im.__dict__['name'] = '键盘'
im.__dict__['price'] = 32.8
print(im.name)