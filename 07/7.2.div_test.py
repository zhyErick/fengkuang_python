import sys
try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = a / b
except IndexError:
    print("索引错误:运行程序时输入的参数个数不够")
except ValueError:
    print("数值错误:程序只能接收整数参数")
except ArithmeticError:
    print("算术错误")
except Exception:
    print("未知异常")