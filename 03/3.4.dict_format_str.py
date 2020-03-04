# 在字符串模板中使用key
temp = '书名: %(name)s, 价格是;%(price)010.2f, 出版社是:%(publish)s'
book = {'name': '疯狂python讲义', 'price': 88.9, 'publish': '电子社'}

# 使用字典为字符串模板中的key传入值
print(temp % book)
book = {'name': '疯狂kotlin讲义', 'price': 78.9, 'publish': '电子社'}

print(temp % book)