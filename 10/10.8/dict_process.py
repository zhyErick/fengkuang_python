s = [('Python', 1), ('Swift', 2), ('Python', 3), ('Swift', 4), ('Python', 9)]
d = {}
for k, v in s:
    # setdefault()方法用于获取指定key对应的value
    # 如果改key不存在, 则先将key对应的value设置为默认值:[]
    d.setdefault(k, []).append(v)

print(list(d.items()))