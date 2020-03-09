def main():
    try:
        # 使用try...except来捕获异常
        # 此时即使程序出现异常,也不会传播给main函数
        mtd(3)
    except Exception as e:
        print('程序出现异常:', e)
    # 不使用try...except捕获异常,异常会传播出来导致程序终止
    mtd(3)

def mtd(a):
    if a > 0:
        raise ValueError("a 的值大于0,不符合要求")

main()