def get_math_func(type):
    result = 1
    # 该函数返回的是lambda表达式
    if type == "square":
        return lambda n: n * n
    elif type == "cube":
        return lambda n: n * n * n
    else:
        return lambda n: (1 + n) * n/2