# 创建一个空的bytes
b1 = bytes()
# 创建一个空的bytes
b2 = b''
# 通过b前缀指定hello是bytes类型的值
b3 = b'hello'
print(b3)
print(b3[0])
print(b3[2:4])

# 调用bytes方法将字符串转换成bytes对象
b4 = bytes('我爱python变成', encoding='utf-8')
print(b4)

# 利用字符串的encode()方法编码成bytes，默认使用UTF-8字符集
b5 = "学习python很有趣".encode('utf-8')
print(b5)

st = b5.decode('utf-8')
print(st)