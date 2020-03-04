class Item:
    def info(self):
        print("Item中的方法：", '这是一个商品')

class Product:
    def info(self):
        print("Product 中方法：", '这是一个工业产品')

# class Mouse(Item, Product):
#     pass
class Mouse(Product, Item):
    pass

m = Mouse()
m.info()