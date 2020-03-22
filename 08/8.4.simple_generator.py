def test(val, step):
    print("---------函数开始执行----------")
    cur = 0
    # 遍历 0 - val
    for i in range(val):
        # cur 添加i * step
        cur += i * step
        yield cur

# 执行函数, 返回生成器
t = test(10 ,2)
print('================')
# 获取生成器的第一个值
print(next(t))
print(next(t))

for ele in t:
    print(ele, end=' ')

t = test(10, 1)
# 将生成器转换成列表
print(list(t))
# 再次创建生成器
t = test(10, 3)
# 将生成器转换成元组
print(tuple(t))