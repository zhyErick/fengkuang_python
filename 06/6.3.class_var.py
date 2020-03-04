class Address:
    detail = '广州'
    post_code = '510660'
    def info(self):
        # 尝试直接访问类变量
        # print(detail)  # 报错
        # 通过类来访问变量
        print(Address.detail)
        print(Address.post_code)
# 通过类来访问Address类的变量
print(Address.detail)   # 输出 广州
addr = Address()
addr.info()
# 修改Address类变量
Address.detail = '佛山'
Address.post_code = '460110'
addr.info()