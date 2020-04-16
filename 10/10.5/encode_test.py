import json
# 将python对象转换为json字符串(元组会被当成数组)
s = json.dumps(['yeeku', {'favorite':('coding', None, 'game', 35)}])
print(s, type(s))

# 将简单的python字符串转换为json字符串
s2 = json.dumps("\"foor\bar")
print(s2)

s3 = json.dumps('\\')
print(s3)

# 将python的dict对象转换为json字符串,并对key进行排序
s4 = json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)
print(s4)

# 将python的列表转换为json字符串,并指定json分隔符: 在逗号和冒号之间没有空格(默认有空格)
s5 = json.dumps([1, 2, 3, {'x': 5, 'y': 7}], separators=(',',':'))
print(s5)

# 指定indent为4, 意味着转换的json字符串有缩进
s6 = json.dumps({'python': 5, 'kotlin': 7}, sort_keys=True, indent=4)
print(s6)

# 使用JSONENCODER的encode方法将python对象转换为json字符串
s7 = json.JSONEncoder().encode({"name": ("孙悟空", "齐天大圣")})
print(s7)

# 使用dump()函数将转换得到的json字符串输出到文件中
f = open('a.json', 'w')
json.dump(['Kotlin', {'python': 'excellent'}], f)