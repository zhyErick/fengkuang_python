class User:
    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd
    def validLogin(self):
        print('验证%s的登录' % self.name)


u = User('crazyit', 'leegang')
# 判断u.name是否包含__call__方法,及判断它是否可调用
print(hasattr(u.name, '__call__'))
print(hasattr(u.passwd, '__call__'))
print(hasattr(u.validLogin, '__call__'))