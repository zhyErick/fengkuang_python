class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    # 定义析构函数
    def __del__(self):
        print('del删除对象')


# 创建一个item对象,将之赋值给im变量
im = Item('鼠标', 29.8)
x = im
# 打印im应用的item对象
del(im)
print('----------------------')