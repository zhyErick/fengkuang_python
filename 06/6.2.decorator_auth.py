def auth(fn):
    def auth_fn(*args):
        # 用一条语句模拟执行权限检查
        print("----模拟执行文件检查----")
        # 回调被修饰的目标函数
        fn(*args)
    return auth_fn

@auth
def test(a,b):
    print("执行test函数,参数a: %s, 参数b: %s" % (a, b))
# 调用test()函数,其实是调用修饰后返回的auth_fn函数
test(20, 15)
