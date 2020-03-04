class User:
    def walk(self):
        print(self, "正在慢慢的走")

# 通过类调用实例方法
a = "aa"
User.walk(a)
u = User()
User.walk(u)